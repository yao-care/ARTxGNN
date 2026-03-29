#!/usr/bin/env python3
"""處理阿根廷 ANMAT 藥品資料

從 PAMI 開放資料平台下載藥品價格清單 CSV 並轉換為 JSON 格式。
PAMI 清單包含完整的阿根廷市售藥品資料（8,000+ 筆、960+ 種活性成分）。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    主要: PAMI 開放資料 - 藥品價格清單（完整藥品資料庫）
          https://datos.pami.org.ar/dataset/medicamentos-para-entidades
    備用: datos.salud.gob.ar CKAN API - VNM（僅 2018 年更新，約 60 筆）
          https://datos.salud.gob.ar/dataset/vademecun-nacional-de-medicamentos-vnm

產生檔案:
    data/raw/ar_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_anmat_data(output_path: Path) -> Path:
    """下載阿根廷藥品資料

    優先從 PAMI 開放資料平台下載完整藥品價格清單 CSV（8,000+ 筆）。
    備用: datos.salud.gob.ar CKAN API（僅 2018 年更新，約 60 筆）。

    Args:
        output_path: CSV 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    ds = config["data_source"]

    print("正在下載阿根廷藥品資料...")
    print()

    # ── 方法 1: PAMI 開放資料（完整藥品清單）──
    pami_urls = ds.get("pami_download_urls", [
        # CSV 格式（分號分隔，latin-1 編碼）
        "http://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20260302_092932.csv",
        # XLSX 格式（備用）
        "http://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/e72a9026-a971-46c1-b828-2638b2b2be37/download/gavade_20260302_092932.xlsx",
    ])

    for url in pami_urls:
        try:
            print(f"嘗試從 PAMI 下載: {url}")
            response = requests.get(url, timeout=180, verify=False)
            response.raise_for_status()

            # 確認回傳非 HTML
            content_type = response.headers.get("Content-Type", "")
            if "text/html" in content_type and len(response.content) < 10000:
                print(f"  跳過: 回傳 HTML 而非資料檔")
                continue

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)

            size_kb = output_path.stat().st_size / 1024
            print(f"  下載完成: {output_path}")
            print(f"  檔案大小: {size_kb:.1f} KB")
            return output_path

        except requests.RequestException as e:
            print(f"  PAMI 下載失敗: {e}")
            continue

    # ── 方法 2: CKAN API (datos.salud.gob.ar) ──
    ckan_urls = ds.get("ckan_api_urls", [])
    dataset_id = ds.get("dataset_id", "vademecun-nacional-de-medicamentos-vnm")

    for base_url in ckan_urls:
        api_url = f"{base_url}/api/3/action/package_show?id={dataset_id}"
        print(f"查詢 CKAN API: {api_url}")

        try:
            response = requests.get(api_url, timeout=60, verify=False)
            response.raise_for_status()
            result = response.json()

            if not result.get("success"):
                print(f"  API 回傳失敗狀態")
                continue

            resources = result.get("result", {}).get("resources", [])

            csv_resources = [
                r for r in resources
                if r.get("format", "").upper() == "CSV"
            ]

            if not csv_resources:
                print(f"  未找到 CSV 資源")
                continue

            resource = csv_resources[-1]
            csv_url = resource.get("url", "")
            resource_name = resource.get("name", "unknown")

            print(f"  找到 CSV 資源: {resource_name}")
            print(f"  下載 URL: {csv_url}")

            csv_response = requests.get(csv_url, timeout=180, verify=False)
            csv_response.raise_for_status()

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(csv_response.content)

            size_kb = output_path.stat().st_size / 1024
            print(f"  下載完成: {output_path}")
            print(f"  檔案大小: {size_kb:.1f} KB")
            return output_path

        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"  CKAN API 失敗: {e}")
            continue

    # ── 方法 3: 直接下載已知 URL ──
    direct_urls = ds.get("direct_download_urls", [])
    for url in direct_urls:
        try:
            print(f"嘗試直接下載: {url}")
            response = requests.get(url, timeout=180, verify=False)
            response.raise_for_status()

            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)

            print(f"  下載完成: {output_path}")
            return output_path
        except requests.RequestException as e:
            print(f"  失敗: {e}")
            continue

    # ── 方法 4: 回報手動下載指引 ──
    raise FileNotFoundError(
        f"自動下載阿根廷藥品資料失敗\n\n"
        f"方法 A: PAMI 開放資料（推薦，完整清單 8,000+ 筆）\n"
        f"  1. 前往 https://datos.pami.org.ar/dataset/medicamentos-para-entidades\n"
        f"  2. 下載 CSV 檔案\n"
        f"  3. 將 CSV 放置於: {output_path}\n\n"
        f"方法 B: datos.salud.gob.ar（僅 2018 更新，約 60 筆）\n"
        f"  1. 前往 https://datos.salud.gob.ar/dataset?groups=vademecum-y-medicamentos\n"
        f"  2. 下載 VNM 的 CSV 檔案\n"
        f"  3. 將 CSV 放置於: {output_path}\n\n"
        f"支援格式: CSV（分號或逗號分隔）"
    )


def process_anmat_csv(csv_path: Path, output_path: Path) -> Path:
    """處理阿根廷藥品 CSV 並轉換為 JSON

    支援兩種格式:
    1. PAMI 藥品價格清單 (分號分隔, 8,000+ 筆):
       ALFABETA;PRINCIPIO ACTIVO;MARCA COMERCIAL;PRESENTACION;LABORATORIO;...
    2. datos.salud.gob.ar VNM (逗號分隔, ~60 筆):
       laboratorio_titular,numero_certificado,nombre_comercial,...

    Args:
        csv_path: CSV 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()
    encoding = config.get("encoding", "utf-8")

    print(f"讀取 CSV 檔案: {csv_path}")

    # ── 自動偵測 CSV 格式（分號 vs 逗號分隔）──
    df = None

    # 嘗試分號分隔（PAMI 格式）
    for enc in ["latin-1", "cp1252", "utf-8-sig", "utf-8"]:
        try:
            df_test = pd.read_csv(
                csv_path, encoding=enc, dtype=str, sep=";", on_bad_lines="skip",
            )
            if len(df_test.columns) > 2 and len(df_test) > 100:
                df = df_test
                print(f"  偵測到 PAMI 格式 (分號分隔, 編碼={enc})")
                break
        except (UnicodeDecodeError, pd.errors.EmptyDataError):
            continue

    # 如果分號分隔失敗，嘗試逗號分隔（VNM 格式）
    if df is None:
        for enc in [encoding, "utf-8-sig", "latin-1", "cp1252"]:
            try:
                df_test = pd.read_csv(
                    csv_path, encoding=enc, dtype=str, on_bad_lines="skip",
                )
                if len(df_test.columns) > 1:
                    df = df_test
                    print(f"  偵測到 VNM 格式 (逗號分隔, 編碼={enc})")
                    break
            except (UnicodeDecodeError, pd.errors.EmptyDataError):
                continue

    if df is None:
        df = pd.read_csv(csv_path, encoding="latin-1", dtype=str, on_bad_lines="skip")

    print(f"原始資料筆數: {len(df)}")
    print(f"欄位: {', '.join(df.columns.tolist())}")

    # ── 標準化欄位名稱 ──
    # PAMI 格式欄位（可能帶尾隨空格）
    df.columns = [c.strip() for c in df.columns]

    col_mapping = {
        # PAMI 格式
        "ALFABETA": "numero_certificado",
        "PRINCIPIO ACTIVO": "nombre_generico",
        "MARCA COMERCIAL": "nombre_comercial",
        "PRESENTACION": "presentacion",
        "LABORATORIO": "laboratorio_titular",
        "PVP PAMI AL 01/03/2026": "precio",
        "COBERTURA": "cobertura",
        "IMPORTE AFILIADO": "copago",
        # PAMI 替代欄位名（不同版本）
        "DROGA": "nombre_generico",
        "MARCA": "nombre_comercial",
        "COPAGO": "copago",
        # VNM 格式
        "LABORATORIO TITULAR": "laboratorio_titular",
        "N\u00b0 CERTIFICADO": "numero_certificado",
        "N° CERTIFICADO": "numero_certificado",
        "NOMBRE COMERCIAL": "nombre_comercial",
        "NOMBRE GENERICO": "nombre_generico",
        "CONCENTRACI\u00d3N": "concentracion",
        "CONCENTRACIÓN": "concentracion",
        "FORMA FARMAC\u00c9UTICA": "forma_farmaceutica",
        "FORMA FARMACÉUTICA": "forma_farmaceutica",
        "PRESENTACI\u00d3N": "presentacion",
        "PRESENTACIÓN": "presentacion",
    }

    renamed = {}
    for old_name, new_name in col_mapping.items():
        if old_name in df.columns and old_name != new_name:
            renamed[old_name] = new_name
    if renamed:
        df = df.rename(columns=renamed)
        print(f"已標準化 {len(renamed)} 個欄位名稱")

    # 處理 PAMI 價格欄位中的 "$" 符號（移除，以便後續處理）
    for col in ["precio", "copago"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(r"^\$\s*", "", regex=True)

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON
    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    if len(data) < 100:
        print()
        print("*** 注意: 資料筆數較少。datos.salud.gob.ar 的 VNM 資料集僅包含")
        print("    2018 年度更新。如需完整資料庫，請使用 PAMI 開放資料：")
        print("    https://datos.pami.org.ar/dataset/medicamentos-para-entidades")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    ingredients_field = fm["ingredients"]
    manufacturer_field = fm.get("manufacturer", "")

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if manufacturer_field and manufacturer_field in df.columns:
        print(f"\n製藥廠商分布 (前 10):")
        lab_counts = df[manufacturer_field].value_counts().head(10)
        for lab, count in lab_counts.items():
            print(f"  {lab}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        if len(df) > 0:
            print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")

    # 劑型統計
    form_field = fm.get("dosage_form", "")
    if form_field and form_field in df.columns:
        print(f"\n劑型分布 (前 10):")
        form_counts = df[form_field].value_counts().head(10)
        for form, count in form_counts.items():
            print(f"  {form}: {count:,}")


def main():
    print("=" * 60)
    print("處理阿根廷 ANMAT 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    csv_path = raw_dir / "anmat_vademecum.csv"
    output_path = raw_dir / "ar_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已下載的 CSV/XLS（優先使用 PAMI 資料）
    pami_path = raw_dir / "pami_vademecum.csv"
    if pami_path.exists():
        csv_path = pami_path
        print(f"使用已存在的 PAMI 檔案: {csv_path}")
    elif not csv_path.exists():
        existing_files = (
            list(raw_dir.glob("pami*.csv"))
            + list(raw_dir.glob("gavade*.csv"))
            + list(raw_dir.glob("anmat*.csv"))
            + list(raw_dir.glob("vnm*.csv"))
            + list(raw_dir.glob("vademecum*.csv"))
            + list(raw_dir.glob("*.csv"))
            + list(raw_dir.glob("vnm*.xls"))
        )
        if existing_files:
            csv_path = existing_files[0]
            print(f"使用已存在的 CSV 檔案: {csv_path}")
        else:
            download_anmat_data(csv_path)
    else:
        print(f"使用已存在的 CSV 檔案: {csv_path}")

    # 處理 CSV
    process_anmat_csv(csv_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
