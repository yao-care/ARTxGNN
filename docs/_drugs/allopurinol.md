---
layout: default
title: Allopurinol
parent: Evidencia Moderada (L3-L4)
nav_order: 21
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Allopurinol: nueva indicación predicha, Porfiria hepática (nivel de evidencia L4). Indicación original: Gota (según el grafo de conocimiento TxGNN"
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
---

# Allopurinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Alopurinol: De Gota a Porfiria Hepática
{: .text-alpha }

## Resumen en Una Frase

Alopurinol es un inhibidor de la xantina oxidasa, originalmente utilizado para el tratamiento de la gota, la hiperuricemia y la nefropatía aguda por uratos.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**, pero actualmente solo hay **2 publicaciones** indirectas (una hipótesis y un estudio preclínico en ratas) y **ningún ensayo clínico** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota (según el grafo de conocimiento TxGNN; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, alopurinol es un inhibidor de la xantina oxidasa, su eficacia en gota e hiperuricemia está comprobada, y mecanísticamente podría tener algún efecto sobre el metabolismo del hemo hepático.

La literatura antigua describe que alopurinol puede influir en la biosíntesis del hemo y en la actividad de la 5-aminolevulinato sintasa (ALAS1) en sistemas experimentales. Los dos artículos recuperados son una hipótesis de 2019 sobre el control metabólico de ALAS1 en porfirias hepáticas agudas y un estudio de 1992 en ratas sobre el efecto de la carbamazepina en el metabolismo del hemo. Ninguno es un estudio clínico de alopurinol en porfiria, por lo que el vínculo es plausible pero indirecto.

Además, existe una preocupación de seguridad: en algunos contextos experimentales alopurinol se ha descrito como agente potencialmente porfirinogénico o degradador del hemo, por lo que la **dirección del efecto es incierta** y podría incluso ser perjudicial.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisión/Hipótesis | Medical Hypotheses | Propone el control metabólico de la ALAS1 hepática mediante triptófano o inhibición de la triptófano 2,3-dioxigenasa como terapia de porfirias hepáticas agudas. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclínico (animal) | Biochemical Pharmacology | La carbamazepina, a dosis muy bajas, agrava las porfirias hepáticas al alterar el metabolismo del hemo en hígado de rata. |

---

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes (todas de producto único, ninguna cancelada). Principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48995 | ALLOPURINOL 300 CRAVERI | 300 mg comp. x 60 | No disponible |
| 49651 | ALLOPURINOL GADOR RETARD | 300 mg comp. x 30 | No disponible |
| 22580 | PURITENK | 300 mg comp. x 20 | No disponible |
| 35535 | ALLOPURINOL GADOR | 100 mg comp. x 30 | No disponible |
| 44167 | COLPURIL A RETARD | Cáps. con microgránulos x 50 | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, función renal alterada, vasculitis por hipersensibilidad, angeítis leucocitoclástica cutánea, vasculitis cutánea alérgica y enfermedad antimembrana basal glomerular.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las de nivel moderado incluyen hidróxido de aluminio, atapulgita, caolín, magaldrato y sucralfato. Las de nivel menor incluyen amoxicilina y clorpropamida. Otras (p. ej., calcitriol, vitamina A, pantoprazol, glimepirida, mesalazina, doxiciclina, metformina, omeprazol) tienen nivel no clasificado.
- **Consideración específica**: alopurinol podría ser porfirinogénico en algunos modelos experimentales, lo que es relevante para la indicación propuesta. Dado que la contraindicación por enfermedad hepática figura en el grafo, esto exige especial cautela.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica e hipotética (L4), sin ensayos clínicos, y la dirección del efecto de alopurinol sobre el metabolismo del hemo es incierta, con posible riesgo en porfiria. El alto puntaje de TxGNN por sí solo no justifica avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de alopurinol (consulta a DrugBank) y análisis del vínculo mecanístico con la regulación de ALAS1.
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad.
- Estudios preclínicos que aclaren si alopurinol es protector o porfirinogénico.
- Revisión de seguridad en pacientes con enfermedad hepática, dada su contraindicación en el grafo.

**Otras predicciones (todas en Hold):** las predicciones siguientes (hipertensión portal no cirrótica familiar de inicio temprano, síndrome hepatopulmonar, cirrosis idiopática asociada al cobre, trombosis portal primitiva, esclerosis hepatoportal, miopatía necrosante inmunomediada, síndrome antisintetasa y miopatía inflamatoria con abundantes macrófagos) carecen de ensayos y literatura (L5). El trastorno del metabolismo de la fenilalanina cuenta con literatura solo indirecta (L4). Ninguna tiene sustento mecanístico en los datos disponibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

