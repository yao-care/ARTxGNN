---
layout: default
title: Rivastigmina
parent: Solo Predicción del Modelo (L5)
nav_order: 319
evidence_level: L5
indication_count: 1
drugbank_id: DB00989
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
last_modified_at: 2026-11-16
description: "Rivastigmina: nueva indicación predicha, Glaucoma (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Rivastigmina
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

## Rivastigmina: Glaucoma
{: .text-alpha }

## Resumen en Una Frase

Rivastigmina es un inhibidor pseudo-irreversible de las colinesterasas (acetilcolinesterasa y butirilcolinesterasa), comercializado en Argentina en cápsulas y parches.
El modelo TxGNN predice que podría ser efectivo para **glaucoma (glaucoma)**, con un puntaje de 0.9927.
Actualmente no hay ensayos clínicos registrados y solo **3 publicaciones** respaldan esta dirección (un estudio preclínico en conejos y dos revisiones).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 0.9927 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según el conocimiento farmacológico general, la rivastigmina inhibe de forma pseudo-irreversible la acetilcolinesterasa y la butirilcolinesterasa, lo que eleva los niveles de acetilcolina en los receptores muscarínicos.

En el ojo, un mayor tono colinérgico puede aumentar la contracción del músculo ciliar y facilitar el drenaje a través de la malla trabecular, reduciendo la presión intraocular (PIO). Es la misma lógica farmacológica de agentes colinérgicos y anticolinesterásicos clásicos usados en glaucoma, como pilocarpina, fisostigmina y ecotiofato. El puntaje alto del modelo es coherente con esta plausibilidad mecanística.

La evidencia es limitada: un estudio preclínico muestra que la rivastigmina tópica redujo la PIO en conejos normotensos. No se dispone de datos de eficacia ni de seguridad en humanos con glaucoma.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclínico (conejo) | J Ocul Pharmacol Ther | La rivastigmina tópica, inhibidor selectivo de la acetilcolinesterasa, redujo la presión intraocular en conejos normotensos |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revisión / genética de sistemas y modelado molecular | Front Mol Biosci | Analiza los agentes colinérgicos para reducir la PIO; los agonistas M3 aprobados tienen limitaciones por efectos adversos colinérgicos sistémicos |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisión (literatura de patentes) | Expert Opin Ther Pat | Actualiza inhibidores y reactivadores de acetilcolinesterasa; menciona la relevancia terapéutica de la inhibición leve en Alzheimer, miastenia gravis y glaucoma |

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones vigentes de productos de rivastigmina de un solo principio activo; la lista puede ser parcial. Principales registros:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56217 | REMIZERAL PARCHES | 9.5 mg parches x 30 | No registrada en los datos locales |
| 45808 | RIVASMINA | 1.5 mg cáps. x 14 | No registrada en los datos locales |
| 21128 | EXELON | 3 mg cáps. x 28 | No registrada en los datos locales |
| 49522 | EXELON PARCHE 15 | 27 mg parches x 30 | No registrada en los datos locales |
| 42089 | EXELON PARCHE 10 | 18 mg parches x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos compilados no incluyen advertencias, contraindicaciones ni interacciones farmacológicas. Como contexto general, la bibliografía señala que los efectos adversos colinérgicos sistémicos limitan el uso de agentes colinérgicos para reducir la PIO, y la tolerabilidad en la superficie ocular de la rivastigmina no está evaluada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto y el mecanismo es plausible, pero la única evidencia que estudia directamente el glaucoma es un estudio preclínico en conejos. No hay datos en humanos ni formulación oftálmica disponible.

**Para avanzar se necesita:**
- Datos de eficacia y seguridad en humanos con glaucoma (estudios clínicos)
- Desarrollo y evaluación de una formulación oftálmica y su tolerabilidad en la superficie ocular
- Evaluación de efectos adversos colinérgicos sistémicos
- Prospecto de ANMAT con advertencias y contraindicaciones
- Datos detallados del mecanismo de acción (DrugBank)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

