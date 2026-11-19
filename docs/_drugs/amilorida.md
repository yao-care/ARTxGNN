---
layout: default
title: Amilorida
parent: Solo Predicción del Modelo (L5)
nav_order: 26
evidence_level: L5
indication_count: 5
drugbank_id: DB00594
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-16
description: "Amilorida: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 11 (en el listado vigente: 11)"
---

# Amilorida
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

## Amilorida: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Amilorida es un diurético ahorrador de potasio que actúa bloqueando el canal epitelial de sodio (ENaC).
El modelo TxGNN predice que podría ser útil para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (11 de 11) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amilorida (traducción no oficial): «El clorhidrato de amilorida es un fármaco ahorrador de potasio (antikaliurético) que posee una actividad natriurética, diurética y antihipertensiva débil (en comparación con los diuréticos tiazídicos). En algunos estudios clínicos, estos efectos han sido parcialmente aditivos a los efectos de los diuréticos tiazídicos.» Texto original en inglés: "Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies." ([DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68), versión del 2026-11-11; consultado el 2026-11-19). Según la información conocida, la amilorida bloquea el canal epitelial de sodio (ENaC) en el riñón, lo que favorece la eliminación de sodio y agua y reduce la pérdida de potasio. Se usa como diurético y antihipertensivo.

Mecanísticamente, el control del sodio y del volumen circulante podría ser relevante en el daño renal asociado a hipertensión grave. Sin embargo, el puntaje elevado (0,9982) corresponde solo a una predicción del modelo: no se aportaron ensayos clínicos ni literatura para esta enfermedad.

La hipertensión maligna con compromiso renal es una condición aguda y de alto riesgo. En ella, el riesgo de hiperpotasemia de la amilorida en presencia de insuficiencia renal es una preocupación de seguridad importante, por lo que la plausibilidad mecanística no es suficiente para apoyar su uso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

La amilorida se encuentra comercializada en Argentina, con 11 autorizaciones vigentes de productos de un solo principio activo (ninguna cancelada ni sin comercializar).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 41831 | DIUREX A 12.5 | 12.5/1.25 mg comp. x 30 |
| 542 | ERROLON A | comp. x 20 |
| 22138 | REN-UR | comp. x 20 |
| 22139 | REN-UR | comp. x 50 |
| 5385 | MODURETIC | comp. x 50 |

Se muestran las 5 primeras de 11 autorizaciones; las demás corresponden a DIUREX A 50, DIUREX A 25, MODURETIC (comp. x 30), ERROLON A (comp. x 50), REN-UR (comp. x 100) y HIDRENOX A.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como consideración general derivada de la evaluación de la predicción: la amilorida puede provocar hiperpotasemia, riesgo que aumenta en la insuficiencia renal, justamente el contexto de la enfermedad predicha.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel de evidencia L5), sin ensayos clínicos ni publicaciones sobre esta enfermedad, y con un riesgo de seguridad relevante (hiperpotasemia en compromiso renal).

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Revisión de literatura y de registros de ensayos específicos sobre la enfermedad renal hipertensiva maligna
- Evaluación del riesgo de hiperpotasemia en pacientes con deterioro de la función renal

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

