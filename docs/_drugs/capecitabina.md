---
noindex: true
sitemap: false
layout: default
title: Capecitabina
parent: Solo Predicción del Modelo (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
---

# Capecitabina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## CAPECITABINA: Evaluación de Reposicionamiento Incompleta — Datos Insuficientes
{: .text-alpha }

## Resumen en Una Frase

CAPECITABINA es un fármaco cuya indicación original no pudo ser recuperada de las fuentes consultadas en este ciclo de recolección.
El modelo TxGNN **no generó predicciones de nuevas indicaciones** para este compuesto, posiblemente debido a la ausencia de datos regulatorios locales cargados en el pipeline.
En consecuencia, **no es posible completar la evaluación de reposicionamiento en este momento**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible |
| Nueva Indicación Predicha | No disponible |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 (sin estudios reales evaluados) |
| Estado de Mercado en Argentina | No comercializado (sin registro) |
| Número de productos en el listado PAMI | 0 (vigentes: 0) |
| Decisión Recomendada | **Hold** |

---

## Por qué la Evaluación Está Incompleta

Las consultas realizadas al 2026-03-29 no retornaron información suficiente para alimentar el pipeline de evaluación:

**Fuentes consultadas y resultados:**

| Fuente | Estado | Resultados | Impacto |
|--------|--------|------------|---------|
| DrugBank | Exitoso | 1 registro encontrado | Datos no integrados al Evidence Pack |
| Base DDI | No encontrado | 0 | Sin datos de interacciones |

> Esto sugiere un problema en la etapa de extracción/integración del pipeline, no una ausencia real de información del fármaco.

<!-- review:begin ar-lic-20261106-capecitabina-1 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «> **Nota importante:** El log de consultas muestra que DrugBank y el prospecto TFDA **sí retornaron resultados**, pero sus datos no fueron capturados en el Evidence Pack actual. Esto sugiere un problema en la etapa de extracción/integración del pipeline, no una ausencia real de información del fármaco.» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-capecitabina-1 -->

Dado que `predicted_indications` está vacío y los datos base del fármaco (indicación original, MOA, advertencias) no están disponibles, el modelo TxGNN no pudo generar candidatos de reposicionamiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La ausencia de datos de indicación original, mecanismo de acción y predicciones TxGNN impide realizar cualquier análisis de reposicionamiento fundamentado.

<!-- review:begin ar-lic-20261106-capecitabina-2 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «La ausencia de datos de indicación original, mecanismo de acción y predicciones TxGNN impide realizar cualquier análisis de reposicionamiento fundamentado. Los datos técnicamente existen en las fuentes (DrugBank y prospecto TFDA devolvieron resultados), pero no fueron integrados correctamente al Evidence Pack.» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-capecitabina-2 -->

**Para avanzar se necesita:**
- Revisar y corregir el paso de extracción del pipeline para DrugBank (1 resultado encontrado, no capturado): recuperar categorías, MOA, indicaciones originales y datos de toxicidad
- Verificar si CAPECITABINA cuenta con registro en ANMAT bajo ese INN u otros nombres comerciales (ej. Xeloda)
- Re-ejecutar el pipeline TxGNN una vez integrados los datos del fármaco para obtener predicciones de nuevas indicaciones
- Completar la búsqueda DDI con el INN correcto o sinónimos farmacológicos

<!-- review:begin ar-lic-20261106-capecitabina-3 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «Revisar y corregir el paso de extracción del pipeline para DrugBank (1 resultado encontrado, no capturado): recuperar categorías, MOA, indicaciones originales y datos de toxicidad / Extraer advertencias, contraindicaciones y clasificación de seguridad del prospecto TFDA (1 documento encontrado, no capturado)» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-capecitabina-3 -->

<!-- review:begin ar-lic-20261106-capecitabina-4 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «Xeloda), ya que la búsqueda TFDA retornó 0 resultados» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-capecitabina-4 -->

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «**Nota importante:** El log de consultas muestra que DrugBank y el prospecto TFDA **sí retornaron resultados**, pero sus datos no fueron cap» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «Los datos técnicamente existen en las fuentes (DrugBank y prospecto TFDA devolvieron resultados), pero no fueron integrados correctamente al» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «Extraer advertencias, contraindicaciones y clasificación de seguridad del prospecto TFDA (1 documento encontrado, no capturado)» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «ya que la búsqueda TFDA retornó 0 resultados» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

