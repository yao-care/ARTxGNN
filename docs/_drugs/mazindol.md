---
layout: default
title: Mazindol
parent: Solo Predicción del Modelo (L5)
nav_order: 184
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Mazindol: nueva indicación predicha, Hipervitaminosis (nivel de evidencia L5). Indicación original: Trastorno de obesidad y obesidad monogénica (según el grafo de conoci…"
monitor_inn: "MAZINDOL"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny", "postural orthostatic tachycardia syndrome", "pentosuria", "lethal polymalformative syndrome, Boissel type"]
---

# Mazindol
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

# Mazindol: De Trastorno de Obesidad a Hipervitaminosis

## Resumen en Una Frase

Mazindol es un anorexígeno simpaticomimético, originalmente utilizado para el tratamiento de la obesidad (incluida la obesidad monogénica).
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de obesidad y obesidad monogénica (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mazindol es un simpaticomimético anorexígeno que inhibe la recaptación de catecolaminas (noradrenalina y dopamina), y su uso en obesidad está establecido.

Sin embargo, **no se identifica un vínculo mecanístico evidente** con la nueva indicación. La hipervitaminosis es un estado de toxicidad que se resuelve suspendiendo la fuente de la vitamina, no modulando la señalización monoaminérgica. El puntaje tan alto del modelo (0,99998) parece ser un artefacto del grafo de conocimiento, sin ensayos clínicos ni literatura que lo respalden.

### Otras predicciones del modelo (todas con nivel L5 y decisión Hold)

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome de microdeleción proximal 16p11.2 | 99.997% | Única conexión indirecta: esta deleción es causa genética de obesidad grave de inicio temprano. Mazindol podría, como máximo, actuar sobre el fenotipo de peso, no sobre las demás manifestaciones del síndrome. |
| Hipertelorismo (término obsoleto) | 99.991% | Malformación craneofacial estructural; ningún mecanismo farmacológico plausible. |
| Frontorrinia | 99.986% | Malformación congénita craneofacial rara; sin vínculo mecanístico. |
| Síndrome de taquicardia postural ortostática (POTS) | 99.604% | La predicción biológicamente más interesante, pero con alerta de seguridad: los inhibidores del transportador de noradrenalina (p. ej., atomoxetina) tienden a empeorar la taquicardia en POTS, por lo que mazindol probablemente agravaría los síntomas. |
| Pentosuria | 99.352% | Error congénito benigno del metabolismo, asintomático; no requiere tratamiento. |
| Síndrome polimalformativo letal tipo Boissel | 99.041% | Síndrome congénito extremadamente raro y letal; la predicción se basa solo en similitud en el grafo. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50919 | MZ1 (Eurofarma) | 1 mg, comprimidos recubiertos x 30 | No disponible en los datos |
| 50920 | MZ2 (Eurofarma) | 2 mg, comprimidos recubiertos x 30 | No disponible en los datos |
| 51529 | FAGOLIP PLUS (Cetus) | Comprimidos x 30 | No disponible en los datos |
| 33936 | DIMAGRIR (Gador) | Cápsulas x 30 | No disponible en los datos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las más relevantes de las listadas son:
  - **Mayores**: tramadol, bupropión, azul de metileno, lorcaserina.
  - **Moderadas** (selección): fentanilo, alfentanilo, fenilefrina, pseudoefedrina, epinefrina, isometepteno, salbutamol, formoterol, arformoterol, amitriptilina, etanol, amifampridina, y antidiabéticos (acarbosa, alogliptina, pioglitazona, albiglutida).
- **Alerta específica de la predicción POTS**: por su acción sobre la recaptación de noradrenalina, mazindol podría agravar la taquicardia; requeriría una evaluación de seguridad cuidadosa antes de cualquier exploración.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones carecen de ensayos clínicos y de literatura (nivel L5), y no existe un vínculo mecanístico plausible; la predicción principal (hipervitaminosis) parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de ANMAT (actualmente no disponibles, lo que bloquea el cribado de seguridad)
- Textos de las indicaciones aprobadas en las autorizaciones locales
- Evidencia preclínica o clínica que justifique cualquier nueva indicación; si se explora alguna, priorizar el fenotipo de obesidad del síndrome 16p11.2 y evitar POTS salvo con una evaluación de seguridad previa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

