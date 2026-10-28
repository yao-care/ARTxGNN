---
layout: default
title: Ezetimibe
parent: Solo Predicción del Modelo (L5)
nav_order: 140
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
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
| Estado de Mercado en Argentina | Comercializado (registros vigentes: al menos 20) |
| Número de Autorizaciones | Al menos 20 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento general, ezetimibe inhibe la absorción intestinal de colesterol mediada por NPC1L1 y reduce el colesterol LDL.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

