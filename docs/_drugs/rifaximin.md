---
layout: default
title: Rifaximin
parent: Solo Predicción del Modelo (L5)
nav_order: 224
evidence_level: L5
indication_count: 6
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
last_modified_at: 2026-11-24
description: "Rifaximin: nueva indicación predicha, Candidiasis oral (oral candidiasis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Rifaximin
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

## Rifaximina: antibacteriano oral no absorbible → Candidiasis oral (oral candidiasis)
{: .text-alpha }

## Resumen en Una Frase

Rifaximina es un antibiótico oral de acción local en el intestino, con escasa absorción sistémica.
El modelo TxGNN predice que podría ser efectivo para **Candidiasis oral (oral candidiasis)**, pero no hay ensayos clínicos registrados y solo existe **1 publicación** relacionada, un estudio de cohorte que sugiere un posible efecto desfavorable (selección de *Candida* resistente a micafungina), no un beneficio terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Candidiasis oral (oral candidiasis) |
| Puntaje de Predicción TxGNN | 0,9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rifaximin (traducción no oficial): «La rifaximina es un fármaco antibacteriano. […] La rifaximina es un derivado semisintético de la rifampicina y actúa uniéndose a la subunidad beta de la ARN polimerasa dependiente de ADN bacteriana, bloqueando uno de los pasos de la transcripción. Esto da lugar a la inhibición de la síntesis de proteínas bacterianas y, en consecuencia, inhibe el crecimiento de las bacterias.» Texto original en inglés: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), versión del 2025-08-27; consultado el 2026-11-19). Según la información conocida, la rifaximina es un antibacteriano no absorbible que actúa principalmente en el tracto gastrointestinal y no tiene actividad antifúngica conocida.

La única publicación vinculada sugiere lo contrario de un efecto terapéutico: el uso de rifaximina se asoció con infecciones por *Candida* resistentes a micafungina en receptores de trasplante alogénico de células madre hematopoyéticas, probablemente por alteración de la microbiota intestinal.

Por lo tanto, el puntaje alto (0,9975) no está respaldado por un mecanismo plausible y podría reflejar cercanía en la red con otros antiinfecciosos. Esta predicción debe interpretarse como una hipótesis computacional sin sustento mecanístico claro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohorte | Annals of Hematology | En receptores de trasplante alogénico de células madre hematopoyéticas, el uso de rifaximina como profilaxis se asoció con infecciones por *Candida* spp. resistentes a micafungina. |

---

## Información de Mercado en Argentina

Hay al menos 20 autorizaciones vigentes (la lista puede ser parcial), todas de productos de rifaximina como único principio activo. Los textos de indicación aprobada no están registrados en los datos locales.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 49637 | RIFADOM | 550 mg comp.x 60 | Domínguez | Vigente |
| 52884 | ROCIAMIN | 200 mg comp.rec.x 20 | Laboratorios Be | Vigente |
| 49524 | RIFADOM | 200 mg comp.x 20 | Domínguez | Vigente |
| 54990 | RIFAXTRIL | 550 mg comp.x 60 | Ariston | Vigente |
| 54989 | RIFAXTRIL | 550 mg comp.x 30 | Ariston | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 69 interacciones. Entre las listadas, una es de nivel mayor: la vacuna viva contra el cólera (*Vibrio cholerae* CVD 103-HgR). Las demás mostradas son de nivel moderado, por ejemplo ciclosporina, warfarina, tolvaptán, daclatasvir, ledipasvir, cabozantinib, apalutamida y alpelisib.
- **Señal de seguridad relacionada con la predicción**: la publicación vinculada sugiere que el uso de rifaximina puede favorecer infecciones por *Candida* resistentes a micafungina en pacientes trasplantados.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen un beneficio de la rifaximina en la candidiasis oral; la única publicación sugiere un posible perjuicio y no hay actividad antifúngica conocida. El puntaje del modelo no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un vínculo con la candidiasis oral
- Estudios preclínicos que evalúen un efecto sobre *Candida* en la mucosa oral
- Evaluación de la señal de riesgo de candidiasis resistente descrita en pacientes trasplantados
- Textos de advertencias y contraindicaciones del prospecto de ANMAT

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

