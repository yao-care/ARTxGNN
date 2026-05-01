---
layout: default
title: Betahistina
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
---

# Betahistina
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

# Betahistina: Evaluación Preliminar — Sin Indicación Predicha Disponible

---

## Resumen en Una Frase

Betahistina es un fármaco histaminérgico ampliamente utilizado a nivel mundial para el tratamiento del vértigo y la enfermedad de Ménière.
En esta evaluación, el modelo TxGNN **no generó predicciones de nuevas indicaciones** para este compuesto,
y **no se identificaron autorizaciones de comercialización vigentes en Argentina**.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Vértigo / Enfermedad de Ménière (uso reconocido internacionalmente; sin registro local identificado) |
| Nueva Indicación Predicha | — No disponible (sin predicción TxGNN) |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | N/A |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se generó una predicción?

Betahistina (INN: betahistine) es un análogo estructural de la histamina que actúa como **agonista parcial del receptor H1** y **antagonista del receptor H3** de histamina. Se utiliza ampliamente en Europa, Asia y Latinoamérica para el manejo del vértigo asociado a la enfermedad de Ménière, mejorando la microcirculación del oído interno y modulando la liberación de histamina en el sistema vestibular.

En el presente análisis, el modelo TxGNN no generó predicciones de reposicionamiento para betahistina. Esto puede deberse a varias razones:
1. **Ausencia del compuesto en el grafo de conocimiento (KG):** Si betahistina no está representada en el grafo de conocimiento biomédico utilizado por TxGNN, el modelo no puede generar predicciones de enlace fármaco-enfermedad.
2. **Falta de identificador DrugBank:** El Evidence Pack no contiene un `drugbank_id` válido, lo que dificulta la integración del fármaco en los pipelines de predicción basados en ontologías estándar.
3. **Perfil farmacológico de nicho:** Betahistina tiene un mecanismo de acción relativamente específico (modulación histaminérgica vestibular), lo que puede limitar la cantidad de conexiones en el grafo.

Para futuros análisis, se recomienda verificar la presencia de betahistina en el KG de TxGNN y, en caso negativo, evaluar la posibilidad de enriquecer el grafo con este compuesto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados, dado que no se generó una predicción de reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible para evaluar, dado que no se generó una predicción de reposicionamiento.

---

## Información de Mercado en Argentina

No se identificaron autorizaciones de comercialización vigentes para betahistina en Argentina (0 registros encontrados en la consulta regulatoria).

> **Nota:** Betahistina está ampliamente comercializada en otros países de la región bajo marcas como Serc® y genéricos. La ausencia de registro local podría representar tanto una barrera como una oportunidad regulatoria dependiendo de la estrategia de desarrollo.

---

## Consideraciones de Seguridad

No se dispone de información de seguridad local (advertencias, contraindicaciones ni interacciones farmacológicas) debido a la ausencia de registro regulatorio en Argentina.

> Consultar el prospecto de referencia internacional (por ejemplo, la ficha técnica de la EMA o el prospecto aprobado en el país de origen) para información completa de seguridad.

**Información de seguridad de referencia general (fuentes internacionales):**
- Betahistina está contraindicada en pacientes con feocromocitoma.
- Debe usarse con precaución en pacientes con asma bronquial o úlcera péptica activa.
- No se han reportado interacciones farmacológicas clínicamente significativas de alta frecuencia, aunque los antihistamínicos H1 podrían teóricamente reducir su eficacia.

---

## Brechas de Datos Identificadas

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente Sugerida |
|----|-----------|---------------|-----------|---------|-----------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto local | **Bloqueante** | No se puede realizar evaluación de seguridad S1 | Autoridad regulatoria local |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) detallado | Alta | Afecta el análisis de correlación mecanística | DrugBank API |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Betahistina no cuenta con predicciones de nuevas indicaciones generadas por TxGNN, no posee registro regulatorio vigente en Argentina y presenta brechas de datos críticas (incluyendo la ausencia de DrugBank ID y datos de seguridad locales). No hay base suficiente para avanzar con una evaluación de reposicionamiento en este momento.

**Para avanzar se necesita:**
- Verificar e incorporar betahistina en el grafo de conocimiento de TxGNN (confirmar presencia del nodo o enriquecer el KG)
- Obtener el identificador DrugBank válido (probable: [DB06698](https://go.drugbank.com/drugs/DB06698)) y vincular los datos farmacológicos
- Obtener datos de MOA estructurados desde DrugBank para alimentar el modelo de predicción
- Evaluar el estado regulatorio en detalle: si existe interés en el mercado argentino, considerar la vía de registro como producto importado
- Re-ejecutar el pipeline TxGNN una vez resueltas las brechas de datos anteriores
---

