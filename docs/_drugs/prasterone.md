---
layout: default
title: Prasterone
parent: Solo Predicción del Modelo (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
monitor_inn: "prasterone"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "severe nonproliferative diabetic retinopathy", "thrombophilia due to protein S deficiency, autosomal recessive", "scleroderma (disease)", "complement component 4a deficiency", "pseudo-von Willebrand disease", "primary release disorder of platelets"]
last_modified_at: 2026-11-24
description: "Prasterone: nueva indicación predicha, Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Prasterone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Prasterona: precursor esteroideo (DHEA) → deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Prasterona (dehidroepiandrosterona, DHEA) es un precursor esteroideo con autorizaciones vigentes en Argentina. El modelo TxGNN predice que podría ser efectivo para la **deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Prasterone (traducción no oficial): «La prasterona es un esteroide endógeno inactivo que se convierte en andrógenos y/o estrógenos activos. El mecanismo de acción de INTRAROSA en mujeres posmenopáusicas con atrofia vulvar y vaginal no está completamente establecido.» Texto original en inglés: "Prasterone is an inactive endogenous steroid and is converted into active androgens and/or estrogens. The mechanism of action of INTRAROSA in postmenopausal women with vulvar and vaginal atrophy is not fully established." ([DailyMed: Intrarosa (prasterone) prescribing information, Millicent US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ada639d4-bac0-2ad0-e053-2a95a90afce7), versión del 2026-07-17; consultado el 2026-11-19). Según la información compilada, es un precursor de esteroides sexuales (andrógenos y estrógenos) y actúa también sobre el receptor de glicina, según los datos farmacológicos disponibles.

La deficiencia del cofactor 2 de la heparina es un trastorno de la coagulación asociado a la proteína SERPIND1. No se conoce ningún mecanismo por el cual la prasterona influya en la función de esta proteína. Cualquier vínculo sería especulativo (por ejemplo, efectos indirectos sobre la coagulación o la síntesis hepática de proteínas).

El puntaje alto (0,9999) refleja una señal del modelo basada en relaciones entre datos, no una validación biológica ni clínica. Las demás predicciones de mayor puntaje también corresponden a trastornos de la coagulación, lo que sugiere un patrón de agrupamiento en el modelo más que evidencia específica. Los agentes hormonales pueden modificar el riesgo trombótico, por lo que el potencial de daño debe evaluarse antes de cualquier hipótesis de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 35633 | SUPLIGOL NF | IM iny.a.x 1 x 1 ml | Lazar | Vigente |
| 980 | LONGEVITAL | 5000 mcg comp.x 30 | Bagó | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Ambas autorizaciones están vigentes y corresponden a productos de un solo principio activo.

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología:** los datos compilados registran una interacción farmacológica con el receptor de glicina (todos los subtipos), sin nivel de gravedad asignado.
- **Consideración teórica:** dado que los metabolitos androgénicos/estrogénicos de la DHEA podrían influir en la coagulación, la dirección del efecto en un trastorno protrombótico o de coagulación es desconocida y podría ser perjudicial.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni publicaciones que estudien directamente esta enfermedad (nivel L5), y no existe un mecanismo plausible conocido que vincule la prasterona con la función del cofactor 2 de la heparina. Además, existe una preocupación de seguridad por el posible efecto de los esteroides sobre la coagulación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la prasterona
- Búsqueda bibliográfica dirigida sobre prasterona/DHEA y el cofactor 2 de la heparina (SERPIND1)
- Obtención y análisis del prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos que respalden un efecto sobre la coagulación antes de considerar cualquier ensayo clínico
- Evaluación del riesgo trombótico asociado a la administración de esteroides

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Intrarosa (prasterone) prescribing information, Millicent US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ada639d4-bac0-2ad0-e053-2a95a90afce7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

