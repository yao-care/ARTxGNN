---
layout: default
title: Nebivolol
parent: Solo Predicción del Modelo (L5)
nav_order: 201
evidence_level: L5
indication_count: 4
monitor_inn: "NEBIVOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Nebivolol: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Nebivolol
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

## Nebivolol: betabloqueante β1 selectivo con vasodilatación mediada por óxido nítrico → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Nebivolol es un betabloqueante altamente selectivo para el receptor β1, con efecto vasodilatador mediado por óxido nítrico, comercializado en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que estudien directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Nebivolol (traducción no oficial): «El mecanismo de acción de la respuesta antihipertensiva de BYSTOLIC no se ha establecido de forma definitiva. Entre los posibles factores que pueden estar implicados se incluyen: disminución de la frecuencia cardíaca, disminución de la contractilidad miocárdica, disminución del flujo simpático tónico hacia la periferia desde los centros vasomotores cerebrales, supresión de la actividad de la renina y vasodilatación y disminución de la resistencia vascular periférica.» Texto original en inglés: "The mechanism of action of the antihypertensive response of BYSTOLIC has not been definitively established. Possible factors that may be involved include: decreased heart rate, decreased myocardial contractility, diminution of tonic sympathetic outflow to the periphery from cerebral vasomotor centers, suppression of renin activity and vasodilation and decreased peripheral vascular resistance." ([DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8), versión del 2024-08-01; consultado el 2026-11-19). Según la información conocida, nebivolol es un bloqueador β1 altamente selectivo que además promueve vasodilatación mediante la activación de la óxido nítrico sintasa endotelial (eNOS) y el agonismo sobre receptores β3. Se comercializa en Argentina como antihipertensivo.

Este perfil ofrece una justificación plausible para una enfermedad renal de origen hipertensivo: reducir la presión arterial y mejorar la función endotelial podría, en teoría, proteger el riñón. Sin embargo, la puntuación del modelo es únicamente una predicción computacional.

Hay que ser cautos: la hipertensión maligna con compromiso renal es una condición aguda y de alto riesgo, que habitualmente se maneja con fármacos intravenosos de acción rápida. No se aportaron ensayos ni literatura para esta indicación específica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El estado de mercado es **comercializado**. La lista de autorizaciones puede ser parcial (al menos 20 registros, todos vigentes). Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52016 | GADOCOR | 10 mg comp. ran. x 30 | No registrada en los datos locales |
| 56489 | NEBIVOLOL DENVER FARMA | 5 mg comp. x 28 | No registrada en los datos locales |
| 58881 | CORPRES 2.5 | 2,5 mg comp. x 60 | No registrada en los datos locales |
| 48494 | NIDIB | 5 mg comp. birran. x 28 | No registrada en los datos locales |
| 52551 | NIDIB | 10 mg comp. birran. x 28 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas, la mayoría son de nivel moderado, por ejemplo con epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, canagliflozina, dapagliflozina y clorpropamida. Las interacciones con ácido acetilsalicílico y óxido de magnesio son de nivel menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo computacional (L5), sin ensayos ni publicaciones que estudien esta enfermedad. Además, se trata de una condición aguda y grave que normalmente requiere tratamiento intravenoso, lo que limita la plausibilidad de una formulación oral.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen directamente nebivolol en enfermedad renal hipertensiva maligna
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de ANMAT
- Análisis de compatibilidad de vía de administración frente al manejo habitual (agentes intravenosos)
- Evaluación de seguridad en pacientes con compromiso renal agudo

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

