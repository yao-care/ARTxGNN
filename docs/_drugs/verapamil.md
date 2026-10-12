---
layout: default
title: Verapamil
parent: Solo Predicción del Modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Verapamilo: De Hipertensión Arterial a Bloqueo de Rama (término obsoleto)

## Resumen en Una Frase

Verapamilo es un bloqueador de los canales de calcio, utilizado originalmente para tratar la hipertensión, la fibrilación auricular, el síndrome coronario agudo, la angina de Prinzmetal y la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectivo para **bloqueo de rama (término obsoleto en la ontología)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
La predicción se basa únicamente en el modelo y debe interpretarse con mucha cautela.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno hipertensivo / hipertensión (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Bloqueo de rama (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, verapamilo es un bloqueador de los canales de calcio tipo L que enlentece la conducción del nodo auriculoventricular y produce vasodilatación, lo que respalda su uso en hipertensión y arritmias supraventriculares.

Sin embargo, la relación mecanística con la nueva indicación **no es convincente**. El bloqueo de rama es una alteración del sistema His-Purkinje, no del nodo AV, y enlentecer la conducción podría empeorar el trastorno. Además, el término está marcado como obsoleto en la ontología, por lo que su relevancia clínica es dudosa. El puntaje alto (0.996) refleja una predicción basada en el grafo, no una evidencia terapéutica.

**Otras predicciones del modelo (todas con evidencia débil):**

| Posición | Indicación predicha | Puntaje | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Enfermedad renal hipertensiva maligna | 99.27% | L5 | Extensión plausible de la indicación antihipertensiva, sin evidencia específica |
| 3 | Hipertensión renovascular maligna | 99.27% | L5 | Mecanismo indirecto; los 2 artículos recuperados no evalúan verapamilo |
| 4 | Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 99.26% | L4 | Apoyo preclínico indirecto; los bloqueadores de calcio generalmente no se recomiendan en este grupo |
| 5 | Hipertensión pulmonar multifactorial de mecanismo incierto | 99.26% | L5 | Preocupación por el efecto inotrópico negativo |
| 6 | Síndrome de Braddock | 99.15% | L5 | Sin vínculo mecanístico evidente |
| 7 | Parálisis periódica con síndrome compartimental transitorio | 99.08% | L5 | Hipótesis de canalopatía, pero podría empeorar la debilidad muscular |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para bloqueo de rama.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 23137 | VERAL | Comprimidos de liberación prolongada 240 mg x 30 | No especificada en los datos |
| 20438 | ISOPTINO | Comprimidos recubiertos 80 mg x 30 | No especificada en los datos |
| 2141 | ISOPTINO MD | Comprimidos recubiertos 240 mg x 30 | No especificada en los datos |
| 4642 | ISOPTINO RETARD | Comprimidos recubiertos 120 mg x 20 | No especificada en los datos |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (incluidas las formas hereditaria y adquirida), neutropenia, agranulocitosis, estenosis aórtica, hipotensión, miocardiopatía hipertrófica, miastenia gravis, taquicardia ventricular, bloqueo auriculoventricular e insuficiencia cardíaca.
- **Interacciones farmacológicas**: se identificaron 328 interacciones. Entre las principales:
  - **Mayor**: loperamida.
  - **Moderada**: hidrocortisona, metformina, bupropión, aprepitant, triamcinolona, ácido acetilsalicílico, dexametasona, betametasona, budesonida, canagliflozina, cimetidina, claritromicina y sales de calcio (fosfato, acetato, carbonato, cloruro, citrato).
  - **Menor**: morfina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene solo respaldo del modelo (L5), sin ensayos ni literatura. Además, el mecanismo del verapamilo (enlentecimiento de la conducción) podría agravar el bloqueo de rama, y el término es obsoleto en la ontología.

**Para avanzar se necesita:**
- Revisar si la indicación predicha es clínicamente válida o reemplazarla por una entidad vigente.
- Obtener datos del mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de ANMAT para advertencias y contraindicaciones oficiales (necesario antes de cualquier evaluación de seguridad).
- Priorizar la evaluación de las predicciones relacionadas con hipertensión (posiciones 2 y 3), que son más coherentes con la indicación original, y buscar evidencia clínica específica.
- Realizar una búsqueda dirigida de ensayos clínicos y literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

