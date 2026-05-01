---
layout: default
title: Cilastatín
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 0
---

# Cilastatín
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

# CILASTATÍN: Evaluación de Reposicionamiento — Sin Predicciones Disponibles

## Resumen en Una Frase

Cilastatín es un inhibidor de la dihidropeptidasa renal (DHP-I) utilizado clásicamente como componente de la combinación imipenem/cilastatín para el tratamiento de infecciones bacterianas graves, previniendo la degradación renal del antibiótico.
El modelo TxGNN **no generó predicciones de reposicionamiento** para este fármaco en el presente ciclo de análisis.
La evaluación queda suspendida hasta completar los datos faltantes identificados.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (sin autorizaciones registradas en Argentina) |
| Nueva Indicación Predicha | Sin predicciones generadas |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | N/A |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No Hay Predicción Disponible

El pipeline TxGNN devolvió un arreglo vacío en `predicted_indications`. Existen dos causas probables que se deben investigar antes de continuar:

**1. Nodo no encontrado en el grafo de conocimiento (KG):** El identificador DrugBank es nulo (`drugbank_id: null`), lo que puede impedir que el modelo mapee correctamente al nodo del fármaco dentro del KG de TxGNN. Sin nodo anclado, el modelo no puede propagar señales y no produce puntuaciones de enfermedad.

**2. Umbral de score no superado:** Alternativamente, el nodo puede existir en el KG pero ninguna enfermedad superó el umbral mínimo configurado, posiblemente por escasez de relaciones en el grafo para este fármaco.

Adicionalmente, la ausencia del mecanismo de acción (MOA) en el Evidence Pack impide realizar el análisis de plausibilidad biológica que normalmente refuerza o cuestiona las predicciones del modelo.

---

## Brechas de Datos Identificadas

| ID | Categoría | Dato Faltante | Severidad | Acción Requerida |
|----|-----------|---------------|-----------|-----------------|
| DG001 | Drug Level | Advertencias/contraindicaciones (ANMAT) | **Bloqueante** | Descargar prospecto oficial y extraer secciones de seguridad |
| DG002 | Drug Level | Mecanismo de acción (MOA) | Alta | Consultar DrugBank API con nombre INN: "cilastatin" |
| DG003 | Pipeline | DrugBank ID ausente | Alta | Resolver mapping INN → DrugBank ID para anclar nodo en KG |

---

## Información de Mercado en Argentina

Cilastatín no cuenta con autorizaciones de comercialización registradas en Argentina. No es posible presentar tabla de productos aprobados.

> El fármaco existe en el mercado global exclusivamente como combinación fija (imipenem + cilastatín), bajo marcas como **Tienam** e **Imipenem/Cilastatín Genérico**. Es posible que las autorizaciones de ANMAT estén registradas bajo el nombre de la combinación y no bajo el INN individual "cilastatín".

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El modelo TxGNN no generó predicciones para este fármaco, lo que junto con la ausencia del DrugBank ID, MOA y datos de seguridad hace imposible completar la evaluación de reposicionamiento en este ciclo.

**Para avanzar se necesita:**

1. **Resolver el DrugBank ID** — Buscar "cilastatin" en DrugBank (probable ID: DB01398) y actualizar el Evidence Pack para permitir el anclaje del nodo en el KG de TxGNN
2. **Re-ejecutar el pipeline TxGNN** — Una vez resuelto el DrugBank ID, volver a correr la predicción con el nodo correctamente mapeado
3. **Obtener MOA** — Consultar DrugBank para el mecanismo de acción (inhibición de DHP-I renal) y actualizar el campo `original_moa`
4. **Re-buscar autorizaciones ANMAT bajo la combinación** — Repetir la búsqueda con el término "imipenem cilastatín" para detectar licencias bajo nombre de combinación fija
5. **Descargar prospecto oficial** — Resolver DG001 extrayendo advertencias y contraindicaciones del PDF del prospecto autorizado
---

