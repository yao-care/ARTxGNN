---
layout: default
title: Acetazolamida
parent: Solo Predicción del Modelo (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
drugbank_id: DB00819
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-11-24
description: "Acetazolamida: nueva indicación predicha, hipertermia maligna inducida por ejercicio (exercise-induced malignant hyperthermia) (nivel de evidencia L5)."
---

# Acetazolamida
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

## Acetazolamida: hipertermia maligna inducida por ejercicio (exercise-induced malignant hyperthermia)
{: .text-alpha }

## Resumen en Una Frase

Acetazolamida es un fármaco con dos autorizaciones vigentes en Argentina, ambas como producto de un solo principio activo.
El modelo TxGNN predice que podría ser útil para **hipertermia maligna inducida por ejercicio (exercise-induced malignant hyperthermia)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipertermia maligna inducida por ejercicio (exercise-induced malignant hyperthermia) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Acetazolamida (traducción no oficial): «La acetazolamida es un potente inhibidor de la anhidrasa carbónica, eficaz en el control de la secreción de líquidos (p. ej., algunos tipos de glaucoma), en el tratamiento de ciertos trastornos convulsivos (p. ej., epilepsia) y en la promoción de la diuresis en casos de retención anormal de líquidos (p. ej., edema cardíaco). La acetazolamida no es un diurético mercurial.» Texto original en inglés: "Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic." ([DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b), versión del 2026-11-10; consultado el 2026-11-19). Por conocimiento general, la acetazolamida inhibe la anhidrasa carbónica, lo que modifica el pH y el manejo de iones, y se usa en trastornos musculares como las parálisis periódicas.

Una hipótesis puramente especulativa es que esa modulación del pH y de los iones en el músculo esquelético podría influir en la hipertermia maligna. Sin embargo, ningún dato muestra beneficio en esta enfermedad ni en la desregulación del calcio mediada por el receptor de rianodina que la caracteriza.

El puntaje muy alto (0,9995) sin ninguna evidencia de respaldo sugiere que podría tratarse de un artefacto de los embeddings del modelo, por lo que la predicción debe tomarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 48845 | ACETA | 250 mg comp.x 20 | Novoplos | Vigente |
| 45899 | DIABO | 250 mg comp.x 50 | Max Vision | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo, sin ensayos ni publicaciones sobre esta enfermedad (nivel L5), y no existe un mecanismo plausible que la sustente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (por ejemplo, desde DrugBank) y una evaluación de su relación con la fisiopatología de la hipertermia maligna
- Revisión sistemática de la literatura específica sobre acetazolamida e hipertermia maligna
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias y contraindicaciones), requisito previo a cualquier evaluación de seguridad
- Estudios preclínicos que respalden la hipótesis antes de considerar ensayos clínicos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: «No se identificaron autorizaciones de comercialización vigentes» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido (revisado el 2026-11-24; versión anterior conservada en el registro)) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

