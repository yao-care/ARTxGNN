---
layout: default
title: Donepezil
parent: Solo Predicción del Modelo (L5)
nav_order: 130
evidence_level: L5
indication_count: 8
monitor_inn: "donepezil"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "extrapyramidal and movement disease", "benign shuddering attacks", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "lingual-facial-buccal dyskinesia"]
last_modified_at: 2026-11-20
description: "Donepezil: nueva indicación predicha, Trastornos del movimiento psicógenos (psychogenic movement disorders) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Donepezil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Donepezilo: inhibidor de la acetilcolinesterasa → trastornos del movimiento psicógenos (psychogenic movement disorders)
{: .text-alpha }

## Resumen en Una Frase

Donepezilo es un inhibidor de la acetilcolinesterasa que se comercializa en Argentina con varias autorizaciones vigentes.
El modelo TxGNN predice que podría ser efectivo para **trastornos del movimiento psicógenos (psychogenic movement disorders)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastornos del movimiento psicógenos (psychogenic movement disorders) |
| Puntaje de Predicción TxGNN | 0,9923 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Donepezil (traducción no oficial): «Las teorías actuales sobre la patogenia de los signos y síntomas cognitivos de la enfermedad de Alzheimer atribuyen algunos de ellos a una deficiencia de la neurotransmisión colinérgica. Se postula que el clorhidrato de donepezilo ejerce su efecto terapéutico al potenciar la función colinérgica.» Texto original en inglés: "Current theories on the pathogenesis of the cognitive signs and symptoms of Alzheimer’s disease attribute some of them to a deficiency of cholinergic neurotransmission. Donepezil hydrochloride is postulated to exert its therapeutic effect by enhancing cholinergic function." ([DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975), versión del 2021-12-30; consultado el 2026-11-19). Por su clase, donepezilo inhibe la acetilcolinesterasa y aumenta la disponibilidad de acetilcolina en el sistema nervioso central.

Una hipótesis posible es que la modulación colinérgica de los circuitos de los ganglios basales influya en la expresión de movimientos anormales. Sin embargo, esta idea es especulativa: los trastornos del movimiento psicógenos son de naturaleza funcional, por lo que el vínculo farmacológico directo no está claro.

El puntaje de TxGNN es alto, pero refleja solo una predicción computacional. No se recuperaron estudios que evalúen directamente esta enfermedad, por lo que el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El estado de mercado es **Comercializado**. Se registraron al menos 20 autorizaciones vigentes de productos con donepezilo como único principio activo; la lista puede ser parcial. Entre ellas:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54878 | LUPRACIL | 10 mg comp. rec. x 60 | No registrada en los datos locales |
| 33064 | ENDOCLAR | 10 mg comp. rec. ran. x 30 | No registrada en los datos locales |
| 26562 | AUROBRAL | 5 mg comp. x 30 | No registrada en los datos locales |
| 25867 | VALPEX | 10 mg comp. rec. x 30 | No registrada en los datos locales |
| 54875 | LUPRACIL | 5 mg comp. rec. x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 257 interacciones en total. Entre las principales:
  - Gravedad mayor: bupropión.
  - Gravedad moderada: famotidina, ranitidina, cimetidina, hiosciamina, atropina, glicopirronio, clidinio, diciclomina, loperamida, dexametasona, metronidazol y dolasetrón, entre otros (varios anticolinérgicos, cuyo efecto puede oponerse al de donepezilo).
  - Gravedad menor: aprepitant, ácido acetilsalicílico, lorcaserina y claritromicina.
- Los datos compilados señalan además que los inhibidores de la colinesterasa pueden asociarse con trastornos del movimiento (por ejemplo, distonía), lo que debe considerarse en una indicación que involucra movimientos anormales.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9923), pero no cuenta con ensayos clínicos ni literatura, y el vínculo mecanístico es poco claro para un trastorno de naturaleza funcional. Por ello solo alcanza el nivel L5.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre donepezilo en trastornos del movimiento funcionales/psicógenos.
- Datos de mecanismo de acción y análisis de la plausibilidad mecanística.
- Obtención y análisis del prospecto de ANMAT (advertencias y contraindicaciones).
- Evaluación del riesgo-beneficio, considerando los reportes de trastornos del movimiento asociados a inhibidores de la colinesterasa, antes de cualquier estudio exploratorio.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Aricept (donepezil hydrochloride) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e451e1-e4d7-4439-a675-c5457ba20975) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

