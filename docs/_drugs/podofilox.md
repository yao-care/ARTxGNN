---
layout: default
title: Podofilox
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Podofilox
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

Usando `txgnn-pipeline` para guiar la generación del informe de evaluación de reposicionamiento.

---

# Podofilox: De Verrugas Genitales a Vulvovaginal Candidiasis

## Resumen en Una Frase

Podofilox es un agente antimitótico tópico globalmente aprobado para el tratamiento de verrugas genitales externas (condilomas acuminados) causadas por el virus del papiloma humano (VPH), cuyo mecanismo principal consiste en inhibir la polimerización de la tubulina en las células epiteliales infectadas.
El modelo TxGNN predice que podría ser efectivo para **Vulvovaginal Candidiasis**,
con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Verrugas genitales externas (condilomas acuminados) — indicación globalmente aprobada |
| Nueva Indicación Predicha | Vulvovaginal Candidiasis |
| Puntaje de Predicción TxGNN | 99.47% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de podofilox en esta base de datos. Según la información conocida, podofilox es un lignano natural derivado de la resina de podofilo (*Podophyllum peltatum*). Su eficacia comprobada en condilomas acuminados se basa en la inhibición de la polimerización de la tubulina, que induce detención del ciclo celular en fase G2/M y apoptosis en las células epiteliales proliferativas infectadas por VPH.

Sin embargo, la conexión mecanística con la vulvovaginal candidiasis es farmacológicamente débil. Esta condición es una infección fúngica causada principalmente por *Candida albicans*, cuyo tratamiento estándar son los antifúngicos azólicos que actúan inhibiendo la síntesis de ergosterol en la membrana celular fúngica. Podofilox no tiene ninguna actividad conocida sobre la pared celular fúngica, el metabolismo del ergosterol ni ninguna otra diana relevante para *Candida* spp.

La única publicación recuperada (PMID 10537386, 1999) es una revisión general de tratamientos para ETS que aborda infecciones vaginales como parte de un panorama amplio, sin datos directos sobre podofilox en candidiasis. La predicción de TxGNN probablemente refleja co-ocurrencia diagnóstica en la misma población de pacientes (clínicas de ETS) antes que una relación farmacológica causal.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Revisión (ETS) | American Family Physician | Resumen de guías CDC 1998 para el tratamiento de ETS; incluye infecciones vaginales, enfermedad inflamatoria pélvica y verrugas genitales como temas generales — no evalúa podofilox directamente para candidiasis vaginal |

---

## Información de Mercado en Argentina

Podofilox no cuenta con ninguna autorización de comercialización registrada en Argentina. Total de autorizaciones: 0.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni base mecanística que respalde el uso de podofilox en vulvovaginal candidiasis; el único artículo recuperado es una revisión de 1999 que no evalúa esta indicación, y el mecanismo antimitótico del fármaco es incompatible con el tratamiento de infecciones fúngicas.

**Para avanzar se necesita:**
- Confirmación o descarte de actividad antifúngica mediante estudios in vitro específicos de podofilox frente a *Candida* spp.
- Obtención del MOA completo vía consulta a DrugBank API (Data Gap DG002)
- Descarga del prospecto oficial para completar información de seguridad, advertencias y contraindicaciones (Data Gap DG001)
- Evaluación de si la asociación detectada por TxGNN es consecuencia de co-morbilidad poblacional (pacientes ETS) en lugar de eficacia farmacológica real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

