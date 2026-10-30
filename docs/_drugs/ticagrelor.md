---
layout: default
title: Ticagrelor
parent: Solo Predicción del Modelo (L5)
nav_order: 236
evidence_level: L5
indication_count: 9
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
last_modified_at: 2026-10-30
description: "Ticagrelor: nueva indicación predicha, arteriosclerosis intracraneal (intracranial arteriosclerosis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ticagrelor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ticagrelor: antiagregante plaquetario inhibidor del receptor P2Y12 → arteriosclerosis intracraneal (intracranial arteriosclerosis)
{: .text-alpha }

## Resumen en Una Frase

Ticagrelor es un antiagregante plaquetario que bloquea el receptor P2Y12 y se comercializa en Argentina.
El modelo TxGNN predice que podría ser efectivo para **arteriosclerosis intracraneal (intracranial arteriosclerosis)**,
con **2 ensayos clínicos** y **2 publicaciones** relacionados con esta predicción, ninguno con resultados de eficacia publicados para esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | arteriosclerosis intracraneal (intracranial arteriosclerosis) |
| Puntaje de Predicción TxGNN | 0,9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, ticagrelor bloquea de forma reversible el receptor plaquetario P2Y12, lo que reduce la agregación plaquetaria y la formación de trombos.

La arteriosclerosis intracraneal es una enfermedad aterotrombótica en la que las placas de las arterias cerebrales pueden generar trombos dependientes de las plaquetas y causar ictus isquémico. Como el bloqueo de P2Y12 actúa sobre esa misma vía, la hipótesis mecanística es plausible.

Además, el estudio CHANCE-2 en portadores de pérdida de función de CYP2C19 con ictus menor o AIT mostró una ventaja de ticagrelor sobre clopidogrel en prevención secundaria cerebrovascular. Esto apoya la plausibilidad en el territorio cerebral, aunque no estudia específicamente la arteriosclerosis intracraneal.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Activo, sin reclutar | 1683 | CAPTIVA: compara rivaroxabán, ticagrelor o ambos frente a clopidogrel para reducir ictus isquémico, hemorragia intracerebral o muerte vascular al año en estenosis aterosclerótica intracraneal. Sin resultados aún; el brazo de ticagrelor debe verificarse |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | No aplica | Reclutando | 100 | Piloto de selección de inhibidor P2Y12 guiada por genotipo frente a clopidogrel en enfermedad aterosclerótica intracraneal sintomática; apoyo exploratorio |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Experiencia con ticagrelor 60 mg dos veces al día más aspirina frente a aspirina y clopidogrel en stent intracraneal |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Diseño de ensayo | Int J Stroke | Diseño y avance temprano de CAPTIVA en estenosis aterosclerótica intracraneal sintomática |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 47785 | BRILINTA | 90 mg comp. x 60 | No registrada en los datos locales |
| 57586 | TICAZAN | 90 mg comp. x 30 | No registrada en los datos locales |
| 47784 | BRILINTA | 90 mg comp. x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (100 registradas; se destacan las principales):
  - Mayor: claritromicina.
  - Moderadas: ácido acetilsalicílico, morfina, aprepitant, dexametasona, budesonida, simvastatina, saxagliptina, entre otras.
- No se dispone de datos de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para esa información. Dado el riesgo hemorrágico de los antiagregantes, conviene prestar especial atención a la hemorragia intracraneal, la enfermedad hepática y el uso concomitante de otros antitrombóticos.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción principal cuenta con un ensayo de Fase 3 en curso (CAPTIVA) y un piloto, ambos directamente sobre la enfermedad, pero sin resultados publicados de eficacia. El mecanismo es plausible y ticagrelor ya está comercializado en Argentina, aunque el riesgo hemorrágico exige salvaguardas.

**Para avanzar se necesita:**
- Resultados de CAPTIVA y confirmación del brazo de ticagrelor.
- Datos de advertencias y contraindicaciones del prospecto de ANMAT.
- Datos detallados del mecanismo de acción.
- Criterios de selección de pacientes, duración del tratamiento y estrategia de monitoreo del riesgo hemorrágico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

