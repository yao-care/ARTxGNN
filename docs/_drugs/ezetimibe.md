---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Procediendo directamente con la generación del informe según las instrucciones del sistema y el Evidence Pack proporcionado.

---

# Ezetimibe: De Hipercolesterolemia a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimibe es un inhibidor selectivo de la absorción intestinal de colesterol, reconocido internacionalmente como tratamiento de primera línea para la hipercolesterolemia primaria y mixta, aunque actualmente no cuenta con aprobación de ANMAT en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Hiperlipoproteinemia**, con **50 ensayos clínicos** y **19 publicaciones** que actualmente respaldan esta dirección.
Esta predicción constituye esencialmente una validación del uso ya establecido globalmente del fármaco, cuya ausencia en el mercado argentino representa la principal brecha a resolver.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro ANMAT (fármaco no comercializado en Argentina; indicación internacional establecida: hipercolesterolemia) |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones ANMAT | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Ezetimibe actúa inhibiendo selectivamente la proteína NPC1L1 (Niemann-Pick C1-Like 1) ubicada en el borde en cepillo del epitelio intestinal, bloqueando la absorción de colesterol dietario, biliar y de esteroles vegetales. Al reducir el aporte de colesterol vía quilomicrones al hígado, se desencadena una regulación al alza compensatoria de los receptores de LDL hepáticos, lo que resulta en una reducción neta del colesterol LDL plasmático de aproximadamente 15-20% como monoterapia y de hasta 25% adicional cuando se combina con estatinas. Este mecanismo complementa directamente al de las estatinas, que actúan en la vía de síntesis endógena de colesterol.

La hiperlipoproteinemia abarca un espectro amplio de alteraciones del metabolismo lipoproteico —incluyendo elevación de LDL-C, hiperlipidemia mixta (tipo IIb) y formas genéticas como la hipercolesterolemia familiar— todas ellas con desequilibrio en el metabolismo del colesterol como denominador común. El mecanismo de ezetimibe, al actuar sobre la entrada intestinal de colesterol, interviene en un nodo clave de la homeostasis lipoproteica, haciendo del fármaco una intervención racional para distintos subtipos de hiperlipoproteinemia. Los estudios con ultrasonido intravascular (IVUS) han confirmado además que la inhibición de la absorción de colesterol, en combinación con estatinas, produce regresión de placa coronaria comparable a la inhibición de síntesis.

La solidez de la predicción del modelo TxGNN (99.63%) refleja una base de evidencia clínica excepcionalmente sólida: múltiples ensayos Fase 3 completados, guías internacionales (EAS, ACC/AHA) que recomiendan explícitamente ezetimibe como terapia de segunda línea, y aprobaciones regulatorias vigentes en FDA y EMA. En este contexto, la predicción del modelo puede interpretarse como una validación del uso establecido, señalando una oportunidad de registro local en Argentina con respaldo de evidencia de máxima calidad.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Completado | 611 | Evaluación de eficacia y seguridad de ezetimibe/simvastatina vs. fenofibrato en pacientes con hiperlipidemia mixta (colesterol elevado + triglicéridos elevados); ensayo pivotal de la combinación |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Fase 3 | Completado | 615 | Estudio doble ciego que utiliza ezetimibe como comparador activo frente a evolocumab (subcutáneo) en adultos con puntaje de riesgo de Framingham ≤10%; confirma el estatus de referencia de ezetimibe como tratamiento |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Fase 4 | Completado | 245 | PRECISE-IVUS: comparación de regresión de placa coronaria entre inhibidor de absorción de colesterol (ezetimibe + estatina) vs. inhibidor de síntesis solo; evaluado por ultrasonido intravascular |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Evaluación de eficacia y seguridad de la coadministración de fenofibrato y ezetimibe en hiperlipidemia mixta; evalúa el perfil lipídico completo incluyendo triglicéridos |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Estudio de seguridad y eficacia de coadministración fenofibrato + ezetimibe en hiperlipidemia mixta; estudio complementario al NCT00092560 con mayor tamaño muestral y diferente ventana temporal |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Fase 3 | Completado | 407 | Estudio doble ciego aleatorizado de combinación de dosis fija obicetrapib 10 mg + ezetimibe 10 mg en pacientes con HeFH y/o ASCVD; confirma el rol de ezetimibe como componente del estándar de tratamiento |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Fase 3 | Completado | 181 | Comparación de fenofibrato 145 mg, ezetimibe 10 mg y su combinación en dislipidemia tipo IIb con síndrome metabólico; evalúa la triada lipídica aterogénica |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimibe 10 mg en combinación con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota (HoFH); ensayo pivotal en subgrupo genético de alto riesgo |
| [NCT05611528](https://clinicaltrials.gov/study/NCT05611528) | Fase 3 | Completado | 10 | Evinacumab (anticuerpo anti-ANGPTL3) en HoFH en vida real en Canadá; ezetimibe como componente de la terapia de fondo estándar en este subgrupo |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Fase 3 | Terminado | 49 | Estudio abierto de provisión global de ezetimibe 10 mg/día en pacientes con HoFH o sitosterolemia homocigota; aporta señales de eficacia y seguridad en población de muy alto riesgo genético |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA Fase 3 | The Lancet | Ensayo TANDEM: combinación de dosis fija obicetrapib/ezetimibe redujo LDL-C significativamente vs. placebo en pacientes de alto riesgo cardiovascular con hiperlipidemia |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA Fase 3 | JAMA | Inhibidor oral de PCSK9 enlicitide en HeFH; ezetimibe utilizado como tratamiento de fondo estándar, confirmando su rol central en HeFH |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Guía/Consenso | European Heart Journal | Declaración de consenso EAS: guía de detección y tratamiento de hipercolesterolemia familiar; ezetimibe recomendado como terapia adyuvante a estatinas para alcanzar objetivos de LDL-C |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Revisión | Cardiology Clinics | Revisión comprehensiva de hipercolesterolemia familiar: estatinas y ezetimibe como pilares del tratamiento; subraya el rol de ezetimibe como segunda línea con perfil de seguridad favorable |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Revisión | Current Cardiology Reports | Revisión global sobre FH: ezetimibe como tratamiento complementario estándar a estatinas para reducción de ASCVD y mortalidad prematura |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Revisión | Nature Reviews Disease Primers | Revisión sobre hipercolesterolemia familiar: descripción del rol de ezetimibe en el manejo con mecanismo complementario (inhibición de absorción vs. inhibición de síntesis) |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Revisión | Int. Journal of Molecular Sciences | Hiperlipidemia postprandial: fisiopatología y tratamientos; ezetimibe puede reducir TG postprandiales al inhibir la absorción intestinal de lípidos en la fase prandial |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Molecular Medicine Reports | Revisión de fármacos actuales para hiperlipidemia; ezetimibe descrito como agente de segunda línea con mecanismo NPC1L1 para prevención de ASCVD |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Revisión | J. Cardiovascular Pharmacology & Therapeutics | Revisión comprehensiva de inhibidores de PCSK9; ezetimibe citado como tratamiento base al que se añaden las nuevas terapias biológicas, especialmente en pacientes intolerantes a estatinas |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Revisión | Indian Heart Journal | Revisión sobre hipercolesterolemia familiar: ezetimibe recomendado en combinación con estatinas para los subgrupos que no alcanzan metas lipídicas con monoterapia |

---

## Información de Mercado en Argentina

Ezetimibe actualmente **no cuenta con ninguna autorización de ANMAT** registrada en Argentina y el fármaco no se encuentra comercializado en el mercado local. Esto contrasta con su amplia disponibilidad en mercados regulados de referencia: está aprobado por la FDA (Zetia®, Merck/Schering-Plough, 2002), la EMA (Ezetrol®) y múltiples agencias de Asia-Pacífico.

Se recomienda consultar la base de datos de autorizaciones ANMAT (Sistema Nacional de Farmacovigilancia / VADEMECUM ANMAT) para verificar el estado regulatorio actualizado, y evaluar los requisitos para una solicitud de registro local basada en el dossier internacional ya existente (dosier FDA/EMA).

---

## Consideraciones de Seguridad

No se dispone de la ficha técnica local de ANMAT dado que el fármaco no está aprobado en Argentina. Para información de seguridad completa (advertencias, contraindicaciones, interacciones farmacológicas), consultar el prospecto internacional vigente:

- **Ficha técnica EMA:** Ezetrol® (ezetimibe 10 mg)
- **Etiquetado FDA:** Zetia® (ezetimibe 10 mg)

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Ezetimibe cuenta con múltiples ensayos clínicos Fase 3 completados, guías de práctica clínica internacionales que lo recomiendan explícitamente y aprobaciones vigentes en los mercados regulatorios de mayor exigencia (FDA, EMA). El modelo TxGNN confirma con un puntaje de 99.63% una indicación ya internacionalmente establecida. La ausencia de registro en Argentina no representa una limitación clínica ni de evidencia, sino exclusivamente una brecha regulatoria local que puede abordarse con el dossier existente.

**Para avanzar se necesita:**
- Iniciar solicitud de registro ANMAT (Categoría de Tramitación: Expediente de Medicamento con fármaco aprobado en países de referencia FDA/EMA)
- Obtener la ficha técnica completa (prospecto con advertencias, contraindicaciones, interacciones farmacológicas) para completar la evaluación de seguridad formal local
- Revisar la situación de patentes vigentes y disponibilidad de formulaciones genéricas aprobadas internacionalmente para evaluar viabilidad comercial en Argentina
- Definir población objetivo prioritaria (hipercolesterolemia primaria, hiperlipidemia mixta, hipercolesterolemia familiar heterocigota) en función del perfil epidemiológico local
- Diseñar plan de farmacovigilancia y monitoreo post-comercializaciónpost-registro si se avanza hacia aprobación local
---

