---
layout: default
title: Atorvastatín
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 0
---

# Atorvastatín
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

# ATORVASTATÍN: Informe de Evaluación de Reposicionamiento

## Resumen en Una Frase

Atorvastatín es una estatina ampliamente utilizada a nivel mundial como inhibidor de la HMG-CoA reductasa para el tratamiento de la hipercolesterolemia y la reducción del riesgo cardiovascular. El presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, y **no se registran autorizaciones de comercialización en Argentina**, por lo que actualmente no es posible realizar una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (conocida: hipercolesterolemia / dislipidemia) |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 — Solo datos preliminares, sin predicción ni estudios asociados |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones Disponibles?

El Evidence Pack recibido para Atorvastatín presenta múltiples brechas de datos críticas que impiden la generación de una evaluación de reposicionamiento completa:

1. **Ausencia de predicciones TxGNN:** El campo `predicted_indications` se encuentra vacío. Sin una indicación candidata predicha por el modelo, no es posible evaluar la viabilidad de reposicionamiento ni asignar un nivel de evidencia basado en ensayos clínicos o literatura.

2. **Mecanismo de acción no documentado en el pack:** Aunque Atorvastatín es ampliamente conocido como un inhibidor competitivo de la HMG-CoA reductasa —enzima clave en la biosíntesis hepática de colesterol—, el Evidence Pack marca el MOA como brecha de datos (DG002, severidad Alta). Este dato es esencial para el análisis de plausibilidad mecanística en cualquier indicación nueva.

3. **Sin registro regulatorio en Argentina:** No se identificaron autorizaciones de comercialización (0 licencias). Esto implica que, aun si existiera una indicación candidata prometedora, la vía regulatoria para el reposicionamiento requeriría primero la aprobación del fármaco base en el país.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack, dado que no se generó una indicación predicha para evaluar.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack, dado que no se generó una indicación predicha para evaluar.

---

## Información de Mercado en Argentina

No se encontraron autorizaciones de comercialización para Atorvastatín en Argentina según los datos del Evidence Pack. El estado de mercado reportado es **"No comercializado"** con **0 licencias** registradas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no se encuentran disponibles en el Evidence Pack actual.

> **Nota:** Las consultas realizadas a las fuentes de seguridad (DDI, prospecto TFDA) no arrojaron resultados para esta denominación del fármaco (consultas del 2026-03-29).

---

## Brechas de Datos Identificadas

El Evidence Pack documenta las siguientes brechas que deben resolverse antes de proceder:

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Fuente para Remediación |
|----|-----------|---------------|-----------|---------|------------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No es posible iniciar la evaluación de seguridad (S1) | Sitio oficial TFDA — descargar y analizar PDF del prospecto |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | Alta | Afecta el análisis de relación mecanística | DrugBank API |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para Atorvastatín carece de los elementos fundamentales para una evaluación de reposicionamiento: no hay indicaciones predichas por TxGNN, no hay registro regulatorio en Argentina, y existen brechas de datos bloqueantes en seguridad y mecanismo de acción. No es posible avanzar en la evaluación hasta que se resuelvan estas carencias.

**Para avanzar se necesita:**
- Ejecutar el modelo TxGNN con los datos correctos de Atorvastatín para generar indicaciones predichas
- Resolver la brecha DG001 (bloqueante): obtener advertencias y contraindicaciones del prospecto oficial
- Resolver la brecha DG002: consultar DrugBank API para obtener el mecanismo de acción detallado (DrugBank ID: [DB01076](https://go.drugbank.com/drugs/DB01076) — Atorvastatin)
- Verificar la denominación del fármaco utilizada en las consultas (ATORVASTATÍN con acento puede diferir de las bases de datos que usan "Atorvastatin")
- Confirmar el estado regulatorio en Argentina, ya que atorvastatina es comercializada globalmente bajo múltiples marcas (Lipitor®, genéricos), y su ausencia en el pack podría deberse a un error de búsqueda

---

> ⚠️ **Aviso importante:** Este informe es únicamente para fines de investigación y no constituye asesoramiento médico. Los candidatos de reposicionamiento de fármacos requieren validación clínica antes de su aplicación.
---

