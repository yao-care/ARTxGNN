---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Lornoxicam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

El skill txgnn-pipeline cubre el contexto operativo del pipeline. El sistema de reporte ya contiene todas las instrucciones necesarias. Procedo directamente con la generación del informe.

---

# Lornoxicam: De Dolor Musculoesquelético y Osteoartritis a Artritis Reumatoide

## Resumen en Una Frase

Lornoxicam es un antiinflamatorio no esteroideo (AINE) de la clase oxicam, reconocido globalmente por el manejo del dolor agudo posoperatorio, osteoartritis y condiciones musculoesqueléticas, aunque actualmente no cuenta con registro en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Artritis Reumatoide (AR)**, indicación respaldada por la farmacología del fármaco y ampliamente documentada en la literatura internacional,
con **0 ensayos clínicos registrados** específicos para esta indicación y **20 publicaciones** —incluyendo estudios clínicos comparativos, revisiones farmacológicas y múltiples estudios de formulación cronoterap&eacute;utica— que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Dolor musculoesquelético agudo, osteoartritis (indicación global; sin registro en Argentina) |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Aunque el campo `original_moa` del Evidence Pack figura como dato pendiente, la literatura científica disponible caracteriza con claridad el mecanismo de lornoxicam: es un inhibidor dual no selectivo de las ciclooxigenasas **COX-1 y COX-2** perteneciente a la clase oxicam (igual que piroxicam y meloxicam). Al suprimir la conversión del ácido araquidónico, reduce la síntesis de prostaglandinas clave —especialmente **PGE₂** y **PGI₂**— responsables de la inflamación, el dolor y la fiebre. A diferencia de otros oxicams, su semivida de eliminación relativamente corta (3–5 horas) lo distingue farmacociné­ticamente y permite mayor flexibilidad en esquemas de dosificación.

La artritis reumatoide es una enfermedad inflamatoria crónica autoinmune cuya patogénesis involucra sobreexpresión de COX-2 en el tejido sinovial, elevación de PGE₂ y cascada de citoquinas proinflamatorias (IL-1β, TNF-α). La supresión directa de PGE₂ sinovial mediante inhibición de COX-1/COX-2 es, precisamente, el mecanismo central por el que los AINEs actúan en AR. Múltiples estudios de formulación incluidos en la evidencia fueron diseñados específicamente para optimizar la entrega de lornoxicam en AR, apuntando a los síntomas de exacerbación matutina —lo que confirma un escenario clínico de aplicación bien definido.

La predicción TxGNN es farmacológicamente sólida. Cabe subrayar que lornoxicam **ya es reconocido en la literatura y en mercados internacionales como tratamiento de AR**, por lo que este caso representa menos un reposicionamiento clásico y más una **oportunidad de entrada regulatoria** en el mercado argentino bajo la indicación de artritis reumatoide, para la cual actualmente no existe registro ante ANMAT.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en ClinicalTrials.gov para lornoxicam en artritis reumatoide.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [12404032](https://pubmed.ncbi.nlm.nih.gov/12404032/) | 2002 | ECA cruzado doble ciego | Reumatismo | Comparación de lornoxicam 8/16 mg vs diclofenaco 150 mg/día en AR; evaluación de rango de dosis y seguridad |
| [12207202](https://pubmed.ncbi.nlm.nih.gov/12207202/) | 2002 | Estudio clínico (largo plazo) | Minerva Medica | Evaluación de seguridad y eficacia terapéutica a largo plazo de lornoxicam en artritis reumatoide |
| [12087911](https://pubmed.ncbi.nlm.nih.gov/12087911/) | 2002 | Estudio clínico | Terapevticheskii Arkhiv | Eficacia y seguridad de xefocam (lornoxicam) en AR con hipertensión arterial concomitante; efectos sobre presión arterial y variabilidad del ritmo cardíaco |
| [22469263](https://pubmed.ncbi.nlm.nih.gov/22469263/) | 2011 | Monografía/Revisión | Profiles of Drug Substances | Perfil integral de lornoxicam: usos en osteoartritis y AR, mecanismo de acción, farmacocinética, métodos de análisis |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Revisión farmacológica | Drugs | Lornoxicam comparable en eficacia analgésica a morfina y petidina; ensayos preliminares confirman eficacia en AR y OA |
| [29026298](https://pubmed.ncbi.nlm.nih.gov/29026298/) | 2017 | Estudio en animales | International Journal of Nanomedicine | Fórmula nanomicelar de lornoxicam muestra mayor eficacia terapéutica que lornoxicam libre en modelos experimentales de AR |
| [32792844](https://pubmed.ncbi.nlm.nih.gov/32792844/) | 2020 | Estudio de formulación | Saudi Pharmaceutical Journal | Microsponge celulósico con lornoxicam para liberación sostenida; diseñado específicamente para manejo del dolor artrítico |
| [23567043](https://pubmed.ncbi.nlm.nih.gov/23567043/) | 2013 | Estudio de formulación | Journal of Controlled Release | Parche transdérmico combinado teriflunomida+lornoxicam para entrega intraarticular en AR; evaluación de permeación y farmacocinética |
| [25553695](https://pubmed.ncbi.nlm.nih.gov/25553695/) | 2015 | Formulación/Cronoterapia | Pakistan J Pharmaceutical Sciences | Mini-tabletas en pulsincap para cronoterapia de AR; apunta a síntomas de exacerbación matutina |
| [24967065](https://pubmed.ncbi.nlm.nih.gov/24967065/) | 2014 | Formulación/Cronoterapia | Iranian Journal of Basic Medical Sciences | Mini-tabletas matriciales de lornoxicam para tratamiento dirigido a síntomas matutinos de AR |

---

## Información de Mercado en Argentina

Lornoxicam **no cuenta con ninguna autorización de comercialización vigente en Argentina** (ANMAT). No se encontraron registros sanitarios activos en la búsqueda realizada el 29 de marzo de 2026. El fármaco sí está disponible en más de 31 países de Europa, Oriente Medio, Lejano Oriente y Sudamérica bajo marcas como Xefo® y Acabel®.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La base farmacológica de lornoxicam para artritis reumatoide es robusta (inhibición COX-1/COX-2 → supresión de PGE₂ sinovial) y está respaldada por estudios clínicos comparativos directos y revisiones internacionales; la evidencia llega a nivel L3. Sin embargo, la ausencia total de registro en Argentina, la falta de datos formales de MOA y seguridad en el Evidence Pack, y la inexistencia de ensayos de Fase 3 en ClinicalTrials.gov para esta indicación específica impiden una decisión de avance pleno.

**Para avanzar se necesita:**
- Completar datos de MOA desde DrugBank API (Data Gap DG002)
- Obtener y analizar el prospecto/ficha técnica del fabricante para advertencias, contraindicaciones e interacciones (Data Gap DG001)
- Realizar búsqueda sistemática en Cochrane y Embase para identificar ECAs de Fase 2/3 publicados que no estén indexados en ClinicalTrials.gov
- Iniciar evaluación de viabilidad regulatoria para registro ante ANMAT (indicación: artritis reumatoide)
- Revisar si los estudios clínicos de largo plazo disponibles (pmid 12207202, 12404032) cumplen los requisitos de evidencia para la presentación regulatoria argentina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

