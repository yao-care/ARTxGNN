---
layout: default
title: Alprazolam
parent: Evidencia Moderada (L3-L4)
nav_order: 22
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Alprazolam: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: Trastorno de ansiedad (según el grafo de conocimiento"
monitor_inn: "ALPRAZOLAM"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Alprazolam
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Alprazolam: De Trastorno de Ansiedad a Insomnio

## Resumen en Una Frase

Alprazolam es una benzodiacepina originalmente utilizada para el tratamiento del trastorno de ansiedad y del trastorno mixto de ansiedad y depresión.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente **no hay ensayos clínicos registrados** y solo se dispone de **18 publicaciones**, en su mayoría indirectas, por lo que la predicción se apoya sobre todo en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de ansiedad (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, alprazolam es una benzodiacepina que potencia la señalización del receptor GABA-A, lo que produce efectos sedantes y ansiolíticos. Su eficacia en los trastornos de ansiedad está bien establecida.

El insomnio suele coexistir con la ansiedad, y la sedación mediada por GABA-A es un mecanismo plausible para mejorar el sueño. Esto explica en parte la alta puntuación del modelo.

Sin embargo, la puntuación es solo una predicción computacional. No hay ensayos clínicos registrados ni ECA directos de alprazolam para insomnio: la literatura revisada incluye sobre todo revisiones sobre trastorno de pánico, farmacocinética, tendencias de uso de benzodiacepinas y desprescripción de zolpidem. Además, alprazolam está indicado principalmente para la ansiedad y no es un hipnótico de primera línea.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguna publicación evalúa directamente la eficacia de alprazolam en insomnio. Las más relevantes son:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Estudio observacional retrospectivo | Medicine | Terapia integrativa (moxibustión, acupuntura auricular) frente a alprazolam en 116 pacientes con cardiopatía coronaria e insomnio; alprazolam fue el grupo control, no la intervención aislada |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Metaanálisis | Acta Pharmaceutica | Tranquilizantes en ancianos con enfermedades crónicas: dosis, resultados y eventos adversos (evidencia indirecta) |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Estudio de prescripción | Sleep Medicine | Patrones de prescripción de "hipnóticos" en una población de atención gestionada |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclínico (ratones) | Aging | La administración repetida de alprazolam causa disfunción mitocondrial y deterioro de la memoria dependiente del hipocampo |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Modelo predictivo | Value in Health Regional Issues | Tendencias y carga económica del uso de benzodiacepinas; el uso prolongado se asocia con pérdida de memoria, dependencia y caídas |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohorte | JHEP Reports | Desprescripción de zolpidem y reducción de caídas y fracturas en cirrosis (no es alprazolam) |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Revisión | American Family Physician | Revisión sobre trastorno de pánico (indirecta) |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opin Drug Metab Toxicol | Farmacocinética de los ansiolíticos (indirecta) |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17228 | TRANQUINAL | 0.25 mg comprimidos x 50 | No disponible |
| 49837 | TRANQUINAL 0.5 | 0.5 mg comprimidos x 60 | No disponible |
| 23721 | ALPRAZOL | 1 mg comprimidos x 30 | No disponible |
| 13402 | BESTROL | 0.5 mg comprimidos x 60 | No disponible |
| 41505 | NOVAZOLAM 0.50 MG | 0.50 mg comprimidos ranurados x 60 | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, glaucoma de ángulo abierto y de ángulo cerrado, obesidad, síndrome de apnea del sueño (incluida la apnea obstructiva) y trastornos relacionados con sustancias/abuso y dependencia.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - **Mayores**: morfina y morfina liposomal (riesgo de depresión del sistema nervioso central y respiratoria).
  - **Moderadas**: aprepitant, bupropión, cimetidina, claritromicina, clotrimazol, miconazol, dronabinol, eliglustat, fenilbutirato de glicerol y metoclopramida.
  - **Menores**: antiácidos (hidróxido de aluminio, carbonato de calcio, compuestos de magnesio) y corticoides (betametasona, dexametasona).
- **Riesgos señalados en la literatura**: dependencia, tolerancia, caídas y deterioro cognitivo, especialmente en adultos mayores.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo es muy alta, pero no hay ensayos registrados ni ECA directos para insomnio, y el uso de benzodiacepinas como hipnóticos conlleva riesgos conocidos de dependencia, caídas y deterioro cognitivo. El nivel de evidencia es L4.

**Para avanzar se necesita:**
- Estudios clínicos controlados que evalúen directamente alprazolam en insomnio, frente a hipnóticos estándar.
- Datos del mecanismo de acción y del prospecto de ANMAT (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Plan de mitigación de riesgos (duración corta, retirada gradual, evitar uso con opioides y alcohol, precaución en adultos mayores).

---

**Nota sobre otras indicaciones predichas:** la **agorafobia** (puntaje 99.56%) tiene mucho mayor respaldo (nivel L1, decisión *Proceed with Guardrails*), con varios estudios controlados de alprazolam en trastorno de pánico con agorafobia, aunque se trata de una indicación cercana a la ya aprobada, con baja novedad. La **tortícolis paroxística benigna de la infancia** (99.61%) carece de evidencia (L5, *Hold*) y presenta un balance riesgo-beneficio desfavorable en lactantes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

