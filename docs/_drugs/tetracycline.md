---
layout: default
title: Tetracycline
parent: Evidencia Moderada (L3-L4)
nav_order: 233
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-13
description: "Tetracycline: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L4). Indicación original: Infecciones bacterianas (infección urinaria, bronquitis, neumonía…"
---

# Tetracycline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tetraciclina: De Infecciones Bacterianas (Conjuntivitis, Neumonía, Acné, entre otras) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La tetraciclina es un antibiótico de la clase de las tetraciclinas, utilizado originalmente para tratar infecciones como las urinarias, bronquitis, neumonía, acné, gonorrea y conjuntivitis.
El modelo TxGNN predice que podría ser efectiva para **queratoconjuntivitis epitelial punteada**,
pero actualmente solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de casos) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (infección urinaria, bronquitis, neumonía, acné, conjuntivitis, entre otras, según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la tetraciclina es un antibiótico de amplio espectro de la clase de las tetraciclinas, su eficacia en infecciones como la conjuntivitis (incluida la causada por *Chlamydia*) es conocida, y mecanísticamente podría ser aplicable a la queratoconjuntivitis epitelial punteada.

La queratoconjuntivitis epitelial punteada puede aparecer después de una conjuntivitis folicular por clamidia. Por ello, el vínculo es plausible a través de la actividad antibacteriana contra *Chlamydia*. Además, las tetraciclinas tienen efectos antiinflamatorios y de inhibición de metaloproteinasas de matriz (MMP) que podrían ayudar en la inflamación de la superficie ocular.

Sin embargo, el único artículo disponible describe una queratitis persistente tras la resolución de la infección, lo que sugiere inflamación postinfecciosa y no infección activa. Esta predicción es en gran medida una extensión de la indicación existente de conjuntivitis, y no hay datos de ensayos que respalden a la tetraciclina para esta condición específica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Reporte de casos | Cornea | Dos casos de conjuntivitis folicular por *Chlamydia trachomatis* tratados con tetraciclina oral o doxiciclina; los folículos se resolvieron, pero luego aparecieron lesiones epiteliales punteadas recurrentes y bilaterales en la córnea |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6177 | TETRACICLINA OMEGA | Comprimidos x 16 | No disponible |
| 3657 | SOLUSTRES | Grageas x 16 | No disponible |

## Citotoxicidad

No aplica; la tetraciclina no es un fármaco antineoplásico, por lo que esta sección se omite.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, epilepsia, diabetes mellitus, cetoacidosis diabética, neutropenia, agranulocitosis, gota, neuropatía periférica, trastornos de la coagulación, colitis por *Clostridium difficile*, deficiencia de G6PD, insuficiencia respiratoria, bloqueo auriculoventricular, fibrilación auricular, entre otras.
- **Interacciones farmacológicas**: se identificaron 308 interacciones. Entre las de nivel **mayor** figuran:
  - Isotretinoína
  - Acitretina
  - Ácido aminolevulínico

  También hay interacciones de nivel moderado (por ejemplo, etinilestradiol, amoxicilina, ampicilina, aminofilina, hidróxido de aluminio, atovacuona) y de nivel menor (acetazolamida, hidroclorotiazida, amilorida).
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia es un reporte de casos de 1992 sin ensayos clínicos, por lo que la predicción se apoya sobre todo en la puntuación del modelo (nivel L4). Es una extensión de la indicación existente de conjuntivitis, sin datos que demuestren beneficio en la queratoconjuntivitis epitelial punteada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco
- Revisión sistemática de la literatura sobre tetraciclinas (incluidas doxiciclina y formulaciones oftálmicas) en queratitis epitelial punteada postinfecciosa
- Estudios clínicos controlados que evalúen eficacia y seguridad en esta condición
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de ANMAT
- Evaluación de la vía de administración (la presentación local es oral, mientras que la condición es ocular)
- Revisión de las interacciones farmacológicas y de las contraindicaciones del grafo de conocimiento frente al prospecto oficial

**Otras predicciones del modelo (referencia):**
- **Rinosinusitis crónica** (puntaje 99.15%, nivel L4): hay una revisión Cochrane (2016), una revisión sobre macrólidos y doxiciclina (2020) y un metaanálisis de doxiciclina (2023). La evidencia se refiere sobre todo a la doxiciclina y no a la tetraciclina, por lo que es indirecta. Se considera una pregunta de investigación que merece un estudio enfocado, con salvaguardas por fotosensibilidad, efectos gastrointestinales, la gran carga de interacciones, el riesgo de resistencia con uso prolongado y la evitación en embarazo y niños pequeños.
- **Sinusitis etmoidal crónica** (puntaje 99.15%, nivel L4, Hold): solo hay datos de sensibilidad in vitro; debería evaluarse dentro de la pregunta más amplia de rinosinusitis crónica.
- **Neoplasia de senos paranasales** (puntaje 99.10%, nivel L5, Hold): sin ensayos ni literatura; no se justifica ninguna acción de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

