---
layout: default
title: Hesperidin
parent: Solo Predicción del Modelo (L5)
nav_order: 158
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Hesperidin: nueva indicación predicha, Neoplasia mieloproliferativa (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "hesperidin"
predicted_indications: ["myeloproliferative neoplasm", "monocytic leukemia", "spermatocytic seminoma", "tubular variant testicular seminoma", "gestational trophoblastic neoplasm"]
---

# Hesperidin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Hesperidina: De Indicación Original No Especificada a Neoplasia Mieloproliferativa

## Resumen en Una Frase

Hesperidina es un flavonoide comercializado en Argentina en varios productos de un solo principio activo (por ejemplo, TERBENOL UD, DAFLON y ATUREN). Los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **neoplasia mieloproliferativa**, pero **no hay ensayos clínicos** y solo **1 publicación** (un estudio in silico) respalda esta dirección, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Neoplasia mieloproliferativa |
| Puntaje de Predicción TxGNN | 99,47% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la hesperidina es un flavonoide glucósido (hesperetina unida a rutinosa) que se comercializa en Argentina, solo o asociado a diosmina, en productos de uso vascular. Su eficacia en la indicación original no puede verificarse con los datos compilados, y cualquier aplicabilidad mecanística a la neoplasia mieloproliferativa es hipotética.

El único respaldo es un estudio computacional (in silico) de reposicionamiento de fármacos dirigido al dominio quinasa de BCR en leucemia mieloide crónica (LMC). Como la LMC es una neoplasia mieloproliferativa impulsada por BCR-ABL, existe un vínculo teórico a través de la inhibición del dominio quinasa. Sin embargo, se trata únicamente de una predicción computacional, sin validación experimental ni clínica.

El puntaje alto de TxGNN (0,995) es una predicción del modelo y no constituye evidencia de eficacia. Además, la hesperidina tiene baja biodisponibilidad oral, lo que reduce aún más la plausibilidad traslacional.

Otras predicciones del modelo, con puntajes similares, son leucemia monocítica, seminoma espermatocítico, seminoma testicular de variante tubular y neoplasia trofoblástica gestacional. La leucemia monocítica solo cuenta con un estudio in vitro (nivel L4) y, de forma parcialmente desfavorable, indica que el rutinósido en C7 atenúa la actividad inductora de apoptosis de los flavonoides. Las otras tres no tienen literatura ni ensayos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | Estudio in silico | Asian Pac J Cancer Prev | Cribado computacional de fármacos reposicionados contra el dominio quinasa de BCR en leucemia mieloide crónica, con el objetivo de superar la resistencia a los inhibidores de tirosina quinasa. Sin validación experimental ni clínica. |

---

## Información de Mercado en Argentina

Las autorizaciones listadas no incluyen texto de indicación aprobada. Se muestran 5 de las 20 autorizaciones vigentes (todas de un solo principio activo).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50487 | TERBENOL UD | sobres x 30 | No disponible |
| 57669 | MILCANOR 500 | comprimidos recubiertos x 60 | No disponible |
| 13576 | DAFLON 500 | 500 mg, comprimidos x 30 | No disponible |
| 50329 | DAFLON 1000 | sachets x 30 | No disponible |
| 58280 | ATUREN | 1000 mg, comprimidos recubiertos x 30 | No disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa casi exclusivamente en el modelo TxGNN, con un único estudio in silico, sin ensayos clínicos y con una baja biodisponibilidad oral que limita la plausibilidad traslacional. Además, faltan los datos de seguridad del prospecto, por lo que no es posible avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) y las indicaciones aprobadas.
- Obtener datos del mecanismo de acción (por ejemplo, desde DrugBank) para analizar el vínculo mecanístico.
- Validación experimental in vitro (líneas celulares de LMC y otras neoplasias mieloproliferativas), considerando la actividad de la aglicona hesperetina frente a la hesperidina.
- Evaluar la biodisponibilidad y la viabilidad de alcanzar concentraciones eficaces por vía oral.
- Revisar la compatibilidad de vías de administración y la comparación con las terapias dirigidas ya establecidas para estas neoplasias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

