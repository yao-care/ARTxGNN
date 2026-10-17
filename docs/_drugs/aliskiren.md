---
layout: default
title: Aliskiren
parent: Evidencia Moderada (L3-L4)
nav_order: 20
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Aliskiren: nueva indicación predicha, Hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia (nivel de evidencia L4). Indicación original: Hipertensión arterial (según la base de conocimi…"
monitor_inn: "ALISKIREN"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "chronic pulmonary heart disease", "cerebrovascular disorder"]
---

# Aliskiren
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Aliskiren: De Hipertensión a Hipertensión Pulmonar Secundaria a Enfermedad Pulmonar y/o Hipoxia

## Resumen en Una Frase

Aliskiren es un inhibidor directo de la renina, originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia**,
pero actualmente no hay **ningún ensayo clínico** y solo se dispone de **4 publicaciones**, todas preclínicas o indirectas, por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según la base de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, aliskiren inhibe la renina, la enzima que da el primer paso del sistema renina-angiotensina-aldosterona (SRAA), y con ello reduce la actividad de toda la cascada. Su eficacia en la hipertensión arterial está comprobada, y mecanísticamente podría ser aplicable a la hipertensión pulmonar.

La relación entre ambas indicaciones es indirecta. Estudios preclínicos en ratas con hipoxia intermitente crónica sugieren que la angiotensina II contribuye a la activación simpática y al remodelado auricular, y que aliskiren atenuó el remodelado en ese modelo. Esto ofrece un apoyo plausible pero indirecto: ningún estudio en humanos ha evaluado criterios de valoración vasculares pulmonares o de hipertensión pulmonar.

El puntaje TxGNN es muy alto, pero es solo una predicción computacional basada en asociaciones del grafo de conocimiento. No debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32982180](https://pubmed.ncbi.nlm.nih.gov/32982180/) | 2020 | Preclínico (animal) | Drug Des Devel Ther | Estudio en ratas con hipoxia intermitente crónica para evaluar el efecto de aliskiren sobre el remodelado auricular; el fármaco mostró un posible efecto protector |
| [29645283](https://pubmed.ncbi.nlm.nih.gov/29645283/) | 2018 | Preclínico (animal) | J Physiol | En ratas, la simpatoexcitación tras hipoxia intermitente está mediada por angiotensina II circulante; la inhibición del SRA previene estos efectos |
| [39133776](https://pubmed.ncbi.nlm.nih.gov/39133776/) | 2024 | Preclínico (in vitro) | Am J Physiol Regul Integr Comp Physiol | Actividad de liberación de angiotensina II en cortes cerebrales de rata; relevancia solo contextual sobre el SRA |
| [26502369](https://pubmed.ncbi.nlm.nih.gov/26502369/) | 2016 | Preclínico | Transplantation | Los inhibidores de calcineurina aumentan la renina local y el VEGF en los conductos colectores renales; relación lejana con la indicación |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43513 | RASILEZ (Novartis) | Comprimidos recubiertos 150 mg x 28 | No disponible en los datos |
| 43515 | RASILEZ (Novartis) | Comprimidos recubiertos 300 mg x 28 | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones según la base de conocimiento** (relaciones fármaco-enfermedad del grafo de conocimiento, no texto del prospecto):
  - Hepáticas y biliares: insuficiencia hepática, enfermedad hepática, encefalopatía hepática, coma hepático, enfermedad de la vesícula biliar, pancreatitis, ictericia neonatal.
  - Angioedema: angioedema (adquirido, hereditario, no histaminérgico e inducido por bloqueadores del SRAA).
  - Renales: anuria, deterioro de la función renal, obstrucción de la arteria renal.
  - Metabólicas y electrolíticas: diabetes mellitus, cetoacidosis diabética, déficit de potasio, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hiperparatiroidismo, osteítis fibrosa, hiperuricemia, gota.
  - Hematológicas: neutropenia, agranulocitosis.
  - Otras: lupus eritematoso sistémico (incluido el pediátrico) e hipotensión.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones, todas de las que se muestran son de nivel moderado. Entre las principales:
  - Corticoides: hidrocortisona, betametasona, budesonida, dexametasona, prednisolona, prednisona.
  - Inhibidores de SGLT2: canagliflozina, dapagliflozina, empagliflozina, ertugliflozina.
  - Sales de potasio: bicarbonato, cloruro, citrato y gluconato de potasio (riesgo de hiperpotasemia).
  - Otros: ácido acetilsalicílico, aprepitant, claritromicina, clotrimazol, miconazol, eliglustat.
- **Contexto de seguridad en la literatura**: el ensayo ALTITUDE planteó preocupaciones con el doble bloqueo del SRAA en pacientes diabéticos con deterioro renal (hipotensión, ictus isquémico, hiperpotasemia).

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en puntaje computacional y en estudios preclínicos indirectos, sin ensayos clínicos ni estudios en humanos sobre hipertensión pulmonar. El mecanismo es plausible pero no está demostrado para esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Revisión del prospecto de ANMAT para advertencias y contraindicaciones oficiales.
- Estudios preclínicos específicos en modelos de hipertensión pulmonar (vascular pulmonar, no solo remodelado auricular).
- Evaluación de la relevancia frente a otras predicciones del modelo con más respaldo; por ejemplo, para el trastorno cerebrovascular existe un ensayo de Fase 2/3 terminado (NCT01417104) y evidencia de nivel L3, aunque tampoco es concluyente.
- Análisis de seguridad en pacientes con enfermedad pulmonar e hipoxia, dada la lista amplia de contraindicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

