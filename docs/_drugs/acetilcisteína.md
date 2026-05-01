---
layout: default
title: Acetilcisteína
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Acetilcisteína
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

# Acetilcisteína: Evaluación Preliminar — Sin Indicaciones Predichas

## Resumen en Una Frase

Acetilcisteína (N-acetilcisteína, NAC) es un agente mucolítico y antioxidante ampliamente utilizado a nivel mundial como expectorante en afecciones respiratorias y como antídoto en la intoxicación por paracetamol. En esta evaluación, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones**, y el fármaco **no cuenta con autorizaciones de comercialización registradas en Argentina** según los datos disponibles, lo que limita significativamente el análisis de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible (sin autorizaciones registradas en Argentina) |
| Nueva Indicación Predicha | — Sin predicciones generadas — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin evidencia disponible para evaluación) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué No se Generaron Predicciones?

Acetilcisteína (NAC) es un derivado acetilado del aminoácido L-cisteína, reconocido mundialmente por dos funciones terapéuticas principales: como **mucolítico** (reduce la viscosidad del moco bronquial al romper los puentes disulfuro de las glicoproteínas) y como **antídoto para la intoxicación por paracetamol** (restaura las reservas de glutatión hepático). Adicionalmente, se investiga su potencial antioxidante y citoprotector en diversas condiciones.

Sin embargo, el modelo TxGNN no generó predicciones de nuevas indicaciones para este fármaco. Esto puede deberse a varios factores: (1) la ausencia de un identificador DrugBank válido (`drugbank_id: null`) impide la correcta integración del fármaco en el grafo de conocimiento del modelo; (2) el nombre en español "ACETILCISTEÍNA" puede no coincidir con las entradas del grafo, que típicamente utilizan nomenclatura INN en inglés ("acetylcysteine"); y (3) la falta de datos de mecanismo de acción (MOA) en el Evidence Pack limita la capacidad del modelo para establecer relaciones fármaco-enfermedad.

Para que el modelo TxGNN pueda generar predicciones significativas, es necesario resolver primero las brechas de datos identificadas, particularmente la vinculación con DrugBank (DB06151 para acetilcisteína) y la carga completa del perfil farmacológico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack, dado que no se generaron predicciones de nuevas indicaciones.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack, dado que no se generaron predicciones de nuevas indicaciones.

---

## Información de Mercado en Argentina

No se encontraron autorizaciones de comercialización registradas para acetilcisteína en Argentina según los datos consultados. El estado de mercado figura como **"No comercializado"** con 0 autorizaciones.

> **Nota:** Acetilcisteína es un fármaco ampliamente comercializado a nivel mundial. La ausencia de registros puede deberse a diferencias en la nomenclatura de búsqueda (nombre en español vs. INN en inglés) o a limitaciones en la fuente de datos consultada. Se recomienda verificar manualmente en el registro de ANMAT utilizando variantes del nombre: "acetilcisteína", "N-acetilcisteína", "acetylcysteine".

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no están disponibles en el Evidence Pack actual.

> **Nota general (basada en conocimiento farmacológico establecido):** Acetilcisteína es generalmente bien tolerada. Las reacciones adversas más comunes incluyen náuseas, vómitos y diarrea por vía oral, y broncoespasmo por vía inhalatoria. En administración intravenosa (protocolo de intoxicación por paracetamol), pueden ocurrir reacciones anafilactoides. Está contraindicada en pacientes con hipersensibilidad conocida al principio activo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No es posible avanzar en la evaluación de reposicionamiento dado que el modelo TxGNN no generó predicciones de nuevas indicaciones y existen múltiples brechas de datos críticas (ausencia de DrugBank ID, MOA, información regulatoria y perfil de seguridad). El Evidence Pack se encuentra en estado incompleto.

**Para avanzar se necesita:**
- **Resolver la identificación del fármaco:** Vincular acetilcisteína con su DrugBank ID correcto (DB06151) y verificar la correspondencia en el grafo de conocimiento de TxGNN
- **Completar el perfil de MOA:** Obtener el mecanismo de acción detallado desde DrugBank API
- **Verificar el estado regulatorio en Argentina:** Consultar ANMAT directamente usando variantes del nombre del fármaco (acetilcisteína, N-acetilcisteína, NAC)
- **Obtener datos de seguridad:** Descargar y analizar el prospecto oficial (si existe registro en Argentina) o utilizar fuentes regulatorias alternativas (FDA, EMA)
- **Re-ejecutar el modelo TxGNN** una vez resueltas las brechas de datos para obtener predicciones válidas

---

*Este informe fue generado el 2026-04-03. Los resultados son exclusivamente para fines de investigación y no constituyen consejo médico. Cualquier candidato a reposicionamiento requiere validación clínica antes de su aplicación.*
---

