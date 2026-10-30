---
layout: default
title: Econazole
parent: Solo Predicción del Modelo (L5)
nav_order: 132
evidence_level: L5
indication_count: 2
monitor_inn: "econazole"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-30
description: "Econazole: nueva indicación predicha, Infección ectótrix (nivel de evidencia L5). Indicación original: No hay texto de indicación aprobada en las autorizaciones locales. La…"
---

# Econazole
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

## Econazol: De Infecciones Dermatofíticas Cutáneas a Infección Ectótrix
{: .text-alpha }

## Resumen en Una Frase

Econazol es un antifúngico imidazólico, utilizado originalmente para infecciones cutáneas como tinea pedis, tinea corporis y candidiasis cutánea.
El modelo TxGNN predice que podría ser efectivo para **infección ectótrix (ectothrix infectious disease)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No hay texto de indicación aprobada en las autorizaciones locales. Las relaciones registradas en el grafo de conocimiento incluyen tinea pedis, tinea corporis, infección por tiña, candidiasis cutánea, pitiriasis versicolor y dermatofitosis de la ingle y la zona perianal |
| Nueva Indicación Predicha | Infección ectótrix |
| Puntaje de Predicción TxGNN | 0,9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, econazol pertenece a la clase de los antifúngicos imidazólicos, que en general se entiende que inhiben la lanosterol 14-alfa-desmetilasa y alteran la síntesis de ergosterol. Este mecanismo no está confirmado por los datos disponibles.

La infección ectótrix es una dermatofitosis del tallo piloso (por ejemplo, *Microsporum* y *Trichophyton*), en la que las artroconidias se forman en el exterior del pelo. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Sin embargo, es más una extensión dentro de la misma clase de fármacos y el mismo grupo de organismos que un reposicionamiento verdadero.

Hay una limitación práctica importante: cuando hay compromiso del tallo piloso y del folículo, los agentes tópicos penetran poco y suelen preferirse antifúngicos sistémicos. Esto reduce el valor práctico de econazol tópico para esta indicación.

*Predicción secundaria:* el modelo también predice **infección endótrix** (puntaje 0,9997, también L5, Hold), con el mismo razonamiento: el hongo vive dentro del tallo piloso y el econazol tópico llegaría mal a él.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 10790 | FILODERMA PLUS | Crema, 20 g | Texto de indicación no disponible en el registro |
| 14091 | GRISEOCREM NF | Pomada, 20 g | Texto de indicación no disponible en el registro |

Ambas autorizaciones son de un solo principio activo, están vigentes y corresponden al fabricante Teva Argentina.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 41 posibles interacciones, todas con nivel de gravedad no clasificado. Algunas de las principales: clotrimazol, fluconazol, metformina, omeprazol, rosiglitazona, lansoprazol, loperamida, glipizida, dexametasona, clopidogrel, heparina, fluticasona, acetaminofén, levotiroxina, aciclovir, diazepam, didanosina, citarabina y lorazepam.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación que estudie directamente la infección ectótrix con econazol, por lo que la evidencia es solo la predicción del modelo (L5). Además, la penetración tópica limitada en el tallo piloso debilita el caso clínico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), que es un vacío de datos bloqueante para el tamizaje de seguridad.
- Confirmar el mecanismo de acción de econazol con DrugBank.
- Buscar estudios clínicos o in vitro sobre econazol en dermatofitosis del cuero cabelludo o del tallo piloso.
- Evaluar la compatibilidad de la vía de administración (tópica frente a sistémica) y la comparación con antifúngicos sistémicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

