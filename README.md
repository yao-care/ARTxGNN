# ARTxGNN - Argentina: Reposicionamiento de Medicamentos

> 本專案由 **藥提醒科技有限公司**（[yao.care](https://www.yao.care)）開發與維運。
> ARTxGNN 站台：<https://artxgnn.yao.care/>｜產品總覽：<https://www.yao.care/medical/txgnn/>

[![Website](https://img.shields.io/badge/Website-artxgnn.yao.care-blue)](https://artxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Predicciones de reposicionamiento de medicamentos para medicamentos aprobados por ANMAT (Argentina) usando el modelo TxGNN.

## Aviso legal

- Los resultados de este proyecto son solo para fines de investigacion y no constituyen consejo medico.
- Los candidatos a reposicionamiento de medicamentos requieren validacion clinica antes de su aplicacion.

## Vision general del proyecto

### Estadisticas de informes

| Elemento | Cantidad |
|------|------|
| **Informes de medicamentos** | 160 |
| **Predicciones totales** | 10,483,518 |
| **Medicamentos unicos** | 390 |
| **Indicaciones unicas** | 14,310 |
| **Datos DDI** | 302,516 |
| **Datos DFI** | 857 |
| **Datos DHI** | 35 |
| **Datos DDSI** | 8,359 |
| **Recursos FHIR** | 314 MK / 2,564 CUD |

### Distribucion de niveles de evidencia

| Nivel de evidencia | Cantidad de informes | Descripcion |
|---------|-------|------|
| **L1** | 0 | Multiples ECAs de Fase 3 |
| **L2** | 0 | ECA unico o multiples Fase 2 |
| **L3** | 0 | Estudios observacionales |
| **L4** | 0 | Estudios preclinicos / mecanisticos |
| **L5** | 314 | Solo prediccion computacional |

### Por fuente

| Fuente | Predicciones |
|------|------|
| DL | 10,480,973 |
| KG + DL | 2,179 |
| KG | 366 |

### Por confianza

| Confianza | Predicciones |
|------|------|
| very_high | 1,665 |
| high | 438,175 |
| medium | 780,855 |
| low | 9,262,823 |

---

## Metodos de prediccion

| Metodo | Velocidad | Precision | Requisitos |
|------|------|--------|----------|
| Grafo de conocimiento | Rapido (segundos) | Menor | Sin requisitos especiales |
| Aprendizaje profundo | Lento (horas) | Mayor | Conda + PyTorch + DGL |

### Metodo del grafo de conocimiento

```bash
uv run python scripts/run_kg_prediction.py
```

| Metrica | Valor |
|------|------|
| ANMAT Total de medicamentos | 10,167 |
| Mapeados a DrugBank | 7,347 (72.3%) |
| Candidatos a reposicionamiento | 2,545 |

### Metodo de aprendizaje profundo

```bash
conda activate txgnn
PYTHONPATH=src python -m artxgnn.predict.txgnn_model
```

| Metrica | Valor |
|------|------|
| Predicciones DL totales | 611,946 |
| Medicamentos unicos | 390 |
| Indicaciones unicas | 14,310 |

### Interpretacion de puntuaciones

La puntuacion TxGNN representa la confianza del modelo en un par farmaco-enfermedad, con un rango de 0 a 1.

| Umbral | Significado |
|-----|------|
| >= 0.9 | Confianza muy alta |
| >= 0.7 | Confianza alta |
| >= 0.5 | Confianza moderada |

#### Distribucion de puntuaciones

| Umbral | Significado |
|-----|------|
| ≥ 0.9999 | Confianza extremadamente alta, predicciones mas confiables del modelo |
| ≥ 0.99 | Confianza muy alta, vale la pena priorizar para validacion |
| ≥ 0.9 | Confianza alta |
| ≥ 0.5 | Confianza moderada (frontera de decision sigmoide) |

#### Definiciones de niveles de evidencia

| Nivel | Definicion | Significancia clinica |
|-----|------|---------|
| L1 | ECA de fase 3 o revision sistematica | Puede respaldar el uso clinico |
| L2 | ECA de fase 2 | Puede considerarse para uso |
| L3 | Fase 1 o estudio observacional | Requiere evaluacion adicional |
| L4 | Reporte de caso o investigacion preclinica | Aun no recomendado |
| L5 | Solo prediccion computacional, sin evidencia clinica | Requiere investigacion adicional |

#### Recordatorios importantes

1. **Las puntuaciones altas no garantizan eficacia clinica: las puntuaciones TxGNN son predicciones basadas en grafos de conocimiento que requieren validacion en ensayos clinicos.**
2. **Las puntuaciones bajas no significan ineficacia: el modelo puede no haber aprendido ciertas asociaciones.**
3. **Se recomienda usar con el pipeline de validacion: utilice las herramientas de este proyecto para revisar ensayos clinicos, literatura y otra evidencia.**

### Pipeline de validacion

```mermaid
flowchart TD
    A["Resultados de prediccion TxGNN"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Nivel de medicamento: ANMAT, DDI, DrugBank"]
        B2["Nivel de indicacion: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Transferencia programatica de datos (100%)"]
        C2["+ LLM Analisis (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Inicio rapido

### Paso 1: Descargar datos

| Archivo | Descarga |
|------|------|
| ANMAT Datos | Fuente de datos |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Paso 2: Instalar dependencias

```bash
uv sync
```

### Paso 3: Procesar datos de medicamentos

```bash
uv run python scripts/process_fda_data.py
```

### Paso 4: Preparar datos de vocabulario

```bash
uv run python scripts/prepare_external_data.py
```

### Paso 5: Ejecutar prediccion del grafo de conocimiento

```bash
uv run python scripts/run_kg_prediction.py
```

### Paso 6: Configurar entorno de aprendizaje profundo

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Paso 7: Ejecutar prediccion de aprendizaje profundo

```bash
conda activate txgnn
PYTHONPATH=src python -m artxgnn.predict.txgnn_model
```

---

## Recursos

### TxGNN Nucleo

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Fuentes de datos

| Categoria | Datos | Fuente | Nota |
|------|------|------|------|
| **Datos de medicamentos** | ANMAT | - | Argentina |
| **Grafo de conocimiento** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Base de datos de medicamentos** | DrugBank | [DrugBank](https://go.drugbank.com/) | Mapeo de ingredientes de medicamentos |
| **Interacciones medicamentosas** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | Pares DDI |
| **Interacciones medicamentosas** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Interacciones de medicamentos aprobados |
| **Ensayos clinicos** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Registro de ensayos clinicos |
| **Ensayos clinicos** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | Plataforma internacional de ensayos clinicos |
| **Literatura** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Busqueda de literatura medica |
| **Mapeo de nombres** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Estandarizacion de nombres de medicamentos |
| **Mapeo de nombres** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Busqueda de sinonimos quimicos |
| **Mapeo de nombres** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Base de datos de bioactividad |
| **Estandares** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Estandares** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | Integracion EHR, OAuth 2.0 + PKCE |

### Descargas de modelos

| Archivo | Descarga | Nota |
|------|------|------|
| Modelo pre-entrenado | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Datos de nodos |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Datos del grafo de conocimiento |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Datos de aristas (DL) |

## Introduccion al proyecto

### Estructura de directorios

```
ARTxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/artxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Leyenda**: 🔵 Desarrollo del proyecto | 🟢 Datos locales | 🟡 Datos TxGNN | 🟠 Pipeline de validacion

### Flujo de datos

```mermaid
flowchart TD
    FDA["ANMAT Datos"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Datos"] --> prep["prepare_external_data.py"]

    proc --> json["ar_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Grafo de conocimiento"]
    ind_map --> DL["Aprendizaje profundo"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Citacion

Si utiliza este conjunto de datos o software, por favor cite:

```bibtex
@software{artxgnn2026,
  author       = {Yao.Care},
  title        = {ARTxGNN: Drug Repurposing Validation Reports for Argentina ANMAT Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/ARTxGNN}
}
```

Cite tambien el articulo original de TxGNN:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

<!-- txgnn-ops:start -->
## 維運：資料還原與許可證更新

### 完整還原

git 只放程式碼與網站頁面；許可證原始資料、證據包、藥師報告原稿、預測結果放在本 repo 的 Release。

```bash
git clone https://github.com/yao-care/artxgnn.git && cd artxgnn
uv sync                                  # Python 相依套件
bash scripts/restore_data.sh             # 取最新的 data-* Release，還原 data/（含校驗）
bash scripts/restore_data.sh --with-kg   # 另加共用知識圖譜與預測模型（只有重跑預測才需要）
```

需要 [GitHub CLI](https://cli.github.com/)（`gh auth login`）與 [uv](https://docs.astral.sh/uv/)。

### 改頁工具鏈

事實層、checker、許可證狀態計算等放在 `tools/txgnn/.claude/`，是母 repo `yao-care/txgnn` 的 `.claude/` 複本（版本見 `tools/txgnn/VERSION`）。
規則要改請改母 repo，再用 `python3 .claude/sync_site_tools.py ARTxGNN` 同步過來，不要直接改這裡的複本。
在本 repo 單獨使用時，先組工作目錄：

```bash
WS=$(bash scripts/txgnn_ws.sh)
cd "$WS"
python3 .claude/dump_license_facts_20261021.py ARTxGNN       # 依證據包算市場狀態（checker 要用）
python3 .claude/checker_trend.py --no-append ARTxGNN           # 全部藥物頁 checker，必須「非 0 0」
```

### 許可證排程更新（GitHub Actions）

`.github/workflows/license-refresh.yml` 每週一 UTC 03:17 自動執行，也可以在 Actions 頁手動觸發（可選只試跑）：

1. 從 Release 還原 `data/`（`scripts/restore_data.sh`）
2. 從主管機關下載最新許可證資料（`scripts/license_adapter.py`），檢查筆數與格式
3. 更新證據包的許可證狀態 → 重算市場狀態 → 同步許可證表 → 事實層改頁 → checker 全量必須 0 → 衍生檔 → gate
4. 全部通過才推上 `main` 並觸發部署；更新後的 `data/` 另存成新的 `data-YYYYMMDD` Release

以下情況一律不推、自動開 issue（label `license-refresh`）：下載失敗或格式改變、狀態變動超過兩成、
改到的藥物頁超過 min(200, 5%)、checker／gate／h1 沒過、有人工查核紀錄的頁會被改到。全程不使用 AI。
<!-- txgnn-ops:end -->
