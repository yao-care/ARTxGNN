#!/usr/bin/env python3
"""藥物頁市場段落（「## Información de Mercado en Argentina」等，site_config.MARKET_RE）的許可證表一律由程式依證據包產生（2026-11-24，用戶決定）。

為什麼：每週許可證排程（母目錄 license_refresh_20261029.py）只改程式管得到的格子；AI 寫的自由格式許可證表
（「| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |」等，多半只列前 5 筆、
第四欄寫「No registrada en los datos locales」）跟著 PAMI 價目表過期，checker 擋頁、要人處理。
做法（照 BrTxGNN／COTxGNN 同名檔）：
- 段落裡的第一張表換成程式表，前後加「<!-- licenses:begin -->」「<!-- licenses:end -->」標記；已有標記就換掉標記之間的內容。
- 表頭「| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |」：欄位取證據包 tfda.records 原文
  （license_id＝PAMI 價目表的 ALFABETA 代碼、brand_name_zh＝nombre_comercial、dosage_form＝presentacion、license_holder＝laboratorio_titular）；
  在 PAMI 現行清單的在前（其餘照證據包原順序）；正文或查核紀錄指名「表上／表外」產品的頁，照 config/license_table_pins.json 置頂原表的號碼（2026-11-24 6 頁）。
- 列數（照 CO）：原表資料列數與 min(5, 可列筆數) 取大（最多 20）；段落裡有 AI 寫的「列了幾筆」說明句（se muestran／la lista muestra／
  los 5 principales…）時照原表列數，免得說明句跟表對不上。重排時以頁面上現有程式表的列數為準，所以每週重排列數不變。
- 狀態：在 PAMI 現行清單＝「Vigente」（本站既有寫法，.claude/license_labels/ARTxGNN.json；本站「vigente」＝在 PAMI 現行清單），
  不在（license_adapter 標 pami_not_listed／license_status cancelled）＝「Ya no figura en el listado de PAMI」（adapter 的 NOT_LISTED 原文）。
  不寫 ANMAT 註冊狀態（不在這份資料裡）。
- 表下一句程式說明（SHOW_*）：顯示幾筆、共幾筆、資料來源、不含 ANMAT 註冊狀態；證據包只收了一部分（total_matches 大於紀錄數）時寫明清單可能不完整。
- 證據包沒有任何紀錄：表換成一句 NONE_LINE。段落裡沒有表、也沒有標記的公開頁，程式區塊補在段落最後（同 CO；noindex 頁不補）。
資料來源兩種：bundle（data/bundles 的 tfda.records；每週排程 adapter 的 sync_tables、手動）與 snapshot
（snapshots/ar_licenses.json.gz 的 rows／total／partial；scripts/apply_drug_reviews.py 結尾、scripts/build_license_snapshot.py 結尾，不需要 data/）。
gate（src/artxgnn/regulatory/licenses.py 的 program_block_problems）擋「程式區塊≠快照重算結果」「市場段落有表卻不是程式區塊」。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--from-snapshot] [--dry-run] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_RX = re.compile(r"^## Informaci[oó]n de [Mm]ercado")  # 市場段落；沒有時退回 SEC_ANY（不含 known_use 頁的標題「Usos conocidos y situación de mercado」）
SEC_ANY = re.compile(r"^## (?!.*Usos conocidos).*[Mm]ercado")  # 同 site_config.MARKET_RE
HEAD = ["| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |",
        "|------|------|------|------|------|"]
VALID = "Vigente"
NOT_LISTED = "Ya no figura en el listado de PAMI"
SRC = "listado de medicamentos para entidades de PAMI"
ANMAT = "el estado del registro en ANMAT no está incluido en estos datos"
# 表下說明句（程式產生；列數＝總數時「los N productos」，較少時「N de los M productos」，證據包只收了一部分時另註明）
SHOW_ALL = "La tabla muestra los {m} productos de este medicamento en los datos ({src}); {anmat}."
SHOW_ALL1 = "La tabla muestra el único producto de este medicamento en los datos ({src}); {anmat}."
SHOW_SOME = "La tabla muestra {n} de los {m} productos de este medicamento en los datos ({src}){first}; {anmat}."
FIRST = ", primero los que siguen en el listado vigente"  # 只在有不在清單的列時加
SHOW_PART = ("La tabla muestra {n} de los {m} productos recopilados de este medicamento en los datos ({src}); los datos solo incluyen "
             "una parte de los productos y la lista puede estar incompleta; {anmat}.")
NONE_LINE = f"Este medicamento no tiene productos en el {SRC} usado en este informe."
MAX_ROWS = 20
# AI 寫的「表上列了幾筆」說明句：有這種句子時程式表照原表列數（不擴到 5 列），免得句子跟表對不上（同 CO）
DISPLAY_RX = re.compile(r"\bse (muestran|listan|incluyen|presentan)\b|\bla (tabla|lista) (muestra|incluye|lista)|\blos \d+ principales\b|"
                        r"\b(primer[oa]s|principales) \d+\b|\bfilas\b|\bno se muestra|\blistad[oa]s\b", re.I)
BEGIN, END = "<!-- licenses:begin -->", "<!-- licenses:end -->"
# 每週排程 3b 自我檢查用（license_adapter.PAGE_NOTE）：程式區塊裡表格列以外的行
NOTE_RX = (r"^(La tabla muestra (el único producto|los \d+ productos|\d+ de los \d+ productos) (recopilados )?de este medicamento en los datos \(.*|"
           + re.escape(NONE_LINE) + r"|<!-- licenses:(begin|end) -->)$")
SHOW_RX = re.compile(NOTE_RX)
SNAP = ROOT / "snapshots" / "ar_licenses.json.gz"


# PAMI 價目表的 laboratorio_titular 欄把非 ASCII 字元存成「¿」（來源檔本身如此；Cassará 存成「Cassarß」；2026-11-24 證據包 8 種寫法）：表上照實際廠商名寫回；
# 欄位寬度截斷的（「Farmac¿」＝Farmacé…）寫成縮寫點，不猜全名
LAB_FIX = {"Bag¿": "Bagó", "Temis-Lostal¿": "Temis-Lostaló", "Andr¿maco": "Andrómaco", "Dom¿nguez": "Domínguez",
           "Qu¿mica Luar": "Química Luar", "G¿minis Farmac¿": "Géminis Farmac.", "Filaxis Farmac¿": "Filaxis Farmac.",
           "Pierre Fabre M¿": "Pierre Fabre M.", "Cassarß": "Cassará", "Nutricia-Bag¿": "Nutricia-Bagó", "Bag¿-Arcor": "Bagó-Arcor"}


def _lab(x):
    x = re.sub(r"\s+", " ", str(x or "")).strip()
    return LAB_FIX.get(x, x)


def _cell(x, n):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t[:n] or "—"


def _listed(r):
    return not (r.get("pami_not_listed") or r.get("license_status") == "cancelled")


PINS = ROOT / "config" / "license_table_pins.json"


def _pins(stem):
    if not stem or not PINS.exists():
        return []
    return (json.loads(PINS.read_text(encoding="utf-8")).get("pages", {}).get(stem) or {}).get("ids") or []


def table_rows(recs, pins=()):
    """證據包紀錄 → 表格列（全部；config/license_table_pins.json 的置頂號碼在最前，其後在 PAMI 現行清單的在前，
    其餘照證據包原順序；同號多筆任一在列即在列）"""
    by, order = {}, []
    for r in recs or []:
        k = str(r.get("license_id") or "").strip()
        if not k:
            continue
        if k not in by:
            order.append(k)
            by[k] = r
        elif _listed(r) and not _listed(by[k]):
            by[k] = r
    out = []
    pin = {k: i for i, k in enumerate(pins)}
    for k in sorted(order, key=lambda k: (pin.get(k, len(pin)), not _listed(by[k]))):
        r = by[k]
        st = VALID if _listed(r) else NOT_LISTED
        out.append(f"| {k} | {_cell(r.get('brand_name_zh'), 60)} | {_cell(r.get('dosage_form'), 50)} | "
                   f"{_cell(_lab(r.get('license_holder') or r.get('manufacturer')), 40)} | {st} |")
    return out


def counts(tf, stem=None):
    """(全部列, 總數, partial)：partial 時總數＝total_matches（證據包外還有），否則＝列數"""
    recs = tf.get("records") or []
    rows = table_rows(recs, _pins(stem))
    tm = int(tf.get("total_matches") or 0)
    partial = tm > len(recs)
    return rows, (tm if partial else len(rows)), partial


def rows_of(tf, stem=None):
    """快照用：(最多 20 列可列的列, 總數, partial)"""
    rows, total, partial = counts(tf, stem)
    return rows[:MAX_ROWS], total, partial


def show_line(n, total, partial, k, mixed=False):
    f = dict(src=SRC, anmat=ANMAT)
    if partial:
        return SHOW_PART.format(n=n, m=k, **f)
    if n >= total:
        return SHOW_ALL1.format(**f) if total == 1 else SHOW_ALL.format(m=total, **f)
    return SHOW_SOME.format(n=n, m=total, first=FIRST if mixed else "", **f)


def program_block(rows, total, partial, n):
    """程式區塊內容（不含標記）：前 n 列的表＋說明句；沒有任何紀錄時是 NONE_LINE"""
    if not rows:
        return [NONE_LINE]
    n = max(1, min(n, len(rows), MAX_ROWS))
    st = [r.endswith(f"| {NOT_LISTED} |") for r in rows]
    mixed = any(st) and st == sorted(st)  # 有不在清單的列、而且確實是在清單的排在前面（置頂頁不一定）
    return HEAD + rows[:n] + ["", show_line(n, total, partial, len(rows), mixed)]


def _section(lines):
    a = next((i + 1 for i, l in enumerate(lines) if SEC_RX.match(l)), None)
    if a is None:
        a = next((i + 1 for i, l in enumerate(lines) if SEC_ANY.match(l)), None)
    if a is None:
        return None, None
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _review_mask(lines):
    """查核框（<!-- review:begin … review:end -->）內的行號：找表、判斷說明句時不算"""
    m, inside = set(), None
    for i, l in enumerate(lines):
        s = l.strip()
        if inside is None and s.startswith("<!-- review:begin "):
            inside = s.split()[2]
        if inside is not None:
            m.add(i)
            if s == f"<!-- review:end {inside} -->":
                inside = None
    return m


def _is_prog(l):
    s = l.strip()
    return bool(SHOW_RX.match(s)) or s == NONE_LINE


def block_rows(lines):
    """頁面程式區塊裡的表格資料列數（沒有區塊回 None）"""
    if BEGIN not in lines or END not in lines:
        return None
    blk = lines[lines.index(BEGIN) + 1:lines.index(END)]
    return sum(1 for l in blk if l.startswith("| ") and not l.startswith(HEAD[0]))


def process(text, rows, total, partial):
    """回傳新頁面；沒有市場段落時回傳原文"""
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None:
        return text
    mask = _review_mask(lines)
    if BEGIN in lines[a:b] and END in lines[a:b]:
        x, y = lines.index(BEGIN, a), lines.index(END, a)
        n = block_rows(lines[x:y + 1]) or min(5, len(rows))
    else:
        tb = [k for k in range(a, b) if lines[k].startswith("|") and k not in mask]
        if not tb:  # 段落裡沒有表：程式區塊（最多 5 列）補在段落最後（公開頁；noindex 頁不補，正文多半是舊的「沒有許可」說法）
            if re.search(r"^noindex:\s*true", text[:3000], re.M):
                return text
            x, y = b, b - 1
            n = min(5, len(rows))
        else:
            x = y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            r0 = max(0, (y - x + 1) - 2)
            disp = any(DISPLAY_RX.search(lines[k]) for k in range(a, b) if k not in mask and not lines[k].startswith("|")
                       and not _is_prog(lines[k]))
            n = r0 if (disp and r0) else max(r0, min(5, len(rows)))
    blk = [BEGIN, ""] + program_block(rows, total, partial, n) + ["", END]
    head = lines[:x]
    while head and not head[-1].strip():
        head.pop()
    rest = [l for l in lines[y + 1:b] if not _is_prog(l)]
    while rest and not rest[0].strip():
        rest.pop(0)
    out = head + [""] + blk + [""] + rest
    if b < len(lines) and out[-1].strip():
        out.append("")
    out += lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def _snap():
    if not SNAP.exists():  # 讀不到快照就停，不當成「沒有資料」靜默略過（交付前驗證規則）
        raise SystemExit(f"找不到 {SNAP.relative_to(ROOT)}（跑 scripts/build_license_snapshot.py）")
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {})


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}
    return None


def run(only=None, from_snapshot=False, dry=False):
    snap = _snap() if from_snapshot else None
    if not from_snapshot and not (ROOT / "data/bundles").is_dir():
        raise SystemExit("找不到 data/bundles（先還原本站 Release 的 data/，或用 --from-snapshot）")
    changed = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only and page.name not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        if from_snapshot:
            e = snap.get(page.stem)
            if not e or "rows" not in e:
                continue
            rows, total, partial = e["rows"], e["total"], e["partial"]
        else:
            tf = _bundle(page.stem)
            if tf is None:
                continue
            rows, total, partial = rows_of(tf, page.stem)
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, total, partial)
        if new != t0:
            changed.append(page.stem)
            if not dry:
                page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = run({x for x in a if not x.startswith("--")} or None, "--from-snapshot" in a, "--dry-run" in a)
    print(f"許可證表（程式區塊）：改 {len(ch)} 頁" + ("（dry-run）" if "--dry-run" in a else ""))
