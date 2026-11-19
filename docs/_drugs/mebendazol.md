---
layout: default
title: Mebendazol
parent: Solo Predicción del Modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 1
drugbank_id: DB00643
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
last_modified_at: 2026-11-20
description: "Mebendazol: nueva indicación predicha, acné (acne (disease)) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 11 (en el listado vigente: 11)"
---

# Mebendazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Mebendazol: acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Mebendazol es un antihelmíntico del grupo de los bencimidazoles que actúa sobre la tubulina del parásito.
El modelo TxGNN predice que podría ser efectivo para **acné (acne (disease))**, pero no hay ensayos clínicos registrados y solo se dispone de **1 publicación**, un reporte de caso sobre esparganosis en el que el acné aparece solo como descripción de las lesiones cutáneas. No respalda la predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | acné (acne (disease)) |
| Puntaje de Prediccion TxGNN | 0.9920 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (11 de 11) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Por ahora, la predicción no tiene una base mecanística creíble. Mebendazol es un antihelmíntico bencimidazólico que se une a la beta-tubulina del parásito e inhibe la polimerización de los microtúbulos. Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Mebendazol (traducción no oficial): «El mebendazol, un bencimidazol, es un antihelmíntico. […] El mebendazol interfiere con la formación de tubulina celular en el helminto y causa cambios degenerativos ultraestructurales en su intestino. Como resultado, se alteran su captación de glucosa y sus funciones digestivas y reproductivas, lo que conduce a la inmovilización, la inhibición de la producción de huevos y la muerte del helminto.» Texto original en inglés: "Mebendazole, a benzimidazole, is an anthelmintic. […] Mebendazole interferes with cellular tubulin formation in the helminth and causes ultrastructural degenerative changes in its intestine. As a result, its glucose uptake and the digestive and reproductive functions are disrupted, leading to immobilization, inhibition of egg production and death of the helminth." ([DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f), versión del 2021-10-05; consultado el 2026-11-19).

La patogenia del acné implica producción excesiva de sebo, hiperqueratinización folicular, colonización por *Cutibacterium acnes* e inflamación. Ninguno de estos procesos es un blanco conocido de la inhibición de tubulina.

El puntaje de 0,9920 es una predicción basada en el modelo y no está respaldado por datos farmacológicos ni clínicos. Por eso debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Reporte de caso | The American Journal of Tropical Medicine and Hygiene | Primer caso de esparganosis proliferativa humana en el hemisferio sur (Venezuela). El paciente presentaba lesiones nodulares y papulares "similares al acné", abscesos subcutáneos, anemia y eosinofilia. No estudia el acné como enfermedad ni evalúa mebendazol para tratarlo. |

## Información de Mercado en Argentina

Mebendazol se comercializa en Argentina con 11 autorizaciones vigentes de productos de un solo principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 12138 | MEBUTAR 200 | Suspensión x 30 ml | — |
| 4567 | NEMASOLE AD | Comprimidos x 6 | — |
| 30667 | MEBENDAZOL FABRA | 500 mg, comprimidos x 6 | — |
| 45488 | TRU M | 200 mg, comprimidos x 6 | — |
| 22451 | NEMASOLE 200 | Comprimidos x 6 | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen mebendazol en acné, y no se identifica un vínculo mecanístico creíble. La única publicación disponible es un reporte de caso que no aborda el tema. El nivel de evidencia es L5, es decir, solo predicción del modelo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de mebendazol y su posible relevancia en la patogenia del acné
- Estudios preclínicos o clínicos que evalúen directamente mebendazol en acné
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT para el análisis de seguridad

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

