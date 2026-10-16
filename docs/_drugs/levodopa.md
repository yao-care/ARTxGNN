---
layout: default
title: Levodopa
parent: Solo Predicción del Modelo (L5)
nav_order: 177
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Levodopa: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (según el grafo de conocimiento"
---

# Levodopa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Levodopa: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Levodopa es un precursor de la dopamina, utilizado originalmente para el tratamiento de la enfermedad de Parkinson y de otros trastornos parkinsonianos.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, levodopa es un precursor de la dopamina cuya acción se ejerce sobre la neurotransmisión dopaminérgica en la enfermedad de Parkinson y trastornos parkinsonianos relacionados. Su eficacia en estas indicaciones está establecida.

La encefalitis de Rasmussen es una enfermedad inflamatoria cerebral rara, crónica y unilateral, probablemente mediada por linfocitos T. Cursa con atrofia hemisférica progresiva, crisis focales refractarias (epilepsia parcial continua) y deterioro neurológico. Su patología central es el daño inmunomediado de neuronas y astrocitos, **no un déficit de dopamina**.

No existe un vínculo mecanístico establecido. Una conexión puramente especulativa es que la enfermedad puede afectar los ganglios basales y causar trastornos del movimiento (hemiparesia, distonía), y que entre las indicaciones originales figura el síndrome de hemiparkinsonismo-hemiatrofia, que comparte un rasgo clínico (atrofia unilateral con signos motores). Esa semejanza podría explicar la predicción basada en el grafo, pero no demuestra que levodopa trate la enfermedad subyacente. Además, levodopa podría reducir el umbral convulsivo en algunos pacientes, lo cual sería una preocupación en una enfermedad dominada por crisis epilépticas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 37910 | PARKINEL 250/25 | 250 mg/25 mg comp. x 60 | No disponible |
| 20074 | LECARGE | 250/25 mg comp. x 30 | No disponible |
| 19636 | MADOPAR DISPERSABLE | 62.5 mg tab. dispers. x 100 | No disponible |
| 11017 | LEBOCAR | 250/25 comp. x 60 | No disponible |
| 49290 | SINEMET 250/25 | comp. x 50 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: se asocian con levodopa, entre otras, epilepsia, glaucoma de ángulo abierto y de ángulo cerrado, trastornos psicóticos y otras enfermedades mentales (esquizofreniforme, esquizoafectivo, ansiedad, trastorno neurótico, distimia), enfermedad hepática, renal y de la vesícula biliar, úlcera gástrica y péptica, diabetes mellitus y cetoacidosis diabética, melanoma, infarto de miocardio, trombosis coronaria, paro cardíaco súbito, enfermedad de la conducción cardíaca, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, discinesia inducida por fármacos, hemoglobinopatía y enfermedad diarreica. Destaca la **epilepsia**, por su relevancia directa con la nueva indicación predicha, que cursa con crisis refractarias.
- **Interacciones Farmacológicas**: se registraron 100 interacciones en total; las primeras listadas son:
  - Moderadas: epinefrina, efedrina, bupropión, metronidazol, piridoxina, hierro, metoclopramida y anticolinérgicos (metscopolamina, hiosciamina, atropina, glicopirronio, clidinio, diciclomina, mepenzolato).
  - Menores: antiácidos (hidróxido de aluminio, carbonato de calcio, magaldrato y sales de magnesio).

Las advertencias principales y contraindicaciones del prospecto de ANMAT no están disponibles; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (puntaje alto, pero sin ensayos ni literatura), no existe un vínculo mecanístico plausible con una enfermedad inmunomediada, y existe una preocupación de seguridad relevante por el posible descenso del umbral convulsivo en un cuadro dominado por crisis.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Revisión sistemática de literatura que busque evidencia de levodopa en encefalitis de Rasmussen o en trastornos del movimiento asociados.
- Evaluar de forma específica el riesgo de crisis convulsivas y la compatibilidad de vías de administración (pendiente).
- Si se considerara avanzar, comenzar con estudios preclínicos o de mecanismo antes de cualquier evaluación clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

