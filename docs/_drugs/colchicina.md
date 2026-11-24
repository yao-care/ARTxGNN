---
layout: default
title: Colchicina
parent: Solo Predicción del Modelo (L5)
nav_order: 125
evidence_level: L5
indication_count: 2
drugbank_id: DB01394
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-24
description: "Colchicina: nueva indicación predicha, Malaria por Plasmodium falciparum (Plasmodium falciparum malaria) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 7 (en el listado vigente: 7)"
---

# Colchicina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Colchicina: Malaria por Plasmodium falciparum (Plasmodium falciparum malaria)
{: .text-alpha }

## Resumen en Una Frase

Colchicina es un fármaco que se comercializa en Argentina como único principio activo y en asociación con alopurinol. El modelo TxGNN predice que podría ser efectivo para **Malaria por Plasmodium falciparum (Plasmodium falciparum malaria)**. Actualmente no hay ensayos clínicos registrados y solo hay **2 publicaciones** preclínicas, ninguna de las cuales estudia la eficacia de colchicina contra esta enfermedad.

<!-- review:begin ar-lic-20261124-colchicina-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Colchicina es un fármaco que se comercializa en Argentina en siete autorizaciones locales de un solo principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), la mayoría de los productos (COLPURIL, ARTREX RETARD) son asociaciones de colchicina con alopurinol; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-colchicina-1 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malaria por Plasmodium falciparum (Plasmodium falciparum malaria) |
| Puntaje de Predicción TxGNN | 0.9960 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Colchicina (traducción no oficial): «Se ha postulado que la eficacia de la colchicina como tratamiento de la gota se debe a su capacidad para bloquear las respuestas inflamatorias mediadas por neutrófilos inducidas por los cristales de urato monosódico en el líquido sinovial. La colchicina altera la polimerización de la β-tubulina en microtúbulos, lo que impide la activación, la desgranulación y la migración de los neutrófilos a los sitios de inflamación.» Texto original en inglés: "Colchicine’s effectiveness as a treatment for gout has been postulated to be due to its ability to block neutrophil-mediated inflammatory responses induced by monosodium urate crystals in synovial fluid. Colchicine disrupts the polymerization of β-tubulin into microtubules, thereby preventing the activation, degranulation, and migration of neutrophils to sites of inflammation." ([DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2), versión del 2026-10-16; consultado el 2026-11-19). Según la información conocida de la literatura farmacológica general, colchicina se une a la tubulina e inhibe la polimerización de los microtúbulos. Los parásitos del género Plasmodium dependen de los microtúbulos para la mitosis, la motilidad y la invasión celular, por lo que un mecanismo de disrupción de microtúbulos es biológicamente plausible.

Los dos estudios disponibles apoyan esta idea solo de forma indirecta. El trabajo de 1994 sobre la expresión del gen pfmdr1 en células de mamífero sugiere que colchicina podría ser sustrato de transportadores de eflujo, lo que plantea una posible preocupación de resistencia. El trabajo de 2013 describe la alteración de microtúbulos en P. falciparum causada por curcumina, no por colchicina. No hay datos de eficacia antipalúdica de colchicina.

Además, colchicina tiene un índice terapéutico estrecho y toxicidad gastrointestinal y hematológica relevante, lo que sería una barrera importante para un uso antipalúdico. El puntaje elevado del modelo es solo una predicción computacional y no está respaldado por evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Preclínico in vitro | Molecular and Cellular Biology | La expresión de pfmdr1 de Plasmodium en células de mamífero se asocia con mayor sensibilidad a cloroquina; relevante para mecanismos de transporte y resistencia, no evalúa eficacia de colchicina. |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Preclínico in vitro | PLoS One | Curcumina altera los microtúbulos de P. falciparum; colchicina no es el agente evaluado. |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 24160 | COLCHICINA HOUDE | comp.x 60 | Ariston | Vigente |
| 8577 | COLCHICINA HOUDE | comp.x 20 | Ariston | Vigente |
| 6445 | COLPURIL | 100 mg comp.rec.x 20 | Siegfried | Vigente |
| 6449 | COLPURIL 300 RETARD | cáps.lib.prol.x 20 | Siegfried | Vigente |
| 6450 | COLPURIL 300 RETARD | cáps.lib.prol.x 50 | Siegfried | Vigente |

La tabla muestra 5 de los 7 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Consultar las advertencias y precauciones del prospecto |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen colchicina directamente contra la malaria por P. falciparum; la evidencia se limita a dos estudios preclínicos indirectos y a un puntaje de predicción del modelo. La toxicidad de colchicina y su estrecho margen terapéutico agravan la incertidumbre.

**Para avanzar se necesita:**
- Datos de eficacia in vitro e in vivo de colchicina frente a P. falciparum, incluidas cepas resistentes
- Datos detallados del mecanismo de acción y evaluación del riesgo de eflujo mediado por pfmdr1
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Evaluación de la ventana terapéutica frente a las concentraciones antipalúdicas requeridas

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2) |
| 2026-11-24 | «de un solo principio activo» → también asociación con alopurinol | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

