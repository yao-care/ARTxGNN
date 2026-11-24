---
layout: default
title: Carvedilol
parent: Solo Predicción del Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 4
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Carvedilol: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Carvedilol
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

## Carvedilol: betabloqueante no selectivo con bloqueo alfa-1 → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con actividad bloqueante alfa-1, comercializado en Argentina con múltiples autorizaciones vigentes.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9955 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción. Según el conocimiento general, carvedilol bloquea los receptores beta y alfa-1 adrenérgicos, lo que produce un efecto antihipertensivo y vasodilatador.

Ese perfil ofrece una justificación plausible para una enfermedad renal asociada a hipertensión. Sin embargo, la hipertensión maligna con compromiso renal es una condición aguda y grave, que normalmente se maneja con agentes intravenosos. Extrapolar desde el uso oral crónico es incierto, y la predicción no cuenta con respaldo de ensayos clínicos ni de literatura.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran productos de carvedilol como único principio activo y también asociaciones con hidroclorotiazida (la lista puede ser parcial). A continuación se muestran las 5 principales.

<!-- review:begin ar-lic-20261124-carvedilol-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Se registran al menos 20 autorizaciones, todas vigentes y de productos de un solo principio activo (la lista puede ser parcial).» Corregido: según los datos (listado de medicamentos de PAMI), el listado de PAMI incluye asociaciones de carvedilol con hidroclorotiazida; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-carvedilol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 59509 | CARVEDIL 12.5 | 12.5 mg comp.x 60 | Bagó | Vigente |
| 59512 | CARVEDIL 50 | 50 mg comp.x 30 | Bagó | Vigente |
| 36205 | CORUBIN | 6.25 mg comp.x 28 | Lazar | Vigente |
| 45532 | ENTARSOL 6.25 | 6.25 mg comp.x 28 | Microsules Arg. | Vigente |
| 51831 | ISOBLOC | 6.25 mg comp.x 60 | Casasco | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - Mayor: epinefrina.
  - Moderadas: hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, canagliflozina, acetohexamida, entre otras (corticoides, sales de calcio y antidiabéticos).
  - Menores: ácido acetilsalicílico, hidróxido de aluminio, attapulgita.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura que estudien directamente esta enfermedad. Además, el cuadro agudo y grave limita la extrapolación desde el uso oral crónico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y su relación con la enfermedad renal hipertensiva maligna.
- Revisión de literatura y estudios clínicos o preclínicos que evalúen directamente esta condición.
- Revisión del prospecto de ANMAT (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Evaluación de la ruta de administración, dado que el manejo habitual de este cuadro es intravenoso.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «todas … de un solo principio activo» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

