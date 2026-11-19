---
layout: default
title: Hidrocortisona
parent: Evidencia Alta (L1-L2)
nav_order: 201
evidence_level: L1
indication_count: 9
drugbank_id: DB00741
monitor_inn: "Hydrocortisone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
last_modified_at: 2026-11-16
description: "Hidrocortisona: nueva indicación predicha, Alopecia areata (nivel de evidencia L1). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Hidrocortisona
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **9** 
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

## Hidrocortisona: Alopecia areata
{: .text-alpha }

## Resumen en Una Frase

La hidrocortisona es un corticosteroide con actividad antiinflamatoria e inmunosupresora, comercializado en Argentina en presentaciones tópicas, orales e inyectables. El modelo TxGNN predice que podría ser efectiva para **alopecia areata (alopecia areata)**, con **1 ensayo clínico** y **20 publicaciones** asociadas. Sin embargo, el único ensayo usó la hidrocortisona como comparador de baja potencia, por lo que no demuestra su eficacia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L1 (ver nota en la conclusión) |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la hidrocortisona es un corticosteroide de baja potencia con efecto antiinflamatorio e inmunosupresor.

La alopecia areata es una enfermedad autoinmune mediada por linfocitos T que atacan los folículos pilosos. Un corticosteroide local podría reducir la inflamación alrededor del folículo, lo que explica la plausibilidad mecanística de la predicción.

Hay una limitación importante: en alopecia areata suelen preferirse corticosteroides de mayor potencia. Existen además informes históricos (décadas de 1950 y 1960) de inyecciones intradérmicas de hidrocortisona, de baja calidad metodológica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Fase 3 | Completado | 41 | Clobetasol 0,05 % en crema frente a hidrocortisona 1 % en crema en niños con alopecia areata. La hidrocortisona fue el comparador de baja potencia, no el fármaco en estudio. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | ECA | JAMA Dermatology | Clobetasol 0,05 % frente a hidrocortisona 1 % en niños con alopecia areata; publicación del ensayo NCT01453686. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Serie de casos histórica | Medical Times | Tratamiento de alopecia areata con cortisona, hidrocortisona y análogos. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Reporte clínico histórico | Der Hautarzt | Crecimiento de pelo tras inyección intracutánea de hidrocortisona. |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Reporte clínico histórico | Actas Dermo-Sifiliográficas | Inyecciones intradérmicas de hidrocortisona en alopecia areata. |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Revisión | J Med Soc New Jersey | Revisión de alopecia areata y otros problemas del cuero cabelludo. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Reporte de casos | J Am Acad Dermatol | Cuatro casos de alopecia areata congénita tratados con minoxidil y diversos tópicos. |
| [28094416](https://pubmed.ncbi.nlm.nih.gov/28094416/) | 2017 | Reporte de caso veterinario | Tierarztl Prax K | Alopecia areata en un perro; el acetato de hidrocortisona tópico no fue eficaz. |

## Información de Mercado en Argentina

Se listan 20 autorizaciones vigentes; el total es de al menos 20 y la lista puede ser parcial. Los textos de indicación aprobada no están registrados en los datos locales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 26462 | ALFACORT | Emulsión 1 % x 15 ml | No registrada |
| 24231 | ALFACORT | Crema 1 % x 30 g | No registrada |
| 38925 | DEMACORT | Crema x 15 g | No registrada |
| 2048 | MICROSONA | Crema 1 % x 15 g | No registrada |
| 7742 | HIDROCORTISONA RICHET | Liofilizado 500 mg x 1 | No registrada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado en alopecia areata, pero la hidrocortisona fue solo el comparador de baja potencia y el resto de la literatura es histórica o de casos. El nivel L1 asignado en los datos es discutible: no hay dos ECA de Fase 3 que prueben la hidrocortisona como fármaco en estudio, por lo que una lectura conservadora sería un nivel inferior.

**Para avanzar se necesita:**
- Revisar el resultado del ensayo NCT01453686 y su publicación (PMID 24226568) para cuantificar la respuesta con hidrocortisona 1 %.
- Datos de mecanismo de acción y del prospecto (advertencias y contraindicaciones) de las autorizaciones locales.
- Comparación con corticosteroides de mayor potencia, que son los preferidos en la práctica.
- Un estudio controlado que evalúe la hidrocortisona como intervención principal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

