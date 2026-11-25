---
layout: default
title: Pridinol
parent: Solo Predicción del Modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Pridinol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "PRIDINOL"
drugbank_id: DB13642
predicted_indications: ["insomnia (disease)"]
---

# Pridinol
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

## Pridinol: De Indicación Original No Especificada a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Pridinol es un relajante muscular de acción central con propiedades anticolinérgicas, comercializado en Argentina principalmente en combinaciones con antiinflamatorios (por ejemplo, meloxicam o diclofenac) para el dolor muscular. En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; el sustento es únicamente la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pridinol es un relajante muscular de acción central con propiedades anticolinérgicas (antimuscarínicas), utilizado en cuadros de dolor y espasmo muscular. Su uso en Argentina se observa sobre todo en asociaciones con antiinflamatorios no esteroides.

Existen dos vías plausibles, ninguna verificada. La primera: la actividad antimuscarínica central podría producir sedación. La segunda: el alivio del espasmo muscular doloroso podría mejorar el sueño de forma indirecta. Ninguna de las dos está documentada en los datos compilados.

Además, los fármacos anticolinérgicos también pueden empeorar la calidad del sueño y la función cognitiva, por lo que la dirección del efecto es incierta. El único respaldo es un puntaje alto del modelo (0.9989), un valor derivado del modelo sin validación clínica. La similitud con la indicación original está pendiente de evaluar y la compatibilidad de vías de administración también está pendiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Las autorizaciones recopiladas en los datos están vigentes y en su mayoría son asociaciones de pridinol con otros principios activos; los datos solo incluyen una parte de los productos (las cifras están en el resumen rápido). Se muestran las 5 principales; los textos de indicación aprobada no figuran en los datos compilados.

<!-- review:begin ar-lic-20261125b-pridinol-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «Se registran 20 autorizaciones vigentes, todas de productos de un solo registro (sin cancelaciones).» Corregido: los datos de este medicamento solo incluyen una parte de los productos del listado de PAMI, y la frase daba como total o como número de filas mostradas una cifra fija que no coincide con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125b-pridinol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 44309 | DIOXAFLEX PLUS | iny.a.x 6 | Bagó | Vigente |
| 47973 | DICLOMAR FLEX POTASICO | comp.x 15 | Mar | Vigente |
| 38086 | FLEXIDOL RELAX | comp.ran.x 20 | Adium | Vigente |
| 16309 | DIOXAFLEX PLUS | comp.x 30 | Bagó | Vigente |
| 35297 | OXADISTEN | comp.rec.x 100 | Beta | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una predicción del modelo sin ensayos clínicos ni literatura (nivel L5). Además, la dirección del efecto es incierta, ya que las propiedades anticolinérgicas podrían empeorar el sueño y la cognición.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente sin datos
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar las indicaciones aprobadas de las autorizaciones en Argentina
- Realizar una búsqueda sistemática de literatura y ensayos sobre pridinol (u otros antimuscarínicos centrales) en trastornos del sueño
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración
- Considerar estudios preclínicos o de mecanismo antes de cualquier ensayo clínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-25 | «20 autorizaciones … un solo registro» → mayoría asociaciones, sin cifra | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

