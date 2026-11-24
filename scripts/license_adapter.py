"""AR（PAMI 藥品給付價目表）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

注意：AR 站的本地資料原本就是 PAMI（國家退休人員醫療機構）的給付價目表，不是 ANMAT 的許可證資料；ANMAT 沒有可程式下載的全量註冊檔
（2026-10-30 查證：VNM 開放資料只有 2018 年兩份更新檔）。用戶 2026-10-30 選「沿用現有來源排程」。
來源：datos.pami.org.ar CKAN 資料集 medicamentos-para-entidades，取最新的 CSV 資源（免金鑰；; 分隔、latin-1）。
欄位 ALFABETA（＝證據包 license_id）。只列當期在價目表的品項、沒有狀態欄：在列不改紀錄，
新清單查不到的代碼保留原狀態、列在 summary（不推定為撤銷）。

2026-11-17（用戶要求確認 11-16 排程「新資料查不到」的 53 張）：ALFABETA 是 Alfabeta（Manual Farmacéutico）的品項代碼，
不是 ANMAT 的 certificado；PAMI 價目表只列當期給付的品項，代碼消失＝「ya no figura en el listado de PAMI」，不等於 ANMAT 註冊失效
（ANMAT 註冊狀態不在這份資料裡，也沒有可下載的全量註冊檔）。同一 CKAN 上的「medicamentos para afiliados」是同一份清單（同 8,734 列）
但沒有 ALFABETA 欄，不能逐號比對。做法：
- fetch() 把整份清單的代碼記成 CURRENT（少於 MIN_CURRENT 不判定）。
- preprocess：證據包裡不在 CURRENT 的代碼標 license_status＝cancelled（本站事實層「cancelled」＝不在 PAMI 現行清單）、
  pami_not_listed＝第一次發現日，status 改「Ya no figura en el listado de PAMI」（原值存 status_before_pami_not_listed）；
  又出現在清單就還原。頁面照 PAMI 的口徑寫，不寫 ANMAT 註冊失效。
- confirmed_absent(lid)：CURRENT 有資料且代碼不在裡面。
"""
import csv
import io
import re
import time

import requests

RAW_FILE = "raw/pami_alfabeta.json"
API = "https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades"
CURRENT: set = set()   # fetch() 填：最新 PAMI 價目表的 ALFABETA 代碼；空的就不做「不在清單」判定
MIN_CURRENT = 7000     # 2026-03-01 版 8,035 列、2026-11-05 版 8,734 列
NOT_LISTED = "Ya no figura en el listado de PAMI"


def _get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(20 * (attempt + 1))


def fetch():
    res = [r for r in _get(API).json()["result"]["resources"] if str(r.get("format", "")).upper() == "CSV" or str(r.get("url", "")).lower().endswith(".csv")]
    if not res:
        raise RuntimeError("資料集沒有 CSV")
    res.sort(key=lambda r: r.get("last_modified") or r.get("created") or r.get("url"))
    raw = _get(re.sub(r"^http://", "https://", res[-1]["url"])).content  # CKAN 給 http 網址；https 也可用（雲端代理只放 https）
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    rows = csv.DictReader(io.StringIO(text), delimiter=";")
    if "ALFABETA" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    out = [{"alfabeta": (x["ALFABETA"] or "").strip()} for x in rows if x.get("ALFABETA")]
    CURRENT.clear()
    if len(out) >= MIN_CURRENT:
        CURRENT.update(r["alfabeta"] for r in out)
    return out


def confirmed_absent(lid):
    """給 license_refresh：PAMI 現行價目表確認已不列這個 ALFABETA 代碼（不代表 ANMAT 註冊失效）"""
    lid = str(lid).strip()
    return bool(CURRENT) and lid.isdigit() and lid not in CURRENT


def preprocess(bundle):
    """不在 PAMI 現行清單的代碼標 cancelled＋pami_not_listed；又出現在清單就還原。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not lid.isdigit():
            continue
        if lid in CURRENT:
            if r.get("pami_not_listed"):
                r.pop("pami_not_listed", None)
                r.pop("license_status", None)
                r["status"] = r.pop("status_before_pami_not_listed", "")
                ch = True
        elif not r.get("pami_not_listed"):
            r["status_before_pami_not_listed"] = r.get("status") or ""
            r["status"] = NOT_LISTED
            r["license_status"] = "cancelled"
            r["pami_not_listed"] = today
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 3000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["alfabeta"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary


# 2026-11-24：市場段落的許可證表改成程式產生（scripts/sync_license_tables.py，用戶決定）。
# 每週排程 3b 自我檢查：程式區塊裡表格列以外的行（標記、表下說明句、沒有紀錄句）也算程式產生的行。
PAGE_NOTE = (r"^(La tabla muestra (el único producto|los \d+ productos|\d+ de los \d+ productos) (recopilados )?de este medicamento en los datos \(.*|"
             r"Este medicamento no tiene productos en el listado de medicamentos para entidades de PAMI usado en este informe\.|<!-- licenses:(begin|end) -->|## Información de Mercado en Argentina)$")


def sync_tables(site_dir, bundles):
    """程式許可證表依證據包重排（狀態有變或證據包補收的藥都跟上）；全站都跑（便宜），回傳改到的頁"""
    import importlib.util
    s = importlib.util.spec_from_file_location("ar_slt", site_dir / "scripts/sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return [(pg, "許可證表", "", "依證據包重排") for pg in m.run()]
