---
layout: default
title: Meloxicam
parent: Solo Predicción del Modelo (L5)
nav_order: 185
evidence_level: L5
indication_count: 8
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-25
description: "Meloxicam: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5). Indicación original: No consta en los dato…"
---

# Meloxicam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Meloxicam: inhibidor de la COX-2 con preferencia (AINE) → displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) con preferencia por la COX-2, comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Meloxicam (traducción no oficial): «El meloxicam tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción de Zybic™, al igual que el de otros AINE, no se conoce por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Meloxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Zybic™, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec), versión del 2026-09-25; consultado el 2026-11-19). Según la información conocida, meloxicam es un AINE con preferencia por la COX-2 que reduce la producción de prostaglandinas y, con ello, el dolor y la inflamación.

La displasia acromesomélica tipo Hunter-Thompson es una enfermedad genética del esqueleto causada por pérdida de función del gen CDMP1/GDF5, que altera el crecimiento de las extremidades. La inhibición de la COX no actúa sobre este defecto de formación ósea. En el mejor de los casos podría plantearse, de forma hipotética, un papel sintomático sobre el dolor articular, sin ningún dato que lo respalde.

El puntaje alto (0.9992) probablemente refleja la cercanía en la red del modelo con términos musculoesqueléticos y no una relación mecanística real. Por ello, la predicción debe considerarse especulativa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Meloxicam figura como comercializado en Argentina, con autorizaciones vigentes en la lista disponible (los datos solo incluyen una parte de los productos; las cifras están en el resumen rápido). Hay productos de meloxicam como único principio activo y también asociaciones (por ejemplo, con pridinol).

<!-- review:begin ar-lic-20261124-meloxicam-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Las autorizaciones son de productos de un solo principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), el listado de PAMI incluye asociaciones de meloxicam con pridinol o con betametasona; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-meloxicam-1 -->

<!-- review:begin ar-lic-20261125b-meloxicam-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «con 20 autorizaciones vigentes en la lista disponible (la cantidad total es de al menos 20 y la lista puede ser parcial).» Corregido: los datos de este medicamento solo incluyen una parte de los productos del listado de PAMI, y la frase daba como total o como número de filas mostradas una cifra fija que no coincide con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125b-meloxicam-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 53872 | FLEXIDOL CB | 15 mg cáps.blandas x 20 | Adium | Vigente |
| 54324 | MELOXICAM TEVA | 15 mg tabl.x 30 | Teva Argentina | Vigente |
| 38348 | MIOLOX | 15 mg comp.ran.x 30 | Baliarda | Vigente |
| 18518 | FLEXIDOL | 15 mg comp.ran.x 30 | Adium | Vigente |
| 19079 | MOBIC | 15 mg comp.x 20 | Boehringer Inge | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para esa información.

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas, la mayoría son de nivel moderado, por ejemplo con:
  - corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida);
  - ácido acetilsalicílico;
  - antidiabéticos (metformina, clorpropamida, glimepirida);
  - mesalazina y balsalazida;
  - aminoglucósidos y vancomicina (kanamicina, vancomicina);
  - aprepitant.

  Linaclotida tiene una interacción de nivel menor.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ningún ensayo clínico ni publicación, el mecanismo de acción de meloxicam no se relaciona de forma plausible con el defecto genético de la enfermedad, y el puntaje alto parece un artefacto de proximidad en la red. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios preclínicos o de mecanismo que justifiquen una acción sobre la vía GDF5/CDMP1 o sobre síntomas de la enfermedad
- Datos detallados del mecanismo de acción de meloxicam
- Revisión de advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Si se explora un papel sintomático (dolor articular), una evaluación clínica específica con enfoque de seguridad

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zybic (meloxicam) prescribing information, Redmont Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a1c2d65f-ebb1-48bf-8fa1-c216f7d570ec) |
| 2026-11-24 | «de un solo principio activo» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-25 | «20 autorizaciones» → sin cifra | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

