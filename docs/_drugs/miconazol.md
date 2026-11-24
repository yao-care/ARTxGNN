---
layout: default
title: Miconazol
parent: Solo Predicción del Modelo (L5)
nav_order: 255
evidence_level: L5
indication_count: 1
drugbank_id: DB01110
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
last_modified_at: 2026-11-24
description: "Miconazol: nueva indicación predicha, acné (acne (disease)) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Miconazol
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

## Miconazol: acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Miconazol es un antifúngico de la clase de los imidazoles, con múltiples productos de uso tópico y vaginal comercializados en Argentina.
El modelo TxGNN predice que podría ser efectivo para **acné (acne (disease))**, con un puntaje de 0.9954. Actualmente no hay ensayos clínicos registrados y la evidencia consiste en **4 publicaciones** (una revisión, dos estudios de cohorte y un estudio in vitro).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Miconazol (traducción no oficial): «El miconazol es un fármaco antifúngico. […] El miconazol inhibe la enzima citocromo P450 14α-desmetilasa, lo que conduce a la inhibición de la síntesis de ergosterol, un componente esencial de la membrana celular fúngica. El miconazol también afecta la síntesis de triglicéridos y ácidos grasos e inhibe las enzimas oxidativas y peroxidativas, lo que aumenta la cantidad de especies reactivas de oxígeno dentro de la célula.» Texto original en inglés: "Miconazole is an antifungal drug. […] Miconazole inhibits the enzyme cytochrome P450 14α-demethylase which leads to inhibition of ergosterol synthesis, an essential component of the fungal cell membrane. Miconazole also affects the synthesis of triglycerides and fatty acids and inhibits oxidative and peroxidative enzymes, increasing the amount of reactive oxygen species within the cell." ([DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a), versión del 2026-01-08; consultado el 2026-11-19). Según la información conocida, el miconazol es un imidazol antifúngico que inhibe la síntesis de ergosterol fúngico (enzima CYP51/lanosterol 14-alfa-desmetilasa) y presenta cierta actividad antibacteriana frente a bacterias Gram positivas.

El vínculo con el acné es plausible por tres vías: (1) actividad in vitro de antifúngicos azólicos contra *Cutibacterium (Propionibacterium) acnes*; (2) actividad frente a *Malassezia* (*Pityrosporum*), levadura implicada en la foliculitis por Malassezia, que clínicamente se parece al acné; y (3) efectos antiinflamatorios descritos en trastornos cutáneos.

Es importante aclarar que el puntaje del modelo es una predicción computacional, no evidencia clínica. Además, la foliculitis por Malassezia es una entidad distinta del acné, y el estudio in vitro no equivale a eficacia clínica. Ninguna de las publicaciones disponibles demuestra, en un ensayo controlado, la eficacia del miconazol en acné; por eso el nivel de evidencia se mantiene en L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opinion on Pharmacotherapy | Revisión de los efectos del miconazol en trastornos de la piel, incluidos efectos antiinflamatorios |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Cohorte | Clinical and Experimental Dermatology | 62 pacientes con foliculitis por Pityrosporum, a menudo mal diagnosticada como acné vulgar; se evaluaron diagnóstico y ensayos terapéuticos |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohorte | Skin Research and Technology | Evaluación clínica y bioinstrumental en cara dividida de acné catamenial inflamatorio leve |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudio in vitro | Biological & Pharmaceutical Bulletin | Actividad in vitro de antifúngicos azólicos contra *P. acnes* aislado de pacientes con acné vulgar |

## Información de Mercado en Argentina

Hay productos de miconazol como único principio activo y asociaciones (con betametasona y gentamicina en cremas, o con metronidazol en óvulos); la lista puede ser parcial. Las 5 principales:

<!-- review:begin ar-lic-20261124-miconazol-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Se listan 20 autorizaciones vigentes de producto único; la cifra total es de al menos 20 y la lista puede ser parcial.» Corregido: según los datos (listado de medicamentos de PAMI), muchos productos son asociaciones de miconazol con betametasona y gentamicina (cremas) o con metronidazol (óvulos); las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-miconazol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 26902 | DERALBINE | pvo.en spray x 90 g | Andrómaco | Vigente |
| 18972 | MICOTRAL | 2% cr.x 30 g | Austral | Vigente |
| 11834 | DAKTARIN | gel oral x 40 g | Janssen-Cilag | Vigente |
| 19976 | DERALBINE | cr.x 40 g | Andrómaco | Vigente |
| 39967 | MICOPUL | cr.x 40 g | Pharmatrix | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en literatura indirecta (estudio in vitro, foliculitis por Malassezia y una revisión general), sin ensayos clínicos que estudien directamente el miconazol en acné. Además, faltan datos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Estudios clínicos (idealmente ECA) que evalúen miconazol en acné vulgar
- Datos curados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT
- Evaluación de la compatibilidad de las vías y formas farmacéuticas con el uso en acné

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Oravig (miconazole) prescribing information, Galt Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dc2427ff-e566-4b48-b289-9e51c011250a) |
| 2026-11-24 | «de producto único» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

