---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# ATENOLOL: Evaluación Preliminar — Sin Indicaciones Predichas

## Resumen en Una Frase

Atenolol es un betabloqueante beta-1 selectivo ampliamente utilizado a nivel mundial para el tratamiento de la hipertensión arterial, angina de pecho y arritmias cardíacas.
Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco,
y **no se cuenta con ensayos clínicos ni publicaciones** que respalden un reposicionamiento específico en esta evaluación.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en el sistema (conocida globalmente: hipertensión, angina, arritmias) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos de base, sin estudios orientados a reposicionamiento) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones?

Atenolol (DrugBank ID: DB00335) es un antagonista selectivo de los receptores beta-1 adrenérgicos. A nivel internacional es uno de los betabloqueantes más prescritos para el manejo de la hipertensión arterial, la angina de pecho estable y ciertas arritmias cardíacas. Sin embargo, en el presente Evidence Pack no se dispone de datos detallados sobre el mecanismo de acción (MOA) provenientes de DrugBank, lo que constituye una brecha de datos de severidad alta (DG002).

El modelo TxGNN no ha generado predicciones de nuevas indicaciones para atenolol en esta iteración. Esto puede deberse a varios factores: (1) el fármaco no se encuentra comercializado en Argentina, lo que limita la integración de datos regulatorios locales; (2) las indicaciones cardiovasculares de atenolol ya están ampliamente cubiertas, reduciendo el espacio para reposicionamiento novedoso; y (3) la ausencia de datos de MOA estructurados puede haber limitado la capacidad del modelo para establecer conexiones mecanísticas con nuevas enfermedades.

Para futuras iteraciones, se recomienda completar los datos de mecanismo de acción y evaluar si la integración de datos regulatorios de otras jurisdicciones permite al modelo generar predicciones relevantes.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con reposicionamiento registrados para esta evaluación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con reposicionamiento disponible para esta evaluación.

---

## Información de Mercado en Argentina

Atenolol **no se encuentra comercializado** en Argentina según los registros consultados. No se identificaron autorizaciones de comercialización vigentes (0 licencias).

> **Nota:** La ausencia de registro en Argentina no implica que el fármaco carezca de aprobación en otras jurisdicciones. Atenolol cuenta con aprobaciones en múltiples países (FDA, EMA, entre otros) para indicaciones cardiovasculares.

---

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no se encuentran disponibles en el presente Evidence Pack.

**Brechas de datos identificadas:**

| ID | Categoría | Item Faltante | Severidad | Impacto |
|----|-----------|---------------|-----------|---------|
| DG001 | Drug_Level | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No es posible realizar la evaluación inicial de seguridad (S1) |
| DG002 | Drug_Level | Mecanismo de acción (MOA) | Alta | Afecta el análisis de relación mecanística |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se dispone de predicciones del modelo TxGNN para nuevas indicaciones de atenolol. Además, el fármaco no está comercializado en Argentina y existen brechas de datos críticas (advertencias/contraindicaciones del prospecto y mecanismo de acción) que impiden completar la evaluación de seguridad inicial.

**Para avanzar se necesita:**
- Completar los datos del mecanismo de acción (MOA) desde DrugBank API (DG002)
- Obtener y analizar el prospecto oficial con advertencias y contraindicaciones (DG001 — severidad bloqueante)
- Verificar si existe registro regulatorio en Argentina bajo nombres comerciales alternativos
- Re-ejecutar el modelo TxGNN una vez completados los datos de MOA para evaluar si se generan predicciones de reposicionamiento
- Considerar la integración de datos regulatorios de jurisdicciones donde atenolol sí está aprobado (FDA, EMA) para enriquecer el perfil del fármaco
---

