---
layout: default
title: Baclofeno
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 0
---

# Baclofeno
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

# Baclofeno: Evaluación Preliminar — Datos Insuficientes para Reposicionamiento

## Resumen en Una Frase

Baclofeno es un agonista del receptor GABA-B, utilizado tradicionalmente como relajante muscular y antiespasmódico en el tratamiento de la espasticidad de diversas etiologías. Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y no se dispone de autorizaciones de comercialización en Argentina. La evidencia disponible es insuficiente para evaluar un potencial reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en las fuentes consultadas (conocido globalmente como antiespasmódico / relajante muscular) |
| Nueva Indicación Predicha | — Sin predicción generada por TxGNN — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | **L5** (sin estudios ni predicciones aplicables) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generó una Predicción?

Baclofeno (DCI: BACLOFENO) es un derivado del ácido gamma-aminobutírico (GABA) que actúa como agonista selectivo del receptor GABA-B. Se utiliza ampliamente a nivel internacional para el tratamiento de la espasticidad asociada a esclerosis múltiple, lesiones de médula espinal y otras condiciones neurológicas. También ha sido investigado de forma off-label para el trastorno por consumo de alcohol.

Sin embargo, el Evidence Pack actual presenta **vacíos de datos críticos** que impidieron al modelo TxGNN generar predicciones válidas:

1. **Sin identificador DrugBank** (`drugbank_id: null`): La ausencia de un identificador molecular estándar impide la integración del fármaco en el grafo de conocimiento (Knowledge Graph) utilizado por TxGNN para inferir nuevas relaciones fármaco-enfermedad.

2. **Mecanismo de acción no registrado en el pack**: Aunque el MOA de baclofeno es bien conocido en la literatura (agonismo GABA-B), esta información no fue incorporada al Evidence Pack, lo que limita el análisis de plausibilidad mecanística.

3. **Sin autorizaciones regulatorias en Argentina**: El fármaco no está comercializado ni tiene licencias vigentes en el territorio, lo cual reduce la viabilidad inmediata de cualquier estrategia de reposicionamiento local.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack para una nueva indicación predicha.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack para una nueva indicación predicha.

---

## Información de Mercado en Argentina

Baclofeno **no cuenta con autorizaciones de comercialización** vigentes en Argentina según las fuentes consultadas (consulta realizada el 2026-03-29). No se encontraron registros de licencias.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad específicos en el Evidence Pack actual (advertencias, contraindicaciones e interacciones farmacológicas no disponibles en las fuentes consultadas).

> Consultar el prospecto del producto de referencia internacional para información completa de seguridad. Se recomienda consultar fuentes como DrugBank, Micromedex o el prospecto de la FDA para baclofeno.

---

## Brechas de Datos Identificadas

El Evidence Pack documenta las siguientes brechas que deben resolverse antes de cualquier avance:

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede realizar la evaluación inicial de seguridad (S1) | Descargar y analizar PDF del prospecto desde fuente regulatoria |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | **Alta** | Afecta el análisis de relación mecanística | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para baclofeno se encuentra en un estado preliminar con brechas de datos bloqueantes. No se generaron predicciones de nuevas indicaciones por parte de TxGNN, no hay autorizaciones regulatorias en Argentina, y faltan datos esenciales de seguridad y mecanismo de acción. No es posible avanzar en la evaluación de reposicionamiento en estas condiciones.

**Para avanzar se necesita:**
- **Resolver DG001 (Bloqueante):** Obtener y analizar el prospecto completo del fármaco para extraer advertencias, contraindicaciones y precauciones de seguridad
- **Resolver DG002 (Alta):** Consultar DrugBank para obtener el `drugbank_id` (probablemente **DB01558**) y el mecanismo de acción detallado, permitiendo la integración al Knowledge Graph de TxGNN
- **Re-ejecutar el modelo TxGNN** una vez integrados los datos moleculares y farmacológicos completos
- **Evaluar viabilidad regulatoria** en Argentina: determinar si existe interés en la importación o registro local del fármaco antes de invertir recursos en la evaluación de reposicionamiento
- **Revisar literatura internacional** sobre usos off-label de baclofeno (e.g., trastorno por consumo de alcohol, neuralgia del trigémino, reflujo gastroesofágico) como punto de partida para futuras predicciones
---

