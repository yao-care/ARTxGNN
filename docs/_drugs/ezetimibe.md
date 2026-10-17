---
layout: default
title: Ezetimibe
parent: Evidencia Alta (L1-L2)
nav_order: 140
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-13
description: "Ezetimibe: nueva indicación predicha, Hiperlipoproteinemia (nivel de evidencia L1). Indicación original: Hiperlipidemia (según el grafo de conocimiento"
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

# Ezetimibe: De Hiperlipidemia a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimibe es un fármaco hipolipemiante, originalmente utilizado para el tratamiento de la hiperlipidemia (incluida la hipercolesterolemia familiar homocigota y la sitosterolemia).
El modelo TxGNN predice que podría ser efectivo para **hiperlipoproteinemia**, con **44 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe aclarar que esta indicación se solapa en gran medida con las indicaciones originales, por lo que no constituye un reposicionamiento en sentido estricto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperlipidemia (según el grafo de conocimiento; los textos de indicación de ANMAT no están disponibles) |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, ezetimibe inhibe la absorción intestinal de colesterol mediada por NPC1L1, lo que reduce el colesterol LDL (LDL-C). Este es el mismo mecanismo que sustenta su uso aprobado en hiperlipidemia.

La hiperlipoproteinemia y la hiperlipidemia son prácticamente el mismo grupo de trastornos del metabolismo de los lípidos. Por ello, la predicción del modelo es coherente, aunque en la práctica no representa una indicación realmente nueva.

Existe evidencia directa de Fase 3 y Fase 4, incluido el uso como tratamiento adicional o en combinación con estatinas y agentes dirigidos a PCSK9.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 44 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Fase 3 | Completado | 511 | Evolocumab vs ezetimibe en pacientes con hipercolesterolemia intolerantes a estatinas por efectos musculares; objetivo principal: cambio de LDL-C a 24 semanas |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Fase 3 | Completado | 1220 | Ezetimibe/simvastatina con niacina de liberación prolongada en hiperlipidemia tipo IIa/IIb |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Coadministración de fenofibrato y ezetimibe en hiperlipidemia mixta |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Completado | 611 | Ezetimibe/simvastatina con fenofibrato en hiperlipidemia mixta |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Fenofibrato y ezetimibe coadministrados en hiperlipidemia mixta |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | Estudio ENHANCE: ezetimibe + simvastatina en dosis alta vs simvastatina sola en la progresión de la aterosclerosis carotídea en hipercolesterolemia familiar heterocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimibe 10 mg añadido a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Fase 3 | Terminado | 49 | Uso de tratamiento abierto con ezetimibe en hipercolesterolemia familiar homocigota o sitosterolemia homocigota; sin control y terminado antes de tiempo |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Fase 4 | Completado | 40 | Ezetimibe solo vs estatina en hipercolesterolemia; estudio pequeño, aleatorizado y abierto |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completado | 1794 | Estudio observacional de 52 semanas en Japón sobre seguridad y eficacia de Zetia en uso real |

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes de las 20 disponibles.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA | JAMA | Eficacia y seguridad del inhibidor oral de PCSK9 enlicitida en hipercolesterolemia familiar heterocigota |
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA (Fase 3) | Lancet | TANDEM: combinación fija de obicetrapib y ezetimibe para reducir el LDL-C |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | ECA | Circulation | ORION-5: inclisirán en hipercolesterolemia familiar homocigota |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | ECA | Lancet | RUTHERFORD-2: evolocumab en hipercolesterolemia familiar heterocigota pese a tratamiento intensivo con estatinas, con o sin ezetimibe |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohorte | Lancet | Experiencia mundial en hipercolesterolemia familiar homocigota: características clínicas y genéticas y resultados del manejo actual |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Molecular Medicine Reports | Avances en los fármacos actuales dirigidos a la hiperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisión | J Am Coll Cardiol | Terapias nuevas y emergentes para reducir LDL-C y apolipoproteína B, sobre la base de estatinas, ezetimibe e inhibidores de PCSK9 |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Revisión | Circulation Research | Agentes hipocolesterolemiantes, su eficacia y seguridad |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Revisión | Nature Reviews Disease Primers | Hipercolesterolemia familiar: genética, fisiopatología y tratamiento |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Revisión | Drug and Therapeutics Bulletin | Actualización sobre ezetimibe: reducción del LDL-C solo o con estatina |

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de un solo principio activo, ninguna cancelada). Los textos de indicación aprobada no están disponibles.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 33428 | ZETIA | Comprimidos 10 mg x 28 | Organon Arg. |
| 35857 | EZETROL | Comprimidos 10 mg x 30 | Organon Arg. |
| 35799 | VADEL | Comprimidos 10 mg x 30 | Teva Argentina |
| 36512 | ALIPAS | Comprimidos 10 mg x 30 | Laboratorios Be |
| 42267 | ATEROCLAR COMBI | Comprimidos 10/10 mg x 30 | Beta |

El resto de las autorizaciones incluye otras marcas de ezetimibe solo y combinaciones con estatinas (por ejemplo, VASOTENAL EZ, REOVEX EZ, ROSUBER PLUS, COMBICOL).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedades musculares, enfermedad del músculo esquelético, parálisis periódica familiar, abuso/dependencia de sustancias, rabdomiólisis y fascitis nodular.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado incluyen ácido quenodesoxicólico, eluxadolina, rosuvastatina y simvastatina. Otras interacciones (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, metformina, omeprazol, morfina, vancomicina, entre otras) tienen nivel de gravedad no clasificado.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados que respaldan el uso de ezetimibe en hiperlipidemia y el fármaco está ampliamente comercializado en Argentina. Sin embargo, la indicación predicha coincide en gran medida con las indicaciones ya existentes, por lo que no aporta un reposicionamiento realmente nuevo.

**Para avanzar se necesita:**
- Obtener los textos de indicación, advertencias y contraindicaciones del prospecto de ANMAT.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Confirmar si "hiperlipoproteinemia" aporta alguna indicación adicional frente a las ya autorizadas.
- Definir un plan de monitoreo hepático y muscular, dadas las contraindicaciones del grafo de conocimiento y las interacciones con estatinas.

**Otras predicciones del modelo (no recomendadas por ahora):**
- *Hipercolesterolemia familiar* (99.38%): L1, Proceed with Guardrails. Está muy alineada con las indicaciones existentes.
- *Hipercolesterolemia por deficiencia de colesterol 7α-hidroxilasa* (99.25%): L5, Hold. Solo hay un estudio preclínico y ningún dato clínico.
- *Deficiencia de proteína de transferencia de ésteres de colesterol* (99.09%): L5, Hold. El vínculo mecanístico es débil y no hay evidencia específica de ezetimibe.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

