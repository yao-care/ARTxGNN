---
layout: default
title: Nistatina
parent: Solo Predicción del Modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 9
drugbank_id: DB00646
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
last_modified_at: 2026-11-24
description: "Nistatina: nueva indicación predicha, enfermedad de la región orbitaria (disease of orbital region) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 7 (en el listado vigente: 7)"
---

# Nistatina
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

## Nistatina: enfermedad de la región orbitaria (disease of orbital region)
{: .text-alpha }

## Resumen en Una Frase

Nistatina es un antifúngico poliénico que se comercializa en Argentina en comprimidos vaginales, comprimidos orales, suspensión oral, crema y óvulos.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la región orbitaria (disease of orbital region)**, con un puntaje de 0,9990.
Para esta predicción no hay estudios que respalden la dirección: el único ensayo clínico vinculado corresponde a otra enfermedad (atrofia geográfica de la retina) y no hay literatura.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad de la región orbitaria (disease of orbital region) |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Nistatina (traducción no oficial): «La nistatina actúa uniéndose a los esteroles de la membrana celular de las especies de Candida sensibles, con el consiguiente cambio en la permeabilidad de la membrana que permite la salida de componentes intracelulares. La nistatina no muestra una actividad apreciable contra bacterias, protozoos ni virus.» Texto original en inglés: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), versión del 2026-02-06; consultado el 2026-11-19). Por conocimiento general, la nistatina se une al ergosterol de la membrana de los hongos y altera su integridad. No se absorbe de forma sistémica tras su uso oral o tópico.

Con ese mecanismo, no se identifica un vínculo biológico creíble con una enfermedad de la región orbitaria. El puntaje alto (0,9990) proviene de una predicción computacional sin respaldo biológico ni clínico, y probablemente refleja asociaciones entre términos de la ontología de enfermedades más que una relación terapéutica real.

Por lo tanto, esta predicción debe tomarse solo como una hipótesis sin sustento y no como una indicación plausible.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Fase 1 | Reclutando | 42 | Estudio de escalada de dosis de ASP7317 (terapia celular) en atrofia geográfica secundaria a degeneración macular asociada a la edad. No involucra nistatina ni enfermedad orbitaria; no aporta evidencia a esta predicción. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 12236 | DIPNI | 100000 UI comp.vag.x 12 | Omega | Vigente |
| 12237 | DIPNI | 500000 UI comp.oral.x 12 | Omega | Vigente |
| 12238 | DIPNI | 500000 UI comp.oral.x 30 | Omega | Vigente |
| 31789 | NISTATINA DENVER FARMA | cr.x 30 g | Denver Farma | Vigente |
| 31788 | NISTATINA DENVER FARMA | susp.oral x 60 ml | Denver Farma | Vigente |

La tabla muestra 5 de los 7 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Se muestran 5 de las 7 autorizaciones vigentes de nistatina de un solo principio activo (las otras dos corresponden a DIPNI comprimidos vaginales x 6 y O BIOL óvulos x 6).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo: el nivel de evidencia es L5, no hay literatura y el único ensayo vinculado estudia una enfermedad retiniana con un tratamiento no relacionado. Además, no existe un mecanismo plausible para que un antifúngico sin absorción sistémica actúe sobre una enfermedad orbitaria.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que vincule la nistatina con la región orbitaria
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Análisis de compatibilidad de vías de administración, dado que las formas disponibles son orales, vaginales y tópicas

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

