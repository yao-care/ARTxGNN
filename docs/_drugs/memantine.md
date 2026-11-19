---
layout: default
title: Memantine
parent: Solo Predicción del Modelo (L5)
nav_order: 186
evidence_level: L5
indication_count: 4
monitor_inn: "MEMANTINE"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-11-20
description: "Memantine: nueva indicación predicha, hipertensión pulmonar (pulmonary hypertension) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Memantine
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

## Memantina: antagonista del receptor NMDA → hipertensión pulmonar (pulmonary hypertension)
{: .text-alpha }

## Resumen en Una Frase

Memantina es un antagonista no competitivo del receptor NMDA, comercializado en Argentina bajo múltiples marcas.
El modelo TxGNN predice que podría ser efectiva para **hipertensión pulmonar (pulmonary hypertension)**, pero **no hay ensayos clínicos** y solo **2 publicaciones**, ambas con relación tangencial, que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipertensión pulmonar (pulmonary hypertension) |
| Puntaje de Predicción TxGNN | 0,9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Memantine (traducción no oficial): «Se ha planteado la hipótesis de que la activación persistente de los receptores de N-metil-D-aspartato (NMDA) del sistema nervioso central por el aminoácido excitador glutamato contribuye a la sintomatología de la enfermedad de Alzheimer. Se postula que la memantina ejerce su efecto terapéutico mediante su acción como antagonista no competitivo (de canal abierto) de los receptores NMDA, de afinidad baja a moderada, que se une preferentemente a los canales catiónicos operados por receptores NMDA.» Texto original en inglés: "Persistent activation of central nervous system N-methyl-D-aspartate (NMDA) receptors by the excitatory amino acid glutamate has been hypothesized to contribute to the symptomatology of Alzheimer’s disease. Memantine is postulated to exert its therapeutic effect through its action as a low to moderate affinity uncompetitive (open-channel) NMDA receptor antagonist which binds preferentially to the NMDA receptor-operated cation channels." ([DailyMed: memantine hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e6977ef-6a0a-4bd9-b500-6ceb15abbd5e), versión del 2026-11-11; consultado el 2026-11-19). Según la información conocida, memantina actúa bloqueando el receptor NMDA de glutamato, y mecanísticamente podría ser aplicable a la hipertensión pulmonar solo de forma especulativa.

Un artículo preclínico sugiere que el eje glutamato/receptor NMDA se ha vinculado con lesión pulmonar aguda, hipertensión arterial pulmonar y diabetes. Sin embargo, ese trabajo estudia la sensibilidad a la insulina y el metabolismo lipídico, no a memantina en hipertensión pulmonar.

Ninguno de los estudios recuperados evalúa directamente memantina en esta enfermedad. El puntaje del modelo es alto, pero no está respaldado por evidencia clínica ni mecanística directa, por lo que el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclínico/mecanístico | Theranostics | La activación del receptor NMDA regula la sensibilidad a la insulina y el metabolismo lipídico; menciona de forma general el eje glutamato/NMDA en la hipertensión arterial pulmonar |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Fase 1 (PK/seguridad) | Clinical Drug Investigation | Farmacocinética y seguridad de MN-08, un derivado nitrato de memantina (compuesto distinto), en voluntarios sanos chinos; en desarrollo para hipertensión arterial pulmonar |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55079 | CARRIER XR | 21 mg comp. x 30 | No registrada |
| 51633 | NEUROPLUS XR | 7 mg comp. rec. lib. pro. x 30 | No registrada |
| 51921 | TONIBRAL XR | 14 mg cáps. x 30 | No registrada |
| 30251 | FENTINA | 10 mg comp. x 30 | No registrada |
| 45317 | CONEXINE 20 | 20 mg comp. rec. x 30 | No registrada |

La lista es parcial; existen al menos 20 autorizaciones vigentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - Moderadas: anticolinérgicos como hiosciamina, atropina, glicopirronio, clidinio, diciclomina, metscopolamina, propantelina, escopolamina, trospio y mepenzolato.
  - Menores: ranitidina, metformina, cimetidina y citrato de potasio.
  - De nivel desconocido: glimepirida, doxiciclina, lansoprazol, loperamida, famotidina y ácido acetilsalicílico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe directamente memantina en hipertensión pulmonar. Las dos publicaciones son tangenciales (una preclínica sobre metabolismo y otra sobre un compuesto distinto), por lo que el puntaje alto del modelo no tiene respaldo y la evidencia es L5.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen memantina en modelos de hipertensión pulmonar
- Datos del mecanismo de acción y su vínculo con la vasculatura pulmonar
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Revisión de las interacciones farmacológicas antes de cualquier ensayo clínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: memantine hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e6977ef-6a0a-4bd9-b500-6ceb15abbd5e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

