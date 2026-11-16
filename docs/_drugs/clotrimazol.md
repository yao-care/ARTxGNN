---
layout: default
title: Clotrimazol
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 2
drugbank_id: DB00257
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-16
description: "Clotrimazol: nueva indicación predicha, Acné (acne (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Clotrimazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Clotrimazol: Acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Clotrimazol es un antifúngico de la clase de los imidazoles, comercializado en Argentina en formas tópicas (cremas, spray, polvo y pasta dérmicos).
El modelo TxGNN predice que podría ser útil para **Acné (acne (disease))**, pero solo hay **1 ensayo clínico** (suspendido, sin resultados y con una combinación triple) y **ninguna publicación** que respalde esta dirección. La evidencia es, por tanto, muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (9 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clotrimazol pertenece a los antifúngicos imidazólicos, que inhiben la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51). Esto bloquea la síntesis de ergosterol y altera la membrana del hongo.

Un vínculo plausible con el acné es indirecto. Los azoles actúan contra *Malassezia* y tienen cierta actividad antiinflamatoria. La foliculitis por *Malassezia* (pitirosporo) se confunde a menudo con acné vulgar, y esto podría explicar parte de la señal del modelo. Clotrimazol no tiene actividad establecida contra el acné impulsado por *Cutibacterium acnes*.

El puntaje de TxGNN es muy alto (0,9986), pero proviene de una predicción basada en redes y no es evidencia clínica. El único ensayo disponible prueba una combinación de beclometasona, gentamicina y clotrimazol. Cualquier efecto observado no podría atribuirse a clotrimazol por sí solo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la eficacia de una crema con beclometasona + gentamicina + clotrimazol en pacientes con dermatosis contaminada con lesiones bilaterales simétricas. No tiene resultados publicados. Al ser una combinación triple, no se puede aislar el aporte de clotrimazol. El enfoque parece ser más de dermatosis infectadas o fúngicas que de acné vulgar. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Clotrimazol figura como comercializado, con 9 autorizaciones vigentes. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 34526 | MYCANDEN | Crema x 20 g |
| 2042 | MICOMAZOL | Crema dérmica x 30 g |
| 32028 | MYCANDEN | Spray x 60 ml |
| 20139 | IKOLAN | Crema 1% x 25 g |
| 32425 | MICOSEP | Pasta dérmica x 30 g |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto, pero no hay ningún estudio con datos interpretables que evalúe clotrimazol en acné. El único ensayo es una combinación triple, está suspendido y no tiene resultados. Tampoco hay literatura de respaldo, y la plausibilidad mecanística es débil.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen clotrimazol solo en acné, o en foliculitis por *Malassezia* si se quiere explorar esa hipótesis.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto, que hoy no están disponibles.
- Una definición clara de la población objetivo (acné vulgar frente a foliculitis por *Malassezia*) y de la formulación tópica adecuada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

