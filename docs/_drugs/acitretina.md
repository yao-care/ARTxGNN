---
layout: default
title: Acitretina
parent: Solo Predicción del Modelo (L5)
nav_order: 16
evidence_level: L5
indication_count: 4
drugbank_id: DB00459
monitor_inn: "Acitretin"
predicted_indications: ["acne (disease)", "pediatric systemic lupus erythematosus", "fetal erythroblastosis", "familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome"]
last_modified_at: 2026-11-16
description: "Acitretina: nueva indicación predicha, acné (acne (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Acitretina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Acitretina: acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Acitretina es un retinoide oral de segunda generación, comercializado en Argentina como NEOTIGASON. El modelo TxGNN predice que podría ser efectivo para **acné (acne (disease))**, pero el respaldo es indirecto: hay **1 ensayo clínico** y **18 publicaciones** compiladas, y casi todo se refiere a la hidradenitis supurativa (acné inverso), no al acné vulgar.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en los datos compilados. Por farmacología conocida de la clase, la acitretina normaliza la diferenciación de los queratinocitos y la queratinización folicular, y tiene efectos inmunomoduladores sobre vías inflamatorias como Th17. Estos efectos podrían, en teoría, ser relevantes en enfermedades que afectan al folículo pilosebáceo.

Las revisiones sobre retinoides respaldan efectos sobre la glándula sebácea, pero el retinoide oral establecido para el acné vulgar es la isotretinoína, no la acitretina. Además, la etiqueta "acné" de la predicción parece mezclarse con el acné inverso (hidradenitis supurativa): el único ensayo y varias publicaciones tratan esa enfermedad. Por eso la relación con el acné vulgar es débil.

Dado que ningún estudio citado evalúa directamente el acné vulgar, el nivel de evidencia se limita a L5, aunque existan datos indirectos en una enfermedad relacionada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07708480](https://clinicaltrials.gov/study/NCT07708480) | Fase 4 | Completado | 70 | Comparación aleatorizada de apremilast (30 mg dos veces al día) frente a acitretina durante 12 semanas en hidradenitis supurativa moderada a grave; criterio principal: puntaje IHS4. Evalúa una enfermedad distinta del acné vulgar y la acitretina puede ser comparador activo. Resultados no disponibles en los datos compilados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Guía clínica | J Eur Acad Dermatol Venereol | Guía europea S1 para el tratamiento de la hidradenitis supurativa/acné inverso |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Serie/estudio clínico | Br J Dermatol | Resultados a largo plazo de acitretina en hidradenitis supurativa |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Reporte de caso | Cutis | Acné noduloquístico e hidradenitis supurativa tratados con acitretina |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Revisión | Der Hautarzt | Tratamiento farmacológico del acné inverso; antibióticos y anti-TNF-α como opciones principales |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Revisión | Dermatology | Retinoides y actividad de la glándula sebácea; eficacia de isotretinoína en acné |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Revisión | Clin Pharmacokinet | Farmacocinética y eficacia de retinoides; acitretina destaca en psoriasis |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Revisión | Clin Dermatol | Vitamina A y retinoides en dermatología |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Revisión | Drugs | Uso actual y potencial futuro de retinoides en dermatología |
| [40888828](https://pubmed.ncbi.nlm.nih.gov/40888828/) | 2025 | Revisión sistemática | Am J Clin Dermatol | Diferencias étnicas en la pustulosis palmoplantar (relación indirecta) |
| [33036809](https://pubmed.ncbi.nlm.nih.gov/33036809/) | 2020 | Consenso | An Bras Dermatol | Uso de isotretinoína oral en dermatología (otro fármaco) |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 27610 | NEOTIGASON | 10 mg cáps. x 30 | No registrada en los datos locales |
| 26974 | NEOTIGASON | 25 mg cáps. x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

La acitretina es un teratógeno potente, contraindicado en el embarazo, y exige un período prolongado de anticoncepción tras el tratamiento. En población pediátrica preocupan además el cierre epifisario prematuro y la toxicidad ósea con uso prolongado. Estas son consideraciones de la clase retinoide y no provienen del prospecto local; para información de seguridad detallada, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio compilado evalúa directamente el acné vulgar; la evidencia disponible corresponde a hidradenitis supurativa, una enfermedad distinta, y la isotretinoína ya es el retinoide oral establecido para el acné. Además, el riesgo teratogénico exige salvaguardas estrictas.

**Para avanzar se necesita:**
- Aclarar si la predicción se refiere a acné vulgar o a acné inverso (hidradenitis supurativa), y evaluar la evidencia por separado
- Estudios clínicos que evalúen la acitretina directamente en la enfermedad definida
- Datos del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT
- Plan de prevención del embarazo y de monitoreo de seguridad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

