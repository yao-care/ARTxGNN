---
layout: default
title: Paroxetina
parent: Solo Predicción del Modelo (L5)
nav_order: 292
evidence_level: L5
indication_count: 1
drugbank_id: DB00715
monitor_inn: "Paroxetine"
predicted_indications: ["Ohdo syndrome and variants"]
last_modified_at: 2026-11-16
description: "Paroxetina: nueva indicación predicha, Síndrome de Ohdo y variantes (Ohdo syndrome and variants) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Paroxetina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Paroxetina: Síndrome de Ohdo y variantes (Ohdo syndrome and variants)
{: .text-alpha }

## Resumen en Una Frase

Paroxetina es un fármaco comercializado en Argentina que pertenece a la clase de los inhibidores selectivos de la recaptación de serotonina (ISRS).
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Ohdo y variantes (Ohdo syndrome and variants)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes (Ohdo syndrome and variants) |
| Puntaje de Predicción TxGNN | 0.9911 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Paroxetina (traducción no oficial): «Se desconoce el mecanismo de acción de PAXIL CR en el tratamiento del trastorno depresivo mayor (TDM), el trastorno de pánico (TP), el trastorno de ansiedad social (TAS) y el trastorno disfórico premenstrual (TDPM), pero se presume que está relacionado con la potenciación de la actividad serotoninérgica en el sistema nervioso central como resultado de la inhibición de la recaptación neuronal de serotonina (5-HT).» Texto original en inglés: "The mechanism of action of PAXIL CR in the treatment of major depressive disorder (MDD), panic disorder (PD), social anxiety disorder (SAD), and premenstrual dysphoric disorder (PMDD) is unknown, but is presumed to be linked to potentiation of serotonergic activity in the central nervous system resulting from inhibition of neuronal reuptake of serotonin (5-HT)." ([DailyMed: Paxil Cr (paroxetine hydrochloride) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=483bd97f-c4d0-4e23-aaa8-6334f4471e0c), versión del 2026-09-30; consultado el 2026-11-19). Según la información conocida, la paroxetina es un ISRS: inhibe el transportador de serotonina (SERT) y, de forma secundaria, se ha descrito un efecto sobre la quinasa GRK2.

El síndrome de Ohdo (incluida la variante Say-Barber-Biesecker-Young-Simpson, asociada a variantes de KAT6B) es un trastorno congénito raro que cursa con discapacidad intelectual, blefarofimosis e hipotonía. Con los datos disponibles no se ha podido establecer un puente mecanístico plausible entre la farmacología de los ISRS y la patología de KAT6B, vinculada a la acetilación de cromatina.

El puntaje alto (0,9911) es una inferencia computacional, no evidencia clínica. Podría reflejar artefactos de proximidad en una red poco densa de enfermedades raras, por ejemplo genes o fenotipos del neurodesarrollo compartidos. Por ello, la razonabilidad biológica de esta predicción es baja por ahora.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

La lista de autorizaciones puede ser parcial: hay al menos 20 autorizaciones y todas las listadas están vigentes. A continuación se muestran las principales (el texto de indicación aprobada no está registrado en los datos locales).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 59864 | TIARIX | 20 mg comprimidos x 60 | Casasco |
| 28151 | PSICOASTEN 10 MG | 10 mg comprimidos recubiertos x 30 | Beta |
| 24495 | PAMOXET | 40 mg comprimidos x 30 | Megalabs Argent |
| 31882 | NEUROTROX | 20 mg comprimidos x 30 | Elea |
| 14153 | AROPAX | 20 mg comprimidos recubiertos x 30 | GlaxoSmithKline |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como punto de atención, la paroxetina tiene preocupaciones conocidas de seguridad en el embarazo (riesgo de malformaciones cardíacas congénitas), lo cual es relevante para una población con un trastorno del desarrollo congénito.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la predicción es un puntaje computacional alto, sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la paroxetina y un análisis de posibles vínculos con la vía KAT6B/acetilación de cromatina
- Estudios preclínicos o series de casos que evalúen directamente el síndrome de Ohdo
- Prospecto de ANMAT con advertencias y contraindicaciones para el cribado de seguridad
- Evaluación del perfil de seguridad en poblaciones pediátricas y con trastornos del desarrollo

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Paxil Cr (paroxetine hydrochloride) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=483bd97f-c4d0-4e23-aaa8-6334f4471e0c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

