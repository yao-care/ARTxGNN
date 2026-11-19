---
layout: default
title: Glimepiride
parent: Solo Predicción del Modelo (L5)
nav_order: 153
evidence_level: L5
indication_count: 9
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-30
description: "Glimepiride: nueva indicación predicha, Síndrome de la persona rígida clásica (classic stiff person syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Glimepiride
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

## Glimepirida: sulfonilurea hipoglucemiante → síndrome de la persona rígida clásica (classic stiff person syndrome)
{: .text-alpha }

## Resumen en Una Frase

Glimepirida es una sulfonilurea que se comercializa en Argentina con numerosas autorizaciones vigentes.
El modelo TxGNN predice que podría ser efectiva para **síndrome de la persona rígida clásica (classic stiff person syndrome)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásica (classic stiff person syndrome) |
| Puntaje de Predicción TxGNN | 0,9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Glimepiride (traducción no oficial): «La glimepirida reduce la glucemia principalmente al estimular la liberación de insulina por las células beta pancreáticas. Las sulfonilureas se unen al receptor de sulfonilurea de la membrana plasmática de las células beta pancreáticas, lo que provoca el cierre del canal de potasio sensible al ATP y, en consecuencia, estimula la liberación de insulina.» Texto original en inglés: "Glimepiride primarily lowers blood glucose by stimulating the release of insulin from pancreatic beta cells. Sulfonylureas bind to the sulfonylurea receptor in the pancreatic beta-cell plasma membrane, leading to closure of the ATP-sensitive potassium channel, thereby stimulating the release of insulin." ([DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa), versión del 2024-08-20; consultado el 2026-11-19). Por conocimiento general, la glimepirida es una sulfonilurea que cierra los canales de potasio sensibles a ATP de las células beta pancreáticas y estimula la liberación de insulina.

El síndrome de la persona rígida es un trastorno autoinmune de la neurotransmisión GABAérgica, asociado frecuentemente con anticuerpos anti-GAD65 y con diabetes como comorbilidad. Esa coincidencia con la diabetes podría explicar la predicción del modelo, pero es una asociación y no una justificación terapéutica.

No se ha establecido un vínculo mecanístico. El puntaje alto (0,9975) es únicamente una predicción computacional y no sustituye a la evidencia clínica. Por ello, el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran al menos 20 autorizaciones vigentes (la lista puede ser parcial), todas de productos de un solo principio activo. Los registros locales no incluyen texto de indicación aprobada. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 25924 | GLEMAZ | 4 mg comp. trirran. x 30 | No registrada |
| 42330 | GLIMEPLIC | 4 mg comp. ran. x 30 | No registrada |
| 43474 | HIPOGLUT 4 | 4 mg comp. x 30 | No registrada |
| 17745 | AMARYL | 4 mg comp. x 15 | No registrada |
| 17756 | ENDIAL | 4 mg comp. x 30 | No registrada |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel moderado figuran fenilefrina, acebutolol, acetazolamida, famotidina, ranitidina, acitretina, formoterol, pseudoefedrina, ketorolaco, epinefrina, ibuprofeno, etinilestradiol, hidrocortisona, albiglutida, salbutamol, etanol, nitazoxanida e hidroclorotiazida. Las interacciones con hidrocortisona tópica y alclometasona tópica son de nivel menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad, y no hay un vínculo mecanístico plausible entre el cierre de canales K-ATP y la fisiopatología de la persona rígida. La evidencia es solo de nivel L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica específica para la enfermedad
- Estudios preclínicos o clínicos que evalúen directamente la glimepirida en esta condición
- Prospecto de ANMAT con advertencias y contraindicaciones para el cribado de seguridad

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

