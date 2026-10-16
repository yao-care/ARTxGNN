---
layout: default
title: Econazole
parent: Evidencia Moderada (L3-L4)
nav_order: 132
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Econazole: nueva indicación predicha, Granuloma de Majocchi (nivel de evidencia L4). Indicación original: Tinea pedis, tinea corporis, infecciones por tinea…"
monitor_inn: "econazole"
predicted_indications: ["Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease", "superficial mycosis", "dermatophytosis of scalp or beard", "tinea profunda", "vulvovaginal candidiasis"]
---

# Econazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Econazol: De Infecciones Fúngicas Cutáneas a Granuloma de Majocchi

## Resumen en Una Frase

Econazol es un antifúngico imidazólico de uso tópico, originalmente utilizado para el tratamiento de la tinea pedis, la tinea corporis, la candidiasis cutánea y la pitiriasis versicolor.
El modelo TxGNN predice que podría ser efectivo para **Granuloma de Majocchi**, con **0 ensayos clínicos** y **1 publicación** (un reporte de caso) que actualmente respaldan esta dirección.
La evidencia es muy limitada y se basa casi exclusivamente en la predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tinea pedis, tinea corporis, infecciones por tinea, candidiasis cutánea, pitiriasis versicolor y dermatofitosis de la ingle y la zona perianal (según el grafo de conocimiento; las autorizaciones locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Granuloma de Majocchi |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El econazol es un antifúngico imidazólico. Actualmente no se dispone de datos detallados sobre su mecanismo de acción en los datos compilados para este informe. Sin embargo, según la información conocida de la clase, los azoles inhiben la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), lo que bloquea la síntesis de ergosterol, un componente esencial de la membrana fúngica.

El granuloma de Majocchi es una infección dermatofítica folicular y perifolicular profunda (típicamente por *Trichophyton rubrum*). Es, en esencia, una extensión de las indicaciones de tinea ya aprobadas, por lo que existe plausibilidad mecanística clara.

La principal limitación es farmacocinética: la afectación folicular profunda suele requerir tratamiento sistémico, porque los agentes tópicos penetran mal. La única literatura disponible es un reporte de caso centrado en el diagnóstico, sin datos específicos de econazol.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37899944](https://pubmed.ncbi.nlm.nih.gov/37899944/) | 2023 | Reporte de caso | Case Reports in Dermatology | Hombre de 54 años con granuloma de Majocchi, "el gran imitador": las infecciones fúngicas pueden confundirse con eccema o psoriasis y tratarse con corticoides tópicos, lo que genera tinea incognita. Se centra en el diagnóstico, sin datos de econazol. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 10790 | FILODERMA PLUS | Crema x 20 g | No disponible en el registro |
| 14091 | GRISEOCREM NF | Pomada x 20 g | No disponible en el registro |

Ambas autorizaciones están vigentes (fabricante: Teva Argentina).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 41 posibles interacciones en la base consultada, todas de nivel de gravedad no clasificado. Entre las principales figuran clotrimazol, fluconazol, metformina, omeprazol, lansoprazol, rosiglitazona, glipizida, dexametasona, clopidogrel, heparina, fluticasona, levotiroxina, aciclovir, diazepam, lorazepam, citarabina y didanosina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo existe un reporte de caso sobre diagnóstico, sin ensayos clínicos ni datos específicos de econazol. Además, la afectación folicular profunda limita la utilidad de una formulación tópica, por lo que la predicción, aunque plausible, no está respaldada por evidencia suficiente.

**Para avanzar se necesita:**
- Revisar el prospecto de ANMAT para obtener advertencias y contraindicaciones, y los textos de indicación aprobada.
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar estudios clínicos o series de casos específicos de econazol (tópico o sistémico) en granuloma de Majocchi.
- Evaluar la penetración folicular de la crema y si se necesitaría terapia sistémica combinada.

---

### Nota sobre otras indicaciones predichas

Aunque el informe se centra en la predicción de mayor puntaje, otras predicciones del modelo muestran un panorama distinto:

- **Candidiasis vulvovaginal** (puntaje 99.50%, nivel L3, recomendación *Proceed with Guardrails*): cuenta con estudios clínicos directos sobre econazol, incluyendo un estudio doble ciego comparativo con clotrimazol y un estudio multicéntrico de 996 casos. Es un uso ya establecido en otras regiones, por lo que tiene menor novedad pero mayor respaldo clínico que el granuloma de Majocchi. Requiere monitoreo de susceptibilidad por resistencia a azoles y especies de *Candida* no albicans.
- **Micosis superficial** (L3): en gran parte reproduce las indicaciones ya aprobadas.
- **Dermatofitosis de cuero cabelludo o barba** (L3): el econazol sería, como máximo, adyuvante.
- **Infección ectothrix, endothrix y tinea profunda** (L5): solo respaldadas por la predicción del modelo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

