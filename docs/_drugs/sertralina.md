---
layout: default
title: Sertralina
parent: Solo Predicción del Modelo (L5)
nav_order: 327
evidence_level: L5
indication_count: 7
drugbank_id: DB01104
monitor_inn: "Sertraline"
predicted_indications: ["schizoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder", "paranoid personality disorder", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
last_modified_at: 2026-11-24
description: "Sertralina: nueva indicación predicha, trastorno de personalidad esquizoide (schizoid personality disorder) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Sertralina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Sertralina: trastorno de personalidad esquizoide (schizoid personality disorder)
{: .text-alpha }

## Resumen en Una Frase

Sertralina es un fármaco antidepresivo de la clase de los inhibidores selectivos de la recaptación de serotonina (ISRS), comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **trastorno de personalidad esquizoide (schizoid personality disorder)**, pero actualmente **no hay ensayos clínicos** y solo **1 publicación** vinculada, que trata sobre otro trastorno (trastorno por atracón), por lo que la evidencia es únicamente la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno de personalidad esquizoide (schizoid personality disorder) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sertralina (traducción no oficial): «La sertralina potencia la actividad serotoninérgica en el sistema nervioso central mediante la inhibición de la recaptación neuronal de serotonina (5-HT).» Texto original en inglés: "Sertraline potentiates serotonergic activity in the central nervous system through inhibition of neuronal reuptake of serotonin (5-HT)." ([DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7), versión del 2023-08-08; consultado el 2026-11-19). Por conocimiento general, la sertralina pertenece a la clase de los ISRS, que aumentan la disponibilidad de serotonina en la sinapsis, y mecanísticamente se podría especular con un efecto sobre síntomas afectivos o de ansiedad asociados a la patología de personalidad.

Sin embargo, los datos compilados no respaldan un vínculo mecanístico directo con el trastorno de personalidad esquizoide. La única publicación vinculada aborda el trastorno por atracón, no la enfermedad predicha. Además, el puntaje de 0,9993 es idéntico para varios trastornos de personalidad no relacionados entre sí, lo que sugiere un artefacto a nivel de clase más que una señal específica de la enfermedad. Debe interpretarse como una hipótesis del modelo, no como evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19794312](https://pubmed.ncbi.nlm.nih.gov/19794312/) | 2009 | Informe de tratamiento multimodal | International Clinical Psychopharmacology | En 30 pacientes con trastorno por atracón se compararon tres tratamientos de 6 meses (dieta, terapia cognitivo-conductual y sertralina, en distintas combinaciones). No aborda el trastorno de personalidad esquizoide. |

## Información de Mercado en Argentina

Sertralina cuenta con al menos 20 autorizaciones vigentes (la lista puede ser parcial), todas de productos de un solo principio activo. Los textos de indicación aprobada no están registrados en los datos locales.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 20681 | ATENIX | 50 mg comp.ran.x 60 | Adium | Vigente |
| 40791 | ZOXX 50 | 50 mg comp.rec.x 30 | Casasco | Vigente |
| 23736 | BICROMIL | 100 mg comp.x 30 | Cetus | Vigente |
| 51568 | DIMENA | 100 mg comp.x 30 | Lepetit | Vigente |
| 26875 | ATENIX | 25 mg comp.ran.x 30 | Adium | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5): no hay ensayos clínicos ni estudios que evalúen directamente el trastorno de personalidad esquizoide, y el puntaje idéntico entre varios trastornos de personalidad indica una posible señal inespecífica.

**Para avanzar se necesita:**
- Estudios clínicos o literatura que evalúen directamente la sertralina en el trastorno de personalidad esquizoide
- Datos del mecanismo de acción y análisis de su vínculo con la enfermedad predicha
- Advertencias y contraindicaciones del prospecto de ANMAT para completar la evaluación de seguridad
- Consideración específica de la seguridad en poblaciones jóvenes (advertencia de los ISRS en menores) si se explorara el uso

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zoloft (sertraline hydrochloride) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda754f6-d0f3-4dce-a17a-927d64f912f7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

