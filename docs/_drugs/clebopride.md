---
layout: default
title: Clebopride
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 0
---

# Clebopride
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

# CLEBOPRIDE: Evaluación Inicial — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

CLEBOPRIDE (DB13511) es un fármaco identificado en DrugBank para evaluación de reposicionamiento candidato.
El pipeline TxGNN no generó indicaciones predichas en esta corrida, y los datos de indicaciones originales, mecanismo de acción y seguridad presentan brechas críticas que impiden completar la evaluación estándar.
Sin evidencia clínica ni predicciones disponibles, el candidato no puede avanzar hasta completar la remediación de datos.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin documentación disponible en el Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 — Solo predicción de modelo, sin estudios reales |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No se Generaron Predicciones

El modelo TxGNN no produjo indicaciones candidatas para CLEBOPRIDE. Las causas más probables son:

1. **Cobertura insuficiente en el grafo de conocimiento**: Si el fármaco no posee suficientes aristas en el knowledge graph (interacciones proteína–fármaco, asociaciones gen–enfermedad), el modelo no puede generar predicciones confiables.

2. **Mecanismo de acción ausente**: El MOA está marcado como brecha de datos crítica (DG002), lo que limita la capacidad del modelo para establecer relaciones mecanísticas con enfermedades candidatas.

3. **Sin licencias regulatorias de referencia**: Con 0 autorizaciones registradas en Argentina y 0 en TFDA, no existe ancla regulatoria que oriente las predicciones ni valide la relevancia clínica del candidato.

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto |
|----|-----------|---------------|-----------|---------|
| DG001 | Drug Level | Advertencias/Contraindicaciones (prospecto TFDA) | **Bloqueante** | Impide evaluación de seguridad inicial S1 |
| DG002 | Drug Level | Mecanismo de Acción (MOA) | **Alto** | Impide análisis de relación mecanística |

---

## Consideraciones de Seguridad

Los datos de seguridad son insuficientes para evaluación formal:

- **Advertencias e interacciones farmacológicas**: Sin datos disponibles. Consultar el prospecto oficial para información de seguridad.
- **Consulta DDI**: Ejecutada sin resultados — no se encontraron interacciones en la base de datos consultada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack carece de los datos mínimos necesarios para una evaluación de reposicionamiento: no hay indicaciones originales documentadas, no se generaron predicciones TxGNN, y los datos de seguridad y MOA están ausentes. Proceder sin esta base implicaría un análisis sin sustento.

**Para avanzar se necesita:**
- **DG001 → Remediar (Bloqueante):** Descargar y parsear el PDF del prospecto TFDA para extraer advertencias y contraindicaciones
- **DG002 → Remediar (Alto):** Consultar DrugBank API para obtener el mecanismo de acción (MOA) de CLEBOPRIDE
- **Re-ejecutar el pipeline TxGNN** con datos completos de MOA y perfil de seguridad
- **Verificar cobertura** de CLEBOPRIDE en el knowledge graph de TxGNN (nodos y aristas disponibles)
- **Levantar indicaciones originales** aprobadas en mercados internacionales (p. ej., España o Japón) para anclar el análisis comparativo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

