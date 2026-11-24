---
layout: default
title: Tropicamida
parent: Solo Predicción del Modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 3
drugbank_id: DB00809
monitor_inn: "Tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
last_modified_at: 2026-11-24
description: "Tropicamida: nueva indicación predicha, síndrome de la cola de caballo (cauda equina syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 3 (en el listado vigente: 3)"
---

# Tropicamida
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Tropicamida: síndrome de la cola de caballo (cauda equina syndrome)
{: .text-alpha }

## Resumen en Una Frase

Tropicamida es un antagonista muscarínico de uso oftálmico tópico, empleado para producir midriasis y cicloplejía.
El modelo TxGNN predice que podría ser efectivo para **síndrome de la cola de caballo (cauda equina syndrome)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | síndrome de la cola de caballo (cauda equina syndrome) |
| Puntaje de Predicción TxGNN | 0.9953 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La tropicamida es un antagonista muscarínico no selectivo (M1–M5) que se usa en el ojo. Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tropicamida (traducción no oficial): «Esta preparación anticolinérgica bloquea las respuestas del músculo esfínter del iris y del músculo ciliar a la estimulación colinérgica, lo que dilata la pupila (midriasis). La preparación más concentrada (1%) también paraliza la acomodación.» Texto original en inglés: "This anticholinergic preparation blocks the responses of the sphincter muscle of the iris and the ciliary muscle to cholinergic stimulation, dilating the pupil (mydriasis). The stronger preparation (1%) also paralyzes accommodation." ([DailyMed: Mydriacyl (tropicamide) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4f4a2e-eb00-4c65-b3fa-baf5738d468d), versión del 2023-02-15; consultado el 2026-11-19).

El puntaje del modelo es muy alto (0,9953), pero probablemente refleja la cercanía en la red con fármacos anticolinérgicos usados en la disfunción neurogénica de vejiga o intestino asociada al síndrome de la cola de caballo. No hay datos clínicos ni mecanísticos que respalden a la tropicamida para la patología neurológica de fondo.

El síndrome de la cola de caballo es una emergencia quirúrgica cuyo tratamiento es la descompresión. Un eventual papel farmacológico se limitaría al manejo sintomático de la disfunción vesical. Además, la tropicamida está formulada y autorizada solo como agente oftálmico, con exposición sistémica mínima, por lo que un efecto anticolinérgico sistémico no está establecido.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 138 | ALCON MYDRIL | 1% sol.oft.x 5 ml | Alcon | Vigente |
| 44489 | MIDRIAX-T | gts.oft.x 5 ml | Klonal | Vigente |
| 31702 | TROPIOFTAL F | sol.oft.x 5 ml | Denver Farma | Vigente |

La tabla muestra los 3 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y la tropicamida solo se comercializa como solución oftálmica con exposición sistémica mínima. El síndrome de la cola de caballo requiere cirugía de descompresión, por lo que el papel de un fármaco sería, como máximo, sintomático.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la tropicamida.
- Advertencias y contraindicaciones del prospecto de ANMAT.
- Caracterización de la exposición sistémica y de la vejiga tras la administración.
- Estudios que evalúen directamente esta enfermedad.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mydriacyl (tropicamide) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4f4a2e-eb00-4c65-b3fa-baf5738d468d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

