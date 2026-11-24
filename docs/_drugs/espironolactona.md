---
layout: default
title: Espironolactona
parent: Solo Predicción del Modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 2
drugbank_id: DB00421
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
last_modified_at: 2026-11-24
description: "Espironolactona: nueva indicación predicha, hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Espironolactona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Espironolactona: hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Espironolactona es un fármaco comercializado en Argentina en múltiples presentaciones de un solo principio activo.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)**, con un puntaje de 0.9926.
Actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección, por lo que se trata solo de una hipótesis computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Espironolactona (traducción no oficial): «La espironolactona y sus metabolitos activos son antagonistas farmacológicos específicos de la aldosterona, que actúan principalmente mediante la unión competitiva a los receptores en el sitio de intercambio sodio-potasio dependiente de aldosterona en el túbulo contorneado distal renal. La espironolactona provoca la excreción de mayores cantidades de sodio y agua, mientras que el potasio se retiene.» Texto original en inglés: "Spironolactone and its active metabolites are specific pharmacologic antagonists of aldosterone, acting primarily through competitive binding of receptors at the aldosterone-dependent sodium-potassium exchange site in the distal convoluted renal tubule. Spironolactone causes increased amounts of sodium and water to be excreted, while potassium is retained." ([DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc), versión del 2025-11-28; consultado el 2026-11-19). Según la información conocida, la espironolactona es un antagonista del receptor de mineralocorticoides que además bloquea el receptor de andrógenos y reduce la síntesis androgénica. Por esta actividad antiandrogénica se usa fuera de indicación en la pérdida de cabello de patrón femenino.

La hipotricosis simple es un trastorno hereditario raro de pérdida de cabello, asociado sobre todo a genes como CDSN, APCDD1 y RPL21, y no es principalmente andrógeno-dependiente. Por ello, el mecanismo antiandrogénico no aborda claramente la patología genética subyacente.

El puntaje alto probablemente refleja la cercanía del fármaco con fenotipos de pérdida de cabello en el modelo, y no evidencia específica de esta enfermedad. El vínculo mecanístico es plausible pero no verificado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones vigentes de productos de un solo principio activo (la lista puede ser parcial). Principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 37124 | REDIUN-E 25 | 25 mg comp.ran.x 30 | Baliarda | Vigente |
| 36476 | ESPIRONOLACTONA DENVER FARMA | 25 mg comp.x 30 | Denver Farma | Vigente |
| 36969 | DRIMUX A | 50 mg comp.x 30 | Gador | Vigente |
| 31634 | LANX | 100 mg comp.x 30 | Elea | Vigente |
| 18719 | ALDACTONE A | 25 mg comp.x 30 | Pfizer | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones que estudien directamente esta enfermedad, y el mecanismo antiandrogénico no se ajusta claramente a una alteración hereditaria no androgénica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar estudios clínicos o preclínicos que evalúen directamente la hipotricosis simple del cuero cabelludo
- Evaluar la compatibilidad de vía de administración, dado que las presentaciones locales son orales

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

