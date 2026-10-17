---
layout: default
title: Entacapone
parent: Solo Predicción del Modelo (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Entacapone: nueva indicación predicha, Neurodegeneración asociada a PLA2G6 (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson"
monitor_inn: "ENTACAPONE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Entacapona: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapona es un inhibidor de la COMT, originalmente utilizado para el tratamiento de la enfermedad de Parkinson y de varios síndromes parkinsonianos relacionados.
El modelo TxGNN predice que podría ser efectivo para **Neurodegeneración asociada a PLA2G6**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (las licencias locales no incluyen texto de indicación aprobada; la indicación proviene del grafo de conocimiento) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, entacapona es un inhibidor de la catecol-O-metiltransferasa (COMT) que se emplea junto con levodopa para prolongar su efecto en la enfermedad de Parkinson. En Argentina se comercializa como parte de la combinación Stalevo.

La neurodegeneración asociada a PLA2G6 incluye fenotipos de distonía-parkinsonismo con compromiso dopaminérgico. Por ello, la inhibición de la COMT podría, en teoría, prolongar el efecto de la levodopa en estos pacientes. Es una hipótesis plausible, pero no está respaldada por ningún ensayo ni publicación.

El puntaje del modelo es muy alto, pero puede reflejar en parte la cercanía en la red de conocimiento y el solapamiento con las indicaciones parkinsonianas existentes, y no necesariamente un efecto biológico demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45029 | STALEVO 125 | 125 mg comp. rec. x 30 | No especificada en los datos |
| 46200 | STALEVO 150 | 150 mg comp. rec. x 100 | No especificada en los datos |
| 43440 | STALEVO 200 | 200 mg comp. rec. x 30 | No especificada en los datos |
| 35401 | STALEVO 50 | 50 mg comp. rec. x 30 | No especificada en los datos |
| 35403 | STALEVO 150 | 150 mg comp. rec. x 30 | No especificada en los datos |

Se muestran 5 de las 8 autorizaciones vigentes (todas del titular Biosidus S.A.U.).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): hipotensión ortostática, atrofia multisistémica, discinesia inducida por fármacos, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica, glaucoma de ángulo abierto y de ángulo cerrado, trastornos psicóticos y otros trastornos mentales, diabetes mellitus y cetoacidosis diabética, melanoma, infarto de miocardio, paro cardíaco súbito y enfermedad de la conducción cardíaca, entre otras.
- **Interacciones farmacológicas**: se identificaron 82 interacciones. Las de nivel moderado incluyen epinefrina (también oftálmica y tópica), morfina (incluida la liposomal), dronabinol, opio, nabilona, metoclopramida y hierro. Otras con nivel no clasificado incluyen pantoprazol, doxiciclina, metformina, omeprazol, lansoprazol, atropina, lactulosa, prednisona, simvastatina y cloruro de potasio.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura específicos para neurodegeneración asociada a PLA2G6. El mecanismo es plausible pero no está demostrado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de entacapona para analizar el vínculo mecanístico con la nueva indicación
- Texto oficial del prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas)
- Estudios preclínicos o series de casos en neurodegeneración asociada a PLA2G6 con distonía-parkinsonismo
- Evaluación de compatibilidad de vías de administración y de la similitud con la indicación original

---

### Nota sobre otras predicciones

Entre las demás indicaciones predichas, la **demencia con cuerpos de Lewy** (puntaje 99.25%, nivel L4) es la única con algún respaldo indirecto: un estudio in vitro sobre agentes antiparkinsonianos y la formación de oligómeros de α-sinucleína, y un ensayo de fase 1 de imagen diagnóstica que no evalúa entacapona. Se la considera una pregunta de investigación, no una recomendación clínica. El resto de las predicciones (por ejemplo, mielitis, encefalitis de Rasmussen y deficiencias metabólicas) carece de vínculo mecanístico evidente y de evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

