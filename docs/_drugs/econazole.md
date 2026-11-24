---
layout: default
title: Econazole
parent: Solo Predicción del Modelo (L5)
nav_order: 132
evidence_level: L5
indication_count: 2
monitor_inn: "econazole"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-11-24
description: "Econazole: nueva indicación predicha, Infección ectótrix (nivel de evidencia L5). Indicación original: No hay texto de indicación aprobada en las autorizaciones locales. La…"
---

# Econazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Econazol: De Infecciones Dermatofíticas Cutáneas a Infección Ectótrix
{: .text-alpha }

## Resumen en Una Frase

Econazol es un antifúngico imidazólico, utilizado originalmente para infecciones cutáneas como tinea pedis, tinea corporis y candidiasis cutánea.
El modelo TxGNN predice que podría ser efectivo para **infección ectótrix (ectothrix infectious disease)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No hay texto de indicación aprobada en las autorizaciones locales. Las relaciones registradas en el grafo de conocimiento incluyen tinea pedis, tinea corporis, infección por tiña, candidiasis cutánea, pitiriasis versicolor y dermatofitosis de la ingle y la zona perianal |
| Nueva Indicación Predicha | Infección ectótrix |
| Puntaje de Predicción TxGNN | 0,9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Econazole (traducción no oficial): «La espuma tópica Ecoza es un antifúngico azólico. […] El nitrato de econazol, un agente antifúngico azólico, inhibe la enzima 14 alfa-lanosterol desmetilasa fúngica mediada por el citocromo P-450. Esta enzima tiene la función de convertir el lanosterol en ergosterol. La acumulación de 14 alfa-metil esteroles se correlaciona con la consiguiente pérdida de ergosterol en la pared celular fúngica y puede ser responsable de la actividad fungistática del econazol.» Texto original en inglés: "Ecoza topical foam is an azole antifungal. […] Econazole nitrate, an azole antifungal agent, inhibits fungal cytochrome P-450-mediated 14 alpha-lanosterol demethylase enzyme. This enzyme functions to convert lanosterol to ergosterol. The accumulation of 14 alpha-methyl sterols correlates with the subsequent loss of ergosterol in the fungal cell wall and may be responsible for the fungistatic activity of econazole." ([DailyMed: Ecoza (econazole nitrate) prescribing information, Resilia Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0bb5fa27-32ed-ed13-e063-6394a90a1577), versión del 2023-12-04; consultado el 2026-11-19). Según la información conocida, econazol pertenece a la clase de los antifúngicos imidazólicos, que en general se entiende que inhiben la lanosterol 14-alfa-desmetilasa y alteran la síntesis de ergosterol. Este mecanismo no está confirmado por los datos disponibles.

La infección ectótrix es una dermatofitosis del tallo piloso (por ejemplo, *Microsporum* y *Trichophyton*), en la que las artroconidias se forman en el exterior del pelo. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Sin embargo, es más una extensión dentro de la misma clase de fármacos y el mismo grupo de organismos que un reposicionamiento verdadero.

Hay una limitación práctica importante: cuando hay compromiso del tallo piloso y del folículo, los agentes tópicos penetran poco y suelen preferirse antifúngicos sistémicos. Esto reduce el valor práctico de econazol tópico para esta indicación.

*Predicción secundaria:* el modelo también predice **infección endótrix** (puntaje 0,9997, también L5, Hold), con el mismo razonamiento: el hongo vive dentro del tallo piloso y el econazol tópico llegaría mal a él.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 10790 | FILODERMA PLUS | cr.x 20 g | Teva Argentina | Vigente |
| 14091 | GRISEOCREM NF | pomo x 20 g | Teva Argentina | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Los productos (FILODERMA PLUS, GRISEOCREM NF) son asociaciones de econazol con diflorasona y gentamicina, del fabricante Teva Argentina.

<!-- review:begin ar-lic-20261124-econazole-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Ambas autorizaciones son de un solo principio activo, están vigentes y corresponden al fabricante Teva Argentina.» Corregido: según los datos (listado de medicamentos de PAMI), FILODERMA PLUS y GRISEOCREM NF son asociaciones de econazol con diflorasona y gentamicina; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-econazole-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 41 posibles interacciones, todas con nivel de gravedad no clasificado. Algunas de las principales: clotrimazol, fluconazol, metformina, omeprazol, rosiglitazona, lansoprazol, loperamida, glipizida, dexametasona, clopidogrel, heparina, fluticasona, acetaminofén, levotiroxina, aciclovir, diazepam, didanosina, citarabina y lorazepam.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación que estudie directamente la infección ectótrix con econazol, por lo que la evidencia es solo la predicción del modelo (L5). Además, la penetración tópica limitada en el tallo piloso debilita el caso clínico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), que es un vacío de datos bloqueante para el tamizaje de seguridad.
- Confirmar el mecanismo de acción de econazol con DrugBank.
- Buscar estudios clínicos o in vitro sobre econazol en dermatofitosis del cuero cabelludo o del tallo piloso.
- Evaluar la compatibilidad de la vía de administración (tópica frente a sistémica) y la comparación con antifúngicos sistémicos.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ecoza (econazole nitrate) prescribing information, Resilia Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0bb5fa27-32ed-ed13-e063-6394a90a1577) |
| 2026-11-24 | «de un solo principio activo» → asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

