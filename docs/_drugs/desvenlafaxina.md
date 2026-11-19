---
layout: default
title: Desvenlafaxina
parent: Solo Predicción del Modelo (L5)
nav_order: 130
evidence_level: L5
indication_count: 8
drugbank_id: DB06700
monitor_inn: "Desvenlafaxine"
predicted_indications: ["obsessive-compulsive disorder", "schizotypal personality disorder", "schizoid personality disorder", "paranoid personality disorder", "histrionic personality disorder (disease)", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
last_modified_at: 2026-11-16
description: "Desvenlafaxina: nueva indicación predicha, Trastorno obsesivo-compulsivo (obsessive-compulsive disorder) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 16 (en el listado vigente: 16)"
---

# Desvenlafaxina
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

## Desvenlafaxina: Trastorno obsesivo-compulsivo (obsessive-compulsive disorder)
{: .text-alpha }

## Resumen en Una Frase

Desvenlafaxina es un inhibidor de la recaptación de serotonina y noradrenalina (IRSN), metabolito activo de la venlafaxina.
El modelo TxGNN predice que podría ser efectiva para **Trastorno obsesivo-compulsivo (obsessive-compulsive disorder)**, pero no hay ensayos clínicos registrados y solo se dispone de **3 publicaciones** de contexto (revisiones y estudios sobre otras condiciones), ninguna de las cuales estudia directamente a la desvenlafaxina en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno obsesivo-compulsivo (obsessive-compulsive disorder) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (16 de 16) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 16 (vigentes: 16) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Desvenlafaxina es un IRSN y el metabolito activo de la venlafaxina. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Desvenlafaxina (traducción no oficial): «Se desconoce el mecanismo exacto de la acción antidepresiva de la desvenlafaxina, pero se cree que está relacionado con la potenciación de la serotonina y la norepinefrina en el sistema nervioso central mediante la inhibición de su recaptación. Los estudios no clínicos han demostrado que la desvenlafaxina es un IRSN potente y selectivo.» Texto original en inglés: "The exact mechanism of the antidepressant action of desvenlafaxine is unknown, but is thought to be related to the potentiation of serotonin and norepinephrine in the central nervous system, through inhibition of their reuptake. Non-clinical studies have shown that desvenlafaxine is a potent and selective SNRI." ([DailyMed: Pristiq Extended-Release (desvenlafaxine succinate) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f43610c-f290-46ea-d186-4f998ed99fce), versión del 2026-04-28; consultado el 2026-11-19). Según la información conocida, la inhibición de la recaptación de serotonina es la base farmacológica del tratamiento del trastorno obsesivo-compulsivo (ISRS, clomipramina), por lo que existe una plausibilidad a nivel de clase.

La venlafaxina, fármaco emparentado, tiene algunos datos de apoyo en este trastorno, pero para la desvenlafaxina no hay evidencia directa. El puntaje alto (0,9991) refleja la cercanía en la red del modelo con otros agentes serotoninérgicos y no constituye evidencia clínica.

Por ello, aunque el vínculo mecanístico es verosímil, la hipótesis sigue siendo una pregunta de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Revisión | Expert Opinion on Pharmacotherapy | Revisión de estudios doble ciego de antidepresivos con marcado efecto serotoninérgico en el trastorno obsesivo-compulsivo; confirma el papel clave del sistema serotoninérgico. No evalúa desvenlafaxina. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | ECA | Psychiatry and Clinical Psychopharmacology | Aumento con risperidona en trastorno de síntomas somáticos resistente a antidepresivos; menciona el trastorno obsesivo-compulsivo solo como contexto. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Revisión | Cureus | Revisión sobre depresión posparto; menciona el trastorno obsesivo-compulsivo como complicación posterior para la madre. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49725 | DROSIX | 50 mg comprimidos de liberación prolongada x 30 | No registrada |
| 48450 | PRISTIQ | 100 mg comprimidos de liberación prolongada x 30 | No registrada |
| 50767 | DESLAFAX | 100 mg comprimidos de acción prolongada x 30 | No registrada |
| 48657 | IXIUM | 100 mg comprimidos de liberación prolongada x 10 | No registrada |
| 49282 | ALFAXIN 100 | 100 mg comprimidos recubiertos de liberación prolongada x 30 | No registrada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ningún estudio que evalúe directamente la desvenlafaxina en el trastorno obsesivo-compulsivo; el puntaje del modelo solo indica cercanía con otros fármacos serotoninérgicos y no sustituye la evidencia clínica. Por ello el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la desvenlafaxina
- Revisión sistemática de la evidencia con venlafaxina y otros IRSN en trastorno obsesivo-compulsivo
- Ensayos clínicos o estudios que evalúen directamente la desvenlafaxina en esta enfermedad
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Pristiq Extended-Release (desvenlafaxine succinate) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f43610c-f290-46ea-d186-4f998ed99fce) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

