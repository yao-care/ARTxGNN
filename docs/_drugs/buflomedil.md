---
layout: default
title: Buflomedil
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Buflomedil
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

# Buflomedil: Evaluación de Reposicionamiento — Sin Predicciones TxGNN Disponibles

## Resumen en Una Frase

Buflomedil es un agente vasoactivo históricamente utilizado para el tratamiento de la enfermedad arterial periférica y trastornos de la circulación. El modelo TxGNN **no generó indicaciones predichas** para este compuesto en el ciclo de análisis actual, posiblemente debido a cobertura insuficiente en el grafo de conocimiento. Con **0 ensayos clínicos** y **0 publicaciones** vinculadas a nuevas indicaciones, no es posible avanzar en la evaluación de reposicionamiento en este momento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad arterial periférica / insuficiencia vascular periférica (uso histórico; no registrado en el pack) |
| Nueva Indicación Predicha | Sin predicción disponible |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin estudios reales; predicción no generada) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué los Datos son Insuficientes para el Análisis

El Evidence Pack presenta tres brechas críticas que impiden completar la evaluación estándar:

1. **Sin predicciones TxGNN**: El campo `predicted_indications` está vacío. Esto puede indicar que Buflomedil no tiene cobertura suficiente en el grafo de conocimiento de TxGNN, que el DrugBank ID (DB13510) no fue mapeado correctamente a nodos del modelo, o que el perfil farmacológico del compuesto no alcanzó el umbral de puntuación mínimo para ninguna indicación candidata.

2. **Mecanismo de acción desconocido**: El MOA figura como dato faltante. Buflomedil es conocido en la literatura como un vasodilatador con posible actividad antagonista adrenérgica alfa, pero esta información no fue confirmada por DrugBank en el ciclo de consulta del 29 de marzo de 2026. Sin MOA verificado, el análisis de trasladabilidad mecanística a nuevas indicaciones no puede realizarse.

3. **Sin datos de seguridad regulatoria**: Las advertencias clave y contraindicaciones de la ficha técnica (TFDA/ANMAT) están ausentes. Cabe señalar que Buflomedil fue retirado del mercado en varios países (incluyendo Francia en 2011) debido a riesgo de convulsiones y efectos neurológicos graves en sobredosis o insuficiencia renal, lo que hace especialmente crítica la resolución de esta brecha antes de cualquier evaluación clínica.

---

## Información de Mercado en Argentina

Buflomedil no cuenta con autorizaciones de comercialización registradas ante ANMAT. No hay productos aprobados para listar.

---

## Consideraciones de Seguridad

> Consultar el prospecto y la literatura regulatoria internacional para información de seguridad. Se advierte que Buflomedil fue retirado de varios mercados europeos por asociación con toxicidad neurológica grave (incluyendo convulsiones y coma) en contextos de sobredosis o deterioro renal. Esta señal de seguridad histórica debe ser evaluada formalmente antes de cualquier iniciativa de reposicionamiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El modelo TxGNN no generó predicciones para Buflomedil, y los datos de base (MOA, seguridad regulatoria, indicaciones originales estructuradas) son insuficientes para sustentar un análisis de reposicionamiento. Adicionalmente, el perfil de seguridad histórico del compuesto representa una señal de alerta que requiere evaluación prioritaria.

**Para avanzar se necesita:**
- Resolver por qué TxGNN no generó predicciones: verificar cobertura del nodo DB13510 en el grafo de conocimiento y considerar re-ejecutar el pipeline con mapeo manual
- Obtener el mecanismo de acción verificado desde DrugBank API o literatura primaria
- Descargar y analizar el prospecto completo (TFDA o EMA) para extraer advertencias, contraindicaciones e interacciones farmacológicas
- Evaluar formalmente el perfil de seguridad histórico (retiro de mercado europeo, riesgo de convulsiones) como criterio de elegibilidad para reposicionamiento
- Confirmar si existe alguna indicación aprobada en mercados internacionales activos (ej. algunos países de Asia o América Latina) que pueda servir de ancla para el análisis
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

