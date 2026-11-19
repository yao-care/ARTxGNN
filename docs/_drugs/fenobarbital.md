---
layout: default
title: Fenobarbital
parent: Solo Predicción del Modelo (L5)
nav_order: 173
evidence_level: L5
indication_count: 3
drugbank_id: DB01174
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
last_modified_at: 2026-11-16
description: "Fenobarbital: nueva indicación predicha, neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 7 (en el listado vigente: 7)"
---

# Fenobarbital
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Fenobarbital: neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Fenobarbital es un fármaco anticonvulsivante de la clase de los barbitúricos, con 7 autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino (trigeminal nerve neoplasm)**, pero no hay ensayos clínicos y la única publicación vinculada (una serie de casos sobre síndrome de Sturge-Weber) no estudia esta enfermedad, por lo que la evidencia es mínima.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, el fenobarbital es un modulador alostérico positivo del receptor GABA-A que refuerza la inhibición neuronal y reduce la excitabilidad, lo que explica su uso para controlar convulsiones.

Ese mecanismo no tiene una conexión directa conocida con una actividad antitumoral sobre tumores del nervio trigémino. La única publicación asociada es una serie de 14 casos de síndrome de Sturge-Weber (1997), una enfermedad vascular neurocutánea en la que el fenobarbital se usa para controlar convulsiones. La relación con el tumor del trigémino probablemente sea un artefacto del modelo, vinculado a la distribución trigeminal de las lesiones faciales y al contexto del manejo de convulsiones, y no a evidencia de eficacia tumoral.

En el mejor de los casos, el fármaco podría servir como tratamiento sintomático de convulsiones asociadas a un tumor, lo que constituye una indicación distinta a la predicha. Por lo tanto, el puntaje alto del modelo no está respaldado por un mecanismo plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales españoles de pediatría | Revisión de 14 casos de síndrome de Sturge-Weber seguidos durante 25 años (características clínicas, evolución y respuesta terapéutica). No estudia neoplasias del nervio trigémino. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17477 | LUMINAL | comp. x 60 | No registrada en los datos locales |
| 12624 | ALEPSAL | comp. x 60 | No registrada en los datos locales |
| 48440 | FENROS | 15 mg comp. x 30 | No registrada en los datos locales |
| 48442 | FENROS | 100 mg comp. x 60 | No registrada en los datos locales |
| 48441 | FENROS | 100 mg comp. x 20 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto, pero no hay ensayos clínicos, la única publicación no aborda esta enfermedad y no existe un mecanismo plausible que vincule al fenobarbital con tumores del nervio trigémino. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (por ejemplo, desde DrugBank) y un análisis de si existe algún vínculo mecanístico real con la enfermedad predicha
- Estudios preclínicos o clínicos que evalúen directamente neoplasias del nervio trigémino
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Aclarar si el vínculo del modelo se debe a un artefacto (Sturge-Weber, control de convulsiones) antes de invertir en más estudios
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

