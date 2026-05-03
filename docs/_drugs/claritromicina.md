---
layout: default
title: Claritromicina
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 0
---

# Claritromicina
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

# Claritromicina: Evaluación de Reposicionamiento — Datos Insuficientes para Predicción

## Resumen en Una Frase

Claritromicina (CLARITROMICINA) es un antibiótico macrólido ampliamente conocido por su uso en infecciones bacterianas y erradicación de *H. pylori*.
El modelo TxGNN **no generó predicciones de nuevas indicaciones** para este fármaco en el presente Evidence Pack,
por lo que no es posible evaluar oportunidades de reposicionamiento con la información actualmente disponible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos registrados en el Evidence Pack |
| Nueva Indicación Predicha | — (sin predicciones TxGNN) |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 — solo predicción del modelo, sin estudios reales |
| Estado de Mercado en Argentina | ✗ No comercializado (0 autorizaciones registradas) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No es Posible Evaluar la Predicción

El Evidence Pack recibido presenta dos limitaciones estructurales que impiden continuar la evaluación estándar:

1. **Sin indicaciones predichas**: el campo `predicted_indications` está vacío. El modelo TxGNN no devolvió ninguna candidatura de reposicionamiento para CLARITROMICINA en esta versión del pipeline (v4, corte 2026-04-19).

2. **Mecanismo de acción no disponible**: el campo `original_moa` figura como `[Data Gap]`. Sin conocer el MOA registrado en DrugBank, no es posible fundamentar la plausibilidad mecanística de ninguna indicación nueva, aunque se generara una predicción.

> A título informativo, Claritromicina es un antibiótico macrólido que inhibe la síntesis proteica bacteriana al unirse a la subunidad 50S del ribosoma. Ha sido explorada en investigación por sus propiedades antiinflamatorias e inmunomoduladoras, pero esta información proviene de conocimiento general y **no está respaldada por los datos del Evidence Pack actual**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en este Evidence Pack.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en este Evidence Pack.

---

## Información de Mercado en Argentina

No se registran autorizaciones de comercialización para CLARITROMICINA en la base de datos consultada (0 licencias, estado: no comercializado).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene predicciones de TxGNN ni datos de seguridad o mecanismo de acción, lo que hace imposible emitir una recomendación de avance con base en evidencia. El fármaco tampoco está autorizado en el mercado argentino según los datos disponibles.

**Para avanzar se necesita:**

- **[Bloqueante]** Obtener el MOA desde DrugBank (DG002 — severidad Alta): necesario para el análisis de plausibilidad mecanística.
- **[Bloqueante]** Obtener advertencias y contraindicaciones del prospecto oficial (DG001 — severidad Bloqueante): requisito para la evaluación de seguridad S1.
- **Regen de predicciones TxGNN**: verificar por qué `predicted_indications` resultó vacío — puede ser un problema de mapeo del nombre INN (CLARITROMICINA vs. Clarithromycin en inglés) o ausencia del nodo en el grafo de conocimiento.
- **Verificar cobertura de mercado**: confirmar si existen registros ANMAT bajo nombres alternativos (ej. Biaxin, Klaricid u otros nombres de marca).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

