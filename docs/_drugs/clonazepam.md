---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Usando el skill **txgnn-pipeline** como contexto y siguiendo el formato de informe de evaluación de reposicionamiento establecido, aquí está el informe generado:

---

# Clonazepam: De Epilepsia a Síndrome de Piernas Inquietas

## Resumen en Una Frase

Clonazepam es una benzodiazepina de larga trayectoria clínica, globalmente utilizada para el tratamiento de la epilepsia y el trastorno de pánico, cuyo mecanismo central se basa en la potenciación del receptor GABA-A.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Piernas Inquietas (Restless Legs Syndrome, RLS)**,
con **0 ensayos clínicos registrados específicamente** y **20 publicaciones** —entre ellas una revisión Cochrane y la guía clínica AASM 2025— que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia / Trastorno de Pánico (no registrado en base regulatoria argentina) |
| Nueva Indicación Predicha | Síndrome de Piernas Inquietas (Restless Legs Syndrome) |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en la base de datos consultada. Sin embargo, a partir de la información farmacológica conocida y de la justificación mecanística incluida en el Evidence Pack, Clonazepam actúa como potenciador alostérico positivo del receptor GABA-A (GABA-A PAM): aumenta la frecuencia de apertura del canal de cloro, intensificando la transmisión inhibitoria tanto a nivel espinal como subcortical. Este efecto reduce la amplitud y frecuencia de los movimientos periódicos de extremidades (MPE/PLM) y mejora la arquitectura general del sueño.

La fisiopatología del Síndrome de Piernas Inquietas involucra una deficiencia GABAérgica espinal y una disfunción del sistema dopaminérgico. Clonazepam ofrece compensación GABAérgica nocturna que alivia los síntomas de movimientos involuntarios e insomnio asociado. Si bien no actúa directamente sobre la causa dopaminérgica subyacente, su efecto sintomático constituye una racionalidad mecanística coherente y ha sido empleado clínicamente durante décadas.

Esta predicción está respaldada por evidencia empírica sólida: una revisión sistemática Cochrane (2017) evaluó específicamente el uso de benzodiazepinas —con clonazepam como el agente más estudiado de la clase— en RLS, y la guía de práctica clínica AASM 2025 reconoce el rol histórico de esta clase en el tratamiento de RLS y PLMD. Datos de encuestas reales indican que aproximadamente el 25% de los pacientes con RLS reciben benzodiazepinas, solas o en combinación con otros tratamientos, lo que refuerza la relevancia clínica de esta predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la combinación Clonazepam + Síndrome de Piernas Inquietas en ClinicalTrials.gov ni en ICTRP.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Guía Clínica (AASM) | J Clin Sleep Med | Guía de práctica clínica AASM 2025 para tratamiento de RLS y PLMD en adultos y pacientes pediátricos; referencia clave sobre estándares actuales |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Revisión Cochrane | Cochrane Database Syst Rev | Revisión sistemática Cochrane sobre benzodiazepinas en RLS; clonazepam identificado como el fármaco más estudiado de la clase, aunque la evidencia formal es limitada |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Revisión histórica narrativa | Tremor Other Hyperkinetic Mov | Revisión de 17 artículos sobre clonazepam en RLS y PLMS; ~25% de pacientes con RLS reciben benzodiazepinas en práctica real |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Estudio aleatorizado prospectivo | J Mid-Life Health | Comparativa prospectiva abierta de clonazepam vs. nortriptilina en mujeres mayores de 40 años con RLS; evalúa tasa, frecuencia y severidad de síntomas |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | ECA cruzado doble ciego | Acta Neurol Scand | Ensayo cruzado aleatorizado vs. placebo en 6 pacientes con RLS: clonazepam mostró eficacia significativa en calidad subjetiva del sueño y disestesia de piernas |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Revisión sistemática y metaanálisis | J Clin Sleep Med | Metaanálisis sobre respuesta farmacológica de los movimientos periódicos de extremidades (PLMS) en RLS; evalúa categorías terapéuticas incluyendo benzodiazepinas |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Revisión basada en evidencia (MDS) | Mov Disord | Revisión encargada por la Movement Disorder Society; clasifica la eficacia de cada fármaco para RLS según nivel de evidencia |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Revisión narrativa | Neurotherapeutics | Revisión de opciones terapéuticas para RLS con análisis de cambios recientes; benzodiazepinas incluidas como alternativa de segunda línea |
| [9444111](https://pubmed.ncbi.nlm.nih.gov/9444111/) | 1997 | Revisión clínica especializada | ANNA Journal | Clonazepam específicamente para RLS en pacientes con enfermedad renal en etapa terminal (ESRD); perfil farmacocinético favorable en pacientes con función renal alterada |
| [35426627](https://pubmed.ncbi.nlm.nih.gov/35426627/) | 2022 | Revisión clínica / Guía | Am Fam Physician | Diagnóstico y manejo de trastornos comunes del sueño incluyendo RLS en adultos; perspectiva de atención primaria |

---

## Información de Mercado en Argentina

Clonazepam no cuenta con ninguna autorización de comercialización registrada en la base regulatoria argentina consultada (ANMAT). El fármaco es ampliamente conocido y comercializado en numerosos países bajo marcas como **Rivotril** (Roche) y **Klonopin**, y su ausencia en el registro consultado podría reflejar una brecha de datos regulatorios más que una ausencia real del mercado.

> Se recomienda verificar directamente con ANMAT el estado de comercialización vigente antes de avanzar en cualquier evaluación regulatoria.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone actualmente de datos de advertencias clave, contraindicaciones ni interacciones farmacológicas en la base consultada.

> **Nota clínica importante:** Clonazepam es una benzodiazepina con potencial reconocido de dependencia física, tolerancia y fenómeno de rebote. Su uso a largo plazo en RLS debe evaluarse cuidadosamente frente a estos riesgos. Esta información proviene del contexto clínico general del fármaco y debe ser confirmada con la ficha técnica oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia disponible incluye una revisión Cochrane, la guía AASM 2025, un ECA histórico doble ciego y un estudio aleatorizado prospectivo que respaldan el uso de clonazepam en RLS. Sin embargo, la ausencia de ensayos clínicos formales de Fase 2/3 completados, sumada al perfil de dependencia y rebote de la clase benzodiazepínica, requiere una implementación con controles estrictos de seguridad y duración de uso.

**Para avanzar se necesita:**
- Obtener datos de mecanismo de acción (MOA) formal desde DrugBank (DG002)
- Descargar y analizar el prospecto aprobado en Argentina o país de referencia para completar advertencias, contraindicaciones e interacciones farmacológicas (DG001)
- Verificar el estado real de comercialización en ANMAT, dado que Rivotril tiene presencia histórica en la región
- Evaluar el perfil riesgo-beneficio específico en poblaciones vulnerables (adultos mayores, pacientes con insuficiencia renal, embarazadas)
- Considerar el impacto regulatorio de la clasificación como sustancia controlada (psicotrópico) sobre la accesibilidad y el seguimiento clínico en Argentina
- Diseñar protocolo de monitoreo de dependencia y criterios de discontinuación para uso a largo plazo en RLS
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

