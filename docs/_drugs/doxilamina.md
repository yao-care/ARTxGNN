---
layout: default
title: Doxilamina
parent: Solo Predicción del Modelo (L5)
nav_order: 148
evidence_level: L5
indication_count: 1
drugbank_id: DB00366
monitor_inn: "Doxylamine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-16
description: "Doxilamina: nueva indicación predicha, enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Doxilamina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Doxilamina: enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Doxilamina es un antihistamínico H1 de primera generación (etanolamina) con marcada actividad anticolinérgica, comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal (nasal cavity disease)**, pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9936 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg (combinación que contiene Doxilamina) (traducción no oficial): «Se desconoce el mecanismo de acción del succinato de doxilamina y el clorhidrato de piridoxina.» Texto original en inglés: "The mechanism of action of doxylamine succinate and pyridoxine hydrochloride is unknown." ([DailyMed: Doxylamine Succinate And Pyridoxine Hydrochloride (doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de265fd1-bc22-4da1-aab5-b5fedd649c8b), versión del 2026-08-24; consultado el 2026-11-19). Según lo conocido de su clase, es un antihistamínico H1 de primera generación (etanolamina) con actividad anticolinérgica marcada.

Mecanísticamente, el bloqueo de los receptores H1 en la mucosa nasal podría reducir la rinorrea, los estornudos, el prurito y la congestión mediados por histamina, como ocurre en la rinitis alérgica. Su efecto anticolinérgico podría además disminuir las secreciones nasales, por ejemplo en la rinorrea asociada al resfriado común.

Esta justificación se infiere solo de las propiedades de la clase del fármaco. El puntaje alto es una predicción computacional sin respaldo de estudios en los datos disponibles, y probablemente refleja la asociación conocida entre antihistamínicos y enfermedad alérgica de vías aéreas superiores, por lo que podría representar un uso ya existente más que una señal novedosa de reposicionamiento. La sedación, los efectos adversos anticolinérgicos y la disponibilidad de antihistamínicos de segunda generación no sedantes y corticoides intranasales limitan su atractivo para este uso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51937 | TONVAL | 10/10 mg cáps. x 30 | No registrada en los datos locales |
| 39716 | EPIDAC | Cáps. x 24 | No registrada en los datos locales |
| 54367 | DETIXOL | Cáps. x 30 | No registrada en los datos locales |
| 52593 | TUERIS | Cáps. x 24 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que estudien directamente la enfermedad de la cavidad nasal. Además, existen alternativas establecidas con mejor perfil de tolerabilidad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura y ensayos específicos sobre doxilamina en enfermedades nasales
- Comparación frente a antihistamínicos de segunda generación y corticoides intranasales
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Doxylamine Succinate And Pyridoxine Hydrochloride (doxylamine succinate and pyridoxine hydrochloride, delayed release tablets 10 mg/10 mg) prescribing information, Par Health USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de265fd1-bc22-4da1-aab5-b5fedd649c8b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

