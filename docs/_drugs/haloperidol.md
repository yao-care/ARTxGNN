---
layout: default
title: Haloperidol
parent: Solo Predicción del Modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 9
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-20
description: "Haloperidol: nueva indicación predicha, Defecto congénito de la glicosilación con fucosilación defectuosa (congenital disorder of glycosylation with defective… (nivel de evidencia L5). Indicación ori…"
---

# Haloperidol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Haloperidol: antipsicótico antagonista de los receptores de dopamina D2 → defecto congénito de la glicosilación con fucosilación defectuosa (congenital disorder of glycosylation with defective fucosylation)
{: .text-alpha }

## Resumen en Una Frase

Haloperidol es un antipsicótico que se comercializa en Argentina con múltiples autorizaciones vigentes.
El modelo TxGNN predice que podría ser efectivo para el **defecto congénito de la glicosilación con fucosilación defectuosa (congenital disorder of glycosylation with defective fucosylation)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Defecto congénito de la glicosilación con fucosilación defectuosa (congenital disorder of glycosylation with defective fucosylation) |
| Puntaje de Predicción TxGNN | 0,9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Haloperidol (traducción no oficial): «El mecanismo de acción del decanoato de haloperidol en el tratamiento de la esquizofrenia en adultos no está claro. Sin embargo, su efecto en la esquizofrenia podría estar mediado por su actividad como antagonista de los receptores dopaminérgicos centrales de tipo 2.» Texto original en inglés: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), versión del 2026-11-03; consultado el 2026-11-19). Por conocimiento general, haloperidol es un antagonista de los receptores de dopamina D2 de la clase de los antipsicóticos típicos (butirofenonas).

No se identificó un vínculo mecanístico plausible entre el bloqueo dopaminérgico D2 y los defectos de fucosilación. El puntaje elevado (0,9991) refleja únicamente una predicción computacional, sin respaldo de estudios reales en los datos compilados.

Por lo tanto, esta predicción debe considerarse exploratoria. Antes de cualquier avance se necesitaría una hipótesis biológica que explique cómo un antagonista dopaminérgico podría modificar una alteración de la glicosilación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

La lista de autorizaciones puede ser parcial: se registran al menos 20 autorizaciones, todas vigentes y de producto de un solo principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 9662 | HALOPERIDOL MEDIPHARMA | 10 mg comp. x 30 | No registrada en los datos locales |
| 26686 | NEUPRAM | 1 mg comp. x 30 | No registrada en los datos locales |
| 32796 | ENABRAN | 10 mg comp. x 60 | No registrada en los datos locales |
| 3974 | HALOPIDOL | 1 mg comp. x 100 | No registrada en los datos locales |
| 27526 | HALOPERIDOL DENVER FARMA DECANOATO | 150 mg amp. x 3 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las de nivel mayor figuran bupropión, morfina, claritromicina y dolasetrón. Entre las de nivel moderado figuran famotidina, epinefrina, hidrocortisona, anfotericina B, atropina y loperamida, entre otras.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (0,9991), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico identificado. No hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que relacione el antagonismo D2 con la vía de fucosilación
- Estudios preclínicos que evalúen un posible efecto en modelos de este defecto de glicosilación
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) para una evaluación de seguridad

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

