---
layout: default
title: Oxazepam
parent: Evidencia Moderada (L3-L4)
nav_order: 207
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-13
description: "Oxazepam: nueva indicación predicha, Insomnio (nivel de evidencia L3). Indicación original: Delirium por abstinencia alcohólica y ansiedad"
monitor_inn: "OXAZEPAM"
predicted_indications: ["insomnia (disease)"]
---

# Oxazepam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

## Oxazepam: De Delirium por Abstinencia Alcohólica y Ansiedad a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Oxazepam es una benzodiacepina de acción corta, originalmente utilizada para el delirium por abstinencia alcohólica y la ansiedad.
El modelo TxGNN predice que podría ser efectivo para **insomnio**,
pero hasta ahora **no hay ensayos clínicos registrados** y solo **10 publicaciones** de relevancia variable (solo unas pocas tratan directamente oxazepam en insomnio o sueño) respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Delirium por abstinencia alcohólica y ansiedad (según la base de conocimiento del modelo; el registro local no incluye texto de indicación) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida de la clase, oxazepam es una benzodiacepina de acción corta que actúa como modulador alostérico positivo de los receptores GABA-A, potenciando la neurotransmisión inhibitoria. Este mecanismo es compartido por la clase y es el que sustenta su eficacia en ansiedad y abstinencia alcohólica.

El efecto sedante-hipnótico derivado de esta modulación se vincula plausiblemente con una mejor iniciación y mantenimiento del sueño. La ansiedad y el insomnio suelen coexistir, lo que refuerza la coherencia de la predicción. Cabe señalar que este vínculo se infiere de la farmacología de clase y no de datos del registro.

Desde el punto de vista farmacocinético, oxazepam tiene una vida media intermedia, no genera metabolitos activos y se elimina por glucuronidación, lo que puede ser conveniente en pacientes mayores o con insuficiencia hepática. Sin embargo, esas mismas características pueden limitar su utilidad como hipnótico por su duración de acción. El puntaje de 99.86% es una predicción computacional y no sustituye la evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | Ensayo clínico comparativo | Am J Psychiatry | Oxazepam y flurazepam mejoraron algunas medidas polisomnográficas del sueño nocturno en 14 pacientes con insomnio crónico; flurazepam produjo somnolencia diurna importante y oxazepam no, aunque hubo cierto rebote |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | Ensayo clínico (probablemente aleatorizado) | Ann Pharmacother | Compara melatonina y oxazepam sobre ansiedad y calidad del sueño en pacientes con infarto con elevación del ST tras angioplastia primaria |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Revisión/estudio en ancianos | Arch Gerontol Geriatr | Eficacia y seguridad de hipnóticos en insomnio en mayores de 70 años (60 pacientes); relevancia indirecta para oxazepam |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opin Drug Metab Toxicol | Farmacocinética de fármacos ansiolíticos |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Revisión | J Clin Exp Hepatol | Manejo del síndrome de abstinencia alcohólica en hepatopatía alcohólica; relación indirecta con la indicación original |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Revisión | Psychiatr Prax | Manejo de síntomas conductuales y psicológicos de la demencia; indirecto |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Estudio observacional | PeerJ | Uso potencialmente inadecuado y a largo plazo de benzodiacepinas y fármacos Z en adultos mayores; contexto de seguridad |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Estudio clínico (casos) | JAMA | Síndrome de abstinencia tras sustituir una benzodiacepina de acción prolongada por una de acción corta (incluido oxazepam); contexto de seguridad |

Nota: se omitieron dos publicaciones sin relación con la eficacia de oxazepam (un reporte de caso sobre agomelatina y una revisión sobre paroxetina en trastorno de pánico).

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 23427 | PAUSAFREN T | Comprimidos x 40 | Sin texto de indicación registrado |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): trastornos de ansiedad y neuróticos, distimia, porfiria, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trastornos psicóticos (incluida esquizofrenia y trastorno esquizoafectivo), trastornos hipotensivos, apnea obstructiva del sueño, insuficiencia respiratoria y enfermedad pulmonar, trastornos por uso de sustancias, trastornos de la personalidad y trastorno explosivo intermitente.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las listadas:
  - **Mayores**: morfina (incluida la forma liposomal), por riesgo de depresión del sistema nervioso central y respiratoria.
  - **Moderadas**: bupropión, dronabinol, nabilona, metoclopramida, opio, sibutramina y teduglutida.
  - **Menores**: antiácidos (hidróxido de aluminio, magaldrato, carbonato de calcio, óxido, carbonato e hidróxido de magnesio).
- **Riesgos de clase a considerar como salvaguardas**: dependencia, abstinencia (incluido el síndrome de rebote), sedación al día siguiente, caídas y deterioro cognitivo en adultos mayores, y especial cuidado con opioides, alcohol y otros depresores del sistema nervioso central.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero la evidencia directa es limitada: no hay ensayos registrados y solo dos estudios clínicos pequeños y antiguos o de diseño por verificar abordan oxazepam en sueño. Además, la carga de interacciones y los riesgos de dependencia y sedación son considerables, y el insomnio ya cuenta con múltiples alternativas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción verificados en una fuente primaria (p. ej., DrugBank)
- Prospecto de ANMAT con advertencias y contraindicaciones oficiales, y texto de indicación aprobada
- Revisión del diseño y los resultados completos de los estudios PMID 6691478 y 29749262
- Ensayos controlados modernos de oxazepam en insomnio, con evaluación de somnolencia diurna y abstinencia
- Evaluación de compatibilidad de vías y formas farmacéuticas para la nueva indicación
- Plan de mitigación de riesgos para poblaciones vulnerables (adultos mayores, hepatopatía, uso concomitante de opioides o alcohol)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

