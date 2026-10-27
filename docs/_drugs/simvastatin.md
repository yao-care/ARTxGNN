---
layout: default
title: Simvastatin
parent: Evidencia Alta (L1-L2)
nav_order: 228
evidence_level: L1
indication_count: 8
last_modified_at: 2026-10-13
description: "Simvastatin: nueva indicación predicha, Hipercolesterolemia familiar (nivel de evidencia L1). Indicación original: Hipertrigliceridemia (según el grafo de conocimiento"
monitor_inn: "SIMVASTATIN"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Simvastatin
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **8** 
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

## Simvastatina: De Hipertrigliceridemia a Hipercolesterolemia Familiar
{: .text-alpha }

## Resumen en Una Frase

La simvastatina es una estatina (inhibidor de la HMG-CoA reductasa), utilizada originalmente para el tratamiento de dislipidemias y la prevención de enfermedad cardiovascular y cerebrovascular.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**, con **8 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta indicación ya figura entre las indicaciones originales del fármaco (hipercolesterolemia familiar homocigota), por lo que la predicción es concordante con el uso conocido y no constituye un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertrigliceridemia (según el grafo de conocimiento; el texto de indicación aprobado en ANMAT no está disponible) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción registrada en la base de datos. Según la información farmacológica conocida, la simvastatina inhibe la HMG-CoA reductasa, reduce la síntesis hepática de colesterol y aumenta la expresión de receptores de LDL, lo que disminuye el colesterol LDL (LDL-C).

La hipercolesterolemia familiar se caracteriza por un defecto en la depuración de LDL (habitualmente variantes en LDLR, APOB o PCSK9). Como la simvastatina actúa justamente sobre la síntesis de colesterol y la captación de LDL, el mecanismo es directamente aplicable. La indicación original del fármaco incluye hiperlipidemias, hipercolesterolemia familiar homocigota y aterosclerosis.

Es importante matizar que la respuesta es menor en pacientes con mutaciones nulas del receptor de LDL, por lo que a menudo se requiere terapia adicional (ezetimiba, inhibidores de PCSK9). Otras predicciones del modelo (por ejemplo, hipercolesterolemia autosómica dominante) corresponden esencialmente al mismo fenotipo y también son concordantes con el uso ya conocido.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | ENHANCE: ezetimiba + simvastatina en dosis alta vs. simvastatina sola sobre la progresión de la aterosclerosis carotídea en hipercolesterolemia familiar heterocigota |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fase 3 | Completado | 248 | Eficacia y seguridad de ezetimiba coadministrada con simvastatina en adolescentes (10-17 años) con hipercolesterolemia familiar heterocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba 10 mg añadida a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de seguridad a largo plazo (hasta 24 meses) de ezetimiba con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completado | 249 | Alirocumab vs. placebo en hipercolesterolemia familiar heterocigota no controlada con terapia hipolipemiante; el papel de la simvastatina (terapia de base) no puede confirmarse |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fase 3 | Completado | 442 | Efectos renales de rosuvastatina y simvastatina durante 6 semanas en dislipidemia tipo IIa/IIb, incluida hipercolesterolemia familiar heterocigota |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completado | 153 | Alirocumab vs. placebo en niños y adolescentes con hipercolesterolemia familiar heterocigota; simvastatina probablemente como terapia de base |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Fase 2 | Completado | 527 | Estudio de búsqueda de dosis de LY3015014 en hipercolesterolemia primaria; la simvastatina no es el agente en estudio |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | ECA | N Engl J Med | Simvastatina con o sin ezetimiba en hipercolesterolemia familiar (ENHANCE), sobre la progresión de la aterosclerosis |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Estatinas en niños con hipercolesterolemia familiar |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Actualización de la revisión sobre estatinas en niños con hipercolesterolemia familiar |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisión | Drug Safety | Beneficios y riesgos de la simvastatina en pacientes con hipercolesterolemia familiar |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Revisión | Expert Opin Drug Saf | Evaluación de beneficios y riesgos de la simvastatina en hipercolesterolemia familiar |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Estudio comparativo | Nutr Metab Cardiovasc Dis | Atorvastatina vs. simvastatina en hipercolesterolemia familiar heterocigota: eficacia sobre LDL-C y variables de coagulación |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guía | J Am Coll Cardiol | Guía ACC/AHA 2026 para el manejo de la dislipidemia, que reemplaza la guía de 2018 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocr Pract | Guías AACE/ACE para el manejo de la dislipidemia y la prevención cardiovascular |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Estudio transversal | J Clin Med | Inmunidad celular innata y adquirida en niños con hipercolesterolemia familiar tratados con simvastatina 10 mg (26 niños) |
| [1346327](https://pubmed.ncbi.nlm.nih.gov/1346327/) | 1992 | Estudio clínico | Lancet | Simvastatina y lipoproteína(a) |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40944 | COLEFLUX | 80 mg comprimidos recubiertos x 30 | No disponible |
| 14602 | REDUSTEROL | 20 mg comprimidos x 30 | No disponible |
| 20850 | LISAC | 10 mg comprimidos recubiertos x 30 | No disponible |
| 33230 | TANAVAT | 20 mg comprimidos x 30 | No disponible |
| 18182 | ZOCOR | 20 mg comprimidos x 30 | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, miopatía y enfermedades musculares, rabdomiólisis, trombocitopenia, hiperglucemia, diabetes mellitus y cetoacidosis diabética, gota, úlcera péptica, hipotensión, trastornos de la coagulación, síndrome coronario agudo, infarto de miocardio, hipofosfatemia, hemoglobinopatía y abuso de sustancias, entre otras.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel **mayor** destacan **amiodarona**, **amlodipino** y **fenofibrato**. Entre las de nivel moderado figuran zidovudina, paclitaxel, nifedipino, omeprazol, aprepitant y etanol, entre otras.
- **Interacción con antirretrovirales**: los inhibidores de proteasa y el cobicistat elevan la exposición a simvastatina (inhibición de CYP3A4) y aumentan el riesgo de miopatía y rabdomiólisis; las guías suelen aconsejar evitar la simvastatina con inhibidores de proteasa potenciados.

Las advertencias y contraindicaciones del prospecto de ANMAT no pudieron obtenerse; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados (como ENHANCE y el estudio en adolescentes con ezetimiba + simvastatina) y abundante literatura, incluidas revisiones Cochrane y guías clínicas, que respaldan el uso de simvastatina en hipercolesterolemia familiar. La indicación es concordante con el uso ya conocido, por lo que se trata más de una confirmación que de un reposicionamiento. Se recomienda proceder con salvaguardas por las interacciones relevantes y el riesgo muscular y hepático.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones y texto de indicación aprobado de las autorizaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Definir un plan de monitoreo de seguridad (función hepática, síntomas musculares/CK) y gestión de interacciones (amiodarona, amlodipino, fenofibrato, inhibidores de proteasa)
- Aclarar el papel de la simvastatina (terapia de base vs. brazo en estudio) en los ensayos con relevancia incierta

**Otras predicciones del modelo (no recomendadas por ahora):**
- Hipercolesterolemia autosómica dominante (L1, Proceed with Guardrails): esencialmente el mismo fenotipo que el de la hipercolesterolemia familiar heterocigota.
- HIV (L3, pregunta de investigación): la evidencia trata sobre dislipidemia asociada a HIV e interacciones farmacológicas, no sobre un efecto de la simvastatina contra el virus; un estudio piloto no mostró actividad anti-HIV.
- Infarto de tronco encefálico (L4, Hold): la única publicación recuperada es un estudio preclínico de otra intervención.
- Deficiencia de proteína de transferencia de ésteres de colesterilo, hipercolesterolemia por deficiencia de colesterol 7α-hidroxilasa, amiloidosis ABri y trastorno del neurodesarrollo con marcha atáxica (L5, Hold): solo predicción computacional, sin ensayos ni literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

