---
layout: default
title: Sulfametoxazol
parent: Solo Predicción del Modelo (L5)
nav_order: 333
evidence_level: L5
indication_count: 1
drugbank_id: DB01015
monitor_inn: "Sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
last_modified_at: 2026-11-24
description: "Sulfametoxazol: nueva indicación predicha, Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 17 (en el listado vigente: 17)"
---

# Sulfametoxazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Sulfametoxazol: Conjuntivitis contagiosa aguda (acute contagious conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Sulfametoxazol es un antibiótico sulfonamida de uso sistémico, comercializado en Argentina bajo varias marcas.
El modelo TxGNN predice que podría ser útil para la **conjuntivitis contagiosa aguda (acute contagious conjunctivitis)**,
pero actualmente solo se dispone de **0 ensayos clínicos** y **1 publicación** de tipo observacional, que no estudia directamente este fármaco para esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (17 de 17) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 17 (vigentes: 17) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Sulfametoxazol es (traducción no oficial): «Inhibidor de la dihidropteroato sintasa bacteriana». Texto original en inglés: "Bacterial dihydropteroate synthase inhibitor" ([ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general de la clase, el sulfametoxazol es una sulfonamida que inhibe la enzima bacteriana dihidropteroato sintasa y bloquea la síntesis de folato, lo que frena el crecimiento de muchas bacterias.

La conjuntivitis contagiosa aguda de origen bacteriano es causada con frecuencia por patógenos como *Staphylococcus aureus*, *Streptococcus pneumoniae* y *Haemophilus influenzae*. Mecanísticamente, un antibacteriano que actúa sobre la síntesis de folato podría ser aplicable. Las sulfonamidas tienen además una larga historia de uso oftálmico tópico.

Conviene ser cautos: el puntaje del modelo es solo una predicción computacional, y los datos compilados no establecen la eficacia del sulfametoxazol (de uso típicamente sistémico) en esta enfermedad. Tampoco se dispone de información sobre la vía de administración requerida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (retrospectivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análisis retrospectivo de la bacteriología y la sensibilidad a antibióticos en conjuntivitis bacteriana aguda infantil en el oeste de Grecia; describe un tratamiento empírico habitual con antibióticos tópicos de amplio espectro. No evalúa el sulfametoxazol como tratamiento. |

## Información de Mercado en Argentina

Hay 17 autorizaciones vigentes de productos con sulfametoxazol como único principio activo. Principales (5 de 17):

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 18740 | BACTRIM | comp.x 20 | Siegfried | Vigente |
| 18317 | BACTICEL | comp.x 12 | Bagó | Vigente |
| 10614 | BACTRIM | IV a.x 5 x 5 ml | Siegfried | Vigente |
| 14645 | ADRENOL | comp.x 10 | Fabra | Vigente |
| 31642 | TRITENK FORTE | comp.x 10 | Biotenk | Vigente |

La tabla muestra 5 de los 17 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en un estudio observacional que no analiza directamente el sulfametoxazol en esta enfermedad, por lo que el nivel de evidencia es L5. Además, el fármaco se usa típicamente por vía sistémica y no hay datos que respalden su eficacia en conjuntivitis.

**Para avanzar se necesita:**
- Ensayos o estudios que evalúen directamente el sulfametoxazol en conjuntivitis bacteriana aguda
- Datos del mecanismo de acción confirmados por una fuente farmacológica
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Evaluación de la compatibilidad de la vía de administración (sistémica frente a oftálmica)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

