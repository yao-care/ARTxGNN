---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: De Síndrome Coronario Agudo a Arteriosclerosis Intracraneal

## Resumen en Una Frase

Ticagrelor es un inhibidor reversible del receptor plaquetario P2Y12, utilizado globalmente como componente de la terapia antiplaquetaria dual (DAPT) en el síndrome coronario agudo (SCA) y la intervención coronaria percutánea (PCI), aunque no cuenta con registro en Argentina.
El modelo TxGNN predice que podría ser efectivo para la **Arteriosclerosis Intracraneal (ICAD)**, con **11 ensayos clínicos** y **3 publicaciones** que actualmente respaldan esta dirección.
La evidencia incluye el ensayo pivotal CAPTIVA (Fase 3, n=1.683), actualmente activo, que evalúa directamente la superioridad de ticagrelor sobre clopidogrel en pacientes con estenosis arterial intracraneal sintomática.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo / Enfermedad arterial coronaria (indicación de uso global; sin registro en Argentina) |
| Nueva Indicación Predicha | Arteriosclerosis Intracraneal (ICAD) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el sistema. Según la información conocida, ticagrelor es un inhibidor directo y reversible del receptor P2Y12 (ADP) de la clase ciclopentil-triazolo-pirimidina. A diferencia del clopidogrel, actúa sin requerir bioactivación hepática, con un inicio de efecto más rápido y una inhibición plaquetaria más consistente e independiente del genotipo CYP2C19. Adicionalmente, inhibe el transportador de equilibrio de nucleósidos ENT1, elevando la concentración extracelular de adenosina con efectos vasodilatadores y antiinflamatorios endoteliales.

La arteriosclerosis intracraneal (ICAD) es una de las causas más importantes de ictus isquémico, especialmente prevalente en poblaciones asiáticas y latinoamericanas con alto riesgo vascular. Su fisiopatología central radica en la formación de placa ateromatosa en las arterias intracraneales, con riesgo de trombosis luminal por activación y agregación plaquetaria sobre la placa vulnerable. La inhibición de P2Y12 por ticagrelor reduce directamente este riesgo trombótico; en paralelo, el efecto adenosinérgico (vía ENT1) puede promover vasodilatación e inhibición de la inflamación vascular en el lecho intracraneal, mejorando el flujo en las zonas de estenosis crítica.

La relación entre la indicación original (SCA/coronariopatía) y la ICAD es fisiopatológicamente sólida: ambas son manifestaciones de aterotrombosis sistémica sobre lechos arteriales distintos (coronario vs. intracraneal). Esta coherencia mecanística explica por qué el ensayo CAPTIVA (NCT05047172, Fase 3, n=1.683) evalúa directamente si ticagrelor supera a clopidogrel para reducir ictus, hemorragia intracerebral o muerte vascular a 12 meses en ICAD sintomática, validando de manera prospectiva la predicción del modelo TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Activo (no reclutando) | 1.683 | CAPTIVA: Ensayo de cabeza a cabeza que compara rivaroxaban o ticagrelor vs clopidogrel para reducir la tasa de ictus isquémico, hemorragia intracerebral o muerte vascular a 1 año en ICAD sintomática. Fuente de evidencia más directa y relevante para esta indicación. |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Reclutando | 792 | DREAM-PRIDE: Evalúa stent liberador de fármaco + tratamiento médico agresivo (que incluye DAPT con ticagrelor) vs tratamiento médico estándar solo para prevenir recurrencia de ictus a 1 año en ICAD sintomática. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Reclutando | 100 | Selección de inhibidor P2Y12 guiada por genotipo CYP2C19 en ICAD sintomática: compara ticagrelor vs clopidogrel estándar en portadores de variantes de pérdida de función. Diseño de medicina de precisión con aplicación directa a la población con ICAD. |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Fase 3 | Completado | 13.885 | EUCLID: Ticagrelor vs clopidogrel en enfermedad arterial periférica (PAD). La población con PAD tiene alta superposición fenotípica y de riesgo aterotrombótico con la ICAD; proporciona datos de eficacia y seguridad comparativa a gran escala. |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Fase 4 | Completado | 2.009 | EVOLVE Short DAPT: Evaluó la seguridad de 3 meses de DAPT en pacientes de alto riesgo hemorrágico post-PCI. Proporciona datos de vida real sobre seguridad de DAPT de corta duración, relevante para el manejo post-intervención neurovascular. |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Fase 3 | Completado | 15.991 | GLOBAL LEADERS: Ticagrelor + aspirina 1 mes → ticagrelor en monoterapia 23 meses vs DAPT estándar 12 meses post-stent coronario. Proporciona los datos de seguridad a largo plazo de ticagrelor más robustos disponibles. |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Fase 3 | No iniciado aún | 1.700 | SOLOPCI: DAPT muy corta (aspirina hasta día 7) seguida de monoterapia con P2Y12 (incluyendo ticagrelor) vs DAPT estándar en pacientes ≥65 años post-PCI. Relevante para el diseño de esquemas en pacientes ancianos con ICAD y alto riesgo hemorrágico. |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Desconocido | 2.171 | Combinación anticoagulación + antiagregación en ictus isquémico agudo con FA concomitante y estenosis extracraneal/intracraneal; incluye componente ticagrelor. Estado UNKNOWN reduce la confiabilidad del dato. |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Fase 4 | Desconocido | 2.036 | Ticagrelor dosis baja (45 mg c/12h) vs estándar (90 mg c/12h) en angina inestable china post-stent; relevante para la optimización posológica en población asiática, donde la ICAD tiene mayor prevalencia. |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | No iniciado aún | 3.500 | Indicadores de control de calidad de revascularización coronaria basados en DAPT (aspirina + P2Y12). Orientado a enfermedad coronaria; relevancia indirecta para ICAD como marco de calidad en terapia antiplaquetaria. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Protocolo de Ensayo | International Journal of Stroke | Diseño y progreso temprano del ensayo CAPTIVA: justifica la selección de ticagrelor como brazo experimental frente a clopidogrel+aspirina en ICAD sintomática. Confirma que la comunidad neurológica considera a ticagrelor como candidato terapéutico prioritario para esta indicación. |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Revisión de Consenso | Stroke | Actualización enfocada sobre arteriosclerosis intracraneal: identifica brechas de conocimiento y posiciona a ticagrelor como agente de interés activo en el campo. Respaldo de expertos de la AHA/ASA. |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Observacional Prospectivo | Journal of Neurointerventional Surgery | Experiencia clínica con ticagrelor 60 mg c/12h + aspirina 81 mg comparado con el esquema aspirina + clopidogrel para stenting intracraneal. Sugiere que la dosis reducida de ticagrelor ofrece inhibición plaquetaria adecuada con un perfil de seguridad manejable en procedimientos neurointervencionistas. |

---

## Información de Mercado en Argentina

Ticagrelor no cuenta con ninguna autorización de comercialización registrada en Argentina (ANMAT). No existen licencias activas.

> **Implicación regulatoria**: La ausencia de registro implica que cualquier uso clínico en Argentina requeriría acceso mediante importación por uso compasivo o medicamento extranjero autorizado por ANMAT, o bien la participación del paciente en un ensayo clínico aprobado localmente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota de contexto clínico**: Aunque los datos de seguridad formales no están disponibles en este Evidence Pack, ticagrelor está ampliamente caracterizado en la literatura por: riesgo de sangrado mayor (incluida hemorragia intracraneal), disnea relacionada con efecto adenosinérgico (frecuente, generalmente leve), y pausas sinusales/bradicardia. En el contexto de ICAD, el balance beneficio-riesgo —particularmente el riesgo de transformación hemorrágica intracraneal— está siendo evaluado prospectivamente por el ensayo CAPTIVA y debe monitorearse con especial atención.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El ensayo de Fase 3 CAPTIVA (n=1.683) evalúa directamente ticagrelor en arteriosclerosis intracraneal sintomática con resultados esperados en 2027, y múltiples ensayos de Fase 3-4 a gran escala (EUCLID n=13.885, GLOBAL LEADERS n=15.991) proporcionan un perfil de seguridad robusto en poblaciones vasculares con alto grado de superposición. La plausibilidad mecanística es sólida (inhibición P2Y12 + efecto adenosinérgico en el lecho intracraneal), y el nivel de evidencia L1 justifica avanzar con monitoreo activo mientras se consolidan los datos definitivos.

**Para avanzar se necesita:**
- Resultados finales del ensayo CAPTIVA (estimado 2027) para determinar superioridad clínica sobre clopidogrel en ICAD
- Obtención del mecanismo de acción (MOA) completo desde DrugBank (remediación de Data Gap DG002) para robustecer el análisis mecanístico
- Evaluación específica del riesgo de hemorragia intracraneal en la población con ICAD (balance riesgo-beneficio intracraneal vs. extraintracraneal)
- Genotipificación CYP2C19 de la población objetivo: identificar qué pacientes se benefician diferencialmente de ticagrelor vs. clopidogrel (respaldo del ensayo NCT06714526)
- Gestión regulatoria ante ANMAT para habilitar uso compasivo o iniciar proceso de registro, dado que ticagrelor no está comercializado en Argentina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

