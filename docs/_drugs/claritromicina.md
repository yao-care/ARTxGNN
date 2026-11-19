---
layout: default
title: Claritromicina
parent: Solo Predicción del Modelo (L5)
nav_order: 107
evidence_level: L5
indication_count: 5
drugbank_id: DB01211
monitor_inn: "Clarithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-11-16
description: "Claritromicina: nueva indicación predicha, síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Claritromicina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Claritromicina: síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Claritromicina es un antibiótico macrólido que se comercializa en Argentina en múltiples presentaciones. El modelo TxGNN predice que podría ser útil para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9935 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Claritromicina (traducción no oficial): «La claritromicina es un fármaco antimicrobiano macrólido. […] La claritromicina ejerce su acción antibacteriana al unirse a la subunidad ribosómica 50S de las bacterias sensibles, lo que da lugar a la inhibición de la síntesis de proteínas.» Texto original en inglés: "Clarithromycin is a macrolide antimicrobial drug. […] Clarithromycin exerts its antibacterial action by binding to the 50S ribosomal subunit of susceptible bacteria resulting in inhibition of protein synthesis." ([DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460), versión del 2026-11-12; consultado el 2026-11-19). Según la información general conocida, es un antibiótico macrólido con cierta actividad inmunomoduladora.

No se identifica un vínculo mecanístico entre este fármaco y el síndrome de hiperviscosidad policlonal, que se relaciona con una elevación policlonal de inmunoglobulinas que aumenta la viscosidad del suero. No existe una justificación establecida por la cual un macrólido pudiera reducir esa viscosidad.

El puntaje de 0,9935 proviene únicamente de una predicción computacional del modelo. Por sí solo no constituye evidencia de eficacia y debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 31701 | AEROXINA U.D. | 500 mg comp. rec. x 8 |
| 56680 | NEUMODRYL | 500 mg comp. x 16 |
| 12610 | KLARICID | IV iny. f.a. x 1 |
| 38660 | CLARIMAX 500 | 500 mg comp. rec. x 8 |
| 23792 | CLARITROMICINA RICHET | 500 mg IV iny. f.a. |

Hay al menos 20 autorizaciones vigentes de producto de un solo principio activo; la lista puede ser parcial.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos, publicaciones ni un mecanismo plausible que la respalde, por lo que el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la claritromicina
- Una hipótesis biológica que vincule el fármaco con la reducción de la viscosidad sérica
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

