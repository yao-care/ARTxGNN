---
layout: default
title: Bicalutamida
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 0
---

# Bicalutamida
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

# Bicalutamida: Evaluación Preliminar — Sin Nuevas Indicaciones Predichas

---

## Resumen en Una Frase

Bicalutamida es un antiandrógeno no esteroideo utilizado clásicamente en el tratamiento del cáncer de próstata.
El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el ciclo de análisis actual.
Los datos disponibles en el Evidence Pack son insuficientes para realizar una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Cáncer de próstata (conocimiento farmacológico general; no registrada en el Evidence Pack) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo información de referencia, sin estudios vinculados) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones Disponibles?

Bicalutamida (INN: bicalutamide) es un antiandrógeno no esteroideo que actúa bloqueando competitivamente los receptores de andrógenos, impidiendo la acción de la testosterona y la dihidrotestosterona sobre las células tumorales prostáticas. Es ampliamente utilizado a nivel mundial como componente del tratamiento del cáncer de próstata, tanto en monoterapia como en combinación con agonistas de GnRH.

Sin embargo, el Evidence Pack actual presenta múltiples brechas de datos críticas que impidieron la ejecución completa del pipeline de predicción:

1. **Sin identificador DrugBank** (`drugbank_id: null`): La ausencia de un ID de DrugBank impide vincular el fármaco al grafo de conocimiento (Knowledge Graph) utilizado por TxGNN, lo cual es un prerrequisito para la generación de predicciones.
2. **Sin mecanismo de acción registrado** (`original_moa: [Data Gap]`): Aunque el MOA de bicalutamida es bien conocido en la literatura (antagonista del receptor de andrógenos), esta información no fue incorporada al pack de evidencia, limitando el análisis de plausibilidad mecanística.
3. **Sin autorizaciones regulatorias en Argentina** (`total_licenses: 0`): El fármaco no tiene registros ante la autoridad regulatoria argentina (ANMAT), lo que indica que no está comercializado en el país.

En consecuencia, el arreglo `predicted_indications` se encuentra vacío y no es posible evaluar ningún candidato de reposicionamiento en este momento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack.

> **Nota:** Dado que no se generaron predicciones de nuevas indicaciones, no se realizó búsqueda de ensayos clínicos para indicaciones alternativas.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack.

> **Nota:** La ausencia de literatura en el pack no implica inexistencia de publicaciones sobre bicalutamida; refleja que no se ejecutó la etapa de recopilación de evidencia al no haber indicaciones predichas.

---

## Información de Mercado en Argentina

Bicalutamida **no se encuentra comercializada** en Argentina. No se identificaron autorizaciones de comercialización vigentes ante ANMAT.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|---------------------|---------------------|---------------------|
| — | — | — | — |

> No se encontraron registros sanitarios para este principio activo en Argentina.

---

## Citotoxicidad

Bicalutamida es un fármaco antineoplásico (antiandrogénico), por lo que esta sección es aplicable.

| Item | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Terapia dirigida (antagonista del receptor de andrógenos, no citotóxico convencional) |
| Riesgo de Mielosupresión | Bajo (bicalutamida no causa mielosupresión significativa como agente único) |
| Clasificación de Emetogenicidad | Baja (riesgo emético mínimo) |
| Ítems de Monitoreo | Función hepática (transaminasas — riesgo de hepatotoxicidad), PSA, hemograma periódico |
| Protección en Manejo | Precauciones estándar para manipulación de antineoplásicos orales; evitar exposición en mujeres embarazadas |

> **Nota:** La información anterior se basa en el perfil farmacológico conocido de bicalutamida. Consultar el prospecto del producto específico para información detallada.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el Evidence Pack actual (advertencias, contraindicaciones e interacciones farmacológicas figuran como brechas de datos).

> Consultar el prospecto para información de seguridad. Se recomienda obtener el prospecto aprobado por la autoridad regulatoria del país de origen para completar esta sección.

**Brechas de datos identificadas:**

| ID | Categoría | Ítem Faltante | Severidad | Remediación Sugerida |
|----|-----------|---------------|-----------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | Descargar y analizar prospecto desde la autoridad regulatoria |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de bicalutamida presenta brechas de datos críticas que impidieron la ejecución del modelo TxGNN. No se generaron predicciones de nuevas indicaciones, no existe registro regulatorio en Argentina, y faltan datos fundamentales de seguridad y mecanismo de acción. No es posible avanzar con la evaluación de reposicionamiento en estas condiciones.

**Para avanzar se necesita:**
- Obtener y vincular el **DrugBank ID** correspondiente (DB00fármaco) al pack de evidencia para habilitar el grafo de conocimiento de TxGNN
- Completar el campo de **mecanismo de acción (MOA)** con datos de DrugBank o literatura de referencia
- Descargar y analizar el **prospecto oficial** (desde EMA, FDA u otra autoridad regulatoria relevante) para extraer advertencias, contraindicaciones e interacciones
- Verificar el **estado regulatorio actualizado** en Argentina (consulta directa a ANMAT)
- **Re-ejecutar el pipeline TxGNN** una vez resueltas las brechas de datos anteriores para generar predicciones de nuevas indicaciones

---

*Este informe fue generado el 2026-04-03. Los resultados son exclusivamente para fines de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
---

