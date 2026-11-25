---
layout: default
title: Metformina
parent: Solo Predicción del Modelo (L5)
nav_order: 248
evidence_level: L5
indication_count: 5
drugbank_id: DB00331
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
last_modified_at: 2026-11-25
description: "Metformina: nueva indicación predicha, síndrome de rigidez focal de las extremidades (focal stiff limb syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Metformina
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

## Metformina: síndrome de rigidez focal de las extremidades (focal stiff limb syndrome)
{: .text-alpha }

## Resumen en Una Frase

Metformina es un fármaco antidiabético que se comercializa en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de rigidez focal de las extremidades (focal stiff limb syndrome)**,
pero **no hay ensayos clínicos ni publicaciones** en los datos compilados para este informe que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | síndrome de rigidez focal de las extremidades (focal stiff limb syndrome) |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metformina (traducción no oficial): «La metformina es un antihiperglucemiante que mejora la tolerancia a la glucosa en pacientes con diabetes mellitus de tipo 2 y reduce tanto la glucosa plasmática basal como la posprandial. La metformina disminuye la producción hepática de glucosa, disminuye la absorción intestinal de glucosa y mejora la sensibilidad a la insulina al aumentar la captación y la utilización periféricas de glucosa.» Texto original en inglés: "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), versión del 2026-09-21; consultado el 2026-11-19). Por conocimiento general, la metformina actúa activando AMPK, inhibiendo el complejo I mitocondrial y reduciendo la gluconeogénesis hepática.

El síndrome de rigidez focal de las extremidades pertenece al espectro del síndrome de la persona rígida, cuyo origen se atribuye a una disfunción de la transmisión GABAérgica/glicinérgica y, con frecuencia, a autoinmunidad (anti-GAD o anti-anfifisina). No existe un vínculo establecido entre las acciones conocidas de la metformina y estos mecanismos.

El puntaje alto (0,9945) es una predicción del modelo y no equivale a evidencia clínica. Otra predicción del modelo (síndrome de la persona rígida clásico) tiene exactamente el mismo puntaje, lo que sugiere un entorno de relaciones compartido y no evidencia independiente. Cualquier conexión mecanística, como una inmunomodulación vía AMPK/mTOR, es especulativa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones (la lista puede ser parcial); las recopiladas en los datos están vigentes y corresponden a productos de un solo principio activo (los datos solo incluyen una parte de los productos; las cifras están en el resumen rápido). Las principales:

<!-- review:begin ar-lic-20261125b-metformina-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «las 20 listadas están vigentes y corresponden a productos de un solo principio activo.» Corregido: los datos de este medicamento solo incluyen una parte de los productos del listado de PAMI, y la frase daba como total o como número de filas mostradas una cifra fija que no coincide con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125b-metformina-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 46018 | METFORMINA ROSPAW 850 AP | 850 mg comp.rec.AP x 30 | Rospaw | Vigente |
| 50161 | DAZOMET | AP 1000 mg comp.x 60 | Savant Generic | Vigente |
| 43470 | DIABESIL AP 850 | AP 850 mg comp.rec.x60 | Gador | Vigente |
| 17330 | METFORMIN TEMIS | 500 mg comp.x 60 | Temis-Lostaló | Vigente |
| 55308 | REDUGLUC | 1000 mg comp.x 100 | Microsules Arg. | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que estudien directamente esta enfermedad, y la relación mecanística con la metformina no está respaldada. La predicción se sostiene solo en el puntaje del modelo (nivel L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la metformina en el contexto de trastornos del espectro de la persona rígida
- Revisión sistemática de la literatura sobre metformina y síndromes de rigidez
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Evaluación de plausibilidad biológica antes de cualquier estudio preclínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |
| 2026-11-25 | «las 20 listadas» → sin cifra | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

