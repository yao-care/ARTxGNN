---
layout: default
title: Salmeterol
parent: Solo Predicción del Modelo (L5)
nav_order: 227
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-03
monitor_inn: "SALMETEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Salmeterol
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

## Salmeterol: malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Salmeterol es un agonista beta-2 adrenérgico de acción prolongada (broncodilatador inhalado) que se comercializa en Argentina en asociación con otros principios activos.
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria (respiratory malformation)**, pero la evidencia es muy limitada: **2 ensayos clínicos** relacionados solo de forma indirecta y **8 publicaciones** que no estudian directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Salmeterol (traducción no oficial): «El salmeterol es un LABA selectivo. Los estudios in vitro muestran que el salmeterol es al menos 50 veces más selectivo por los adrenorreceptores beta 2 que el albuterol. Aunque los adrenorreceptores beta 2 son los receptores adrenérgicos predominantes en el músculo liso bronquial y los adrenorreceptores beta 1 son los receptores predominantes en el corazón, también existen adrenorreceptores beta 2 en el corazón humano, que constituyen entre el 10% y el 50% del total de adrenorreceptores beta.» Texto original en inglés: "Salmeterol is a selective LABA. In vitro studies show salmeterol to be at least 50 times more selective for beta 2 -adrenoceptors than albuterol. Although beta 2 -adrenoceptors are the predominant adrenergic receptors in bronchial smooth muscle and beta 1 -adrenoceptors are the predominant receptors in the heart, there are also beta 2 -adrenoceptors in the human heart comprising 10% to 50% of the total beta-adrenoceptors." ([DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4), versión del 2022-10-10; consultado el 2026-11-19). Por su clase, salmeterol estimula los receptores beta-2 y produce broncodilatación sostenida; también hay estudios preclínicos que sugieren efectos sobre la función ciliar y la inflamación en otras enfermedades respiratorias.

El análisis no identificó un vínculo mecanístico claro con la malformación respiratoria. El puntaje alto del modelo probablemente refleja asociaciones compartidas con otras enfermedades respiratorias (como fibrosis quística o discinesia ciliar) y no un efecto terapéutico sobre una anomalía estructural.

La broncodilatación podría aliviar síntomas en algunas condiciones relacionadas, pero esto no está respaldado para las malformaciones en sí. La predicción debe considerarse solo una hipótesis computacional.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | No aplica | Suspendido | No disponible | Efecto a largo plazo de salmeterol vs. albuterol o placebo en fibrosis quística (6 meses, dos inhalaciones diarias); condición relacionada pero distinta, sin resultados |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | No aplica | Completado | 1 | Tratamiento del asma en el embarazo y resultados adversos del embarazo; no aborda malformación respiratoria |

## Evidencia de Literatura

Ninguna de las publicaciones estudia directamente la malformación respiratoria.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | ECA / revisión | JAMA Pediatrics | Corticoides inhalados solos o con beta-agonistas de acción prolongada para la función pulmonar reducida en niños nacidos prematuros |
| [15293609](https://pubmed.ncbi.nlm.nih.gov/15293609/) | 2004 | Estudio cruzado aleatorizado | Eur Respir J | Efecto de salmeterol sobre la respuesta ventilatoria al ejercicio en EPOC |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Revisión | Int J Chron Obstruct Pulmon Dis | Doble broncodilatación en el manejo de la EPOC |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Eficacia y seguridad de budesonida/formoterol en asma persistente |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Observacional | Respir Med | Frecuencia de batido ciliar disminuida en células nasales de pacientes con EPOC |
| [30021361](https://pubmed.ncbi.nlm.nih.gov/30021361/) | 2018 | In vitro | Biomed Pharmacother | Extracto de tomillo aumenta la frecuencia de batido ciliar en células de pacientes con EPOC |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Reporte de caso | Arerugi | Discinesia ciliar primaria tratada inicialmente como asma |
| [37327273](https://pubmed.ncbi.nlm.nih.gov/37327273/) | 2023 | Reporte de caso | Medicine | Infección pulmonar por Aspergillus tratada con omalizumab |

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de producto con un solo principio activo según los registros; la lista puede ser parcial. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43666 | PROAIR BRONQUIAL | 250/25 mcg aerosol x 120 dosis | No disponible en los datos |
| 54355 | VETALONE | 250/25 mcg aerosol x 120 dosis | No disponible en los datos |
| 45233 | PROAIR BRONQUIAL 500/50 | Cápsulas para inhalación x 60 + aplicador | No disponible en los datos |
| 47968 | FLUTIVENT HFA | 250/25 mcg x 120 dosis | No disponible en los datos |
| 26250 | SERETIDE DISKUS | 50/500 mcg x 60 dosis | No disponible en los datos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; ejemplos principales):
  - Mayor: claritromicina.
  - Moderadas: epinefrina, acarbosa, famotidina, isometepteno, albiglutida, alogliptina, canagliflozina, dapagliflozina, empagliflozina, dulaglutida, clorpropamida, dietilpropión, dolasetrón.
  - Menores: corticoides como hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona y budesonida.

Para advertencias y contraindicaciones consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado aborda directamente la malformación respiratoria, el vínculo mecanístico no es claro y el puntaje alto del modelo parece reflejar asociaciones con otras enfermedades respiratorias. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un fundamento biológico plausible para una anomalía estructural.
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad.
- Revisión del prospecto aprobado en Argentina para advertencias y contraindicaciones.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

