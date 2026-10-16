---
layout: default
title: Perindopril
parent: Evidencia Moderada (L3-L4)
nav_order: 210
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-13
description: "Perindopril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L4). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "PERINDOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Perindopril
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Perindopril: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (ECA), originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente no hay **ningún ensayo clínico** y solo **1 publicación** de relevancia indirecta que respalde esta dirección, por lo que la predicción se apoya prácticamente solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, perindopril es un inhibidor de la ECA: reduce la formación de angiotensina II y, con ello, la vasoconstricción y la activación del sistema renina-angiotensina-aldosterona (SRAA). Su eficacia en la hipertensión está comprobada, y mecanísticamente el bloqueo del SRAA podría ser aplicable al daño renal de origen hipertensivo.

La relación entre la indicación original y la nueva es estrecha: la enfermedad renal hipertensiva maligna es la afectación del riñón por una hipertensión grave. Es probable que el alto puntaje (0.998) refleje la cercanía de este diagnóstico con la indicación ya existente de hipertensión, más que evidencia independiente.

Hay además limitaciones importantes. La hipertensión maligna es una emergencia hipertensiva que suele manejarse con fármacos parenterales, por lo que un inhibidor de la ECA oral no es una opción de primera línea. La única publicación recuperada trata sobre la función de un riñón solitario tras nefrectomía por cáncer renal, y no sobre nefropatía hipertensiva maligna.

Otras predicciones del modelo (todas en estado "Hold"):
- **Hipertensión renovascular maligna** (99.77%, L5): plausible por ser un cuadro dependiente de renina, pero los inhibidores de la ECA pueden precipitar insuficiencia renal aguda en estenosis bilateral de arteria renal o de riñón solitario.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (99.75%, L4): solo hay estudios preclínicos en ratas hipóxicas (por ejemplo, PMID 11282121 y 10602319), sin evidencia en humanos, y las guías no respaldan los inhibidores de la ECA en este grupo.
- **Hipertensión pulmonar de mecanismo multifactorial poco claro** (99.75%, L5): vínculo inespecífico, sin ensayos ni literatura.
- **Síndrome de Braddock** (99.66%, L5): sin fundamento mecanístico evidente; el puntaje probablemente refleja cercanía en el grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Cohorte | Urologiia | Estado funcional del riñón solitario tras nefrectomía por cáncer renal; solo aporta contexto indirecto, no trata la nefropatía hipertensiva maligna |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42977 | COVERENE 10 | Comprimidos 10 mg x 30 | No especificada en los datos |
| 42976 | COVERENE | Comprimidos 5 mg x 30 | No especificada en los datos |
| 43975 | PRETERAX | Comprimidos recubiertos 2.5/0.625 mg x 30 | No especificada en los datos |
| 46415 | COVERAM 10/10 | Comprimidos 10/10 x 30 | No especificada en los datos |
| 46418 | PRETERAX 10 | Comprimidos recubiertos 10/2.5 mg x 30 | No especificada en los datos |

Se muestran 5 de las 13 autorizaciones vigentes, todas del laboratorio Servier. Incluyen presentaciones de perindopril solo y en combinación con indapamida, amlodipina o ambas (COVERENE, PRETERAX, COVERAM, TRIPLIXAM).

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (adquirido, hereditario, inducido por bloqueadores del SRAA y no histaminérgico), neutropenia, agranulocitosis, trastornos hipotensivos, enfermedades del tejido conectivo, enfermedades óseas y del cartílago, y obstrucción de la arteria renal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel **mayor** incluyen citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia). Entre las de nivel moderado figuran corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropión y dronabinol.
- **Relevancia para las indicaciones predichas**: la literatura recuperada incluye reportes de casos de angioedema grave por inhibidores de la ECA, y la hipertensión renovascular conlleva riesgo de insuficiencia renal aguda.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no estuvieron disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cinco predicciones carecen de ensayos clínicos y la evidencia disponible es nula, indirecta o solo preclínica (nivel L4–L5). Además, el puntaje alto del modelo parece reflejar cercanía con la indicación original de hipertensión, y existen preocupaciones de seguridad renal y de manejo clínico (emergencia hipertensiva) que superan el respaldo actual.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del farmaco desde DrugBank
- Advertencias y contraindicaciones del prospecto oficial de ANMAT, necesarias para el tamizaje de seguridad
- Literatura clínica específica sobre inhibidores de la ECA en nefropatía hipertensiva maligna (estudios observacionales o ensayos)
- Evaluación del riesgo renal (estenosis de arteria renal, riñón solitario) y de hiperpotasemia antes de cualquier ensayo
- Verificación de compatibilidad de vía de administración y de similitud con la indicación original, hoy pendientes
- Revisión de las indicaciones aprobadas localmente, ya que los textos de indicación están vacíos en los datos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

