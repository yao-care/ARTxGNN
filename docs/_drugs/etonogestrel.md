---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: De Anticoncepción Hormonal a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno sintético utilizado como anticonceptivo en implantes subdérmicos de larga duración, suprimiendo la ovulación de forma sostenida.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, con **1 ensayo clínico** y **2 publicaciones** identificadas en relación a esta dirección.
Sin embargo, la amenorrea es un efecto secundario conocido e inducido por el propio etonogestrel, lo que hace que esta predicción sea mecánicamente paradójica y requiera interpretación cuidadosa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin indicación aprobada en Argentina |
| Nueva Indicación Predicha | Amenorrea (amenorrhea disease) |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de etonogestrel en esta base de datos. Según la información conocida, etonogestrel es un progestágeno de tercera generación derivado del 19-nortestosterona. Su efecto principal consiste en suprimir la secreción de LH y FSH a nivel del eje hipotálamo-hipofisario, inhibiendo la ovulación, espesando el moco cervical y produciendo atrofia endometrial. Es el principio activo del implante subdérmico Implanon/Nexplanon, ampliamente utilizado como anticonceptivo de larga duración.

La relación entre etonogestrel y la amenorrea es, sin embargo, **causal inversa**: el fármaco la induce como efecto secundario en un 20–30% de las usuarias, no la trata. La supresión hormonal sostenida provoca atrofia endometrial, lo que resulta en ausencia de menstruación; esto constituye amenorrea secundaria inducida por fármaco, no una enfermedad que el medicamento resuelve.

Esta paradoja mecánica es determinante para la evaluación de reposicionamiento. El modelo TxGNN identificó una fuerte asociación estadística entre etonogestrel y amenorrea en su grafo de conocimiento, pero dicha asociación refleja que el fármaco **causa** la condición, no que tenga potencial para **tratarla**. La predicción es estadísticamente elevada pero clínicamente mal orientada bajo los criterios convencionales de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Completado | 498 | Evaluación de eficacia anticonceptiva extendida (años 4–5) del implante de etonogestrel; la amenorrea se registra como patrón de sangrado secundario y no es el objetivo terapéutico del estudio |

> **Nota de relevancia (Grado C):** Este ensayo no tiene como objetivo el tratamiento de amenorrea. Los datos de amenorrea son observaciones de patrón de sangrado, no endpoints terapéuticos, y no constituyen evidencia de reposicionamiento.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA | Contraception | Estudio multicéntrico aleatorizado que compara el implante de un solo vástago (Implanon, etonogestrel) vs seis cápsulas (Norplant) en 200 mujeres durante 2–4 años; evalúa patrones de sangrado incluyendo amenorrea como resultado secundario, sin objetivos terapéuticos para la condición |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | ECA | Trials | Protocolo de ensayo de BIO101 para prevención de deterioro respiratorio en COVID-19; sin relación con etonogestrel ni con amenorrea — probable falso positivo en la búsqueda automatizada |

---

## Información de Mercado en Argentina

Etonogestrel no cuenta con ninguna autorización de comercialización registrada en Argentina. No existen licencias vigentes ni formas farmacéuticas aprobadas localmente disponibles en esta base de datos (total de autorizaciones: 0).

---

## Consideraciones de Seguridad

Los datos de seguridad específicos (advertencias clave, contraindicaciones e interacciones farmacológicas) no están disponibles en este Evidence Pack. Consultar el prospecto del producto y las guías de prescripción aprobadas internacionalmente (EMA, FDA) para información de seguridad completa antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN refleja una asociación estadística real entre etonogestrel y amenorrea, pero esta asociación representa causalidad directa del fármaco (lo induce como efecto secundario), no potencial terapéutico para tratar la enfermedad. El único ensayo clínico identificado no evalúa amenorrea como objetivo de tratamiento, y una de las dos publicaciones literarias es claramente irrelevante. En ausencia de registro en Argentina y sin datos de seguridad locales disponibles, no existen condiciones para avanzar en este momento.

**Para avanzar se necesita:**
- Revisión conceptual del modelo TxGNN para distinguir asociaciones de tipo "fármaco causa condición" vs. "fármaco trata condición" antes de incorporar esta predicción a un pipeline de reposicionamiento
- Datos completos de mecanismo de acción (MOA) desde DrugBank (DG002)
- Descarga y análisis del prospecto oficial para advertencias y contraindicaciones (DG001)
- Investigación exploratoria sobre si existe algún subtipo específico de amenorrea (p.ej., amenorrea hipotalámica funcional con hiperandrogenismo) donde el perfil progestágeno de etonogestrel pudiera tener un rol terapéutico diferenciado
- Evaluación de viabilidad regulatoria ante la ausencia total de registro en Argentina
---

