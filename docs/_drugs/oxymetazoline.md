---
layout: default
title: Oxymetazoline
parent: Solo Predicción del Modelo (L5)
nav_order: 208
evidence_level: L5
indication_count: 2
monitor_inn: "oxymetazoline"
predicted_indications: ["nasal cavity disease", "headache disorder"]
last_modified_at: 2026-10-30
description: "Oxymetazoline: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Oxymetazoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Oximetazolina: agonista adrenérgico alfa tópico → Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Oximetazolina es un descongestivo tópico que actúa sobre receptores adrenérgicos y se comercializa en Argentina en forma de spray nasal.
El modelo TxGNN predice que podría ser útil para **Enfermedad de la cavidad nasal (nasal cavity disease)**,
pero hasta ahora no hay ensayos clínicos registrados y la literatura disponible no estudia directamente esta enfermedad con oximetazolina, por lo que la evidencia es solo de predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0,9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología general, la oximetazolina es un agonista adrenérgico tópico (alfa-1 y alfa-2 parcial) que provoca vasoconstricción de los vasos de la mucosa nasal. Esto reduce la hinchazón y la congestión y mejora la permeabilidad nasal. Los datos de farmacología compilados muestran además afinidad por receptores adrenérgicos alfa-1 (A, B, D) y alfa-2 (A, B, C), y por receptores serotoninérgicos 5-HT1B, 5-HT1D y 5-HT2C.

Este mecanismo es plausible para afecciones de la cavidad nasal con congestión vascular o edema, como la rinitis aguda o la sinusitis. Sin embargo, el puntaje muy alto (0,9996) probablemente refleja la cercanía con usos ya conocidos del fármaco más que una señal novedosa.

Los artículos encontrados son indirectos: describen función olfatoria en rinitis aguda, un modelo de sinusitis en conejo, un caso de rinoscleroma y otros contextos nasales donde la oximetazolina es incidental o una herramienta de medición. Ninguno evalúa directamente la oximetazolina como tratamiento de una enfermedad de la cavidad nasal, por lo que el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Estudio clínico | Annals of the New York Academy of Sciences | Efecto del resfriado común sobre la función olfatoria en 36 sujetos, con potenciales evocados y rinometría acústica |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Preclínico (animal) | Annals of Otology, Rhinology, and Laryngology | Gotas nasales de oximetazolina y su efecto sobre la defensa tisular local en sinusitis aguda en conejos |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Observacional | Journal of Plastic Surgery and Hand Surgery | Permeabilidad nasal por rinometría acústica tras reparación de labio y paladar hendidos; la oximetazolina probablemente se usó como herramienta de medición |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Serie de casos / procedimiento | American Journal of Rhinology & Allergy | Tratamiento con coblación de telangiectasias nasales en telangiectasia hemorrágica hereditaria; papel de la oximetazolina probablemente periprocedimiento |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Reporte de caso | Global Pediatric Health | Rinoscleroma en un niño de 9 años; papel de la oximetazolina poco claro |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43788 | OXILER D | Spray x 10 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: los datos compilados no muestran interacciones con otros fármacos con nivel de gravedad asignado; solo describen la unión a receptores adrenérgicos alfa-1/alfa-2 y serotoninérgicos (5-HT1B, 5-HT1D, 5-HT2C). Además, la literatura revisada señala que los vasoconstrictores simpaticomiméticos pueden interactuar con los inhibidores de la monoaminooxidasa (IMAO), con riesgo de hipertensión.
- **Condiciones que requieren precaución** (relaciones de contraindicación recogidas en los datos compilados, no texto de prospecto): hipertensión, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad cardíaca y cardiovascular, enfermedad coronaria, aterosclerosis, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis), infecciones oculares y conjuntivitis, y trastornos de la visión.

Consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo: no hay ensayos clínicos y ningún estudio citado evalúa directamente la oximetazolina en enfermedad de la cavidad nasal. El puntaje alto probablemente refleja la cercanía con usos ya conocidos del fármaco.

**Para avanzar se necesita:**
- Definir qué condición nasal concreta (por ejemplo, rinitis aguda o sinusitis) se quiere evaluar, ya que "enfermedad de la cavidad nasal" es una categoría amplia
- Estudios clínicos o revisiones que evalúen directamente la oximetazolina en esa condición
- Datos oficiales del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT
- Límites de seguridad respecto a IMAO, enfermedad cardiovascular y glaucoma de ángulo cerrado, y sobre la duración del uso
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

