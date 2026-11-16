---
layout: default
title: Nistatina
parent: Solo Predicción del Modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 9
drugbank_id: DB00646
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
last_modified_at: 2026-11-16
description: "Nistatina: nueva indicación predicha, Disease of orbital region (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Nistatina
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

## Nistatina: Disease of orbital region
{: .text-alpha }

## Resumen en Una Frase

La nistatina es un antifúngico poliénico de uso tópico y oral.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Disease of orbital region |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La nistatina es un antifúngico poliénico que se une al ergosterol de la membrana celular del hongo, formando poros que provocan la fuga del contenido celular. Este mecanismo actúa directamente sobre las especies de *Candida*, la principal causa de la vulvovaginitis infecciosa. Cabe señalar que en los datos compilados para este informe el campo de mecanismo de acción no está registrado; la descripción anterior proviene del análisis mecanístico de la predicción.

La candidiasis vulvovaginal es una de las causas más frecuentes de vaginitis (*Candida albicans* explica el 85–90 % de los casos), por lo que la predicción es biológicamente plausible y coherente con el uso tópico conocido de la nistatina.

Limitaciones: la nistatina no se espera que funcione en causas no fúngicas de vulvovaginitis ni, probablemente, en cepas de *Candida* no albicans o resistentes. Además, una revisión de 1992 señala que los imidazoles y triazoles han superado a la nistatina como primera elección en candidiasis vulvovaginal.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

La evidencia disponible se compone principalmente de revisiones y artículos de manejo clínico; no se identificaron ensayos controlados aleatorizados. Se listan las publicaciones más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Revisión | BMJ Clinical Evidence | Candidiasis vulvovaginal: segunda causa más común de vaginitis; *C. albicans* en 85–90 % de los casos |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Revisión | BMJ Clinical Evidence | Actualización sobre tratamiento de la candidiasis vulvovaginal |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Revisión | BMJ Clinical Evidence | Revisión previa sobre candidiasis vulvovaginal |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Revisión | Pharmaceutics | Manejo de candidiasis vulvovaginal resistente a fluconazol; incluye nistatina entre las alternativas, junto con ácido bórico, oteseconazol e ibrexafungerp |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Revisión | Journal of Women's Health | Ácido bórico en candidiasis vulvovaginal recurrente; mayor resistencia de especies no albicans a azoles |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Revisión | Obstetrics and Gynecology Clinics of North America | Antifúngicos tópicos: la nistatina (introducida en los años 50) fue superada por imidazoles y triazoles como primera opción |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Revisión | Medical Clinics of North America | Monografía sobre nistatina |
| [37830930](https://pubmed.ncbi.nlm.nih.gov/37830930/) | 2023 | Preclínico (modelo animal) | Future Microbiology | Violeta de genciana comparada con nistatina en candidiasis vulvovaginal murina |
| [36588489](https://pubmed.ncbi.nlm.nih.gov/36588489/) | 2022 | Estudio clínico/morfopatológico | Rom J Morphol Embryol | Aspectos clínicos y microbiológicos de la vulvovaginitis por *Candida* antes del tratamiento local con nistatina |
| [35136875](https://pubmed.ncbi.nlm.nih.gov/35136875/) | 2022 | Consenso de expertos | Women's Health Reports | Tratamiento tópico de la candidiasis vulvovaginal recurrente |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 12236 | DIPNI | 100000 UI comp. vaginales x 12 |
| 12237 | DIPNI | 500000 UI comp. orales x 12 |
| 12238 | DIPNI | 500000 UI comp. orales x 30 |
| 31789 | NISTATINA DENVER FARMA | Crema x 30 g |
| 31788 | NISTATINA DENVER FARMA | Suspensión oral x 60 ml |

Las 7 autorizaciones registradas corresponden a productos de un solo principio activo y todas están vigentes (se listan las 5 principales).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se registraron interacciones farmacológicas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación es biológicamente plausible y respaldada por literatura (principalmente revisiones) que describe el uso de la nistatina en candidiasis vulvovaginal, pero no existen ensayos clínicos registrados y la nistatina ha sido superada por azoles como primera opción.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones)
- Confirmar el mecanismo de acción en una fuente farmacológica de referencia
- Evidencia comparativa actual (ensayos controlados) frente a azoles
- Definir la población objetivo: candidiasis por *Candida albicans* sensible, excluyendo causas no fúngicas y cepas resistentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

