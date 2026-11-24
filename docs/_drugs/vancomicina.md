---
layout: default
title: Vancomicina
parent: Solo Predicción del Modelo (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
drugbank_id: DB00512
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
last_modified_at: 2026-11-24
description: "Vancomicina: nueva indicación predicha, Esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Vancomicina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Vancomicina: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Vancomicina es un antibiótico glucopéptido que actúa sobre la pared celular bacteriana y se comercializa en Argentina.
El modelo TxGNN predice que podría ser efectiva para **esclerodermia difusa (diffuse scleroderma)**, pero no hay ensayos clínicos y la única publicación vinculada es un reporte de caso sobre eritrodermia con sepsis, que no trata esta enfermedad.
La predicción se apoya únicamente en el modelo y no en estudios reales.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Vancomicina (traducción no oficial): «La vancomicina es un fármaco antibacteriano. […] La acción bactericida de la vancomicina se debe principalmente a la inhibición de la biosíntesis de la pared celular. Además, la vancomicina altera la permeabilidad de la membrana celular bacteriana y la síntesis de ARN.» Texto original en inglés: "Vancomycin is an antibacterial drug. […] The bactericidal action of vancomycin results primarily from inhibition of cell-wall biosynthesis. In addition, vancomycin alters bacterial-cell-membrane permeability and RNA synthesis." ([DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560), versión del 2026-08-19; consultado el 2026-11-19). Por el conocimiento farmacológico general, la vancomicina es un glucopéptido que inhibe la síntesis de la pared celular de bacterias Gram positivas.

Ese mecanismo no tiene relación conocida con la esclerodermia difusa (esclerosis sistémica), una enfermedad autoinmune y fibrosante. La vancomicina no tiene actividad antifibrótica ni inmunomoduladora conocida que sea relevante para ella.

Por lo tanto, la predicción no es plausible desde el punto de vista mecanístico. El puntaje alto (0,9992) parece ser un artefacto de la predicción del modelo y no refleja un beneficio clínico esperable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Reporte de caso | The American Journal of Case Reports | Caso de erupción exfoliativa difusa con sepsis y eosinofilia (posible eritrodermia) en un hombre de 56 años. No estudia esclerodermia ni evalúa vancomicina como tratamiento para ella. |

Ninguna publicación aborda directamente la esclerodermia difusa, por lo que el nivel de evidencia se mantiene en L5.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 15836 | VANCOMICINA FABRA | 1000 mg iny.f.a.x 1 | Fabra | Vigente |
| 15835 | VANCOMICINA FABRA | 500 mg iny.f.a.x 1 | Fabra | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Ambas autorizaciones son de producto único y están vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo clínico ni mecanístico: no hay ensayos, la única publicación no trata esclerodermia y el mecanismo conocido de la vancomicina no es plausible para esta enfermedad. El puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Evidencia directa (estudios preclínicos o clínicos) que evalúe vancomicina en esclerodermia difusa
- Una hipótesis mecanística fundamentada que justifique la relación
- Datos de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Datos del mecanismo de acción desde una fuente farmacológica de referencia

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

