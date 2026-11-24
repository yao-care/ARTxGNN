---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 163
evidence_level: L5
indication_count: 9
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "eosinophilia-myalgia syndrome"]
last_modified_at: 2026-11-24
description: "Imipenem: nueva indicación predicha, Esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Imipenem
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

## Imipenem: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico de uso intravenoso. El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa (diffuse scleroderma)**, pero actualmente no hay **ensayos clínicos** ni **publicaciones** que respalden esta dirección; la predicción se apoya únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Imipenem es (traducción no oficial): «Inhibidor de las proteínas bacterianas de unión a penicilina». Texto original en inglés: "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708), CC BY-SA 3.0; consultado el 2026-11-19). Por conocimiento general, imipenem es un carbapenem que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina (PBP), con amplio espectro frente a bacterias grávidas Gram-positivas y Gram-negativas.

La esclerodermia difusa es una enfermedad autoinmune y fibrótica, sin un componente infeccioso bacteriano conocido como causa central. No se identifica un vínculo mecanístico plausible entre la inhibición de la pared celular bacteriana y los procesos autoinmunes o fibróticos de esta enfermedad.

Por lo tanto, el puntaje elevado del modelo probablemente refleja un artefacto de las asociaciones del propio modelo y no una señal biológica verosímil. Esta predicción debe considerarse una hipótesis sin sustento hasta que exista evidencia real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 38546 | IMIPENEM FABRA | 500 mg IV pvo.p/iny.x 1 | Fabra | Vigente |

La tabla muestra el único producto de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

El estado de mercado en Argentina es comercializado; el producto (IMIPENEM FABRA, fabricante: Fabra) es una asociación de imipenem con cilastatina.

<!-- review:begin ar-lic-20261124-imipenem-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «El estado de mercado en Argentina es comercializado, con una autorización vigente de un producto de un solo principio activo (fabricante: Fabra).» Corregido: según los datos (listado de medicamentos de PAMI), IMIPENEM FABRA es una asociación de imipenem con cilastatina; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-imipenem-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones a vigilar**: los datos compilados registran relaciones de contraindicación con epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal. No provienen del texto del prospecto, por lo que deben confirmarse en él.
- **Interacciones farmacológicas** (15 registradas):
  - **Mayores**: bupropión, iohexol, iopamidol.
  - **Moderadas**: polietilenglicol (3350 con electrolitos), dicumarol, warfarina, lindano, aminofilina, difilina, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexed.

Para advertencias y precauciones completas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que estudien imipenem en esclerodermia difusa, y no hay un mecanismo plausible que vincule un antibiótico con una enfermedad autoinmune fibrótica. La predicción se basa solo en el modelo (L5).

**Para avanzar se necesita:**
- Una hipótesis mecanística biológicamente fundamentada que justifique el uso de un antibacteriano en esta enfermedad
- Datos preclínicos que respalden algún efecto relevante
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Datos del mecanismo de acción verificados

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708) |
| 2026-11-24 | «de un solo principio activo» → asociación con cilastatina | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

