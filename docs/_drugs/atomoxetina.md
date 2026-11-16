---
layout: default
title: Atomoxetina
parent: Solo Predicción del Modelo (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
drugbank_id: DB00289
monitor_inn: "Atomoxetine"
predicted_indications: ["specific developmental disorder", "faciodigitogenital syndrome", "chondromyxoid fibroma", "trichotillomania", "restless legs syndrome", "manic bipolar affective disorder", "Tourette syndrome", "transient tic disorder", "cerebellar ataxia", "autosomal dominant cerebellar ataxia"]
last_modified_at: 2026-11-16
description: "Atomoxetina: nueva indicación predicha, trastorno específico del desarrollo (specific developmental disorder) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Atomoxetina
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

## Atomoxetina: trastorno específico del desarrollo (specific developmental disorder)
{: .text-alpha }

## Resumen en Una Frase

Atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina, comercializado en Argentina bajo la marca RECIT.
El modelo TxGNN predice que podría ser efectivo para **trastorno específico del desarrollo (specific developmental disorder)**,
pero actualmente no hay ensayos clínicos registrados y la literatura recopilada se refiere casi por completo al TDAH, no a esta categoría diagnóstica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno específico del desarrollo (specific developmental disorder) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 5) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe, por lo que el análisis mecanístico es limitado.

"Trastorno específico del desarrollo" es una categoría amplia que se solapa con el TDAH y las dificultades de aprendizaje. El puntaje alto del modelo probablemente refleja esta cercanía con los trastornos del neurodesarrollo en los que atomoxetina ya se utiliza, más que una señal específica para esta categoría.

La literatura recuperada incluye metaanálisis en red sobre TDAH en adultos y un metaanálisis sobre TDAH en niños con autismo, pero ningún estudio evalúa directamente un trastorno específico del desarrollo distinto del TDAH. Varios artículos recuperados no guardan relación con el tema (catinonas sintéticas, interacciones farmacológicas, costos sanitarios). Por ello el nivel de evidencia se fija en L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Revisión sistemática / metaanálisis en red | The Lancet Psychiatry | Eficacia y aceptabilidad comparativas de intervenciones farmacológicas, psicológicas y de neuroestimulación para el TDAH en adultos |
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Revisión / metaanálisis | Autism Research | Atomoxetina para síntomas de TDAH en niños con autismo; tres ECA con 241 niños |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohorte retrospectiva | Neuropsychopharmacology Reports | Factores asociados con la eficacia de atomoxetina en TDAH adulto |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Revisión | Therapeutic Advances in Psychopharmacology | Eficacia de atomoxetina en TDAH con comorbilidades frecuentes |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Cohorte | Clinical EEG and Neuroscience | EEG cuantitativo en TDAH infantil y dificultades de aprendizaje |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Cohorte (preprint) | bioRxiv | Desviaciones de conectividad estructural en jóvenes con TDAH que predicen síntomas y resultados del tratamiento |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33698 | RECIT | 10 mg cáps. x 7 | No registrada en los datos locales |
| 33699 | RECIT | 18 mg cáps. x 7 | No registrada en los datos locales |
| 33700 | RECIT | 25 mg cáps. x 14 | No registrada en los datos locales |
| 33701 | RECIT | 40 mg cáps. x 14 | No registrada en los datos locales |
| 33702 | RECIT | 60 mg cáps. x 14 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni con estudios que evalúen directamente esta categoría diagnóstica; el puntaje alto parece reflejar la cercanía con el TDAH, y la categoría es demasiado amplia para orientar una decisión.

**Para avanzar se necesita:**
- Definir con precisión qué trastorno específico del desarrollo (por ejemplo, trastornos específicos del aprendizaje) se quiere evaluar
- Estudios que evalúen atomoxetina directamente en esa población, distinta de la población con TDAH
- Datos de mecanismo de acción
- Advertencias y contraindicaciones del prospecto aprobado en Argentina

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «No existen autorizaciones de comercialización vigentes» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

