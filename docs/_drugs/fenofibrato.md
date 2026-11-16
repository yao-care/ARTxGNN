---
layout: default
title: Fenofibrato
parent: Solo Predicción del Modelo (L5)
nav_order: 174
evidence_level: L5
indication_count: 1
drugbank_id: DB01039
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-16
description: "Fenofibrato: nueva indicación predicha, Cholesterol-ester transfer protein deficiency (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Fenofibrato
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Fenofibrato: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## Resumen en Una Frase

El fenofibrato es un fibrato que se comercializa en Argentina con múltiples autorizaciones vigentes. Sin embargo, el respaldo es muy débil: **1 ensayo clínico** relacionado con la enfermedad (que no evalúa fenofibrato) y **10 publicaciones**, entre las que solo un estudio de cohorte de 1984 incluye a un paciente homocigoto tratado con fenofibrato.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Cholesterol-ester transfer protein deficiency |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 (muy limitado; ver justificación abajo) |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (17 de 17) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 17 (vigentes: 17) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el fenofibrato activa el receptor PPAR-alfa, lo que aumenta la actividad de la lipoproteína lipasa y la oxidación de ácidos grasos. El resultado es una reducción de triglicéridos y un aumento del colesterol HDL, con un efecto modesto sobre el colesterol LDL.

La hipercolesterolemia familiar homocigota se debe a una actividad casi nula del receptor de LDL. El efecto del fenofibrato sobre el LDL depende en parte de que exista cierta función residual de ese receptor. Por eso es poco probable que logre una reducción relevante del LDL-C en esta enfermedad.

El puntaje del modelo es alto, pero probablemente refleja la cercanía de esta enfermedad con otros trastornos lipídicos en el modelo y no un vínculo mecanístico específico. La predicción debe interpretarse con cautela.

**Justificación del nivel de evidencia:** se asigna L3 porque existe un estudio de cohorte observacional (PMID 6593751) que incluyó a un paciente con la enfermedad. Se trata de un solo paciente en una cohorte de 22, publicada en 1984. Si se exigiera evidencia más sólida, la evidencia efectiva sería prácticamente solo la predicción del modelo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Estudio abierto de alirocumab (inhibidor de PCSK9) en niños y adolescentes de 8 a 17 años con hipercolesterolemia familiar homocigota. Mide el LDL-C a la semana 12. **No incluye fenofibrato**, por lo que no aporta evidencia directa para este fármaco. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Revisión | Indian Heart Journal | Fármacos hipolipemiantes no estatínicos. La indicación más definida de fenofibrato en monoterapia es el triglicérido en ayunas >500 mg/dl, para reducir el riesgo de pancreatitis aguda. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Revisión | Annals of the New York Academy of Sciences | Tratamiento farmacológico y quirúrgico de niños y adolescentes con dislipidemias, sobre todo hipercolesterolemia familiar. Menciona al fenofibrato entre los fármacos que lograron reducir los lípidos. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocrine Practice | Guías de AACE/ACE para el manejo de dislipidemia y prevención cardiovascular. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Revisión | Current Atherosclerosis Reports | Manejo de la dislipidemia en el embarazo. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Revisión | Indian Heart Journal | LDL-C, estatinas e inhibidores de PCSK9 en hipercolesterolemia grave. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Revisión | Pharmacotherapy | Ezetimibe como inhibidor selectivo de la absorción de colesterol. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Revisión | Drugs | Farmacología y potencial terapéutico de atorvastatina en hiperlipidemias. |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Revisión | Canadian Journal of Cardiology | Avances en el tratamiento farmacológico de la dislipidemia, con foco en atorvastatina. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Estudio farmacocinético | Pharmacotherapy | Interacciones farmacocinéticas de lomitapida (aprobada para hipercolesterolemia familiar homocigota) con hipolipemiantes, entre ellos el fenofibrato. No evalúa eficacia del fenofibrato. |

---

## Información de Mercado en Argentina

El texto de indicación aprobada no figura registrado en los datos locales. Se muestran las primeras 5 de las autorizaciones vigentes (todas de monodroga).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 47731 | LIPTUIN | 200 mg cápsulas x 30 |
| 52158 | FENOSANE | 200 mg cápsulas x 30 |
| 35060 | CRAVERIL | comprimidos recubiertos x 30 |
| 1289 | PROCETOKEN | 100 mg comprimidos x 60 |
| 28384 | MINUSLIP | 200 mg cápsulas x 30 |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El único ensayo clínico asociado a la enfermedad evalúa otro fármaco (alirocumab). La única observación con fenofibrato es un paciente homocigoto en una cohorte de 1984.
- El mecanismo del fenofibrato (efecto modesto sobre el LDL, que depende de cierta función residual del receptor de LDL) no coincide bien con una enfermedad de actividad casi nula de ese receptor. El puntaje alto del modelo no es suficiente por sí solo.

**Para avanzar se necesita:**
- Estudios clínicos de fenofibrato, solo o como terapia adyuvante, en pacientes con hipercolesterolemia familiar homocigota, con LDL-C como criterio principal.
- Datos detallados del mecanismo de acción.
- Revisión del prospecto autorizado en Argentina para completar advertencias, contraindicaciones e interacciones.
- Si se avanzara, un plan de monitoreo de función hepática y renal, y de riesgo de miopatía en combinación con estatinas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

