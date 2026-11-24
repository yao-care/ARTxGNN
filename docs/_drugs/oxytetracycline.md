---
layout: default
title: Oxytetracycline
parent: Solo Predicción del Modelo (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
monitor_inn: "oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
last_modified_at: 2026-11-24
description: "Oxytetracycline: nueva indicación predicha, rinosinusitis crónica (chronic rhinosinusitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Oxytetracycline
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

## Oxitetraciclina: antibiótico tetraciclina → rinosinusitis crónica (chronic rhinosinusitis)
{: .text-alpha }

## Resumen en Una Frase

La oxitetraciclina es un antibiótico de la clase de las tetraciclinas, disponible en Argentina en presentaciones tópicas (ungüento y spray).
El modelo TxGNN predice que podría ser efectiva para **rinosinusitis crónica (chronic rhinosinusitis)**, pero actualmente no hay ensayos clínicos ni publicaciones que respalden directamente esta predicción; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | rinosinusitis crónica (chronic rhinosinusitis) |
| Puntaje de Predicción TxGNN | 0,9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Oxytetracycline es (traducción no oficial): «Inhibidor del ribosoma 70S bacteriano». Texto original en inglés: "Bacterial 70S ribosome inhibitor" ([ChEMBL CHEMBL1517 (oxytetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1517), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la oxitetraciclina pertenece a la clase de las tetraciclinas, que actúan como antibacterianos de amplio espectro y además presentan propiedades antiinflamatorias y de inhibición de metaloproteinasas de matriz (MMP).

Mecanísticamente, estas propiedades podrían relacionarse con la inflamación crónica de los senos paranasales y con infecciones bacterianas de las vías respiratorias superiores. Es una hipótesis plausible, pero especulativa.

Es importante subrayar que el puntaje del modelo (0,9961) no está acompañado de ningún estudio que evalúe esta enfermedad. Por ello, el nivel de evidencia es L5 y la predicción debe tratarse como una hipótesis a investigar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para rinosinusitis crónica.

---

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 6413 | TERRA CORTRIL | ung.tópico 14.2 g | Pfizer | Vigente |
| 28596 | TERRA CORTRIL | spray x 100 ml | Pfizer | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Los productos (TERRA CORTRIL, fabricados por Pfizer) son asociaciones de oxitetraciclina con hidrocortisona.

<!-- review:begin ar-lic-20261124-oxytetracycline-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Las dos autorizaciones están vigentes y corresponden a productos de un solo principio activo, fabricados por Pfizer.» Corregido: según los datos (listado de medicamentos de PAMI), TERRA CORTRIL es una asociación de oxitetraciclina con hidrocortisona; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-oxytetracycline-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 144 interacciones en total. Entre las principales:
  - **Mayor**: vitamina A.
  - **Moderada**: amoxicilina, balsalazida, sales de calcio (fosfato y acetato), citrato de potasio, sales de magnesio (óxido, sulfato y cloruro), sales de zinc (sulfato y acetato) y distintas insulinas (aspart, degludec, detemir, glargina, glulisina, humana).
  - **Menor**: manitol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para rinosinusitis crónica se basa únicamente en el modelo, sin ensayos clínicos ni literatura que estudien esta enfermedad. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre tetraciclinas en rinosinusitis crónica
- Datos del mecanismo de acción del fármaco
- Evaluación de la viabilidad de la vía de administración, ya que las presentaciones locales son tópicas (ungüento y spray)
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos o ensayos exploratorios que evalúen directamente esta indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL1517 (oxytetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1517) |
| 2026-11-24 | «de un solo principio activo» → asociación con hidrocortisona | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

