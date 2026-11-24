---
layout: default
title: Clindamicina
parent: Solo Predicción del Modelo (L5)
nav_order: 110
evidence_level: L5
indication_count: 6
drugbank_id: DB01190
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-24
description: "Clindamicina: nueva indicación predicha, queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5)."
---

# Clindamicina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Clindamicina: queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Clindamicina es un antibiótico de la clase de las lincosamidas, comercializado en Argentina en presentaciones orales, inyectables, tópicas y vaginales.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)**, pero **no se recuperó ningún ensayo clínico ni publicación** que respalde esta dirección: se trata de una predicción puramente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clindamicina (traducción no oficial): «La clindamicina inhibe la síntesis de proteínas bacterianas mediante su unión al ARN 23S de la subunidad 50S del ribosoma. La clindamicina es bacteriostática.» Texto original en inglés: "Clindamycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the ribosome. Clindamycin is bacteriostatic." ([DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a), versión del 2026-09-16; consultado el 2026-11-19). Por conocimiento general, la clindamicina es un antibacteriano que inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosomal 50S, con actividad principalmente frente a bacterias Gram positivas.

La relación mecanística con la nueva indicación es débil. La queratitis epitelial punteada suele ser de origen viral (por ejemplo, adenovirus) o no infeccioso (ojo seco, toxicidad), por lo que un antibacteriano no tiene un fundamento terapéutico claro. El puntaje alto probablemente refleja cercanía con otros fármacos antiinfecciosos oculares en el modelo y no un vínculo terapéutico real.

Por lo tanto, esta predicción debe considerarse una hipótesis sin respaldo, y no una recomendación de uso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El estado de mercado es **comercializado**: las 20 autorizaciones listadas están vigentes y la lista puede ser parcial (al menos 20 autorizaciones).

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 36632 | CLIDAN | gel dérm.x 15 g | Cassará | Vigente |
| 17438 | CLINDAMICINA RICHET | 300 mg cáps.x 16 | Richet | Vigente |
| 59420 | MICROBION | 300 mg cáps.x 16 | Montpellier | Vigente |
| 15812 | CLINDAMICINA FABRA | 600 mg a.x 1 | Fabra | Vigente |
| 54601 | RESBIOTIC | 300 mg cáps.x 16 | Casasco | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Las presentaciones incluyen vías oral, inyectable, tópica (geles, loción, solución) y vaginal (óvulos y cápsulas blandas).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no cuenta con ensayos clínicos ni literatura (nivel de evidencia L5), y su fundamento mecanístico es débil, ya que la enfermedad suele ser viral o no infecciosa y la clindamicina es un antibacteriano.

**Para avanzar se necesita:**
- Datos de mecanismo de acción detallados y verificados
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Evaluación de la compatibilidad de vía de administración (por ejemplo, formulación oftálmica, que no figura entre las presentaciones locales)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

