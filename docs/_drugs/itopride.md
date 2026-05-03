---
layout: default
title: Itopride
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 4
---

# Itopride
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

---

# ITOPRIDE: De Dispepsia Funcional a Enfermedad de Crohn del Intestino Delgado

## Resumen en Una Frase

Itopride es un agente procinético gastrointestinal que actúa mediante inhibición de la acetilcolinesterasa y antagonismo del receptor D2 de dopamina, utilizado originalmente para el tratamiento de la dispepsia funcional y trastornos de la motilidad gastrointestinal. El modelo TxGNN predice que podría ser efectivo para la **Enfermedad de Crohn del Intestino Delgado**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección a la fecha. Esta predicción se sustenta exclusivamente en el algoritmo de grafos de conocimiento biológico (nivel L5), sin evidencia empírica directa disponible.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Dispepsia funcional / Trastornos de motilidad gastrointestinal |
| Nueva Indicación Predicha | Enfermedad de Crohn del Intestino Delgado |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción provenientes de DrugBank (brecha identificada como DG002). Sin embargo, según la información inferida del Evidence Pack, Itopride ejerce su efecto mediante dos mecanismos complementarios: **inhibición de la acetilcolinesterasa** —elevando la concentración de acetilcolina (ACh) en la pared intestinal— y **antagonismo del receptor D2 de dopamina** —removiendo la inhibición dopaminérgica sobre la motilidad del tracto gastrointestinal—. Ambos mecanismos convergen en promover el vaciamiento gástrico y la peristalsis, lo que sustenta su uso clásico en dispepsia funcional.

La conexión teórica con la Enfermedad de Crohn del Intestino Delgado descansa en la **vía antiinflamatoria colinérgica (Cholinergic Anti-inflammatory Pathway, CAP)**: al aumentar la disponibilidad de ACh en la mucosa intestinal, Itopride podría activar la señalización vagal y suprimir la producción de citoquinas proinflamatorias clave como el TNF-α e IL-6, que son centrales en la patogenia de la enfermedad de Crohn. Esta hipótesis ha recibido atención científica creciente en el contexto de enfermedades inflamatorias intestinales.

No obstante, la conexión mecanística debe calificarse como **indirecta y especulativa**. La Enfermedad de Crohn es una condición inmunomediada compleja cuyo tratamiento estándar son inmunosupresores (azatioprina, metotrexato) y agentes biológicos anti-TNF. El aumento de la motilidad intestinal podría, paradójicamente, **agravar síntomas como el dolor abdominal tipo cólico** en pacientes con Crohn activo del intestino delgado. La racionalidad mecanística global se evalúa como **baja a moderada**, y el modelo TxGNN podría estar capturando correlaciones de fondo en el grafo de conocimiento más que una relación causal farmacológica directa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Itopride **no cuenta con ninguna autorización de comercialización** registrada en Argentina a la fecha de corte del análisis (2026-05-01). El fármaco no se encuentra disponible en el mercado argentino bajo ninguna presentación o nombre comercial.

---

## Otras Indicaciones Predichas por TxGNN

Este paquete de evidencia es de tipo multi-indicación. Además de la indicación principal, el modelo TxGNN identificó tres candidatos adicionales para Itopride:

| Rango | Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Racionalidad Mecanística |
|-------|------------|---------------|-------------------|---------------|--------------------------|
| 2 | Insuficiencia Venosa | 99.23% | L5 | Hold | **Muy débil** — probable asociación espuria en el grafo de conocimiento; sin mecanismo directo conocido |
| 3 | Aclorhidria | 99.16% | L5 | Research Question | **Moderada** para subtipos funcionales; ACh estimula receptores M3 de células parietales gástricas |
| 4 | Hernia de Hiato | 99.02% | L5 | Research Question | **Alta** — mejor candidato mecanístico del conjunto |

> **Nota sobre la Hernia de Hiato (Rango 4):** Esta es la indicación con mayor racionalidad mecanística entre las cuatro predicciones. Itopride aumenta la presión del esfínter esofágico inferior (EEI) mediante antagonismo D2 —la dopamina normalmente inhibe el EEI— y acelera el vaciamiento gástrico, reduciendo el volumen disponible para el reflujo. El precedente clínico de Metoclopramide (también antagonista D2) en GERD y hernia de hiato provee evidencia analógica indirecta. Esta indicación merece consideración prioritaria frente a la Enfermedad de Crohn como siguiente paso de investigación.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de Itopride para Enfermedad de Crohn del Intestino Delgado se basa exclusivamente en el algoritmo TxGNN (L5), sin ningún ensayo clínico ni publicación que la respalde directamente. La conexión mecanística es indirecta, y el riesgo de exacerbación sintomática en pacientes con Crohn activo representa una preocupación clínica real. Entre las cuatro indicaciones predichas, la **Hernia de Hiato** posee la racionalidad mecanística más sólida y debería priorizarse como siguiente candidato a evaluar.

**Para avanzar se necesita:**
- Completar los datos de mecanismo de acción (MOA) desde DrugBank (brecha DG002)
- Obtener y revisar las advertencias y contraindicaciones del prospecto oficial (brecha DG001)
- Realizar búsqueda de literatura sobre Itopride en modelos preclínicos de enfermedad inflamatoria intestinal (EII) para evaluar si la vía CAP tiene sustento experimental
- Redirigir el análisis hacia la indicación de **Hernia de Hiato** como candidato prioritario de reposicionamiento
- Verificar el estado regulatorio de Itopride en mercados donde sí está aprobado (ej. Japón, India, Europa) para obtener datos de seguridad reales antes de cualquier avance clínico en Argentina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

