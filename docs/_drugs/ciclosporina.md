---
layout: default
title: Ciclosporina
parent: Solo Predicción del Modelo (L5)
nav_order: 99
evidence_level: L5
indication_count: 7
drugbank_id: DB00091
monitor_inn: "Cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland"]
last_modified_at: 2026-11-16
description: "Ciclosporina: nueva indicación predicha, enfermedad granulomatosa crónica autosómica recesiva (granulomatous disease, chronic, autosomal recessive) (nivel de evidencia L5)."
---

# Ciclosporina
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

## Ciclosporina: enfermedad granulomatosa crónica autosómica recesiva (granulomatous disease, chronic, autosomal recessive)
{: .text-alpha }

## Resumen en Una Frase

Ciclosporina es un inmunosupresor que se comercializa en Argentina en formulaciones oftálmicas.
El modelo TxGNN predice que podría ser efectivo para **enfermedad granulomatosa crónica autosómica recesiva (granulomatous disease, chronic, autosomal recessive)**,
pero no hay ensayos clínicos registrados y solo **1 publicación** se relaciona con esta dirección, un estudio de cohorte sobre trasplante de células madre que no evalúa a la ciclosporina como tratamiento de la enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad granulomatosa crónica autosómica recesiva (granulomatous disease, chronic, autosomal recessive) |
| Puntaje de Predicción TxGNN | 0.9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la ciclosporina es un inhibidor de la calcineurina (vía NFAT) que suprime la activación de los linfocitos T.

La enfermedad granulomatosa crónica es un defecto de la NADPH oxidasa de los fagocitos. La ciclosporina no tiene un efecto corrector conocido sobre este defecto. Cualquier vínculo es indirecto, a través de la inmunosupresión posterior a un trasplante de células madre hematopoyéticas.

Además, la ciclosporina podría aumentar el riesgo de infecciones en un grupo de pacientes que ya es susceptible a ellas. Por eso la predicción debe considerarse con mucha cautela: el puntaje del modelo no está respaldado por estudios que evalúen directamente este fármaco en la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohorte | The Journal of Allergy and Clinical Immunology | Supervivencia excelente tras trasplante de células madre de donante hermano o no emparentado en enfermedad granulomatosa crónica; no estudia la ciclosporina como tratamiento de la enfermedad. |

**Nivel de evidencia:** L5. El único estudio citado trata del trasplante de células madre y no estudia directamente a la ciclosporina en esta enfermedad, por lo que no se alcanza un nivel superior.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42509 | RESTASIS | Viales x 30 unid. x 0,4 ml | — |
| 55823 | INMUNOSPORIN 0.1% | Solución oftálmica x 5 ml | — |
| 51198 | CIPOS 0.1 | Solución oftálmica x 5 ml | — |
| 47768 | CLOSPORIL 0.1% | Gotas oftálmicas x 5 ml | — |

Las cuatro autorizaciones están vigentes y corresponden a productos de un solo principio activo. Los registros locales no incluyen texto de indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación disponible no estudia a la ciclosporina en esta enfermedad. Además, no hay un vínculo mecanístico plausible y existe un riesgo teórico de aumentar las infecciones en estos pacientes. Las formulaciones locales son oftálmicas, lo que tampoco es compatible con una indicación sistémica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de ANMAT
- Estudios que evalúen directamente la ciclosporina en la enfermedad granulomatosa crónica
- Análisis de compatibilidad de vías de administración, dado que las presentaciones locales son oftálmicas
- Evaluación del riesgo de infecciones en pacientes con inmunodeficiencia de fagocitos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «La consulta a ANMAT/TFDA devolvió `result_count: 0` para el nombre INN "CICLOSPORINA". Esto puede deberse a que el fármaco está registrado b» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «TFDA o» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

