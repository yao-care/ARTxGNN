---
layout: default
title: Propafenona
parent: Solo Predicción del Modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 6
drugbank_id: DB01182
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
last_modified_at: 2026-11-24
description: "Propafenona: nueva indicación predicha, trastorno afectivo bipolar maníaco (manic bipolar affective disorder) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Propafenona
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

## Propafenona: trastorno afectivo bipolar maníaco (manic bipolar affective disorder)
{: .text-alpha }

## Resumen en Una Frase

Propafenona es un antiarrítmico que se comercializa en Argentina bajo la marca Normorytmin.
El modelo TxGNN predice que podría ser efectivo para **trastorno afectivo bipolar maníaco (manic bipolar affective disorder)**, pero no hay ensayos clínicos y las **3 publicaciones** disponibles son un caso clínico de manía provocada por propafenona, un caso de psicosis por interacción con venlafaxina y una revisión de interacciones; es decir, señales de daño y no de beneficio.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno afectivo bipolar maníaco (manic bipolar affective disorder) |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Propafenona (traducción no oficial): «La propafenona es un fármaco antiarrítmico de clase 1C con efectos anestésicos locales y una acción estabilizadora directa sobre las membranas miocárdicas. El efecto electrofisiológico de la propafenona se manifiesta en una reducción de la velocidad de ascenso (fase 0) del potencial de acción monofásico.» Texto original en inglés: "Propafenone is a Class 1C antiarrhythmic drug with local anesthetic effects, and a direct stabilizing action on myocardial membranes. The electrophysiological effect of propafenone manifests itself in a reduction of upstroke velocity (Phase 0) of the monophasic action potential." ([DailyMed: propafenone hydrochloride prescribing information, Northstar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2ecd6452-ccc3-493f-9a4a-69f0fbf67a42), versión del 2026-06-04; consultado el 2026-11-19). Por conocimiento general, la propafenona es un antiarrítmico de clase 1C (bloqueante de canales de sodio) con cierta actividad betabloqueante.

No se conoce un mecanismo establecido que vincule este perfil con la estabilización del ánimo. Un caso publicado de manía asociada a propafenona sugiere que el fármaco podría tener efectos sobre el estado de ánimo, pero en el sentido de provocar manía, no de tratarla.

No debe interpretarse como indicio de beneficio.

**Nota sobre el nivel de evidencia:** ninguna publicación estudia a la propafenona como tratamiento de esta enfermedad; por ello el nivel se fija en L5, aunque existan reportes de eventos adversos relacionados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacological Reports | Analiza interacciones dañinas entre antipsicóticos y fármacos cardiovasculares en pacientes con trastorno bipolar o esquizofrenia y comorbilidad cardiovascular. |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Reporte de caso | J Clin Psychiatry | Caso de manía secundaria a propafenona; se plantea que podría tener efectos afectivos adversos. |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Reporte de caso | Int J Psychiatry Med | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar. |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 7781 | NORMORYTMIN | 150 mg comp.rec.x 50 | Abbott EPD | Vigente |
| 7783 | NORMORYTMIN | 300 mg comp.rec.x 50 | Abbott EPD | Vigente |
| 4652 | NORMORYTMIN | 150 mg comp.rec.x 20 | Abbott EPD | Vigente |
| 4653 | NORMORYTMIN | 300 mg comp.rec.x 20 | Abbott EPD | Vigente |

La tabla muestra los 4 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las publicaciones disponibles describen manía inducida por propafenona y toxicidad neuropsiquiátrica por interacción con venlafaxina, lo que apunta a posible daño en esta población.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo. La literatura disponible señala riesgo de manía y de interacciones, no beneficio, y no existe un mecanismo plausible que respalde el uso en trastorno bipolar maníaco.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto de ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos o clínicos que evalúen directamente la propafenona en manía
- Evaluación del riesgo proarrítmico y de interacciones con estabilizadores del ánimo y antipsicóticos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: propafenone hydrochloride prescribing information, Northstar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2ecd6452-ccc3-493f-9a4a-69f0fbf67a42) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

