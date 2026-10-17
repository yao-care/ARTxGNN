---
layout: default
title: Heparin
parent: Solo Predicción del Modelo (L5)
nav_order: 157
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
description: "Heparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (nivel de evidencia L5). Indicación original: Embolia pulmonar, coagulación intravascular diseminada"
---

# Heparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Heparina: De Embolia Pulmonar a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)

## Resumen en Una Frase

La heparina es un anticoagulante utilizado originalmente en el tratamiento de la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectiva para **trombofilia por deficiencia de proteína C (autosómica recesiva)**, pero actualmente no hay **ningún ensayo clínico ni publicación** que respalde esta indicación específica; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar, coagulación intravascular diseminada, púrpura fulminante (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.29% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la heparina potencia la acción de la antitrombina e inhibe la trombina y el factor Xa, lo que la convierte en un anticoagulante de amplio uso.

La deficiencia grave de proteína C genera un estado de hipercoagulabilidad. La heparina ya se emplea en la púrpura fulminante, una complicación típica de esta deficiencia, y esa similitud probablemente explique el puntaje tan alto del modelo. Mecanísticamente, contrarrestar la hipercoagulabilidad con un anticoagulante es plausible.

Sin embargo, el tratamiento estándar en la deficiencia congénita grave es el concentrado de proteína C, y la heparina sería, como mucho, un complemento. No hay ensayos ni literatura para esta indicación, por lo que la evidencia es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (trombofilia por deficiencia de proteína C).

Nota: para la segunda indicación predicha (trastorno de liberación plaquetaria primario) se recuperaron 20 publicaciones, pero ninguna evalúa a la heparina como tratamiento de esa condición; tratan sobre trombocitopenia inducida por heparina, coagulación en cirrosis, tromboembolismo asociado a cáncer, entre otros. Esa predicción parece un falso positivo con posible riesgo de seguridad (la heparina podría empeorar el sangrado), por lo que no se desarrolla en este informe.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42347 | HEPATRIET (Craveri) | Gel tópico x 60 g | No disponible en los datos |
| 44887 | CYCLOPARIN (Siegfried) | Gel tópico x 60 g | No disponible en los datos |

Las dos autorizaciones vigentes corresponden a formulaciones **tópicas** (gel). Esto es relevante: la nueva indicación predicha (trombofilia sistémica) requeriría anticoagulación sistémica, por lo que las presentaciones comercializadas localmente no serían adecuadas para ella.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedades hematológicas, trombocitopenia (incluida la inducida por heparina), trastornos de la coagulación, hemofilia, déficit de antitrombina III, defectos plaquetarios cualitativos (incluida la trombastenia de Glanzmann), hemorragia intracraneal e intracerebral, desprendimiento de placenta, úlcera péptica activa, colitis ulcerosa y enfermedad inflamatoria intestinal, enfermedad de las vías biliares e ictericia obstructiva, endocarditis infecciosa, retinopatías (diabética, hipertensiva), osteoporosis y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se identificaron 614 interacciones. Entre las de nivel moderado figuran el ácido acetilsalicílico y varios hipoglucemiantes (clorpropamida, glimepirida, repaglinida, nateglinida, tolazamida, glipizida, glibenclamida, acetohexamida, tolbutamida), además de fenfluramina, dexfenfluramina y sibutramina. Otras interacciones, de nivel desconocido, incluyen levocarnitina, manitol, calcitriol, vitamina A, pantoprazol, mesalazina y doxiciclina.

No se dispone de advertencias ni contraindicaciones del prospecto de ANMAT; se debe consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y de literatura (nivel L5). Además, el estándar de tratamiento es el concentrado de proteína C, y las presentaciones locales son geles tópicos, no sistémicos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallados (por ejemplo, desde DrugBank)
- Prospecto de ANMAT con advertencias y contraindicaciones oficiales
- Revisión de la literatura clínica sobre heparina en deficiencia de proteína C y púrpura fulminante neonatal
- Evaluación de la compatibilidad de vía de administración (se requeriría una formulación sistémica)
- Análisis de seguridad, dadas las numerosas contraindicaciones hematológicas y hemorrágicas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

