---
layout: default
title: Tramadol
parent: Solo Predicción del Modelo (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tramadol: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Osteoartritis / artropatía (según el grafo de conocimiento"
monitor_inn: "TRAMADOL"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Tramadol: De Osteoartritis a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Tramadol es un analgésico opioide con acción dual (opioide/inhibidor de la recaptación de serotonina y noradrenalina), originalmente asociado a osteoartritis y artropatía.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoartritis / artropatía (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tramadol es un analgésico de acción central con componente opioide y monoaminérgico, útil para el control sintomático del dolor, incluido el dolor osteoarticular.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética rara causada por mutaciones en CDMP1/GDF5. Tramadol no actúa sobre esa vía, por lo que no existe un vínculo mecanístico plausible de modificación de la enfermedad. A lo sumo, podría aliviar el dolor asociado.

El alto puntaje del modelo probablemente refleja la cercanía en la red de conocimiento entre enfermedades esqueléticas y articulares y las indicaciones originales (osteoartritis, artropatía), y no un mecanismo farmacológico demostrado. Lo mismo se observa en otras predicciones de la lista (braquiolmia, pseudoacondroplasia, miosclerosis, artritis idiopática juvenil, entre otras), todas con nivel de evidencia L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Argentina

Se listan 5 de las 20 autorizaciones vigentes (todas de producto único, sin combinaciones ni canceladas):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57554 | ULTRAGESIC CB (Adium) | 50 mg cáps. blanda x 30 | No informada |
| 23408 | TRAMAL (Vannier-Grunent) | 100 mg/ml gotas x 10 ml | No informada |
| 45866 | TRAMAL (Vannier-Grunent) | 50 mg cápsulas x 20 | No informada |
| 52661 | TRAMADOLTEN (Pfizer) | 50 mg comprimidos x 20 | No informada |
| 58307 | LIXIDOL GOTAS (Casasco) | 50 mg gotas x 10 ml | No informada |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia hepática, cirrosis y enfermedad hepática, epilepsia, trastornos de ansiedad, cetoacidosis diabética, diabetes mellitus, abuso/dependencia de sustancias, síndrome de abstinencia (incluida abstinencia alcohólica), insuficiencia respiratoria, intoxicación por paracetamol, síndrome serotoninérgico, hipertensión intracraneal/pseudotumor cerebral, síndrome de Wernicke-Korsakoff, infecciones del sistema nervioso central, hiperlipidemia y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de nivel **mayor**: alvimopán, bupropión, cisaprida, dexfenfluramina, dietilpropión, dolasetrón, dronabinol, efedrina y fenfluramina. De nivel **moderado**: atropina, bisacodilo, cimetidina, claritromicina, famotidina, eliglustat y eluxadolina, entre otros.
- Las interacciones con fármacos serotoninérgicos (p. ej., bupropión, fenfluramina) son relevantes por el riesgo de síndrome serotoninérgico y convulsiones.
- Se debe consultar el prospecto para advertencias y contraindicaciones oficiales, ya que no se dispone de ellas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un mecanismo plausible de modificación de la enfermedad en una displasia esquelética genética. El perfil de seguridad de tramadol, con múltiples contraindicaciones e interacciones relevantes, tampoco favorece avanzar sin respaldo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco, para evaluar un posible vínculo mecanístico.
- Texto de advertencias y contraindicaciones del prospecto de ANMAT, así como los textos de indicación aprobada, hoy vacíos.
- Estudios preclínicos o clínicos que muestren algún beneficio (incluso solo sintomático) en esta enfermedad.
- Valorar otras predicciones de la lista con mayor plausibilidad clínica (p. ej., dolor en pseudoacondroplasia o artritis), aunque también carecen de evidencia directa.
- Evaluación específica de riesgos si se considerara su uso en población pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

