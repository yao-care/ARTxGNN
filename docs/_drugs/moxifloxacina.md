---
layout: default
title: Moxifloxacina
parent: Solo Predicción del Modelo (L5)
nav_order: 266
evidence_level: L5
indication_count: 9
drugbank_id: DB00218
monitor_inn: "Moxifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
last_modified_at: 2026-11-20
description: "Moxifloxacina: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 10 (en el listado vigente: 10)"
---

# Moxifloxacina
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

## Moxifloxacina: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Moxifloxacina es un antibiótico fluoroquinolónico comercializado en Argentina en presentaciones sistémicas y oftálmicas.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (10 de 10) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 10 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Moxifloxacina (traducción no oficial): «Moxifloxacino Tableta es un miembro de la clase de agentes antibacterianos de las fluoroquinolonas. […] La acción bactericida del moxifloxacino resulta de la inhibición de la topoisomerasa II (DNA girasa) y de la topoisomerasa IV, necesarias para la replicación, la transcripción, la reparación y la recombinación del DNA bacteriano.» Texto original en inglés: "Moxifloxacin Tablet is a member of the fluoroquinolone class of antibacterial agents. […] The bactericidal action of moxifloxacin results from inhibition of the topoisomerase II (DNA gyrase) and topoisomerase IV required for bacterial DNA replication, transcription, repair, and recombination." ([DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5), versión del 2026-11-06; consultado el 2026-11-19). Según la información conocida, moxifloxacina es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su uso es antibacteriano.

Con base en el análisis de los datos compilados, **no se identifica un vínculo mecanístico plausible** con la nueva indicación: moxifloxacina no tiene efecto conocido sobre la viscosidad sérica ni sobre los niveles de inmunoglobulinas. El puntaje elevado (0,9998) es solo una salida del modelo y no está respaldado por estudios reales.

Por lo tanto, la predicción debe considerarse una hipótesis sin sustento mecanístico ni clínico en este momento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Las 10 autorizaciones registradas están vigentes y corresponden a productos de un solo principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 43812 | AVELOX I.V. | 400 mg solución para infusión x 250 ml |
| 58352 | FLOMOX | Solución oftálmica x 5 ml |
| 36318 | VIGAMOX | 0,5 % solución oftálmica x 5 ml |
| 25691 | AVELOX | 400 mg comprimidos recubiertos x 5 |
| 56081 | MOXIBASE | 400 mg comprimidos recubiertos x 10 |

Se muestran las 5 principales; existen otras 5 autorizaciones vigentes (AVELOX x 7, MOXIDROP, MOFLAG, VIGADEXA y MOFLAG D).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no cuenta con ensayos clínicos ni literatura, no tiene un mecanismo plausible y su nivel de evidencia es L5. No hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que explique un efecto sobre la viscosidad sérica o las inmunoglobulinas
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Obtener del prospecto de ANMAT las advertencias y contraindicaciones, y los datos del mecanismo de acción
- Contrastar la predicción con otras opciones de mayor sustento antes de asignar recursos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

