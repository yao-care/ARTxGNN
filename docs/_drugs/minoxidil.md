---
layout: default
title: Minoxidil
parent: Solo Predicción del Modelo (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
monitor_inn: "MINOXIDIL"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pseudopelade of Brocq", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with HIV infection"]
last_modified_at: 2026-11-20
description: "Minoxidil: nueva indicación predicha, hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Minoxidil
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

## Minoxidil: antihipertensivo vasodilatador / estimulante del folículo piloso → hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Minoxidil es un fármaco vasodilatador que se utiliza tanto por vía sistémica como tópica, con uso conocido en el control de la presión arterial y en la caída del cabello.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)**, con **0 ensayos clínicos** y **3 publicaciones** (reportes de caso) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 1,0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Minoxidil es (traducción no oficial): «Abridor del receptor de sulfonilurea 2, Kir6.2». Texto original en inglés: "Sulfonylurea receptor 2, Kir6.2 opener" ([ChEMBL CHEMBL802 (minoxidil): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL802), CC BY-SA 3.0; consultado el 2026-11-19). Según la literatura revisada, minoxidil actúa (a través de su metabolito sulfato) como abridor de canales de potasio: prolonga la fase anágena, acorta la fase telógena y aumenta el tamaño del folículo y el flujo sanguíneo perifolicular.

La hipotricosis simple hereditaria del cuero cabelludo es un trastorno raro de miniaturización y crecimiento del folículo piloso. Por ello, un fármaco que estimula el crecimiento folicular es mecanísticamente plausible para esta enfermedad.

Sin embargo, la evidencia es limitada: los tres artículos (2022-2024) describen casos aislados o series pequeñas, casi siempre con minoxidil combinado con factores de crecimiento, extractos botánicos o plasma rico en plaquetas. Esto impide aislar la contribución del minoxidil por sí solo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Reporte de caso | Frontiers in Genetics | Niño de 8 años con hipotricosis simple del cuero cabelludo por mutación en CDSN, tratado con extractos botánicos y minoxidil |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Reporte de caso | J Dermatol Treat | Paciente de 14 años tratada con inyección de plasma rico en plaquetas más minoxidil tópico al 2 % |
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Reporte/serie de casos | Dermatologic Therapy | Hipotricosis simple hereditaria tratada con minoxidil oral y factores de crecimiento |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24664 | YLOX 5 | loc.x 100 ml | No registrada en los datos locales |
| 1023 | YLOX | loc.x 100 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registran 100 interacciones en total; entre las de nivel moderado figuran hidrocortisona, bupropión, triamcinolona, morfina, dexametasona, betametasona, budesonida y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), además de dronabinol, nabilona, opio, prednisolona, prednisona y sapropterina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni estudio comparativo que evalúe directamente minoxidil en esta enfermedad; solo hay tres reportes de caso con terapias combinadas. Con ese respaldo, el nivel de evidencia es L5 (predicción del modelo con apoyo clínico anecdótico) y no justifica avanzar todavía.

**Para avanzar se necesita:**
- Estudios clínicos controlados o series de casos más amplias que aíslen el efecto del minoxidil en monoterapia
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto aprobado en Argentina
- Evaluación de la forma farmacéutica local (solución tópica) frente a la vía oral usada en algunos reportes

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL802 (minoxidil): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL802) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

