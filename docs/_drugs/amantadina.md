---
layout: default
title: Amantadina
parent: Solo Predicción del Modelo (L5)
nav_order: 23
evidence_level: L5
indication_count: 4
drugbank_id: DB00915
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
last_modified_at: 2026-11-24
description: "Amantadina: nueva indicación predicha, Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Amantadina
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

## Amantadina: Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumen en Una Frase

Amantadina es un fármaco comercializado en Argentina con cuatro autorizaciones vigentes de producto de un solo principio activo.
El modelo TxGNN predice que podría ser efectivo para la **Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción exclusivamente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Puntaje de Predicción TxGNN | 0.9948 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amantadina (traducción no oficial): «Se desconoce el mecanismo por el cual la amantadina ejerce su eficacia en el tratamiento de la discinesia en pacientes con enfermedad de Parkinson o como tratamiento complementario de levodopa/carbidopa en pacientes con enfermedad de Parkinson que presentan episodios 'off'. La amantadina es un antagonista no competitivo débil del receptor NMDA.» Texto original en inglés: "The mechanism by which amantadine exerts efficacy in the treatment of dyskinesia in patients with Parkinson's disease or as adjunctive treatment to levodopa/carbidopa in patients with Parkinson's disease experiencing 'off' episodes is unknown. Amantadine is a weak uncompetitive antagonist of the NMDA receptor." ([DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28), versión del 2026-10-05; consultado el 2026-11-19). Según la información conocida, amantadina actúa como antagonista del receptor NMDA, modulador de la transmisión dopaminérgica e inhibidor del canal iónico M2 viral.

Una hipótesis puramente especulativa es que el bloqueo NMDA podría reducir la excitotoxicidad mediada por glutamato. La encefalitis de Rasmussen implica neuroinflamación mediada por linfocitos T y mecanismos relacionados con receptores de glutamato, por lo que existiría un punto de contacto teórico.

Ningún estudio respalda este vínculo. El puntaje alto del modelo, por sí solo, no basta para justificar su consideración clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 46782 | VIROSOL | 100 mg comp.x 30 | Elea | Vigente |
| 7636 | VIROSOL | 100 mg comp.x 10 | Elea | Vigente |
| 39691 | AMPAKINE | 100 mg comp.x 60 | Rontag | Vigente |
| 39690 | AMPAKINE | 100 mg comp.x 30 | Rontag | Vigente |

La tabla muestra los 4 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo, sin ensayos clínicos ni literatura que estudien directamente la enfermedad. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de seguridad del prospecto de ANMAT
- Revisión de literatura preclínica sobre antagonismo NMDA y excitotoxicidad en encefalitis de Rasmussen
- Evaluación de plausibilidad biológica por parte de expertos antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

