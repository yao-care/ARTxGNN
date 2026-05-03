---
layout: default
title: Ciclobenzaprina
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 0
---

# Ciclobenzaprina
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

# Ciclobenzaprina: Evaluación de Reposicionamiento — Datos Insuficientes para Análisis Completo

---

## Resumen en Una Frase

Ciclobenzaprina es un relajante muscular de acción central conocido en la literatura por el tratamiento de espasmos musculoesqueléticos agudos. El presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, y los datos de indicación original e información de seguridad estructurada están ausentes, por lo que no es posible completar el análisis de reposicionamiento en esta instancia. Se requiere resolver las brechas de datos identificadas antes de continuar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este Evidence Pack |
| Nueva Indicación Predicha | No disponible — sin predicciones TxGNN |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin estudios reales vinculados) |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No es Posible Completar esta Evaluación

El Evidence Pack presenta tres brechas críticas que bloquean el análisis de reposicionamiento:

**1. Sin predicciones TxGNN:** El campo `predicted_indications` está vacío. Esto indica que el pipeline no generó candidatos de reposicionamiento para Ciclobenzaprina, ya sea por falta de nodo en el grafo de conocimiento, por error en el paso de mapeo, o porque los datos no fueron integrados antes de generar este pack.

**2. Sin mecanismo de acción estructurado (DG002 — severidad Alta):** El MOA figura como `[Data Gap]`. Aunque Ciclobenzaprina es conocida farmacológicamente como un compuesto tricíclico que actúa sobre el tronco cerebral inhibiendo la actividad eferente motora, estos datos no están cargados en el sistema y por lo tanto no pueden ser utilizados para el análisis de plausibilidad mecanística.

**3. Sin advertencias ni contraindicaciones (DG001 — severidad Bloqueante):** Los datos de seguridad (advertencias clave y contraindicaciones) figuran como `[Data Gap]`. Cabe destacar que el `query_log` registra un resultado exitoso en la consulta a `tfda_package_insert` (`result_count: 1`) y a DrugBank (`result_count: 1`), lo que sugiere que los datos **existen** en la fuente pero **no fueron integrados** correctamente en el pack.

---

## Información de Mercado en Argentina

No se encontraron registros de autorización para Ciclobenzaprina en la base de datos consultada. El fármaco figura como **no comercializado**, con **0 autorizaciones** vigentes.

> **Nota:** Vale la pena verificar si Ciclobenzaprina se comercializa bajo nombres alternativos o como parte de combinaciones a dosis fijas, dado que en algunos mercados se presenta combinada con antiinflamatorios (ej. diclofenac + ciclobenzaprina).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack carece de predicciones TxGNN y de los datos mínimos requeridos para evaluar la plausibilidad mecanística y la seguridad del candidato. No es posible emitir una recomendación de reposicionamiento en este estado.

**Para avanzar se necesita:**
- **[Bloqueante]** Integrar los datos del prospecto oficial ya recuperados (la consulta `tfda_package_insert` devolvió 1 resultado — revisar por qué no se volcó en `safety`)
- **[Bloqueante]** Integrar los datos de DrugBank ya recuperados (la consulta devolvió 1 resultado — revisar extracción de MOA y categorías)
- **[Crítico]** Ejecutar o revisar el pipeline TxGNN para generar predicciones de indicación para Ciclobenzaprina — confirmar que el nodo del fármaco existe en el grafo de conocimiento
- **[Opcional]** Verificar registros bajo nombres alternativos o combinaciones en ANMAT para determinar el estado real de mercado en Argentina
- Recargar el Evidence Pack con los datos completos y regenerar este informe
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

