---
layout: default
title: Ibuprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 161
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Ibuprofen: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide (según el grafo de conocimiento"
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
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

# Ibuprofeno: De Artritis Reumatoide a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

El ibuprofeno es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para tratar la artritis reumatoide, la osteoartritis, las cefaleas y otras afecciones articulares.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, el ibuprofeno es un inhibidor no selectivo de la ciclooxigenasa (COX) con efectos antiinflamatorios y analgésicos, y su eficacia en enfermedades articulares inflamatorias como la artritis reumatoide y la osteoartritis está bien establecida.

Sin embargo, el análisis de la relación mecanística no respalda la predicción. La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética rara causada por variantes de pérdida de función en CDMP1/GDF5, que alteran la condrogénesis y la formación de las extremidades. El ibuprofeno no actúa sobre la vía de señalización GDF5/BMP.

El puntaje alto del modelo (0.997) probablemente refleja la cercanía en el grafo de conocimiento con términos musculoesqueléticos y de artropatía, y no un fundamento farmacológico. En el mejor de los casos, el ibuprofeno podría aliviar el dolor de problemas articulares secundarios, lo cual es manejo sintomático y no modificación de la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46593 | IBUMAR 600 | 600 mg comp. x 20 | No disponible |
| 40445 | IBUPROFENO 600 FECOFAR | 600 mg comp. x 10 | No disponible |
| 38942 | IBUTENK | 800 mg comp. x 10 | No disponible |
| 46707 | ACTRON PEDIATRICO 4% | Suspensión oral x 100 ml | No disponible |
| 3744 | IBUPIRAC 600 MG | comp. x 20 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia hepática, enfermedad renal, enfermedad hepática, epilepsia, EPOC, trombocitopenia, hipotiroidismo, enfermedad ulcerosa péptica, enfermedad inflamatoria intestinal, lupus eritematoso sistémico, diabetes mellitus, cetoacidosis diabética, hiperplasia prostática benigna, hipotensión, trastornos de la coagulación, enfermedad cerebrovascular, accidente cerebrovascular, infarto cerebral e infarto de miocardio, entre otras.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales mostradas:
  - **Mayor**: ácido acetilsalicílico.
  - **Moderada**: corticoides (betametasona, budesonida, dexametasona, hidrocortisona), sulfonilureas (acetohexamida, clorpropamida, glimepirida, glipizida, gliburida), aprepitant, balsalazida, fenfluramina y dexfenfluramina, exenatida, kanamicina y levofloxacina.
  - **Menor**: famotidina, ranitidina y cimetidina.
- Para la exposición prenatal a AINE existe una preocupación de seguridad, especialmente relevante en malformaciones congénitas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico creíble entre la inhibición de COX y una displasia esquelética de origen genético. Las otras seis predicciones evaluadas (por ejemplo, braquiolmia, pseudoacondroplasia, miosclerosis) presentan el mismo perfil de evidencia y también quedan en espera.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y un fundamento biológico que conecte el ibuprofeno con la vía GDF5/BMP
- Estudios preclínicos que demuestren algún efecto sobre la enfermedad
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente faltante
- Si el interés es solo el control sintomático del dolor, evaluar ese objetivo de forma separada, sin considerarlo reposicionamiento modificador de la enfermedad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

