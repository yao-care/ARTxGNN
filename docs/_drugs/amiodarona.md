---
layout: default
title: Amiodarona
parent: Solo Predicción del Modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
drugbank_id: DB01118
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-11-16
description: "Amiodarona: nueva indicación predicha, taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia) (nivel de evidencia L5)."
---

# Amiodarona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Amiodarona: taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia)
{: .text-alpha }

## Resumen en Una Frase

Amiodarona es un antiarrítmico de uso cardiovascular con cuatro autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser efectivo para **taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia)**, pero los datos compilados no incluyen ensayos clínicos y la literatura disponible consiste en reportes de caso, cohortes y revisiones que no demuestran eficacia de amiodarona en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia) |
| Puntaje de Predicción TxGNN | 0.9978 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. De forma general, amiodarona es un antiarrítmico con efectos sobre canales iónicos y acción simpaticolítica, y esto es lo que sustenta, en teoría, su uso en arritmias ventriculares.

La taquicardia ventricular polimórfica catecolaminérgica es una canalopatía hereditaria rara, causada por mutaciones en RYR2 o CASQ2, en la que la fuga diastólica de calcio genera arritmias desencadenadas por estimulación adrenérgica. Los efectos betabloqueantes y sobre el calcio de amiodarona son mecanísticamente plausibles, pero no actúan sobre el receptor RyR2.

Los tratamientos preferidos en esta enfermedad son los betabloqueantes (p. ej., nadolol), la flecainida y la denervación simpática cardíaca. La literatura recuperada menciona amiodarona solo de forma incidental, por lo que el puntaje alto del modelo no está respaldado por evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguno de los estudios siguientes evalúa directamente la eficacia de amiodarona en esta enfermedad.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revisión sistemática (cohortes) | Life (Basel) | Características clínicas, genéticas y desenlaces arrítmicos de pacientes con CPVT en China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte retrospectiva | Rev Cardiovasc Med | Características clínicas, base genética y costos sanitarios de CPVT en una ciudad china |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento farmacológico de las arritmias ventriculares |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Reporte de caso | Front Cardiovasc Med | CPVT resuelta con denervación simpática cardíaca derecha en un adolescente |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Reporte de caso | Pacing Clin Electrophysiol | Flecainida suprime las tormentas inducidas por el desfibrilador en CPVT |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Reporte de caso | Medicine | Diagnóstico tardío de CPVT con mutación RYR2 en un niño de 9 años |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Reporte de caso | Turk Pediatri Arsivi | Paro cardíaco súbito por CPVT en un niño de 2 años |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Reporte de caso | BMJ Case Reports | Supervivencia de un niño con paro cardíaco extrahospitalario y taquicardia ventricular recurrente |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 7639 | ATLANSIL | comp. x 50 | No registrada en los datos locales |
| 37428 | MIODARONA | 200 mg comp. x 40 | No registrada en los datos locales |
| 37427 | MIODARONA | 200 mg comp. x 20 | No registrada en los datos locales |
| 7638 | ATLANSIL | comp. x 20 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje del modelo es muy alto (0,9978), no hay ensayos clínicos ni estudios que evalúen directamente amiodarona en esta enfermedad. Existen alternativas con respaldo clínico y mecanístico mejor establecido (betabloqueantes, flecainida, denervación simpática).

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen específicamente amiodarona en esta enfermedad
- Datos del mecanismo de acción y del prospecto de ANMAT (advertencias y contraindicaciones)
- Comparación frente a las terapias de referencia
- Revisión de interacciones farmacológicas, ya que los datos compilados no las registran

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «No se identificaron autorizaciones de comercialización vigentes (0 licencias)» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

