---
layout: default
title: Eritromicina
parent: Solo Predicción del Modelo (L5)
nav_order: 157
evidence_level: L5
indication_count: 4
drugbank_id: DB00199
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
last_modified_at: 2026-11-24
description: "Eritromicina: nueva indicación predicha, queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5)."
---

# Eritromicina
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

## Eritromicina: queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Eritromicina es un antibiótico macrólido con propiedades antibacterianas y antiinflamatorias, comercializado en Argentina en presentaciones orales, oftálmicas y tópicas.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)**,
pero actualmente no hay ensayos clínicos y solo **1 publicación** (una revisión sobre blefaroqueratoconjuntivitis crónica en niños) se relaciona de forma indirecta con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (16 de 16) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 16 (vigentes: 16) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Eritromicina (traducción no oficial): «La eritromicina actúa inhibiendo la síntesis de proteínas al unirse a las subunidades ribosómicas 50S de los microorganismos sensibles. No afecta a la síntesis de ácidos nucleicos.» Texto original en inglés: "Erythromycin acts by inhibition of protein synthesis by binding 50S ribosomal subunits of susceptible organisms. It does not affect nucleic acid synthesis." ([DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd), versión del 2018-12-04; consultado el 2026-11-19). Según la información conocida, la eritromicina es un macrólido con actividad antibacteriana y propiedades antiinflamatorias, y mecanísticamente podría ser aplicable a cuadros oculares de origen bacteriano o inflamatorio.

Los macrólidos tópicos u orales se utilizan en la blefaroqueratoconjuntivitis crónica (por ejemplo, la asociada a estafilococos o a disfunción de las glándulas de Meibomio), que puede cursar con queratitis epitelial punteada. Sin embargo, el vínculo es indirecto: el único artículo disponible es una revisión sobre el manejo de la blefaroqueratoconjuntivitis pediátrica, no un estudio de la queratoconjuntivitis epitelial punteada en sí.

El puntaje elevado del modelo (0,9989) es solo una predicción computacional y no está respaldado por datos de ensayos clínicos. Dado que ningún estudio citado aborda directamente esta enfermedad, el nivel de evidencia se establece en L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Revisión | Journal of Pediatric Ophthalmology and Strabismus | Describe la historia, los síntomas, los signos clínicos y el tratamiento de la blefaroqueratoconjuntivitis crónica en niños; no estudia directamente la queratoconjuntivitis epitelial punteada |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 23320 | ERITROFARM | colirio x 5 ml | Poen | Vigente |
| 11986 | PANTOMICINA 500 | E.S.500 mg comp.x 16 | Bagó | Vigente |
| 46126 | ERITROMICINA ELEA | ung.x 3.5 g | Elea | Vigente |
| 31844 | ERITROFARM | ung.oft.unidosis x 20 | Poen | Vigente |
| 9947 | PANTOMICINA 200 | E.S.200 mg susp.x 100 ml | Bagó | Vigente |

La tabla muestra 5 de los 16 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Se muestran 5 de las 16 autorizaciones vigentes de productos de un solo principio activo.

## Citotoxicidad

No aplica a este fármaco; sección omitida por no ser antineoplásico.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación disponible aborda una enfermedad relacionada (blefaroqueratoconjuntivitis crónica pediátrica), no la queratoconjuntivitis epitelial punteada. El puntaje del modelo es alto, pero no tiene respaldo clínico directo.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen eritromicina tópica directamente en queratoconjuntivitis epitelial punteada
- Datos del mecanismo de acción (MOA)
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Evaluación de la compatibilidad de vías de administración (las formas oftálmicas ya comercializadas serían el punto de partida)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

