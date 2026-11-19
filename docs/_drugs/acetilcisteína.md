---
layout: default
title: Acetilcisteína
parent: Evidencia Alta (L1-L2)
nav_order: 14
evidence_level: L2
indication_count: 10
drugbank_id: DB06151
monitor_inn: "Acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "laryngotracheitis", "angle-closure glaucoma"]
last_modified_at: 2026-11-16
description: "Acetilcisteína: nueva indicación predicha, Enfermedad trombótica (thrombotic disease) (nivel de evidencia L2). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Acetilcisteína
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

## Acetilcisteína: Enfermedad trombótica (thrombotic disease)
{: .text-alpha }

## Resumen en Una Frase

La acetilcisteína es un agente mucolítico y antioxidante con grupos tiol que está comercializado en Argentina. El modelo TxGNN predice que podría ser útil para la **enfermedad trombótica (thrombotic disease)**. La respaldan **7 ensayos clínicos** registrados y **20 publicaciones** recuperadas, pero la evidencia se concentra en subtipos concretos (púrpura trombocitopénica trombótica y microangiopatía trombótica asociada a trasplante) y no en la trombosis en general.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad trombótica (thrombotic disease) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Aun así, la acetilcisteína es un compuesto con grupos tiol capaz de reducir puentes disulfuro. Esto es relevante para el factor de von Willebrand (VWF), cuyos multímeros ultralargos se unen a las plaquetas y favorecen la formación de trombos. Al reducir esos puentes, el fármaco disminuye el tamaño de los multímeros y su capacidad de unirse a las plaquetas.

Además, repone glutatión y reduce el estrés oxidativo y la activación endotelial, factores asociados a un fenotipo protrombótico. Estos mecanismos se relacionan con las microangiopatías trombóticas, como la púrpura trombocitopénica trombótica (PTT) y la microangiopatía trombótica asociada a trasplante (TA-TMA). Los modelos preclínicos en ratón y babuino con PTT respaldan esta lógica.

Conviene tener presente que "enfermedad trombótica" es una categoría amplia. Los estudios disponibles se concentran en PTT, TA-TMA y trombocitopenia inmune, y no hay datos que demuestren beneficio en otras enfermedades trombóticas, como la trombosis venosa o arterial.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fase 3 | Completado | 170 | Seguridad y eficacia de la acetilcisteína en microangiopatía trombótica asociada a trasplante de progenitores hematopoyéticos. Directamente relevante; los resultados deben confirmarse en publicaciones. |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fase 2/3 | Activo, sin reclutar | 44 | Ensayo multicéntrico de brazo único con acetilcisteína en TA-TMA. Directamente relevante; aún sin resultados. |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fase 2 | Completado | 40 | RENACTIF: ensayo cruzado, doble ciego y controlado con placebo para reducir el fenotipo trombótico en insuficiencia renal. Evalúa un fenotipo biomarcador, no una enfermedad trombótica definida. |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Fase 1 temprana | Completado | 3 | Estudio piloto con acetilcisteína intravenosa en sospecha de PTT durante recambio plasmático. Muestra demasiado pequeña para inferir. |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fase 2 | Desconocido | 44 | Acetilcisteína más dexametasona en dosis altas en trombocitopenia inmune recién diagnosticada. Trastorno de plaquetas, no trombótico; la combinación impide atribuir el efecto. |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fase 1/2 | Desconocido | 200 | Atorvastatina, acetilcisteína y danazol en trombocitopenia inmune resistente o recidivante. Indirecto y con diseño combinado. |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Fase 1 temprana | Completado | 15 | Atorvastatina más acetilcisteína sobre el recuento plaquetario en trombocitopenia inmune. Indirecto y de muestra pequeña. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37171598](https://pubmed.ncbi.nlm.nih.gov/37171598/) | 2023 | Serie de casos | Annals of Hematology | Doce pacientes con PTT adquirida tratados con acetilcisteína en dosis altas (150 mg/kg/día) junto con recambio plasmático y esteroides. |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohorte retrospectiva | Annals of Hematology | Evalúa la asociación entre acetilcisteína y mortalidad hospitalaria en PTT adquirida; su uso sigue siendo controvertido. |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclínico | Blood | Acetilcisteína en modelos de PTT en ratón y babuino; respalda el mecanismo sobre el VWF. |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisión | Blood | Revisión de la PTT, microangiopatía trombótica ligada a la deficiencia de ADAMTS13. |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | Journal of Clinical Medicine | Fisiopatología, diagnóstico y manejo de la PTT. |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Revisión | Transfusion Clinique et Biologique | Manejo de la PTT, con recambio plasmático y rituximab como pilares. |
| [26637782](https://pubmed.ncbi.nlm.nih.gov/26637782/) | 2015 | Revisión | Hematology (ASH Education Program) | Tratamientos de la PTT más allá del recambio plasmático. |
| [30871975](https://pubmed.ncbi.nlm.nih.gov/30871975/) | 2019 | Estudio de mecanismo | Biology of Blood and Marrow Transplantation | Hemo-oxigenasa-1 y activación del complemento en la TA-TMA. |
| [35084258](https://pubmed.ncbi.nlm.nih.gov/35084258/) | 2022 | Cohorte retrospectiva | Science Progress | Acetilcisteína oral en dosis altas en pacientes hospitalizados con COVID-19, un contexto con estado protrombótico. Indirecto. |

Las demás publicaciones recuperadas son revisiones sobre COVID-19 o estudios básicos sin relación directa con el beneficio clínico en enfermedad trombótica.

## Información de Mercado en Argentina

El texto de indicación aprobada no figura en los datos locales. Se listan 5 de las autorizaciones vigentes; hay al menos 20 y el listado puede ser parcial.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 44931 | BRONCOLIUM | 600 mg, comprimidos efervescentes x 12 | Temis-Lostal |
| 21647 | ACEMUK | 600 mg, tabletas efervescentes x 20 | Siegfried |
| 52064 | DOSOMUK | 600 mg, comprimidos dispersables x 10 | Beta |
| 54594 | ACETILCISTEINA TEVA | 600 mg, comprimidos efervescentes x 10 | Teva Argentina |
| 42683 | ACC EXPECTORANTE | 600 mg, comprimidos efervescentes x 10 | Novartis-Sandoz |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado y otro de Fase 2/3 en curso en microangiopatía trombótica asociada a trasplante. También hay series de casos y cohortes en PTT, junto con un mecanismo plausible respaldado por modelos preclínicos. Sin embargo, los resultados de los ensayos no están confirmados y la evidencia se limita a subtipos, no a la enfermedad trombótica en general.

**Para avanzar se necesita:**
- Confirmar los resultados publicados del ensayo NCT03252925 y esperar los del NCT07279610.
- Delimitar los subtipos de enfermedad trombótica (PTT, TA-TMA) donde el beneficio sea plausible, en lugar de asumir un efecto general.
- Obtener datos formales de mecanismo de acción.
- Revisar advertencias, contraindicaciones e interacciones en los prospectos aprobados por ANMAT, porque no hay datos de seguridad disponibles.
- Definir una dosis y una vía de administración adecuadas, ya que los estudios de PTT usaron dosis altas por vía intravenosa, distintas de las presentaciones orales comercializadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

