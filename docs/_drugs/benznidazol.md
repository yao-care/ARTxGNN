---
layout: default
title: Benznidazol
parent: Solo Predicción del Modelo (L5)
nav_order: 47
evidence_level: L5
indication_count: 3
drugbank_id: DB11989
monitor_inn: "Benznidazole"
predicted_indications: ["congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-11-20
description: "Benznidazol: nueva indicación predicha, analbuminemia congénita (congenital analbuminemia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Benznidazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Benznidazol: analbuminemia congénita (congenital analbuminemia)
{: .text-alpha }

## Resumen en Una Frase

Benznidazol es un antiprotozoario de la familia de los nitroimidazoles, comercializado en Argentina con el nombre ABARAX.
El modelo TxGNN predice que podría ser efectivo para **analbuminemia congénita (congenital analbuminemia)**, con un puntaje de 0,9951.
Actualmente no hay **ningún ensayo clínico ni publicación** que respalde esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | analbuminemia congénita (congenital analbuminemia) |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Benznidazol (traducción no oficial): «El benznidazol es un fármaco antimicrobiano nitroimidazólico. […] El benznidazol inhibe la síntesis de ADN, ARN y proteínas dentro del parásito T. cruzi. Los estudios sugieren que el benznidazol es reducido por una enzima nitrorreductasa de tipo I (NTR) de T. cruzi, lo que produce una serie de intermediarios de vida corta que pueden favorecer el daño a varias macromoléculas, incluido el ADN.» Texto original en inglés: "Benznidazole is a nitroimidazole antimicrobial drug. […] Benznidazole inhibits the synthesis of DNA, RNA, and proteins within the T. cruzi parasite. Studies suggest that benznidazole is reduced by a Type I nitroreductase (NTR) enzyme of T. cruzi producing a series of short-lived intermediates that may promote damage to several macromolecules including DNA." ([DailyMed: benznidazole prescribing information, Exeltis USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8983d6a0-f63f-4f8e-bba4-38223f39e29b), versión del 2026-08-27; consultado el 2026-11-19). Según la información general conocida, benznidazol es un profármaco nitroimidazólico que es activado por nitrorreductasas del parásito *Trypanosoma cruzi*. Esa activación genera metabolitos reactivos que dañan el ADN, las proteínas y los lípidos del parásito.

La analbuminemia congénita es un trastorno autosómico recesivo raro, causado por mutaciones de pérdida de función en el gen *ALB*, que reducen o eliminan la albúmina sérica. Es un defecto genético de síntesis proteica, sin componente parasitario ni dependiente de nitrorreductasas.

Por lo tanto, **no se identifica un vínculo mecanístico plausible**. El puntaje alto (0,9951) probablemente refleja artefactos del modelo, como vecinos compartidos en la red de relaciones o el transporte de fármacos por la albúmina, y no una relación terapéutica real. No debe interpretarse como respaldo para reposicionar el fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 47976 | ABARAX | 100 mg comp. x 100 | No registrada en los datos locales |
| 47975 | ABARAX | 50 mg comp. x 100 | No registrada en los datos locales |

Ambas autorizaciones corresponden a productos de un solo principio activo, están vigentes y pertenecen al fabricante Elea.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, no tiene un vínculo mecanístico plausible y el nivel de evidencia es L5. Además, faltan los datos de seguridad del prospecto local.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Disponer de evidencia preclínica o clínica que vincule benznidazol con la analbuminemia congénita; sin ella no se recomienda continuar.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «(TFDA)» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: benznidazole prescribing information, Exeltis USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8983d6a0-f63f-4f8e-bba4-38223f39e29b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

