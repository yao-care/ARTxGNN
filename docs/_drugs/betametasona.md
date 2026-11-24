---
layout: default
title: Betametasona
parent: Solo Predicción del Modelo (L5)
nav_order: 51
evidence_level: L5
indication_count: 7
drugbank_id: DB00443
monitor_inn: "Betamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions"]
last_modified_at: 2026-11-24
description: "Betametasona: nueva indicación predicha, Alopecia mucinosa (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Betametasona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Betametasona: Alopecia mucinosa
{: .text-alpha }

## Resumen en Una Frase

Betametasona es un corticosteroide de uso sistémico, inyectable y tópico, con múltiples autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser útil para **alopecia mucinosa (alopecia mucinosa)**, pero la evidencia que lo respalda se limita a **1 publicación** de 1964 (serie de casos con revisión de terapias) y **ningún ensayo clínico**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Alopecia mucinosa |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Betametasona (traducción no oficial): «Los corticosteroides desempeñan un papel en la señalización celular, la función inmunitaria, la inflamación y la regulación de las proteínas; sin embargo, se desconoce el mecanismo de acción exacto de SERNIVO Spray en la psoriasis.» Texto original en inglés: "Corticosteroids play a role in cellular signaling, immune function, inflammation, and protein regulation; however, the precise mechanism of action of SERNIVO Spray in psoriasis is unknown." ([DailyMed: Sernivo (betamethasone dipropionate) prescribing information, Primus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b3d1b0-da9b-11eb-ad76-0800200c9a66), versión del 2026-04-22; consultado el 2026-11-19). Según la información conocida, la betametasona es un corticosteroide potente con actividad antiinflamatoria e inmunosupresora.

La alopecia mucinosa (mucinosis folicular) se caracteriza por infiltrados inflamatorios perifoliculares con depósito de mucina. Por ello, un corticosteroide tópico o intralesional es una opción terapéutica plausible desde el punto de vista mecanístico.

Conviene ser prudente: la única publicación identificada es una serie de tres casos con revisión de terapias, de 1964, que no es un estudio controlado y no evalúa de forma directa y concluyente la betametasona. Dado que ningún estudio citado aborda con rigor esta enfermedad con el fármaco, el nivel de evidencia se establece en L5 y el puntaje alto de TxGNN debe entenderse solo como una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14164963](https://pubmed.ncbi.nlm.nih.gov/14164963/) | 1964 | Serie de casos / Revisión | Archives of Dermatology | Reporte de tres casos de mucinosis folicular (alopecia mucinosa) con revisión de las terapias empleadas; no hay resumen disponible ni datos controlados |

## Información de Mercado en Argentina

La lista siguiente puede ser parcial: el total de autorizaciones es de al menos 20, y todas las listadas figuran como vigentes. Los registros no incluyen texto de indicación aprobada.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 56322 | VITACORTIL B | susp.oral x 30 ml | Biosintex | Vigente |
| 44188 | CORTICAS RETARD | iny.f.a.x 1 x 2 ml | Casasco | Vigente |
| 3338 | BETNOVATE CAPILAR | loc.x 30 ml | GlaxoSmithKline | Vigente |
| 44186 | CORTICAS | gts.x 20 ml | Casasco | Vigente |
| 39514 | METAMAR RETARD | f.a.x 1 x 2 ml + jga. | Mar | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un puntaje alto de TxGNN y en una plausibilidad mecanística general, pero la única evidencia es una serie de casos de 1964 sin datos controlados y sin ensayos clínicos. No hay estudios que evalúen directamente la betametasona en esta enfermedad.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre corticosteroides en mucinosis folicular, incluyendo series de casos más recientes
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto
- Evaluación de compatibilidad de vía de administración (tópica o intralesional) con las presentaciones disponibles
- Estudio exploratorio (por ejemplo, serie prospectiva de casos) antes de considerar un ensayo formal

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «No se identificaron autorizaciones de comercialización vigentes» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sernivo (betamethasone dipropionate) prescribing information, Primus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b3d1b0-da9b-11eb-ad76-0800200c9a66) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

