---
layout: default
title: Benserazida
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 0
---

# Benserazida
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

# BENSERAZIDA: Evaluación de Candidato para Reposicionamiento

## Resumen en Una Frase

Benserazida es un inhibidor periférico de la DOPA descarboxilasa, utilizado en combinación con levodopa (co-beneldopa/Madopar) para el tratamiento de la enfermedad de Parkinson.
El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el ciclo de análisis actual, y **no se dispone de datos regulatorios ni de seguridad** en el territorio evaluado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (en combinación con Levodopa) — *según conocimiento farmacológico; no se encontraron autorizaciones locales* |
| Nueva Indicación Predicha | — Sin predicciones generadas por TxGNN |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | N/A — Sin predicción que evaluar |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

## Por qué no hay Predicciones Disponibles?

Benserazida es un inhibidor de la DOPA descarboxilasa de acción periférica. No atraviesa la barrera hematoencefálica y su función principal es prevenir la conversión periférica de levodopa en dopamina, reduciendo así los efectos adversos periféricos (náuseas, hipotensión) y permitiendo que una mayor proporción de levodopa alcance el sistema nervioso central. Por sí solo, benserazida carece de actividad terapéutica significativa; su valor reside en la sinergia con levodopa.

El modelo TxGNN no generó predicciones de nuevas indicaciones para benserazida en este ciclo de análisis. Esto puede deberse a varios factores: (1) la ausencia de un identificador DrugBank válido (`drugbank_id: null`) limita la integración del fármaco en el grafo de conocimiento; (2) benserazida funciona exclusivamente como adyuvante farmacocinético y no posee un mecanismo de acción independiente con potencial terapéutico directo; (3) la falta de datos de mecanismo de acción detallado (`original_moa: [Data Gap]`) reduce la capacidad del modelo para inferir conexiones con nuevas enfermedades.

Adicionalmente, el fármaco no se encuentra comercializado en el territorio evaluado (0 autorizaciones encontradas), lo que limita significativamente la viabilidad regulatoria de cualquier estrategia de reposicionamiento local.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados, dado que no se generaron predicciones de nuevas indicaciones.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el contexto de reposicionamiento, dado que no se generaron predicciones de nuevas indicaciones.

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad. No se encontraron datos de advertencias, contraindicaciones ni interacciones farmacológicas en las fuentes consultadas para este territorio.

**Nota:** Aunque los datos locales no están disponibles, la literatura internacional reporta para benserazida (en combinación con levodopa) precauciones relevantes incluyendo: discinesias, síndrome neuroléptico maligno al suspender abruptamente, precaución en pacientes con glaucoma de ángulo cerrado, úlcera péptica activa e insuficiencia hepática o renal severa.

## Brechas de Datos Identificadas

| ID | Categoría | Dato Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede realizar evaluación de seguridad inicial (S1) | Autoridad regulatoria — descargar y analizar prospecto PDF |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de relación mecanística | DrugBank — consultar API de DrugBank |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen predicciones de TxGNN para nuevas indicaciones de benserazida. El fármaco no está comercializado en el territorio evaluado, carece de identificador DrugBank válido, y presenta brechas de datos críticas (seguridad y MOA). Además, su naturaleza como adyuvante farmacocinético (sin actividad terapéutica independiente) reduce inherentemente su potencial como candidato de reposicionamiento.

**Para avanzar se necesita:**
- Resolver la brecha de datos **bloqueante** DG001: obtener información de seguridad del prospecto oficial
- Asignar un `drugbank_id` válido para integrar benserazida en el grafo de conocimiento de TxGNN (DrugBank ID conocido: **DB11770**)
- Completar datos de mecanismo de acción (MOA) detallado desde DrugBank
- Re-ejecutar el modelo TxGNN una vez completados los datos anteriores para verificar si se generan predicciones
- Evaluar si el reposicionamiento debe enfocarse en la combinación levodopa/benserazida en lugar de benserazida como monodroga
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

