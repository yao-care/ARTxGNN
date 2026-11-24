---
layout: default
title: Naproxeno
parent: Solo Predicción del Modelo (L5)
nav_order: 270
evidence_level: L5
indication_count: 4
drugbank_id: DB00788
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
last_modified_at: 2026-11-24
description: "Naproxeno: nueva indicación predicha, síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Naproxeno
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

## Naproxeno: síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Resumen en Una Frase

Naproxeno es un antiinflamatorio no esteroideo (AINE) con múltiples autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser efectivo para **síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) |
| Puntaje de Predicción TxGNN | 0.9935 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Naproxeno (traducción no oficial): «El naproxeno tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción de NAPRELAN, al igual que el de otros AINE, no se comprende por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Naproxen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of NAPRELAN, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893), versión del 2026-01-08; consultado el 2026-11-19). Según el conocimiento farmacológico general, naproxeno inhibe de forma no selectiva las enzimas COX-1 y COX-2 y reduce la síntesis de prostaglandinas, lo que explica su efecto analgésico y antiinflamatorio.

Sin embargo, no se identifica un vínculo mecanístico plausible con este síndrome, que es un trastorno genético del desarrollo con alteraciones en la formación de las extremidades. En el mejor de los casos, un AINE aportaría alivio sintomático del dolor, sin modificar la enfermedad.

El puntaje alto del modelo (0,9935) es una señal computacional y no sustituye la evidencia clínica. Por ello, la razonabilidad biológica de esta predicción es baja.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay productos de naproxeno como único principio activo y también asociaciones (con carisoprodol o con esomeprazol); la lista puede ser parcial. Principales autorizaciones:

<!-- review:begin ar-lic-20261124-naproxeno-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Hay al menos 20 autorizaciones registradas, todas vigentes y de producto de un solo principio activo;» Corregido: según los datos (listado de medicamentos de PAMI), el listado de PAMI incluye asociaciones de naproxeno con carisoprodol o con esomeprazol; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-naproxeno-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 40276 | DEBRIL | 500 mg comp.x 10 | Monserrat | Vigente |
| 41754 | NAPRUX RAPID | 550 mg comp.rec.ran.x 10 | Andrómaco | Vigente |
| 8779 | NAPRONTAG | 500 mg comp.x 50 | Rontag | Vigente |
| 603 | ALIDASE 500 | comp.x 40 | Laboratorios Be | Vigente |
| 40403 | NAPRONTAG GESIC | 550 mg comp.rec.x 10 | Rontag | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Nota: como antecedente general, la inhibición de prostaglandinas es un motivo de cautela durante el embarazo y el desarrollo, lo que hace desfavorable cualquier racional de uso en trastornos del desarrollo.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, y no se identifica un mecanismo plausible que vincule la inhibición de COX con este síndrome del desarrollo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis mecanístico específico para esta enfermedad
- Revisión sistemática de literatura que estudie directamente la enfermedad
- Obtención y análisis del prospecto de ANMAT (advertencias y contraindicaciones)
- Evidencia preclínica que respalde cualquier efecto más allá del alivio sintomático

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893) |
| 2026-11-24 | «todas … de un solo principio activo» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

