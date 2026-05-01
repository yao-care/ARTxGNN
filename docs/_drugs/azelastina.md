---
layout: default
title: Azelastina
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 0
---

# Azelastina
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

# Azelastina: Evaluación Preliminar — Sin Indicación Predicha Disponible

## Resumen en Una Frase

Azelastina es un antihistamínico de segunda generación (antagonista del receptor H1) utilizado ampliamente para el tratamiento de la rinitis alérgica y la conjuntivitis alérgica.
El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el ciclo de análisis actual,
y el Evidence Pack presenta **múltiples brechas de datos críticas** que impiden una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack (conocida: rinitis alérgica, conjuntivitis alérgica) |
| Nueva Indicación Predicha | — Ninguna predicción generada por TxGNN — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin estudios ni predicción aplicable) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generó una Predicción?

Azelastina es un antagonista selectivo del receptor de histamina H1, con propiedades antiinflamatorias y estabilizadoras de mastocitos adicionales. Se utiliza principalmente en formulaciones tópicas (spray nasal y gotas oftálmicas) para el alivio sintomático de condiciones alérgicas como rinitis alérgica estacional y perenne, y conjuntivitis alérgica.

El modelo TxGNN no generó predicciones de nuevas indicaciones para Azelastina en este ciclo de análisis. Esto puede deberse a varias razones: (1) el fármaco no se encuentra actualmente en el grafo de conocimiento del modelo, (2) su perfil farmacológico no alcanzó los umbrales de confianza requeridos para ninguna nueva indicación, o (3) las indicaciones potenciales ya están cubiertas por su uso aprobado actual.

Adicionalmente, el Evidence Pack carece de información crítica: no se dispone del identificador DrugBank (`drugbank_id`: null), del mecanismo de acción detallado (MOA), ni de las advertencias y contraindicaciones del prospecto. Estas brechas de datos, clasificadas como **Blocking** y **High severity**, impiden realizar una evaluación de seguridad inicial (S1) y un análisis de relación mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados en el Evidence Pack.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible en el Evidence Pack.

---

## Información de Mercado en Argentina

Azelastina **no se encuentra comercializada** en Argentina. No se identificaron autorizaciones de comercialización vigentes (0 registros encontrados en la consulta regulatoria del 2026-03-29).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no están disponibles en el Evidence Pack actual.

> ⚠️ **Brecha de datos crítica (Blocking):** No se ha obtenido el prospecto con advertencias y contraindicaciones de la autoridad regulatoria. Se requiere descargar y analizar el prospecto PDF desde la fuente oficial antes de avanzar con cualquier evaluación de seguridad.

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Blocking** | No es posible iniciar la evaluación de seguridad S1 | Sitio web de la autoridad regulatoria (descargar y analizar prospecto PDF) |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | **Alta** | Afecta el análisis de relación mecanística | DrugBank API |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se dispone de una predicción de nueva indicación por parte de TxGNN, y el Evidence Pack presenta brechas de datos críticas (Blocking) que impiden avanzar con cualquier evaluación de reposicionamiento. Además, el fármaco no se encuentra comercializado en Argentina, lo que añade barreras regulatorias significativas.

**Para avanzar se necesita:**
- Resolver la brecha **DG001** (Blocking): obtener el prospecto completo con advertencias y contraindicaciones desde la fuente regulatoria oficial
- Resolver la brecha **DG002** (Alta): obtener el mecanismo de acción detallado desde DrugBank (consultar con INN "Azelastine" en inglés)
- Verificar la inclusión de Azelastina en el grafo de conocimiento de TxGNN y, de ser necesario, incorporarla para generar predicciones en el próximo ciclo
- Evaluar si existen formulaciones de Azelastina registradas en Argentina bajo otros nombres comerciales o combinaciones (p. ej., Azelastina + Fluticasona)
- Considerar la búsqueda manual de literatura sobre usos off-label de Azelastina (p. ej., asma, urticaria crónica, dermatitis) para alimentar futuros ciclos del modelo
---

