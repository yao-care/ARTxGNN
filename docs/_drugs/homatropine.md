---
layout: default
title: Homatropine
parent: Solo Predicción del Modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Homatropine: nueva indicación predicha, Síndrome de la cola de caballo (nivel de evidencia L5). Indicación original: Enfermedad ulcerosa péptica (según el grafo de conocimiento"
---

# Homatropine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Homatropina: De Úlcera Péptica a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Homatropina es un fármaco antimuscarínico (anticolinérgico) utilizado originalmente en trastornos gastrointestinales como la úlcera péptica y el síndrome de intestino irritable, así como en patologías oftálmicas como la uveítis y la cicloplejía.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad ulcerosa péptica (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la homatropina es un antagonista muscarínico con perfil antiespasmódico y antisecretor. Su eficacia en indicaciones digestivas y oculares se basa en el bloqueo de los receptores muscarínicos.

El síndrome de la cola de caballo puede causar disfunción vesical neurogénica. En teoría, la actividad anticolinérgica sobre los receptores muscarínicos del detrusor podría aliviar algunos síntomas urinarios. Sin embargo, el fármaco no trataría la causa de fondo (la compresión nerviosa), que requiere descompresión quirúrgica urgente. El vínculo es indirecto: se infiere a partir de la vía de los síntomas vesicales, no de la enfermedad en sí.

Otras predicciones del modelo apuntan en la misma línea mecanística:

| Posición | Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Vejiga neurogénica (término obsoleto) | 99.75% | Los antimuscarínicos son una clase establecida para esta condición, pero existen alternativas aprobadas (oxibutinina, tolterodina, solifenacina). El término debería actualizarse a la ontología vigente. |
| 3 | Gastroduodenitis | 99.51% | Muy cercana a una indicación ya existente (úlcera péptica); aporta poca novedad. |
| 4 | Vejiga hiperactiva | 99.16% | Mecanísticamente coherente, pero existen antimuscarínicos más selectivos y mejor caracterizados. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6736 | SUMAL | Comprimidos x 20 | No disponible en los datos compilados |
| 49685 | FACTOR AG ANTIESPASMODICO | Gotas x 30 ml | No disponible en los datos compilados |
| 18623 | SUMAL | Comprimidos x 10 | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 17 interacciones.
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas**: otros anticolinérgicos (diciclomina, glicopirronio, hiosciamina, mepenzolato, metescopolamina, propantelina, ipratropio), opioides (opio, hidrocodona), inhibidores de la colinesterasa (edrofonio, fisostigmina), y ciclizina, fenindamina, fenilefrina y tietilperazina.
- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia hepática, epilepsia, úlcera gástrica, trastornos de ansiedad, porfiria, enfermedad renal, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo, enfermedad inflamatoria intestinal, hiperplasia prostática benigna, neutropenia, agranulocitosis, hipotensión, encefalopatía hepática, abuso de sustancias, enfermedad coronaria y apnea del sueño.

Dado que no se dispone del texto del prospecto, es necesario consultarlo para confirmar las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero es únicamente computacional (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo no abordaría la causa del síndrome de la cola de caballo, y las indicaciones vesicales cuentan con alternativas aprobadas y más selectivas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Realizar una búsqueda sistemática de literatura y ensayos sobre homatropina en síntomas vesicales neurogénicos.
- Evaluar si conviene priorizar la vejiga neurogénica o la vejiga hiperactiva (con el término de enfermedad actualizado) frente al síndrome de la cola de caballo.
- Valorar el perfil de seguridad anticolinérgico, en especial en adultos mayores, y las 17 interacciones registradas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

