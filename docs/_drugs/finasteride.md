---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando el skill `txgnn-pipeline` como referencia contextual del proyecto. Ahora procedo a redactar el informe de evaluación basado en el Evidence Pack proporcionado.

---

# Finasteride: De Hiperplasia Prostática Benigna a Hipertricosis Universalis Congénita tipo Ambras

## Resumen en Una Frase

Finasteride es un inhibidor de la 5α-reductasa, conocido globalmente por su uso en la hiperplasia prostática benigna y la alopecia androgénica masculina, aunque no cuenta con registro en Argentina.
El modelo TxGNN predice que podría ser efectivo para la **Hipertricosis Universalis Congénita tipo Ambras**,
sin embargo, actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación, situando la predicción en el nivel de evidencia más bajo (L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro en Argentina; globalmente indicado para hiperplasia prostática benigna y alopecia androgénica |
| Nueva Indicación Predicha | Hipertricosis Universalis Congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack (pendiente de consulta a DrugBank API). Según la información científicamente establecida, Finasteride pertenece a la clase de los inhibidores de la 5α-reductasa tipo II: bloquea la conversión periférica de testosterona en dihidrotestosterona (DHT), reduciendo así la señalización androgénica en tejidos como el folículo piloso y la glándula prostática. Su eficacia en hiperplasia prostática benigna y alopecia androgénica ha sido ampliamente comprobada en ensayos clínicos de Fase 3.

La conexión teórica con la Hipertricosis Universalis Congénita tipo Ambras parte del supuesto de que la reducción de DHT podría disminuir el estímulo androgénico al crecimiento folicular generalizado. Sin embargo, la Hipertricosis tipo Ambras es una condición genética causada por reorganización cromosómica en el cromosoma 8 (locus TRPS1/EXT1), cuya patogénesis es **independiente de los andrógenos**. El mecanismo del fármaco no actúa sobre defectos estructurales del genoma ni sobre la expresión génica aberrante propia de este síndrome.

En consecuencia, aunque el modelo asigna una puntuación de predicción muy elevada (99.99%), la conexión mecanística es extremadamente débil y no cuenta con respaldo clínico ni bibliográfico. La alta puntuación probablemente refleja conexiones indirectas en el grafo de conocimiento entre nodos de crecimiento folicular, andrógenos y trastornos cutáneos, y no una relevancia terapéutica real para esta enfermedad específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Finasteride no cuenta con ninguna autorización de comercialización registrada en Argentina a la fecha de corte (2026-05-01). No se dispone de información de autorizaciones ANMAT para este fármaco.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La Hipertricosis Universalis Congénita tipo Ambras presenta una base patogénica genético-cromosómica que no involucra la vía DHT, por lo que el mecanismo de acción de Finasteride no tiene conexión directa con esta enfermedad. La ausencia total de evidencia clínica y bibliográfica (nivel L5) no justifica ningún avance hacia estudios aplicados.

**Para avanzar se necesita:**
- Investigación básica que explore si existe algún rol de los andrógenos o de la 5α-reductasa en la expresión fenotípica de la Hipertricosis tipo Ambras
- Obtención de datos completos del mecanismo de acción (MOA) desde DrugBank API
- Obtención de advertencias de seguridad e información regulatoria de ANMAT (juzgado como Blocking en el Evidence Pack)
- Evaluación de modelos in vitro o estudios mecanísticos antes de considerar cualquier protocolo clínico
---

