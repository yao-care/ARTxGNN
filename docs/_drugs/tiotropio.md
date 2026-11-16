---
layout: default
title: Tiotropio
parent: Solo Predicción del Modelo (L5)
nav_order: 345
evidence_level: L5
indication_count: 4
drugbank_id: DB01409
monitor_inn: "Tiotropium"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
last_modified_at: 2026-11-16
description: "Tiotropio: nueva indicación predicha, Respiratory malformation (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tiotropio
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Tiotropio: Respiratory malformation
{: .text-alpha }

## Resumen en Una Frase

Tiotropio es un broncodilatador inhalado antagonista muscarínico de acción prolongada, comercializado en Argentina como SPIRIVA RESPIMAT. Su indicación aprobada local no figura en los datos compilados para este informe.
La evidencia se concentra en la enfermedad pulmonar obstructiva crónica (EPOC).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Respiratory malformation |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción formal del mecanismo de acción del fármaco. La literatura revisada lo describe como un antagonista muscarínico de acción prolongada. Bloquea los receptores M3 del músculo liso de la vía aérea. Esto produce una broncodilatación sostenida y reduce el tono colinérgico y la secreción de moco. Los estudios farmacológicos indican que se disocia muy lentamente de los receptores M1 y M3, lo que permite una administración una vez al día.

La obstrucción del flujo aéreo, característica de la enfermedad pulmonar obstructiva, depende en buena parte de ese tono colinérgico. Por eso el mecanismo es biológicamente aplicable. La categoría está dominada por la EPOC, donde existen varios ensayos de Fase 3 grandes, incluido uno de más de 17.000 pacientes (TIOSPIR).

Para esta indicación, la predicción es más confirmatoria que novedosa. Se apoya en un uso clínico ampliamente documentado del fármaco.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes para la enfermedad predicha, de un total de 40 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Fase 3 | Completado | 914 | Tiotropio 18 µg/día vs. placebo durante 48 semanas; evalúa el cambio del VEF1 valle según el estado tabáquico en EPOC |
| [NCT01126437](https://clinicaltrials.gov/study/NCT01126437) | Fase 3 | Completado | 17.183 | TIOSPIR: compara tiotropio Respimat (2,5 y 5 µg) con HandiHaler 18 µg en seguridad y exacerbaciones |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Fase 3 | Completado | 5.993 | Tiotropio vs. placebo sobre la tasa de declive de la función pulmonar en EPOC |
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Fase 3 | Completado | 2.624 | TONADO 1: tiotropio + olodaterol vs. cada componente durante 52 semanas en EPOC |
| [NCT02796677](https://clinicaltrials.gov/study/NCT02796677) | Fase 3 | Completado | 1.595 | Aclidinio/formoterol vs. monoterapias y tiotropio 18 µg durante 24 semanas en EPOC estable |
| [NCT00929110](https://clinicaltrials.gov/study/NCT00929110) | Fase 3 | Completado | 1.066 | Glicopirronio vs. placebo durante 52 semanas, con brazo abierto de tiotropio, en EPOC |
| [NCT01970878](https://clinicaltrials.gov/study/NCT01970878) | Fase 3 | Completado | 892 | Extensión de seguridad de 28 semanas con tiotropio HandiHaler como control activo en EPOC moderada a muy grave |
| [NCT01072396](https://clinicaltrials.gov/study/NCT01072396) | Fase 4 | Completado | 126 | Tiotropio vs. placebo (cruzado, 6 semanas) sobre hiperinsuflación dinámica y capacidad de ejercicio en EPOC temprana |
| [NCT00144196](https://clinicaltrials.gov/study/NCT00144196) | Fase 4 | Completado | 224 | SPIRIMILD: tiotropio vs. placebo durante 12 semanas en EPOC leve |
| [NCT01483625](https://clinicaltrials.gov/study/NCT01483625) | Fase 4 | Completado | 140 | Tiotropio vs. placebo durante 12 semanas en EPOC con infección respiratoria aguda |

## Evidencia de Literatura

Se muestran 10 de las 20 publicaciones, priorizando ensayos aleatorizados y luego revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | ECA | N Engl J Med | Evalúa si el uso prolongado de tiotropio mejora la función pulmonar y frena su declive en EPOC leve a moderada |
| [31119643](https://pubmed.ncbi.nlm.nih.gov/31119643/) | 2019 | Revisión | Drugs | Revisión de tiotropio/olodaterol como mantenimiento a largo plazo en EPOC |
| [26683033](https://pubmed.ncbi.nlm.nih.gov/26683033/) | 2016 | Revisión | Drugs | Ensayos de Fase 3 de 6 a 52 semanas de tiotropio/olodaterol en obstrucción del flujo aéreo por EPOC |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Revisión | Drugs | Perfil farmacológico: antagonismo M1/M2/M3 con disociación lenta de M3 y mejora de la función pulmonar en EPOC con dosis única diaria de 18 µg |
| [15596697](https://pubmed.ncbi.nlm.nih.gov/15596697/) | 2004 | Revisión | Chest | Broncodilatación de más de 24 h por bloqueo prolongado de M3; mejora la espirometría y los volúmenes pulmonares |
| [10673478](https://pubmed.ncbi.nlm.nih.gov/10673478/) | 2000 | Revisión | Chest | Propiedades farmacológicas: unos 10 veces más potente que ipratropio en pulmón humano |
| [11281822](https://pubmed.ncbi.nlm.nih.gov/11281822/) | 2001 | Revisión | Expert Opin Investig Drugs | Anticolinérgico de acción prolongada con efecto broncodilatador en estudios de Fase II |
| [31540819](https://pubmed.ncbi.nlm.nih.gov/31540819/) | 2019 | Revisión | Semergen | Broncodilatadores en la prevención de exacerbaciones; tiotropio es el principio activo con mayor evidencia |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Revisión | Curr Med Res Opin | Evidencia de tiotropio + olodaterol para reducir exacerbaciones, según las recomendaciones GOLD 2020 |
| [29583021](https://pubmed.ncbi.nlm.nih.gov/29583021/) | 2018 | Revisión | COPD | Resumen anual de 2017 que incluye el tratamiento con tiotropio en pacientes leves a moderados |

## Información de Mercado en Argentina

El estado de mercado es **comercializado**. La autorización registrada está vigente.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45181 | SPIRIVA RESPIMAT | Solución para inhalación, 30 dosis + inhalador | No registrada en los datos locales |

## Consideraciones de Seguridad

No se registraron interacciones farmacológicas en la consulta realizada. Los datos de advertencias y contraindicaciones del prospecto no están disponibles. Consultar el prospecto para información de seguridad.

Como puntos de vigilancia, los antagonistas muscarínicos inhalados se asocian a efectos anticolinérgicos, como retención urinaria y glaucoma de ángulo estrecho. También conviene revisar la seguridad cardiovascular en pacientes de edad avanzada. Estos puntos deben verificarse contra el prospecto aprobado.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados y de gran tamaño, como TIOSPIR, SAFE y el estudio de declive de la función pulmonar. A ellos se suman metaanálisis y revisiones que respaldan la eficacia y seguridad de tiotropio en enfermedad pulmonar obstructiva, principalmente EPOC. Esto corresponde a un nivel de evidencia L1. Sin embargo, faltan los datos de seguridad del prospecto local, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones).
- Confirmar la población y la formulación autorizadas (Respimat frente a HandiHaler).
- Completar los datos del mecanismo de acción desde una fuente de referencia farmacológica.
- Definir un plan de monitoreo de efectos anticolinérgicos y de seguridad cardiovascular en pacientes de edad avanzada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

