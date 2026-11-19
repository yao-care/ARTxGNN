---
layout: default
title: Labetalol
parent: Solo Predicción del Modelo (L5)
nav_order: 172
evidence_level: L5
indication_count: 3
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
last_modified_at: 2026-11-20
description: "Labetalol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Labetalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Labetalol: bloqueador adrenérgico alfa-1 y beta no selectivo → Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Labetalol es un antagonista adrenérgico alfa-1 y beta no selectivo, utilizado como antihipertensivo.
El modelo TxGNN predice que podría ser efectivo para **Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, con un puntaje de 0.9908.
Actualmente no hay ensayos clínicos ni publicaciones que estudien directamente esta enfermedad, por lo que la evidencia se limita a la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9908 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Labetalol bloquea los receptores alfa-1 (reduce la resistencia vascular sistémica) y los receptores beta de forma no selectiva (reduce la frecuencia y la contractilidad cardíacas). Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Labetalol (traducción no oficial): «El labetalol tiene actividad bloqueante alfa1-adrenérgica competitiva y actividad bloqueante beta-adrenérgica competitiva. En el ser humano, se ha estimado que la relación entre el bloqueo alfa y el bloqueo beta es de aproximadamente 1:7 tras la administración intravenosa.» Texto original en inglés: "Labetalol has both competitive alpha1-adrenergic blocking and competitive beta-adrenergic blocking activity. In man, the ratio of alpha- to beta-blockade has been estimated to be approximately 1:7 following intravenous administration." ([DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55), versión del 2025-12-19; consultado el 2026-11-19).

La enfermedad renal hipertensiva maligna (nefroesclerosis maligna) es una complicación renal de la hipertensión grave. Por ello, es mecanísticamente plausible que reducir la presión arterial proteja el riñón.

Es importante matizar: esta predicción es esencialmente una extensión de su uso antihipertensivo y no un reposicionamiento en sentido estricto. El puntaje alto probablemente refleja la cercanía con la hipertensión, y no se ha demostrado un beneficio renal específico de labetalol en los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 30277 | BIASCOR | 200 mg comp. x 20 |
| 61054 | BIASCOR | 200 mg comp. x 60 |
| 51245 | BLOCAMINE | 200 mg comp. x 20 |
| 30278 | BIASCOR | 5 mg/ml amp. x 10 x 4 ml |

Las cuatro autorizaciones figuran como vigentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (se consultaron 100 interacciones; se listan las principales):
  - Gravedad mayor: epinefrina, dolasetrón.
  - Gravedad moderada: hidrocortisona, metescopolamina, hiosciamina, triamcinolona, morfina, atropina, dexametasona, betametasona, budesonida, canagliflozina, dapagliflozina, clorpropamida, cimetidina, diciclomina, fosfato de calcio, acetato de calcio.
  - Gravedad menor: ácido acetilsalicílico, óxido de magnesio.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que estudien directamente la enfermedad renal hipertensiva maligna con labetalol. El puntaje alto del modelo probablemente refleja la proximidad con la hipertensión y no un beneficio renal demostrado.

**Para avanzar se necesita:**
- Estudios clínicos u observacionales de labetalol con desenlaces renales en hipertensión maligna
- Datos de mecanismo de acción y de advertencias y contraindicaciones del prospecto de ANMAT
- Comparación con los antihipertensivos ya usados en esta condición, para determinar si aporta un valor adicional

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

