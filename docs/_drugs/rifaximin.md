---
layout: default
title: Rifaximin
parent: Solo Predicción del Modelo (L5)
nav_order: 224
evidence_level: L5
indication_count: 6
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
last_modified_at: 2026-10-30
description: "Rifaximin: nueva indicación predicha, Candidiasis oral (oral candidiasis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la rifaximina es un antibacteriano no absorbible que actúa principalmente en el tracto gastrointestinal y no tiene actividad antifúngica conocida.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49637 | RIFADOM | 550 mg comp. x 60 | No registrada |
| 52884 | ROCIAMIN | 200 mg comp. rec. x 20 | No registrada |
| 54990 | RIFAXTRIL | 550 mg comp. x 60 | No registrada |
| 54200 | LISIBACTER | 550 mg comp. rec. x 30 | No registrada |
| 40623 | COLOXIMINA | 200 mg comp. rec. x 20 | No registrada |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

