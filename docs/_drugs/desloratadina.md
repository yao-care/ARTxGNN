---
layout: default
title: Desloratadina
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 4
drugbank_id: DB00967
monitor_inn: "Desloratadine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
last_modified_at: 2026-11-24
description: "Desloratadina: nueva indicación predicha, enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Desloratadina
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

## Desloratadina: enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Desloratadina es un antihistamínico antagonista selectivo de los receptores H1 periféricos (metabolito activo de la loratadina).
El modelo TxGNN predice que podría ser útil para **enfermedad de la cavidad nasal (nasal cavity disease)**, pero actualmente solo hay **2 publicaciones preclínicas o indirectas** y **ningún ensayo clínico** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Desloratadina (traducción no oficial): «La desloratadina es un antagonista tricíclico de la histamina de acción prolongada con actividad antagonista selectiva de la histamina en los receptores H1. Los datos de unión a receptores indican que, a una concentración de 2-3 ng/mL (7 nanomolar), la desloratadina muestra una interacción significativa con el receptor H1 de la histamina humano.» Texto original en inglés: "Desloratadine is a long-acting tricyclic histamine antagonist with selective H1-receptor histamine antagonist activity. Receptor binding data indicates that at a concentration of 2-3 ng/mL (7 nanomolar), desloratadine shows significant interaction with the human histamine H1-receptor." ([DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f), versión del 2025-10-23; consultado el 2026-11-19). Según la información conocida, la desloratadina es un antagonista selectivo del receptor H1 de histamina de acción periférica y es el metabolito activo de la loratadina. Mecanísticamente, el bloqueo de la histamina podría ser aplicable a la patología de la cavidad nasal, donde la histamina contribuye a los síntomas de tipo alérgico.

El puntaje alto (0,9987) es coherente con esta farmacología conocida, por lo que la predicción parece más un redescubrimiento de un uso ya esperable que un reposicionamiento novedoso. Conviene interpretarla con cautela: el puntaje del modelo no equivale a evidencia clínica.

Las dos publicaciones recuperadas no estudian la desloratadina en la enfermedad nasal de forma directa, por lo que no alcanzan para elevar el nivel de evidencia por encima de L5.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30488351](https://pubmed.ncbi.nlm.nih.gov/30488351/) | 2019 | Estudio animal (preclínico) | European Archives of Oto-Rhino-Laryngology | Modelo de rinitis alérgica inducida por ovoalbúmina en ratas; evalúa hesperidina y timol, no desloratadina. |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Estudio animal (preclínico) | American Journal of Rhinology & Allergy | Modelo felino de congestión nasal; evalúa loratadina (compuesto original) con montelukast, y pseudoefedrina con y sin desloratadina. |

---

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones vigentes de productos con desloratadina como único principio activo (la lista puede ser parcial). No se registra texto de indicación aprobada en los datos locales. Principales autorizaciones:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 52847 | TERALMINA | 5 mg comp.rec.x 7 | Microsules Arg. | Vigente |
| 35738 | HEXALER | jbe.x 60 ml | Siegfried | Vigente |
| 37706 | NOVO ALERPRIV | 5 mg comp.rec.x 20 | Montpellier | Vigente |
| 32833 | FRENALER | 5 mg comp.rec.x 7 | Roemmers | Vigente |
| 50979 | DELORAT | 5 mg comp.rec.x 14 | Lazar | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en dos estudios animales indirectos, ninguno con desloratadina como agente evaluado en esta enfermedad. No hay ensayos clínicos ni datos de seguridad que permitan avanzar.

**Para avanzar se necesita:**
- Estudios clínicos o literatura que evalúen directamente la desloratadina en enfermedad de la cavidad nasal
- Datos del mecanismo de acción confirmados desde fuentes farmacológicas
- Advertencias y contraindicaciones del prospecto de ANMAT
- Definir con precisión el criterio clínico (la categoría "enfermedad de la cavidad nasal" es amplia)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

