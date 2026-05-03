---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 4
---

# Memantine
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

# Memantine: De Enfermedad de Alzheimer a Hipertensión Pulmonar

## Resumen en Una Frase

Memantine es un antagonista del receptor NMDA (N-metil-D-aspartato), conocido principalmente por su uso en el tratamiento de la enfermedad de Alzheimer moderada a grave. El modelo TxGNN predice que podría ser efectivo para la **hipertensión pulmonar**, con **0 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección. La evidencia disponible es mayoritariamente indirecta y no establece un vínculo mecanístico directo entre el bloqueo del NMDAR y la fisiopatología vascular pulmonar.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Enfermedad de Alzheimer (demencia moderada a grave) |
| Nueva Indicación Predicha | Hipertensión Pulmonar |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta base de datos. Según la información farmacológica conocida, memantine actúa como antagonista no competitivo y dependiente del voltaje del receptor NMDA, reduciendo la excitotoxicidad glutamatérgica. Su eficacia en la demencia de Alzheimer ha sido ampliamente comprobada a través de este mecanismo, disminuyendo la sobreactivación neuronal crónica por glutamato.

La conexión con la hipertensión pulmonar se apoya en una hipótesis indirecta: el eje glutamato/NMDAR ha sido implicado en la biología de las células musculares lisas vasculares y en la señalización del óxido nítrico (NO), procesos relevantes en la remodelación vascular pulmonar característica de esta enfermedad. Sin embargo, esta relación es especulativa y carece de validación experimental directa en el contexto de la vasculatura pulmonar.

El puntaje elevado de TxGNN (99,54%) probablemente refleja conexiones distantes dentro del grafo de conocimiento biomédico —tales como la asociación entre NMDAR, señalización NO y enfermedad vascular— más que un vínculo mecanístico experimentalmente validado. Ninguna de las dos publicaciones recuperadas evalúa directamente el efecto terapéutico de memantine sobre la hipertensión pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Estudio Animal/Mecanístico | *Theranostics* | Explora el rol del eje glutamato/NMDAR en la sensibilidad a la insulina y el metabolismo lipídico. Menciona incidentalmente la hipertensión arterial pulmonar como condición asociada al eje NMDAR, sin evaluar memantine como tratamiento directo. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Estudio PK Fase 1 *(MN-08, no Memantine)* | *Clinical Drug Investigation* | Evalúa farmacocinética, seguridad y tolerabilidad de MN-08 (derivado nitratado de memantine, un fármaco diferente) en voluntarios chinos sanos. Confirma interés en la clase NMDAR para hipertensión arterial pulmonar, pero no evalúa memantine directamente. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para hipertensión pulmonar carece de respaldo clínico directo: no existen ensayos clínicos registrados y las dos publicaciones disponibles son indirectas —una estudia metabolismo en modelos animales y la otra evalúa un derivado químico distinto (MN-08). Sin evidencia mecanística ni clínica que valide específicamente esta indicación para memantine, no es posible avanzar a las etapas de evaluación superiores.

**Para avanzar se necesita:**
- Estudios preclínicos que establezcan un vínculo directo entre el bloqueo NMDAR y la remodelación vascular pulmonar (proliferación de células musculares lisas, señalización NO)
- Datos completos de MOA de memantine (actualmente identificado como dato faltante en esta base de datos)
- Información de seguridad, advertencias y contraindicaciones del prospecto oficial
- Evaluación de interacciones farmacológicas con tratamientos estándar de hipertensión pulmonar (inhibidores de PDE5, prostanoides, antagonistas de endotelina)
- Definición de una hipótesis mecanística testeable y revisión sistemática de literatura antes de considerar cualquier diseño de estudio clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

