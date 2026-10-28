---
layout: default
title: Lornoxicam
parent: Evidencia Alta (L1-L2)
nav_order: 182
evidence_level: L2
indication_count: 8
monitor_inn: "LORNOXICAM"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "tendinitis", "idiopathic granulomatous myositis"]
last_modified_at: 2026-10-23
description: "Lornoxicam: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L2). Indicación original: No disponible: el texto de indicación de la autorización local está v…"
---

# Lornoxicam
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

## Lornoxicam: De Uso Analgésico/Antiinflamatorio a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Lornoxicam es un antiinflamatorio no esteroideo (AINE) de la clase de los oxicams, con propiedades analgésicas, antiinflamatorias y antipiréticas. El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **1 ensayo clínico** de Fase 2 completado y **2 publicaciones** (revisiones) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible: el texto de indicación de la autorización local está vacío |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, lornoxicam es un inhibidor no selectivo de COX-1 y COX-2 de la clase de los oxicams. Al inhibir la síntesis de prostaglandinas, reduce el dolor y la inflamación.

Mecanísticamente, esa inhibición podría disminuir la inflamación neurogénica y la sensibilización de las vías trigeminovasculares, que es la misma lógica con la que se usan los AINE en la migraña aguda. El puntaje alto del modelo (0.9987) es coherente con esta hipótesis.

Una revisión de 1992 sobre AINE en migraña menciona a lornoxicam entre los fármacos evaluados. Sin embargo, el texto disponible no permite confirmar los resultados específicos para este fármaco.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00293657](https://clinicaltrials.gov/study/NCT00293657) | Fase 2 | Completado | 150 | Estudio aleatorizado, doble ciego, controlado con placebo, de dosis única de lornoxicam intravenoso (8 mg o 16 mg) en el tratamiento agudo de la cefalea de la migraña (2005-2006). No se dispone de resultados publicados en los datos compilados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1495823](https://pubmed.ncbi.nlm.nih.gov/1495823/) | 1992 | Revisión | Pathologie-biologie | Revisa estudios controlados de AINE en ataques de migraña y profilaxis, incluyendo lornoxicam entre los fármacos evaluados |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Revisión | Drugs | Revisión de farmacología y potencial terapéutico de lornoxicam en cuadros dolorosos e inflamatorios; no se centra específicamente en migraña |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46072 | XEFO RAPID (Takeda) | 8 mg comp. rec. x 30 | No disponible en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Predicciones del Modelo (Referencia)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Cefalea (headache disorder) | 0.9980 | L2 | Se apoya en el mismo ensayo y las mismas publicaciones que migraña; no es evidencia independiente |
| Tendinitis | 0.9972 | L5 | El único estudio (2017) evaluó el síndrome de pinzamiento subacromial, no tendinitis; lornoxicam inyectable fue inferior a betametasona |
| Migraña con aura del tronco encefálico | 0.9985 | L5 | Sin estudios específicos |
| Cefalea autonómica trigeminal | 0.9975 | L5 | Sin evidencia directa |
| Mielitis/miositis granulomatosa idiopática | 0.9970 | L5 | Solo predicción del modelo |
| Síndrome de braquidactilia-sindactilia | 0.9982 | L5 | Sin vínculo mecanístico plausible; probable artefacto del modelo |
| Síndrome de microftalmia colobomatosa-displasia rizomélica | 0.9981 | L5 | Sin vínculo mecanístico plausible; probable artefacto del modelo |

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado, aleatorizado y controlado con placebo, que estudia directamente la cefalea de la migraña, además de un mecanismo plausible (inhibición de COX). Sin embargo, no se dispone de resultados de eficacia ni de datos de seguridad locales, por lo que se recomienda avanzar con cautela.

**Para avanzar se necesita:**
- Obtener los resultados del ensayo NCT00293657 (eficacia y seguridad).
- Descargar y analizar el prospecto de ANMAT (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Verificar la vía de administración: el ensayo usó lornoxicam intravenoso, mientras que la presentación local es un comprimido recubierto de 8 mg.
- Aclarar la indicación aprobada en la autorización local, cuyo texto está vacío.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

