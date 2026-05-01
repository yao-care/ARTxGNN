---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Bimatoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bimatoprost: Evaluación Preliminar — Sin Nuevas Indicaciones Predichas

## Resumen en Una Frase

Bimatoprost es un análogo sintético de prostaglandina F2α, ampliamente conocido por su uso en el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular, así como para la hipotricosis de pestañas. En esta evaluación, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y el Evidence Pack presenta múltiples brechas de datos que impiden una evaluación completa.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (conocida: glaucoma / hipertensión ocular) |
| Nueva Indicación Predicha | — Ninguna predicción generada — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | N/A (sin predicción) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se generaron predicciones?

Bimatoprost (DrugBank ID: [DB00905](https://go.drugbank.com/drugs/DB00905)) es un análogo sintético de la prostamida, estructuralmente relacionado con la prostaglandina F2α. Su mecanismo de acción principal consiste en aumentar el flujo de salida del humor acuoso a través de la vía uveoescleral y trabecular, reduciendo así la presión intraocular. También se utiliza tópicamente para estimular el crecimiento de las pestañas.

La ausencia de predicciones por parte del modelo TxGNN puede deberse a varios factores:

1. **Perfil farmacológico altamente específico**: Bimatoprost actúa predominantemente a nivel ocular local, con efectos sistémicos limitados. Esto restringe el espacio de indicaciones potenciales que el modelo podría explorar.
2. **Brechas de datos en el Evidence Pack**: El mecanismo de acción detallado (MOA) no fue incorporado al modelo, lo cual limita la capacidad de TxGNN para identificar conexiones con otras patologías en el grafo de conocimiento.
3. **Ausencia de registro regulatorio en Argentina**: Sin autorizaciones locales, el fármaco carece de la información regulatoria contextual que podría alimentar la predicción.

Es importante señalar que la falta de predicciones **no implica** que Bimatoprost carezca de potencial de reposicionamiento. Simplemente indica que, con los datos disponibles actualmente, el modelo no identificó candidatos con suficiente confianza.

---

## Evidencia de Ensayos Clínicos

El Evidence Pack no contiene predicciones de nuevas indicaciones, por lo que no se realizó búsqueda de ensayos clínicos asociados a reposicionamiento.

> Actualmente no hay ensayos clínicos relacionados registrados para nuevas indicaciones predichas.

---

## Evidencia de Literatura

El Evidence Pack no contiene predicciones de nuevas indicaciones, por lo que no se realizó búsqueda de literatura asociada a reposicionamiento.

> Actualmente no hay literatura relacionada disponible para nuevas indicaciones predichas.

---

## Información de Mercado en Argentina

Bimatoprost **no se encuentra comercializado** en Argentina. No se identificaron autorizaciones de ANMAT vigentes para este principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|--------------------|--------------------|---------------------|
| — | — | — | Sin autorizaciones registradas |

> **Nota**: La ausencia de registro en Argentina representa una barrera regulatoria significativa. Cualquier estrategia de reposicionamiento requeriría primero la obtención de la autorización de comercialización correspondiente ante ANMAT.

---

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad.

No se dispone de datos de seguridad en el Evidence Pack actual (advertencias, contraindicaciones e interacciones farmacológicas pendientes de recopilación). A nivel general, los efectos adversos conocidos de Bimatoprost incluyen:

- Hiperemia conjuntival
- Prurito ocular
- Crecimiento de pestañas
- Hiperpigmentación del iris (cambio permanente del color)
- Oscurecimiento periorbital de la piel
- Enoftalmos y cambios periorbitales (prostaglandin-associated periorbitopathy)

*Estos datos provienen de conocimiento farmacológico general y no del Evidence Pack proporcionado.*

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | Imposibilita la evaluación de seguridad inicial (S1) | Descargar y analizar prospecto desde sitio regulatorio |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de relación mecanística | Consulta a API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se generaron predicciones de nuevas indicaciones por parte de TxGNN para Bimatoprost. Además, el fármaco no está comercializado en Argentina y existen brechas de datos críticas (incluyendo una de severidad bloqueante) que impiden completar la evaluación. No es posible avanzar en la evaluación de reposicionamiento en estas condiciones.

**Para avanzar se necesita:**
- Resolver la brecha de datos **DG001** (bloqueante): obtener las advertencias y contraindicaciones del prospecto oficial
- Resolver la brecha de datos **DG002**: incorporar el mecanismo de acción detallado desde DrugBank para alimentar adecuadamente el modelo TxGNN
- Re-ejecutar el modelo TxGNN una vez que se disponga de datos completos de MOA y perfil farmacológico
- Evaluar la viabilidad regulatoria de registro ante ANMAT como paso previo a cualquier estrategia de reposicionamiento en Argentina
---

