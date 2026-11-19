---
layout: default
title: Bisoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 58
evidence_level: L5
indication_count: 4
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Bisoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Bisoprolol
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

## Bisoprolol: bloqueante beta-1 adrenérgico selectivo → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Bisoprolol es un bloqueante beta-1 adrenérgico selectivo comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Bisoprolol (traducción no oficial): «El FUMARATO DE BISOPROLOL es un bloqueante de los adrenorreceptores beta 1 -selectivo (cardioselectivo) sin actividad estabilizadora de membrana ni actividad simpaticomimética intrínseca significativas en su intervalo de dosis terapéuticas. Sin embargo, la cardioselectividad no es absoluta y, a dosis más altas (≥ 20 mg), el fumarato de bisoprolol también inhibe los adrenorreceptores beta 2 , localizados principalmente en la musculatura bronquial y vascular; por lo tanto, para conservar la selectividad es importante utilizar la dosis eficaz más baja.» Texto original en inglés: "BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose." ([DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e), versión del 2026-11-11; consultado el 2026-11-19). Por su clase conocida, bisoprolol es un bloqueante beta-1 selectivo: reduce la liberación de renina y el gasto cardíaco, lo que disminuye la presión arterial.

La enfermedad renal hipertensiva maligna se produce en el contexto de una elevación grave de la presión arterial, por lo que existe un vínculo conceptual plausible con un fármaco que reduce la presión. Sin embargo, no se aportaron ensayos ni literatura que lo confirmen.

La hipertensión maligna es una emergencia hipertensiva que suele tratarse con fármacos intravenosos (por ejemplo labetalol, nicardipino, nitroprusiato) y bloqueantes del sistema renina-angiotensina. El bisoprolol oral no sería una terapia primaria. El puntaje alto (0,9994) probablemente refleja la cercanía con el término de hipertensión en el modelo, y no evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran al menos 20 autorizaciones vigentes (la lista puede ser parcial). Las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55671 | PROBLOCK | 5 mg comprimidos recubiertos x 30 | No registrada en los datos locales |
| 57506 | PROBLOCK | 10 mg comprimidos recubiertos x 30 | No registrada en los datos locales |
| 25417 | CORBIS | 10 mg comprimidos recubiertos x 30 | No registrada en los datos locales |
| 53329 | BISOPIL | 2,5 mg comprimidos recubiertos x 30 | No registrada en los datos locales |
| 55925 | BISOPROLOL TEVA | 5 mg comprimidos x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron interacciones de nivel moderado, entre otras, con epinefrina, hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, bupropión, morfina, atropina, hiosciamina, metescopolamina, acetohexamida y sales de calcio (acetato, carbonato, citrato, gluconato). También se registran interacciones leves con ácido acetilsalicílico, hidróxido de aluminio y attapulgita.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo, sin ensayos ni publicaciones que estudien esta enfermedad. Además, el manejo estándar de la hipertensión maligna usa otros fármacos, por lo que el bisoprolol oral no sería una opción principal.

**Para avanzar se necesita:**
- Estudios clínicos o literatura que evalúen bisoprolol en enfermedad renal hipertensiva maligna
- Datos del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT
- Evaluación del papel de un bloqueante beta-1 oral frente a las terapias estándar de esta emergencia hipertensiva

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

