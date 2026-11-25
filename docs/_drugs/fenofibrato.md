---
layout: default
title: Fenofibrato
parent: Solo Predicción del Modelo (L5)
nav_order: 174
evidence_level: L5
indication_count: 1
drugbank_id: DB01039
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-25
description: "Fenofibrato: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5)."
---

# Fenofibrato
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

## Fenofibrato: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Fenofibrato es un agonista del receptor PPARα que se comercializa en Argentina y actúa sobre el metabolismo de los lípidos. El modelo TxGNN predice que podría ser útil para la **deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)**. Hasta ahora no hay **ensayos clínicos** registrados y solo existen **3 publicaciones** de tipo mecanístico o preclínico, ninguna de las cuales estudia esta enfermedad en pacientes.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El fenofibrato es un agonista de PPARα que eleva el colesterol HDL y reduce los triglicéridos. Lo hace en parte modulando la remodelación de las lipoproteínas: induce la proteína de transferencia de fosfolípidos (PLTP), aumenta la expresión de apoA-I y apoA-II e incrementa la actividad de la lipoproteína lipasa. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en la literatura citada.

La deficiencia de la proteína de transferencia de ésteres de colesterol (CETP) es una condición genética. Se caracteriza por un HDL-C muy elevado y por una transferencia alterada de ésteres de colesterol entre el HDL y las lipoproteínas con apoB. La relación con el fenofibrato es **indirecta**. La literatura describe sus efectos sobre el metabolismo del HDL y su combinación con un inhibidor de CETP en ratones (PMID 20332533). También describe el agrandamiento del HDL por inducción de PLTP mediada por PPARα (PMID 11342537).

Hay una limitación importante. Quienes tienen deficiencia de CETP ya presentan HDL-C alto, así que elevarlo aún más no es un objetivo terapéutico evidente. No hay evidencia de beneficio clínico del fenofibrato en estos pacientes. El puntaje alto del modelo es una predicción computacional y probablemente refleja cercanía entre redes del metabolismo lipídico, no una relación terapéutica demostrada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Estudio preclínico (ratones transgénicos) | J Cardiovasc Pharmacol Ther | En ratones con apoB100 y CETP humanas, la inhibición de CETP con torcetrapib combinada con el agonismo PPARα del fenofibrato modificó el perfil lipídico. No es un estudio en pacientes con deficiencia de CETP. |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Estudio preclínico/mecanístico (ratones) | J Biol Chem | En ratones, el fenofibrato induce el gen de PLTP, lo que explica el agrandamiento del HDL rico en ésteres de colesterol. |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Estudio mecanístico/traslacional | Front Physiol | Analiza la relación entre HDL-C, función del HDL, excreción fecal de colesterol y eflujo de colesterol. Sugiere que la funcionalidad del HDL importa más que su nivel. No aporta evidencia de tratamiento con fenofibrato en deficiencia de CETP. |

Ninguna de estas publicaciones estudia directamente la deficiencia de CETP en pacientes tratados con fenofibrato.

---

## Información de Mercado en Argentina

Estado de mercado: ✓ Comercializado. A continuación se listan cinco de las autorizaciones registradas.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 47731 | LIPTUIN | 200 mg cáps.x 30 | Temis-Lostaló | Vigente |
| 52158 | FENOSANE | 200 mg cáps.x 30 | Eczane | Vigente |
| 35060 | CRAVERIL | comp.rec.x 30 | Craveri | Vigente |
| 1289 | PROCETOKEN | 100 mg comp.x 60 | Laboratorios Be | Vigente |
| 28384 | MINUSLIP | 200 mg cáps.x 30 | Teva Argentina | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción se apoya solo en el modelo y en estudios preclínicos o mecanísticos indirectos, sin ensayos clínicos ni estudios en pacientes con esta enfermedad. Por eso el nivel de evidencia es L5.
- Además, no está claro que elevar el HDL sea un objetivo terapéutico en una condición que ya cursa con HDL-C alto.

**Para avanzar se necesita:**
- Evidencia directa en pacientes con deficiencia de CETP, como series de casos o estudios observacionales.
- Una justificación fisiopatológica de qué beneficio clínico se buscaría con el fenofibrato en esta condición.
- Datos detallados del mecanismo de acción.
- Información de seguridad del prospecto local (advertencias y contraindicaciones).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

