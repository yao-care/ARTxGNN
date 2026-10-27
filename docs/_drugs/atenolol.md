---
layout: default
title: Atenolol
parent: Solo Predicción del Modelo (L5)
nav_order: 36
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Atenolol: nueva indicación predicha, Infarto de miocardio posterolateral (nivel de evidencia L5). Indicación original: Hipertensión arterial e infarto de miocardio (según el grafo de conoc…"
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Atenolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Atenolol: De Hipertensión Arterial a Infarto de Miocardio Posterolateral
{: .text-alpha }

## Resumen en Una Frase

Atenolol es un betabloqueante cardioselectivo, originalmente utilizado para el tratamiento de la hipertensión arterial y del infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para el **infarto de miocardio posterolateral**, aunque actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden específicamente esta predicción.
Se trata de un subtipo anatómico de una indicación ya conocida, por lo que el puntaje alto refleja sobre todo la cercanía en la ontología y no una señal real de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial e infarto de miocardio (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Infarto de miocardio posterolateral |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, atenolol es un betabloqueante selectivo del receptor beta-1. Su bloqueo reduce la frecuencia cardíaca, la contractilidad y la demanda de oxígeno del miocardio, que es el fundamento de su uso tras un infarto.

El infarto de miocardio posterolateral es un subtipo anatómico del infarto de miocardio, una indicación original del fármaco. Por ello, la predicción es plausible, pero no constituye un reposicionamiento genuino: el puntaje elevado refleja la proximidad con la indicación ya establecida.

Otras predicciones del modelo (infarto posteroinferior y septal, hipertensión renovascular maligna, hipertensión pulmonar, cor pulmonale crónico) siguen la misma lógica o son más débiles. En las formas pulmonares, además, los betabloqueantes exigen cautela por el riesgo de reducir el gasto cardíaco o empeorar el broncoespasmo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (infarto de miocardio posterolateral).

Como referencia, para el infarto posteroinferior (segunda predicción, mismo puntaje) se recuperó un único estudio:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | ECA (simple ciego, cruzado, pequeño) | La Revue de médecine interne | Comparación de la actividad antiisquémica de atenolol (200 mg) y diltiazem (240 mg) en 23 pacientes en readaptación, 4 semanas después de un infarto posteroinferior o anterior, mediante prueba de esfuerzo computarizada. Estudio pequeño, antiguo e indirecto. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 3849 | ATENOLOL GADOR (Gador) | Comprimidos 100 mg x 28 | No disponible en los datos |
| 32121 | ATENOLOL MICROSULES (Microsules Arg.) | Comprimidos 50 mg x 28 | No disponible en los datos |
| 59354 | VERICORDIN (Lazar) | Comprimidos 100 mg x 60 | No disponible en los datos |
| 35433 | PLENACOR 50 (Bagó) | Comprimidos 50 mg x 60 | No disponible en los datos |
| 34628 | ATENOLOL GADOR (Gador) | Comprimidos 25 mg x 30 | No disponible en los datos |

Hay 20 autorizaciones vigentes, todas de monofármaco; se muestran las 5 primeras.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): bloqueo auriculoventricular, asma (incluidas las formas intrínseca y alérgica), diabetes mellitus tipo 1 y 2, cetoacidosis diabética, enfermedad de Raynaud, anafilaxia, insuficiencia hepática, pancreatitis, lupus eritematoso sistémico, psoriasis, gota, anuria y trastornos del calcio, fósforo y potasio, entre otros.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado incluyen epinefrina, hidrocortisona, hioscina, bupropión, triamcinolona, morfina, acetohexamida, atropina, betametasona, budesonida y diversas sales de calcio. Las de nivel menor incluyen ácido acetilsalicílico, hidróxido de aluminio y attapulgita.
- **Contexto pulmonar**: en hipertensión pulmonar y enfermedad pulmonar crónica, los betabloqueantes, incluso los cardioselectivos, pueden empeorar el broncoespasmo o reducir el gasto cardíaco.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde a un subtipo de una indicación ya establecida, sin ensayos ni literatura específica, por lo que no aporta una señal nueva de reposicionamiento. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Confirmar si la indicación de infarto de miocardio figura en el prospecto aprobado por ANMAT (los textos de indicación están vacíos en los datos).
- Obtener las advertencias y contraindicaciones oficiales del prospecto de ANMAT.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar si conviene priorizar otras predicciones con un componente de reposicionamiento más claro, o descartar las que son meros subtipos de indicaciones ya aprobadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

