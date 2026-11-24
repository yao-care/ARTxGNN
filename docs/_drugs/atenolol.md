---
layout: default
title: Atenolol
parent: Solo Predicción del Modelo (L5)
nav_order: 36
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Atenolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Atenolol
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

## Atenolol: betabloqueante cardioselectivo (beta-1) → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Atenolol es un betabloqueante cardioselectivo (beta-1) utilizado como antihipertensivo y comercializado actualmente en Argentina.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Atenolol (traducción no oficial): «TENORMIN es un bloqueante de los receptores beta-adrenérgicos selectivo beta 1 (cardioselectivo) sin actividad estabilizadora de membrana ni actividad simpaticomimética intrínseca (agonista parcial). Sin embargo, este efecto preferencial no es absoluto y, a dosis más altas, TENORMIN inhibe los adrenorreceptores beta 2, localizados principalmente en la musculatura bronquial y vascular.» Texto original en inglés: "TENORMIN is a beta 1 -selective (cardioselective) beta-adrenergic receptor blocking agent without membrane stabilizing or intrinsic sympathomimetic (partial agonist) activities. This preferential effect is not absolute, however, and at higher doses, TENORMIN inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a), versión del 2025-09-18; consultado el 2026-11-19). Según la información farmacológica general, atenolol bloquea selectivamente los receptores beta-1, lo que reduce la frecuencia cardíaca, el gasto cardíaco y la liberación de renina.

Esa reducción de la presión arterial y de la actividad de la renina da un vínculo teórico con la enfermedad renal causada por hipertensión severa. Sin embargo, la puntuación del modelo es solo una predicción y el mecanismo no puede verificarse con los datos disponibles.

Además, la hipertensión maligna con compromiso renal suele manejarse con fármacos parenterales de acción rápida y bloqueo del sistema renina-angiotensina-aldosterona, por lo que el papel de un betabloqueante oral sería, como mucho, complementario y debe confirmarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran al menos 20 autorizaciones vigentes de productos con atenolol como único principio activo; la lista puede ser parcial. Se muestran las 5 principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 3849 | ATENOLOL GADOR | 100 mg comp.x 28 | Gador | Vigente |
| 32121 | ATENOLOL MICROSULES | 50 mg comp.x 28 | Microsules Arg. | Vigente |
| 59354 | VERICORDIN | 100 mg comp.x 60 | Lazar | Vigente |
| 35433 | PLENACOR 50 | 50 mg comp.x 60 | Bagó | Vigente |
| 34628 | ATENOLOL GADOR | 25 mg comp.x 30 | Gador | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (nivel moderado, entre otras): epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, acetohexamida, atropina, betametasona, budesonida y varias sales de calcio (acetato, carbonato, citrato, gluconato, lactato, fosfato). Con ácido acetilsalicílico, hidróxido de aluminio y attapulgita las interacciones son de nivel leve. Se identificaron 100 interacciones en total.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (0,9985), sin ensayos clínicos ni literatura sobre esta enfermedad; el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Revisión de la literatura clínica y fisiopatológica específica sobre betabloqueantes en nefropatía hipertensiva maligna
- Datos del mecanismo de acción y análisis de su vínculo con esta enfermedad
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Evaluación de seguridad renal e interacciones en pacientes con hipertensión severa, antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

