---
layout: default
title: Gemfibrozil
parent: Solo Predicción del Modelo (L5)
nav_order: 151
evidence_level: L5
indication_count: 9
monitor_inn: "GEMFIBROZIL"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
last_modified_at: 2026-10-27
description: "Gemfibrozil: nueva indicación predicha, Artritis reumatoide (rheumatoid arthritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Gemfibrozil
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

## Gemfibrozil: inhibidor de lípidos agonista de PPAR-alfa → artritis reumatoide (rheumatoid arthritis)
{: .text-alpha }

## Resumen en Una Frase

Gemfibrozil es un fármaco hipolipemiante que actúa sobre los receptores PPAR-alfa. El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide (rheumatoid arthritis)**, pero actualmente no hay ensayos clínicos registrados y solo existe literatura indirecta (modelos animales y estudios con otros fibratos), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Artritis reumatoide (rheumatoid arthritis) |
| Puntaje de Predicción TxGNN | 0,9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 7 de 7) |
| Número de Autorizaciones | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este fármaco. Según la información conocida, gemfibrozil es un agonista de PPAR-alfa, una clase de fármacos que regula el metabolismo de los lípidos.

Mecanísticamente, la activación de PPAR podría reducir citocinas proinflamatorias y modular respuestas de los linfocitos T (por ejemplo, la regulación de Foxp3), algo plausible en una artritis autoinmune. Sin embargo, este razonamiento es indirecto.

Los datos compilados incluyen un estudio en modelo experimental de artritis con bezafibrato (otro fibrato, agonista pan-PPAR) y un trabajo de 2019 en ratas con artritis inducida por adyuvante que combina gemfibrozil con una dosis reducida de esteroides. Ningún estudio evalúa directamente gemfibrozil en pacientes con artritis reumatoide. Por ello, el nivel de evidencia se mantiene en L5, ya que ninguna publicación citada estudia esta enfermedad en humanos con el fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclínico (modelo en ratas) | Modern Rheumatology | Gemfibrozil combinado con una dosis reducida de prednisolona en artritis inducida por adyuvante en ratas; se evaluó si logra un control similar al de la dosis completa de esteroides |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclínico (otro fibrato) | International Immunopharmacology | Bezafibrato, agonista pan-PPAR, atenúa la artritis experimental mediante la modulación de vías inflamatorias dependientes de PPAR, con énfasis en PPAR-γ |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclínico (mecanístico) | Journal of Immunology | Estudio sobre la regulación de Foxp3 en linfocitos T por óxido nítrico; relación solo mecanística e indirecta |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revisión | American Journal of Clinical Dermatology | Revisión sobre eritema palmar; no es relevante para gemfibrozil en artritis reumatoide |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 13209 | LOPID UD | 900 mg comp. x 15 | No registrada en los datos locales |
| 13210 | LOPID UD | 900 mg comp. x 30 | No registrada en los datos locales |
| 6327 | LOPID 600 | comp. x 60 | No registrada en los datos locales |
| 6326 | LOPID 600 | comp. x 30 | No registrada en los datos locales |
| 45027 | HIPOLIXAN 900 | comp. x 30 | No registrada en los datos locales |

Se muestran las 5 autorizaciones principales; todas las autorizaciones registradas están vigentes.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron interacciones de nivel mayor con eluxadoline, loperamida, pioglitazona, repaglinida, rosuvastatina y simvastatina. Con las estatinas existe un riesgo particular de miopatía y rabdomiólisis. También hay interacciones de nivel moderado con clorpropamida, nateglinida, rosiglitazona, rifaximina, ácido quenodesoxicólico, tolazamida y diversas insulinas (aspart, degludec, detemir, glargina, glulisina, humana).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Pese al puntaje alto de predicción (0,9990), no existen ensayos clínicos ni estudios en humanos que evalúen gemfibrozil en artritis reumatoide; la única base son datos preclínicos e indirectos. No hay evidencia suficiente para avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen directamente gemfibrozil (no otros fibratos) en modelos de artritis reumatoide, con diseño metodológico verificable
- Datos detallados del mecanismo de acción aplicables a la inflamación articular
- Revisión del prospecto de ANMAT para completar advertencias y contraindicaciones
- Evaluación de seguridad en una población con artritis reumatoide, que suele recibir medicación concomitante con posibles interacciones
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

