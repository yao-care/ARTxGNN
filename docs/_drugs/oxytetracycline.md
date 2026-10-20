---
layout: default
title: Oxytetracycline
parent: Solo Predicción del Modelo (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Oxytetracycline: nueva indicación predicha, Rinosinusitis crónica (nivel de evidencia L5). Indicación original: Infección del tracto urinario (según el grafo de conocimiento"
monitor_inn: "oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
---

# Oxytetracycline
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

# Oxitetraciclina: De Infección del Tracto Urinario a Rinosinusitis Crónica

## Resumen en Una Frase

La oxitetraciclina es un antibiótico de la familia de las tetraciclinas, utilizado originalmente para infecciones bacterianas como las del tracto urinario, bronquitis, neumonía y conjuntivitis.
El modelo TxGNN predice que podría ser efectivo para **rinosinusitis crónica**, pero para esta indicación **no hay ensayos clínicos ni publicaciones** que respalden la predicción; se trata únicamente de una predicción del modelo.
La única indicación predicha con literatura es la otitis externa (17 publicaciones, en su mayoría antiguas y sobre productos combinados), que se comenta más abajo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Rinosinusitis crónica |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la oxitetraciclina es una tetraciclina de amplio espectro con actividad antibacteriana, su eficacia en infecciones como las del tracto urinario, respiratorias y oculares está establecida, y mecanísticamente podría ser aplicable a la rinosinusitis crónica.

Las tetraciclinas también tienen efectos antiinflamatorios y de inhibición de metaloproteinasas de matriz (MMP) descritos en la literatura, que podrían relacionarse con la inflamación sinusal crónica. Además, la cobertura antibacteriana de patógenos sinusales es una vía plausible. Este razonamiento es hipotético: no hay estudios que lo confirmen para esta indicación.

Otras predicciones del modelo con puntajes similares (sinusitis etmoidal crónica, 99.61%; queratoconjuntivitis epitelial punteada, 99.52%) muestran un patrón parecido. Algunas, como la neoplasia de senos paranasales o la cardiomiopatía de Chagas, carecen de una justificación mecanística clara y probablemente reflejan la cercanía en el grafo de conocimiento y no una relación terapéutica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para rinosinusitis crónica (la indicación principal predicha) actualmente no hay literatura relacionada disponible.

Como referencia, para la predicción de rango 10, **otitis externa** (puntaje 99.27%, nivel L3), se identificaron publicaciones. Se listan las más relevantes (ECA y estudios comparativos primero); varias clasificaciones son tentativas porque solo se dispone del título:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8222746](https://pubmed.ncbi.nlm.nih.gov/8222746/) | 1993 | Estudio comparativo aleatorizado | Curr Med Res Opin | 30 pacientes con otitis externa: ciprofloxacino en gotas vs. combinación de oxitetraciclina, polimixina B e hidrocortisona, durante 7 días |
| [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/) | 1985 | ECA | Arch Otorhinolaryngol | 55 pacientes: framicetina/gramicidina vs. oxitetraciclina/hidrocortisona con polimixina B; 78% curados, sin diferencias significativas entre tratamientos |
| [2156538](https://pubmed.ncbi.nlm.nih.gov/2156538/) | 1990 | Estudio aleatorizado (tentativo) | Eur Arch Otorhinolaryngol | 46 pacientes: butirato de hidrocortisona vs. oxitetraciclina/hidrocortisona/polimixina B; tasa global de curación 80% |
| [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/) | 2005 | Estudio clínico aleatorizado abierto | J Laryngol Otol | 51 pacientes: betametasona sola vs. hidrocortisona con oxitetraciclina y polimixina B |
| [11583468](https://pubmed.ncbi.nlm.nih.gov/11583468/) | 2001 | Modelo animal | Eur Arch Otorhinolaryngol | En ratas, un esteroide tópico sin antibiótico fue eficaz en otitis externa; se comparó con hidrocortisona más oxitetraciclina |
| [12019482](https://pubmed.ncbi.nlm.nih.gov/12019482/) | 2002 | Reporte clínico | Am J Otolaryngol | Uso de polvo ótico en otitis externa aguda |
| [13447965](https://pubmed.ncbi.nlm.nih.gov/13447965/) | 1957 | Reporte clínico | Eye Ear Nose Throat Mon | Tratamiento de otitis externa con suspensión de Terra-Cortril |
| [13313924](https://pubmed.ncbi.nlm.nih.gov/13313924/) | 1956 | Reporte clínico | Am Pract Dig Treat | Gotas óticas de terramicina-polimixina en oídos infectados |
| [14412537](https://pubmed.ncbi.nlm.nih.gov/14412537/) | 1959 | Reporte clínico | Monatsschr Ohrenheilkd | Otitis externa tratada con oxitetraciclina e hidrocortisona |
| [6412426](https://pubmed.ncbi.nlm.nih.gov/6412426/) | 1983 | In vitro | Vet Microbiol | EDTA-Tris combinado con antimicrobianos frente a bacterias patógenas (contexto veterinario) |

La evidencia se refiere sobre todo a productos tópicos combinados, por lo que es difícil aislar el aporte propio de la oxitetraciclina, y las comparaciones con ciprofloxacino y con esteroides solos no muestran una superioridad clara.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6413 | TERRA CORTRIL (Pfizer) | Ungüento tópico 14.2 g | No disponible |
| 28596 | TERRA CORTRIL (Pfizer) | Spray x 100 ml | No disponible |

---

## Consideraciones de Seguridad

Según el grafo de conocimiento (no el texto del prospecto), la oxitetraciclina figura con contraindicación o precaución en: enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de G6PD, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, insuficiencia respiratoria, fibrilación auricular, bloqueo auriculoventricular, síndrome de Adams-Stokes, síndrome de Wolff-Parkinson-White, deficiencia de potasio, galactosemia, cistinuria, enfermedad por almacenamiento de glucógeno y piouréter.

- **Interacciones Farmacológicas**: se identificaron 144 interacciones; entre las principales mostradas:
  - **Mayor**: vitamina A.
  - **Moderadas**: sales de calcio, magnesio y zinc (acetato y fosfato de calcio, óxido, sulfato y cloruro de magnesio, sulfato y acetato de zinc), citrato de potasio, amoxicilina, balsalazida y varias insulinas (aspart, degludec, detemir, glargina, glulisina, humana).
  - **Menor**: manitol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para rinosinusitis crónica se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, las autorizaciones locales corresponden a formas tópicas (ungüento y spray), cuya aplicabilidad a una patología sinusal no está establecida.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la oxitetraciclina
- Texto de indicaciones, advertencias y contraindicaciones del prospecto ANMAT
- Revisión de la literatura específica sobre tetraciclinas en rinosinusitis crónica
- Evaluación de compatibilidad de vías de administración (las formas autorizadas son tópicas)
- Si se prioriza otitis externa, una revisión sistemática que separe el efecto de la oxitetraciclina del de los esteroides y otros antibióticos asociados, considerando que es en esencia una indicación tópica de uso histórico y no un reposicionamiento novedoso
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

