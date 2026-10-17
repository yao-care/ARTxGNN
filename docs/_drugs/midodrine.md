---
layout: default
title: Midodrine
parent: Solo Predicción del Modelo (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Midodrine: nueva indicación predicha, Prionopatía sensible a proteasas de forma variable (nivel de evidencia L5). Indicación original: Hipotensión ortostática"
monitor_inn: "MIDODRINE"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
---

# Midodrine
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

# Midodrina: De Hipotensión Ortostática a Prionopatía Sensible a Proteasas de Forma Variable

## Resumen en Una Frase

La midodrina se utiliza originalmente para el tratamiento de la hipotensión ortostática y otros trastornos de la regulación autonómica de la presión arterial.
El modelo TxGNN predice que podría ser efectiva para la **prionopatía sensible a proteasas de forma variable**, una enfermedad neurodegenerativa por plegamiento anómalo de proteínas.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipotensión ortostática (también atrofia multisistémica y síndrome de taquicardia postural ortostática, según el grafo de conocimiento; los registros locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Prionopatía sensible a proteasas de forma variable |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, la midodrina es un profármaco cuyo metabolito activo, la desglimidodrina, es un agonista adrenérgico alfa-1 periférico. Aumenta el tono arteriolar y venoso y eleva la presión arterial, lo que respalda su uso en la hipotensión ortostática.

La relación con la nueva indicación es débil. La prionopatía sensible a proteasas de forma variable es una enfermedad neurodegenerativa causada por el plegamiento anómalo de proteínas, y no existe un vínculo mecanístico identificable con la acción vasoconstrictora periférica de la midodrina. Además, la desglimidodrina no atraviesa de forma significativa la barrera hematoencefálica.

El puntaje tan alto del modelo (99.99%) parece ser un artefacto del grafo de conocimiento. Podría estar relacionado con rasgos autonómicos compartidos con otros trastornos neurodegenerativos, y ningún ensayo ni publicación lo respalda. No debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 43726 | GUTRON | Comprimidos 2.5 mg x 20 |
| 43727 | GUTRON | Comprimidos 2.5 mg x 50 |

Ambas autorizaciones son de producto único y están vigentes. No hay autorizaciones canceladas.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): feocromocitoma (de glándula suprarrenal), paraganglioma simpático, cáncer de duodeno, cáncer de intestino delgado, cáncer de corazón, cáncer de glándula suprarrenal, tirotoxicosis, hipertiroidismo y enfermedad de Graves.
- **Interacciones farmacológicas**: se registraron 81 interacciones. Entre las listadas, las de nivel moderado incluyen:
  - simpaticomiméticos y vasoconstrictores: epinefrina (incluidas las formas oftálmica y tópica), efedrina (incluida la nasal) e isometepteno;
  - anorexígenos y estimulantes: fentermina, dietilpropión, mazindol, sibutramina y lorcaserina;
  - otros: bupropión, trospio, rolapitant y fenilbutirato de glicerol.

  Las interacciones menores incluyen ranitidina, cimetidina y metformina. La interacción con calcitriol es de nivel desconocido.
- **Consideraciones clínicas generales** (según el análisis de la indicación): riesgo de hipertensión en posición supina, retención urinaria y bradicardia refleja. Esta última es especialmente relevante en trastornos del nodo sinusal.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura que la respalden (nivel L5), y no existe un vínculo mecanístico plausible entre un agonista alfa-1 periférico y una prionopatía. El puntaje alto del modelo parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Evidencia preclínica o mecanística que justifique siquiera una hipótesis de eficacia en esta enfermedad.
- Datos detallados del mecanismo de acción (MOA) y del texto del prospecto aprobado en Argentina (advertencias y contraindicaciones).
- Revisión de las contraindicaciones del grafo de conocimiento frente a cualquier población de estudio.

**Nota complementaria:** entre las otras predicciones del modelo, el *trastorno hipotensivo* (puntaje 99.90%) tiene un ensayo de Fase 2 completado (NCT02893553, n=21, en lesión medular) y una extensa literatura de revisión. Alcanza el nivel L2 con recomendación *Proceed with Guardrails*. Es una extensión cercana al uso aprobado y la dirección más prometedora para el reposicionamiento de este fármaco. Las predicciones relacionadas con el nodo sinoauricular (enfermedad y bloqueo) deben considerarse como alertas de seguridad (bradicardia refleja), no como candidatas terapéuticas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

