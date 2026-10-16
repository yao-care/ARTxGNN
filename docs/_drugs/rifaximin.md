---
layout: default
title: Rifaximin
parent: Evidencia Moderada (L3-L4)
nav_order: 224
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Rifaximin: nueva indicación predicha, Candidiasis oral (nivel de evidencia L4). Indicación original: Encefalopatía hepática, coma hepático (según el grafo de conocimiento"
---

# Rifaximin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Rifaximina: De Encefalopatía Hepática a Candidiasis Oral

## Resumen en Una Frase

Rifaximina es un antibiótico oral no absorbible, originalmente utilizado para el tratamiento de la encefalopatía hepática y el coma hepático.
El modelo TxGNN predice que podría ser efectivo para **candidiasis oral**, pero actualmente no hay ensayos clínicos y solo existe **1 publicación** (un estudio de cohorte) cuya señal apunta a un posible riesgo, no a un beneficio terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Encefalopatía hepática, coma hepático (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Candidiasis oral |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la rifaximina es un antibacteriano de acción local en el intestino, con absorción sistémica mínima. Su eficacia en la encefalopatía hepática se asocia a la reducción de bacterias intestinales productoras de toxinas.

Mecanísticamente, **la predicción no se sostiene bien**. La rifaximina no tiene actividad antifúngica conocida. El único estudio disponible (PMID 34180023) asocia su uso con infecciones por *Candida* resistentes a micafungina en receptores de trasplante alogénico de progenitores hematopoyéticos. Esto sugiere una posible asociación adversa (probablemente por alteración de la microbiota intestinal y presión de selección), no un beneficio.

Por lo tanto, el puntaje alto del modelo no tiene respaldo en un mecanismo terapéutico plausible, y la señal disponible apunta en sentido contrario. Se trata más de una alerta de seguridad que de una oportunidad de reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Estudio de cohorte | Annals of Hematology | El uso de rifaximina como profilaxis en receptores de trasplante alogénico de progenitores hematopoyéticos se asoció con infecciones por *Candida* resistentes a micafungina. No muestra beneficio terapéutico. |

## Información de Mercado en Argentina

Los textos de indicación aprobada no están disponibles para ninguna de las autorizaciones. Se listan las 5 primeras de las 20 autorizaciones vigentes (todas de monofármaco):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49637 | RIFADOM | 550 mg comprimidos x 60 | No disponible |
| 52884 | ROCIAMIN | 200 mg comprimidos recubiertos x 20 | No disponible |
| 49524 | RIFADOM | 200 mg comprimidos x 20 | No disponible |
| 54990 | RIFAXTRIL | 550 mg comprimidos x 60 | No disponible |
| 54989 | RIFAXTRIL | 550 mg comprimidos x 30 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas**: se identificaron 69 interacciones, entre ellas:
  - **Mayor**: vacuna viva contra el cólera (cepa *Vibrio cholerae* CVD 103-HgR).
  - **Moderadas** (ejemplos): warfarina, ciclosporina, tolvaptán, cabozantinib, alpelisib, apalutamida, daclatasvir, ledipasvir, ácido picosulfúrico.
- **Señal de seguridad relevante**: la literatura sugiere que el uso de rifaximina podría favorecer infecciones por *Candida* resistentes a micafungina en pacientes trasplantados.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La rifaximina carece de actividad antifúngica, no existen ensayos clínicos y la única publicación disponible indica un riesgo asociado, no un beneficio. El puntaje alto de TxGNN no se respalda con un mecanismo plausible.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la rifaximina.
- Advertencias y contraindicaciones del prospecto de ANMAT (pendiente de obtener).
- Evidencia preclínica de actividad antifúngica o de un efecto beneficioso sobre la candidiasis oral.
- Evaluación del riesgo de sobrecrecimiento fúngico en poblaciones vulnerables (trasplantados, cirróticos).

**Nota sobre otras predicciones:** las demás indicaciones predichas (fístula comisural del labio, osteorradionecrosis de la mandíbula, leucoedema oral, síndrome de boca ardiente y candidiasis) tampoco cuentan con evidencia que las respalde. Para la candidiasis en general, los estudios observacionales disponibles indican riesgo y no un papel terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

