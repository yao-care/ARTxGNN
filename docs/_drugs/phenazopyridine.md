---
layout: default
title: Phenazopyridine
parent: Solo Predicción del Modelo (L5)
nav_order: 211
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Phenazopyridine: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: No disponible en la licencia de ANMAT (el fármaco se describe como an…"
monitor_inn: "phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Fenazopiridina: De Analgésico Urinario a Bronquitis
{: .text-alpha }

## Resumen en Una Frase

La fenazopiridina es un analgésico del tracto urinario, comercializado en Argentina como UROTEM DOL; el texto de indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la licencia de ANMAT (el fármaco se describe como analgésico del tracto urinario) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fenazopiridina es un analgésico que actúa localmente sobre la mucosa del tracto urinario, aunque su mecanismo exacto no está bien caracterizado.

No se ha establecido un vínculo mecanístico con la bronquitis. No se conoce una vía farmacológica que conecte a este fármaco con la inflamación bronquial o la infección respiratoria. Su uso original (alivio sintomático urinario) y la nueva indicación (enfermedad de las vías respiratorias) son áreas terapéuticas muy distintas.

El puntaje alto de TxGNN (0.992) proviene únicamente de la predicción del grafo de conocimiento y no está respaldado por evidencia clínica ni bibliográfica. Podría reflejar artefactos de la red, como vecinos compartidos con otros fármacos o genes, y no una relación biológica real. Esta predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 30587 | UROTEM DOL | Comprimidos (10 + 10) | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provienen del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática (incluida encefalopatía/coma hepático), enfermedad renal, porfiria, enfermedad pulmonar obstructiva crónica, apnea del sueño, enfermedad arterial coronaria, hiperplasia prostática benigna, trastornos de ansiedad y neuróticos, abuso/dependencia de sustancias, enfermedad de la vesícula biliar, y trastornos hematológicos (anemia, trombocitopenia, neutropenia, agranulocitosis). Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 24 interacciones, de las cuales se listan 20 en los datos disponibles.
  - **Mayores**: ácido nitroso, leflunomida.
  - **Moderadas** (principales): naltrexona, anestésicos locales (lidocaína, benzocaína, tetracaína, oxibuprocaína, cinchocaína, cocaína), metotrexato, asparaginasa, pegaspargasa, brentuximab vedotina, clofarabina, idelalisib e interferón beta-1a/1b.

Para las advertencias y contraindicaciones del prospecto, consultar el prospecto oficial de ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible entre un analgésico urinario local y la bronquitis. Además, el perfil de seguridad no está completo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica y de ensayos específica para fenazopiridina y enfermedades respiratorias.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original.
- Reconsiderar la decisión solo si se identifica evidencia preclínica o mecanística que sustente la hipótesis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

