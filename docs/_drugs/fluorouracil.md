---
layout: default
title: Fluorouracil
parent: Solo Predicción del Modelo (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluorouracil: nueva indicación predicha, Rabdomiosarcoma (la predicción de mayor puntaje es la variante botrio… (nivel de evidencia L5). Indicación original: Las licencias locales no incluyen texto d…"
monitor_inn: "fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-beta-thalassemia disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome"]
---

# Fluorouracil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Fluorouracilo: De Carcinoma Basocelular Superficial a Rabdomiosarcoma

## Resumen en Una Frase

Fluorouracilo es un antimetabolito citotóxico, originalmente utilizado en enfermedades de la piel (carcinoma basocelular superficial multifocal, queratosis actínica) y en tumores digestivos (cáncer gástrico, adenocarcinoma de páncreas, metástasis de cáncer de colon).
El modelo TxGNN predice que podría ser efectivo para **rabdomiosarcoma**, con **0 ensayos clínicos** y solo **4 publicaciones** indirectas (revisiones antiguas y un reporte de caso) que lo respaldan.
La evidencia actual es muy limitada y se basa principalmente en la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las licencias locales no incluyen texto de indicación aprobada; la base de conocimiento lista carcinoma basocelular superficial multifocal, queratosis actínica y cáncer gástrico, entre otras |
| Nueva Indicación Predicha | Rabdomiosarcoma (la predicción de mayor puntaje es la variante botrioide embrionaria de vagina; la primera con literatura es rabdomiosarcoma general) |
| Puntaje de Predicción TxGNN | 99.75 % (rabdomiosarcoma botrioide embrionario de vagina); 99.74 % (rabdomiosarcoma general) |
| Nivel de Evidencia | L5 (predicción principal); L4 para rabdomiosarcoma general |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el fluorouracilo es un antimetabolito que inhibe la timidilato sintasa y se incorpora al ARN y ADN, lo que interrumpe la síntesis de ácidos nucleicos en células de rápida división.

Su eficacia en tumores epiteliales (piel, estómago, páncreas, colon) está comprobada. Mecanísticamente, esa acción citotóxica general podría ser aplicable a un sarcoma proliferativo como el rabdomiosarcoma.

Sin embargo, es importante señalar que el fluorouracilo no es un componente estándar de los esquemas de primera línea para rabdomiosarcoma (tipo VAC/VAI). Por lo tanto, el alto puntaje del modelo no está respaldado por evidencia clínica directa. Las predicciones de síndromes de células falciformes (puntajes idénticos de 99.62 %) parecen derivar de una inferencia compartida del grafo y no de una señal específica de la enfermedad; además, el perfil de toxicidad del fármaco lo hace poco adecuado para una enfermedad crónica no maligna.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Literatura para rabdomiosarcoma (disease):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Reporte de caso | Case Reports in Oncological Medicine | Rabdomiosarcoma lingual en un adulto joven. Doxorrubicina + ifosfamida y luego cisplatino + 5-fluorouracilo produjeron progresión; la respuesta llegó con un tercer esquema (vincristina, actinomicina D y otros). No se demuestra un aporte del fluorouracilo |
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Revisión/serie clínica | Cancer | Valor de la quimioterapia adyuvante en sarcomas infantiles, incluido el rabdomiosarcoma |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Revisión | Annals of the Academy of Medicine, Singapore | Curabilidad de cánceres avanzados con quimioterapia, incluidos cánceres infantiles como el rabdomiosarcoma |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Serie de casos retrospectiva | Medical and Pediatric Oncology | Carcinoma nasofaríngeo indiferenciado infantil; relevancia baja para rabdomiosarcoma |

Para otras predicciones (sarcoma hepático, rabdomiosarcoma de vía biliar extrahepática) la literatura recuperada es indirecta: trata histologías distintas (carcinoma de vía biliar, metástasis hepáticas colorrectales), estudios preclínicos en ratones o trabajos no relacionados. El único estudio clínico directo sobre sarcoma hepático es una cohorte retrospectiva de adultos de un solo hospital (PMID 29346784, 2019), donde el aporte del fluorouracilo no está claro.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40612 | ACLER (Pharmatrix) | Crema, 20 g | No se dispone de texto de indicación |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase fluoropirimidina) |
| Riesgo de Mielosupresión | Alto en uso sistémico; la base de conocimiento registra trombocitopenia, neutropenia, agranulocitosis y leucopenia como contraindicaciones. La presentación local en crema tiene menor exposición sistémica |
| Clasificación de Emetogenicidad | Baja a moderada (uso sistémico) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; considerar la deficiencia de dihidropirimidina deshidrogenasa (DPD) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (base de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, enfermedad diarreica, úlcera péptica activa, faringitis, estomatitis, pipiuréter y deficiencia de dihidropirimidina deshidrogenasa.
- **Interacciones farmacológicas**: se identificaron 361 interacciones. Las de nivel moderado incluyen metronidazol y tinidazol; las de nivel menor incluyen cimetidina y levofloxacino. Muchas otras (por ejemplo omeprazol, pantoprazol, metformina, morfina) no tienen nivel clasificado.

Consultar el prospecto para la información de seguridad completa de la presentación local.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya casi solo en el modelo: no hay ensayos clínicos y la literatura es antigua, indirecta o anecdótica. El fluorouracilo no forma parte de los esquemas estándar de rabdomiosarcoma y su toxicidad es considerable. Además, la única presentación autorizada en Argentina es una crema, que no es compatible con el tratamiento sistémico de un sarcoma.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Prospecto de ANMAT con advertencias y contraindicaciones
- Revisión de literatura específica sobre fluorouracilo en rabdomiosarcoma y sarcomas de tejidos blandos
- Evaluación de la compatibilidad de vía de administración (se requeriría formulación sistémica)
- Datos preclínicos o ensayos exploratorios que respalden eficacia y relación riesgo-beneficio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

