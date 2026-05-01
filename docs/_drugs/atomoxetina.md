---
layout: default
title: Atomoxetina
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 0
---

# Atomoxetina
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

# ATOMOXETINA: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina (ISRN), ampliamente conocido por su uso en el tratamiento del Trastorno por Déficit de Atención e Hiperactividad (TDAH). Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y el Evidence Pack presenta múltiples brechas de datos que impiden una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el registro regulatorio consultado (conocida: TDAH) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos preliminares, sin estudios ni predicción) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones Disponibles?

Atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina (NRI). A diferencia de los estimulantes tradicionales (metilfenidato, anfetaminas), actúa bloqueando el transportador de noradrenalina (NET) en la corteza prefrontal, aumentando las concentraciones sinápticas de noradrenalina y, secundariamente, de dopamina en dicha región. Este mecanismo lo distingue como una opción no estimulante para el tratamiento del TDAH.

El array `predicted_indications` del Evidence Pack se encuentra vacío, lo que significa que el modelo TxGNN no ha generado candidatos de reposicionamiento para este fármaco en el ciclo de análisis actual. Esto puede deberse a varias razones: (1) el fármaco no se encuentra representado en el grafo de conocimiento utilizado por TxGNN, (2) las asociaciones fármaco-enfermedad no alcanzaron el umbral mínimo de confianza del modelo, o (3) los datos de entrada del fármaco (DrugBank ID, MOA estructurado) están ausentes, lo que limita la capacidad predictiva.

Adicionalmente, el mecanismo de acción detallado figura como brecha de datos (DG002, severidad Alta), lo cual impacta directamente la capacidad del modelo para establecer relaciones mecanísticas con nuevas indicaciones. Sin un DrugBank ID vinculado ni datos de MOA estructurados, el pipeline de predicción no puede operar de forma completa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados, dado que no se ha generado una indicación predicha para evaluar.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el contexto de reposicionamiento, dado que no se ha generado una indicación predicha.

---

## Información de Mercado en Argentina

Atomoxetina **no se encuentra comercializada** en Argentina según los registros consultados. No existen autorizaciones de comercialización vigentes.

> **Nota:** La ausencia de registro en Argentina no implica que el fármaco carezca de aprobación en otros mercados. Atomoxetina (Strattera®) se encuentra aprobada y comercializada en múltiples países (EE.UU., UE, Japón, entre otros) para el tratamiento del TDAH.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no se encuentran disponibles en el Evidence Pack actual.

> **Brechas de datos identificadas:**
> - **DG001** (Severidad: Bloqueante) — Faltan las advertencias y contraindicaciones del prospecto regulatorio. Se requiere descargar y analizar el prospecto oficial.
> - **DG002** (Severidad: Alta) — Falta el mecanismo de acción estructurado. Se requiere consulta a la API de DrugBank.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No es posible avanzar con una evaluación de reposicionamiento dado que el modelo TxGNN no ha generado predicciones de nuevas indicaciones para Atomoxetina. Adicionalmente, existen brechas de datos críticas (ausencia de DrugBank ID, MOA, datos de seguridad) que impiden una evaluación integral. El fármaco tampoco se encuentra comercializado en Argentina, lo que añade una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Vincular el DrugBank ID correcto para Atomoxetina (probablemente **DB00289**)
- Obtener los datos estructurados de mecanismo de acción (MOA) desde DrugBank
- Descargar y analizar el prospecto regulatorio para extraer advertencias y contraindicaciones
- Re-ejecutar el modelo TxGNN con los datos completos del fármaco para generar predicciones
- Evaluar el estado regulatorio en Argentina y la viabilidad de importación o registro
---

