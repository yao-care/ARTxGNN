---
layout: default
title: Hydroquinone
parent: Solo Predicción del Modelo (L5)
nav_order: 160
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
description: "Hydroquinone: nueva indicación predicha, Queratosis seborreica (nivel de evidencia L5). Indicación original: No disponible en la autorización registrada"
monitor_inn: "hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
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

## Hidroquinona: De Indicación No Especificada a Queratosis Seborreica
{: .text-alpha }

## Resumen en Una Frase

La hidroquinona es un agente despigmentante de uso tópico, comercializado en Argentina como MELASMAX en crema. En la autorización disponible no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **queratosis seborreica**, pero actualmente solo hay **1 publicación** de apoyo indirecto y **ningún ensayo clínico** directo, por lo que la evidencia es limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización registrada |
| Nueva Indicación Predicha | Queratosis seborreica |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Hydroquinone (traducción no oficial): «La aplicación tópica de hidroquinona produce una despigmentación reversible de la piel mediante la inhibición de la oxidación enzimática de la tirosina a 3,4-dihidroxifenilalanina (dopa) (Denton, C. et al., 1952)1 y la supresión de otros procesos metabólicos de los melanocitos (Jimbow, K. et al., 1974)2. La exposición a la luz solar o a la luz ultravioleta causará la repigmentación de las zonas despigmentadas (Parrish, L.A. et al., 1978)3.» Texto original en inglés: "Topical application of hydroquinone produces a reversible depigmentation of the skin by inhibition of the enzymatic oxidation of tyrosine to 3,4-dihydroxyphenylalanine (dopa) (Denton, C. et al., 1952)1 and suppression of other melanocyte metabolic processes (Jimbow, K. et al., 1974)2. Exposure to sunlight or ultraviolet light will cause repigmentation of bleached areas (Parrish, L.A. et al., 1978)3." ([DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b), versión del 2026-07-10; consultado el 2026-11-19). Según la información conocida, la hidroquinona inhibe la tirosinasa y reduce la síntesis de melanina, por lo que se usa en trastornos de hiperpigmentación como el melasma.

La queratosis seborreica es una proliferación epidérmica benigna que a veces presenta hiperpigmentación. La hidroquinona podría aclarar ese componente pigmentario en algunas lesiones, pero la queratosis seborreica no es principalmente un trastorno de producción de melanina, por lo que el ajuste mecanístico es indirecto.

El puntaje alto de TxGNN (0.9973) es una predicción computacional y no está respaldado por datos clínicos directos. El único estudio disponible es observacional y trata trastornos pigmentarios faciales en general, no queratosis seborreica como objetivo principal.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratosis seborreica.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Estudio observacional de cohorte prospectivo | J Plast Reconstr Aesthet Surg | Algoritmo de tratamiento combinado para trastornos pigmentarios faciales en pacientes asiáticos; la mayoría presenta varios trastornos a la vez. No evalúa la queratosis seborreica como objetivo principal. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 2609 | MELASMAX | Crema x 10 g | No especificada en el registro |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: quemadura solar, insuficiencia adrenocortical, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente, enfermedad arterial periférica, eccema atópico y dermatitis.
- No se encontraron interacciones farmacológicas registradas.

Consultar el prospecto para información adicional de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un puntaje computacional alto, pero sin ensayos clínicos y con un único estudio observacional indirecto. El mecanismo es indirecto y no hay datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT con advertencias y contraindicaciones, y confirmar la indicación aprobada
- Completar los datos del mecanismo de acción
- Buscar estudios que evalúen hidroquinona directamente en queratosis seborreica
- Evaluar la seguridad en relación con las condiciones cutáneas señaladas por el modelo TxGNN (aprendizaje profundo) (dermatitis, atrofia cutánea, eccema atópico), que pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica

---

**Nota sobre otras predicciones evaluadas:** queratosis folicular invertida vulvar (L5), exantema (L4) y enfermedad liquenoide (L4) también quedan en *Hold*. Las tres carecen de evidencia directa y en el caso del exantema la predicción parece un artefacto de mapeo de etiquetas.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

