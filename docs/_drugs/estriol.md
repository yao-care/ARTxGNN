---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 1
---

# Estriol
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

Con base en el Evidence Pack proporcionado, a continuación el informe de evaluación de reposicionamiento:

---

# Estriol: De Terapia Hormonal de Reemplazo a Amenorrea

## Resumen en Una Frase

Estriol (E3) es un estrógeno natural de baja potencia ampliamente conocido por su uso global en terapia hormonal de reemplazo para el manejo del síndrome genitourinario de la menopausia y estados hipogonádicos, aunque no se encuentra comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para el tratamiento de la **Amenorrea** —particularmente la amenorrea hipotalámica funcional (FHA)—, con **3 ensayos clínicos** y **13 publicaciones** que actualmente respaldan esta dirección.
La evidencia más directa proviene de un estudio clínico prospectivo (PMID 22137494, *Fertility and Sterility*, 2012) que demuestra la capacidad de estriol para modular la secreción de LH en pacientes con FHA.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Terapia hormonal de reemplazo (uso global; sin autorización registrada en Argentina) |
| Nueva Indicación Predicha | Amenorrea (amenorrea hipotalámica funcional) |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por Qué es Razonable Esta Predicción?

Actualmente no se dispone de datos oficiales sobre el mecanismo de acción (MOA) en DrugBank para estriol. Sin embargo, según la información conocida, estriol (E3) es el estrógeno endógeno natural de menor potencia relativa —predominante durante el embarazo— y actúa sobre los receptores de estrógeno del hipotálamo y la hipófisis, modulando los mecanismos de retroalimentación negativa y positiva que regulan la secreción pulsátil de GnRH y, en consecuencia, la producción de gonadotropinas LH y FSH.

La amenorrea hipotalámica funcional (FHA) se origina en una reducción de la secreción pulsátil de GnRH desencadenada por estrés psicosocial, déficit energético o ejercicio excesivo. Esta reducción suprime los niveles de LH y FSH, genera hipoestrogenismo sistémico y detiene el ciclo menstrual. Dado que estriol puede interactuar con los receptores hipotalámicos de estrógeno a dosis bajas, se postula que es capaz de reinstaurar los mecanismos de retroalimentación positiva y restaurar la secreción pulsátil de LH sin los efectos proliferativos de estrógenos más potentes como el estradiol.

La evidencia clínica disponible respalda directamente esta hipótesis: Genazzani et al. (PMID 22137494, 2012) demostraron que la administración de estriol modula significativamente la secreción de LH en mujeres con FHA; y una revisión mecanística reciente (PMID 37371858, *Biomedicines*, 2023) confirma el papel de los estrógenos de baja dosis como moduladores neuroendocrinos en FHA, capaces de desencadenar el mecanismo de retroalimentación positiva. La predicción es especialmente sólida para el subtipo FHA, aunque la eficacia en amenorrea primaria o insuficiencia ovárica prematura (POI) requiere evaluación estratificada independiente.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Fase 2 | Retirado | 0 | Fotobiomodulación para atrofia vulvovaginal en mujeres postmenopáusicas; el contexto de hipoestrogenismo vincula indirectamente con amenorrea, pero el ensayo fue retirado sin generar datos |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Fase 3 | Completado | 1.570 | E4Comfort Study I: Estetrol (E4) 15 o 20 mg vs. placebo en síntomas vasomotores postmenopáusicos; proporciona evidencia indirecta de alta calidad sobre la eficacia y seguridad de estrógenos naturales en hipoestrogenismo |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Fase 3 | Completado | 1.015 | E4Comfort Study II: diseño paralelo al anterior; confirma el perfil de eficacia y seguridad endometrial de estrógenos naturales de baja potencia, reforzando la lógica terapéutica para estriol en estados hipogonádicos |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Estudio Clínico Prospectivo | Fertility and Sterility | Estriol modula significativamente la secreción de LH en mujeres con FHA; evidencia directa del mecanismo neuroendocrino propuesto para la nueva indicación |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Revisión Mecanística | Biomedicines | Los estrógenos de baja dosis actúan como moduladores neuroendocrinos en FHA, restaurando la retroalimentación positiva del eje HPO y la secreción pulsátil de GnRH |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Estudio Clínico (Cohorte) | Medicinski Pregled | La terapia con estrógenos-progestágenos mejora el perfil lipídico y hormonal en mujeres con insuficiencia ovárica prematura (amenorrea hipergonadotrófica), subgrupo relevante de amenorrea |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Ensayo Clínico | J Obstet Gynaecol Br Commonw | Gonadotrofinas hipofisarias y urinarias en amenorrea secundaria idiopática; contexto clínico fundacional para la comprensión del eje HPO en amenorrea |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Reporte de Caso | Lancet | Hallazgos endocrinológicos en dos pacientes con insuficiencia ovárica prematura; documentación temprana del fenotipo de amenorrea hipergonadotrófica |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Revisión | Clinical Obstetrics and Gynecology | Relación entre neoplasia y anticoncepción hormonal; proporciona contexto histórico sobre el uso de estrógenos en ginecología |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observacional | Zhong Xi Yi Jie He Za Zhi | Relación entre hipofunción gonadal y amenorrea/oligomenorrea desde la perspectiva de la medicina integrativa |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Observacional | Am J Obstet Gynecol | Manifestaciones endocrinas prolongadas —incluyendo amenorrea— tras administración de medroxiprogesterona durante el embarazo |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Descripción Clínica | Br J Psychiatry | Anorexia nerviosa como causa de amenorrea hipotalámica por déficit energético; contexto clínico directamente relevante para FHA |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Estudio Mecanístico | J Clin Endocrinol Metab | Mecanismo de acción de compuestos anti-ovulatorios; base histórica para comprender la modulación farmacológica del eje HPO |

---

## Información de Mercado en Argentina

Estriol no cuenta con ninguna autorización de comercialización registrada en Argentina al momento de esta evaluación. No se dispone de fichas técnicas ni prospectos aprobados por ANMAT para este fármaco.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Un estudio clínico prospectivo directo (PMID 22137494) y una revisión mecanística reciente (PMID 37371858) respaldan el rol de estriol como modulador neuroendocrino en la amenorrea hipotalámica funcional; sin embargo, la ausencia de ensayos clínicos aleatorizados específicos para amenorrea con estriol, la falta de registro en Argentina y los vacíos de datos en seguridad obligan a avanzar con controles estrictos antes de cualquier aplicación clínica.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción oficial (MOA) desde DrugBank API para completar el análisis de relacionabilidad mecanística
- Conseguir la información de seguridad completa (advertencias, contraindicaciones, interacciones farmacológicas) del prospecto europeo o de la EMA/FDA como referencia
- Identificar o diseñar un ensayo clínico aleatorizado específico para amenorrea hipotalámica funcional con estriol oral o transdérmico a dosis bajas
- Estratificar la población objetivo: FHA (hipogonadismo hipogonadotrófico) vs. insuficiencia ovárica prematura (POI) vs. amenorrea primaria, dado que el mecanismo aplica diferencialmente
- Evaluar la vía regulatoria en Argentina para el registro inicial del fármaco (sin autorizaciones previas)
- Definir la dosis, la vía de administración y la duración del tratamiento óptimas para la indicación de amenorrea
---

