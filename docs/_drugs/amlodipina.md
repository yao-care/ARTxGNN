---
layout: default
title: Amlodipina
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 0
---

# Amlodipina
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

# Amlodipina: Evaluación Preliminar — Datos Insuficientes para Reposicionamiento

---

## Resumen en Una Frase

Amlodipina es un bloqueante de los canales de calcio dihidropiridínico ampliamente utilizado a nivel mundial para el tratamiento de la hipertensión arterial y la angina de pecho. Sin embargo, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el presente análisis, y el Evidence Pack presenta **múltiples brechas de datos críticas** que impiden una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en el Evidence Pack (conocida: hipertensión arterial, angina de pecho) |
| Nueva Indicación Predicha | — Sin predicción disponible — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos de referencia, sin predicción ni estudios asociados) |
| Estado de Mercado en Argentina | No comercializado (según registros consultados) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicción de Reposicionamiento?

Amlodipina (DCI: amlodipina) es un bloqueante de los canales de calcio de tipo L, perteneciente al grupo de las dihidropiridinas. Su mecanismo de acción consiste en inhibir el flujo transmembrana de iones de calcio hacia el músculo liso vascular y el músculo cardíaco, produciendo vasodilatación periférica y coronaria. Es uno de los antihipertensivos más prescritos a nivel mundial, con indicaciones establecidas en hipertensión arterial y angina de pecho (tanto estable crónica como vasoespástica).

El modelo TxGNN no generó predicciones de nuevas indicaciones para amlodipina en esta corrida de análisis. Esto puede deberse a varios factores: (1) el fármaco no fue incluido en el grafo de conocimiento utilizado por TxGNN bajo el nombre "AMLODIPINA", (2) el identificador DrugBank no fue resuelto (`drugbank_id: null`), lo que impide el mapeo correcto al nodo del fármaco en la red, o (3) las indicaciones existentes de amlodipina ya cubren ampliamente los dominios terapéuticos donde el modelo encontraría asociaciones relevantes.

Es importante señalar que la ausencia de predicción **no implica ausencia de potencial de reposicionamiento**. Existe literatura emergente que explora el uso de amlodipina en contextos como enfermedad de Raynaud, migraña profiláctica y protección renal en pacientes diabéticos. Sin embargo, estas asociaciones no fueron capturadas en el presente análisis debido a las brechas de datos identificadas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados en este Evidence Pack, dado que no se generó una predicción de reposicionamiento por parte de TxGNN.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible en este Evidence Pack.

---

## Información de Mercado en Argentina

No se encontraron autorizaciones de comercialización registradas para amlodipina en la base de datos consultada (ANMAT). Se registraron **0 licencias**.

> **Nota:** Amlodipina es un fármaco ampliamente comercializado a nivel mundial bajo múltiples marcas (Norvasc®, Amloc®, entre otras). La ausencia de registros puede deberse a una búsqueda bajo el nombre "AMLODIPINA" que no coincidió con las denominaciones registradas en la base de datos local, o a que los registros corresponden a combinaciones fijas (por ejemplo, amlodipina/valsartán) que no fueron capturadas bajo esta búsqueda individual.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el presente Evidence Pack. Consultar el prospecto aprobado para información completa de seguridad.

> **Información de referencia conocida sobre amlodipina:**
> - **Advertencias principales:** Puede causar hipotensión sintomática, especialmente en pacientes con estenosis aórtica severa. Puede exacerbar la angina o causar infarto de miocardio al inicio del tratamiento o al aumentar la dosis.
> - **Contraindicaciones conocidas:** Hipersensibilidad a amlodipina o a otras dihidropiridinas.
> - **Interacciones relevantes:** Potenciación del efecto hipotensor con otros antihipertensivos; interacción con inhibidores de CYP3A4 (puede aumentar niveles plasmáticos); precaución con simvastatina (limitar dosis a 20 mg/día).
>
> *Esta información es de referencia general y no proviene del Evidence Pack. Debe verificarse con el prospecto oficial.*

---

## Brechas de Datos Identificadas

| ID | Categoría | Item Faltante | Severidad | Impacto | Remediación Sugerida |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede realizar la evaluación inicial de seguridad (S1) | Descargar y analizar el prospecto PDF desde el sitio oficial de ANMAT |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de correlación mecanística | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para amlodipina presenta brechas de datos críticas: no se resolvió el identificador DrugBank, no se registraron indicaciones originales, y el modelo TxGNN no generó predicciones de nuevas indicaciones. Sin una predicción de reposicionamiento, no existe una hipótesis evaluable en este momento.

**Para avanzar se necesita:**
- Resolver el `drugbank_id` de amlodipina (probable: [DB00381](https://go.drugbank.com/drugs/DB00381)) y re-ejecutar el pipeline TxGNN con el mapeo correcto
- Verificar que el nombre "AMLODIPINA" (DCI en español) esté correctamente mapeado en el grafo de conocimiento de TxGNN; considerar usar "amlodipine" (INN en inglés)
- Obtener y parsear el prospecto oficial de ANMAT para completar datos de seguridad (DG001)
- Consultar DrugBank API para obtener el mecanismo de acción detallado (DG002)
- Verificar registros de comercialización en Argentina bajo nombres alternativos y combinaciones fijas
- Una vez resueltas las brechas, re-generar el Evidence Pack y evaluar nuevamente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

