---
layout: default
title: Verapamil
parent: Solo Predicción del Modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 6
monitor_inn: "verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
last_modified_at: 2026-11-20
description: "Verapamil: nueva indicación predicha, Bloqueo de rama obsoleto (obsolete bundle branch block) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Verapamil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Verapamilo: bloqueador de canales de calcio tipo L → bloqueo de rama obsoleto (obsolete bundle branch block)
{: .text-alpha }

## Resumen en Una Frase

Verapamilo es un bloqueador de los canales de calcio tipo L que se comercializa actualmente en Argentina.
El modelo TxGNN predice que podría ser efectivo para **bloqueo de rama obsoleto (obsolete bundle branch block)**, pero no hay ensayos clínicos ni publicaciones que respalden esta dirección, por lo que se trata solo de una predicción del modelo. Además, el término de la enfermedad está marcado como obsoleto, lo que sugiere un artefacto de la ontología.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bloqueo de rama obsoleto (obsolete bundle branch block) |
| Puntaje de Predicción TxGNN | 0,9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Verapamil (traducción no oficial): «Angina: El mecanismo de acción preciso del clorhidrato de verapamilo como agente antianginoso aún no se ha determinado por completo, pero incluye los dos mecanismos siguientes: 1. Relajación y prevención del espasmo de las arterias coronarias: El clorhidrato de verapamilo dilata las arterias coronarias principales y las arteriolas coronarias, tanto en las regiones normales como en las isquémicas, y es un potente inhibidor del espasmo de las arterias coronarias, ya sea espontáneo o inducido por ergonovina.» Texto original en inglés: "Angina: The precise mechanism of action of verapamil hydrochloride as an antianginal agent remains to be fully determined, but includes the following two mechanisms: 1. Relaxation and prevention of coronary artery spasm: Verapamil hydrochloride dilates the main coronary arteries and coronary arterioles, both in normal and ischemic regions, and is a potent inhibitor of coronary artery spasm, whether spontaneous or ergonovine-induced." ([DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c), versión del 2026-10-30; consultado el 2026-11-19). Según la información conocida, el verapamilo bloquea los canales de calcio tipo L y enlentece la conducción en el nodo auriculoventricular.

El bloqueo de rama compromete la conducción infranodal (sistema His-Purkinje), donde el bloqueo de canales de calcio no se espera que ayude y podría empeorar los trastornos de conducción. El puntaje alto parece reflejar la cercanía en el modelo con indicaciones de arritmias, y no un efecto terapéutico plausible.

En conjunto, la predicción carece de respaldo mecanístico y clínico. Debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 23137 | VERAL | rtd. 240 mg comp. x 30 |
| 20438 | ISOPTINO | 80 mg comp. rec. x 30 |
| 2141 | ISOPTINO MD | 240 mg comp. rec. x 30 |
| 4642 | ISOPTINO RETARD | 120 mg comp. rec. x 20 |

Las cuatro autorizaciones figuran como vigentes y corresponden a productos de un solo principio activo.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron 328 interacciones. Entre las principales figuran la loperamida (nivel mayor) y, con nivel moderado, hidrocortisona, metformina, bupropión, aprepitant, ácido acetilsalicílico, dexametasona, cimetidina y claritromicina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe verapamilo en esta enfermedad, el término está marcado como obsoleto y el mecanismo de acción del fármaco no sugiere beneficio en el bloqueo infranodal; incluso podría empeorar la conducción.

**Para avanzar se necesita:**
- Confirmar si el término de la enfermedad corresponde a un artefacto de la ontología o a una entidad clínica vigente
- Datos del mecanismo de acción y del prospecto aprobado en Argentina (advertencias y contraindicaciones)
- Evidencia preclínica o clínica que estudie directamente esta enfermedad antes de reconsiderar la decisión

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

