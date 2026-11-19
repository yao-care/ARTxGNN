---
layout: default
title: Tetracycline
parent: Solo Predicción del Modelo (L5)
nav_order: 233
evidence_level: L5
indication_count: 4
monitor_inn: "tetracycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
last_modified_at: 2026-11-20
description: "Tetracycline: nueva indicación predicha, Queratoconjuntivitis epitelial punctata (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). Indicación original: No consta en los datos locale"
---

# Tetracycline
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

## Tetraciclina: antibiótico de la clase de las tetraciclinas → queratoconjuntivitis epitelial punctata (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Tetraciclina es un antibiótico de amplio espectro de la clase de las tetraciclinas.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punctata (punctate epithelial keratoconjunctivitis)**,
pero actualmente solo existe **1 publicación** (un reporte de casos) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punctata (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0,9958 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Tetracycline es (traducción no oficial): «Inhibidor del ribosoma 70S bacteriano» Texto original en inglés: "Bacterial 70S ribosome inhibitor" ([ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la tetraciclina es un antibiótico bacteriostático de amplio espectro que inhibe la síntesis proteica bacteriana. Además, las tetraciclinas tienen efectos antiinflamatorios, como la inhibición de metaloproteinasas de matriz, que son relevantes en la superficie ocular.

La queratitis epitelial punctata puede aparecer como secuela de infecciones por clamidia, un agente sensible a las tetraciclinas. El vínculo es por lo tanto plausible pero indirecto, a través de la etiología infecciosa y la actividad antiinflamatoria, y no está demostrado para esta enfermedad. El puntaje tan alto del modelo probablemente refleja la cercanía con las indicaciones de conjuntivitis.

**Nivel de evidencia:** el único estudio disponible describe dos casos de queratitis punctata tras conjuntivitis por clamidia, tratados con tetraciclina o doxiciclina. Es un reporte de casos que no evalúa el efecto del fármaco sobre la queratitis; por ello se asigna L5 y no el nivel L4 que figura en los datos de origen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Reporte de casos | Cornea | Dos casos de conjuntivitis folicular por *Chlamydia trachomatis*, tratados con tetraciclina o doxiciclina oral con resolución de los folículos. Luego presentaron queratitis epitelial punctata recurrente y bilateral. No muestra beneficio de la tetraciclina sobre la queratitis. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6177 | TETRACICLINA OMEGA | Comprimidos x 16 | No registrada en los datos locales |
| 3657 | SOLUSTRES | Grageas x 16 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Contraindicaciones (no provenientes del prospecto):** los datos compilados señalan posibles contraindicaciones o precauciones en enfermedad hepática y renal, epilepsia, neutropenia y agranulocitosis, deficiencia de G6PD, colitis por *Clostridium difficile*, entre otras. No proceden del texto del prospecto y deben verificarse.
- **Interacciones Farmacológicas:** se identificaron 308 interacciones. Entre las de nivel mayor figuran isotretinoína, acitretina y ácido aminolevulínico. Entre las de nivel moderado figuran etinilestradiol, amoxicilina, ampicilina, aminofilina, atracurio y antiácidos con aluminio.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en un reporte de casos que no estudia el efecto de la tetraciclina sobre esta enfermedad. No hay ensayos clínicos.

**Para avanzar se necesita:**
- Estudios clínicos o series que evalúen la tetraciclina (o la clase) en queratoconjuntivitis epitelial punctata
- Datos del mecanismo de acción
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Evaluación de la vía de administración (oral frente a oftálmica) necesaria para esta indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

