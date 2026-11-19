---
layout: default
title: Propranolol
parent: Solo Predicción del Modelo (L5)
nav_order: 219
evidence_level: L5
indication_count: 4
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
last_modified_at: 2026-10-30
description: "Propranolol: nueva indicación predicha, miopatía distal tipo Tateyama (distal myopathy, Tateyama type) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Propranolol
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

## Propranolol: bloqueador beta-adrenérgico no selectivo → miopatía distal tipo Tateyama (distal myopathy, Tateyama type)
{: .text-alpha }

## Resumen en Una Frase

Propranolol es un bloqueador beta-adrenérgico no selectivo, comercializado actualmente en Argentina.
El modelo TxGNN predice que podría ser útil para **miopatía distal tipo Tateyama (distal myopathy, Tateyama type)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | miopatía distal tipo Tateyama (distal myopathy, Tateyama type) |
| Puntaje de Predicción TxGNN | 0,9940 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Propranolol (traducción no oficial): «No se ha establecido el mecanismo del efecto antihipertensivo del propranolol. Entre los factores que contribuyen a la acción antihipertensiva se encuentran: la disminución del gasto cardíaco, la inhibición de la liberación de renina por los riñones y la disminución del flujo simpático tónico desde los centros vasomotores del cerebro.» Texto original en inglés: "The mechanism of the antihypertensive effect of propranolol has not been established. Among factors that contribute to the antihypertensive action are: decreased cardiac output, inhibition of renin release by the kidneys, and diminution of tonic sympathetic nerve outflow from vasomotor centers in the brain." ([DailyMed: Inderal Xl (propranolol hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac196ff5-9215-402b-bc57-69aa87f8bade), versión del 2026-08-27; consultado el 2026-11-19). Por conocimiento general, propranolol bloquea de forma no selectiva los receptores beta-adrenérgicos.

La miopatía distal tipo Tateyama es un trastorno muscular raro. Con los datos disponibles no se identifica ninguna conexión farmacológica clara entre el bloqueo beta-adrenérgico y la fisiopatología de esta enfermedad.

Por ello, el puntaje elevado del modelo debe interpretarse solo como una señal computacional. El vínculo mecanístico es especulativo y requeriría validación biológica y estudios preclínicos antes de cualquier consideración clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Propranolol cuenta con autorizaciones vigentes en Argentina (todas de producto de un solo principio activo, fabricante Gador):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 12900 | PROPRANOLOL GADOR | 40 mg comp. x 100 | No registrada en los datos locales |
| 3910 | PROPRANOLOL GADOR | 80 mg comp. x 50 | No registrada en los datos locales |
| 9130 | PROPRANOLOL GADOR | 40 mg comp. x 50 | No registrada en los datos locales |
| 3908 | PROPRANOLOL GADOR | 10 mg comp. x 20 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se listan algunas de las principales):
  - Mayor: epinefrina.
  - Moderada: hidrocortisona, metescopolamina, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, budesonida, canagliflozina, clorpropamida, cimetidina, fosfato de calcio, acetato de calcio.
  - Menor: ácido ascórbico, ácido acetilsalicílico, óxido de magnesio.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, no hay un vínculo mecanístico respaldado por los datos y el nivel de evidencia es L5. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de propranolol y una hipótesis biológica que lo vincule con la miopatía distal tipo Tateyama.
- Estudios preclínicos que respalden la plausibilidad de la predicción.
- Revisión del prospecto aprobado en ANMAT para obtener advertencias y contraindicaciones.
- Evaluación de seguridad, en particular de las interacciones de riesgo mayor (p. ej., epinefrina).

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Inderal Xl (propranolol hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac196ff5-9215-402b-bc57-69aa87f8bade) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

