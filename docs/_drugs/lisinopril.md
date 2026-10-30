---
layout: default
title: Lisinopril
parent: Solo Predicción del Modelo (L5)
nav_order: 180
evidence_level: L5
indication_count: 6
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
last_modified_at: 2026-10-30
description: "Lisinopril: nueva indicación predicha, Hipertensión pulmonar debida a enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hyp… (nivel de evidencia L5). Indicación ori…"
---

# Lisinopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Lisinopril: inhibidor de la enzima convertidora de angiotensina (ECA) → hipertensión pulmonar debida a enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia)
{: .text-alpha }

## Resumen en Una Frase

Lisinopril es un inhibidor de la enzima convertidora de angiotensina (ECA) comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar debida a enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia)**,
pero actualmente **no hay ensayos clínicos** registrados y la literatura recopilada no incluye ningún estudio que evalúe directamente esta enfermedad con lisinopril; la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertensión pulmonar debida a enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia) |
| Puntaje de Predicción TxGNN | 0,9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (11 de 11) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por su clase farmacológica, lisinopril inhibe la ECA y reduce la producción de angiotensina II, lo que podría atenuar la vasoconstricción y el remodelado vascular pulmonar.

Sin embargo, el mecanismo es débil para esta enfermedad: un estudio preclínico en arterias pulmonares aisladas de rata (PMID 10456287) indica que la respuesta contráctil a la hipoxia depende sobre todo de la endotelina y no de la angiotensina II. Esto debilita la justificación mecanística.

El resto de la literatura recuperada es preclínica o tangencial (expresión génica en músculo con ejercicio, retinopatía del prematuro, fibrosis pancreática en ratas, fisiología de la trucha, hipertensión pulmonar experimental con simvastatina). Ninguna estudia lisinopril en hipertensión pulmonar asociada a hipoxia en humanos. Por ello el nivel de evidencia se limita a L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Selección de las publicaciones más cercanas al tema; ninguna estudia directamente la enfermedad predicha en humanos con lisinopril.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10456287](https://pubmed.ncbi.nlm.nih.gov/10456287/) | 1999 | Preclínico (vasos aislados) | Fundamental & Clinical Pharmacology | En arterias pulmonares de rata, la respuesta contráctil a la hipoxia depende de la endotelina, no de la angiotensina II. |
| [16698853](https://pubmed.ncbi.nlm.nih.gov/16698853/) | 2006 | Animal | Am J Physiol Lung Cell Mol Physiol | Simvastatina (otro fármaco) atenúa la hipertensión pulmonar grave en un modelo de rata. |
| [8016291](https://pubmed.ncbi.nlm.nih.gov/8016291/) | 1994 | Sin clasificar | Puerto Rico Health Sci J | Tras administración sublingual de inhibidores de la ECA en cateterismo se observaron aumentos transitorios de la presión arterial pulmonar y de la resistencia vascular pulmonar. |
| [26407530](https://pubmed.ncbi.nlm.nih.gov/26407530/) | 2016 | Mecanístico/fisiología humana | Scand J Med Sci Sports | La inhibición de la ECA modifica la expresión de genes proangiogénicos y mitocondriales tras el ejercicio. |
| [3208727](https://pubmed.ncbi.nlm.nih.gov/3208727/) | 1988 | Preclínico | Experimental Lung Research | La adaptación a la hipoxia en ratas protege la función metabólica endotelial pulmonar (actividad de ECA). |
| [8405086](https://pubmed.ncbi.nlm.nih.gov/8405086/) | 1993 | Sin clasificar | Eur J Pharmacol | Lisinopril mejora la recuperación durante la reoxigenación en cardiomiocitos cultivados. |

## Información de Mercado en Argentina

Las 11 autorizaciones registradas son de producto de un solo principio activo y están vigentes. El texto de indicación aprobada no está registrado en los datos locales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 7048 | TENSOPRIL | 10 mg comp. x 20 | No registrada en los datos locales |
| 564 | TENSOPRIL | 10 mg comp. x 40 | No registrada en los datos locales |
| 563 | TENSOPRIL | 5 mg comp. x 40 | No registrada en los datos locales |
| 3249 | ZESTRIL | 10 mg comp. x 60 | No registrada en los datos locales |
| 565 | TENSOPRIL | 20 mg comp. x 40 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (11 de las primeras 20 consultadas son de nivel moderado y 2 de nivel mayor; el total registrado es de 100):
  - Nivel mayor: citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - Nivel moderado: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol y preparados de limpieza intestinal.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (puntaje 0,9989) no cuenta con ensayos clínicos ni estudios directos en humanos, y la evidencia preclínica sugiere que la hipoxia actúa principalmente por la vía de la endotelina, lo que debilita el fundamento mecanístico. Se mantiene en espera.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción de lisinopril en circulación pulmonar hipóxica.
- Revisión dirigida de la literatura clínica sobre inhibidores de la ECA en hipertensión pulmonar asociada a enfermedad pulmonar/hipoxia.
- Estudios clínicos que evalúen directamente esta indicación.
- Obtención y análisis del prospecto aprobado por ANMAT para completar advertencias y contraindicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

