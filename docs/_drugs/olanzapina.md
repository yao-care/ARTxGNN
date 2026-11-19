---
layout: default
title: Olanzapina
parent: Solo Predicción del Modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 2
drugbank_id: DB00334
monitor_inn: "Olanzapine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
last_modified_at: 2026-11-20
description: "Olanzapina: nueva indicación predicha, torticolis paroxística benigna de la infancia (benign paroxysmal torticollis of infancy) (nivel de evidencia L5)."
---

# Olanzapina
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

## Olanzapina: torticolis paroxística benigna de la infancia (benign paroxysmal torticollis of infancy)
{: .text-alpha }

## Resumen en Una Frase

Olanzapina es un antipsicótico que cuenta con múltiples autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser efectivo para **torticolis paroxística benigna de la infancia (benign paroxysmal torticollis of infancy)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | torticolis paroxística benigna de la infancia (benign paroxysmal torticollis of infancy) |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Olanzapina (traducción no oficial): «Se desconoce el mecanismo de acción de la olanzapina en las indicaciones enumeradas. Sin embargo, la eficacia de la olanzapina en la esquizofrenia podría estar mediada por una combinación de antagonismo de los receptores de dopamina y de serotonina tipo 2 (5HT 2 ).» Texto original en inglés: "The mechanism of action of olanzapine, in the listed indications, is unclear. However, the efficacy of olanzapine in schizophrenia could be mediated through a combination of dopamine and serotonin type 2 (5HT 2 ) antagonism." ([DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c), versión del 2026-10-26; consultado el 2026-11-19). Según la información conocida, olanzapina actúa como antagonista de los receptores dopaminérgicos D2 y serotoninérgicos 5-HT2A.

La torticolis paroxística benigna de la infancia es un trastorno pediátrico raro, relacionado con canalopatías (a menudo vinculado a CACNA1A), que suele resolverse de forma espontánea. La predicción parece originarse en la cercanía dentro de la red de relaciones con otros trastornos neurológicos o del movimiento, y no en una justificación farmacológica sólida.

El antagonismo D2/5-HT2A de olanzapina no tiene un papel establecido en esta condición. Además, la exposición a antipsicóticos en lactantes conlleva un riesgo importante de reacciones distónicas agudas y otros efectos adversos. Como el cuadro es autolimitado, la relación riesgo-beneficio es desfavorable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se identificaron al menos 20 autorizaciones, todas vigentes y de producto de un solo principio activo; la lista puede ser parcial. Principales registros:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43521 | APSICO | 5 mg comprimidos recubiertos x 28 | — |
| 61891 | MIDAX | 2,5 mg comprimidos x 28 | — |
| 48279 | OLANZAPINA ROSPAW | 10 mg comprimidos x 28 | — |
| 47583 | ROLANZAX 10 | 10 mg comprimidos recubiertos x 28 | — |
| 52689 | ONOTRAN | 10 mg comprimidos recubiertos x 28 | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como advertencia contextual del análisis: el uso de antipsicóticos en lactantes conlleva riesgo de reacciones distónicas agudas, lo que es especialmente relevante en un cuadro que suele ser autolimitado.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación del modelo es alta, pero no existe ningún ensayo ni publicación que estudie olanzapina en esta enfermedad. La relación riesgo-beneficio en lactantes es desfavorable, dado que el cuadro suele resolverse solo.

**Para avanzar se necesita:**
- Evidencia directa (preclínica o clínica) sobre olanzapina en esta enfermedad
- Datos del mecanismo de acción que justifiquen un vínculo farmacológico
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones) y evaluación de seguridad pediátrica

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

