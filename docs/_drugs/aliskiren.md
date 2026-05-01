---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# ALISKIREN: Evaluación de Reposicionamiento — Sin Nuevas Indicaciones Predichas

## Resumen en Una Frase

Aliskiren es un inhibidor directo de la renina utilizado originalmente para el tratamiento de la hipertensión arterial. El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco. Adicionalmente, el fármaco **no se encuentra comercializado en Argentina** y presenta múltiples brechas de datos que impiden una evaluación completa.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial (conocida por clase terapéutica; sin autorización local registrada) |
| Nueva Indicación Predicha | — Sin predicciones disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin evidencia; solo datos de referencia del fármaco) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generaron Predicciones?

Aliskiren (DrugBank ID: DB09026) es un inhibidor directo de la renina, el primer fármaco aprobado en su clase. Actúa bloqueando la renina, la enzima que inicia la cascada del sistema renina-angiotensina-aldosterona (SRAA), reduciendo así la producción de angiotensina I y angiotensina II, lo que resulta en una disminución de la presión arterial. A nivel internacional, ha sido comercializado bajo los nombres Tekturna® (EE.UU.) y Rasilez® (Europa).

El modelo TxGNN no generó predicciones de nuevas indicaciones para este fármaco. Esto puede deberse a varios factores: (1) la representación del fármaco en el grafo de conocimiento utilizado por TxGNN puede ser insuficiente, (2) las relaciones fármaco-enfermedad conocidas para aliskiren pueden no presentar patrones transferibles a otras patologías dentro del modelo, o (3) el perfil farmacológico altamente específico del inhibidor directo de renina puede limitar su aplicabilidad predicha a nuevas indicaciones.

Adicionalmente, la ausencia de datos de mecanismo de acción (MOA) en el Evidence Pack y la falta de autorizaciones regulatorias en Argentina reducen la cantidad de señales de entrada disponibles para el modelo predictivo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados, dado que no se generaron predicciones de reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible, dado que no se generaron predicciones de reposicionamiento.

---

## Información de Mercado en Argentina

Aliskiren **no se encuentra comercializado en Argentina**. No se identificaron autorizaciones de comercialización vigentes en el registro regulatorio consultado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** No se dispone de datos locales de advertencias, contraindicaciones ni interacciones farmacológicas en el Evidence Pack. Como referencia general, a nivel internacional aliskiren presenta las siguientes precauciones conocidas:
> - **Contraindicado** en combinación con inhibidores de la ECA o bloqueantes de los receptores de angiotensina (ARA II) en pacientes con diabetes mellitus o insuficiencia renal (TFG < 60 mL/min).
> - **Riesgo en embarazo**: Puede causar daño fetal; está contraindicado en el embarazo (categoría D).
> - **Hiperpotasemia**: Riesgo aumentado cuando se combina con otros fármacos que actúan sobre el SRAA o con suplementos de potasio.
> - **Angioedema**: Se han reportado casos de angioedema que requieren la suspensión inmediata del tratamiento.

---

## Brechas de Datos Identificadas

| ID | Categoría | Ítem Faltante | Severidad | Impacto | Remediación Sugerida |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No es posible realizar la evaluación inicial de seguridad (S1) | Descargar y analizar el prospecto desde el sitio de la autoridad regulatoria |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | Alta | Afecta el análisis de relación mecanística | Consultar la API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No se generaron predicciones de nuevas indicaciones por parte del modelo TxGNN para aliskiren. Además, el fármaco no se encuentra comercializado en Argentina (0 autorizaciones), y existen brechas de datos críticas — incluyendo la ausencia de información de seguridad local (severidad bloqueante) y de mecanismo de acción — que impiden avanzar con cualquier evaluación de reposicionamiento.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001: obtener las advertencias y contraindicaciones del prospecto oficial
- Completar los datos de mecanismo de acción (MOA) desde DrugBank (DG002)
- Verificar si existen datos adicionales en el grafo de conocimiento de TxGNN que puedan mejorar la representación de aliskiren
- Evaluar si la ausencia de predicciones se debe a limitaciones del modelo o a una genuina falta de potencial de reposicionamiento
- Considerar si el fármaco amerita una nueva ejecución del modelo una vez que se completen las brechas de datos
---

