---
layout: default
title: Capecitabina
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Capecitabina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# CAPECITABINA: Evaluación de Reposicionamiento Incompleta — Datos Insuficientes

## Resumen en Una Frase

CAPECITABINA es un fármaco cuya indicación original no pudo ser recuperada de las fuentes consultadas en este ciclo de recolección.
El modelo TxGNN **no generó predicciones de nuevas indicaciones** para este compuesto, posiblemente debido a la ausencia de datos regulatorios locales cargados en el pipeline.
En consecuencia, **no es posible completar la evaluación de reposicionamiento en este momento**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible |
| Nueva Indicación Predicha | No disponible |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 (sin estudios reales evaluados) |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué la Evaluación Está Incompleta

Las consultas realizadas al 2026-03-29 no retornaron información suficiente para alimentar el pipeline de evaluación:

**Fuentes consultadas y resultados:**

| Fuente | Estado | Resultados | Impacto |
|--------|--------|------------|---------|
| TFDA (registros) | Exitoso | 0 registros | Sin datos regulatorios locales |
| TFDA (prospecto/inserto) | Exitoso | 1 documento encontrado | Datos no integrados al Evidence Pack |
| DrugBank | Exitoso | 1 registro encontrado | Datos no integrados al Evidence Pack |
| Base DDI | No encontrado | 0 | Sin datos de interacciones |

> **Nota importante:** El log de consultas muestra que DrugBank y el prospecto TFDA **sí retornaron resultados**, pero sus datos no fueron capturados en el Evidence Pack actual. Esto sugiere un problema en la etapa de extracción/integración del pipeline, no una ausencia real de información del fármaco.

Dado que `predicted_indications` está vacío y los datos base del fármaco (indicación original, MOA, advertencias) no están disponibles, el modelo TxGNN no pudo generar candidatos de reposicionamiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La ausencia de datos de indicación original, mecanismo de acción y predicciones TxGNN impide realizar cualquier análisis de reposicionamiento fundamentado. Los datos técnicamente existen en las fuentes (DrugBank y prospecto TFDA devolvieron resultados), pero no fueron integrados correctamente al Evidence Pack.

**Para avanzar se necesita:**
- Revisar y corregir el paso de extracción del pipeline para DrugBank (1 resultado encontrado, no capturado): recuperar categorías, MOA, indicaciones originales y datos de toxicidad
- Extraer advertencias, contraindicaciones y clasificación de seguridad del prospecto TFDA (1 documento encontrado, no capturado)
- Verificar si CAPECITABINA cuenta con registro en ANMAT bajo ese INN u otros nombres comerciales (ej. Xeloda), ya que la búsqueda TFDA retornó 0 resultados
- Re-ejecutar el pipeline TxGNN una vez integrados los datos del fármaco para obtener predicciones de nuevas indicaciones
- Completar la búsqueda DDI con el INN correcto o sinónimos farmacológicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

