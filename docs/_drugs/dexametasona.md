---
layout: default
title: Dexametasona
parent: Solo Predicción del Modelo (L5)
nav_order: 131
evidence_level: L5
indication_count: 9
drugbank_id: DB01234
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
last_modified_at: 2026-11-16
description: "Dexametasona: nueva indicación predicha, Alopecia mucinosa (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Dexametasona
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

## Dexametasona: Alopecia mucinosa
{: .text-alpha }

## Resumen en Una Frase

La dexametasona es un glucocorticoide sintético con numerosas autorizaciones vigentes en Argentina, en presentaciones orales, inyectables y oftálmicas.
Los datos compilados no incluyen ensayos clínicos registrados, pero sí **20 publicaciones**. Varias de ellas evalúan directamente la dexametasona en minipulsos orales o pulsos intravenosos para esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Alopecia mucinosa |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, la dexametasona es un agonista potente del receptor de glucocorticoides, con acción antiinflamatoria e inmunosupresora marcada.

La alopecia areata es una enfermedad autoinmune en la que los linfocitos T atacan el folículo piloso. Un glucocorticoide sistémico puede atenuar esa agresión inmunitaria, por lo que el mecanismo es biológicamente plausible. Esto concuerda con el puntaje alto del modelo.

La literatura recuperada muestra que el uso de dexametasona en esta enfermedad ya se explora en la práctica clínica. Se describen minipulsos orales (por ejemplo, 5 mg dos días consecutivos por semana), pulsos intravenosos mensuales y su combinación con corticosteroides tópicos o inhibidores de JAK. Esta evidencia es mayormente observacional, con un solo ensayo aleatorizado pequeño en población pediátrica. Por eso la plausibilidad es sólida, pero la confirmación de eficacia sigue siendo limitada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | ECA | Dermatologic Therapy | Ensayo abierto con 30 niños con alopecia areata grave no progresiva. Compara minipulsos orales de dexametasona a dosis baja con sensibilización de contacto con difenilciclopropenona (DPCP) en cuanto a eficacia y seguridad. |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Revisión sistemática y metaanálisis en red | Archives of Dermatological Research | Compara corticosteroides sistémicos, inhibidores de JAK orales e inmunoterapia de contacto en alopecia areata grave, para identificar la opción más eficaz. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisión | Pediatric Dermatology | Revisa los esquemas de dosificación, la administración y los efectos adversos de la corticoterapia en pulsos en niños con alopecia areata. Señala que los regímenes no están bien establecidos. |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Cohorte prospectiva | Journal of Clinical Medicine | Evidencia de la práctica real sobre eficacia y seguridad de los minipulsos orales de dexametasona, con análisis de factores asociados a la respuesta. |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Estudio multicéntrico | Dermatologic Therapy | Minipulsos de dexametasona oral en alopecia areata moderada a grave, como alternativa accesible frente a los inhibidores de JAK. |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Cohorte prospectiva | Dermatologic Therapy | 73 pacientes pediátricos con alopecia areata grave. Compara pulsos intravenosos de dexametasona de 1 día frente a 3 días, más clobetasol tópico. |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Seguimiento a largo plazo | Dermatologic Therapy | 65 niños y adolescentes con alopecia areata extensa tratados con pulsos orales de dexametasona cada 4 semanas, con seguimiento mediano de 96 meses. |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Cohorte retrospectiva | European Journal of Dermatology | 19 pacientes con alopecia areata grave. Estrategia escalonada con corticosteroides tópicos y baricitinib, con pulsos de dexametasona como rescate en no respondedores. |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Estudio comparativo | Dermatology | Compara eficacia, tasa de recaída y efectos adversos de tres modalidades de corticoterapia sistémica en alopecia areata. |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Serie de pacientes | The Journal of Dermatology | 30 pacientes con alopecia areata extensa tratados con pulso oral de 5 mg de dexametasona dos días consecutivos por semana. |

---

## Información de Mercado en Argentina

La dexametasona figura como **comercializada** en Argentina, con autorizaciones vigentes de producto de un solo principio activo. La lista de autorizaciones puede ser parcial. Los registros locales no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 33509 | DEXATOTAL | Comprimidos 4 mg x 10 |
| 50467 | DECADRON | Ampolla 4 mg/ml x 2 ml con jeringa |
| 51328 | DEXALAF | Comprimidos 8 mg x 10 |
| 49762 | DEXAMETASONA FABRA | Inyectable 8 mg x 1 con jeringa |
| 30440 | NEXADRON OFTAL | Solución oftálmica 0,1 % x 5 ml |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La plausibilidad mecanística es alta (puntaje TxGNN 0,9999). Además, varios estudios observacionales, una revisión sistemática con metaanálisis en red y un ensayo aleatorizado pediátrico pequeño evalúan directamente la dexametasona en alopecia areata. Sin embargo, no hay ensayos clínicos registrados ni ensayos de fase 3 que confirmen la eficacia. Los datos de seguridad locales tampoco están disponibles.

**Para avanzar se necesita:**
- Obtener y revisar los prospectos de ANMAT (advertencias y contraindicaciones), que hoy no están disponibles.
- Completar los datos del mecanismo de acción desde una fuente farmacológica de referencia.
- Evaluar los riesgos de la corticoterapia sistémica: supresión del eje hipotálamo-hipófiso-suprarrenal, efectos metabólicos y óseos, y recaída frecuente al suspender el tratamiento.
- Definir el esquema de dosis y la duración (minipulsos orales o pulsos intravenosos), con apoyo de los estudios y revisiones citados.
- Idealmente, contar con ensayos aleatorizados de mayor tamaño y comparaciones con los inhibidores de JAK.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

