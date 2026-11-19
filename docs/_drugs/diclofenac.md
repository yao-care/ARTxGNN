---
layout: default
title: Diclofenac
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
monitor_inn: "DICLOFENAC"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
last_modified_at: 2026-10-30
description: "Diclofenac: nueva indicación predicha, hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Diclofenac
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

## Diclofenaco: inhibidor de la ciclooxigenasa (AINE) → hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Diclofenaco es un antiinflamatorio no esteroideo (AINE) con amplia comercialización en Argentina.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)**, pero no hay ensayos clínicos ni publicaciones que estudien esta enfermedad, por lo que la predicción no cuenta con respaldo de evidencia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0,9969 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Diclofenac (traducción no oficial): «El diclofenaco tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción del diclofenaco, al igual que el de otros AINE, no se comprende por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Diclofenac has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of diclofenac, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Diclofenac Sodium Delayed Release (diclofenac sodium) prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc99e6af-7050-4653-a681-5b252305a970), versión del 2026-09-24; consultado el 2026-11-19). Por su clase, diclofenaco es un AINE que inhibe la ciclooxigenasa (COX-1/COX-2) y reduce la síntesis de prostaglandinas, con efecto antiinflamatorio y analgésico.

La hipotricosis simple del cuero cabelludo es un trastorno genético del folículo piloso (variantes como CDSN, APCDD1 o RPL21). No se identifica un vínculo mecanístico claro con la inhibición de COX: la enfermedad tiene un origen genético que un AINE no debería corregir.

Por ello, el puntaje alto del modelo (0,9969) parece reflejar una asociación basada en la estructura de los datos y no una razón biológica o clínica. Debe tratarse como una hipótesis sin sustento actual.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El diclofenaco se encuentra comercializado en Argentina. Los datos compilados muestran al menos 20 autorizaciones vigentes, y la lista puede ser parcial. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 30268 | VESALION | 75 mg comprimidos x 15 | No registrada en los datos locales |
| 57006 | OXA 75 | comprimidos recubiertos x 15 | No registrada en los datos locales |
| 50302 | METAFLEX 75 CB | cápsulas blandas x 15 | No registrada en los datos locales |
| 37442 | OXA 100 | comprimidos recubiertos x 30 | No registrada en los datos locales |
| 29732 | OXA GEL PLUS | gel x 50 g | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 100 interacciones. Entre las listadas, de gravedad moderada: ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), metformina, sulfonilureas (glimepirida, glipizida, clorpropamida, acetohexamida), mesalazina, balsalazida, aprepitant y exenatida. De gravedad menor: famotidina, ranitidina y cimetidina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura que estudien esta enfermedad, y no existe un vínculo mecanístico plausible entre la inhibición de COX y un trastorno genético del folículo piloso. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco.
- Evidencia preclínica que muestre un papel de las prostaglandinas o la COX en esta enfermedad.
- Revisión del prospecto aprobado en ANMAT para advertencias y contraindicaciones.
- Evaluación de la vía de administración (por ejemplo, formulación tópica) si surgiera evidencia que lo justifique.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Diclofenac Sodium Delayed Release (diclofenac sodium) prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc99e6af-7050-4653-a681-5b252305a970) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

