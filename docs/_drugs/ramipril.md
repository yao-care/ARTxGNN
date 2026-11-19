---
layout: default
title: Ramipril
parent: Solo Predicción del Modelo (L5)
nav_order: 222
evidence_level: L5
indication_count: 9
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
last_modified_at: 2026-10-30
description: "Ramipril: nueva indicación predicha, Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia) (nivel de evidencia L5). Indicación origin…"
---

# Ramipril
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

## Ramipril: inhibidor de la enzima convertidora de angiotensina (ECA) → hipertensión pulmonar por enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia)
{: .text-alpha }

## Resumen en Una Frase

Ramipril es un inhibidor de la enzima convertidora de angiotensina (ECA) que se comercializa en Argentina.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar por enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia)**,
pero actualmente no hay ensayos clínicos registrados y solo existe un estudio preclínico en ratas que aborda directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia (pulmonary hypertension owing to lung disease and/or hypoxia) |
| Puntaje de Predicción TxGNN | 0,9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (9 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ramipril (traducción no oficial): «El ramipril y el ramiprilato inhiben la ECA en seres humanos y en animales. La enzima convertidora de angiotensina es una peptidil dipeptidasa que cataliza la conversión de la angiotensina I en la sustancia vasoconstrictora angiotensina II. La angiotensina II también estimula la secreción de aldosterona por la corteza suprarrenal.» Texto original en inglés: "Ramipril and ramiprilat inhibit ACE in human subjects and animals. Angiotensin converting enzyme is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II. Angiotensin II also stimulates aldosterone secretion by the adrenal cortex." ([DailyMed: ramipril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=245d3580-77c6-4c0f-b324-c8514b792c59), versión del 2026-11-11; consultado el 2026-11-19). Con base en el conocimiento general, ramipril inhibe la ECA y reduce la formación de angiotensina II, un vasoconstrictor que participa en la remodelación vascular.

Un estudio preclínico de 1996 (PMID 9200213) en ratas expuestas a hipoxia crónica durante tres semanas y tratadas con ramipril (10 mg/kg diarios) mostró menor presión de perfusión basal en el pulmón aislado. Esto sugiere que la inhibición de la ECA atenúa los efectos de la hipoxia crónica sobre los vasos pulmonares, lo que respalda el vínculo mecanístico con esta predicción.

Sin embargo, el resto de los artículos recuperados tratan temas indirectamente relacionados (infarto de miocardio, pérdida capilar renal, necrosis cerebral por radiación, entre otros). No hay evidencia en humanos, y el puntaje elevado del modelo es solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclínico (animal) | Physiological research | En ratas con hipoxia crónica, ramipril redujo la presión de perfusión pulmonar basal y atenuó los efectos de la hipoxia sobre los vasos pulmonares |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclínico (animal) | Am J Physiol Regul Integr Comp Physiol | Función cardíaca ante hipoxia-reoxigenación en ratas transgénicas con renina-angiotensinógeno; relación indirecta |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclínico/tejido humano | Eur Heart J | Aumento de la expresión de ECA2 tras infarto de miocardio en ratas y humanos; relación indirecta |
| [19380417](https://pubmed.ncbi.nlm.nih.gov/19380417/) | 2009 | Preclínico (animal) | Cardiovasc Res | La inhibición de la ECA favorece las células progenitoras endoteliales en sobrecarga de presión cardíaca; relación indirecta |
| [18464162](https://pubmed.ncbi.nlm.nih.gov/18464162/) | 2008 | Preclínico (animal) | Microcirculation | Ramipril o valsartán atenúan la pérdida de capilares peritubulares; relación indirecta |
| [24907870](https://pubmed.ncbi.nlm.nih.gov/24907870/) | 2014 | Preclínico (animal) | Basic Res Cardiol | Activación de guanilil ciclasa soluble tras infarto frente a inhibición de la ECA; relación indirecta |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21981 | LOSTAPRES | 2.5 mg comp. x 30 | No registrada en los datos locales |
| 45497 | TRITACE | 10 mg comp. x 30 | No registrada en los datos locales |
| 20465 | TRITACE | 2.5 mg comp. x 30 | No registrada en los datos locales |
| 47211 | LOSTAPRES | 10 mg comp. x 30 | No registrada en los datos locales |
| 20467 | TRITACE | 5 mg comp. x 30 | No registrada en los datos locales |

Las 9 autorizaciones registradas están vigentes; se listan las 5 principales.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; ejemplos):
  - Mayor: citrato de potasio, bicarbonato de potasio.
  - Moderada: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, ácido acetilsalicílico, morfina, bupropión, metformina, glimepirida, alogliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.

No se dispone de advertencias ni contraindicaciones extraídas del prospecto; consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un único estudio preclínico en ratas sobre hipoxia crónica y no existen ensayos clínicos ni estudios en humanos. El puntaje del modelo (0,9993) es una predicción computacional y no sustituye evidencia clínica.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Revisión del prospecto de ANMAT (advertencias y contraindicaciones), aún pendiente
- Estudios preclínicos adicionales y, de ser posibles, estudios clínicos en pacientes con hipertensión pulmonar asociada a enfermedad pulmonar o hipoxia
- Evaluación de seguridad en esta población, especialmente en cuanto a hipotensión y función renal

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ramipril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=245d3580-77c6-4c0f-b324-c8514b792c59) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

