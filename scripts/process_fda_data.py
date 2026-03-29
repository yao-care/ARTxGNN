#!/usr/bin/env python3
"""處理阿根廷 ANMAT 藥品資料

從 datos.salud.gob.ar CKAN API 下載 Vademécum 藥品 CSV 並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    主要: datos.salud.gob.ar CKAN API - Vademécum Nacional de Medicamentos (VNM)
          https://datos.salud.gob.ar/dataset/vademecun-nacional-de-medicamentos-vnm
    備用: datos.gob.ar 鏡像站
          https://datos.gob.ar/dataset/salud-actualizaciones-vademecun-nacional-medicamentos-vnm

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
    """從 datos.salud.gob.ar 下載 ANMAT 藥品 CSV

    透過 CKAN API 取得 Vademécum Nacional de Medicamentos 的 CSV 資源。
    API 回傳的資源包含多個版本 (2018-06, 2018-12 等)，優先下載最新的 CSV。

    Args:
        output_path: CSV 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    ds = config["data_source"]

    print("正在從 datos.salud.gob.ar 下載 ANMAT 藥品資料...")
    print()

    # ── 方法 1: CKAN API ──
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

            # 優先取 CSV，按建立日期倒序
            csv_resources = [
                r for r in resources
                if r.get("format", "").upper() == "CSV"
            ]

            if not csv_resources:
                print(f"  未找到 CSV 資源")
                continue

            # 取最後一個 (通常是最新的)
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

    # ── 方法 2: 直接下載已知 URL ──
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

    # ── 方法 3: 回報手動下載指引 ──
    page_url = ds.get("page_url", "https://datos.salud.gob.ar/dataset?groups=vademecum-y-medicamentos")
    raise FileNotFoundError(
        f"自動下載 ANMAT Vademécum CSV 失敗\n\n"
        f"datos.salud.gob.ar 上的 VNM 資料集僅包含 2018 年度更新 (約 60 筆)，\n"
        f"非完整藥品資料庫。如需完整資料，請手動取得：\n\n"
        f"方法 A: datos.salud.gob.ar (部分更新資料)\n"
        f"  1. 前往 {page_url}\n"
        f"  2. 下載 VNM 的 CSV 檔案\n"
        f"  3. 將 CSV 放置於: {output_path}\n\n"
        f"方法 B: ANMAT Vademécum 完整資料庫\n"
        f"  1. 前往 https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul\n"
        f"  2. 此為查詢介面，完整資料庫約 49,000+ 筆\n"
        f"  3. 可依字母逐批匯出，或聯繫 ANMAT\n"
        f"     (responde@anmat.gob.ar 或 0800-333-1234)\n\n"
        f"方法 C: ANMAT 藥品查詢頁面\n"
        f"  1. 前往 https://www.anmat.gob.ar/Medicamentos/basedat.asp\n"
        f"  2. 匯出搜尋結果\n"
        f"  3. 將檔案放置於: {output_path}\n\n"
        f"支援格式: CSV, XLS"
    )


def process_anmat_csv(csv_path: Path, output_path: Path) -> Path:
    """處理 ANMAT CSV 並轉換為 JSON

    datos.salud.gob.ar 的 VNM CSV 欄位為：
      - laboratorio_titular / LABORATORIO TITULAR
      - numero_certificado / N° CERTIFICADO
      - nombre_comercial / NOMBRE COMERCIAL
      - nombre_generico / NOMBRE GENERICO
      - concentracion / CONCENTRACION
      - forma_farmaceutica / FORMA FARMACEUTICA
      - presentacion / PRESENTACION

    Args:
        csv_path: CSV 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()
    encoding = config.get("encoding", "utf-8")

    print(f"讀取 CSV 檔案: {csv_path}")

    # 嘗試不同編碼
    for enc in [encoding, "utf-8-sig", "latin-1", "cp1252"]:
        try:
            df = pd.read_csv(csv_path, encoding=enc, dtype=str, on_bad_lines="skip")
            if len(df.columns) > 1:
                break
        except (UnicodeDecodeError, pd.errors.EmptyDataError):
            continue
    else:
        df = pd.read_csv(csv_path, encoding="latin-1", dtype=str, on_bad_lines="skip")

    print(f"原始資料筆數: {len(df)}")
    print(f"欄位: {', '.join(df.columns.tolist())}")

    # 標準化欄位名稱 (datos.salud.gob.ar 有兩種格式)
    col_mapping = {
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
        if old_name in df.columns:
            renamed[old_name] = new_name
    if renamed:
        df = df.rename(columns=renamed)
        print(f"已標準化 {len(renamed)} 個欄位名稱")

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
        print("    2018 年度更新。如需完整資料庫 (約 49,000+ 筆)，請參考")
        print("    ANMAT/PAMI Vademécum 完整資料。")

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

    # 尋找已下載的 CSV/XLS
    if not csv_path.exists():
        existing_files = (
            list(raw_dir.glob("anmat*.csv"))
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
