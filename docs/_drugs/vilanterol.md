---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

Usando `txgnn-pipeline` para redactar el informe de evaluación de reposicionamiento.

---

# Vilanterol: De Broncodilatador LABA Sin Registro Local a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Vilanterol es un agonista β₂ adrenérgico de larga duración (LABA) desarrollado como componente de combinaciones inhaladas fijas (FF/VI, UMEC/VI, FF/UMEC/VI) aprobadas globalmente para EPOC y asma, aunque **no cuenta con registro en Argentina**.
El modelo TxGNN predice que podría ser efectivo para **Enfermedad Pulmonar Obstructiva (obstructive lung disease)**,
con **más de 10 ensayos clínicos de Fase 3/4 completados** y **20 publicaciones** que actualmente respaldan esta dirección con el mayor nivel de evidencia posible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin indicación registrada en Argentina (ANMAT) |
| Nueva Indicación Predicha | Enfermedad Pulmonar Obstructiva (obstructive lung disease) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No registrado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales del mecanismo de acción en la base de datos local. Sin embargo, la evidencia clínica consolidada permite inferir que Vilanterol (GW642444M) es un **agonista β₂ adrenérgico inhalado de acción ultralarga (LABA) con actividad intrínseca de 24 horas**. Su mecanismo central consiste en la unión selectiva a los receptores β₂ del músculo liso bronquial, induciendo relajación y broncodilatación sostenida que reduce la resistencia al flujo aéreo. A diferencia de los LABA convencionales (salmeterol, formoterol), Vilanterol fue diseñado para administración única diaria, lo que lo convierte en un componente estratégico de combinaciones de inhalación única.

Vilanterol ha sido desarrollado exclusivamente como componente de tres combinaciones fijas aprobadas: **FF/VI** (fluticasona furoato/vilanterol, Relvar®/Breo® Ellipta®) para asma y EPOC; **UMEC/VI** (umeclidinium/vilanterol, Anoro® Ellipta®) para EPOC; y **FF/UMEC/VI** (Trelegy® Ellipta®) para asma y EPOC. Estas tres combinaciones han completado múltiples ensayos de Fase 3 con decenas de miles de pacientes y obtuvieron aprobación de la FDA, EMA y otras agencias regulatorias, constituyendo una base mecanística y clínica directamente aplicable a la enfermedad pulmonar obstructiva.

La predicción TxGNN de 99.97% es altamente coherente con la realidad científica: la enfermedad pulmonar obstructiva (EPOC y asma) es precisamente el dominio terapéutico para el cual Vilanterol fue diseñado y validado. La brecha detectada es **regulatoria-local** (ausencia de registro ANMAT en Argentina), no científica. Estudios pivotales como IMPACT (*N Engl J Med*, 2018), FULFIL (*Am J Respir Crit Care Med*, 2017) y SUMMIT (*N=16.568*) aportan un respaldo de nivel L1 que ubica a este candidato entre los más sólidos identificados en el pipeline.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Fase 3 | Completado | 16,568 | Estudio SUMMIT: FF/VI 100/25 mcg vs placebo en EPOC moderada con antecedentes/riesgo cardiovascular; evaluación de supervivencia a largo plazo |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Fase 3 | Completado | 1,621 | FF/VI 100/25 mcg vs VI 25 mcg (12 semanas): evaluación de la contribución de la fracción ICS sobre FEV1 trough en EPOC; estudio multicéntrico doble ciego |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Fase 3 | Completado | 1,538 | UMEC/VI vs UMEC vs VI vs placebo en EPOC (24 semanas): demostración de superioridad de la doble broncodilatación sobre cada componente por separado |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Fase 3 | Completado | 905 | UMEC/VI 62.5/25 mcg vs Tiotropium 18 mcg en EPOC (24 semanas): superioridad estadística en FEV1 trough con perfil de seguridad comparable |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Fase 3 | Completado | 717 | UMEC/VI vs fluticasona propionato/salmeterol en EPOC (12 semanas): diseño multicéntrico doble ciego, doble dummy, paralelo |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Fase 4 | Completado | 800 | Triple terapia FF/UMEC/VI en un solo inhalador vs Tiotropium en monoterapia en EPOC: función pulmonar y síntomas a 12 semanas |
| [NCT01181895](https://clinicaltrials.gov/study/NCT01181895) | Fase 3 | Completado | 348 | Vilanterol vs salmeterol vs placebo en asma persistente no controlada con ICS de fondo (12 semanas); primer ECA controlado con vilanterol en asma |
| [NCT05535972](https://clinicaltrials.gov/study/NCT05535972) | Fase 4 | Completado | 463 | Efectividad en mundo real de Trelegy® Ellipta (FF/UMEC/VI) en EPOC sintomática: estado de salud (SGRQ), disnea y función pulmonar |
| [NCT02799784](https://clinicaltrials.gov/study/NCT02799784) | Fase 4 | Completado | 236 | UMEC/VI vs Tiotropium/Olodaterol en EPOC moderada: estudio cruzado, open-label, comparación directa head-to-head en 2 períodos |
| [NCT06474039](https://clinicaltrials.gov/study/NCT06474039) | Fase 3 | Reclutando | 50 | Triple terapia ICS/LABA/LAMA (FF/VI/UMEC) vs doble broncodilatación (VI/UMEC): efectos sobre atrapamiento aéreo y mediadores inflamatorios en EPOC |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | ECA Fase 3 (Estudio IMPACT) | N Engl J Med | FF/UMEC/VI reduce significativamente exacerbaciones de EPOC vs ICS/LABA y vs LAMA/LABA; primer ECA pivotal de triple terapia en un solo inhalador |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | ECA Fase 3 (Estudio FULFIL) | Am J Respir Crit Care Med | FF/UMEC/VI superior a budesonida/formoterol BD en FEV1 trough y calidad de vida (SGRQ) en EPOC a 24 semanas |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | Análisis post-hoc de ECA | Am J Respir Crit Care Med | FF/UMEC/VI reduce significativamente la mortalidad por todas las causas vs UMEC/VI en pacientes con EPOC y riesgo de exacerbaciones (post-hoc IMPACT) |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Revisión Sistemática / NMA | Adv Ther | FF/UMEC/VI es superior a terapias duales y comparable o superior a otras triples terapias en EPOC en metaanálisis en red (network meta-analysis) |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Metaanálisis de ECAs | BMC Pulm Med | UMEC/VI asociado a mejora clínicamente significativa en función pulmonar y calidad de vida vs broncodilatadores en monoterapia o doble terapia en EPOC leve-moderada |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Revisión Sistemática / NMA | BMJ | Comparación de efectividad y seguridad de triples terapias en inhalador único (FF/UMEC/VI vs BUD/GLY/FORM) en EPOC en práctica clínica habitual |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | Estudio de Efectividad Comparativa | Adv Ther | FF/UMEC/VI vs BUD/GLY/FORM en pacientes con EPOC en EE.UU.: impacto diferencial en exacerbaciones y hospitalización en cohorte de mundo real |
| [37213116](https://pubmed.ncbi.nlm.nih.gov/37213116/) | 2023 | Estudio de Cohorte | JAMA Intern Med | Comparación de LAMA/LABA vs ICS/LABA en nuevos usuarios de inhaladores combinados para EPOC: exacerbaciones, neumonía y generalizabilidad vs ECAs |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | Análisis de Subgrupo de ECA | Eur Respir J | Estudio IMPACT: eficacia de FF/UMEC/VI estratificada por historia previa de exacerbaciones y conteo de eosinófilos en sangre |
| [40619503](https://pubmed.ncbi.nlm.nih.gov/40619503/) | 2025 | Efectividad Comparativa en Mundo Real | Adv Ther | FF/UMEC/VI vs BUD/GLY/FORM en pacientes con EPOC que escalaron desde terapia dual: análisis específico de resultados en población step-up |

---

## Información de Mercado en Argentina

Vilanterol **no cuenta con ninguna autorización de comercialización vigente en Argentina (ANMAT)**. No existen productos registrados que contengan vilanterol como principio activo, ya sea en monoterapia o en combinación fija. Esta ausencia no refleja una señal de seguridad negativa, sino una brecha regulatoria respecto a los mercados donde las combinaciones que contienen vilanterol (Trelegy®, Anoro®, Relvar®) sí han sido aprobadas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La enfermedad pulmonar obstructiva es la indicación para la cual Vilanterol fue diseñado y validado mediante ECAs de Fase 3 y 4 con más de 25,000 pacientes acumulados, incluyendo estudios pivotales publicados en *NEJM* y *AJRCCM*. El nivel de evidencia L1 es el máximo del pipeline. La barrera para el uso en Argentina no es científica sino **regulatoria**: ninguna combinación que contenga vilanterol está registrada ante ANMAT.

**Para avanzar se necesita:**
- Iniciar el trámite de registro ante ANMAT para alguna de las combinaciones fijas disponibles (FF/UMEC/VI / UMEC/VI / FF/VI), priorizando la formulación con mayor demanda local para EPOC
- Obtener el prospecto aprobado por FDA/EMA para extracción formal de advertencias, contraindicaciones y precauciones de seguridad (actualmente en Data Gap)
- Confirmar la disponibilidad del dispositivo inhalador ELLIPTA® y la cadena de frío/distribución en el mercado argentino
- Evaluar la elegibilidad de los datos del estudio SUMMIT y del análisis de mortalidad del IMPACT para inclusión en el dossier regulatorio local
- Revisar interacciones medicamentosas (DDI) mediante bases especializadas dado que la consulta actual no arrojó resultados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

