---
layout: default
title: Mosapride
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 1
---

# Mosapride
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

El skill txgnn-pipeline cubre el pipeline técnico de entrenamiento/validación, pero la tarea es generación de informe desde un Evidence Pack — las instrucciones del sistema prompt son suficientes. Procedo directamente con el informe.

---

# Mosapride: De Dispepsia Funcional a Insomnio

## Resumen en Una Frase

Mosapride es un agente gastroprocinético, agonista selectivo del receptor 5-HT4, utilizado principalmente para el tratamiento de la dispepsia funcional y trastornos de la motilidad gastrointestinal.
El modelo TxGNN predice que podría ser efectivo para el **Insomnio**, con un puntaje de confianza del 99.87%.
Sin embargo, la evidencia directa es prácticamente inexistente: los 2 ensayos clínicos identificados evalúan probióticos y solo incluyen Mosapride como medicación de fondo —no como intervención en estudio—, y **no se encontró ninguna publicación** que respalde esta dirección terapéutica.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Dispepsia funcional (agente gastroprocinético) |
| Nueva Indicación Predicha | Insomnio (*Insomnia disease*) |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos completos sobre el mecanismo de acción de Mosapride desde fuentes regulatorias locales. Según la información farmacológica disponible, Mosapride es un **agonista selectivo del receptor 5-HT4 (serotonina tipo 4)**, clasificado como agente gastroprocinético. Su mecanismo primario consiste en facilitar la liberación de acetilcolina en el plexo mientérico del tracto gastrointestinal, acelerando el vaciamiento gástrico y mejorando la motilidad digestiva. Esta acción es altamente selectiva por el receptor 5-HT4 y no genera los efectos antidopaminérgicos centrales de agentes más antiguos como metoclopramida.

El vínculo teórico entre Mosapride y el insomnio es **indirecto y especulativo**. Si bien el sistema serotoninérgico en su conjunto participa en la regulación del sueño, el receptor 5-HT4 no es el subtipo principal de los circuitos sueño-vigilia. Existe una relación epidemiológica conocida entre la dispepsia funcional y los trastornos del sueño —los pacientes con patología gastrointestinal funcional frecuentemente presentan insomnio como comorbilidad—, por lo que el grafo de conocimiento utilizado por TxGNN probablemente asocia estos nodos a través de esa proximidad de comorbilidad, no a través de una farmacología directa.

El alto puntaje TxGNN (0.999) refleja con mayor probabilidad la **asociación de comorbilidad** dispepsia funcional ↔ insomnio en el grafo de enfermedades, antes que un efecto farmacológico directo sobre el sueño. No existe literatura conocida que sustente que Mosapride tenga eficacia primaria para el insomnio.

---

## Evidencia de Ensayos Clínicos

> ⚠️ **Advertencia de relevancia**: Los 2 ensayos identificados son de Grado C (no relevantes para la hipótesis central). Ambos evalúan probióticos en pacientes con dispepsia funcional; Mosapride aparece únicamente como medicación convencional de fondo, no como intervención en estudio. Ninguno mide el insomnio como desenlace.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|--------|-------------|----------------------|
| [NCT07182890](https://clinicaltrials.gov/study/NCT07182890) | Fase 4 | Reclutando | 180 | Evalúa *Clostridium butyricum* para ansiedad y depresión en dispepsia funcional (Roma IV). Mosapride citrato es el tratamiento convencional de fondo para el malestar posprandial, no la intervención bajo estudio. No evalúa insomnio. |
| [NCT07187492](https://clinicaltrials.gov/study/NCT07187492) | Fase 4 | Reclutando | 180 | Evalúa *Bacillus coagulans* para ansiedad y depresión en dispepsia funcional (Roma IV). Mismo diseño: Mosapride como medicación de base estándar, no como intervención principal ni para insomnio. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para Mosapride en insomnio alcanza únicamente Nivel de Evidencia L5 (solo predicción del modelo, sin estudios reales). El vínculo mecanístico es indirecto —basado en comorbilidad epidemiológica entre dispepsia funcional e insomnio, no en farmacología directa sobre el sueño—, la evidencia clínica directa es nula, y el fármaco no está comercializado en Argentina, lo que elimina el punto de partida regulatorio para una estrategia de reposicionamiento local.

**Para avanzar se necesita:**
- Datos completos de mecanismo de acción (MOA) desde DrugBank o literatura primaria para evaluar si existe algún efecto serotoninérgico central relevante
- Al menos un estudio preclínico o de mecanismo que demuestre efecto directo de Mosapride sobre parámetros polisomnográficos o biomarcadores de sueño
- Un ensayo clínico exploratorio (Fase 1/2) que evalúe Mosapride como intervención primaria para insomnio, antes de considerar cualquier avance
- Información de seguridad completa (advertencias, contraindicaciones, interacciones farmacológicas) desde fuentes regulatorias de mercados donde sí está aprobado (Japón, China, India)
- Revisión de indicaciones aprobadas en mercados internacionales para establecer el perfil regulatorio de referencia antes de contemplar ANMAT
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

