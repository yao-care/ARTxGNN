---
layout: default
title: Ticagrelor
parent: Solo Predicción del Modelo (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ticagrelor: nueva indicación predicha, Arteriosclerosis intracraneal (nivel de evidencia L5). Indicación original: Síndrome coronario agudo (según el grafo de conocimiento"
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "mesenteric vascular occlusion", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
---

# Ticagrelor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Ticagrelor: De Síndrome Coronario Agudo a Arteriosclerosis Intracraneal

## Resumen en Una Frase

Ticagrelor es un inhibidor reversible del receptor plaquetario P2Y12, utilizado originalmente para el tratamiento del síndrome coronario agudo y de enfermedades vasculares periféricas.
El modelo TxGNN predice que podría ser efectivo para **arteriosclerosis intracraneal**,
con **2 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección (un ensayo de Fase 3 aún sin resultados).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Arteriosclerosis intracraneal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 (basado en el diseño del ensayo de Fase 3 CAPTIVA, aún sin resultados; ver nota en la conclusión) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ticagrelor es un inhibidor reversible del receptor P2Y12 plaquetario; su eficacia en el síndrome coronario agudo ha sido comprobada y, mecanísticamente, podría ser aplicable a la arteriosclerosis intracraneal.

La estenosis aterosclerótica intracraneal sintomática implica trombosis dependiente de plaquetas y embolia de arteria a arteria, por lo que el bloqueo de P2Y12 es mecanísticamente plausible. La relación con la indicación original es clara: ambas son enfermedades ateroscleróticas arteriales en las que la activación plaquetaria es central.

La evidencia es más sólida en portadores de variantes de pérdida de función de CYP2C19, donde ticagrelor evita la activación reducida de clopidogrel. El principal riesgo es el sangrado, incluida la hemorragia intracraneal, y la dosificación en contextos neurointervencionistas aún se está refinando.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Activo, sin reclutamiento | 1683 | CAPTIVA: determina si rivaroxabán, ticagrelor o ambos son superiores a clopidogrel para reducir a 1 año el ictus isquémico, la hemorragia intracerebral o la muerte vascular. Resultados aún no disponibles. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | No aplica | Reclutando | 100 | Estudio piloto de selección de inhibidor P2Y12 guiada por genotipo frente a clopidogrel convencional en enfermedad aterosclerótica intracraneal sintomática. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Experiencia con ticagrelor 60 mg dos veces al día más aspirina 81 mg frente al régimen estándar con clopidogrel en stent intracraneal. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Revisión | Int J Stroke | Diseño y avance inicial del ensayo CAPTIVA, que evalúa combinaciones antitrombóticas frente a clopidogrel más aspirina en estenosis intracraneal sintomática. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 47785 | BRILINTA (AstraZeneca) | 90 mg comprimidos x 60 | No disponible |
| 57586 | TICAZAN (Elea) | 90 mg comprimidos x 30 | No disponible |
| 47784 | BRILINTA (AstraZeneca) | 90 mg comprimidos x 30 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar y hemorragia intracraneal.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; las principales son:
  - **Mayor**: claritromicina.
  - **Moderada**: ácido acetilsalicílico, morfina, aprepitant, dexametasona, budesonida, simvastatina, saxagliptina, miconazol, cisaprida, clotrimazol, rolapitant, eliglustat, naldemedina, metreleptina, nitisinona y dexfenfluramina.
  - **Menor**: naloxegol y prucaloprida.

Se recomienda consultar el prospecto para las advertencias oficiales, ya que no están incluidas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 de gran tamaño (CAPTIVA) que evalúa directamente ticagrelor en arteriosclerosis intracraneal, pero aún no tiene resultados y no es específico de ticagrelor. El nivel L1 se sustenta en el diseño y no en resultados; estrictamente, no se cumple el criterio de ≥2 ECAs de Fase 3 completados, por lo que la evidencia debe considerarse preliminar. La hemorragia intracraneal es una contraindicación señalada, lo que exige cautela.

**Para avanzar se necesita:**
- Resultados del ensayo CAPTIVA (finalización prevista para 2027).
- Texto de indicaciones y advertencias del prospecto de ANMAT.
- Datos detallados del mecanismo de acción.
- Criterios de selección de pacientes (por ejemplo, genotipo CYP2C19), duración del tratamiento y plan de monitoreo del riesgo de sangrado.

### Otras indicaciones predichas (para referencia)

- **Enfermedad isquémica** (puntaje 99.64%, L1, Proceed with Guardrails): hay numerosos ECAs de alto impacto, pero se superpone con la indicación original de síndrome coronario agudo, por lo que es en gran parte confirmatoria y no un reposicionamiento novedoso.
- **Hold** (sin evidencia clínica sólida o con relación mecanística débil o inversa): arteriosclerosis de Mönckeberg, priapismo, síndrome de May-Thurner, livedo reticularis, oclusión vascular mesentérica, ectasia vascular, angiodisplasia (el antiagregante podría empeorar el sangrado) y tromboembolismo venoso (el tratamiento estándar son los anticoagulantes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

