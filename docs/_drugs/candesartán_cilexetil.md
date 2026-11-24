---
layout: default
title: Candesartán Cilexetil
parent: Solo Predicción del Modelo (L5)
nav_order: 76
evidence_level: L5
indication_count: 4
drugbank_id: DB00796
monitor_inn: "Candesartan cilexetil"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Candesartán Cilexetil: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5)."
---

# Candesartán Cilexetil
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

## Candesartán Cilexetil: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Candesartán cilexetilo es un fármaco comercializado en Argentina en varias presentaciones de comprimidos, solo y en combinación.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (15 de 15) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 15 (vigentes: 15) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción del fármaco. Según el conocimiento general, el candesartán es un bloqueador del receptor de angiotensina II tipo 1 (ARA-II). La hipertensión maligna con compromiso renal está fuertemente impulsada por la activación del sistema renina-angiotensina-aldosterona, por lo que reducir la presión arterial y proteger el riñón mediante el bloqueo del receptor AT1 es mecanísticamente plausible.

Sin embargo, no se dispone de ensayos clínicos ni literatura para esta indicación, y el puntaje del modelo (0,9968) es solo una predicción. Dado que el fármaco ya se comercializa para uso cardiovascular, esto podría representar en gran parte una extensión de un uso existente más que un reposicionamiento genuino.

Además, el uso en hipertensión maligna requeriría especial cautela: los ARA-II pueden empeorar la función renal en contextos agudos, por ejemplo con estenosis de la arteria renal o depleción de volumen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Argentina

El fármaco está comercializado en Argentina, como monofármaco y en asociación con felodipina (ATACAND DUO). Ninguna incluye texto de indicación aprobada.

<!-- review:begin ar-lic-20261124-candesartán_cilexetil-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «El fármaco está comercializado en Argentina, con 15 autorizaciones vigentes, todas de monofármaco según los registros.» Corregido: según los datos (listado de medicamentos de PAMI), ATACAND DUO es una asociación de candesartán cilexetilo con felodipina; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-candesartán_cilexetil-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 28929 | DACTEN | 8 mg comp.x 15 | Elea | Vigente |
| 55471 | ATACAND | 8 mg comp.divis.x 28 | Biopas Argentin | Vigente |
| 55473 | ATACAND | 32 mg comp.divis.x 28 | Biopas Argentin | Vigente |
| 47502 | CANDESARTAN RICHET | 16 mg comp.x 30 | Richet | Vigente |
| 28932 | DACTEN | 16 mg comp.x 30 | Elea | Vigente |

La tabla muestra 5 de los 15 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Se muestran las 5 primeras de 15 autorizaciones.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como consideración general, derivada del análisis del modelo y no de datos del prospecto: los ARA-II pueden empeorar la función renal en situaciones agudas, y la hipotensión sistémica es una preocupación en poblaciones con enfermedad vascular pulmonar.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (0,9968), sin ensayos clínicos ni publicaciones que estudien directamente esta enfermedad (nivel de evidencia L5).

**Para avanzar se necesita:**
- Revisar los ensayos clínicos y la literatura sobre candesartán en hipertensión maligna y nefropatía hipertensiva
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción
- Evaluar el riesgo de empeoramiento de la función renal en contextos agudos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «todas de monofármaco» → también asociación con felodipina | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

