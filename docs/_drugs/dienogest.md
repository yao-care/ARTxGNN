---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Dienogest
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

El skill de TxGNN Pipeline no aporta instrucciones adicionales para este tipo de tarea. Procedo directamente a generar el informe según las especificaciones del sistema.

---

# Dienogest: De Endometriosis a Amenorrea

## Resumen en Una Frase

Dienogest es una progestina de cuarta generación reconocida internacionalmente por el tratamiento de la endometriosis, cuyo mecanismo central consiste en inducir un estado de amenorrea y un entorno hipoestrógénico que suprime el tejido endometrial ectópico.
El modelo TxGNN predice una asociación altamente significativa con **Amenorrea**, con un puntaje de confianza del 99.71% y respaldo de **4 ensayos clínicos** y **4 publicaciones científicas** que documentan este vínculo.
La predicción captura una relación bidireccional: la amenorrea es simultáneamente el mecanismo farmacológico y el resultado terapéutico buscado con dienogest en condiciones ginecológicas estrógeno-dependientes.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicacion Original | Endometriosis (indicación internacional; sin registro en ANMAT) |
| Nueva Indicacion Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 99.71% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información clínica conocida, dienogest es una progestina de cuarta generación con alta selectividad por el receptor de progesterona y actividad androgénica mínima. Su eficacia en el tratamiento de la endometriosis ha sido extensamente documentada en estudios multicéntricos internacionales, y opera fundamentalmente suprimiendo el ciclo ovárico y generando un estado de amenorrea e hipoestrogenismo que inhibe el crecimiento del tejido endometrial ectópico.

La conexión entre endometriosis y amenorrea es de naturaleza mecanística directa: la inducción de amenorrea terapéutica no es un efecto colateral accidental del dienogest, sino su objetivo farmacológico central. Múltiples publicaciones científicas (PMID 41329046, PMID 34405378) describen explícitamente que el tratamiento hormonal de la endometriosis busca "inducir amenorrea y un entorno hipoestrógénico". La predicción del modelo TxGNN refleja con precisión esta relación farmacológica consolidada en la literatura.

La extensión clínica de esta predicción apuntaría al uso de dienogest en otras condiciones ginecológicas donde la supresión menstrual terapéutica es deseable más allá de la endometriosis, como la adenomiosis, la dismenorrea severa o el sangrado uterino anormal. Sin embargo, esta aplicación ampliada requiere validación clínica específica y un perfil de seguridad formalmente establecido en el contexto regulatorio argentino.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completado | 968 | Estudio observacional de Visanne® (dienogest) en práctica clínica real para endometriosis; evalúa efectividad a largo plazo incluyendo patrones de sangrado y tasas de amenorrea |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completado | 895 | Cohorte prospectiva en mujeres asiáticas con endometriosis; documenta calidad de vida y cambios en el ciclo menstrual (incluyendo amenorrea) durante tratamiento con dienogest |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Activo (sin reclutamiento) | 138 | Compara dienogest + estradiol transdérmico vs drospirenona en endometriosis; evalúa tolerabilidad y satisfacción con el régimen de supresión menstrual |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Reclutando | 290 | Estudio de no inferioridad: Indinol Forto® 200 mg vs Visanne® (dienogest 2 mg) en tratamiento de endometriosis |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Revisión | Eur J Contracept Reprod Health Care | Documenta el alto índice de inhibición y transformación del dienogest 2 mg; establece que el objetivo del tratamiento es inducir amenorrea y entorno hipoestrógénico para endometriosis |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revisión | Rev Endocrine Metab Disord | Describe los mecanismos endocrinos del tratamiento hormonal de endometriosis; posiciona la supresión estrogénica y la amenorrea terapéutica como objetivos centrales de los progestágenos |
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Revisión sistemática | BMC Pharmacol Toxicol | Revisión sistemática con análisis bayesiano de efectos adversos de dienogest; documenta prevalencia de amenorrea durante el tratamiento de endometriosis y adenomiosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Cohorte retrospectiva | Reprod Sci | Evalúa eficacia y seguridad de dienogest a largo plazo (>12 meses) en 514 mujeres con endometrioma ovárico; documenta tasas de amenorrea, reducción del dolor y tasas de recurrencia |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone actualmente de datos de advertencias, contraindicaciones ni interacciones farmacológicas en el repositorio consultado para Argentina.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificación:**
Aunque el vínculo mecanístico entre dienogest y amenorrea es científicamente sólido y la predicción TxGNN presenta alta confianza (99.71%), el fármaco carece de registro en Argentina (ANMAT), y los datos de seguridad —advertencias, contraindicaciones e interacciones— están completamente ausentes en el repositorio local, lo que impide completar la evaluación mínima de seguridad requerida para avanzar.

**Para avanzar se necesita:**
- Iniciar el proceso de registro ante ANMAT o identificar una especialidad medicinal equivalente ya aprobada en Argentina
- Obtener y revisar el prospecto completo de Visanne® (Bayer) u otro producto registrado internacionalmente, con foco en advertencias y contraindicaciones
- Definir la indicación específica dentro del espectro "amenorrea terapéutica" que se desea estudiar (ej. adenomiosis, dismenorrea severa, supresión menstrual en contextos específicos)
- Completar el análisis de interacciones farmacológicas (DDI)
- Diseñar un protocolo clínico que diferencie el uso de dienogest para amenorrea terapéutica más allá de la endometriosis
---

