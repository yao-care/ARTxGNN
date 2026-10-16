---
layout: default
title: Dexketoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dexketoprofen: nueva indicación predicha, Tendinitis (primera predicción) (nivel de evidencia L5). Indicación original: No disponible (los textos de indicación de las autorizaciones están v…"
---

# Dexketoprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dexketoprofeno: De Indicación No Registrada en la Licencia a Tendinitis (y Migraña como Candidata con Mayor Evidencia)

> **Nota sobre la selección de la indicación:** la predicción de mayor puntaje del modelo es **tendinitis**, pero solo cuenta con una publicación indirecta (L4). La indicación con evidencia clínica sustancial entre las predichas es la **migraña** (L1), por lo que se la analiza en detalle en las secciones de evidencia.

## Resumen en Una Frase

Dexketoprofeno es un antiinflamatorio no esteroideo (AINE) comercializado en Argentina, utilizado como analgésico (comprimidos, solución inyectable y gel). Los textos de indicación aprobada no figuran en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **tendinitis** (puntaje 99.90%, sin ensayos clínicos y con 1 publicación indirecta). Entre las demás predicciones, **migraña** es la mejor respaldada: **5 ensayos clínicos** y **más de 20 publicaciones** (incluidos un metaanálisis y varios ECA).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Tendinitis (primera predicción); migraña (mejor respaldada) |
| Puntaje de Predicción TxGNN | Tendinitis: 99.90%; Migraña: 99.87% |
| Nivel de Evidencia | Tendinitis: L4; Migraña: L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Tendinitis: Hold; Migraña: Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, dexketoprofeno es un AINE inhibidor de la ciclooxigenasa (COX-1/COX-2), que reduce la síntesis de prostaglandinas y, con ello, la inflamación y el dolor.

**Tendinitis:** la reducción de la inflamación mediada por prostaglandinas es plausible para la inflamación tendinosa. Sin embargo, el único respaldo es un ECA en dolor musculoesquelético no traumático en urgencias (dexketoprofeno IV vs. paracetamol), que es evidencia indirecta y no específica de tendinitis.

**Migraña:** la inhibición de COX disminuye la inflamación neurogénica y la sensibilización nociceptiva durante el ataque agudo. Esta es la predicción con mayor respaldo: ensayos aleatorizados controlados con placebo, un estudio de fase II y un metaanálisis de ECA. La evidencia corresponde al tratamiento del ataque agudo.

**Otras predicciones** (fibromialgia, miositis fibrosa, miositis granulomatosa idiopática, artritis reumatoide, exostosis, hipotricosis congénita con milia) se basan solo en la predicción del modelo. Para la artritis reumatoide el uso de AINE como alivio sintomático es plausible a nivel de clase, pero no modifica la enfermedad. Para la hipotricosis congénita con milia no hay vínculo mecanístico plausible y el puntaje probablemente refleja un artefacto del grafo.

---

## Evidencia de Ensayos Clínicos

**Tendinitis:** actualmente no hay ensayos clínicos relacionados registrados.

**Migraña** (ensayos más relevantes):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Fase 4 | Completado | 224 | Dexketoprofeno IV vs. placebo en ataque de migraña en urgencias |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Fase 4 | Completado | 200 | Dexketoprofeno IV vs. paracetamol en cefalea por migraña aguda |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Fase 4 | Completado | 160 | Ibuprofeno IV vs. dexketoprofeno IV en cefalea relacionada con migraña |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | No especificada | Completado | 150 | Metoclopramida vs. dexketoprofeno vs. combinación en ataque agudo de migraña |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Fase 4 | Desconocido | 210 | Paracetamol, dexketoprofeno e ibuprofeno IV sobre escala VAS en migraña aguda |

---

## Evidencia de Literatura

**Tendinitis:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | ECA | Am J Emerg Med | Dexketoprofeno IV vs. paracetamol en dolor musculoesquelético no traumático en urgencias (evidencia indirecta) |

**Migraña** (publicaciones más relevantes):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Metaanálisis de ECA | Medicine | Eficacia de dexketoprofeno vs. placebo en el control del dolor del ataque de migraña |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | ECA | Cephalalgia | Dexketoprofeno IV vs. placebo en migraña en urgencias |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | ECA fase II | J Pain | Dexketoprofeno trometamol 25 y 50 mg vs. placebo, estudio cruzado doble ciego (93 pacientes) |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | ECA | Am J Emerg Med | Metoclopramida vs. dexketoprofeno vs. combinación en ataque agudo de migraña |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | ECA | Emerg Med J | Paracetamol IV vs. dexketoprofeno en migraña aguda en urgencias |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | ECA | Cephalalgia | Frovatriptán + dexketoprofeno vs. frovatriptán solo en migraña con o sin aura |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | ECA | Expert Rev Neurother | Eficacia y tolerabilidad de frovatriptán y dexketoprofeno en ataques agudos |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía | Headache | Actualización 2025 de la guía de la AHS sobre tratamiento parenteral de la migraña en urgencias |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | ECA | Ann Saudi Med | Mesoterapia intradérmica vs. dexketoprofeno IV en migraña sin aura |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Revisión sistemática / metaanálisis en red | BMC Neurol | Metoclopramida frente a otros antimigrañosos (evidencia indirecta para dexketoprofeno) |

**Otros tipos de cefalea:** la evidencia es limitada; incluye un ECA de lidocaína vs. dexketoprofeno en cefalea tensional ([33423013](https://pubmed.ncbi.nlm.nih.gov/33423013/), 2021) y una serie de casos de cefalea asociada a COVID-19 ([39063663](https://pubmed.ncbi.nlm.nih.gov/39063663/), 2024). Para **migraña con aura de tronco encefálico** solo hay estudios de migraña aguda general (nivel L2, "pregunta de investigación"); la aplicabilidad al subtipo es inferida.

---

## Información de Mercado en Argentina

Se listan 5 de las 10 autorizaciones vigentes (todas de monodroga). Los textos de indicación aprobada no están disponibles en los datos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 29099 | ENANTYUM | Comprimidos 25 mg x 40 | Siegfried |
| 30573 | ENANTYUM | Gel x 60 g (tópico) | Siegfried |
| 33647 | ENANTYUM | Inyectable 50 mg/2 ml x 6 | Siegfried |
| 53512 | IDOLGINA | Comprimidos recubiertos ranurados 25 mg x 20 | Baliarda |
| 52060 | TACRAF GEL | Gel x 60 g (tópico) | Trb-Pharma |

---

## Consideraciones de Seguridad

No se dispone de datos de advertencias ni contraindicaciones del prospecto, y no se encontraron interacciones farmacológicas en la consulta realizada. Consultar el prospecto para información de seguridad.

Como precauciones de clase para AINE (según las salvaguardas señaladas en la evaluación): riesgos gastrointestinales, renales y cardiovasculares, y riesgo de cefalea por abuso de medicación en el uso en cefaleas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold para tendinitis (predicción principal); Proceed with Guardrails para migraña**

**Justificación:**
- Tendinitis, con el mayor puntaje del modelo, solo tiene evidencia indirecta (L4), por lo que se mantiene en espera. Migraña cuenta con ECA controlados con placebo, un estudio de fase II y un metaanálisis (L1), aunque los ensayos son de fase 4/fase 2 y no ensayos clásicos de fase 3 de registro, y la evidencia se limita al tratamiento del ataque agudo.
- Las demás predicciones (fibromialgia, miositis, artritis reumatoide, exostosis, hipotricosis congénita con milia) quedan en espera por falta de evidencia (L5).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) antes del cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Verificar la indicación aprobada actual en las autorizaciones de ANMAT para confirmar si la migraña o el dolor agudo ya están incluidos.
- Para tendinitis: ensayos específicos en tendinopatía, con evaluación de la compatibilidad de vía de administración (por ejemplo, gel tópico frente a vía oral).
- Para migraña: definir población, vía (oral frente a IV) y plan de monitoreo de seguridad gastrointestinal, renal y cardiovascular.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

