---
layout: default
title: Simvastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 5
monitor_inn: "SIMVASTATIN"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Simvastatin: nueva indicación predicha, Infarto del tronco encefálico (brain stem infarction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Simvastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Simvastatina: inhibidor de la HMG-CoA reductasa → infarto del tronco encefálico (brain stem infarction)
{: .text-alpha }

## Resumen en Una Frase

Simvastatina es una estatina utilizada para reducir los lípidos en sangre. El modelo TxGNN predice que podría ser útil para el **infarto del tronco encefálico (brain stem infarction)**, pero actualmente **no hay ensayos clínicos** ni publicaciones que estudien directamente esta enfermedad con simvastatina, por lo que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infarto del tronco encefálico (brain stem infarction) |
| Puntaje de Predicción TxGNN | 0,9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Simvastatin (traducción no oficial): «La simvastatina es un profármaco que, tras su administración, se hidroliza a su forma activa de β-hidroxiácido, el ácido de simvastatina. El ácido de simvastatina y sus metabolitos son inhibidores de la HMG-CoA reductasa, la enzima limitante de la velocidad que convierte la HMG-CoA en mevalonato, un precursor del colesterol.» Texto original en inglés: "Simvastatin is a prodrug and is hydrolyzed to its active β-hydroxyacid form, simvastatin acid, after administration. Simvastatin acid and its metabolites are inhibitors of HMG-CoA reductase, the rate-limiting enzyme that converts HMG-CoA to mevalonate, a precursor of cholesterol." ([DailyMed: Zocor (simvastatin) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f55d5de-5a4f-4a39-8c84-c53976dd6af9), versión del 2025-03-28; consultado el 2026-11-19). Por conocimiento general, simvastatina pertenece a la clase de las estatinas, que inhiben la HMG-CoA reductasa y reducen el colesterol LDL.

Las estatinas tienen además efectos llamados pleiotrópicos: mejoran la función del endotelio, reducen la inflamación, estabilizan las placas de ateroma y podrían ejercer neuroprotección. Estos efectos ofrecen un vínculo biológicamente coherente con la enfermedad cerebrovascular isquémica, de la cual el infarto del tronco encefálico es una localización anatómica.

Sin embargo, el puntaje alto del modelo probablemente refleja la cercanía con otras enfermedades cerebrovasculares ya vinculadas al fármaco, y no evidencia nueva. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27465579](https://pubmed.ncbi.nlm.nih.gov/27465579/) | 2016 | Preclínico | Journal of Translational Medicine | Estudio en ratas con isquemia cerebral focal: ferulato de sodio y n-butilidenoftalida combinados con células estromales de médula ósea mejoraron la angiogénesis y la neurogénesis. No evalúa simvastatina, por lo que no aporta respaldo directo. |

## Información de Mercado en Argentina

Se listan hasta 5 de las autorizaciones registradas. La lista de autorizaciones es parcial: hay al menos 20 autorizaciones y pueden existir más. Todas las listadas están vigentes. Los datos locales no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40944 | COLEFLUX | 80 mg comprimidos recubiertos x 30 | No registrada |
| 14602 | REDUSTEROL | 20 mg comprimidos x 30 | No registrada |
| 20850 | LISAC | 10 mg comprimidos recubiertos x 30 | No registrada |
| 33230 | TANAVAT | 20 mg comprimidos x 30 | No registrada |
| 18182 | ZOCOR | 20 mg comprimidos x 30 | No registrada |

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (se registraron 100 interacciones; se destacan las de nivel mayor): amiodarona, amlodipino y fenofibrato. También constan interacciones moderadas, por ejemplo con zidovudina, paclitaxel, nifedipino, omeprazol y etanol.
- **Riesgo de miopatía con antirretrovirales**: la literatura revisada para otra predicción señala que los inhibidores de proteasa y el cobicistat elevan la exposición a simvastatina e incrementan el riesgo de miopatía y rabdomiólisis. Es relevante si el paciente recibe estos fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ningún estudio que evalúe directamente el infarto del tronco encefálico con simvastatina; el único artículo recuperado no estudia este fármaco. El nivel de evidencia es L5, solo predicción del modelo.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre estatinas en el ictus isquémico de territorio vertebrobasilar o del tronco encefálico.
- Datos del mecanismo de acción y del prospecto aprobado (advertencias y contraindicaciones).
- Si se justifica, un estudio observacional o ensayo clínico específico en esta población.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zocor (simvastatin) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f55d5de-5a4f-4a39-8c84-c53976dd6af9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

