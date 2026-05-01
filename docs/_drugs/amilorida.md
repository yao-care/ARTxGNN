---
layout: default
title: Amilorida
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 0
---

# Amilorida
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

# Amilorida: Evaluación Preliminar — Sin Nueva Indicación Predicha

---

## Resumen en Una Frase

Amilorida es un diurético ahorrador de potasio que actúa bloqueando los canales epiteliales de sodio (ENaC) en el túbulo renal, utilizado clásicamente en el manejo de hipertensión y edema. En esta evaluación, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y además **no se encuentra comercializado en Argentina** (0 autorizaciones vigentes), lo que limita significativamente la viabilidad de cualquier estrategia de reposicionamiento en este mercado.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en Argentina (conocida internacionalmente como diurético ahorrador de potasio para hipertensión/edema) |
| Nueva Indicación Predicha | — Sin predicción disponible — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin estudios ni predicción del modelo) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué No Hay Predicción?

El modelo TxGNN no generó indicaciones predichas para Amilorida. Esto puede deberse a varios factores:

1. **Cobertura del grafo de conocimiento**: Amilorida podría no estar suficientemente representada en el grafo de conocimiento terapéutico utilizado por TxGNN, o sus conexiones moleculares y fenotípicas no alcanzan el umbral mínimo de confianza para generar una predicción.

2. **Ausencia de identificador DrugBank**: El Evidence Pack no contiene un `drugbank_id` asociado, lo que sugiere que la integración de datos moleculares y farmacológicos pudo haber sido incompleta durante la fase de preparación del grafo.

3. **Perfil farmacológico específico**: Amilorida actúa mediante el bloqueo de canales ENaC, un mecanismo relativamente específico del epitelio renal. Aunque existen investigaciones emergentes sobre el rol de ENaC en otros tejidos (pulmón, colon), es posible que la evidencia disponible aún no sea suficiente para que el modelo identifique oportunidades de reposicionamiento con alta confianza.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados, dado que el modelo no generó predicciones para este fármaco.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible en el contexto de esta evaluación.

---

## Información de Mercado en Argentina

Amilorida **no se encuentra comercializada en Argentina**. No se identificaron autorizaciones vigentes ante la autoridad regulatoria.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|---------------------|---------------------|---------------------|
| — | — | — | Sin autorizaciones registradas |

> **Nota:** La ausencia de comercialización en Argentina implica que cualquier estrategia de reposicionamiento requeriría primero obtener la autorización regulatoria para la indicación original o directamente para la nueva indicación, lo que incrementa significativamente los tiempos y costos del proyecto.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad específicos en el Evidence Pack actual (advertencias, contraindicaciones e interacciones farmacológicas no fueron recuperados de fuentes locales).

> Consultar el prospecto internacional para información de seguridad. A nivel general, Amilorida presenta riesgo de **hiperpotasemia** (especialmente en combinación con IECAs, ARA-II, suplementos de potasio o en pacientes con insuficiencia renal), y está contraindicada en pacientes con niveles elevados de potasio sérico o insuficiencia renal severa.

---

## Brechas de Datos Identificadas

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente Sugerida |
|----|-----------|---------------|-----------|---------|-----------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No es posible completar la evaluación de seguridad inicial (S1) | Prospecto oficial / autoridad regulatoria |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de relación mecanística con nuevas indicaciones | DrugBank API |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Amilorida no cuenta con predicciones de nuevas indicaciones por parte del modelo TxGNN, no está comercializada en Argentina (0 autorizaciones), y presenta brechas de datos críticas que impiden una evaluación completa. No existe base suficiente para avanzar con una estrategia de reposicionamiento en este momento.

**Para avanzar se necesita:**
- Completar la integración del fármaco en el grafo de conocimiento de TxGNN (verificar `drugbank_id` y datos moleculares asociados)
- Obtener datos de mecanismo de acción (MOA) desde DrugBank u otra fuente curada
- Recuperar información de seguridad del prospecto oficial (advertencias, contraindicaciones)
- Re-ejecutar el modelo TxGNN una vez que los datos de entrada estén completos
- Evaluar la viabilidad regulatoria en Argentina si en el futuro se identifican indicaciones candidatas
---

