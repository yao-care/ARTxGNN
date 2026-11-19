---
layout: default
title: Heparin
parent: Solo Predicción del Modelo (L5)
nav_order: 157
evidence_level: L5
indication_count: 2
monitor_inn: "heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
last_modified_at: 2026-10-30
description: "Heparin: nueva indicación predicha, trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency… (nivel de evidencia L5). Indicación original: No consta …"
---

# Heparin
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

## Heparina: anticoagulante que potencia la antitrombina → trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive)
{: .text-alpha }

## Resumen en Una Frase

La heparina es un anticoagulante que actúa potenciando la antitrombina e inhibiendo la trombina y el factor Xa.
El modelo TxGNN predice que podría ser útil para **trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive) |
| Puntaje de Predicción TxGNN | 0,9929 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Heparin (traducción no oficial): «La heparina interactúa con la proteína plasmática de origen natural antitrombina III e induce un cambio conformacional que potencia notablemente la actividad inhibidora de serina proteasas de la antitrombina III, con lo que inhibe los factores de coagulación activados que participan en la secuencia final, en particular Xa y IIa. Pequeñas cantidades de heparina inhiben el factor Xa, y cantidades mayores inhiben la trombina (factor IIa).» Texto original en inglés: "Heparin interacts with the naturally occurring plasma protein, antithrombin III, to induce a conformational change, which markedly enhances the serine protease activity of antithrombin III, thereby inhibiting the activated coagulation factors involved in the closing sequence, particularly Xa and IIa. Small amounts of heparin inhibit Factor Xa, and larger amounts inhibit thrombin (Factor IIa)." ([DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e), versión del 2026-05-25; consultado el 2026-11-19). Según el conocimiento general, la heparina potencia la antitrombina e inhibe la trombina y el factor Xa, lo que reduce la generación de trombina.

La deficiencia grave congénita de proteína C provoca una generación descontrolada de trombina y trombosis microvascular (por ejemplo, púrpura fulminante neonatal). Como la heparina actúa sobre esa misma vía de coagulación, existe una justificación mecanística plausible. El puntaje elevado (0,9929) probablemente refleja esa cercanía fisiopatológica.

Sin embargo, no se recuperaron ensayos ni literatura que apoyen la predicción. En la práctica, la anticoagulación en esta deficiencia suele manejarse con reposición de proteína C y/o antagonistas de la vitamina K, por lo que el valor añadido de la heparina no está verificado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42347 | HEPATRIET | gel tópico x 60 g | No registrada en los datos locales |
| 44887 | CYCLOPARIN | gel tópico x 60 g | No registrada en los datos locales |

Ambas autorizaciones están vigentes y corresponden a formulaciones tópicas (gel), no a presentaciones sistémicas.

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (614 interacciones registradas; principales de nivel moderado):
- Ácido acetilsalicílico
- Antidiabéticos: clorpropamida, glimepirida, repaglinida, nateglinida, tolazamida, glipizida, gliburida, acetohexamida, tolbutamida
- Anorexígenos: fenfluramina, dexfenfluramina, sibutramina

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones que estudien esta enfermedad. Además, las únicas presentaciones locales son geles tópicos, que no son compatibles con el uso sistémico necesario para esta condición.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos de heparina en deficiencia grave de proteína C
- Comparación con el tratamiento estándar (reposición de proteína C, antagonistas de la vitamina K)
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones)
- Evaluación de la disponibilidad de una formulación sistémica en Argentina

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

