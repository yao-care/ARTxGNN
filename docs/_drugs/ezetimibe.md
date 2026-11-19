---
layout: default
title: Ezetimibe
parent: Solo Predicción del Modelo (L5)
nav_order: 140
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-20
description: "Ezetimibe: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Hiperlipidemia"
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Ezetimibe: De Hiperlipidemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol
{: .text-alpha }

## Resumen en Una Frase

Ezetimibe es un fármaco hipolipemiante utilizado originalmente para tratar la hiperlipidemia y la hipercolesterolemia familiar. El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero no hay **ningún ensayo clínico** ni estudio que aborde directamente esta enfermedad; solo hay **2 publicaciones** de contexto general sobre lípidos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperlipidemia (según las relaciones registradas en el grafo de conocimiento; las licencias locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0,9909 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ezetimibe (traducción no oficial): «La ezetimiba reduce el colesterol en sangre al inhibir la absorción del colesterol en el intestino delgado. Se ha demostrado que la diana molecular de la ezetimiba es el transportador de esteroles Niemann-Pick C1-Like 1 (NPC1L1), que participa en la captación intestinal del colesterol y de los fitoesteroles.» Texto original en inglés: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), versión del 2026-10-08; consultado el 2026-11-19). Según el conocimiento general, ezetimibe inhibe la absorción intestinal de colesterol mediada por NPC1L1 y reduce el colesterol LDL.

La deficiencia de CETP es una condición genética en la que la transferencia de ésteres de colesterol desde las HDL hacia las lipoproteínas con apoB está alterada, lo que suele producir HDL-C elevado y LDL-C más bajo. Ambas situaciones comparten vías del metabolismo lipídico, lo que probablemente explica el puntaje alto del modelo.

Sin embargo, la deficiencia de CETP habitualmente no se reconoce como una enfermedad que requiera tratamiento. No existe una justificación terapéutica clara para ezetimibe, y la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La relación con la indicación original es indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revisión | European Heart Journal | Panorama de dianas para reducir lípidos (LDL-C, triglicéridos, apoB, Lp(a)); no estudia directamente la deficiencia de CETP |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Estudio animal | Int J Mol Sci | Modelo de hámster con deficiencia heterocigota de Ldlr para evaluar un anticuerpo anti-PCSK9; no evalúa ezetimibe en deficiencia de CETP |

Ninguna de las publicaciones estudia directamente la enfermedad predicha.

## Información de Mercado en Argentina

La lista de autorizaciones es parcial (se muestran 20 registros, con al menos 20 en total); los registros no incluyen texto de indicación aprobada. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33428 | ZETIA | 10 mg comprimidos x 28 | No disponible en el registro |
| 35857 | EZETROL | 10 mg comprimidos x 30 | No disponible en el registro |
| 35799 | VADEL | 10 mg comprimidos x 30 | No disponible en el registro |
| 36512 | ALIPAS | 10 mg comprimidos x 30 | No disponible en el registro |
| 33900 | TRILIP | 10 mg comprimidos x 30 | No disponible en el registro |

## Consideraciones de Seguridad

- **Enfermedades con contraindicación registrada en el grafo de conocimiento** (no proviene del texto del prospecto): pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedades musculares y del músculo esquelético, parálisis periódica familiar, abuso/dependencia de sustancias, rabdomiólisis y fascitis nodular.
- **Interacciones farmacológicas** (100 registradas; se destacan las de nivel moderado): ácido quenodesoxicólico, eluxadolina, rosuvastatina y simvastatina. Otras interacciones tienen nivel no clasificado, por ejemplo calcitriol, pantoprazol, glimepirida, metformina y omeprazol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción se basa solo en el modelo (L5): no hay ensayos ni estudios que aborden directamente la deficiencia de CETP, y esta condición no suele requerir tratamiento.

**Para avanzar se necesita:**
- Justificar clínicamente si la deficiencia de CETP constituye una necesidad terapéutica real.
- Datos del mecanismo de acción y análisis mecanístico específico.
- Revisión del prospecto aprobado por ANMAT (advertencias y contraindicaciones).
- Evidencia directa (preclínica o clínica) sobre ezetimibe en esta condición.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

