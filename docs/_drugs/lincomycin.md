---
layout: default
title: Lincomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Lincomycin: nueva indicación predicha, Hiperamilasemia (nivel de evidencia L5). Indicación original: Infecciones neumocócicas…"
---

# Lincomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Lincomicina: De Infecciones Neumocócicas, Estafilocócicas y Estreptocócicas a Hiperamilasemia

## Resumen en Una Frase

La lincomicina es un antibiótico originalmente utilizado para el tratamiento de infecciones neumocócicas, estafilocócicas y estreptocócicas.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones neumocócicas, estafilocócicas y estreptocócicas (según el grafo de conocimiento; el texto de indicación aprobado en las autorizaciones locales está vacío) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.14% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. La lincomicina pertenece a la clase de los antibióticos lincosamidas, y su eficacia en infecciones bacterianas por cocos grampositivos es la base de su uso original. Sin embargo, no hay un vínculo mecanístico documentado que la conecte con la hiperamilasemia.

La hiperamilasemia es un hallazgo de laboratorio (elevación de amilasa en sangre) que suele ser secundario a enfermedad pancreática o de glándulas salivales, y no una infección bacteriana. No existe una vía plausible respaldada por los datos que relacione la acción antibacteriana de la lincomicina con esta condición.

El puntaje alto (0.991) refleja una predicción basada en el grafo de conocimiento, sin respaldo clínico ni bibliográfico. Debe interpretarse con cautela. Otras predicciones del modelo con el mismo puntaje (síndrome de hiperviscosidad policlonal y analbuminemia congénita) tampoco tienen un vínculo mecanístico sustentado.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6675 | FRADEMICINA | 500 mg cápsulas x 16 | No disponible en el texto de autorización |
| 2276 | FRADEMICINA | 300 mg ampollas x 4 x 1 ml | No disponible en el texto de autorización |

Ambas autorizaciones están vigentes, corresponden a monofármaco y su titular es Janssen-Cilag.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, colitis y enfermedades del aparato digestivo e intestinales.
- **Interacciones Farmacológicas** (21 registradas):
  - Moderadas: balsalazida, ácido picosulfúrico, attapulgita, caolín, eritromicina y etinilestradiol.
  - Nivel no determinado: clotrimazol, cimetidina, morfina, metformina, omeprazol, lactulosa, triamcinolona, simvastatina, ranitidina, warfarina, lidocaína, cetirizina, montelukast y salmeterol.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto aprobado.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible entre un antibiótico lincosamida y la hiperamilasemia. Además, existe una brecha de seguridad importante, pues no se dispone del texto de advertencias y contraindicaciones del prospecto de ANMAT.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y registros de ensayos sobre lincomicina e hiperamilasemia.
- Evaluar la relevancia clínica de la indicación predicha, dado que la hiperamilasemia es un hallazgo de laboratorio y no una enfermedad en sí misma.
- Valorar el riesgo de las contraindicaciones digestivas (colitis, *C. difficile*) y hepáticas señaladas en el grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

