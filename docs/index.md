---
layout: default
title: Predicciones de Reposicionamiento de Medicamentos
nav_order: 1
description: "Predicciones de reposicionamiento de medicamentos impulsadas por IA para Argentina. Análisis basado en evidencia de medicamentos aprobados para posibles nuevas indicaciones terapéuticas."
permalink: /
---

# Predicciones de Reposicionamiento de Medicamentos — Argentina

Este proyecto utiliza el modelo TxGNN (aprendizaje profundo) para predecir posibles nuevos usos terapéuticos para medicamentos aprobados en Argentina.

**Descargo de Responsabilidad**: Este contenido es solo para fines de investigación y no constituye consejo médico. Todas las predicciones de reposicionamiento de medicamentos requieren validación clínica antes de su aplicación.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Argentina: qué cubre este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [ANMAT](https://www.argentina.gob.ar/anmat) (Argentina).

Informes por nivel de evidencia: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Medicamentos con mayor nivel de evidencia en este sitio

| Medicamento | Nivel de evidencia |
|---|---|
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Natamycin](/drugs/natamycin/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Salmeterol](/drugs/salmeterol/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Trazodone](/drugs/trazodone/) | L2 |
| [Lornoxicam](/drugs/lornoxicam/) | L2 |
| [Montelukast](/drugs/montelukast/) | L2 |
| [Calcipotriol](/drugs/calcipotriol/) | L3 |
| [Citalopram](/drugs/citalopram/) | L3 |

### Medicamentos que solo cubre este sitio entre los 30 sitios TxGNN

| Medicamento | Nivel de evidencia |
|---|---|
| [Aniracetam](/drugs/aniracetam/) | L4 |

<!-- local-home:end -->

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
de empresa 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ARTxGNN es el sitio de Argentina de la línea de productos "TxGNN Drug Repurposing" de la empresa.
El mismo sistema está desplegado en 30 países y regiones, cada uno denominado `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, y así sucesivamente) en `{cc}txgnn.yao.care`.
Descripción del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN en sí fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado
en *Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 construyó
sobre ese modelo, y abarca la integración de los datos nacionales de registro de medicamentos, la
predicción por aprendizaje profundo que excluye los usos ya registrados en el grafo de conocimiento, la gradación de evidencia con
PubMed / ClinicalTrials y la integración con la historia clínica electrónica mediante SMART on FHIR.
