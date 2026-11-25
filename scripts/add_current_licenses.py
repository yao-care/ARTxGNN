"""依原收集規則補收 PAMI 現行價目表有、證據包沒收的本藥代碼（2026-11-25 第六輪，用戶決定；全程不用 AI）。

問題：證據包的 tfda 區塊是 collectors/arfda.py 收的：藥名 → DrugBank ID（tfda.drugbank_ids）→ data/processed/drug_mapping.csv 裡同一個 ID
的 ALFABETA 代碼 → data/raw/ar_fda_drugs.json（2026-03-01 版 PAMI 價目表）的那一列；最多存 20 筆（單方在前），total_matches 是全部筆數。
2026-03 之後才出現在價目表的代碼不在 drug_mapping、也不在 ar_fda_drugs.json，永遠收不進來（第五輪量測 151 包／890 筆）。

收集規則（每個證據包第一次跑時判定，記在 tfda.collection_rule）：
- 2026-10-12 rescue_mapping（母 repo .claude/rescue_mapping.py，補救失敗成分）之前收的證據包（collection_log 的 tfda queried_at 早於
  2026-10-12）照 drug_mapping.csv.bak_20261012，之後收的照現行 drug_mapping.csv；用那份對照在 ar_fda_drugs.json 重算原收集器，
  **筆數正好等於 total_matches、而且證據包現有紀錄都在裡面**才算數（另一份對照也試；兩份都重算不出就整包不補、列進報告，停損）。
- 當時算進 total_matches、因 20 筆上限沒存的代碼回填 tfda.records_not_stored（防重複計數）。

補收（只加不刪、可重複執行）：PAMI 現行價目表（data/raw/pami_alfabeta.json，license_adapter.fetch() 存的，有 PRINCIPIO ACTIVO 等欄）的每一列，
- 代碼在該份 drug_mapping 裡 → 原號碼對照（已在原收集結果裡，不會重複補）；
- 代碼不在（新代碼）→ 成分字串（PRINCIPIO ACTIVO，寫法同 ar_fda_drugs.json 的 nombre_generico）照同一份 drug_mapping 的
  「原始成分字串 → DrugBank ID」對照（見過、當時對不到的照舊對不到）；沒見過的字串用 Phase 1 的 mapping/drugbank_mapper
  （map_fda_drugs_to_drugbank 同一套：get_all_synonyms 拆成分、逐成分對照，成分各自成立）；現行對照（rescue 後）另把對不到的成分
  照 rescue_20261012 的規則補救（tools/txgnn/.claude/rescue_mapping.py，母 repo 同步來的那份；2026-11-25 第七輪前是站上複本）。
對到本藥 DrugBank ID、證據包還沒有（records、records_not_stored、excluded_records）的就補：records 未滿 20 筆存進 records（單方在前），
滿了只記代碼在 records_not_stored；兩者都算進 total_matches。每筆記 source（清單與日期、規則）與 added（補收日）。
EXCLUDE（每筆附理由）：看起來不是原規則該收的類別，不補。

用法（repo 根目錄）：python3 scripts/add_current_licenses.py [--download] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑（下載失敗不擋排程）。
"""
import csv
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as A  # noqa: E402

BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data" / A.RAW_FILE
BASE_LIST = ROOT / "data/raw/ar_fda_drugs.json"
CUR, BAK = "drug_mapping.csv", "drug_mapping.csv.bak_20261012"
MAPS = {CUR: ROOT / "data/processed" / CUR, BAK: ROOT / "data/processed" / BAK}
RESCUE_DATE = "2026-10-12"
CAP = 20
# (代碼, 理由)：照原規則對得到、但不該算本藥的（例：成分欄錯植）。2026-11-25 第一次補收逐筆看過，沒有要排除的。
EXCLUDE: dict = {}


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def skey(t):
    return str(t or "").strip().lower()


def load_map(p):
    lic, oi, ids_all = {}, {}, set()
    with open(p, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            lid = str(row.get("license_id") or "").strip()
            ids_all.add(lid)
            o = skey(row.get("original_ingredient"))
            oi.setdefault(o, set())
            db = str(row.get("drugbank_id") or "").strip().upper()
            if not db or str(row.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            oi[o].add(db)
            if lid:
                lic.setdefault(db, set()).add(lid)
    return {"lic": lic, "oi": oi, "ids": ids_all}


def load_rescue():
    """2026-10-12 rescue_mapping 的規則（tools/txgnn/.claude/rescue_mapping.py＝母 repo .claude/rescue_mapping.py，sync_site_tools.py 同步；
    2026-11-25 第七輪起改讀這份、不再放站上複本）。詞表由 RESCUE_MAPPING_VOCAB 指向本站 data/external/drugbank_vocab.csv。"""
    import importlib.util
    import os
    p = ROOT / "tools/txgnn/.claude/rescue_mapping.py"
    if not p.exists():
        raise SystemExit(f"找不到 {p.relative_to(ROOT)}，判斷不了現行對照，不補收")
    os.environ["RESCUE_MAPPING_VOCAB"] = str(ROOT / "data/external/drugbank_vocab.csv")
    saved = list(sys.path)  # 它會把 tools/txgnn/.claude 插到 sys.path 最前面，載完還原，免得遮住本站同名模組
    try:
        spec = importlib.util.spec_from_file_location("rescue_mapping", p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


class Phase1:
    """Phase 1 的成分 → DrugBank 對照（map_fda_drugs_to_drugbank 同一套）；rescue=True 時對不到的成分再照 rescue_20261012 補救"""

    def __init__(self):
        from artxgnn.mapping import drugbank_mapper as M
        from artxgnn.mapping.normalizer import get_all_synonyms
        self.M, self.syn = M, get_all_synonyms
        self.idx = M.build_name_index(M.load_drugbank_vocab())
        self.cache = {}
        self._rc = None

    def rescue(self, name):
        if self._rc is None:
            self._rc = load_rescue()
        return {self._rc.vocab[n] for n, _ in self._rc.rescue_ingredient(name)}

    def ids(self, s, rescue):
        k = (s, rescue)
        if k not in self.cache:
            out = set()
            for main, syns in self.syn(str(s)):
                db = self.M.map_ingredient_to_drugbank(main, self.idx)
                for sy in ([] if db else syns):
                    db = self.M.map_ingredient_to_drugbank(sy, self.idx)
                    if db:
                        break
                if db:
                    out.add(str(db).upper())
                elif rescue:
                    out |= {x.upper() for x in self.rescue(main or s)}
            self.cache[k] = out
        return self.cache[k]


def ncomp(s):
    return len(re.split(r"[,;+/&]|&&| and | y | e | und | et ", str(s or "x")))


def coll_date(b):
    q = [x.get("queried_at", "") for x in b.get("collection_log") or [] if x.get("source") == "tfda"]
    return (q[0] if q else (b.get("metadata") or {}).get("created_at", ""))[:10]


def text_match(drug, rows):
    """原收集器的備援（mapping 一筆都沒有時，比對成分欄）"""
    core = norm(drug)
    if len(core) < 4:
        return []
    if " " not in core and len(core) >= 6:
        pat = re.compile(rf" {re.escape(core)}[a-z]{{0,3}} ")
        return [r for r in rows if pat.search(" " + norm(r.get("nombre_generico")) + " ")]
    return [r for r in rows if f" {core} " in " " + norm(r.get("nombre_generico")) + " "]


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    today = datetime.date.today().isoformat()
    if "--download" in argv:
        cur = A.fetch()
        if len(cur) < A.MIN_CURRENT:
            raise SystemExit(f"現行清單只有 {len(cur)} 筆，疑似下載或格式有問題，不補收")
        RAW.write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    else:
        try:
            cur = json.loads(RAW.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到現行清單 {RAW}：{e}")
    if len(cur) < A.MIN_CURRENT or sum(1 for r in cur if r.get("nombre_generico")) < 0.9 * len(cur):
        raise SystemExit(f"現行清單 {len(cur)} 筆、成分欄不足，不補收（2026-11-25 前的格式沒有成分欄）")
    ldate = datetime.date.fromtimestamp(RAW.stat().st_mtime).isoformat()
    curd = {str(r["alfabeta"]).strip(): r for r in cur if r.get("alfabeta")}
    try:
        maps = {k: load_map(p) for k, p in MAPS.items() if p.exists()}
        base = {}
        for x in json.loads(BASE_LIST.read_text(encoding="utf-8")):
            base[str(x["numero_certificado"]).strip()] = base.get(str(x["numero_certificado"]).strip(), 0) + 1
    except Exception as e:
        raise SystemExit(f"讀不到對照資料：{e}")
    if CUR not in maps:
        raise SystemExit("沒有 data/processed/drug_mapping.csv，不補收")
    p1 = Phase1()
    cand = {}  # rule → db → [現行清單代碼]
    for rule, mp in maps.items():
        lic_db = {}
        for db, ls in mp["lic"].items():
            for lid in ls:
                lic_db.setdefault(lid, set()).add(db)
        by_db = {}
        for lid, r in curd.items():
            if lid in mp["ids"]:
                dbs = lic_db.get(lid, set())
            else:
                s = skey(r.get("nombre_generico"))
                dbs = mp["oi"][s] if s in mp["oi"] else (p1.ids(r.get("nombre_generico"), rule == CUR) if s else set())
            for db in dbs:
                by_db.setdefault(db, []).append(lid)
        cand[rule] = by_db
    rows, nb, nrec, nfill, gaps, nrule, nex = [], 0, 0, 0, [], 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        t = b.get("tfda")
        if not t:
            continue
        recs = list(t.get("records") or [])
        not_stored = [str(x) for x in t.get("records_not_stored") or []]
        have = {str(r.get("license_id") or "") for k in ("records", "excluded_records") for r in (t.get(k) or [])} | set(not_stored)
        total = int(t.get("total_matches") or len(recs))
        ids = {str(x).upper() for x in t.get("drugbank_ids") or []}
        rule = t.get("collection_rule")
        changed = False
        if not rule:  # 第一次：照收集日期判定規則、重算驗證、回填當時沒存的代碼
            first = BAK if coll_date(b) < RESCUE_DATE else CUR
            for rn in (first, CUR if first == BAK else BAK):
                if rn not in maps:
                    continue
                m = sorted({lid for db in ids for lid in maps[rn]["lic"].get(db, ()) if lid in base})
                if sum(base[x] for x in m) == total and {str(r.get("license_id")) for r in recs} <= set(m):
                    rule = rn
                    hid = [x for x in m if x not in have]
                    if hid:
                        not_stored += hid
                        have |= set(hid)
                        nfill += 1
                        rows.append(f"{page}\t-\t({len(hid)} 筆當時沒存的代碼)\tbackfill_not_stored\t{rn}\t")
                    break
            if not rule:
                gaps.append(page)
                rows.append(f"{page}\t-\t(兩份對照都重算不出 total_matches {total})\tskipped_rule\t\t")
                continue
            nrule += 1
            changed = True
        if total - len(recs) - len(not_stored) > 0:
            gaps.append(page)
            rows.append(f"{page}\t-\t(total_matches 比已知代碼多 {total - len(recs) - len(not_stored)} 筆)\tskipped_gap\t\t")
            continue
        if rule not in maps:
            gaps.append(page)
            rows.append(f"{page}\t-\t(沒有 {rule})\tskipped_rule\t\t")
            continue
        want = {lid for db in ids for lid in cand[rule].get(db, ())}
        if not want and total == 0:  # 原收集器：mapping 一筆都沒有才比對成分欄
            want = {str(r["alfabeta"]) for r in text_match((b.get("drug") or {}).get("inn"), list(curd.values()))}
        want -= have
        src = (f"PAMI medicamentos para entidades ({ldate}); matched by the original collector rule ({rule}"
               f"{', mapping used when this bundle was collected before the 2026-10-12 rescue' if rule == BAK else ''})")
        added = []
        for lid in sorted(want, key=lambda x: (ncomp(curd[x].get("nombre_generico")) > 1, x)):
            r = curd[lid]
            if (page, lid) in EXCLUDE or ("*", lid) in EXCLUDE:
                nex += 1
                rows.append(f"{page}\t{lid}\t{r.get('nombre_comercial', '')}\texcluded\t{r.get('nombre_generico', '')}\t{EXCLUDE.get((page, lid)) or EXCLUDE.get(('*', lid))}")
                continue
            rec = {"license_id": lid, "brand_name_zh": r.get("nombre_comercial", ""), "brand_name_en": r.get("nombre_generico", ""),
                   "ingredients": r.get("nombre_generico", ""), "indication": "", "dosage_form": r.get("presentacion", ""),
                   "manufacturer": r.get("laboratorio_titular", ""), "license_holder": r.get("laboratorio_titular", ""),
                   "approval_date": "", "expiry_date": "", "status": "", "source": src, "added": today}
            total += 1
            if len(recs) < CAP:
                recs.append(rec)
                where = "records"
            else:
                not_stored.append(lid)
                where = "not_stored"
            added.append(lid)
            rows.append(f"{page}\t{lid}\t{r.get('nombre_comercial', '')}\t{where}\t{r.get('nombre_generico', '')}\t{r.get('presentacion', '')}")
        if not added and not changed:
            continue
        nb += bool(added)
        nrec += len(added)
        t2 = dict(t, records=recs, total_matches=total, found=bool(recs), collection_rule=rule)
        if not_stored:
            t2["records_not_stored"] = not_stored
        if not dry:
            b["tfda"] = t2
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tproduct\twhere\tingredients\tpresentation\n" + "\n".join(rows) + "\n", encoding="utf-8")
    if nrule:
        print(f"記下收集規則：{nrule} 個證據包（回填 records_not_stored {nfill} 個）")
    if nex:
        print(f"排除（EXCLUDE）：{nex} 筆")
    if gaps:
        print(f"⚠ 重算不出收集規則或總數對不上、這次不補的證據包 {len(gaps)} 個：{', '.join(gaps[:20])}")
    print(f"{'（試跑）' if dry else ''}依原收集規則補收：{nb} 個證據包、{nrec} 筆（現行清單 {len(curd)} 筆，{ldate}）")


if __name__ == "__main__":
    main(sys.argv[1:])
