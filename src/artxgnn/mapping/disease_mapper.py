"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === 心血管系統 (Cardiovascular) ===
    "hipertensión": "hypertension",
    "hipertensión arterial": "hypertension",
    "presión arterial alta": "hypertension",
    "hipotensión": "hypotension",
    "infarto de miocardio": "myocardial infarction",
    "infarto": "myocardial infarction",
    "angina de pecho": "angina",
    "arritmia": "arrhythmia",
    "arritmia cardíaca": "arrhythmia",
    "fibrilación auricular": "atrial fibrillation",
    "insuficiencia cardíaca": "heart failure",
    "insuficiencia cardiaca congestiva": "heart failure",
    "enfermedad coronaria": "coronary artery disease",
    "cardiopatía isquémica": "ischemic heart disease",
    "trombosis venosa profunda": "deep vein thrombosis",
    "embolia pulmonar": "pulmonary embolism",
    "hipercolesterolemia": "hypercholesterolemia",
    "dislipidemia": "dyslipidemia",
    "aterosclerosis": "atherosclerosis",
    "endocarditis": "endocarditis",
    "miocarditis": "myocarditis",
    "pericarditis": "pericarditis",

    # === 呼吸系統 (Respiratory) ===
    "enfermedad pulmonar obstructiva crónica": "chronic obstructive pulmonary disease",
    "epoc": "chronic obstructive pulmonary disease",
    "asma": "asthma",
    "asma bronquial": "asthma",
    "neumonía": "pneumonia",
    "bronquitis": "bronchitis",
    "bronquitis crónica": "chronic bronchitis",
    "gripe": "influenza",
    "influenza": "influenza",
    "tuberculosis": "tuberculosis",
    "fibrosis quística": "cystic fibrosis",
    "apnea del sueño": "obstructive sleep apnea",
    "disnea": "dyspnea",
    "enfisema": "emphysema",
    "sinusitis": "sinusitis",
    "rinitis alérgica": "allergic rhinitis",

    # === 消化系統 (Gastrointestinal) ===
    "enfermedad por reflujo gastroesofágico": "gastroesophageal reflux disease",
    "reflujo gastroesofágico": "gastroesophageal reflux disease",
    "úlcera péptica": "peptic ulcer",
    "úlcera gástrica": "gastric ulcer",
    "úlcera duodenal": "duodenal ulcer",
    "gastritis": "gastritis",
    "síndrome del intestino irritable": "irritable bowel syndrome",
    "enfermedad inflamatoria intestinal": "inflammatory bowel disease",
    "enfermedad de crohn": "crohn disease",
    "colitis ulcerosa": "ulcerative colitis",
    "estreñimiento": "constipation",
    "diarrea": "diarrhea",
    "náuseas": "nausea",
    "vómitos": "vomiting",
    "hígado graso": "hepatic steatosis",
    "cirrosis": "liver cirrhosis",
    "cirrosis hepática": "liver cirrhosis",
    "hepatitis": "hepatitis",
    "hepatitis b": "hepatitis b",
    "hepatitis c": "hepatitis c",
    "pancreatitis": "pancreatitis",
    "colelitiasis": "cholelithiasis",

    # === 神經系統 (Neurological) ===
    "enfermedad de alzheimer": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "enfermedad de parkinson": "parkinson disease",
    "parkinson": "parkinson disease",
    "epilepsia": "epilepsy",
    "esclerosis múltiple": "multiple sclerosis",
    "migraña": "migraine",
    "cefalea": "headache",
    "dolor de cabeza": "headache",
    "accidente cerebrovascular": "stroke",
    "ictus": "stroke",
    "neuropatía": "neuropathy",
    "neuropatía periférica": "peripheral neuropathy",
    "neuralgia del trigémino": "trigeminal neuralgia",
    "meningitis": "meningitis",
    "encefalitis": "encephalitis",

    # === 精神疾病 (Psychiatric) ===
    "depresión": "depression",
    "trastorno depresivo mayor": "major depressive disorder",
    "ansiedad": "anxiety disorder",
    "trastorno de ansiedad generalizada": "generalized anxiety disorder",
    "trastorno bipolar": "bipolar disorder",
    "esquizofrenia": "schizophrenia",
    "trastorno obsesivo-compulsivo": "obsessive-compulsive disorder",
    "toc": "obsessive-compulsive disorder",
    "trastorno de estrés postraumático": "post-traumatic stress disorder",
    "tept": "post-traumatic stress disorder",
    "insomnio": "insomnia",
    "trastorno por déficit de atención": "attention deficit hyperactivity disorder",
    "tdah": "attention deficit hyperactivity disorder",

    # === 內分泌系統 (Endocrine) ===
    "diabetes mellitus": "diabetes mellitus",
    "diabetes tipo 1": "type 1 diabetes mellitus",
    "diabetes tipo 2": "type 2 diabetes mellitus",
    "hipotiroidismo": "hypothyroidism",
    "hipertiroidismo": "hyperthyroidism",
    "bocio": "goiter",
    "síndrome de cushing": "cushing syndrome",
    "enfermedad de addison": "addison disease",
    "obesidad": "obesity",
    "síndrome metabólico": "metabolic syndrome",
    "hiperuricemia": "hyperuricemia",
    "gota": "gout",

    # === 肌肉骨骼系統 (Musculoskeletal) ===
    "artritis": "arthritis",
    "artritis reumatoide": "rheumatoid arthritis",
    "osteoartritis": "osteoarthritis",
    "artrosis": "osteoarthritis",
    "osteoporosis": "osteoporosis",
    "lupus eritematoso sistémico": "systemic lupus erythematosus",
    "lupus": "systemic lupus erythematosus",
    "fibromialgia": "fibromyalgia",
    "espondilitis anquilosante": "ankylosing spondylitis",
    "tendinitis": "tendinitis",
    "dolor lumbar": "low back pain",
    "lumbago": "low back pain",

    # === 皮膚疾病 (Dermatological) ===
    "psoriasis": "psoriasis",
    "eccema": "eczema",
    "dermatitis atópica": "atopic dermatitis",
    "dermatitis": "dermatitis",
    "urticaria": "urticaria",
    "acné": "acne",
    "rosácea": "rosacea",
    "vitíligo": "vitiligo",
    "alopecia": "alopecia",
    "herpes zóster": "herpes zoster",
    "herpes simple": "herpes simplex",
    "micosis": "fungal infection",

    # === 泌尿系統 (Urological) ===
    "infección del tracto urinario": "urinary tract infection",
    "cistitis": "cystitis",
    "nefritis": "nephritis",
    "insuficiencia renal": "renal failure",
    "insuficiencia renal crónica": "chronic kidney disease",
    "enfermedad renal crónica": "chronic kidney disease",
    "litiasis renal": "nephrolithiasis",
    "cálculos renales": "nephrolithiasis",
    "hiperplasia prostática benigna": "benign prostatic hyperplasia",
    "incontinencia urinaria": "urinary incontinence",

    # === 眼科 (Ophthalmological) ===
    "glaucoma": "glaucoma",
    "cataratas": "cataract",
    "degeneración macular": "macular degeneration",
    "conjuntivitis": "conjunctivitis",
    "retinopatía diabética": "diabetic retinopathy",
    "ojo seco": "dry eye syndrome",
    "uveítis": "uveitis",

    # === 耳鼻喉 (ENT) ===
    "otitis media": "otitis media",
    "otitis": "otitis",
    "faringitis": "pharyngitis",
    "amigdalitis": "tonsillitis",
    "laringitis": "laryngitis",
    "vértigo": "vertigo",

    # === 感染症 (Infectious) ===
    "vih": "hiv infection",
    "sida": "acquired immunodeficiency syndrome",
    "malaria": "malaria",
    "dengue": "dengue",
    "covid-19": "covid-19",
    "coronavirus": "covid-19",
    "sepsis": "sepsis",
    "candidiasis": "candidiasis",
    "infección por hongos": "fungal infection",
    "herpes": "herpes simplex",
    "toxoplasmosis": "toxoplasmosis",
    "leishmaniasis": "leishmaniasis",
    "chagas": "chagas disease",

    # === 過敏 (Allergic) ===
    "alergia": "allergy",
    "anafilaxia": "anaphylaxis",
    "asma alérgica": "allergic asthma",
    "rinitis": "rhinitis",
    "dermatitis de contacto": "contact dermatitis",
    "alergia alimentaria": "food allergy",

    # === 婦科 (Gynecological) ===
    "endometriosis": "endometriosis",
    "síndrome de ovario poliquístico": "polycystic ovary syndrome",
    "menopausia": "menopause",
    "dismenorrea": "dysmenorrhea",
    "amenorrea": "amenorrhea",
    "vaginitis": "vaginitis",
    "mioma uterino": "uterine fibroid",
    "preeclampsia": "preeclampsia",

    # === 腫瘤/癌症 (Oncological) ===
    "cáncer": "cancer",
    "cáncer de mama": "breast cancer",
    "cáncer de pulmón": "lung cancer",
    "cáncer colorrectal": "colorectal cancer",
    "cáncer de próstata": "prostate cancer",
    "cáncer de hígado": "liver cancer",
    "cáncer de estómago": "stomach cancer",
    "cáncer gástrico": "stomach cancer",
    "cáncer de páncreas": "pancreatic cancer",
    "leucemia": "leukemia",
    "linfoma": "lymphoma",
    "melanoma": "melanoma",
    "cáncer de riñón": "kidney cancer",
    "cáncer de vejiga": "bladder cancer",
    "cáncer de tiroides": "thyroid cancer",

    # === 一般症狀 (General) ===
    "fiebre": "fever",
    "dolor": "pain",
    "dolor crónico": "chronic pain",
    "inflamación": "inflammation",
    "edema": "edema",
    "fatiga": "fatigue",
    "anemia": "anemia",
    "trombocitopenia": "thrombocytopenia",
    "neutropenia": "neutropenia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get("CLASSE_TERAPEUTICA", "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
