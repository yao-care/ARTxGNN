---
layout: default
title: Fenoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 142
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Fenoterol: nueva indicación predicha, Atrofia multisistémica (nivel de evidencia L5). Indicación original: No consta en los datos compilados (las autorizaciones de ANMAT no inc…"
monitor_inn: "FENOTEROL"
predicted_indications: ["multiple system atrophy", "postural orthostatic tachycardia syndrome", "variably protease-sensitive prionopathy", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "sinoatrial block", "sinoatrial node disease"]
---

# Fenoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Fenoterol: De Broncodilatador a Atrofia Multisistémica

## Resumen en Una Frase

Fenoterol es un agonista selectivo de los receptores beta-2 adrenérgicos, conocido como broncodilatador y también mencionado para frenar el trabajo de parto prematuro, y comercializado en Argentina como Berotec y Berodual.
El modelo TxGNN predice que podría ser efectivo para **atrofia multisistémica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos compilados (las autorizaciones de ANMAT no incluyen texto de indicación aprobada) |
| Nueva Indicación Predicha | Atrofia multisistémica |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, fenoterol es un agonista de receptores beta-adrenérgicos (con actividad sobre ADRB1, ADRB2 y ADRB3, siendo su efecto principal sobre beta-2), utilizado como broncodilatador y para suprimir el trabajo de parto prematuro.

La relación con la atrofia multisistémica (AMS) es **especulativa**. La AMS cursa con falla autonómica e hipotensión ortostática neurogénica. La vasodilatación mediada por beta-2 y la taquicardia podrían alterar la hemodinamia, pero cabría esperar que la vasodilatación empeore la hipotensión ortostática. No se identifica un mecanismo modificador de la enfermedad.

El puntaje alto de TxGNN es solo una predicción computacional, sin ensayos ni literatura de respaldo.

### Otras indicaciones predichas (todas L5, sin ensayos ni literatura)

| Posición | Enfermedad | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|------|
| 2 | Síndrome de taquicardia postural ortostática | 99.61% | Cuestionable: la vasodilatación y la taquicardia refleja podrían agravar los síntomas |
| 3 | Prionopatía variablemente sensible a proteasa | 99.54% | Sin vínculo plausible; probable artefacto del grafo de conocimiento |
| 4 | Glaucoma de ángulo abierto | 99.43% | Indirecta pero plausible (modulación adrenérgica de la presión intraocular); la más plausible, con riesgo cardiovascular sistémico |
| 5 | Enfermedad de Raynaud | 99.41% | Plausible de forma indirecta (vasodilatación); ya existen alternativas establecidas (bloqueadores de canales de calcio) |
| 6 | Glaucoma hereditario primario | 99.37% | Menos relevante, por su origen frecuentemente del desarrollo |
| 7 | Bloqueo sinoauricular | 99.35% | Coherente con el efecto cronotrópico positivo, pero con riesgo proarrítmico y sin uso estándar |
| 8 | Enfermedad del nódulo sinusal | 99.25% | Teórica; preocupan las arritmias y la taquifilaxia |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1639 | BEROTEC | Solución 0.5% x 20 ml | No especificada en los datos |
| 44183 | BEROTEC HFA | Aerosol HFA x 10 ml | No especificada en los datos |
| 1407 | BERODUAL | Solución x 20 ml | No especificada en los datos |
| 44184 | BERODUAL HFA | Aerosol HFA x 10 ml | No especificada en los datos |

Todas las autorizaciones están vigentes y pertenecen a Boehringer Ingelheim.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de receptores**: los datos compilados muestran actividad sobre los receptores β1 (ADRB1), β2 (ADRB2) y β3 (ADRB3) adrenérgicos. No se registran interacciones con otros fármacos con nivel de gravedad definido.
- **Riesgos plausibles según el mecanismo** (no provienen del prospecto): taquicardia, hipotensión y riesgo proarrítmico por la exposición sistémica a agonistas beta, aspectos relevantes en las indicaciones cardiovasculares y autonómicas predichas.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para atrofia multisistémica se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo conocido (vasodilatación beta-2) podría empeorar la hipotensión ortostática característica de la enfermedad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas), requisito previo para el análisis de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión de literatura y ensayos preclínicos que respalden algún vínculo con atrofia multisistémica.
- Evaluar si otras candidatas (por ejemplo, glaucoma de ángulo abierto) tienen un fundamento más sólido antes de priorizar recursos.
- Analizar la compatibilidad de vía de administración (actualmente las formas disponibles son solución y aerosol inhalatorio/nebulizable).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

