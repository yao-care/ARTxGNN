---
layout: default
title: Terazosin
parent: Solo Predicción del Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
monitor_inn: "terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
last_modified_at: 2026-11-24
description: "Terazosin: nueva indicación predicha, hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 18 (en el listado vigente: 18)"
---

# Terazosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Terazosina: bloqueante alfa-1 adrenérgico → hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Terazosina es un bloqueante alfa-1 adrenérgico que se comercializa en Argentina. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0,9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (18 de 18) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 18 (vigentes: 18) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Terazosin (traducción no oficial): «Hiperplasia prostática benigna Los síntomas asociados a la hiperplasia prostática benigna (HPB) están relacionados con la obstrucción del tracto de salida de la vejiga, que consta de dos componentes subyacentes: estático y dinámico. El componente estático está relacionado con un aumento del tamaño de la próstata causado, en parte, por una proliferación de células de músculo liso en el estroma prostático. […] El bloqueo del receptor alfa-1 disminuye la resistencia uretral y puede aliviar la obstrucción de los síntomas de la HPB y mejorar el flujo urinario Hipertensión El mecanismo de acción de la terazosina es el bloqueo selectivo del subtipo alfa-1 de los receptores adrenérgicos.» Texto original en inglés: "Benign Prostatic Hyperplasia The symptoms associated with benign prostatic hyperplasia (BPH) are related to bladder outlet obstruction, which is comprised of two underlying components: static and dynamic. The static component is related to an increase in prostate size caused, in part by a proliferation of smooth muscle cells in the prostatic stroma. […] Blockade of the alpha-1 receptor decreases urethral resistance and may relieve the obstruction of BPH symptoms and improve urine flow Hypertension The mechanism of action of terazosin is selective blockade of the alpha-1 subtype of adrenergic receptors." ([DailyMed: Tezruly (terazosin) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69582e0c-6569-490c-8c14-999f3750336f), versión del 2025-04-18; consultado el 2026-11-19). Por su clase, la terazosina bloquea los receptores alfa-1 adrenérgicos, lo que produce vasodilatación y relajación del músculo liso.

Un vínculo con el cuero cabelludo solo sería plausible a través de una mayor perfusión de los folículos, como ocurre con otros agentes vasoactivos. Esta hipótesis es especulativa y no cuenta con datos que la respalden.

Además, la hipotricosis simple es un trastorno genético hereditario. Un vasodilatador sintomático difícilmente modificaría su patología de base. Por ello, el puntaje alto del modelo debe interpretarse con cautela: es una señal para generar hipótesis, no una demostración de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Todas las autorizaciones registradas (18) son de productos de un solo principio activo y están vigentes. La lista siguiente muestra las 5 principales; el texto de indicación aprobada no figura en los datos locales.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 32798 | ANDRIN | 2 mg comp.x 30 | Casasco | Vigente |
| 34232 | GERIPROST | 10 mg comp.ran.x 20 | Teva Argentina | Vigente |
| 16334 | FOSFOMIK | 5 mg comp.birran.x 20 | Finadiet | Vigente |
| 18283 | BLAVIN | 2 mg comp.x 30 | Baliarda | Vigente |
| 24737 | BENAPROST | 5 mg comp.x 28 | Bagó | Vigente |

La tabla muestra 5 de los 18 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 137 interacciones en total. Entre las de nivel moderado figuran corticoides (hidrocortisona, dexametasona, betametasona, budesonida, prednisona, prednisolona, triamcinolona), morfina y opio, bupropión, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina) y cannabinoides (dronabinol, nabilona).
- No se dispone de texto de prospecto sobre advertencias ni contraindicaciones; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, el mecanismo propuesto es especulativo y la enfermedad es de origen genético. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen el efecto de la terazosina sobre el folículo piloso y la perfusión del cuero cabelludo
- Datos del mecanismo de acción del fármaco
- Texto de advertencias y contraindicaciones del prospecto de ANMAT
- Definir si una vía de administración distinta de la oral sería necesaria para un efecto local en el cuero cabelludo

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tezruly (terazosin) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69582e0c-6569-490c-8c14-999f3750336f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

