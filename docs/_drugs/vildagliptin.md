---
layout: default
title: Vildagliptin
parent: Solo Predicción del Modelo (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vildagliptin: nueva indicación predicha, Síndrome de la persona rígida clásico (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2"
monitor_inn: "VILDAGLIPTIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Vildagliptin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Vildagliptina: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

La vildagliptina es un inhibidor de la dipeptidil peptidasa-4 (DPP-4) que se utiliza originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la persona rígida clásico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: es una señal puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según el grafo de conocimiento; los registros de ANMAT no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción del mecanismo de acción. Se sabe que la vildagliptina inhibe la DPP-4, lo que preserva las hormonas incretinas (GLP-1 y GIP), mejora la respuesta de las células beta a la glucosa y reduce la secreción inapropiada de glucagón. Los datos farmacológicos disponibles confirman como dianas la DPP-4, la DPP-8 y la DPP-9, además de TRPV4.

Entre el síndrome de la persona rígida y la diabetes existe una relación indirecta. El síndrome es una enfermedad de origen autoinmune, asociada a anticuerpos anti-GAD65, y suele coexistir con diabetes tipo 1. Una hipótesis posible, pero **no verificada**, es que los efectos inmunomoduladores de la inhibición de DPP-4 pudieran ser relevantes. No existe respaldo mecanístico directo.

Es probable que el puntaje alto refleje la cercanía en el grafo de conocimiento entre ambas enfermedades. La variante "síndrome de la extremidad rígida focal" obtiene exactamente el mismo puntaje, lo que sugiere que ambas comparten el mismo vecindario en el grafo y no que haya apoyo independiente para cada una.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

La vildagliptina cuenta con 20 autorizaciones vigentes, todas de producto único y ninguna cancelada. A continuación se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 42278 | GALVUS | 50 mg, comprimidos x 56 | Celnova Argenti |
| 43318 | GALVUS | 50 mg, comprimidos x 28 | Celnova Argenti |
| 57293 | ZATIUM | 50 mg, comprimidos x 60 | Elea |
| 58633 | JOVIUS | 50 mg, comprimidos x 30 | Teva Argentina |
| 42498 | GALVUS MET | 50/1000 mg, comprimidos x 60 | Celnova Argenti |

El resto de las autorizaciones corresponde a otras marcas (Carflax, Zomarist, Glucemix, Vilzer) y a combinaciones con metformina (Zomarist Met, Jovius Met, Zatium Met).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de la persona rígida se basa solo en el modelo, sin ensayos clínicos, literatura ni mecanismo plausible demostrado (nivel L5). Aunque la vildagliptina ya está comercializada en Argentina para diabetes, eso no aporta evidencia para esta nueva indicación.

**Para avanzar se necesita:**
- Una revisión sistemática de la literatura sobre inhibidores de DPP-4 en enfermedades neuroinmunes y en síndrome de la persona rígida.
- Datos detallados del mecanismo de acción y un análisis de plausibilidad biológica con la autoinmunidad anti-GAD65.
- Los textos de indicación y las advertencias y contraindicaciones del prospecto de ANMAT.
- Priorizar otras indicaciones predichas con evidencia real. Por ejemplo, para la **diabetes mellitus tipo 1** hay un ensayo de Fase 2 completado (NCT02803892, rapamicina más vildagliptina) y un ensayo de Fase 3 de estado desconocido (NCT01559025). También hay un ECA publicado (PMID 33124663) y estudios mecanísticos. Esa línea alcanza un nivel L2 y es más prometedora como pregunta de investigación, aunque sigue siendo un uso fuera de indicación con riesgos a considerar, como cetoacidosis y la señal de pancreatitis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

