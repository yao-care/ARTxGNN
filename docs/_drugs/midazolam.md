---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

El skill de txgnn-pipeline cubre gestión de infraestructura del pipeline, no la generación de informes. Procedo directamente con el informe siguiendo el formato del sistema.

---

# Midazolam: De Sedación y Anestesia a Insomnio

## Resumen en Una Frase

Midazolam es un fármaco benzodiazepínico ampliamente utilizado como agente sedante y de preanestesia en procedimientos quirúrgicos e intervenciones médicas, donde actúa sobre los receptores GABA-A para producir depresión del sistema nervioso central.
El modelo TxGNN predice que podría ser efectivo para el tratamiento del **Insomnio**,
con **10 ensayos clínicos** y **7 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Sedación procedimental y anestesia |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No registrado en ANMAT |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Midazolam pertenece a la clase farmacológica de las benzodiazepinas. Su mecanismo de acción consiste en la unión al sitio específico para benzodiazepinas del receptor GABA-A, potenciando la neurotransmisión inhibitoria mediada por GABA. El resultado funcional es una depresión del sistema nervioso central que se traduce en reducción de la latencia de inicio del sueño y aumento del tiempo total de sueño —particularmente en la fase 2 del sueño NREM—, con reducción concomitante del sueño REM.

La relación entre el perfil hipnótico-sedante de midazolam y el insomnio es mecanísticamente directa: el mismo circuito GABAérgico que sustenta su uso en sedación procedimental actúa sobre los sistemas neurobiológicos que regulan el ciclo sueño-vigilia. El insomnio primario se caracteriza por un estado de hiperarousal que la facilitación GABAérgica contrarresta, lo que explica la alta coherencia de la predicción TxGNN (99.74%). De hecho, estudios clínicos publicados desde la década de 1980 documentan el uso de midazolam oral como hipnótico en pacientes con trastornos del sueño.

No obstante, el perfil de midazolam para el tratamiento crónico del insomnio presenta limitaciones importantes: el uso prolongado induce regulación negativa de receptores GABA-A, tolerancia farmacológica e insomnio de rebote al suspender el tratamiento. Por estas razones, las guías clínicas actuales no lo recomiendan como tratamiento de primera línea para el insomnio crónico. La oportunidad de reposicionamiento se orienta más bien hacia indicaciones específicas —insomnio situacional de corto plazo, insomnio perioperatorio o en contextos de alta carga de ansiedad— donde el balance beneficio-riesgo resulta más favorable.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Comparación directa de calidad del sueño postoperatorio entre midazolam y dexmedetomidina en pacientes con TURP bajo anestesia espinal; es la evidencia más directa disponible sobre midazolam y calidad del sueño |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Reclutando | 280 | ECA doble ciego con midazolam oral preoperatorio en pacientes con disturbios del sueño o ansiedad sometidos a resección laparoscópica de cáncer colorrectal; evalúa efecto sobre dolor postoperatorio y calidad del sueño |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Fase 3 | Desconocido | 120 | ECA pediátrico en UCI con ventilación mecánica que compara dexmedetomidina versus midazolam como sedante; calidad del sueño incluida como resultado secundario |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Fase 3 | Aún no reclutando | 195 | Comparación de melatonina versus midazolam oral como premedicación en niños sometidos a amigdalectomía; evalúa inducción del sueño, calidad y perfil de efectos adversos |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminado | 5 | Comparación de calidad y cantidad del sueño mediante polisomnografía de 24 horas entre dexmedetomidina y midazolam en pacientes críticos; terminado prematuramente por baja inscripción |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Terminado | 6 | Efecto de agonistas α2 versus agonistas GABA (incluyendo midazolam) sobre fases del sueño y tiempo total de sueño en pacientes con ventilación mecánica; limitado por muestra reducida |
| [NCT04879771](https://clinicaltrials.gov/study/NCT04879771) | N/A | Desconocido | 100 | Comparación del efecto de sedación con midazolam/propofol en endoscopía gastrointestinal matutina versus vespertina sobre la calidad del sueño postprocedimiento |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Fase 4 | Completado | 100 | Estudio piloto aleatorizado de protocolo de sueño nocturno con dexmedetomidina nocturna en UCI; evalúa viabilidad, delirium y alteraciones del sueño frente a manejo estándar |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Fase 4 | Completado | 90 | Efectos a corto plazo de la sedación con dexmedetomidina sobre sueño e inflamación en pacientes con lesión pulmonar aguda (ALI/ARDS); midazolam como referencia comparativa |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | N/A | Completado | 23 | ECA doble ciego que evalúa la transición de benzodiazepinas a dexmedetomidina versus continuación con midazolam en pacientes de UCI médica/quirúrgica próximos a extubación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | ECA de búsqueda de dosis | Arzneimittel-Forschung | Evaluación de eficacia y seguridad de midazolam oral (10–30 mg) en 75 pacientes hospitalizados con insomnio leve a moderado; establece rango de dosis óptimo para uso hipnótico |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | ECA | British Journal of Clinical Pharmacology | Doble ciego; midazolam 15 mg vs. Vesparax en 30 pacientes con insomnio secundario a enfermedad neuromuscular; midazolam resultó más eficaz y mejor tolerado, sin efecto resaca |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA multicéntrico | Journal of Clinical Psychopharmacology | Resumen ejecutivo del estudio multicéntrico de 14 días con flurazepam y midazolam en insomniacs crónicos; evalúa sueño, rendimiento cognitivo y niveles plasmáticos |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | Ensayo clínico | Journal of Clinical Psychopharmacology | ECA aleatorizado multicéntrico en grupos paralelos que examina sueño, rendimiento y estado de ánimo durante 14 días de uso de flurazepam y midazolam en insomniacs crónicos con antecedente de uso de benzodiazepinas |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatrica Scandinavica | Revisión del uso clínico de hipnóticos benzodiazepínicos incluyendo midazolam; analiza perfil farmacocinético, eficacia diferencial y selección según patrón de insomnio (conciliación vs. mantenimiento) |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Estudio clínico | Journal of Clinical Medicine | Estudio piloto que evalúa lemborexant versus benzodiazepinas para insomnio en pacientes de alto riesgo con patología pancreatobiliar; advierte que benzodiazepinas como midazolam pueden aumentar riesgo de delirium |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Revisión | Orvosi Hetilap | Revisión sobre fisiopatología del insomnio y su relación con hipoperfusión cerebral; contextualiza la clasificación primaria/secundaria del insomnio y el estado de hiperarousal como diana terapéutica |

---

## Información de Mercado en Argentina

Midazolam actualmente **no se encuentra registrado en ANMAT** y no tiene autorizaciones de comercialización vigentes en Argentina (0 licencias). No se dispone de fichas técnicas locales ni textos de indicaciones aprobadas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo GABAérgico de midazolam es directamente relevante para el insomnio y existe evidencia clínica histórica sólida de uso hipnótico (cuatro estudios Tier 1 de los años 80–90), con un ensayo en curso que evalúa midazolam oral específicamente en pacientes con disturbios del sueño. Sin embargo, la ausencia de registro en Argentina, el perfil de tolerancia/dependencia con uso crónico, y los datos de seguridad incompletos obligan a avanzar con cautela.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (ANMAT/TFDA) para completar la evaluación de advertencias, contraindicaciones e interacciones farmacológicas
- Definir el nicho clínico específico (insomnio agudo/situacional, perioperatorio) donde el perfil beneficio-riesgo es más favorable frente a alternativas modernas (antagonistas de orexina, z-drugs)
- Evaluar la viabilidad de un proceso de registro en ANMAT dada la situación actual de no comercialización
- Confirmar la vía y formulación de administración adecuada para la indicación de insomnio (formulación oral vs. parenteral)
- Diseñar un plan de monitoreo de seguridad que contemple riesgo de dependencia, tolerancia e insomnio de rebote en la población objetivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

