---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 0
---

# Bosentan
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

# Bosentan: Evaluación Preliminar — Datos Insuficientes para Reposicionamiento

---

## Resumen en Una Frase

Bosentan es un antagonista de los receptores de endotelina (ETA/ETB), conocido internacionalmente por su uso en hipertensión arterial pulmonar (HAP). Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco. Además, el evidence pack presenta múltiples brechas de datos críticas que impiden una evaluación completa.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el evidence pack (conocida internacionalmente: Hipertensión Arterial Pulmonar) |
| Nueva Indicación Predicha | — Sin predicciones generadas — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin estudios asociados a una nueva indicación) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué no se Generaron Predicciones?

Bosentan (DrugBank ID: DB00559) es un antagonista dual de los receptores de endotelina tipo A (ETA) y tipo B (ETB). Su mecanismo de acción consiste en bloquear la vasoconstricción mediada por endotelina-1, lo que reduce la presión arterial pulmonar y mejora la capacidad de ejercicio en pacientes con hipertensión arterial pulmonar (HAP). Es un fármaco ampliamente utilizado a nivel mundial bajo nombres comerciales como Tracleer®.

Sin embargo, el evidence pack actual **no contiene predicciones de TxGNN** para nuevas indicaciones (`predicted_indications` vacío). Esto puede deberse a varias razones:

1. **Cobertura del grafo de conocimiento**: Es posible que el nodo correspondiente a Bosentan no esté suficientemente conectado en el grafo de conocimiento (KG) utilizado por TxGNN, lo que limita la capacidad del modelo para generar predicciones con puntuación significativa.
2. **Especificidad del mecanismo**: El bloqueo de los receptores de endotelina es un mecanismo altamente específico para la fisiopatología vascular pulmonar, lo que podría limitar las asociaciones cruzadas con otras enfermedades en el modelo.
3. **Brechas de datos de entrada**: La ausencia de datos de mecanismo de acción (MOA) y de información regulatoria en el evidence pack podría haber limitado el procesamiento del pipeline de predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con una nueva indicación predicha, dado que no se generaron predicciones de reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con una nueva indicación predicha disponible en este evidence pack.

---

## Información de Mercado en Argentina

Bosentan **no se encuentra comercializado** en Argentina según los datos disponibles. No se registran autorizaciones vigentes.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|---------------------|---------------------|---------------------|
| — | — | — | — |

> **Nota:** La ausencia de registro en Argentina no implica que el fármaco carezca de aprobación en otros mercados. Bosentan cuenta con aprobación de la FDA (EE.UU.), EMA (Europa) y otras agencias regulatorias para hipertensión arterial pulmonar.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el evidence pack actual (advertencias, contraindicaciones e interacciones farmacológicas no disponibles).

> Consultar el prospecto internacional del producto (Tracleer®) para información de seguridad completa. Se conocen las siguientes precauciones relevantes de Bosentan a nivel internacional:
> - **Hepatotoxicidad**: Requiere monitoreo mensual de transaminasas hepáticas (ALT/AST)
> - **Teratogenicidad**: Categoría X — contraindicado en embarazo
> - **Interacciones con CYP**: Bosentan es inductor de CYP3A4 y CYP2C9, lo que puede reducir la eficacia de anticonceptivos hormonales, warfarina y otros fármacos metabolizados por estas vías

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Remediación Sugerida |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No es posible realizar la evaluación inicial de seguridad (S1) | Descargar y analizar el prospecto desde la agencia regulatoria correspondiente |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | Alta | Afecta el análisis de relación mecanística | Consultar la API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El evidence pack de Bosentan presenta brechas de datos críticas y, fundamentalmente, **no contiene predicciones de nuevas indicaciones** por parte de TxGNN. Sin predicciones generadas, no es posible evaluar oportunidades de reposicionamiento en este momento. Además, el fármaco no está comercializado en Argentina, lo que añade complejidad regulatoria para cualquier iniciativa futura.

**Para avanzar se necesita:**
- Completar los datos de mecanismo de acción (MOA) desde DrugBank API
- Obtener y analizar el prospecto completo del fármaco desde la agencia regulatoria correspondiente (o prospecto internacional de Tracleer®)
- Verificar la cobertura de Bosentan en el grafo de conocimiento de TxGNN y, de ser necesario, enriquecer el nodo del fármaco con datos adicionales
- Re-ejecutar el pipeline de predicción de TxGNN una vez que las brechas de datos hayan sido subsanadas
- Evaluar la viabilidad regulatoria de importación/registro en Argentina si se identifican nuevas indicaciones prometedoras en futuras iteraciones
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

