---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Trazodone
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

El skill confirma que este es un flujo TxGNN estándar. La tarea actual es generación de informe — procedo directamente con el formato definido en el sistema.

---

# Trazodone: De Depresión Mayor a Trastorno Obsesivo-Compulsivo

## Resumen en Una Frase

Trazodone es un antidepresivo atípico aprobado mundialmente para el tratamiento de la **Depresión Mayor**, con un perfil serotonérgico único que combina antagonismo 5-HT2A e inhibición de la recaptación de serotonina.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Obsesivo-Compulsivo (TOC)**,
con **0 ensayos clínicos registrados** y **20 publicaciones científicas** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Depresión Mayor (aprobación FDA/EMA global; sin registros locales en Argentina) |
| Nueva Indicación Predicha | Trastorno Obsesivo-Compulsivo (TOC) |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta versión del Evidence Pack. Sin embargo, la literatura científica recopilada confirma que trazodone actúa sobre el sistema serotonérgico mediante al menos dos vías: antagonismo del receptor postsináptico 5-HT2A e inhibición de la recaptación de serotonina (SERT), además de propiedades antihistaminérgicas y alfa-1 adrenérgicas. Este perfil lo distingue de los SSRI convencionales y le otorga un mecanismo complementario dentro de la farmacología serotonérgica.

La conexión con el TOC es mecanísticamente sólida. El TOC está asociado a una hiperactividad del circuito córtico-estriado-tálamo-cortical (CSTC) modulada por disfunción serotonérgica. Todos los tratamientos de primera línea aprobados para el TOC —clomipramina, fluoxetina, fluvoxamina, paroxetina, sertralina— actúan precisamente sobre el sistema 5-HT. Trazodone ofrece una vía complementaria a través de la regulación descendente del receptor 5-HT2A, lo que en teoría reduce la excitabilidad del circuito CSTC y puede atenuar la expresión de síntomas obsesivo-compulsivos. Esta hipótesis está respaldada por estudios de PET que mostraron correlaciones directas entre la respuesta clínica a trazodone y cambios en el metabolismo de glucosa en los núcleos caudados.

La evidencia clínica más relevante es un ensayo doble ciego controlado con placebo (Pigott et al., 1992) que investigó específicamente la eficacia antiobsesiva de trazodone, así como un ensayo abierto en pacientes resistentes a clomipramina (Hermesh et al., 1990) que documentó tres respondedores verificados mediante retirada y reintroducción del fármaco. Aunque la eficacia clínica es modesta y no supera a los SSRI de referencia, el perfil de tolerabilidad favorable de trazodone y su utilidad en pacientes con comorbilidad insomnio-TOC o TOC-depresión bipolar representan nichos clínicos de valor.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados (búsqueda en ClinicalTrials.gov e ICTRP, corte 2026-04-20).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | ECA Doble ciego | J Clin Psychopharmacol | Primer ECA controlado con placebo de trazodone en TOC; investigó la eficacia antiobsesiva aprovechando sus propiedades inhibidoras de recaptación de 5-HT, tras informes previos favorables en estudios abiertos |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Ensayo abierto | Clin Neuropharmacol | Trazodone en 9 pacientes con TOC resistentes a clomipramina ± litio; 3 respondedores verificados con reaparición de síntomas al retirar el fármaco y remisión al reintroducirlo |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Estudio neuroimagen (PET) | Psychopathology | Correlación entre respuesta clínica a trazodone y reducción del metabolismo de glucosa (18F-FDG PET) en núcleos caudados; evidencia de sustrato neurobiológico para el efecto antiobsesivo |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Revisión | J Clin Psychiatry | Revisión de estrategias biológicas para TOC resistente al tratamiento; evalúa combinación de IRS con otros agentes serotonérgicos incluyendo trazodone |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Revisión | Psychopharmacol Bull | Monoterapia y politerapia en TOC; establece el rol exclusivo de los IRS y el rol central de la 5-HT en la patogénesis, contextualizando el uso de trazodone |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Revisión | South Med J | Manejo farmacológico del TOC; discute el papel de la serotonina y dopamina en la fisiopatología y los avances con agentes serotonérgicos incluyendo trazodone |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Revisión narrativa | Postgrad Med | Revisión integral del uso de trazodone en indicaciones aprobadas y off-label (TOC, insomnio, TEPT, ansiedad generalizada); describe mecanismo de acción, dosis y efectos adversos |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Revisión | Curr Pharm Design | Evidencia, beneficios y riesgos del uso off-label de trazodone; incluye TOC, trastorno de pánico, dependencia a benzodiacepinas, fibromialgia y deterioro cognitivo |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Serie de casos | J Nerv Ment Dis | Dos pacientes con TOC grave y depresión superpuesta que habían fracasado con múltiples antidepresivos; ambos obtuvieron mejoría rápida e impresionante tanto en depresión como en síntomas obsesivo-compulsivos con trazodone |
| [29343875](https://pubmed.ncbi.nlm.nih.gov/29343875/) | 2017 | Reporte de caso | Riv Psichiatria | Trazodone de liberación prolongada en comorbilidad Trastorno Bipolar II + TOC (aprox. 21% de pacientes bipolares tienen TOC concomitante); manejo eficaz de síntomas depresivos y obsesivos sin desestabilizar el humor |

---

## Información de Mercado en Argentina

Trazodone no cuenta con autorizaciones de comercialización registradas en Argentina a la fecha de corte de datos (2026-05-05). No se identificaron licencias en la base ANMAT.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo clínico doble ciego controlado con placebo, estudios abiertos con verificación por retirada/reintroducción, y evidencia de neuroimagen (PET) que en conjunto conforman un nivel de evidencia L2 para el uso de trazodone en TOC. El mecanismo serotonérgico es farmacológicamente coherente con los tratamientos estándar del TOC, y los nichos clínicos identificados (TOC resistente a SSRI, comorbilidad con insomnio o trastorno bipolar) ofrecen una justificación clínica diferenciada. La ausencia de registro local en Argentina y la falta de datos de seguridad locales requieren cautela en la implementación.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (MOA) desde DrugBank (DG002 pendiente)
- Obtener y analizar las advertencias, contraindicaciones y perfil de seguridad completo del prospecto (DG001 pendiente — Blocking)
- Evaluar la viabilidad de registro en Argentina ante ANMAT para esta indicación off-label
- Diseñar un protocolo de estudio comparativo frente a SSRI de primera línea (fluoxetina/fluvoxamina) para definir el perfil de paciente que podría beneficiarse preferentemente de trazodone (ej. resistentes a SSRI, con insomnio concomitante o contraindicación a tricíclicos)
- Verificar interacciones farmacológicas relevantes una vez disponibles los datos de DDI
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

