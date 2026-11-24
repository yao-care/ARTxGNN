---
layout: default
title: Clortalidona
parent: Solo Predicción del Modelo (L5)
nav_order: 123
evidence_level: L5
indication_count: 9
drugbank_id: DB00310
monitor_inn: "Chlorthalidone"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
last_modified_at: 2026-11-24
description: "Clortalidona: nueva indicación predicha, Glaucoma hereditario primario (primary hereditary glaucoma) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 7 (en el listado vigente: 7)"
---

# Clortalidona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Clortalidona: Glaucoma hereditario primario (primary hereditary glaucoma)
{: .text-alpha }

## Resumen en Una Frase

Clortalidona es un diurético de tipo tiazídico que se comercializa en Argentina; los datos locales no registran el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser útil para **glaucoma hereditario primario (primary hereditary glaucoma)**.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se trata solo de una hipótesis del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Glaucoma hereditario primario (primary hereditary glaucoma) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clortalidona (traducción no oficial): «La clortalidona es un diurético oral de acción prolongada con actividad antihipertensiva. Los efectos diuréticos de la clortalidona y de los diuréticos benzotiadiazínicos (tiazídicos) parecen surgir de mecanismos similares, y el efecto máximo de la clortalidona y el de las tiazidas parecen ser similares.» Texto original en inglés: "Chlorthalidone is a long-acting oral diuretic with antihypertensive activity. The diuretic effects of chlorthalidone and the benzothiadiazine (thiazide) diuretics appear to arise from similar mechanisms and the maximal effect of chlorthalidone and the thiazides appear to be similar." ([DailyMed: Thalitone (chlorthalidone) prescribing information, Casper Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc5a0299-115b-4e60-bb3f-c75a95c51c15), versión del 2026-06-25; consultado el 2026-11-19). Clortalidona es un diurético de tipo tiazídico. Se sabe que actúa sobre el cotransportador de sodio y cloro del túbulo distal, y reduce el volumen de líquido corporal.

Un vínculo posible, pero no demostrado, sería un efecto pequeño sobre la presión intraocular o sobre el equilibrio de líquidos. Sin embargo, el glaucoma hereditario primario tiene una base genética y estructural en la malla trabecular y el ángulo de drenaje. Un diurético sistémico difícilmente corrija esa alteración.

El puntaje alto del modelo (0,9992) probablemente refleje patrones internos del modelo y no una relación biológica comprobada. No hay estudios que lo respalden, y la relación mecanística con el uso original sigue pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay 7 autorizaciones vigentes, todas de producto de un solo principio activo. Se listan las 5 principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 58994 | EURETICO | 25 mg comp.x 30 | Casasco | Vigente |
| 36177 | EURETICO | 50 mg comp.x 30 | Casasco | Vigente |
| 10758 | BEMPLAS | comp.x 30 | Casasco | Vigente |
| 12200 | PRENORETIC | 100 mg comp.x 56 | AstraZeneca | Vigente |
| 12201 | PRENORETIC | 50 mg comp.x 56 | AstraZeneca | Vigente |

La tabla muestra 5 de los 7 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura sobre glaucoma hereditario primario. El mecanismo es poco plausible para una enfermedad de origen genético y estructural, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de clortalidona.
- Estudios preclínicos o clínicos que evalúen el efecto de clortalidona sobre la presión intraocular.
- Revisión de las advertencias y contraindicaciones del prospecto de ANMAT.
- Revisión por un oftalmólogo para decidir si la hipótesis merece estudiarse.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Thalitone (chlorthalidone) prescribing information, Casper Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc5a0299-115b-4e60-bb3f-c75a95c51c15) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

