---
layout: default
title: Benazepril
parent: Solo Predicción del Modelo (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-10-30
description: "Benazepril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 12 (en el listado vigente: 12)"
---

# Benazepril
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

## Benazepril: inhibidor de la enzima convertidora de angiotensina (IECA) → Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Benazepril es un inhibidor de la enzima convertidora de angiotensina (IECA) que se comercializa en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados para este informe que respalden esta dirección; el apoyo se basa solo en el puntaje del modelo y en un razonamiento indirecto de clase.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9965 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (12 de 12) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 12 (vigentes: 12) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Benazepril (traducción no oficial): «El benazepril y el benazeprilato inhiben la enzima convertidora de angiotensina (ECA) en seres humanos y en animales. El benazeprilato tiene una actividad inhibidora de la ECA mucho mayor que la del benazepril. La ECA es una peptidil dipeptidasa que cataliza la conversión de la angiotensina I en la sustancia vasoconstrictora angiotensina II.» Texto original en inglés: "Benazepril and benazeprilat inhibit angiotensin-converting enzyme (ACE) in human subjects and animals. Benazeprilat has much greater ACE inhibitory activity than does benazepril. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e), versión del 2025-09-30; consultado el 2026-11-19). Según la información conocida, benazepril pertenece a la clase de los IECA, que reducen la activación del sistema renina-angiotensina-aldosterona (SRAA) y, con ello, la presión arterial.

La enfermedad renal hipertensiva maligna (nefroesclerosis maligna) está impulsada por elevaciones muy intensas de la presión arterial y por la activación del SRAA. Por eso, mecanísticamente, un fármaco que bloquea este sistema podría ser aplicable. Los IECA también se usan ampliamente por su efecto protector renal.

Esta justificación es solo un razonamiento indirecto de clase. No hay estudios compilados que evalúen benazepril en esta enfermedad, por lo que el nivel de evidencia se mantiene en L5 (solo predicción del modelo).

## Información de Mercado en Argentina

Hay 12 autorizaciones vigentes, todas de productos con asociación a dosis fija (presentaciones con dos concentraciones, p. ej. 5/10 mg). Los datos locales no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 36106 | ILDUC DUO | 5/10 mg cáps. x 30 |
| 31897 | ARTERIOSAN PLUS | 5/10 mg cáps. x 30 |
| 46167 | ARTERIOSAN PLUS | 5/20 mg cáps. x 30 |
| 36107 | ILDUC DUO | 2.5/10 mg cáps. x 30 |
| 39462 | ILDUC DUO | 5/20 mg cáps. x 30 |

La lista muestra las 5 autorizaciones principales de un total de 12.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las primeras listadas son de nivel moderado e incluyen hidrocortisona, antidiabéticos (alogliptina, acetohexamida, clorpropamida, dapagliflozina, exenatida, glimepirida, glipizida, gliburida) y varias insulinas (humana, aspart, degludec, detemir, glargina, glulisina, lispro). Esto sugiere vigilar la glucemia ante el uso conjunto con tratamientos antidiabéticos.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no hay datos de etiqueta disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que estudien directamente benazepril en enfermedad renal hipertensiva maligna. El puntaje alto de TxGNN (0.9965) y el razonamiento de clase no bastan para avanzar.

**Para avanzar se necesita:**
- Revisión de la literatura y de ensayos sobre IECA en nefroesclerosis maligna y enfermedad renal hipertensiva
- Datos detallados del mecanismo de acción (MOA) de benazepril
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones), en especial para pacientes con insuficiencia renal, dado el riesgo de empeoramiento de la función renal y de hiperpotasemia
- Texto de indicación aprobada en los registros locales
- Evaluación de la relación riesgo-beneficio en pacientes con hipertensión maligna, que suelen requerir manejo hospitalario

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

