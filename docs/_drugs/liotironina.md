---
layout: default
title: Liotironina
parent: Solo Predicción del Modelo (L5)
nav_order: 236
evidence_level: L5
indication_count: 9
drugbank_id: DB00279
monitor_inn: "Liothyronine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "angiomyxoma", "myxoma", "hypotrichosis simplex of the scalp"]
last_modified_at: 2026-11-24
description: "Liotironina: nueva indicación predicha, hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Liotironina
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

## Liotironina: hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)
{: .text-alpha }

## Resumen en Una Frase

Liotironina es la forma sintética de la triyodotironina (T3), una hormona tiroidea de uso clínico en Argentina.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)**.
No hay **ningún ensayo clínico** ni **ninguna publicación** que estudie directamente esta enfermedad, por lo que la predicción no tiene respaldo experimental ni clínico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Liotironina (traducción no oficial): «Las hormonas tiroideas ejercen sus acciones fisiológicas mediante el control de la transcripción del DNA y de la síntesis de proteínas. La triyodotironina (T3) y la L-tiroxina (T4) difunden al núcleo celular y se unen a proteínas receptoras tiroideas unidas al DNA.» Texto original en inglés: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3), versión del 2026-05-18; consultado el 2026-11-19). Según la información conocida, la liotironina es una hormona tiroidea que actúa sobre los receptores nucleares de hormona tiroidea y regula el metabolismo y el desarrollo de varios tejidos.

Un vínculo biológico posible es que la señalización de hormonas tiroideas participa en el desarrollo renal. Sin embargo, la hipodisplasia y la aplasia renal son malformaciones congénitas estructurales que se establecen durante la vida fetal. Es poco probable que un tratamiento posnatal con liotironina las revierta.

El puntaje alto del modelo (0,9995) probablemente refleja una cercanía en las anotaciones de genes o fenotipos compartidos, y no un mecanismo terapéutico demostrado. La predicción debe interpretarse como una hipótesis sin respaldo, no como una indicación plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 54595 | T3 MONTPELLIER 20 | comp.x 30 | Montpellier | Vigente |

La tabla muestra el único producto de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Esta autorización corresponde a un producto de un solo principio activo y se encuentra vigente.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. En los datos compilados no se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe la liotironina en hipodisplasia/aplasia renal. La enfermedad es una malformación congénita sin mecanismo creíble de respuesta a una hormona tiroidea administrada después del nacimiento. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la liotironina.
- Evidencia preclínica o clínica que estudie directamente esta enfermedad y justifique un vínculo mecanístico.
- Información de seguridad del prospecto aprobado en Argentina (advertencias y contraindicaciones).
- Evaluación de la vía de administración y de la población, ya que la enfermedad es principalmente prenatal.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

