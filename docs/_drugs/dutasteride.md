---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Dutasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

---

# Dutasteride: De Hiperplasia Prostática Benigna a Hypertrichosis Universalis Congenita tipo Ambras

## Resumen en Una Frase

Dutasteride es un inhibidor dual de la 5α-reductasa (tipos 1 y 2), utilizado originalmente para el tratamiento de la hiperplasia prostática benigna (HPB) y la alopecia androgenética.
El modelo TxGNN predice que podría ser efectivo para **Hypertrichosis Universalis Congenita tipo Ambras**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden directamente esta indicación, y el análisis mecanístico sugiere que se trata de un artefacto de red del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia Prostática Benigna (HPB) |
| Nueva Indicación Predicha | Hypertrichosis Universalis Congenita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos de este reporte. Según el conocimiento farmacológico establecido, Dutasteride es un inhibidor dual de la 5α-reductasa (tipos 1 y 2), que bloquea la conversión de testosterona en dihidrotestosterona (DHT). Al reducir los niveles de DHT, disminuye la estimulación androgénica tanto del tejido prostático (mecanismo de acción en HPB) como de los folículos pilosos androgénico-sensibles (mecanismo de acción en alopecia androgenética).

La Hypertrichosis Universalis Congenita tipo Ambras es una condición genética extremadamente rara causada por anomalías cromosómicas en la región 8q22-q23, que resulta en un crecimiento piloso excesivo y generalizado de origen estructural. A diferencia de la alopecia androgenética —donde la DHT es un mediador clave—, el síndrome de Ambras no está mediado por el eje DHT/5α-reductasa. El defecto genético subyacente es independiente de las vías en las que actúa Dutasteride.

El análisis mecanístico concluye que esta predicción es probablemente un **artefacto de red del modelo TxGNN**: el sistema conecta los nodos de biología folicular de Dutasteride con enfermedades del cabello de forma inespecífica, sin que exista una vía molecular real entre la inhibición de la 5α-reductasa y la corrección de la anomalía cromosómica responsable del síndrome de Ambras. **No hay base mecanística que respalde esta predicción.**

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Dutasteride no cuenta con autorizaciones de comercialización registradas en Argentina a la fecha del presente informe (corte de datos: 2026-05-01).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de que el puntaje numérico de TxGNN es extremadamente alto (99.998%), la predicción carece por completo de respaldo mecanístico, clínico y bibliográfico: la Hypertrichosis tipo Ambras es una enfermedad cromosómica cuyo origen no involucra la vía DHT/5α-reductasa, lo que hace que Dutasteride sea farmacológicamente incoherente para esta indicación. El puntaje elevado refleja un artefacto de la red de conocimiento del modelo, no una asociación biológicamente válida.

**Para avanzar se necesita:**
- Completar la información del mecanismo de acción (resolver brecha DG002: consulta a DrugBank API)
- Obtener información de seguridad completa del prospecto de referencia (resolver brecha DG001)
- Evaluar indicaciones alternativas con mayor respaldo mecanístico —en particular **alopecia androgenética** (rank 8, con literatura asociada) o **hypotrichosis simplex of the scalp** (rank 6)— para las cuales la vía DHT/5α-reductasa sí es clínicamente relevante
- Verificar estado regulatorio en Argentina para eventuales indicaciones con mayor nivel de evidencia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

