---
layout: default
title: Clenbuterol
parent: Solo Predicción del Modelo (L5)
nav_order: 109
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Clenbuterol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "CLENBUTEROL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Clenbuterol
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

## Clenbuterol: De Indicación Original No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Clenbuterol es un agonista selectivo de los receptores beta-2 adrenérgicos, comercializado en Argentina con 5 autorizaciones vigentes, aunque los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9919 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 5) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, clenbuterol es un agonista selectivo de los receptores beta-2 adrenérgicos. En Argentina se comercializa en productos como BRONQ C y OXIBRON, en jarabe, comprimidos y gotas, lo que sugiere un uso respiratorio (broncodilatador). Este uso no está confirmado por los textos de indicación y debe verificarse en el prospecto.

La señalización adrenérgica modula el tono vascular cerebral, y los betabloqueantes (por ejemplo, propranolol) son un tratamiento profiláctico establecido de la migraña. Esto indica que la vía adrenérgica es biológicamente relevante para la migraña.

Sin embargo, un agonista beta-2 se esperaría que actúe en dirección opuesta a un betabloqueante (vasodilatación, efectos simpaticomiméticos), por lo que la dirección del efecto es incierta y podría ser desfavorable. El puntaje elevado de TxGNN (0.9919) es solo una predicción computacional.

La segunda predicción, **migraña con aura del tronco encefálico** (puntaje 0.9904), es un subtipo de la migraña. Su puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, por lo que no constituye evidencia independiente. Al ser un subtipo raro, es improbable que se estudie específicamente sin evidencia previa en la población general con migraña.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 5487 | BRONQ C | Jarabe x 100 ml | No disponible |
| 18230 | BRONQ C | Comprimidos x 30 | No disponible |
| 10116 | OXIBRON | Comprimidos x 20 | No disponible |
| 3239 | OXIBRON N.F. | Gotas x 30 ml | No disponible |
| 3238 | OXIBRON N.F. | Comprimidos x 30 | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura de respaldo. Además, el mecanismo agonista beta-2 podría actuar en dirección contraria a la de los betabloqueantes usados en migraña, y no se dispone de datos de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada), requisito bloqueante para cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión sistemática de literatura preclínica y clínica sobre agonistas beta-2 y migraña, para aclarar la dirección del efecto
- Evaluar la compatibilidad de las vías de administración y la similitud con la indicación original una vez conocida
- Reevaluar la decisión solo si aparece evidencia independiente que respalde la dirección del efecto
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

