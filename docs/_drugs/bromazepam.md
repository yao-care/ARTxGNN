---
layout: default
title: Bromazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 62
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Bromazepam: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (las autorizaciones no incluyen…"
monitor_inn: "BROMAZEPAM"
predicted_indications: ["migraine disorder"]
---

# Bromazepam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Bromazepam: De Indicación Original No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Bromazepam es una benzodiazepina comercializada en Argentina; los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Bromazepam es (traducción no oficial): «Modulador alostérico positivo de la subunidad alfa-2 del receptor GABA». Texto original en inglés: "GABA receptor alpha-2 subunit positive allosteric modulator" ([ChEMBL CHEMBL277062 (bromazepam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL277062), CC BY-SA 3.0; consultado el 2026-11-19). Según la información farmacológica conocida, bromazepam es una benzodiazepina que actúa como modulador alostérico positivo de los receptores GABA-A, lo que potencia la neurotransmisión inhibitoria.

Mecanísticamente, podría plantearse un vínculo con la migraña a través de la reducción de la hiperexcitabilidad cortical y trigeminal, además del alivio de la ansiedad y la tensión muscular, que pueden actuar como desencadenantes o comorbilidades de la migraña.

Sin embargo, este vínculo es especulativo. El puntaje de TxGNN es muy alto (0.9906), pero es solo una predicción derivada del modelo, sin estudios que la respalden. Las benzodiazepinas no son una terapia establecida para la migraña, y sus riesgos (dependencia, sedación, tolerancia y cefalea por abuso de medicación) desaconsejan su uso sin evidencia directa.

## Información de Mercado en Argentina

Se registran productos de bromazepam como único principio activo y también asociaciones (con trimebutina, o con domperidona y simeticona); la lista de estos datos es parcial. Se muestran las 5 principales:

<!-- review:begin ar-lic-20261124-bromazepam-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Se registran 20 autorizaciones vigentes, todas de monofármaco (sin combinaciones) y ninguna cancelada.» Corregido: según los datos (listado de medicamentos de PAMI), el listado de PAMI incluye asociaciones de bromazepam con trimebutina o con domperidona y simeticona; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-bromazepam-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 7510 | LEXOTANIL | 6 mg comp.x 50 | Biopas Argentin | Vigente |
| 7509 | LEXOTANIL | 3 mg comp.x 50 | Biopas Argentin | Vigente |
| 10449 | LEXOTANIL | 3 mg comp.x 30 | Biopas Argentin | Vigente |
| 3196 | CREOSEDIN | 6 mg comp.x 50 | Rontag | Vigente |
| 2768 | NULASTRES | 6 mg comp.x 50 | Duncan | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Además, la predicción en sí advierte de los riesgos propios de las benzodiazepinas en este contexto: dependencia, sedación, tolerancia y cefalea por abuso de medicación.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y las benzodiazepinas no son una terapia establecida para la migraña, con riesgos relevantes de dependencia y cefalea por abuso de medicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), indispensable para la evaluación de seguridad
- Confirmar la indicación aprobada en Argentina
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar evidencia clínica o preclínica directa de bromazepam en migraña
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL277062 (bromazepam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL277062) |
| 2026-11-24 | «sin combinaciones» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

