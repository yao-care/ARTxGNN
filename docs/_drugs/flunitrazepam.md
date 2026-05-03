---
layout: default
title: Flunitrazepam
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Flunitrazepam
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

---

# Flunitrazepam: De Sedante-Hipnótico a Insomnio

## Resumen en Una Frase

Flunitrazepam (Rohypnol) es una benzodiacepina de alta potencia históricamente utilizada como hipnótico nocturno y agente preanestésico en múltiples países, aunque actualmente no comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**,
con **1 ensayo clínico** y **11 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro en Argentina (uso histórico documentado: hipnótico/anestésico) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en la base de datos consultada. Sin embargo, la literatura farmacológica revisada describe con claridad que flunitrazepam actúa como modulador positivo del receptor GABA-A, potenciando la inhibición GABAérgica en el sistema nervioso central. Este mecanismo produce efectos hipnóticos pronunciados: acorta la latencia de inicio del sueño, prolonga el sueño NREM y reduce los despertares nocturnos. Es, en esencia, el mecanismo central de los hipnóticos benzodiacepínicos clásicos, y flunitrazepam es uno de los representantes más potentes de esta clase (PMID 6108205).

El vínculo entre flunitrazepam e insomnio no es especulativo: el fármaco fue históricamente aprobado en Japón y múltiples países europeos específicamente para el tratamiento del insomnio a corto plazo. Esta predicción de TxGNN con puntuación del 99.89% refleja la solidez del nexo mecanístico más que una indicación genuinamente nueva. Existen estudios clínicos directos que confirman su eficacia hipnótica en pacientes insomnes (PMID 40195, PMID 8519370) y una auditoría clínica multicéntrica japonesa que compara flunitrazepam IV con midazolam IV específicamente para insomnio primario en pacientes con cáncer terminal (PMID 17985961).

La principal limitación para el avance clínico no es la falta de eficacia, sino el perfil de seguridad y el contexto regulatorio global: el fármaco ha sido retirado del mercado o severamente restringido en la mayoría de los países por su altísimo potencial de abuso, sus propiedades amnésicas y su asociación con delitos facilitados por drogas. En Argentina, actualmente no existe ningún registro activo de comercialización del principio activo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1.400 | Estudio de cohorte prospectivo en Taiwan que evalúa el riesgo y beneficio de hipnóticos —incluyendo benzodiacepinas como flunitrazepam— en ancianos con trastornos del sueño. Examina patrones de uso a corto y largo plazo, características farmacocinéticas y farmacogenéticas, y resultados clínicos, económicos y humanísticos. Diseño observacional; no proporciona evidencia interventiva directa de eficacia, pero aporta datos de seguridad en contexto de uso real (caídas, deterioro cognitivo, dependencia). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17985961](https://pubmed.ncbi.nlm.nih.gov/17985961/) | 2007 | Auditoría clínica multicéntrica | J Palliat Med | Comparación retrospectiva de midazolam IV y flunitrazepam IV para insomnio primario en pacientes con cáncer terminal en Japón. Primera evidencia empírica directa sobre eficacia y seguridad de flunitrazepam IV en esta indicación específica. |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | Estudio comparativo clínico | Eur Respir J | Comparación de dosis única de zolpidem 10 mg, triazolam 0,25 mg y flunitrazepam 1 mg en 12 pacientes con EPOC grave e insomnio. Evalúa efectos sobre gases arteriales y control respiratorio; datos directos de flunitrazepam en pacientes insomnes de alto riesgo. |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | Observación clínica | JAMA | Evaluación de 5 benzodiacepinas —incluyendo flunitrazepam— en 15 estudios de laboratorio del sueño. Documenta insomnio de rebote tras retirada de flunitrazepam administrado en dosis nocturna única durante períodos cortos; advertencia de seguridad clave. |
| [684426](https://pubmed.ncbi.nlm.nih.gov/684426/) | 1978 | Observación clínica | Science | Primer informe del síndrome de insomnio de rebote tras retirada de benzodiacepinas de acción corta/intermedia incluyendo flunitrazepam. Propone hipótesis de receptores benzodiacepínicos cerebrales para explicar el efecto. |
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | Estudio clínico | Nouv Presse Med | Estudio directo sobre la acción de flunitrazepam en trastornos del sueño orgánicos y funcionales. Datos originales de eficacia del fármaco en la indicación de insomnio. |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Revisión clínica | Acta Psychiatr Scand Suppl | Revisión de cambios farmacodinámicos de benzodiacepinas —incluyendo flunitrazepam— en el envejecimiento normal y en enfermedades. Estudios controlados demuestran respuesta aumentada 2-3 veces en ancianos sanos, independiente de enfermedad o concentraciones plasmáticas. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión clínica | Acta Psychiatr Scand Suppl | Discute la necesidad de distintos hipnóticos benzodiacepínicos según el tipo de insomnio (dificultad para conciliar el sueño, despertares frecuentes o despertar precoz). Evalúa perfiles farmacocinéticos y farmacodinámicos relevantes para la selección del hipnótico adecuado. |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Revisión de seguridad | Sleep Med Rev | Revisión del impacto de hipnóticos —incluyendo benzodiacepinas— sobre el equilibrio corporal y la estabilidad postural. Caídas y fracturas de cadera son eventos frecuentes en pacientes que se despiertan por la noche o en la mañana tras usar medicación para el sueño. |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Revisión farmacológica | Drugs | Revisión de triazolam con comparativa frente a flunitrazepam, nitrazepam y flurazepam. Posiciona a flunitrazepam como hipnótico de vida media más prolongada, potencialmente menos adecuado que fármacos de acción corta para el insomnio por mayor acumulación. |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | Estudio animal | Psychopharmacology | Modelo de rata con perturbación del sueño para evaluar características de hipnóticos. Valida la utilidad del modelo para estimar efectos de benzodiacepinas sobre el ciclo sueño-vigilia; soporte preclínico de la clase farmacológica. |

---

## Información de Mercado en Argentina

Flunitrazepam no posee ninguna autorización de comercialización vigente registrada ante la ANMAT. No se registran licencias activas para este principio activo en Argentina.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota clínica:** Aunque los datos estructurados de advertencias no están disponibles en las fuentes consultadas, la literatura revisada documenta las siguientes preocupaciones de seguridad directamente relevantes para la indicación de insomnio:
>
> - **Insomnio de rebote:** documentado tras retirada incluso con uso breve de dosis nocturna única (PMID 430730, PMID 684426); obliga a reducción gradual de dosis
> - **Deterioro postural y riesgo de caídas:** especialmente crítico en pacientes ancianos; asociado con fracturas de cadera (PMID 20171127)
> - **Depresión respiratoria:** precaución en pacientes con EPOC grave; datos de seguridad disponibles (PMID 8519370)
> - **Amnesia anterógrada:** efecto documentado a dosis terapéuticas; contribuye al perfil de abuso como droga facilitadora de agresión sexual
> - **Alto potencial de abuso y dependencia:** retirado del mercado o severamente restringido en la mayoría de países; actualmente ilegal importarlo a EE.UU. y otros países (PMID 9475831)

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El vínculo mecanístico de flunitrazepam con el insomnio es robusto y está respaldado por uso clínico histórico documentado en múltiples países, publicaciones clínicas directas (incluyendo una auditoría multicéntrica japonesa) y una base farmacológica sólida en el receptor GABA-A. No obstante, el altísimo potencial de abuso, la ausencia total de registro en Argentina y la disponibilidad de alternativas hipnóticas más seguras imponen guardarraíles estrictos que deben ser evaluados formalmente antes de cualquier avance clínico o regulatorio.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (EMA/Rote Liste/prospecto japonés) para completar los datos de advertencias, contraindicaciones e interacciones — **Data Gap DG001 (nivel Blocking)**
- Confirmar el mecanismo de acción formal mediante consulta a DrugBank API — **Data Gap DG002 (nivel High)**
- Evaluar el marco regulatorio vigente en Argentina para benzodiacepinas de alta potencia (Ley 17.818 de psicotrópicos) y determinar si existe vía legal para un eventual uso hospitalario restringido
- Realizar análisis de beneficio-riesgo comparativo frente a hipnóticos actualmente disponibles en Argentina con perfil de seguridad superior (zolpidem, lormetazepam, melatonina)
- Definir una estrategia formal de mitigación del riesgo de abuso (programa de acceso restringido, uso exclusivo hospitalario) antes de considerar cualquier solicitud de registro o protocolo de investigación clínica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

