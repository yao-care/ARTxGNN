---
layout: default
title: Amantadina
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 0
---

# Amantadina
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

# AMANTADINA: Evaluación Preliminar — Datos Insuficientes para Reposicionamiento

---

## Resumen en Una Frase

Amantadina es un fármaco conocido internacionalmente como antiviral (Influenza A) y agente antiparkinsonianos (antagonista NMDA / agonista dopaminérgico indirecto). El presente Evidence Pack **no contiene predicciones de TxGNN** para nuevas indicaciones, y presenta múltiples brechas de datos críticas que impiden avanzar en la evaluación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (conocida internacionalmente: Influenza A, Enfermedad de Parkinson, síntomas extrapiramidales inducidos por fármacos) |
| Nueva Indicación Predicha | **Sin predicción** — el modelo TxGNN no generó indicaciones candidatas |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | **L5** (sin datos de predicción ni estudios asociados) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicción de Reposicionamiento?

El Evidence Pack para Amantadina presenta **brechas de datos críticas** que impidieron la generación de predicciones por parte del modelo TxGNN:

1. **Ausencia de DrugBank ID**: No se pudo vincular el fármaco a su perfil farmacológico completo en DrugBank, lo que limita la capacidad del modelo para identificar relaciones mecanísticas entre el fármaco y posibles nuevas indicaciones.

2. **Mecanismo de acción (MOA) no disponible en el pack**: Aunque Amantadina es un fármaco bien caracterizado a nivel internacional — actúa como antagonista del receptor NMDA, facilita la liberación de dopamina y bloquea los canales iónicos de la proteína M2 del virus Influenza A — esta información no fue incorporada al Evidence Pack, limitando el análisis de relaciones mecanísticas.

3. **Sin registro regulatorio en Argentina**: Amantadina no cuenta con autorizaciones de comercialización vigentes en Argentina (ANMAT), por lo que no existen datos regulatorios locales que alimenten el modelo.

Sin estos datos fundamentales, el pipeline de predicción no pudo ejecutarse de manera confiable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack.

> **Nota:** A nivel internacional, Amantadina cuenta con amplia evidencia clínica para sus indicaciones aprobadas (Parkinson, Influenza A, fatiga en esclerosis múltiple, lesión cerebral traumática). Sin embargo, esta información no fue incluida en el presente Evidence Pack y no está vinculada a una predicción de reposicionamiento específica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack.

---

## Información de Mercado en Argentina

Amantadina **no se encuentra comercializada** en Argentina. No se identificaron autorizaciones de comercialización (ANMAT) vigentes para este principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|---------------------|---------------------|---------------------|
| — | — | — | — |

> No se encontraron registros.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el presente Evidence Pack. Consultar el prospecto para información de seguridad.

> **Referencia general (no incluida en el Evidence Pack):** A nivel internacional, las advertencias conocidas de Amantadina incluyen riesgo de síndrome neuroléptico maligno al suspender abruptamente, prolongación del intervalo QT, impulsos patológicos (ludopatía), ideación suicida, y exacerbación de insuficiencia cardíaca congestiva. Estas advertencias deberán confirmarse con fuentes regulatorias oficiales antes de cualquier evaluación formal.

---

## Brechas de Datos Identificadas

El Evidence Pack documenta las siguientes brechas críticas que deben resolverse antes de avanzar:

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto (ANMAT) | **Bloqueante** | No es posible realizar la evaluación inicial de seguridad (S1) | Sitio web de ANMAT — descargar y analizar prospecto PDF |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | **Alta** | Afecta el análisis de relación mecanística con nuevas indicaciones | Consulta a API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Amantadina presenta brechas de datos bloqueantes: no hay predicción de TxGNN, no se dispone de DrugBank ID, el MOA no está documentado en el pack, y el fármaco no está comercializado en Argentina. No es posible evaluar el potencial de reposicionamiento sin resolver estas deficiencias fundamentales.

**Para avanzar se necesita:**
- Vincular Amantadina a su **DrugBank ID** correspondiente (DB00915) y obtener el perfil farmacológico completo
- Incorporar el **mecanismo de acción** detallado (antagonista NMDA, facilitador de liberación dopaminérgica, bloqueador de proteína M2)
- Verificar el **estado regulatorio** actualizado en Argentina (ANMAT) o, en su defecto, evaluar la viabilidad de importación
- Obtener las **advertencias, contraindicaciones y precauciones** del prospecto oficial
- **Re-ejecutar el modelo TxGNN** una vez completados los datos anteriores para generar predicciones de reposicionamiento válidas
- Evaluar si las indicaciones internacionales no aprobadas localmente (ej. fatiga en esclerosis múltiple, lesión cerebral traumática) podrían constituir oportunidades de reposicionamiento prioritarias
---

