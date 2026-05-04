---
layout: default
title: Piribedil
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 5
---

# Piribedil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# PIRIBEDIL: De Enfermedad de Parkinson a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

PIRIBEDIL es un agonista de los receptores dopaminérgicos D2/D3, cuya aplicación clínica principal es el tratamiento de la enfermedad de Parkinson y trastornos cognitivos asociados al déficit dopaminérgico.
El modelo TxGNN predice que podría ser efectivo para la **distrofia retiniana con o sin anomalías extraoculares**,
sin embargo, esta predicción está respaldada únicamente por **0 ensayos clínicos** y **15 publicaciones** que abordan anomalías oculares en términos generales, sin evaluar directamente el uso de PIRIBEDIL en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Enfermedad de Parkinson (agonista dopaminérgico D2/D3) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No registrado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos confirmados sobre el mecanismo de acción en la ficha técnica argentina. Según la información conocida derivada del análisis de reposicionamiento documentado en este Evidence Pack, PIRIBEDIL actúa como agonista de los receptores dopaminérgicos D2/D3, compensando la señalización dopaminérgica deficitaria en el estriado. La dopamina sí tiene presencia funcional en la retina —liberada principalmente por células amacrinas— y cumple un rol en la adaptación luminosa (fotoadaptación). Sin embargo, los receptores dopaminérgicos con mayor expresión retiniana son los de tipo D1 y D4, no los D2/D3 que constituyen el blanco principal de PIRIBEDIL.

El vínculo mecanístico entre PIRIBEDIL y las distrofias retinianas es considerado extremadamente débil. Las distrofias retinianas son enfermedades de etiología predominantemente genética (mutaciones en genes como *RPGR*, *RHO*, *USH2A*, entre otros), que causan degeneración estructural del epitelio pigmentario y los fotorreceptores. Un agonista dopaminérgico no posee capacidad para corregir la causa subyacente genética ni revertir el daño estructural ya establecido; cualquier efecto sería, en el mejor de los casos, puramente sintomático y de relevancia clínica incierta.

La alta puntuación otorgada por TxGNN (99.34%) probablemente refleja conexiones en el grafo de conocimiento que comparten nodos de "anomalías extraoculares" entre distintas condiciones neurológicas, sin que esto implique una causalidad biológica real. El análisis mecanístico del propio Evidence Pack concluye que la asociación es de grado "extremadamente bajo (indirecto/especulativo)".

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

> **Aviso importante**: Las 15 publicaciones recuperadas abordan anomalías oculares y extraoculares en términos generales. No se identificó ninguna publicación que evalúe directamente el uso de PIRIBEDIL en distrofia retiniana. La relevancia de esta literatura para la hipótesis de reposicionamiento es considerada muy baja.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Clasificación y características por imagen de lesiones orbitarias oculares pediátricas: lesiones congénitas, del desarrollo, infecciosas y neoplásicas |
| [36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/) | 2023 | Pendiente | Invest Ophthalmol Vis Sci | Mutaciones missense en MAB21L1 causan síndrome ocular AD BAMD (blefarofimosis + disgenesia del segmento anterior y macular) de herencia autosómica dominante |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan J Ophthalmol | Anomalías congénitas de la forma del cristalino, incluyendo asociaciones con disgenesia del segmento anterior y persistencia de estructuras fetales |
| [36116851](https://pubmed.ncbi.nlm.nih.gov/36116851/) | 2022 | Pendiente | Semin Ultrasound CT MR | Anatomía y patología del tercer nervio craneal (oculomotor); la RM es el método de elección para su evaluación |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Observacional | Int J Mol Sci | Anomalías del nervio óptico y la retina asociadas a fibrosis congénita de músculos extraoculares (CFEOM) por mutaciones en KIF21A y TUBB3 |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | J Binocul Vis Ocul Motil | Revisión de los trastornos congénitos de disinerción craneal (CCDDs): limitaciones del movimiento ocular, diagnóstico diferencial y confirmación genética |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Revisión | Am J Ophthalmol | Propuesta de teoría unificadora sobre patogénesis de la maculopatía asociada a anomalías cavitarias del disco óptico y enfoque terapéutico |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Pendiente | J Neuroophthalmol | Caso de sincinesia troclear-oculomotora congénita en niño de 6 años; discusión de fisiopatología de los CCDDs |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klin Monbl Augenheilkd | Ptosis congénita simple y complicada: distrofia grasa y fibrosis del músculo elevador, asociación con errores refractivos y alteración binocular |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Serie/Revisión | Documenta Ophthalmologica | Complejo Wagner-Stickler: degeneración vitreorretiniana con miopía, catarata, vitreo óptico vacío y desprendimientos retinianos de mal pronóstico quirúrgico |

---

## Información de Mercado en Argentina

PIRIBEDIL no se encuentra registrado en Argentina (ANMAT). No existen autorizaciones de comercialización activas. El fármaco se comercializa en algunos países de Europa (p. ej., Francia: Trivastal®) y Asia, pero no cuenta con aprobación local al momento del corte de datos (2026-05-04).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no están disponibles en este Evidence Pack y deben obtenerse del prospecto oficial antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para distrofia retiniana carece de respaldo mecanístico sólido: PIRIBEDIL actúa sobre receptores D2/D3 mientras que la retina expresa predominantemente D1/D4, y las distrofias retinianas tienen etiología genética primaria que no puede ser modificada por agonistas dopaminérgicos. No se registran ensayos clínicos ni publicaciones que evalúen directamente esta combinación fármaco-indicación.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción detallado (MOA) desde DrugBank API (brecha DG002 del Evidence Pack)
- Obtener advertencias y contraindicaciones del prospecto oficial (brecha DG001, clasificada como Blocking)
- Realizar una revisión bibliográfica específica sobre el papel funcional de los receptores D2/D3 en la fisiopatología de distrofias retinianas hereditarias
- **Considerar redirigir el análisis** hacia las indicaciones con mayor racionalidad mecanística identificadas en este mismo Evidence Pack: **Rank 2** (Parálisis agitante juvenil de Hunt) y **Rank 5** (Enfermedad de Parkinson juvenil 19A, PARK19A), ambas con mecanismo D2/D3 de alta pertinencia y recomendación "Research Question"
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

