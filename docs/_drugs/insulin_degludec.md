---
layout: default
title: Insulin Degludec
parent: Evidencia Alta (L1-L2)
nav_order: 166
evidence_level: L1
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **6** 
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

# Insulina Degludec: De Diabetes Mellitus a Diabetes Mellitus Tipo 1

## Resumen en Una Frase

La insulina degludec es un análogo de insulina basal de acción ultra larga, originalmente utilizado para el tratamiento de la diabetes mellitus y la cetoacidosis diabética.
El modelo TxGNN predice que podría ser efectiva para la **diabetes mellitus tipo 1**, aunque en la práctica se trata de un uso ya establecido del fármaco más que de un reposicionamiento propiamente dicho.
Esta dirección está respaldada por **44 ensayos clínicos** y **20 publicaciones** en los datos compilados para este informe.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus y cetoacidosis diabética (según el grafo de conocimiento; el texto de indicación de la licencia local está vacío) |
| Nueva Indicación Predicha | Diabetes mellitus tipo 1 |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la insulina degludec es un análogo de insulina basal de acción ultra larga que se une al receptor de insulina y reduce la glucemia. Su eficacia en la diabetes mellitus está comprobada.

La diabetes tipo 1 se caracteriza por deficiencia de insulina, de modo que el reemplazo de insulina basal es la base del tratamiento. La diabetes tipo 1 ya está contenida dentro de la indicación original (diabetes mellitus), por lo que el puntaje alto del modelo (0.994) es coherente con el mecanismo establecido y con décadas de uso clínico.

Otras indicaciones predichas (ooforitis autoinmune, opsismodisplasia, síndrome de disfunción sensible a tiamina, síndrome de la persona rígida clásico y síndrome de extremidad rígida focal) no cuentan con ensayos ni literatura. Su recomendación es **Hold**. En varios casos, la insulina trataría solo la diabetes asociada y no la enfermedad de fondo.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (priorizando Fase 3 completados y estudios directos con degludec en diabetes tipo 1).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02034513](https://clinicaltrials.gov/study/NCT02034513) | Fase 3 | Completado | 501 | SWITCH 1: degludec vs. glargina, ambas con insulina aspart, en diabetes tipo 1 (cruzado doble ciego) |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Fase 3 | Completado | 1108 | Insulina aspart de acción rápida vs. NovoRapid, ambas con degludec, en adultos con diabetes tipo 1 |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Fase 3 | Completado | 834 | Aspart de acción rápida vs. NovoRapid, con degludec, en niños y adolescentes con diabetes tipo 1 |
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Fase 3 | Completado | 692 | Insulina semanal efsitora alfa vs. degludec en diabetes tipo 1 con inyecciones diarias múltiples |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Fase 3 | Completado | 362 | Degludec/aspart una vez al día vs. detemir en niños y adolescentes con diabetes tipo 1 |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Fase 3 | Completado | 548 | Degludec/aspart más aspart vs. detemir más aspart en diabetes tipo 1 (BOOST T1) |
| [NCT01569841](https://clinicaltrials.gov/study/NCT01569841) | Fase 3 | Completado | 24 | Degludec vs. glargina en control glucémico con monitoreo continuo de glucosa |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Fase 4 | Completado | 343 | Toujeo vs. Tresiba: tiempo en rango y variabilidad glucémica con monitoreo continuo en diabetes tipo 1 |
| [NCT03838783](https://clinicaltrials.gov/study/NCT03838783) | Fase 4 | Desconocido | 30 | Degludec con infusión subcutánea continua de insulina en pacientes con diabetes tipo 1 que realizan ejercicio intenso |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Fase 2 | Completado | 178 | Dos formulaciones de degludec vs. glargina, con aspart, en esquema basal-bolo en diabetes tipo 1 |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | ECA | Lancet | ONWARDS 6: insulina icodec semanal vs. degludec diaria en diabetes tipo 1 (fase 3a, treat-to-target) |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | ECA | Lancet Diabetes Endocrinol | EXPECT: degludec vs. detemir en embarazadas con diabetes tipo 1 (no inferioridad) |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | ECA | Lancet | QWINT-5: efsitora semanal vs. degludec diaria en adultos con diabetes tipo 1 |
| [40903851](https://pubmed.ncbi.nlm.nih.gov/40903851/) | 2025 | Estudio clínico (clasificado como cohorte) | Diabetes Obes Metab | Degludec temprana con infusión intravenosa de insulina en cetoacidosis diabética |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Metaanálisis | Clin Ther | Eficacia y tolerabilidad de degludec vs. glargina y detemir en diabetes tipo 1 y 2 |
| [40627908](https://pubmed.ncbi.nlm.nih.gov/40627908/) | 2025 | Metaanálisis | J Diabetes Complications | Comparación de eficacia y seguridad de efsitora vs. degludec |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Revisión sistemática | Cochrane Database Syst Rev | Análogos de insulina de acción (ultra)larga en diabetes tipo 1 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Revisión sistemática y metaanálisis en red | Value Health | Eficacia y seguridad relativa de regímenes de insulina basal en adultos con diabetes tipo 1 |
| [35147781](https://pubmed.ncbi.nlm.nih.gov/35147781/) | 2022 | Estudio observacional | Acta Diabetol | Resultados del embarazo en mujeres con diabetes tipo 1 que usan degludec |
| [31393288](https://pubmed.ncbi.nlm.nih.gov/31393288/) | 2019 | Revisión | Cardiol Rev | Revisión de insulinas basales de acción prolongada de aprobación reciente |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57128 | INSULINA TRESIBA FLEXTOUCH | 200 U lapiceras x3 x3 ml | No disponible en los datos de la licencia |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 351 interacciones en total. Entre las principales (nivel moderado) figuran:
  - Otros antidiabéticos: metformina, pioglitazona, alogliptina y albiglutida.
  - Agonistas adrenérgicos y simpaticomiméticos: epinefrina, salbutamol, formoterol, fenilefrina y pseudoefedrina.
  - Betabloqueantes: acebutolol.
  - Corticoides: hidrocortisona.
  - Hormonas: estradiol, levonorgestrel y noretisterona.
  - Otros: hidroclorotiazida, doxiciclina, alpelisib y etanol.
  - Los corticoides tópicos (hidrocortisona tópica y aclometasona tópica) presentan interacciones de nivel leve.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La diabetes tipo 1 es una indicación central y bien establecida de la insulina degludec, respaldada por múltiples ensayos de Fase 3 completados y metaanálisis. Se mantienen salvaguardas porque faltan los datos del prospecto local y del mecanismo de acción en los datos compilados.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente no disponible.
- Confirmar el texto de indicación aprobada en la licencia local, que figura vacío.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Revisar las interacciones de nivel moderado, sobre todo con otros antidiabéticos, betaagonistas y corticoides, y definir un plan de monitoreo de glucemia e hipoglucemia.
- Mantener en **Hold** las otras cinco indicaciones predichas hasta contar con evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

