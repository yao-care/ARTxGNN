---
layout: default
title: Loperamida
parent: Solo Predicción del Modelo (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
drugbank_id: DB00836
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
last_modified_at: 2026-11-24
description: "Loperamida: nueva indicación predicha, conjuntivitis contagiosa aguda (acute contagious conjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Loperamida
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

## Loperamida: conjuntivitis contagiosa aguda (acute contagious conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Loperamida es un agonista opioide periférico que actúa sobre los receptores mu del intestino para reducir la motilidad intestinal.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda (acute contagious conjunctivitis)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | conjuntivitis contagiosa aguda (acute contagious conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Loperamida (traducción no oficial): «Los estudios in vitro y en animales muestran que las cápsulas de clorhidrato de loperamida actúan al enlentecer la motilidad intestinal y al afectar el movimiento de agua y electrolitos a través del intestino. La loperamida se une al receptor de opiáceos en la pared intestinal.» Texto original en inglés: "In vitro and animal studies show that loperamide hydrochloride capsules act by slowing intestinal motility and by affecting water and electrolyte movement through the bowel. Loperamide binds to the opiate receptor in the gut wall." ([DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b), versión del 2026-07-09; consultado el 2026-11-19). Por conocimiento farmacológico general, la loperamida es un agonista opioide mu de acción periférica sobre las neuronas del plexo mientérico intestinal, que reduce la motilidad y el tránsito.

Con base en el análisis disponible, **no existe un vínculo mecanístico plausible** entre este mecanismo y la conjuntivitis contagiosa aguda. La loperamida no tiene actividad antimicrobiana, antiinflamatoria ni ocular conocida. El puntaje alto (0,9997) es una salida del modelo sin respaldo clínico ni bibliográfico, y probablemente refleja artefactos de la red de relaciones y no una razón biológica.

Por ello, la predicción debe considerarse una hipótesis sin sustento, y no una oportunidad real de reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Los datos locales muestran que el fármaco está comercializado, con al menos 20 autorizaciones vigentes de productos de un solo principio activo (la lista puede ser parcial). Principales autorizaciones:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 20312 | IONET | comp.x 10 | Cetus | Vigente |
| 20401 | LOPERAMIDA FABRA | comp.x 10 | Fabra | Vigente |
| 20141 | LANSEKA | 2 mg comp.x 10 | Lafedar | Vigente |
| 47217 | LOVOPREN | 2 mg comp.x 10 | Eczane | Vigente |
| 20842 | REGULANE SOLUCION | sol.x 60 ml | Finadiet | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal de seguridad general, la literatura compilada para otras predicciones del mismo fármaco describe casos de colitis fulminante y depresión respiratoria asociados al uso de loperamida en contextos de inflamación intestinal grave. No guardan relación directa con la conjuntivitis, pero indican cautela en poblaciones vulnerables.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos, literatura ni mecanismo plausible (nivel L5). El puntaje alto del modelo no basta para justificar avanzar.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que estudie directamente la conjuntivitis contagiosa aguda
- Una hipótesis mecanística justificada, incluida la compatibilidad de vía de administración (el fármaco se comercializa en formas orales)
- Datos de mecanismo de acción y de advertencias y contraindicaciones del prospecto local

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

