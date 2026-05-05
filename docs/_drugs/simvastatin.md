---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Simvastatin: De Hipercolesterolemia a Hipercolesterolemia Familiar

## Resumen en Una Frase

Simvastatin es un inhibidor de la HMG-CoA reductasa de la clase estatinas, originalmente utilizado para reducir los niveles de colesterol LDL y el riesgo cardiovascular en pacientes con hipercolesterolemia. El modelo TxGNN predice que podría ser efectivo para la **Hipercolesterolemia Familiar (Familial Hypercholesterolemia)**, con **19 ensayos clínicos** y **18 publicaciones** que actualmente respaldan esta dirección. La evidencia disponible, incluyendo las guías ACC/AHA 2026, confirma que esta predicción es sólida y científicamente consistente con la práctica clínica establecida.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia / Reducción del riesgo cardiovascular |
| Nueva Indicación Predicha | Hipercolesterolemia Familiar (Familial Hypercholesterolemia) |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, según la información conocida, simvastatin pertenece a la clase de inhibidores de la HMG-CoA reductasa (estatinas). Su eficacia en la reducción del colesterol LDL ha sido ampliamente comprobada, y mecanísticamente es directamente aplicable a la fisiopatología de la hipercolesterolemia familiar: al inhibir la síntesis hepática de colesterol, simvastatin desencadena una regulación compensatoria al alza de los receptores de LDL (LDLR) en los hepatocitos.

La hipercolesterolemia familiar (FH) es un trastorno monogénico hereditario —principalmente asociado a mutaciones en el gen LDLR— que impide la eliminación eficiente del colesterol LDL circulante, acortando la expectativa de vida entre 15 y 30 años si no se trata adecuadamente. Los pacientes con FH heterocigota conservan receptores LDLR residuales con actividad parcial: simvastatin maximiza la función de estos receptores para reducir el LDL-C plasmático. Esta acción farmacológica hace que la predicción del modelo TxGNN tenga una base biológica sólida y directamente trasladable a la clínica.

La predicción con un puntaje de 99.63% es además consistente con la evidencia clínica acumulada durante décadas: el tratamiento con estatinas —incluido simvastatin— es reconocido como estándar de atención en FH en las guías internacionales más recientes (ACC/AHA 2026, AACE/ACE 2017), y múltiples ensayos de Fase 3 han evaluado directamente simvastatin en esta población, tanto en monoterapia como en combinación con ezetimibe.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | Ensayo ENHANCE: ezetimibe + simvastatin en dosis alta vs simvastatin solo; evaluación de progresión de aterosclerosis carotídea en HeFH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimibe 10 mg co-administrado con atorvastatin o simvastatin en hipercolesterolemia familiar homocigota (HoFH) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Seguridad y tolerabilidad a largo plazo (hasta 24 meses) de ezetimibe agregado a atorvastatin o simvastatin en HoFH; extensión abierta del estudio previo |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fase 3 | Completado | 248 | Ezetimibe en co-administración con simvastatin en adolescentes de 10-17 años con HeFH: eficacia y seguridad en población pediátrica |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Fase 3 | Completado | 216 | Alirocumab como terapia complementaria a estatinas estables (incluyendo simvastatin) en HeFH y pacientes de alto riesgo cardiovascular |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Fase 3 | Completado | 486 | Alirocumab vs placebo en HeFH: evaluación de reducción de LDL-C a 24 semanas; mayor escala del programa con simvastatin como posible terapia de fondo |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completado | 249 | Alirocumab vs placebo en HeFH no controlada con terapia modificadora de lípidos; simvastatin como posible comparador o terapia de fondo |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Fase 3 | Completado | 2341 | Alirocumab: seguridad y tolerabilidad a largo plazo en alto riesgo cardiovascular con hiperlipidemia; simvastatin como tratamiento de fondo |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fase 3 | Completado | 442 | Comparación de efectos renales de rosuvastatina y simvastatin en dislipidemia tipo IIa y IIb, incluyendo HeFH |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Fase 4 | Completado | 194 | Colesevelam en pacientes pediátricos con HeFH en dosis estable de estatina aprobada para pediatría (incluyendo simvastatin) o sin tratamiento previo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guía de Práctica Clínica | Circulation | Guía ACC/AHA 2026 sobre manejo de dislipidemia; reemplaza la guía 2018 e incluye recomendaciones actualizadas sobre estatinas en FH |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisión Sistemática Cochrane | Cochrane Database Syst Rev | Revisión sistemática de estatinas para niños con FH: evaluación de eficacia, seguridad y calidad de la evidencia disponible |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | ECA | N Engl J Med | Simvastatin con o sin ezetimibe en FH (ensayo ENHANCE): efecto sobre progresión de aterosclerosis carotídea evaluada por IMT |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Estudio Clínico | J Am Coll Cardiol | Estatinas en FH heterocigota: cuantificación de la reducción de eventos de enfermedad coronaria y mortalidad total en la práctica clínica |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Evaluación Beneficio-Riesgo | Expert Opin Drug Saf | Beneficios y riesgos de simvastatin en FH: análisis integral de seguridad y tolerabilidad a largo plazo para selección de terapia |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | ECA | Int Angiology | Eficacia y seguridad del tratamiento prolongado con ezetimibe/simvastatin en FH; evaluación de reducción de LDL-C y progresión de IMT carotídea |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Estudio Clínico | J Clin Med | Evaluación del efecto de simvastatin 10 mg sobre parámetros de inmunidad celular innata y adquirida en niños con FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisión | Drug Safety | Beneficios y riesgos de simvastatin en FH: perspectiva sobre tolerabilidad crónica y perfil de seguridad |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía de Práctica Clínica | Endocr Pract | Guías AACE/ACE 2017 para manejo de dislipidemia y prevención cardiovascular; incluye recomendaciones de estatinas en FH |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Estudio Genético | Pharmacogenomics J | Estrategia NGS que combina paneles genéticos de FH con regiones farmacogenómicas para guiar la prescripción de estatinas en práctica clínica |

---

## Información de Mercado en Argentina

Simvastatin no cuenta con autorizaciones de comercialización registradas ante ANMAT según los datos disponibles. No se recuperaron fichas de producto ni registros sanitarios activos para este fármaco en Argentina, lo que implica que cualquier uso clínico requeriría previamente la aprobación regulatoria correspondiente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3 completados —incluyendo el emblemático ensayo ENHANCE (N=720)— y las guías internacionales más recientes (ACC/AHA 2026) respaldan con solidez el uso de simvastatin en hipercolesterolemia familiar, confirmando la predicción del modelo TxGNN. El principal obstáculo para el avance en Argentina es la ausencia de autorización de comercialización ante ANMAT, no la fortaleza de la evidencia clínica.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción detallado (MOA) desde DrugBank para completar el análisis farmacológico formal del expediente
- Recuperar el prospecto oficial (ANMAT o referencia FDA/EMA) para documentar advertencias específicas, contraindicaciones e interacciones farmacológicas relevantes (especialmente con inhibidores potentes de CYP3A4: itraconazol, ketoconazol, inhibidores de proteasa del VIH, ciclosporina)
- Iniciar el proceso de registro ante ANMAT para obtener autorización de comercialización en Argentina
- Definir un plan de monitoreo de seguridad para poblaciones especiales: pediatría (≥10 años con FH), pacientes con insuficiencia hepática y adultos mayores
- Establecer guardrails farmacológicos explícitos relativos a la miopatía/rabdomiólisis inducida por estatinas, dado que simvastatin es metabolizado por CYP3A4 y presenta mayor riesgo de interacciones que otras estatinas de la clase
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

