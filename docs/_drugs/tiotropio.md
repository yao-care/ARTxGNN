---
layout: default
title: Tiotropio
parent: Solo Predicción del Modelo (L5)
nav_order: 345
evidence_level: L5
indication_count: 4
drugbank_id: DB01409
monitor_inn: "Tiotropium"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
last_modified_at: 2026-11-20
description: "Tiotropio: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Tiotropio
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Tiotropio: malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Tiotropio es un antagonista muscarínico de acción prolongada (receptor M3) que se administra por inhalación con el dispositivo Respimat.
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria (respiratory malformation)**, con un puntaje de 0.9995.
Los datos compilados incluyen **3 ensayos clínicos** (todos en fibrosis quística, no en malformaciones respiratorias) y **5 publicaciones** sin estudios que evalúen directamente esta condición, por lo que la evidencia directa es nula.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tiotropio (traducción no oficial): «El tiotropio es un agente antimuscarínico de acción prolongada, al que a menudo se denomina anticolinérgico. Tiene una afinidad similar por los subtipos de receptores muscarínicos, de M 1 a M 5. En las vías respiratorias, ejerce efectos farmacológicos mediante la inhibición de los receptores M 3 del músculo liso, lo que produce broncodilatación.» Texto original en inglés: "Tiotropium is a long-acting, antimuscarinic agent, which is often referred to as an anticholinergic. It has similar affinity to the subtypes of muscarinic receptors, M 1 to M 5. In the airways, it exhibits pharmacological effects through inhibition of M 3 -receptors at the smooth muscle leading to bronchodilation." ([DailyMed: Spiriva Handihaler (tiotropium bromide) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=820839ef-e53d-47e8-a3b9-d911ff92e6a9), versión del 2025-11-10; consultado el 2026-11-19). Según el conocimiento general de la clase, el tiotropio bloquea el receptor muscarínico M3, relaja el músculo liso de la vía aérea y reduce la broncoconstricción colinérgica y la secreción de moco.

Mecanísticamente, esto podría aliviar una obstrucción secundaria del flujo de aire o una hiperreactividad bronquial en algunos trastornos estructurales de la vía aérea o de la pared torácica. Sin embargo, "malformación respiratoria" es una categoría amplia y heterogénea, y ningún ensayo ni publicación disponible muestra eficacia del tiotropio en una cohorte con malformaciones congénitas o estructurales.

El puntaje alto (0.9995) probablemente refleja la cercanía en la red del modelo con enfermedades obstructivas de la vía aérea, y no evidencia en poblaciones con malformaciones. Por ello se trata de una hipótesis de investigación.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Fase 3 | Completado | 464 | Tiotropio 5 mcg una vez al día vía Respimat vs placebo durante 12 semanas en fibrosis quística; confirma eficacia y seguridad. Apoyo indirecto de broncodilatación en obstrucción. |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Fase 2 | Completado | 510 | Dos dosis de tiotropio (2,5 y 5 mcg) vs placebo durante 12 semanas en fibrosis quística; evalúa función pulmonar, seguridad y farmacocinética. |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Fase 1 | Completado | 113 | Seguridad, tolerabilidad y farmacocinética de dosis únicas y múltiples (28 días) en pacientes pediátricos y adultos con fibrosis quística. |

Ninguno de estos ensayos estudia malformaciones respiratorias; aportan solo apoyo indirecto sobre seguridad y broncodilatación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | ECA | Respiratory Medicine | Tiotropio/olodaterol reduce la hiperinsuflación y podría mejorar las respuestas cardiocirculatorias al esfuerzo en EPOC. |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Revisión | Int J Chron Obstruct Pulmon Dis | Papel clínico de la doble broncodilatación (indacaterol-glicopirronio) en EPOC. |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohorte | Respiratory Medicine | El batido ciliar nasal está disminuido en sujetos con EPOC. |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Reporte de caso | Rev Fac Cienc Med (Córdoba) | COVID-19 en un paciente joven con pectus excavatum, una alteración de la pared torácica. |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Preclínico | Chem Biol Interact | Mecanismos de la disfunción ventilatoria por desregulación colinérgica en ratones expuestos a un agente neurotóxico. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45181 | SPIRIVA RESPIMAT | Solución para inhalación x 30 dosis + inhalador | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe el tiotropio directamente en malformaciones respiratorias; los ensayos disponibles son en fibrosis quística y la literatura trata sobre EPOC u otros temas. El puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Definir qué tipo de malformación respiratoria y qué componente obstructivo reversible se pretende tratar
- Datos del mecanismo de acción y de seguridad (advertencias y contraindicaciones del prospecto de ANMAT)
- Estudios exploratorios en una cohorte con malformación respiratoria antes de considerar ensayos clínicos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Spiriva Handihaler (tiotropium bromide) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=820839ef-e53d-47e8-a3b9-d911ff92e6a9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

