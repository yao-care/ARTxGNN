---
layout: default
title: Buprenorfina
parent: Solo Predicción del Modelo (L5)
nav_order: 68
evidence_level: L5
indication_count: 6
drugbank_id: DB00921
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
last_modified_at: 2026-11-16
description: "Buprenorfina: nueva indicación predicha, porfiria aguda intermitente (acute intermittent porphyria) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Buprenorfina
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

## Buprenorfina: porfiria aguda intermitente (acute intermittent porphyria)
{: .text-alpha }

## Resumen en Una Frase

Buprenorfina es un opioide analgésico que se comercializa en Argentina en forma de parches.
El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente (acute intermittent porphyria)**,
pero solo existe **1 publicación** (un reporte de caso de manejo anestésico de 1993) y **ningún ensayo clínico**, por lo que la predicción carece de respaldo clínico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | porfiria aguda intermitente (acute intermittent porphyria) |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Buprenorfina (traducción no oficial): «SUBLOCADE inyectable contiene buprenorfina. La buprenorfina es un agonista parcial del receptor opioide mu y un antagonista del receptor opioide kappa.» Texto original en inglés: "SUBLOCADE Injection contains buprenorphine. Buprenorphine is a partial agonist at the mu- opioid receptor and an antagonist at the kappa-opioid receptor." ([DailyMed: Sublocade (buprenorphine) prescribing information, Indivior Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6189fb21-9432-45f8-8481-0bfaf3ccde95), versión del 2026-07-27; consultado el 2026-11-19). Según la información conocida, la buprenorfina es un agonista parcial del receptor opioide mu, utilizado como analgésico, y no actúa sobre el defecto de biosíntesis del hemo que causa la porfiria aguda intermitente.

No se identifica un vínculo mecanístico claro. La única publicación disponible describe el manejo anestésico de una paciente con esta enfermedad, un contexto de seguridad perioperatoria (riesgo porfirinogénico) y no de beneficio terapéutico. El puntaje alto del modelo (0,9941) no está respaldado por evidencia clínica.

En el mejor de los casos, su uso en esta enfermedad se limitaría a la analgesia, y aun así habría que verificar primero su seguridad en porfiria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Reporte de caso | Masui (Revista japonesa de anestesiología) | Manejo anestésico de una paciente de 40 años con sospecha de porfiria aguda intermitente sometida a cirugía ginecológica oncológica. No evalúa eficacia terapéutica de buprenorfina. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61001 | BUPRIVA | Parche 10 mg x 1 | No registrada |
| 60425 | BIVALIS | Parche 20 mg x 4 | No registrada |
| 61000 | BUPRIVA | Parche 5 mg x 1 | No registrada |
| 61002 | BUPRIVA | Parche 20 mg x 1 | No registrada |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única publicación es un reporte de caso sobre manejo anestésico, sin estudios que evalúen la buprenorfina como tratamiento de la porfiria aguda intermitente, y no hay ensayos clínicos. El nivel de evidencia es L5: solo predicción del modelo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la buprenorfina y su posible vínculo con la fisiopatología de la porfiria
- Revisión del prospecto aprobado en ANMAT (advertencias y contraindicaciones), incluida la seguridad en porfiria
- Revisión de literatura sobre seguridad porfirinogénica de la buprenorfina
- Estudios preclínicos o clínicos que evalúen directamente esta indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sublocade (buprenorphine) prescribing information, Indivior Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6189fb21-9432-45f8-8481-0bfaf3ccde95) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

