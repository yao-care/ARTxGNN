---
layout: default
title: Levotiroxina
parent: Solo Predicción del Modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 4
drugbank_id: DB00451
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-11-20
description: "Levotiroxina: nueva indicación predicha, hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Levotiroxina
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

## Levotiroxina: hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)
{: .text-alpha }

## Resumen en Una Frase

Levotiroxina es una forma sintética de la hormona tiroidea tiroxina (T4), comercializada en Argentina en comprimidos e inyectable.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Levotiroxina (traducción no oficial): «Las hormonas tiroideas ejercen sus acciones fisiológicas mediante el control de la transcripción del DNA y de la síntesis de proteínas. La triyodotironina (T3) y la L-tiroxina (T4) difunden al núcleo celular y se unen a proteínas receptoras tiroideas unidas al DNA.» Texto original en inglés: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174), versión del 2026-11-06; consultado el 2026-11-19). Según la información conocida, la levotiroxina es un reemplazo de la hormona tiroidea que participa en el desarrollo y la maduración de múltiples órganos, incluido el riñón.

Sin embargo, la hipodisplasia/aplasia renal es una malformación estructural congénita, habitualmente de origen genético (por ejemplo, PAX2, HNF1B, RET). No se espera que la levotiroxina administrada después del nacimiento revierta un defecto del desarrollo ya establecido.

Por lo tanto, el vínculo mecanístico es especulativo y no se identifica un mecanismo terapéutico plausible. El puntaje alto del modelo (0,9967) refleja una predicción computacional, no un efecto de tratamiento demostrado.

## Información de Mercado en Argentina

Se registran al menos 20 autorizaciones vigentes de producto de un solo principio activo (la lista puede ser parcial). Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42758 | EUTHYROX | 88 mcg, comprimidos birranurados x 50 | No registrada en los datos locales |
| 39848 | T4 MONTPELLIER 175 | 175 mcg, comprimidos x 50 | No registrada en los datos locales |
| 38312 | T4 MONTPELLIER | 200 mcg, inyectable x 1 ml | No registrada en los datos locales |
| 26920 | LEVOTIROXINA GSK | 175 mcg, comprimidos x 50 | No registrada en los datos locales |
| 33625 | T4 MONTPELLIER 50 | 50 mcg, comprimidos x 50 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que estudien la levotiroxina en hipodisplasia/aplasia renal, y el razonamiento biológico indica que un reemplazo hormonal no corregiría una malformación estructural congénita. La predicción se sustenta únicamente en el modelo (nivel L5).

**Para avanzar se necesita:**
- Evidencia clínica o preclínica que estudie directamente esta enfermedad
- Datos del mecanismo de acción y una hipótesis mecanística plausible
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Revisión de la ruta de administración y de la población objetivo (por ejemplo, uso fetal o neonatal)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

