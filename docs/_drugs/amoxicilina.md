---
layout: default
title: Amoxicilina
parent: Solo Predicción del Modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 8
drugbank_id: DB01060
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-24
description: "Amoxicilina: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Amoxicilina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Amoxicilina: hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico que actúa sobre bacterias. El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amoxicilina (traducción no oficial): «La amoxicilina es un fármaco antibacteriano. […] La amoxicilina es similar a la penicilina en su acción bactericida contra las bacterias sensibles durante la fase de multiplicación activa. Actúa mediante la inhibición de la biosíntesis de la pared celular, lo que provoca la muerte de las bacterias.» Texto original en inglés: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), versión del 2026-11-13; consultado el 2026-11-19). Por conocimiento general, la amoxicilina es un betalactámico que interfiere con la síntesis de la pared celular bacteriana.

La hiperamilasemia es un hallazgo de laboratorio (de origen pancreático o salival) y no una enfermedad infecciosa. No se identificó ningún mecanismo plausible que conecte la acción antibacteriana de la amoxicilina con la regulación de la amilasa.

La predicción debe considerarse una hipótesis sin fundamento mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran al menos 20 autorizaciones vigentes de productos de amoxicilina como único principio activo (la lista puede ser parcial). Se muestran 5 de ellas:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 10482 | AMOXICLER 500 | comp.x 16 | Monserrat | Vigente |
| 15588 | AMOXICILINA FECOFAR | 500 mg jbe.x 90 ml | Fecofar | Vigente |
| 19845 | DARZITIL | 500 mg jbe.x 120 ml | Fabra | Vigente |
| 37674 | AMOXI 500 MAR | 500 mg susp.ext.x 150 ml | Mar | Vigente |
| 37114 | DARZITIL | 500 mg comp.x 21 | Fabra | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, carece de mecanismo plausible y la hiperamilasemia no es una condición tratable con un antibacteriano. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la amoxicilina
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Una hipótesis biológica que justifique la relación con la amilasa, antes de considerar cualquier estudio

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

