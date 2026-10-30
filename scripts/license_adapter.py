"""AR（PAMI 藥品給付價目表）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

注意：AR 站的本地資料原本就是 PAMI（國家退休人員醫療機構）的給付價目表，不是 ANMAT 的許可證資料；ANMAT 沒有可程式下載的全量註冊檔
（2026-10-30 查證：VNM 開放資料只有 2018 年兩份更新檔）。用戶 2026-10-30 選「沿用現有來源排程」。
來源：datos.pami.org.ar CKAN 資料集 medicamentos-para-entidades，取最新的 CSV 資源（免金鑰；; 分隔、latin-1）。
欄位 ALFABETA（＝證據包 license_id）。只列當期在價目表的品項、沒有狀態欄：在列不改紀錄，
新清單查不到的代碼保留原狀態、列在 summary（不推定為撤銷）。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/pami_alfabeta.json"
API = "https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades"


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
    raw = _get(res[-1]["url"]).content
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    rows = csv.DictReader(io.StringIO(text), delimiter=";")
    if "ALFABETA" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    return [{"alfabeta": (x["ALFABETA"] or "").strip()} for x in rows if x.get("ALFABETA")]


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
