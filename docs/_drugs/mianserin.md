---
layout: default
title: Mianserin
parent: Solo Predicción del Modelo (L5)
nav_order: 188
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Mianserin: nueva indicación predicha, Tortícolis paroxística benigna de la infancia (nivel de evidencia L5). Indicación original: Depresión unipolar (según el grafo de conocimiento"
monitor_inn: "mianserin"
predicted_indications: ["benign paroxysmal torticollis of infancy", "dysthymic disorder", "agoraphobia", "Ohdo syndrome and variants", "melancholia", "neurotic disorder"]
---

# Mianserin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Mianserina: De Depresión Unipolar a Trastorno Paroxístico Tortícolis Benigno de la Infancia

## Resumen en Una Frase

Mianserina (comercializada en Argentina como LERIVON) se utiliza originalmente para el tratamiento de la depresión unipolar, la depresión endógena, el trastorno depresivo mayor y el trastorno de ansiedad.
El modelo TxGNN predice que podría ser efectivo para la **tortícolis paroxística benigna de la infancia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Depresión unipolar (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99.49% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la mianserina es un antidepresivo tetracíclico; los datos farmacológicos compilados muestran que interactúa con múltiples receptores serotoninérgicos (5-HT1B, 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6, 5-HT7), receptores adrenérgicos alfa-1 (1A, 1B, 1D), el receptor LPA1 y el transportador de noradrenalina (NET).

La tortícolis paroxística benigna de la infancia es una condición pediátrica probablemente relacionada con la migraña y con una posible base de canalopatía. Con los datos disponibles no se identifica un vínculo mecanístico plausible entre la acción de la mianserina y esta enfermedad. El puntaje alto del modelo probablemente refleja asociaciones en el grafo de conocimiento más que plausibilidad biológica.

Cabe destacar que esta no es la predicción mejor respaldada. Otras predicciones del modelo tienen más sustento, aunque en su mayoría son superposiciones con la indicación ya aprobada:

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|
| Trastorno distímico | 99.45% | L4 | Un metaanálisis de antidepresivos como clase (PMID 21527126), sin aislar mianserina |
| Agorafobia | 99.40% | L4 | Un solo artículo, sobre inhibidores de MAO-A, solo tangencialmente relevante |
| Melancolía | 99.17% | L5 | Probablemente un reetiquetado de la depresión endógena; sin literatura |
| Depresión neurótica | 99.16% | L4 | 20 publicaciones, mayormente generales; superposición con la indicación aprobada |
| Trastorno neurótico | 99.02% | L3 | 4 publicaciones, incluidos estudios comparativos de mianserina |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la tortícolis paroxística benigna de la infancia.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 10308 | LERIVON (MSD Argentina) | Comprimidos 60 mg x 30 | No especificada en los datos |
| 6189 | LERIVON (Organon Arg.) | Comprimidos 30 mg x 30 | No especificada en los datos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas / Perfil farmacológico**: la consulta se completó con 11 registros, que corresponden a interacciones con blancos farmacológicos y no a interacciones con otros fármacos. Incluyen receptores serotoninérgicos (5-HT1B, 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6, 5-HT7), receptores adrenérgicos alfa-1 (1A, 1B, 1D), el receptor LPA1 y el transportador de noradrenalina (NET). No se dispone de niveles de gravedad.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay un mecanismo plausible que vincule la mianserina con esta condición pediátrica. Además, aún no se han revisado las advertencias y contraindicaciones del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Obtener datos detallados del mecanismo de acción de la mianserina.
- Evaluar un posible vínculo mecanístico con la fisiopatología de la tortícolis paroxística benigna (migraña/canalopatía) antes de invertir más recursos.
- Considerar priorizar candidatas con mayor respaldo, como el trastorno neurótico (L3) o el trastorno distímico (L4), teniendo en cuenta que muchas son cercanas a las indicaciones ya aprobadas.
- Considerar que la población es pediátrica, lo que exige una evaluación de seguridad específica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

