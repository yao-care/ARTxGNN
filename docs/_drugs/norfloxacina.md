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
last_modified_at: 2026-11-16
description: "Norfloxacina: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 20 (en el listado vigente: 20)"
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
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (20 de 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 20 (vigentes: 20) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Norfloxacina es (traducción no oficial): «Inhibidor de la topoisomerasa IV; inhibidor de la ADN girasa bacteriana» Texto original en inglés: "Topoisomerase IV inhibitor; Bacterial DNA gyrase inhibitor" ([ChEMBL CHEMBL9 (norfloxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL9), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la norfloxacina es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas.

Ese mecanismo no tiene relación identificable con la regulación de la amilasa ni con el manejo de enzimas pancreáticas. El puntaje alto del modelo parece ser un artefacto de la estructura de datos del modelo, sin respaldo clínico ni bibliográfico.

Por lo tanto, esta predicción debe tratarse solo como una hipótesis computacional. No hay un fundamento mecanístico que la sustente, y la similitud con la indicación original no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 12196 | NORFLOXACINA CRAVERI | comp. x 10 |
| 47270 | ACTOBIAN | 400 mg comp. rec. x 20 |
| 1537 | UROXACIN | 400 mg comp. rec. x 10 |
| 25454 | NORFLOXACINA KLONAL | 400 mg comp. x 20 |
| 9457 | UROTEM | comp. x 14 |

Se muestran las 5 primeras de 20 autorizaciones vigentes, todas de producto de un solo principio activo. Los textos de indicación aprobada no están registrados en los datos locales.

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

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL9 (norfloxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

