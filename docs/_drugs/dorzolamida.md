---
layout: default
title: Dorzolamida
parent: Solo Predicción del Modelo (L5)
nav_order: 145
evidence_level: L5
indication_count: 7
drugbank_id: DB00869
monitor_inn: "Dorzolamide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "congestive heart failure", "acute pulmonary heart disease", "respiratory failure"]
last_modified_at: 2026-11-20
description: "Dorzolamida: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 8 (en el listado vigente: 8)"
---

# Dorzolamida
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Dorzolamida: Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Dorzolamida es un inhibidor tópico de la anhidrasa carbónica II, utilizado en forma de colirio para reducir la presión intraocular.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)**, con un puntaje de 0,9995, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (8 de 8) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 8 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Dorzolamida (traducción no oficial): «La anhidrasa carbónica (AC) es una enzima presente en muchos tejidos del organismo, incluido el ojo. Cataliza la reacción reversible que comprende la hidratación del dióxido de carbono y la deshidratación del ácido carbónico. […] La solución oftálmica de clorhidrato de dorzolamida contiene clorhidrato de dorzolamida, un inhibidor de la anhidrasa carbónica II humana.» Texto original en inglés: "Carbonic anhydrase (CA) is an enzyme found in many tissues of the body including the eye. It catalyzes the reversible reaction involving the hydration of carbon dioxide and the dehydration of carbonic acid. […] Dorzolamide hydrochloride ophthalmic solution contains dorzolamide hydrochloride, an inhibitor of human carbonic anhydrase II." ([DailyMed: Dorzolamide Hydrochloride Ophthalmic Solution (dorzolamide hydrochloride) prescribing information, Micro Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4698e4e1-c5f6-4db1-9328-74464a85afea), versión del 2026-11-14; consultado el 2026-11-19). Según la información conocida, dorzolamida inhibe la anhidrasa carbónica II y, al aplicarse en el ojo, reduce la producción de humor acuoso y con ello la presión intraocular.

La hipotricosis simple es un trastorno genético de miniaturización del folículo piloso. No se identificó ninguna vía que conecte la inhibición de la anhidrasa carbónica con este trastorno, por lo que no existe un vínculo mecanístico creíble.

El puntaje alto (0,9995) proviene únicamente de la predicción del modelo y no está respaldado por estudios reales. Esta predicción debe considerarse una señal exploratoria de muy baja plausibilidad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 36325 | DORLAMIDA | Solución oftálmica x 5 ml | — |
| 40713 | ZOPIROL DM | Solución oftálmica x 5 ml | — |
| 25086 | GLAUCOTENSIL TD | Colirio x 5 ml | — |
| 36326 | DORLAMIDA T | Solución oftálmica x 5 ml | — |
| 39900 | ALIVIAPRES | Solución oftálmica x 5 ml | — |

Se muestran 5 de las 8 autorizaciones vigentes. El texto de indicación aprobada no figura en los datos locales.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad, y no se identifica un mecanismo plausible. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de dorzolamida
- Estudios preclínicos que sugieran un vínculo entre la anhidrasa carbónica y la biología del folículo piloso
- Información de seguridad del prospecto aprobado por ANMAT
- Evaluación de compatibilidad de la vía de administración (colirio frente a aplicación en cuero cabelludo)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Dorzolamide Hydrochloride Ophthalmic Solution (dorzolamide hydrochloride) prescribing information, Micro Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4698e4e1-c5f6-4db1-9328-74464a85afea) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

