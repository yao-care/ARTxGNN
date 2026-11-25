---
layout: default
title: Norfloxacina
parent: Solo Predicción del Modelo (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
drugbank_id: DB01059
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-25
description: "Norfloxacina: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Norfloxacina
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

## Norfloxacina: hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Norfloxacina es un antibiótico de la clase de las fluoroquinolonas que se comercializa actualmente en Argentina. El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9970 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Norfloxacina es (traducción no oficial): «Inhibidor de la topoisomerasa IV; inhibidor de la ADN girasa bacteriana». Texto original en inglés: "Topoisomerase IV inhibitor; Bacterial DNA gyrase inhibitor" ([ChEMBL CHEMBL9 (norfloxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL9), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la norfloxacina es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas.

Ese mecanismo no tiene relación identificable con la regulación de la amilasa ni con el manejo de enzimas pancreáticas. El puntaje alto del modelo parece ser un artefacto de la estructura de datos del modelo, sin respaldo clínico ni bibliográfico.

Por lo tanto, esta predicción debe tratarse solo como una hipótesis computacional. No hay un fundamento mecanístico que la sustente, y la similitud con la indicación original no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 12196 | NORFLOXACINA CRAVERI | comp.x 10 | Craveri | Vigente |
| 47270 | ACTOBIAN | 400 mg comp.rec.x 20 | Savant Generic | Vigente |
| 1537 | UROXACIN | 400 mg comp.rec.x 10 | Lazar | Vigente |
| 25454 | NORFLOXACINA KLONAL | 400 mg comp.x 20 | Klonal | Vigente |
| 9457 | UROTEM | comp.x 14 | Temis-Lostaló | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Los productos contienen norfloxacina como único principio activo, salvo UROTEM DOL (asociación con fenazopiridina). Los textos de indicación aprobada no están registrados en los datos locales.

<!-- review:begin ar-lic-20261124-norfloxacina-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Se muestran las 5 primeras de 20 autorizaciones vigentes, todas de producto de un solo principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), UROTEM DOL es una asociación de norfloxacina con fenazopiridina; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-norfloxacina-1 -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, no tiene un mecanismo plausible y la norfloxacina no actúa sobre la regulación de la amilasa. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde una fuente como DrugBank
- Prospecto de ANMAT con advertencias y contraindicaciones, para el cribado de seguridad
- Cualquier estudio clínico o preclínico que evalúe directamente la norfloxacina en hiperamilasemia
- Justificación biológica que explique la asociación antes de reconsiderar la decisión

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL9 (norfloxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL9) |
| 2026-11-24 | «todas de un solo principio activo» → UROTEM DOL es asociación | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

