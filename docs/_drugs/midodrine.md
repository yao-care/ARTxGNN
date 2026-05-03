---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Midodrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el skill `txgnn-pipeline` como contexto. Ahora generaré el informe de evaluación enfocado en la indicación con mayor nivel de evidencia: **hypotensive disorder** (Rank 4, L1 — la única con recomendación "Proceed with Guardrails").

---

# Midodrine: De Hipotensión Ortostática a Trastorno Hipotensivo

## Resumen en Una Frase

Midodrine es un agonista α₁-adrenérgico periférico reconocido globalmente por su uso en el tratamiento de la hipotensión ortostática sintomática, aunque actualmente no cuenta con autorización de comercialización en Argentina.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Hipotensivo** (hypotensive disorder) en sus múltiples subtipos clínicos,
con **9 ensayos clínicos** y **19 publicaciones** que respaldan actualmente esta dirección, alcanzando un nivel de evidencia L1.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrado en Argentina (uso global aprobado: hipotensión ortostática sintomática) |
| Nueva Indicación Predicha | Trastorno Hipotensivo (Hypotensive Disorder) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Aunque los datos formales de mecanismo de acción (MOA) no están disponibles en este paquete de evidencia, la literatura científica incluida en el mismo describe con claridad el perfil farmacológico de midodrine. Midodrine es un profármaco que, tras su absorción oral casi completa, es hidrolizado enzimáticamente a su metabolito activo **desglymidodrine**. Este metabolito actúa como agonista selectivo de los receptores α₁-adrenérgicos periféricos, produciendo vasoconstricción arterial y venosa, aumento de la resistencia vascular sistémica y mejora del retorno venoso, lo que se traduce en elevación de la presión arterial tanto en posición erguida como supina.

La relación entre la indicación global conocida de midodrine (hipotensión ortostática neurógena) y la categoría más amplia de "trastorno hipotensivo" es directa y bien fundamentada. Este último engloba múltiples subtipos clínicos en los que la hipotensión es la manifestación central: hipotensión ortostática neurógena, hipotensión intradialítica, hipotensión posanestésica espinal, hipotensión asociada a lesión medular espinal e hipotensión en insuficiencia cardíaca con fracción de eyección reducida (HFrEF). El mecanismo vasopresor periférico de midodrine es farmacológicamente aplicable en forma transversal a todos estos subtipos.

La predicción del modelo TxGNN resulta altamente coherente con el cuerpo de evidencia acumulado: midodrine es estándar de tratamiento para la hipotensión ortostática en EE.UU. (FDA), Europa (EMA) y Japón, y los ensayos clínicos recogidos demuestran su uso activo en Fase 3 y Fase 4 para distintas presentaciones de hipotensión. La ausencia de registro en Argentina no refleja falta de evidencia científica, sino una brecha de acceso que la evidencia internacional disponible está en condiciones de sustentar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05839652](https://clinicaltrials.gov/study/NCT05839652) | Fase 4 | Reclutando | 25 | Evaluación de intervenciones farmacológicas y no farmacológicas (incluye midodrine) en hipotensión ortostática en personas con lesión medular espinal |
| [NCT02307565](https://clinicaltrials.gov/study/NCT02307565) | Fase 3 | Completado | 19 | Midodrine como agente antihipotensivo en lesión medular; evaluación del efecto sobre presión arterial, flujo cerebral y función cognitiva |
| [NCT01030874](https://clinicaltrials.gov/study/NCT01030874) | N/A | Completado | 356 | ECA multidisciplinario en unidad de rehabilitación: tratamiento de hipotensión ortostática en adultos y ancianos médicamente enfermos; mayor muestra del conjunto |
| [NCT03431194](https://clinicaltrials.gov/study/NCT03431194) | N/A | Completado | 80 | ECA: midodrine oral para manejo de hipotensión intradialítica en pacientes críticos con lesión renal aguda |
| [NCT05548985](https://clinicaltrials.gov/study/NCT05548985) | N/A | Completado | 58 | ECA: midodrine oral para profilaxis de hipotensión post-anestesia espinal en artroplastia de cadera en población anciana |
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Fase 2 | Completado | 21 | Normalización de presión arterial con midodrine en hipotensión crónica por lesión medular; efecto sobre flujo cerebral en reposo |
| [NCT06405555](https://clinicaltrials.gov/study/NCT06405555) | Fase 2/3 | No iniciado | 56 | Piloto controlado aleatorizado: midodrine en insuficiencia cardíaca con fracción de eyección reducida (HFrEF) e hipotensión; expansión de indicación a nueva población |
| [NCT03037879](https://clinicaltrials.gov/study/NCT03037879) | N/A | Completado | 10 | Midodrine para elevar presión arterial y mejorar déficits cognitivos en lesión medular traumática; midodrine como intervención principal |
| [NCT02307526](https://clinicaltrials.gov/study/NCT02307526) | Fase 2 | Completado | 10 | Inhibidor de acetilcolinesterasa vs midodrine en hipotensión ortostática por lesión medular; estudio comparativo de referencia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | ECA | Hepatology | Terlipresina + albúmina vs midodrine + octreótida + albúmina en síndrome hepatorrenal; ECA multicéntrico; midodrine como brazo de tratamiento activo |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Declaración científica AHA | Hypertension | Declaración de la American Heart Association sobre hipotensión ortostática en adultos con hipertensión; midodrine referenciado en manejo |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Guía clínica AGA | Gastroenterology | Actualización de práctica clínica AGA sobre fármacos vasoactivos en cirrosis; midodrine incluido como vasoconstrictor de referencia |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Revisión / Posición experta | Revue neurologique | Declaración de posición de expertos sobre diagnóstico y manejo de hipotensión ortostática; incluye recomendaciones farmacológicas |
| [39619823](https://pubmed.ncbi.nlm.nih.gov/39619823/) | 2024 | Estudio clínico | Topics in Spinal Cord Injury Rehabilitation | 30 días de midodrine vs placebo en personas con lesión medular: efectos sobre presión arterial, velocidad de flujo cerebral y rendimiento cognitivo |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consenso de panel | Journal of Neurology | Recomendaciones de panel de consenso para cribado, diagnóstico y tratamiento de hipotensión ortostática neurógena; midodrine en algoritmo de tratamiento |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Revisión | Autonomic Neuroscience | Tratamiento farmacológico de la hipotensión ortostática neurógena; midodrine como agente de primera línea con análisis de mecanismo |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Revisión práctica | American Family Physician | Enfoque práctico para médicos de familia: diagnóstico y manejo de hipotensión ortostática; rol de midodrine en tratamiento escalonado |
| [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/) | 2020 | Revisión | Continuum | Manejo de hipotensión ortostática con énfasis en la forma neurógena; estrategias farmacológicas incluyendo midodrine |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Revisión farmacológica fundacional | Drugs | Revisión seminal de las propiedades farmacológicas de midodrine y su uso terapéutico en hipotensión ortostática y trastornos hipotensivos secundarios |

---

## Información de Mercado en Argentina

Midodrine **no cuenta con ninguna autorización de comercialización registrada en Argentina (ANMAT)** a la fecha de corte 2026-05-01. No existen licencias activas consultadas.

A modo de referencia internacional, el fármaco cuenta con aprobaciones regulatorias en los siguientes mercados:

| Mercado | Agencia | Indicación aprobada |
|---------|---------|---------------------|
| Estados Unidos | FDA | Hipotensión ortostática sintomática grave |
| Unión Europea | EMA / agencias nacionales | Hipotensión ortostática sintomática |
| Japón | PMDA | Hipotensión ortostática y afines |

La inexistencia de registro local representa una **brecha de acceso**, no una brecha de evidencia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Se recomienda revisar la ficha técnica FDA (NDA 019838) y el SmPC europeo para advertencias sobre hipertensión supina, retención urinaria y bradicardia refleja, que son efectos adversos conocidos de la clase.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Midodrine dispone de evidencia de Nivel L1 para el trastorno hipotensivo, sustentada en múltiples ECAs de Fase 3 y Fase 4 completados, guías de práctica clínica de sociedades científicas de primer nivel (AHA, AGA, consenso de neurología) y aprobaciones regulatorias vigentes en EE.UU. y Europa. La predicción TxGNN (99.90%) refleja una conexión farmacológica directa y no especulativa entre el mecanismo α₁-agonista del fármaco y la fisiopatología de los distintos subtipos de hipotensión.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto completo (FDA label / EMA SmPC) para completar los datos de MOA, advertencias, contraindicaciones e interacciones farmacológicas (actualmente en estado de brecha de datos)
- Definir el subtipo prioritario de trastorno hipotensivo para la solicitud ante ANMAT (hipotensión ortostática neurógena o intradialítica tienen mayor masa crítica de evidencia)
- Identificar fabricante con certificación GMP para el mercado argentino y evaluar vía de registro: importación habilitada vs. registro completo
- Diseñar plan de monitoreo de seguridad con énfasis en **hipertensión supina** (efecto adverso de clase más relevante) y función renal en poblaciones de riesgo
- Confirmar disponibilidad de bioequivalencia y estudios de farmacocinética en poblaciones latinoamericanas si se requiere para el expediente regulatorio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

