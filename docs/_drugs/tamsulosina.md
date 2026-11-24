---
layout: default
title: Tamsulosina
parent: Solo Predicción del Modelo (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
drugbank_id: DB00706
monitor_inn: "Tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
last_modified_at: 2026-11-24
description: "Tamsulosina: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita) (nivel de evidencia L5)."
---

# Tamsulosina
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

## Tamsulosina: Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita)
{: .text-alpha }

## Resumen en Una Frase

Tamsulosina es un antagonista de los receptores adrenérgicos alfa-1A/1D, de uso urológico, comercializado en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tamsulosina (traducción no oficial): «Los síntomas asociados a la hiperplasia prostática benigna (HPB) están relacionados con la obstrucción del tracto de salida vesical, que consta de dos componentes subyacentes: estático y dinámico. El componente estático está relacionado con un aumento del tamaño de la próstata causado, en parte, por una proliferación de células de músculo liso en el estroma prostático. […] La tamsulosina, un agente bloqueante de los adrenorreceptores alfa 1, presenta selectividad por los receptores alfa 1 de la próstata humana.» Texto original en inglés: "The symptoms associated with benign prostatic hyperplasia (BPH) are related to bladder outlet obstruction, which is comprised of two underlying components: static and dynamic. The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Tamsulosin, an alpha 1 adrenoceptor blocking agent, exhibits selectivity for alpha 1 receptors in the human prostate." ([DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f), versión del 2026-11-12; consultado el 2026-11-19). Según la información conocida, la tamsulosina bloquea selectivamente los receptores alfa-1A/1D adrenérgicos, y su uso se centra en afecciones urológicas.

Desde el punto de vista mecanístico, no se identifica un vínculo plausible con esta enfermedad. La hipertricosis tipo Ambras es una condición congénita rara, asociada a reordenamientos cromosómicos que afectan la regulación de TRPS1. El bloqueo alfa-1 adrenérgico no actúa sobre esa vía.

El puntaje alto del modelo parece ser un artefacto de la propagación en la red a partir de nodos vecinos de enfermedades del cabello, y no una relación farmacológica sustentada. La ausencia de datos de mecanismo de acción y de indicaciones originales debilita aún más la interpretabilidad de esta predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones vigentes de tamsulosina como monofármaco (la lista puede ser parcial). Se muestran las 5 principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 51153 | OMNIC OCAS | 0.4mg comp.lib.prol.x 60 | Gador | Vigente |
| 50819 | DENVERPROST | 0.4 mg cáps.lib.cont.x30 | Denver Farma | Vigente |
| 43134 | UROPROST-Q | 0.4 mg cáps.x 30 | Ariston | Vigente |
| 59850 | URALOS CR | 0.4 mg comp.x 60 | Casasco | Vigente |
| 22906 | OMNIC | 0.4mg caps.lib.cont.x 30 | Gador | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura que estudien directamente esta enfermedad, no tiene un vínculo mecanístico plausible y su puntaje elevado parece un artefacto computacional. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Texto de indicaciones y advertencias/contraindicaciones del prospecto de ANMAT
- Evidencia preclínica o clínica que estudie directamente esta enfermedad antes de reconsiderar la decisión

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: tamsulosin hydrochloride prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6b6aeab-bedd-4254-8811-4f65cf8a351f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

