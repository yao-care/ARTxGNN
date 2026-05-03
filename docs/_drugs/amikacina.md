---
layout: default
title: Amikacina
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 0
---

# Amikacina
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

# Amikacina: Evaluación de Reposicionamiento — Sin Indicaciones Predichas

## Resumen en Una Frase

Amikacina es un antibiótico aminoglucósido utilizado ampliamente para el tratamiento de infecciones bacterianas graves causadas por microorganismos gramnegativos. El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el presente ciclo de análisis, y no se dispone de datos regulatorios ni de seguridad suficientes para realizar una evaluación completa.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (conocida: infecciones graves por gramnegativos) |
| Nueva Indicación Predicha | — Sin predicciones generadas por TxGNN — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos de entrada, sin predicción ni estudios asociados) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generaron Predicciones?

Amikacina (nombre DCI: AMIKACINA) es un antibiótico aminoglucósido de amplio uso clínico para infecciones graves causadas por bacterias gramnegativas, incluyendo *Pseudomonas aeruginosa*, *Escherichia coli*, *Klebsiella* spp., entre otras. Su mecanismo de acción consiste en la unión irreversible a la subunidad ribosomal 30S bacteriana, inhibiendo la síntesis de proteínas y provocando la muerte celular bacteriana.

El modelo TxGNN no generó indicaciones predichas (`predicted_indications` vacío) para este fármaco. Esto puede deberse a varias razones:

1. **Ausencia en el grafo de conocimiento (KG):** Si amikacina no se encuentra representada en la red de conocimiento terapéutico utilizada por TxGNN, el modelo no puede generar predicciones de reposicionamiento.
2. **Perfil farmacológico limitado en la base de datos:** El DrugBank ID no fue identificado (`null`), lo que sugiere que la consulta no logró vincular el nombre "AMIKACINA" con su entrada correspondiente en DrugBank, posiblemente por diferencias en la nomenclatura (español vs. inglés: amikacin).
3. **Falta de datos regulatorios locales:** Con 0 autorizaciones y estado "No comercializado" en Argentina, el pipeline de datos no pudo extraer información de prospectos ni indicaciones aprobadas localmente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados, dado que no se generaron predicciones de reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible, dado que no se generaron predicciones de reposicionamiento.

---

## Información de Mercado en Argentina

Amikacina **no se encuentra comercializada** en Argentina según los datos regulatorios consultados. No se identificaron autorizaciones de comercialización vigentes.

> **Nota:** Amikacina es un antibiótico ampliamente disponible a nivel mundial. La ausencia de registros puede deberse a que se comercializa bajo nombres o sales diferentes (por ejemplo, amikacina sulfato) que no fueron capturados por la consulta realizada con el término "AMIKACINA".

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el Evidence Pack actual. A partir del conocimiento general sobre amikacina:

- **Advertencias Principales:** Nefrotoxicidad y ototoxicidad (efectos adversos clase aminoglucósido). Requiere monitoreo de niveles séricos, función renal y función auditiva.
- **Contraindicaciones:** Hipersensibilidad conocida a amikacina u otros aminoglucósidos.
- **Interacciones Farmacológicas:** Potenciación de nefrotoxicidad con otros agentes nefrotóxicos (vancomicina, anfotericina B, cisplatino). Potenciación de bloqueo neuromuscular con relajantes musculares.

> ⚠️ Esta información es de referencia general. Consultar el prospecto oficial para información de seguridad completa y actualizada.

---

## Brechas de Datos Identificadas

El Evidence Pack identifica las siguientes brechas críticas:

| ID | Categoría | Item Faltante | Severidad | Impacto | Remediación Sugerida |
|----|-----------|---------------|-----------|---------|---------------------|
| DG001 | Nivel de Fármaco | Advertencias/Contraindicaciones del prospecto | **Bloqueante** | No se puede iniciar la evaluación de seguridad S1 | Descargar y analizar prospecto PDF desde el sitio regulatorio |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | Alta | Afecta el análisis de relación mecanística | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se generaron predicciones de reposicionamiento para amikacina. El Evidence Pack presenta brechas de datos críticas (severidad "Bloqueante") que impiden una evaluación significativa. Además, el fármaco no se encuentra registrado en Argentina bajo el nombre consultado, lo que limita la aplicabilidad regulatoria local.

**Para avanzar se necesita:**
- Verificar la nomenclatura de búsqueda: repetir consultas usando "amikacin" (inglés), "amikacin sulfate" y variantes de sal para vincular correctamente con DrugBank y bases regulatorias
- Obtener el DrugBank ID correspondiente (probablemente **DB00479**) para alimentar correctamente el modelo TxGNN
- Confirmar si amikacina está representada en el grafo de conocimiento (KG) de TxGNN; de no estarlo, evaluar su incorporación
- Resolver la brecha DG001 (prospecto regulatorio) antes de cualquier evaluación de seguridad
- Re-ejecutar el pipeline de predicción TxGNN una vez resueltas las brechas de datos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

