---
layout: default
title: Digoxina
parent: Solo Predicción del Modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 5
drugbank_id: DB00390
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-11-24
description: "Digoxina: nueva indicación predicha, Angina de Prinzmetal (Prinzmetal angina) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 5 (en el listado vigente: 5)"
---

# Digoxina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Digoxina: Angina de Prinzmetal (Prinzmetal angina)
{: .text-alpha }

## Resumen en Una Frase

Digoxina es un glucósido cardíaco que inhibe la bomba Na+/K+-ATPasa. El modelo TxGNN predice que podría ser efectivo para **Angina de Prinzmetal (Prinzmetal angina)**, pero no hay ensayos clínicos y solo se recuperó **1 publicación** (una revisión general sobre cronofarmacología del tratamiento antihipertensivo) que no estudia directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Angina de Prinzmetal (Prinzmetal angina) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 5) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Digoxina (traducción no oficial): «Todas las acciones de la digoxina están mediadas por sus efectos sobre la Na-K ATPasa. Esta enzima, la «bomba de sodio», se encarga de mantener el medio intracelular en todo el organismo, desplazando los iones sodio hacia el exterior de las células y los iones potasio hacia su interior.» Texto original en inglés: "All of digoxin’s actions are mediated through its effects on Na-K ATPase. This enzyme, the “sodium pump,” is responsible for maintaining the intracellular milieu throughout the body by moving sodium ions out of and potassium ions into cells." ([DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707), versión del 2025-10-17; consultado el 2026-11-19). Por conocimiento farmacológico general, la digoxina inhibe la Na+/K+-ATPasa y eleva el calcio intracelular, lo que aumenta la contractilidad del miocardio.

Con ese mecanismo, **no se identifica un vínculo creíble** con la angina de Prinzmetal. Esta enfermedad es de origen vasoespástico y se trata con vasodilatadores como los bloqueadores de los canales de calcio y los nitratos. La farmacología de la digoxina podría incluso aumentar el tono vascular y agravar teóricamente el vasoespasmo coronario, es decir, va en sentido contrario a la necesidad terapéutica.

El puntaje alto (0,9981) probablemente refleja cercanía en la red de asociaciones cardiovasculares compartidas y no una señal terapéutica real. Debe interpretarse como un resultado computacional sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Revisión | Acta physiologica et pharmacologica Bulgarica | Revisión sobre ritmos circadianos y cronofarmacología aplicada al tratamiento antihipertensivo. No estudia digoxina ni angina de Prinzmetal. |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 29874 | DIGOXINA LAFEDAR | 0.25 mg comp.x 40 | Lafedar | Vigente |
| 4370 | LANOXIN (DIGOXINA) | 0.25 mg comp.x 100 | Roemmers | Vigente |
| 29875 | DIGOXINA LAFEDAR | 75 mg gts.x 10 ml | Lafedar | Vigente |
| 9110 | LANOXIN (DIGOXINA) | 0.25 mg comp.x 50 | Roemmers | Vigente |
| 9109 | LANOXIN (DIGOXINA) | 0.25 mg comp.x 25 | Roemmers | Vigente |

La tabla muestra los 5 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones que estudien directamente el uso de digoxina en la angina de Prinzmetal, por lo que el nivel de evidencia es L5. Además, el mecanismo conocido de la digoxina podría empeorar el vasoespasmo coronario, por lo que la predicción carece de plausibilidad biológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una justificación mecanística creíble que explique por qué la digoxina no agravaría el vasoespasmo.
- Estudios preclínicos o clínicos que evalúen directamente la digoxina en la angina vasoespástica.
- Revisión del prospecto aprobado en ANMAT para completar la información de advertencias, contraindicaciones e interacciones.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

