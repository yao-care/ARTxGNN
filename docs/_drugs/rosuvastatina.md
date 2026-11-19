---
layout: default
title: Rosuvastatina
parent: Solo Predicción del Modelo (L5)
nav_order: 321
evidence_level: L5
indication_count: 6
drugbank_id: DB01098
monitor_inn: "Rosuvastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
last_modified_at: 2026-11-20
description: "Rosuvastatina: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5)."
---

# Rosuvastatina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Rosuvastatina: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Rosuvastatina es una estatina, es decir, un inhibidor de la enzima HMG-CoA reductasa que reduce el colesterol LDL.
El modelo TxGNN predice que podría ser útil para la **deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)**.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rosuvastatina (traducción no oficial): «CRESTOR es un inhibidor de la HMG‑CoA reductasa, la enzima limitante de la velocidad que convierte la 3‑hidroxi‑3‑metilglutaril coenzima A en mevalonato, un precursor del colesterol.» Texto original en inglés: "CRESTOR is an inhibitor of HMG‑CoA reductase, the rate-limiting enzyme that converts 3‑hydroxy‑3‑methylglutaryl coenzyme A to mevalonate, a precursor of cholesterol." ([DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee), versión del 2026-09-23; consultado el 2026-11-19). Según la información conocida, la rosuvastatina inhibe la HMG-CoA reductasa, la enzima limitante de la síntesis de colesterol. Con ello reduce el colesterol LDL y, en menor medida, eleva modestamente el colesterol HDL.

El puntaje de 0,9954 parece reflejar la cercanía de ambos elementos dentro de la red del metabolismo lipídico. La deficiencia de CETP se caracteriza por un colesterol HDL marcadamente elevado. En los datos compilados no se identifica una necesidad clínica ni un fundamento terapéutico para reducir el LDL en esta condición.

Por lo tanto, el vínculo entre el fármaco y esta enfermedad es solo una asociación calculada por el modelo. No hay estudios que la respalden, y debe tratarse como una hipótesis sin validar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El fármaco figura como comercializado en Argentina, con al menos 20 autorizaciones vigentes de productos de un solo principio activo. La lista puede ser parcial. Algunos ejemplos:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 33101 | CRESTOR | 20 mg comp. x 28 | AstraZeneca |
| 45251 | SINLIP | 20 mg comp. rec. x 60 | Gador |
| 50618 | PARASUL | 5 mg comp. x 28 | Sidus |
| 46502 | ARTOMEY | 20 mg comp. x 30 | Teva Argentina |
| 49967 | ROSULIP | 20 mg comp. x 30 | Eurofarma |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni publicaciones, por lo que el nivel de evidencia es L5. Además, no se aprecia una razón terapéutica para reducir el LDL en una condición caracterizada por HDL elevado.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Un fundamento clínico o biológico que justifique el uso de una estatina en esta condición.
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad.
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones).

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

