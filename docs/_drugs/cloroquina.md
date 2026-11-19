---
layout: default
title: Cloroquina
parent: Solo Predicción del Modelo (L5)
nav_order: 122
evidence_level: L5
indication_count: 4
drugbank_id: DB00608
monitor_inn: "Chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
last_modified_at: 2026-11-16
description: "Cloroquina: nueva indicación predicha, artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis) (nivel de evidencia L5)."
---

# Cloroquina
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

## Cloroquina: artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis)
{: .text-alpha }

## Resumen en Una Frase

Cloroquina es un antipalúdico con actividad inmunomoduladora. El modelo TxGNN predice que podría ser útil para la **artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis)**. Actualmente no hay ensayos clínicos registrados y solo hay **1 publicación** vinculada, que trata sobre leflunomida y no sobre cloroquina, por lo que la evidencia directa es prácticamente nula.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis) |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cloroquina (traducción no oficial): «La cloroquina, una 4-aminoquinolina, es un agente antiprotozoario. Se desconoce el mecanismo preciso por el cual la cloroquina ejerce su actividad. La cloroquina puede ejercer su efecto contra las especies de Plasmodium concentrándose en las vesículas ácidas del parásito e inhibiendo la polimerización del hemo.» Texto original en inglés: "Chloroquine, a 4-aminoquinoline, is an anti-protozoal agent. The precise mechanism by which chloroquine exhibits activity is not known. Chloroquine, may exert its effect against Plasmodium species by concentrating in the acid vesicles of the parasite and by inhibiting polymerization of heme." ([DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570), versión del 2026-10-21; consultado el 2026-11-19). Según la información conocida, la cloroquina es un antipalúdico con efecto inmunomodulador: eleva el pH lisosomal, reduce el procesamiento y la presentación de antígenos, inhibe la señalización de los receptores TLR y disminuye la producción de citocinas proinflamatorias. Estas acciones son plausibles frente a una artritis poliarticular de base autoinmune.

Sin embargo, la única publicación vinculada a esta predicción específica estudia leflunomida en artritis idiopática juvenil, no cloroquina. Por lo tanto, ningún estudio citado evalúa directamente esta enfermedad con el fármaco. El puntaje alto refleja la cercanía en la red del modelo con enfermedades de tipo reumatoide, no datos clínicos.

Como el estudio disponible no aborda directamente la enfermedad con cloroquina, el nivel de evidencia se establece en L5 (solo predicción del modelo), aunque el sistema de puntuación interno haya asignado L4.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohorte | The Journal of Rheumatology | Experiencia prospectiva de largo plazo con leflunomida en artritis idiopática juvenil; no evalúa cloroquina |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 7082 | NIVAQUINE | Comprimidos x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no existen ensayos clínicos ni estudios que evalúen la cloroquina en esta enfermedad. La única publicación vinculada trata sobre otro fármaco (leflunomida).

**Para avanzar se necesita:**
- Datos de mecanismo de acción verificados (por ejemplo, desde DrugBank)
- Prospecto de ANMAT con advertencias y contraindicaciones para completar la evaluación de seguridad
- Revisión específica de la literatura sobre cloroquina en artritis idiopática juvenil poliarticular con factor reumatoide positivo
- Evaluación de seguridad retiniana y de conducción cardíaca antes de cualquier consideración adicional, dado que la hidroxicloroquina ha reemplazado en gran medida a la cloroquina en la práctica reumatológica

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

