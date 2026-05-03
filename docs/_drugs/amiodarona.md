---
layout: default
title: Amiodarona
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 0
---

# Amiodarona
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

# Amiodarona: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Amiodarona es un antiarrítmico de clase III ampliamente utilizado para el tratamiento de arritmias ventriculares y supraventriculares graves, incluyendo fibrilación auricular y taquicardia ventricular. El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el presente análisis. La evaluación se encuentra en estado preliminar debido a múltiples brechas de datos críticas identificadas en el Evidence Pack.

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en el Evidence Pack (conocida: arritmias ventriculares y supraventriculares graves) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin estudios asociados a una nueva indicación) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

## ¿Por qué no hay Predicciones Disponibles?

El Evidence Pack actual para Amiodarona presenta brechas de datos significativas que impiden al modelo TxGNN generar predicciones confiables. No se dispone del identificador de DrugBank (`drugbank_id: null`), lo cual limita la integración del fármaco en el grafo de conocimiento utilizado por TxGNN para inferir nuevas relaciones fármaco-enfermedad. Asimismo, el mecanismo de acción (MOA) no fue capturado en esta iteración del análisis.

Desde el punto de vista farmacológico, Amiodarona es un antiarrítmico con un perfil mecanístico excepcionalmente amplio: bloquea canales de potasio (clase III de Vaughan-Williams), pero también exhibe actividad sobre canales de sodio (clase I), canales de calcio (clase IV) y receptores beta-adrenérgicos (clase II). Esta polivalencia mecanística la convierte, en principio, en una candidata interesante para reposicionamiento, particularmente en áreas como cardioprotección, enfermedades tiroideas (por su contenido de yodo) o incluso actividad antimicrobiana, áreas que han sido exploradas en la literatura.

Para que el modelo pueda generar predicciones, es necesario completar la integración del fármaco en el knowledge graph, incluyendo su DrugBank ID, sus targets moleculares y su MOA detallado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con una nueva indicación registrados, dado que no se generaron predicciones de reposicionamiento.

## Evidencia de Literatura

Actualmente no hay literatura relacionada con una nueva indicación disponible en el Evidence Pack, dado que no se generaron predicciones de reposicionamiento.

## Información de Mercado en Argentina

Amiodarona **no se encuentra comercializada** en Argentina según los registros consultados. No se identificaron autorizaciones de comercialización vigentes (0 licencias).

> **Nota:** Esto puede deberse a que el fármaco se comercializa bajo un nombre diferente, en combinaciones no indexadas, o a una limitación en la consulta regulatoria. Se recomienda verificar directamente con la autoridad regulatoria local (ANMAT).

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el Evidence Pack actual. Sin embargo, Amiodarona es un fármaco con un perfil de seguridad bien documentado a nivel internacional que requiere vigilancia estrecha:

> Consultar el prospecto para información de seguridad completa. Se recomienda especial atención a los riesgos conocidos de Amiodarona, que incluyen toxicidad pulmonar, hepatotoxicidad, disfunción tiroidea (tanto hipo como hipertiroidismo), neuropatía periférica, depósitos corneales y fotosensibilidad. El monitoreo periódico de función tiroidea, hepática y pulmonar es esencial durante el tratamiento.

## Brechas de Datos Identificadas

El Evidence Pack documenta las siguientes brechas críticas que deben resolverse antes de avanzar:

| ID | Categoría | Item Faltante | Severidad | Impacto | Remediación |
|----|-----------|---------------|-----------|---------|-------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede realizar la evaluación de seguridad inicial (S1) | Descargar y analizar prospecto desde el sitio regulatorio |
| DG002 | Nivel de Fármaco | Mecanismo de acción (MOA) | Alta | Afecta el análisis de correlación mecanística | Consultar API de DrugBank |

**Datos adicionales ausentes:**
- DrugBank ID no vinculado (`null`)
- Indicaciones originales no registradas en el pack (array vacío)
- Sin predicciones de TxGNN generadas
- Sin datos de interacciones farmacológicas

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Amiodarona se encuentra en un estado incompleto que impide la generación de predicciones de reposicionamiento y la evaluación de seguridad. La brecha DG001 es de severidad bloqueante. No es posible avanzar en el análisis sin completar los datos fundamentales del fármaco.

**Para avanzar se necesita:**
- Vincular el DrugBank ID correspondiente (DB01118) e integrar el fármaco en el knowledge graph de TxGNN
- Obtener y analizar el prospecto regulatorio para completar advertencias, contraindicaciones e indicaciones aprobadas
- Registrar el mecanismo de acción detallado (bloqueo multicanal: K⁺, Na⁺, Ca²⁺, β-adrenérgico)
- Re-ejecutar el modelo TxGNN una vez completada la integración de datos
- Verificar el estado regulatorio con ANMAT mediante consulta directa, dado que Amiodarona es un fármaco ampliamente utilizado a nivel mundial y su ausencia en los registros puede ser un artefacto de búsqueda
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

