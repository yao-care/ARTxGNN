---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Citalopram: Evaluación con Datos Insuficientes para Reposicionamiento

## Resumen en Una Frase

Citalopram (DB00215) es un fármaco con registro en DrugBank, pero el Evidence Pack actual no contiene indicaciones originales documentadas ni predicciones TxGNN activas.
El modelo **no generó indicaciones predichas** en esta ejecución, por lo que no es posible evaluar una nueva dirección terapéutica en este momento.
La evaluación queda en estado **Hold** hasta completar las brechas de datos críticas identificadas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos en el pack (original_indications vacío) |
| Nueva Indicación Predicha | **Sin predicciones disponibles** (predicted_indications vacío) |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | **L5** – Sin estudios reales; sin predicción activa del modelo |
| Estado de Mercado en Argentina | ✗ No comercializado (0 autorizaciones registradas) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No hay Predicción Disponible

El pipeline TxGNN devolvió un array vacío en `predicted_indications`. Esto puede ocurrir por alguna de las siguientes razones:

1. **Brechas de datos bloqueantes**: El pack registra dos gaps de severidad *Blocking* / *High*: ausencia del prospecto oficial (DG001) y ausencia del mecanismo de acción (DG002). Sin MOA, el modelo Knowledge Graph puede no conectar el nodo del fármaco con nodos de enfermedad con suficiente confianza para generar una predicción rankeada.

2. **Sin indicaciones originales registradas**: El campo `original_indications` está vacío, lo que impide al pipeline contrastar la indicación base con candidatos de reposicionamiento.

3. **Sin datos de seguridad**: Todos los campos de `safety` contienen gaps, lo que puede filtrar candidatos en etapas tempranas de triage de seguridad.

Hasta resolver DG001 y DG002, el modelo no puede generar una predicción confiable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados (sin indicación predicha activa sobre la cual buscar evidencia).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible (sin indicación predicha activa sobre la cual buscar evidencia).

---

## Información de Mercado en Argentina

No hay autorizaciones de comercialización registradas para Citalopram en esta consulta (total_licenses: 0).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene predicciones TxGNN ni indicaciones originales documentadas; sin estos insumos no es posible evaluar viabilidad de reposicionamiento ni la solidez de la evidencia clínica.

**Para avanzar se necesita:**

- **[DG001 – Bloqueante]** Descargar y parsear el prospecto oficial (ANMAT/fuente regulatoria) para obtener indicaciones aprobadas, advertencias clave y contraindicaciones
- **[DG002 – Alto]** Consultar DrugBank API para recuperar el mecanismo de acción (MOA) completo y las categorías farmacológicas del fármaco
- Re-ejecutar el pipeline TxGNN una vez cargados los datos anteriores para generar `predicted_indications` con puntaje de confianza
- Verificar si existen registros ANMAT activos para Citalopram que no hayan sido capturados en la consulta TFDA actual (posible desfase de fuente de datos)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

