---
layout: default
title: Aniracetam
parent: Evidencia Moderada (L3-L4)
nav_order: 33
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-30
description: "Aniracetam: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: No disponible en los registros de ANMAT compilados"
monitor_inn: "ANIRACETAM"
predicted_indications: ["insomnia (disease)"]
---

# Aniracetam
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Aniracetam: De Indicación No Especificada a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Aniracetam es un fármaco comercializado en Argentina como PERGAMID (Pfizer); en los registros de ANMAT disponibles no consta el texto de su indicación aprobada, y se lo describe de forma general como un nootrópico (potenciador cognitivo).
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente no hay ensayos clínicos registrados y solo se dispone de **2 publicaciones** de apoyo limitado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros de ANMAT compilados |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0,9923 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, aniracetam es un nootrópico que se describe como modulador de la transmisión glutamatérgica de tipo AMPA, y la base de datos farmacológica consultada lo muestra como ligando de los receptores GluA1, GluA2, GluA3 y GluA4 (genes GRIA1–GRIA4). Se trata de conocimiento de contexto y no de una confirmación del mecanismo en los datos aportados.

Mecanísticamente, la modulación glutamatérgica (y posibles efectos colinérgicos y monoaminérgicos) podría influir en circuitos relacionados con el sueño. Sin embargo, no hay una indicación original documentada con la cual comparar, por lo que no es posible establecer una relación directa entre la indicación original y el insomnio.

El puntaje de TxGNN (0,9923) es únicamente una predicción computacional. La única señal clínica es un informe de 1998 en el que aniracetam se usó junto con zopiclona; esto apunta a un contexto de terapia complementaria y no a un efecto propio de aniracetam sobre el insomnio.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9628149](https://pubmed.ncbi.nlm.nih.gov/9628149/) | 1998 | Informe clínico de terapia combinada | Psychiatry and Clinical Neurosciences | Nueve pacientes de edad avanzada con insomnio asociado a trastornos cerebrales (infarto cerebral, cerebroatrofia, Alzheimer, Parkinson) recibieron zopiclona más aniracetam; el tratamiento fue efectivo en 7 de 9 casos (78%). Diseño no controlado y muestra muy pequeña. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Observacional (análisis de datos del mundo real) | Zhongguo Zhong Yao Za Zhi (China Journal of Chinese Materia Medica) | Análisis de datos hospitalarios de 20 hospitales nacionales sobre enfermedades concurrentes y uso de medicamentos (medicina tradicional china y occidental) en pacientes con insomnio. No evalúa directamente la eficacia de aniracetam. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17308 | PERGAMID | 750 mg comprimidos x 60 | No especificada en los datos disponibles |
| 17307 | PERGAMID | 750 mg comprimidos x 30 | No especificada en los datos disponibles |

Ambas autorizaciones son de monofármaco, vigentes, y su titular es Pfizer.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y devolvió 4 registros, todos de tipo farmacológico (no interacciones medicamentosas clínicas con nivel de gravedad): aniracetam actúa como ligando de los receptores de glutamato GluA1, GluA2, GluA3 y GluA4 (GRIA1–GRIA4). No se informan interacciones con otros fármacos.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es alta, pero la evidencia real se limita a un informe clínico pequeño de 1998 con terapia combinada (zopiclona + aniracetam) y a un estudio observacional que no evalúa eficacia. No hay ensayos clínicos, no se conoce la indicación aprobada localmente y no se dispone de datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada de PERGAMID)
- Confirmar el mecanismo de acción a partir de fuentes como DrugBank
- Evaluar la plausibilidad mecanística entre la modulación AMPA y los circuitos del sueño
- Buscar o diseñar estudios controlados que evalúen aniracetam solo (no en combinación) en insomnio
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original una vez esta última esté definida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

