---
layout: default
title: Adapaleno
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# Adapaleno
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

# ADAPALENO: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Adapaleno es un retinoide de tercera generación utilizado ampliamente a nivel mundial para el tratamiento del acné vulgar.
Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco,
y no se dispone de evidencia complementaria (ensayos clínicos ni literatura) en el contexto de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en el Evidence Pack (conocida: acné vulgar) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin estudios de reposicionamiento disponibles) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones Disponibles?

Adapaleno (nombre DCI: ADAPALENO) es un análogo sintético del ácido retinoico que actúa como agonista selectivo del receptor de ácido retinoico gamma (RAR-γ). Se utiliza internacionalmente como tratamiento tópico de primera línea para el acné vulgar leve a moderado, tanto en monoterapia como en combinación con peróxido de benzoílo.

Sin embargo, el Evidence Pack actual presenta múltiples brechas de datos que impiden la generación de predicciones de reposicionamiento:

1. **Ausencia de DrugBank ID**: No se pudo vincular el fármaco a la base de datos DrugBank (`drugbank_id: null`), lo que limita la integración con el grafo de conocimiento de TxGNN.
2. **Mecanismo de acción no disponible en el pack**: El campo `original_moa` figura como brecha de datos, lo cual impacta directamente la capacidad del modelo para inferir relaciones mecanísticas con nuevas enfermedades.
3. **Sin indicaciones originales registradas**: El arreglo `original_indications` está vacío, lo que impide al modelo establecer un punto de partida para la exploración de indicaciones análogas.

Es probable que la combinación de estos factores haya resultado en un arreglo vacío de `predicted_indications`, ya que el modelo TxGNN requiere datos mínimos de entrada para generar predicciones fiables.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con reposicionamiento registrados en el Evidence Pack.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con reposicionamiento disponible en el Evidence Pack.

---

## Información de Mercado en Argentina

Adapaleno **no se encuentra comercializado** en Argentina según los registros consultados. No se identificaron autorizaciones de ANMAT vigentes para este principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|------------------------|---------------------|---------------------|---------------------|
| — | — | — | Sin autorizaciones registradas |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Las siguientes brechas de datos fueron identificadas y requieren remediación antes de cualquier evaluación de seguridad:
>
> - **Advertencias y contraindicaciones del prospecto**: No disponibles. Fuente sugerida: sitio web de la autoridad regulatoria (ANMAT/TFDA), descarga y análisis de prospecto en PDF.
> - **Interacciones farmacológicas (DDI)**: Consulta realizada sin resultados (`not_found`).

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Remediación Sugerida |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias / Contraindicaciones del prospecto | **Bloqueante** | No es posible iniciar la evaluación de seguridad (S1) | Descargar y analizar prospecto PDF desde la autoridad regulatoria |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | **Alta** | Afecta el análisis de relación mecanística | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para ADAPALENO presenta brechas de datos críticas (severidad bloqueante) que impidieron la generación de predicciones por parte del modelo TxGNN. Sin un DrugBank ID vinculado, sin mecanismo de acción documentado y sin indicaciones originales registradas, no es posible evaluar el potencial de reposicionamiento de este fármaco en este momento. Además, el fármaco no está comercializado en Argentina, lo que limita la viabilidad regulatoria inmediata.

**Para avanzar se necesita:**
- Vincular ADAPALENO a su identificador DrugBank correspondiente (DB00210)
- Obtener y documentar el mecanismo de acción (agonista selectivo RAR-γ)
- Registrar las indicaciones originales aprobadas (acné vulgar)
- Descargar y analizar el prospecto para extraer advertencias, contraindicaciones y precauciones
- Re-ejecutar el modelo TxGNN una vez completadas las brechas de datos
- Evaluar la viabilidad regulatoria en Argentina, considerando que actualmente no existen autorizaciones vigentes
---

