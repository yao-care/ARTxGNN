---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

El skill txgnn-pipeline confirma el contexto del proyecto. Ahora procedo a generar el informe de evaluación siguiendo el formato v5 del sistema.

---

# Vildagliptin: De Diabetes Mellitus Tipo 2 a Diabetes Mellitus Tipo 1

## Resumen en Una Frase

Vildagliptin es un inhibidor potente y selectivo de la enzima DPP-4, aprobado internacionalmente para el tratamiento de la diabetes mellitus tipo 2 (T2DM), donde mejora el control glucémico mediante la preservación de las hormonas incretinas GLP-1 y GIP.
El modelo TxGNN predice que podría ser efectivo para **Diabetes Mellitus Tipo 1 (T1DM)**, respaldado por una cadena mecanística multivía que incluye protección de células beta, inmunomodulación a través de CD26 y control del glucagón.
Esta indicación cuenta con **1 ensayo clínico de Fase 2 completado directamente en T1DM** y **múltiples publicaciones clínicas con diseño aleatorizado**, configurando un nivel de evidencia L2.

> **Nota metodológica:** La indicación con mayor puntaje TxGNN en este perfil es el *síndrome de persona rígida clásico* (*classic stiff person syndrome*, puntaje 99,88%, Rango TxGNN #922), que sin embargo carece de toda evidencia clínica o preclínica de respaldo (Nivel L5, recomendación **Hold**). Por criterio de utilidad clínica, este informe prioriza la **diabetes mellitus tipo 1** (puntaje 99,37%, Rango TxGNN #3334), que posee el mayor nivel de evidencia del perfil y la única recomendación accionable (*Proceed with Guardrails*).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes Mellitus Tipo 2 (aprobación internacional; no comercializado en Argentina) |
| Nueva Indicación Predicha | Diabetes Mellitus Tipo 1 |
| Puntaje de Predicción TxGNN | 99,37% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción desde DrugBank. Sin embargo, la evidencia clínica y los estudios mecanísticos en humanos permiten reconstruir el perfil farmacológico con precisión: vildagliptin actúa como inhibidor competitivo de la DPP-4 (dipeptidil peptidasa-4), enzima responsable de la inactivación rápida de las hormonas incretinas GLP-1 (péptido similar al glucagón tipo 1) y GIP (polipéptido insulinotrópico dependiente de glucosa) tras su liberación intestinal. Al inhibir esta enzima, vildagliptin mantiene niveles activos de ambas incretinas durante las comidas a lo largo de un ciclo de 24 horas, estimulando la secreción de insulina de manera estrictamente dependiente de glucosa y suprimiendo la secreción inapropiada de glucagón. Este mecanismo fue validado en T2DM, pero su lógica biológica no se limita a ese contexto.

La extensión a T1DM se sustenta en una cadena mecanística de cuatro vías complementarias: ① **Función beta-celular residual**: en el período de "luna de miel" de T1DM y en casos de larga evolución con función C-péptido detectable, GLP-1 elevado puede potenciar la secreción insulínica residual y retrasar la pérdida de función; ② **Protección antiapoptótica y neogénesis**: GLP-1 ejerce efectos directos de protección y proliferación sobre las células beta, con evidencia preclínica de neogénesis beta-celular bajo vildagliptin en modelos de T1DM; ③ **Inmunomodulación vía CD26**: DPP-4 es molecularmente idéntico a CD26, una proteína de superficie de linfocitos T activados; su inhibición modula la activación y el tráfico de células T, con potencial de atenuar el componente autoinmune de la destrucción beta-celular; ④ **Control de glucagón**: la supresión del glucagón posprandial reduce las excursiones hiperglucémicas en T1DM de forma independiente al incremento de insulina endógena, con el efecto adicional de preservar la contrarregulación glucagonémica durante hipoglucemia.

La transición de T2DM a T1DM representa la extensión hacia una enfermedad fisiopatológicamente distinta, pero farmacológicamente conectada a través de la biología del eje incretina-glucagón-célula beta. Los estudios clínicos publicados —incluyendo ensayos controlados aleatorizados con doble enmascaramiento en T1DM pediátrico y adulto— confirman que esta conexión ha sido explorada con rigor metodológico creciente, aunque se requieren ensayos de Fase 3 específicos en T1DM para establecer la eficacia definitiva en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02803892](https://clinicaltrials.gov/study/NCT02803892) | Fase 2 | Completado | 55 | Ensayo doble ciego, aleatorizado, 3 brazos paralelos (1:1:1) en T1DM de larga evolución: placebo vs. rapamicina (4 semanas) vs. rapamicina + vildagliptin (3 meses). Evalúa recuperación de producción endógena de insulina y corrección de labilidad glucémica. Único ensayo que evalúa vildagliptin directamente en T1DM. |
| [NCT00138606](https://clinicaltrials.gov/study/NCT00138606) | Fase 3 | Completado | 179 | Extensión de 28 semanas de vildagliptin añadido a insulina en T2DM con control glucémico insuficiente en monoterapia insulínica. Los datos de seguridad de la combinación insulina + DPP-4i son directamente extrapolables al manejo de T1DM, especialmente para evaluación de riesgo de hipoglucemia. |
| [NCT00099931](https://clinicaltrials.gov/study/NCT00099931) | Fase 3 | Completado | 254 | Estudio de eficacia y seguridad de vildagliptin en combinación con insulina en T2DM. Junto con NCT00138606, constituye la base de seguridad de la combinación insulina + vildagliptin relevante para T1DM. |
| [NCT05102149](https://clinicaltrials.gov/study/NCT05102149) | Fase 3 | Desconocido | 672 | Multicéntrico, aleatorizado, doble ciego, controlado con vildagliptin y placebo para evaluar PB-201 en T2DM naive. Ensayo de diseño riguroso con vildagliptin como brazo de referencia activo; proporciona contexto comparativo de alta calidad para el perfil de eficacia de vildagliptin. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | ECA Prospectivo | Diabetology & Metabolic Syndrome | Vildagliptin oral adyuvante en adolescentes y adultos jóvenes con T1DM en sistema de asa cerrada avanzado (MiniMed™ 780G) durante Ramadán; demuestra reducción de excursiones glucémicas posprandiales del Iftar con bajo riesgo de hipoglucemia. Evidencia clínica directa en T1DM. |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | ECA | Diabetes, Obesity & Metabolism | Vildagliptin adyuvante en adolescentes con T1DM y esteatohepatitis no alcohólica (NASH); evalúa MMP-14, rigidez hepática y aterosclerosis subclínica como endpoints cardiovasculares y hepáticos en T1DM. Amplía el perfil de beneficios más allá del control glucémico. |
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | ECA Doble Ciego | J Clin Endocrinol Metab | Publicación del ensayo NCT02803892: rapamicina + vildagliptin en T1DM de larga evolución. Evalúa si el esquema combinado restaura la producción endógena de insulina y corrige la labilidad glucémica; diseño riguroso con doble enmascaramiento y control placebo. |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | ECA Crossover | J Clin Endocrinol Metab | Vildagliptin reduce la secreción de glucagón durante hiperglucemia pero preserva la contrarregulación glucagonémica durante hipoglucemia en T1DM; efecto dual clínicamente favorable que establece el perfil de seguridad glucagonémica en T1DM. |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Estudio Mecanístico en Humanos | Frontiers in Endocrinology | Análisis detallado del mecanismo de acción de vildagliptin en humanos: mantiene GLP-1 y GIP activos durante 24h; mejora la sensibilidad de células beta a glucosa en IFG, IGT y T2DM. Proporciona el fundamento mecanístico aplicable a T1DM con función residual. |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Revisión Narrativa | Expert Opinion on Investigational Drugs | Revisión de efectos pleomórficos de inhibidores DPP-4 más allá del uso antihiperglucémico etiquetado: protección de células beta contra destrucción inmune en T1DM, efectos nefroprotectores en T1DM y T2DM, y potencial como terapia adyuvante en T1DM. |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Estudio Animal (Rata) | Current Pharmaceutical Biotechnology | Primera evidencia publicada de neogénesis de células beta inducida por vildagliptin y mejora del perfil lipídico en fase tardía de T1DM en modelo de rata Fischer con diabetes inducida por aloxano; respalda la hipótesis de eficacia a largo plazo. |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Estudio Clínico | Hormone and Metabolic Research | Efecto de vildagliptin sobre la concentración de glucagón durante las comidas en pacientes con T1DM; establece el primer fundamento clínico directo para su aplicación en T1DM mediante modulación del eje glucagón posprandial. |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Estudio Animal (Rata) | Archives of Medical Research | Vildagliptin ameliora el estrés oxidativo y la destrucción de células beta pancreáticas en ratas con T1DM; evidencia de protección pancreática complementaria al mecanismo incretínico. |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Estudio Animal (Rata) | Canadian J Physiology and Pharmacology | Combinación vildagliptin/pioglitazona mejoró el control glucémico global en ratas con T1DM; explora sinergias terapéuticas en este contexto y amplía el perfil de combinaciones potenciales. |

---

## Información de Mercado en Argentina

Vildagliptin no cuenta con ninguna autorización de comercialización registrada ante ANMAT en Argentina. La base de datos regulatoria consultada no contiene licencias activas para este principio activo. Cabe señalar que vildagliptin sí posee aprobación internacional (EMA, entre otras) para T2DM, con amplia experiencia clínica global, lo que facilita el acceso a datos de seguridad poblacional para su evaluación regulatoria futura en Argentina.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (datos de advertencias y contraindicaciones no disponibles en la fuente consultada para este análisis).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo clínico de Fase 2 completado con diseño aleatorizado doble ciego que evalúa vildagliptin directamente en T1DM (NCT02803892, n=55), respaldado por múltiples ECA publicados en poblaciones T1DM pediátricas y adultas (2008–2024), y una base mecanística sólida de cuatro vías complementarias con evidencia en humanos. La solidez conjunta de la evidencia clínica directa justifica avanzar hacia estudios de mayor escala, con las salvaguardas apropiadas para una indicación fuera de etiqueta.

**Para avanzar se necesita:**
- Datos completos de mecanismo de acción (MOA) desde DrugBank (actualmente no disponibles)
- Información de advertencias, contraindicaciones e interacciones desde el prospecto oficial (EMA/ANMAT)
- Evaluación de viabilidad regulatoria para registro en Argentina ante ANMAT (0 autorizaciones activas)
- Diseño de ensayo clínico Fase 2/3 específico para T1DM en Argentina, priorizando pacientes con función C-péptido residual detectable como criterio de selección y predictor de respuesta
- Plan de monitoreo de hipoglucemia estructurado para el contexto de terapia combinada con insulina
- Definición de ventana terapéutica óptima: período de "luna de miel" de T1DM como población de intervención prioritaria
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

