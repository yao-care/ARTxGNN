---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

La skill confirma el contexto TxGNN. Procedo a generar el informe completo basado en el Evidence Pack.

---

# PRASUGREL: De Síndrome Coronario Agudo a Hipertensión Pulmonar

## Resumen en Una Frase

Prasugrel es un agente antiplaquetario de la clase tienopiridinas, ampliamente utilizado para la prevención de eventos aterotrombóticos en pacientes con síndrome coronario agudo (SCA) sometidos a intervención coronaria percutánea (ICP). El modelo TxGNN predice que podría ser efectivo para la **Hipertensión Pulmonar**, con **2 ensayos clínicos** y **2 publicaciones** recuperados en la búsqueda, aunque ninguno evalúa directamente prasugrel en esta indicación. La evidencia actual es preliminar e indirecta, sin respaldo clínico directo que sostenga este reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome Coronario Agudo / Prevención aterotrombótica en ICP |
| Nueva Indicación Predicha | Hipertensión Pulmonar |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos local. Según la información conocida, prasugrel es un profármaco tienopiridínico que, tras activación hepática, bloquea de forma irreversible el receptor P2Y12 plaquetario, inhibiendo la activación y agregación plaquetaria inducida por ADP. Su eficacia en la reducción de eventos cardiovasculares mayores (infarto, trombosis del stent) en SCA con ICP ha sido comprobada en ensayos de Fase 3 (p. ej., TRITON-TIMI 38).

En la hipertensión pulmonar (HP), la patogénesis incluye disfunción endotelial, vasoconstricción progresiva, remodelación vascular y formación de microtrombos in situ en la microvasculatura pulmonar. Las plaquetas activadas liberan tromboxano A2 y serotonina, mediadores que promueven la vasoconstricción y la proliferación de células musculares lisas vasculares. Bajo esta lógica, la inhibición del receptor P2Y12 podría teóricamente reducir la carga de microtrombos y la activación plaquetaria en el lecho vascular pulmonar.

Sin embargo, este mecanismo no ha sido validado clínicamente en HP. Las terapias aprobadas para HP actúan sobre las vías prostaciclina/endotelina/fosfodiesterasa-5, mecanísticamente distintas a la inhibición P2Y12. La predicción de TxGNN probablemente refleja una conexión estructural en el grafo de conocimiento (coexistencia de activación plaquetaria y microtrombosis en ambas condiciones) sin que exista una relación terapéutica directamente establecida.

---

## Evidencia de Ensayos Clínicos

> **Nota importante:** Los ensayos recuperados tienen grado de relevancia C y no evalúan directamente prasugrel en hipertensión pulmonar. Se presentan para transparencia del proceso de búsqueda.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completado | 500 | Estudio observacional multicéntrico sobre manejo de NOACs (anticoagulantes orales) en pacientes ancianos con fibrilación auricular no valvular en España. No evalúa prasugrel ni hipertensión pulmonar. |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completado | 300 | Estudio retrospectivo sobre trombosis asociada a cáncer y elegibilidad al ensayo CARAVAGGIO. No evalúa prasugrel ni hipertensión pulmonar. |

---

## Evidencia de Literatura

> **Nota importante:** Las publicaciones recuperadas no evalúan directamente prasugrel en hipertensión pulmonar.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Observacional/Registro | Kardiologiia | Análisis del registro ACTIV SARS-CoV-2 sobre el efecto de la terapia cardiovascular previa en el riesgo de mortalidad por COVID-19. Relevancia indirecta; no evalúa prasugrel en HP. |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte / Farmacoepidemiología | Current Medical Research and Opinion | Factores asociados al uso, adherencia y persistencia de clopidogrel en SCA post-ICP; menciona prasugrel como alternativa en guías clínicas. No evalúa hipertensión pulmonar. |

---

## Información de Mercado en Argentina

Prasugrel no cuenta con ninguna autorización de comercialización registrada en Argentina. No hay datos de productos aprobados disponibles.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existe una conexión mecanística teórica plausible (inhibición de activación plaquetaria y microtrombosis en HP), la evidencia clínica directa es inexistente. Ninguno de los ensayos ni publicaciones recuperados evalúa prasugrel en hipertensión pulmonar. Las vías terapéuticas establecidas para HP son mecanísticamente distintas a la inhibición P2Y12, y prasugrel no está comercializado en Argentina, lo que añade una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Búsqueda dirigida de estudios preclínicos que evalúen inhibidores P2Y12 en modelos experimentales de HP
- Obtención de datos completos de MOA desde DrugBank API (DG002)
- Obtención e interpretación del prospecto internacional para evaluación de seguridad (DG001)
- Evaluación del riesgo de sangrado en la población con HP, especialmente en contextos de anticoagulación concurrente
- Revisión de la indicación de rango 2 (migraña con PFO), que cuenta con literatura más directamente relevante para prasugrel (PMID 30478067, 30478066), como candidata prioritaria alternativa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

