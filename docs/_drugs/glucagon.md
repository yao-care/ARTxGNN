---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

El skill `txgnn-pipeline` no contiene instrucciones específicas sobre el formato de reporte; la plantilla ya está definida en el sistema. Procedo a generar el informe completo.

---

# Glucagon: De Antiespasmódico Gastrointestinal a Síndrome de Intestino Irritable

## Resumen en Una Frase

Glucagon es una hormona peptídica endógena utilizada clínicamente como antídoto de emergencia en hipoglucemia grave y como agente antiespasmódico en procedimientos de endoscopía gastrointestinal.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Intestino Irritable (SII)**,
con **11 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia es predominantemente indirecta, proveniente del eje GLP-1/Glucagon.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Antiespasmódico gastrointestinal / Hipoglucemia grave |
| Nueva Indicación Predicha | Síndrome de Intestino Irritable |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Glucagon es una hormona peptídica que actúa sobre el músculo liso gastrointestinal inhibiendo la contractilidad y la motilidad. Esta propiedad antiespasmódica tiene aplicación clínica establecida: se usa rutinariamente como relajante durante endoscopías para mejorar la visualización del tracto digestivo. Esta capacidad de modular la motilidad intestinal es el punto de partida para explorar su aplicabilidad al SII, un trastorno funcional caracterizado precisamente por alteraciones en la motilidad y la hipersensibilidad visceral.

El vínculo mecanístico más sólido proviene del eje GLP-1/Glucagon: ambos péptidos se derivan del proglucagón y sus receptores comparten distribución parcialmente solapada en el tracto gastrointestinal. El GLP-1, secretado por las células L intestinales en respuesta a nutrientes, reduce la hipersensibilidad visceral, modula la motilidad y participa en la señalización neuroendocrina del eje intestino-cerebro, tres mecanismos centrales en la fisiopatología del SII. El análogo de GLP-1 ROSE-010 ha demostrado en ensayos Fase 1/2 completados que reduce el dolor abdominal durante exacerbaciones agudas del SII-C, mientras que revisiones sistemáticas recientes (2025) confirman el beneficio general de los agonistas del receptor GLP-1 (GLP-1 RAs) en esta condición.

No obstante, es fundamental distinguir que toda la evidencia clínica disponible corresponde a GLP-1 RAs (ROSE-010, liraglutide, exenatida), que actúan principalmente a través del receptor GLP-1 (GLP-1R), no del receptor de glucagón (GCGR). Glucagon per se no cuenta con ningún ensayo clínico directo en SII. Si bien la predicción del modelo TxGNN es biológicamente plausible y el mecanismo antiespasmódico ofrece una base conceptual, la brecha entre la evidencia indirecta y el uso directo de Glucagon en SII es sustancial y requiere investigación específica antes de avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Completado | 52 | ROSE-010 (análogo GLP-1) demora el vaciamiento gástrico y mejora la acomodación gástrica sin retardar el tránsito colónico en mujeres con IBS-C; estudio randomizado doble ciego controlado con placebo |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Completado | 12 | GLP-1 nativo inhibe la motilidad antro-duodeno-yeyunal prandial in vivo; estudios in vitro sobre mecanismo de acción en tiras musculares del tracto GI humano |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Fase 2 | Terminado prematuramente | 8 | Liraglutida vs. placebo en pacientes con anastomosis ileoanal (IPAA) y alta frecuencia evacuatoria; terminado por baja inscripción, resultados limitados |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completado | 66 | Comparación de ejercicio moderado continuo vs. intervalos de alta intensidad sobre GLP-1 y disbiosis intestinal en pacientes obesos pre-diabéticos con SII |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completado | 37 | Mecanismo de acción del butirato en el colon humano; vinculación indirecta con SII a través de la hipótesis de deficiencia de butirato y posible implicación de células L secretoras de GLP-1 |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Activo sin reclutamiento | 375 | Evaluación del efecto de antígenos nutricionales y agentes terapéuticos sobre organoides intestinales humanos; investigación básica de mecanismos intestinales |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completado | 12 | Prevalencia de hipoglucemia reactiva idiopática y efecto de suplementación con FOS sobre variabilidad glucémica; involucra mecanismo regulador de glucagón |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Desconocido | 110 | Dieta baja en energía vs. balón intragástrico en adultos con obesidad; contexto metabólico con posible implicación de secreción GLP-1 |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completado | 41 | Efecto de la velocidad de ingesta de alimentos ultraprocesados sobre el comportamiento alimentario y respuestas metabólicas; sin relación directa con Glucagon en SII |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completado | 33 | Intervención nutricional dirigida a la microbiota intestinal para preservar la permeabilidad GI durante hipoxia hipobárica; evidencia de contexto sobre barrera intestinal |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisión Sistemática y Metaanálisis | Frontiers in Endocrinology | GLP-1 RAs asociados a mejora del SII: GLP-1 y su análogo ROSE-010 inhiben el complejo motor migratorio y reducen la motilidad gastrointestinal; metaanálisis confirma beneficio sintomático |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Reporte Clínico (Fase 1/2) | Scand J Gastroenterology | ROSE-010 redujo el dolor abdominal durante crisis de SII; subanálisis cruzado identifica subpoblación de pacientes con mayor respuesta al tratamiento |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Revisión Sistemática | J Headache Pain | GLP-1 RAs y su potencial en trastornos de dolor; relevancia para manejo del dolor visceral en SII a través de vías neurológicas |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohorte/Observacional | Ann Gastroenterology | Patrones de prescripción y discontinuación de GLP-1 RAs en pacientes con SII; evidencia de mundo real sobre efectos GI adversos y uso en trastornos funcionales |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisión | Experimental Physiology | Papel de las células L y la secreción de GLP-1 en los cambios fisiopatológicos del SII; vincula microbiota, ácidos biliares y sensibilización neuronal intestinal |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observacional | Clin Res Hepatol Gastroenterol | Niveles séricos reducidos de GLP-1 correlacionan con dolor abdominal en IBS-C; se evalúa expresión del receptor GLP-1 en colon |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | Ensayo Clínico (Fase 1/2) | Am J Physiol Gastrointest Liver Physiol | ROSE-010 (30–300 μg sc) en diseño doble ciego controlado con placebo en IBS-C femenino: retraso del vaciamiento gástrico y mejora de la acomodación gástrica documentados |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclínico | Neurogastroenterol Motil | Exendina-4 (GLP-1 RA) ameliora la disfunción GI en modelo de rata Wistar Kyoto de SII; mecanismo mediado por activación de neuronas mientéricas |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclínico | Int J Mol Med | Roles del GLP-1 en la patogénesis del SII experimental en rata (IBS-C e IBS-D); medición de expresión del receptor GLP-1 y respuesta a distensión colorrectal |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Preclínico/Clínico Temprano | Adv Exp Med Biol | GLP-1 aerosólico propuesto como alternativa de administración para diabetes e IBS; proporciona fundamentos sobre el papel de GLP-1 en motilidad intestinal |

---

## Información de Mercado en Argentina

Glucagon (DB00040) no cuenta con ninguna autorización de comercialización registrada en Argentina. El fármaco no está disponible en el mercado local bajo ninguna forma farmacéutica o nombre comercial en la base de datos consultada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN (99.24%) identifica una señal biológicamente plausible, respaldada por revisiones sistemáticas y ensayos clínicos Fase 1/2 completados en SII; sin embargo, toda la evidencia clínica proviene de agonistas GLP-1 (ROSE-010, liraglutide), no de Glucagon directamente, y el fármaco carece de autorización en Argentina y de datos de seguridad evaluables, lo que impide avanzar a evaluación formal sin investigación adicional.

**Para avanzar se necesita:**
- Búsqueda dirigida de ensayos clínicos que usen Glucagon (no análogos GLP-1) específicamente en pacientes con SII
- Obtención de ficha técnica o prospecto para evaluación de seguridad (advertencias, contraindicaciones, interacciones farmacológicas)
- Consulta de DrugBank API para completar datos de mecanismo de acción (MOA) y categorías farmacológicas detalladas
- Evaluación de la vía y forma de administración viable para un uso crónico en SII (Glucagon es actualmente de uso parenteral/emergencia)
- Revisión regulatoria en Argentina sobre la posibilidad de registrar una nueva indicación para un fármaco actualmente sin autorización local
---

