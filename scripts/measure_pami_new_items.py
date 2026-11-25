"""量測：PAMI 現行價目表（data/raw/pami_alfabeta.json）有、證據包沒收的本藥代碼（只量、不改；2026-11-25 用戶第五輪決定）。

規則照原收集器（src/artxgnn/collectors/arfda.py）：代碼的 PRINCIPIO ACTIVO → DrugBank ID（同一成分字串在 data/processed/drug_mapping.csv
已有對照就沿用，含 2026-10-12 rescue；沒有就照 run_kg_prediction.py 同一支 map_fda_drugs_to_drugbank 逐成分對照），
跟證據包 tfda.drugbank_ids 有交集、代碼不在證據包 records／excluded_records 的，算漏收。不放寬。
「新代碼」＝不在 data/raw/ar_fda_drugs.json（2026-03-01 版價目表，drug_mapping 的基準）的代碼。
用法：python3 scripts/measure_pami_new_items.py [--out 檔.json]
"""
import argparse, collections, csv, glob, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def page_kind(slug):
    p = ROOT / "docs/_drugs" / f"{slug}.md"
    if not p.exists():
        return "nopage"
    fm = p.read_text(encoding="utf-8").split("---")[1]
    return "redirect" if "id_redirect" in fm else ("noindex" if re.search(r"^noindex:\s*true", fm, re.M) else "public")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out"); a = ap.parse_args()
    import pandas as pd
    from artxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
    D = ROOT / "data"
    cur = {r["alfabeta"]: r for r in json.loads((D / "raw/pami_alfabeta.json").read_text(encoding="utf-8"))}
    if not any(r.get("nombre_generico") for r in cur.values()):
        sys.exit("pami_alfabeta.json 沒有成分欄（2026-11-25 前的格式）；先跑每週排程或 license_adapter.fetch()")
    base = {str(x["numero_certificado"]) for x in json.loads((D / "raw/ar_fda_drugs.json").read_text(encoding="utf-8"))}
    by_orig = collections.defaultdict(set)
    for x in csv.DictReader(open(D / "processed/drug_mapping.csv", encoding="utf-8-sig")):
        if x["mapping_success"] == "True":
            by_orig[x["original_ingredient"].strip().lower()].add(x["drugbank_id"].upper())
    new = sorted(set(cur) - base)
    need = [cur[i] for i in new if cur[i]["nombre_generico"].strip().lower() not in by_orig]
    mapped = collections.defaultdict(set)
    if need:
        m = map_fda_drugs_to_drugbank(pd.DataFrame(need), field_mapping={"license_id": "alfabeta", "brand_name": "nombre_comercial", "ingredients": "nombre_generico"})
        for _, x in m.iterrows():
            if isinstance(x.get("drugbank_id"), str) and x["drugbank_id"]:
                mapped[str(x["license_id"])].add(x["drugbank_id"].upper())
    db = {i: by_orig.get(cur[i]["nombre_generico"].strip().lower()) or mapped.get(i, set()) for i in new}
    per, tot = [], collections.Counter()
    for bf in sorted(glob.glob(str(D / "bundles/*/drug_bundle.json"))):
        slug = Path(bf).parent.name
        t = json.loads(Path(bf).read_text(encoding="utf-8")).get("tfda") or {}
        ids = {x.upper() for x in t.get("drugbank_ids") or []}
        have = {str(r.get("license_id")) for r in (t.get("records") or []) + (t.get("excluded_records") or [])}
        hit = [i for i in new if db[i] & ids and i not in have]
        if not hit:
            continue
        kind, partial = page_kind(slug), (t.get("total_matches") or 0) > len(t.get("records") or [])
        per.append({"slug": slug, "page": kind, "partial": partial, "n": len(hit), "records": len(t.get("records") or []),
                    "total_matches": t.get("total_matches"),
                    "items": [[i, cur[i]["nombre_generico"], cur[i]["nombre_comercial"], cur[i]["presentacion"]] for i in hit]})
        tot["bundles"] += 1; tot["items"] += len(hit); tot[f"bundles_{kind}"] += 1; tot["bundles_partial" if partial else "bundles_complete"] += 1
    s = {"current": len(cur), "base": len(base), "new_codes": len(new), "new_mapped": sum(1 for v in db.values() if v),
         "new_in_some_bundle": len({i for p in per for i, *_ in p["items"]}), **tot}
    print(json.dumps(s, ensure_ascii=False))
    if a.out:
        Path(a.out).write_text(json.dumps({"summary": s, "bundles": per}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
