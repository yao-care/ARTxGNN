"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定把 KrTxGNN／MyTxGNN 的做法移植到本站；照 COTxGNN 同名檔（同為西班牙文）改成本站句型）。

正文裡「N autorizaciones vigentes」「N productos」這類 PAMI 價目表張數敘述，由程式依許可證快照（snapshots/ar_licenses.json.gz 的 facts）
改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My／CO：程式改寫的張數敘述是程式產生的正文）。
本站「vigente」＝在 PAMI 現行價目表（事實層 valid）；不在清單＝事實層 cancelled（「ya no figura en el listado de PAMI」）。

只改「句型明確、數字確定是本藥張數」的地方，其餘一律不動：
  - 句子要有許可證名詞（autorización(es)、registro(s)、licencia(s)；在市場段落（site_config.MARKET_RE）裡「N productos」也算），
    而且數字右邊緊接名詞或狀態字（vigente、ya no figura…）；沒有交互作用、試驗、文獻、劑量、年份等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（al menos、parcial、incomplet、podría）、講證據包或查詢結果（datos compilados、Evidence Pack、
    se encontraron）、相對數（otros、más、además de、restantes、adicionales）、劑型或廠商子集（comprimidos、cápsulas、inyectable、
    colirio、laboratorio、fabricante、titular…）；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（se muestran／la lista muestra／la tabla／listadas／principales、「N de M」的 N）、文字數詞（cinco、ambas…，不比對）。
角色看數字右側：ya no figura(n)／cancelad／dad(o)s de baja→不在清單；vigente(s)／siguen en el listado→在清單；
de un solo principio activo／monofármaco→單方；en combinación→複方；其餘→總數。
單方／複方：本站事實層的 single_total 原本沒有拆「+」複方（diosmina+hesperidina 也算單方）；2026-11-24 起 reviewer 依「+」切分
（src/artxgnn/regulatory/ingredients.py），單方／複方數字仍只驗不改：不等於事實層讀法就列 single-combo 待查；句中另有單方／複方說法而其他張數要改時，也整句列 single-combo。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的在清單／不在清單數字時，沒有限定詞的數字確定是總數。
數字已等於該角色的任一合理讀法就不動；不等於時各讀法相同才改，不同就列 ambiguous。
不改、列待查：文字數詞跟事實不符（word-numeral）、同一行另有 las otras dos／los demás 之類的相對說法（relative）、原數字是 0（zero-premise）、要改成 0（zero-new）、改寫要跨過 1（plural：單複數要跟著變）；
前提檢查：說「todas vigentes／ninguna cancelada」而事實有不在清單的、說全部單方或全部複方而事實不符時整句不動（premise）。
"""
from __future__ import annotations

import re

from .site_config import C

MARKET_SEC = re.compile(r"^## .*(?:" + C["MARKET_RE"] + ")")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡*\[(>-])")
NUM = re.compile(r"(?<![\w.,/-])(\d{1,3}(?:\.\d{3})+|\d+)(?![\w.,/%-]|[.,]\d)")
NOUN = r"(?:autorizaci(?:ón|ones|on)|registros?|licencias?|productos?|presentaciones?)"
LICENSE = re.compile(r"\bautorizaci(ón|ones|on)\b|\blicencias?\b|\bPAMI\b|"
                     r"\d+\s+registros?\b(?!\s+de\s+(ensayos?|estudios?|pacientes?|casos?))", re.I)
MKT_NOUN = re.compile(r"\d+\s+(registros?|productos?|presentaciones?)\b", re.I)
NOT_LICENSE = re.compile(r"interacci|ensayo|estudio|art[ií]culo|PMID|NCT|pacientes?|casos?\b|efectos? adversos?|\bmg\b|\bml\b|\bmcg\b|%|"
                         r"\baños?\b|\bmeses\b|semanas?|d[ií]as?\b|candidat|predicci|predich|puntuaci|score|rank|farmacolog|blancos?\b|"
                         r"receptor|DrugBank|ChEMBL|PubMed|ClinicalTrials|publicaci|DDInter", re.I)
HEDGED = re.compile(r"al menos|como m[ií]nimo|parcial|incomplet|puede haber m[aá]s|pueden existir|podr[ií]a|posiblemente|datos compilados|compilad|"
                    r"Evidence Pack|paquete de evidencia|consulta|devolvi|se (encontraron|identificaron)|identificad|"
                    r"\botr[oa]s\b|\bm[aá]s\b|adem[aá]s de|restantes?|adicional|resto|incluid|entre ellos|tambi[eé]n hay|"
                    r"veterinari|exportaci|laboratori|\bS\.?A\.?\b|pertenec|fabricant|titular|"
                    r"comprimid|\bcomp\.|tableta|c[aá]psula|grageas?|inyectable|ampolla|frasco|vial|soluci[oó]n|crema|jarabe|suspensi[oó]n|"
                    r"oft[aá]lmic|colirio|t[oó]pic|\boral\b|\bgel\b|ung[uü]ento|pomada|polvo|parche|aerosol|inhalad|gotas|[oó]vulo|vaginal|"
                    r"supositori|forma farmac|presentaci[oó]n de|\b\d+\s*x\b|\(\s*\d+\s+de\s", re.I)
DISPLAY = re.compile(r"(se muestran?|se listan?|la (tabla|lista)|listad[oa]s|anteriores|siguientes|arriba|abajo|mostrad[oa]s|principales)", re.I)
SINGLE_WORDS = re.compile(r"un solo principio activo|[uú]nico principio activo|principio activo [uú]nico|monocomponente|monof[aá]rmaco|monodroga|"
                          r"producto [uú]nico|ingrediente [uú]nico|combinaci[oó]n|combinad[oa]s|asociaci[oó]n", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
VIG = r"(?:vigentes?|en vigor|v[aá]lid[oa]s?|(?:siguen|sigue|figuran|figura|est[aá]n?)\s+en el listado|en el listado (?:vigente|de PAMI|de medicamentos))"
CANC = (r"(?:ya no figuran?|no figuran? (?:ya )?en el listado|cancelad[oa]s?|revocad[oa]s?|anulad[oa]s?|dad[oa]s? de baja|"
        r"fuera del listado|retirad[oa]s? del listado)")


# 文字數詞（dos～veinte、ambos／ambas；不含 un／una，避免冠詞誤中）：不改，跟事實不符時整行不動、列 word-numeral 待查
NUMW = {"dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
        "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
        "ambos": 2, "ambas": 2}
WNUM = re.compile(r"\b(" + "|".join(sorted(NUMW, key=len, reverse=True)) + r")\b(?=\s+(?:\w+\s+)?" + NOUN + r")", re.I)
# 同一行另有「las otras dos」「los demás」「Todas corresponden a…」這類相對或全稱說法：張數改了這些說法就對不上，整行不動
RELATIVE = re.compile(r"\b(l[oa]s )?(otr[oa]s|dem[aá]s|restantes)\b|\b(tod[oa]s|ambos|ambas)\b", re.I)


def _role(s, a, b):
    left, right = s[max(0, a - 30):a].lower(), s[b:b + 60].lower()
    if re.match(r"\s*de\s+(los\s+|las\s+)?\d", right):
        return "display"
    # 「N de M」「las N principales de M」的 M 是總數（或在清單數），不是顯示筆數：照右側判斷
    if DISPLAY.search(left) and not re.search(r"\bde\s+(los\s+|las\s+)?$", left):
        return "display"
    if DISPLAY.search(right[:30]) and not re.match(rf"\s*{NOUN}", right):
        return "display"
    near = right[:60]
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:est[aá]n\s+|son\s+)?{CANC}", near):
        return "cancelled"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,3}}(?:de\s+)?(?:un solo principio activo|un [uú]nico principio activo|monocomponentes?|"
                r"monof[aá]rmacos?|monodrogas?|ingrediente [uú]nico|principio activo [uú]nico|[uú]nico principio activo|producto [uú]nico)", near):
        return "single"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:son\s+|en\s+|de\s+)?(?:combinaci[oó]n|combinad[oa]s|asociaci[oó]n)", near):
        return "combo"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:locales\s+|de PAMI\s+)?(?:est[aá]n\s+|figuran\s+como\s+|siguen\s+)?(?:actualmente\s+)?{VIG}", near):
        return "valid"
    if re.match(rf"\s*{NOUN}\b", right):
        return "total"
    return None


def _readings(role, f, sent, explicit=False):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    st, vs = f.get("single_total"), f.get("valid_single")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "single":  # 只驗不改（事實層單方沒拆「+」複方）
        return {st, vs}, None
    if role == "combo":
        ct = None if t is None or st is None else t - st
        cv = None if v is None or vs is None else v - vs
        return {ct, cv}, None
    if explicit:  # 同一句另有明確的在清單／不在清單數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v}, t if t == v else None


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}\b(vigentes?|en el listado)\b|ning[uú]n[oa]? (\w+ ){0,3}(est[aá] )?(cancelad|revocad|dad[oa] de baja)|"
                 r"sin (\w+ ){0,2}(cancelad|cancelaciones|bajas)", lo) and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(un solo principio activo|un [uú]nico principio activo|monof[aá]rmaco|producto [uú]nico)", lo):
        return False  # 單方張數只驗不改
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(combinaci[oó]n|combinad)", lo):
        return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not (NUM.search(sent) or WNUM.search(sent)) or not (LICENSE.search(sent) or (market and (MKT_NOUN.search(sent) or WNUM.search(sent)))):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    if not any(r not in (None, "display") for _, r in found) and not WNUM.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    for m in WNUM.finditer(sent):
        role = _role(sent, m.start(), m.end())
        if role in ("valid", "cancelled", "total"):
            ok, _ = _readings(role, f, sent, False)
            if NUMW[m.group(1).lower()] not in ok:
                return sent, "word-numeral"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs = []
    for m, role in found:
        if role in (None, "display"):
            continue
        old = int(m.group(1).replace(".", ""))
        ok, v = _readings(role, f, sent, explicit)
        if old in ok:
            continue
        if role in ("single", "combo"):
            return sent, "single-combo"
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-new"
        if (old == 1) != (v == 1):
            return sent, "plural"
        subs.append((m, v))
    if not subs:
        return sent, None
    if SINGLE_WORDS.search(sent):  # 句中另說單方／複方：張數改了，單方說法無從驗證（事實層沒拆「+」複方），整句不動
        return sent, "single-combo"
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}".replace(",", ".") if v >= 1000 else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    if new != parts and RELATIVE.search(ln):  # 改了張數、同一行另有相對說法（las otras dos…）：整行不動
        skipped.append(("relative", ln.strip()))
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            market = bool(MARKET_SEC.match(ln))
        lines.append(ln if "\x00" in ln else _line(ln, facts, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
