---
layout: default
title: Nebivolol
parent: Solo Predicción del Modelo (L5)
nav_order: 201
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Nebivolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
monitor_inn: "NEBIVOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Nebivolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Nebivolol: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Nebivolol es un betabloqueante utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; la predicción se basa solo en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, nebivolol es un betabloqueante selectivo β1 con efecto vasodilatador mediado por óxido nítrico (NO) a través del endotelio. Su eficacia en la hipertensión arterial está establecida y, mecanísticamente, podría ser aplicable al control de la presión arterial en la enfermedad renal hipertensiva.

La indicación original (hipertensión) y la nueva indicación (enfermedad renal hipertensiva maligna) están estrechamente relacionadas: la segunda es una complicación grave de la primera, en la que el control de la presión arterial es central. Sin embargo, se trata de un cuadro severo, y no cabe esperar que un betabloqueante en monoterapia sea suficiente.

El puntaje elevado (0.994) es únicamente una inferencia computacional. No existen estudios que evalúen nebivolol en esta enfermedad, por lo que la plausibilidad mecanística no equivale a evidencia de eficacia.

**Otras predicciones del modelo (todas con evidencia limitada):**
- Hipertensión renovascular maligna (99.42%): sin estudios; L5.
- Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia (99.39%): solo literatura indirecta (L4); ver más abajo.
- Hipertensión pulmonar de mecanismo multifactorial poco claro (99.39%): sin estudios; L5.
- Síndrome de Braddock (99.14%): no se identificó vínculo mecanístico claro; L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal ni para las otras predicciones.

## Evidencia de Literatura

Para la indicación principal (enfermedad renal hipertensiva maligna) actualmente no hay literatura relacionada disponible.

Para la predicción de hipertensión pulmonar por enfermedad pulmonar/hipoxia, se recuperó literatura **indirecta**, ninguna de la cual evalúa nebivolol en hipertensión pulmonar. Se muestran los estudios más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Ensayo clínico | Int J Cardiol | Estudio CARNEBI: comparación de carvedilol, nebivolol y bisoprolol en insuficiencia cardíaca moderada |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | ECA | Cardiovasc Ther | Nebivolol vs. carvedilol sobre el rendimiento al ejercicio en hipoxia de altitud en sujetos sanos |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | Estudio clínico fisiológico | J Hypertens | Efectos de betabloqueo selectivo y no selectivo sobre la presión arterial ambulatoria en hipoxia hipobárica |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisión | Cardiovasc Drugs Ther | Efectos respiratorios de los betabloqueantes en insuficiencia cardíaca |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclínico (animal) | Pharmacol Rep | Efecto renoprotector de nebivolol en lesión renal aguda en ratas, vía SGLT2 |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclínico (animal) | Can J Physiol Pharmacol | Protección de nebivolol frente a nefrotoxicidad por metotrexato en ratas (vía AKT1/Hif-1α/eNOS) |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclínico (animal) | Drug Chem Toxicol | Nebivolol atenúa el daño hepático por metotrexato (vía AKT1/Hif1α/eNOS) |
| [35202159](https://pubmed.ncbi.nlm.nih.gov/35202159/) | 2022 | Preclínico (in vitro) | Toxins | Protección de nebivolol contra el estrés oxidativo por ácidos aristolóquicos en células endoteliales |
| [23400988](https://pubmed.ncbi.nlm.nih.gov/23400988/) | 2013 | Preclínico (animal) | Anesth Analg | El bloqueo β1 altamente selectivo (nebivolol) deteriora la perfusión cerebral tras hemodilución en ratas |
| [42264321](https://pubmed.ncbi.nlm.nih.gov/42264321/) | 2026 | In vitro | Life Sci | Efectos de nebivolol sobre la respuesta endotelial en un modelo in vitro de preeclampsia |

Nota: dos referencias recuperadas (PMID 28579836, sobre toxicidad renal de contrastes yodados, y PMID 40091400, sobre nanomedicina antitumoral) no son específicas de nebivolol o no son pertinentes, por lo que se omitieron.

## Información de Mercado en Argentina

Se listan 5 de las 20 autorizaciones vigentes (todas de monodroga, ninguna cancelada). Los datos compilados no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 52016 | GADOCOR | 10 mg comprimidos recubiertos ranurados x 30 | Gador |
| 56489 | NEBIVOLOL DENVER FARMA | 5 mg comprimidos x 28 | Denver Farma |
| 58881 | CORPRES 2.5 | 2.5 mg comprimidos x 60 | Roemmers |
| 48494 | NIDIB | 5 mg comprimidos birranurados x 28 | Baliarda |
| 29100 | NEBILET | 5 mg comprimidos x 28 | Siegfried |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica, hipoglucemia, bloqueo auriculoventricular, enfermedad bronquial, síndrome del seno enfermo (incluida la forma familiar).
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las revisadas, la mayoría son de nivel moderado: epinefrina, hidrocortisona, hioscina (hiosciamina), bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, budesonida, glicopirronio, canagliflozina, dapagliflozina, clorpropamida y diciclomina, entre otras. Las de nivel menor incluyen ácido acetilsalicílico y óxido de magnesio.
- **Consideración específica**: los betabloqueantes han generado preocupación de seguridad en hipertensión pulmonar y estados hipóxicos, por lo que la seguridad debería establecerse antes de cualquier trabajo clínico en esas indicaciones.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad renal hipertensiva maligna tiene un puntaje alto (99.42%), pero se sustenta únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa. Además, es un cuadro grave en el que un betabloqueante en monoterapia probablemente no sería suficiente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) detallado del fármaco.
- Revisión sistemática de literatura específica sobre nebivolol en enfermedad renal hipertensiva y nefroesclerosis maligna.
- Información oficial de seguridad del prospecto de ANMAT (advertencias y contraindicaciones), actualmente no disponible.
- Evaluación del rol de nebivolol dentro de esquemas combinados, dado el contexto de severidad.
- Si se priorizara la hipertensión pulmonar (nivel L4, pregunta de investigación): estudios preclínicos y de seguridad dirigidos antes de cualquier trabajo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

