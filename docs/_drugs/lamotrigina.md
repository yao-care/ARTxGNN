---
layout: default
title: Lamotrigina
parent: Solo Predicción del Modelo (L5)
nav_order: 224
evidence_level: L5
indication_count: 2
drugbank_id: DB00555
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
last_modified_at: 2026-11-16
description: "Lamotrigina: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Lamotrigina
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

## Lamotrigina: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Lamotrigina es un fármaco antiepiléptico que bloquea los canales de sodio dependientes de voltaje y reduce la liberación de glutamato.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino (trigeminal nerve neoplasm)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lamotrigina bloquea los canales de sodio dependientes de voltaje de manera uso-dependiente y reduce la liberación de glutamato. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lamotrigina (traducción no oficial): «Se desconoce(n) el(los) mecanismo(s) preciso(s) mediante el(los) cual(es) la lamotrigina ejerce su acción anticonvulsiva. En modelos animales diseñados para detectar actividad anticonvulsiva, la lamotrigina fue eficaz para prevenir la propagación de las convulsiones en las pruebas de electrochoque máximo (MES) y de pentilentetrazol (scMet), y previno las convulsiones en las pruebas de posdescarga evocada visual y eléctricamente (EEAD) para la actividad antiepiléptica.» Texto original en inglés: "The precise mechanism(s) by which lamotrigine exerts its anticonvulsant action are unknown. In animal models designed to detect anticonvulsant activity, lamotrigine was effective in preventing seizure spread in the maximum electroshock (MES) and pentylenetetrazol (scMet) tests, and prevented seizures in the visually and electrically evoked after-discharge (EEAD) tests for antiepileptic activity." ([DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4), versión del 2026-10-12; consultado el 2026-11-19).

El puntaje muy alto (0,9997) probablemente refleja la cercanía en la red del modelo con la neuralgia del trigémino, un síntoma de las lesiones del nervio trigémino, y no un mecanismo antineoplásico. Este mecanismo podría aliviar el dolor neuropático asociado a una neoplasia, pero no hay ninguna evidencia de efecto sobre la biología del tumor.

En consecuencia, la predicción debe interpretarse con mucha cautela: es una señal del modelo, sin respaldo clínico ni bibliográfico directo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones registradas (la lista puede ser parcial), todas vigentes y de producto de un solo principio activo. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 39062 | LATRIGIN 100 | comp. dispersable x 30 | No registrada en los datos locales |
| 41442 | LAMOCAS | 50 mg comp. dispersable x 30 | No registrada en los datos locales |
| 50171 | LAMIRAX | 100 mg comp. dispersable x 60 | No registrada en los datos locales |
| 21953 | LAMICTAL DISPERSABLE | 25 mg comp. x 30 | No registrada en los datos locales |
| 33277 | EPILEPAX | 25 mg comp. dispersable x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad, y el puntaje alto parece derivarse de la proximidad con la neuralgia del trigémino y no de un efecto antitumoral. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen directamente un efecto de lamotrigina en la neoplasia del nervio trigémino
- Datos del mecanismo de acción que sustenten un vínculo con la biología tumoral
- Información de advertencias y contraindicaciones del prospecto de ANMAT para completar el análisis de seguridad
- Aclarar si el objetivo real es el control del dolor neuropático asociado, lo que correspondería evaluar como otra pregunta de investigación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

