---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

Usando el skill `txgnn-pipeline` para contexto del pipeline TxGNN. El skill confirma el flujo de trabajo estándar; procedo ahora a generar el informe de evaluación de reposicionamiento para GEMFIBROZIL basado en el Evidence Pack proporcionado, enfocado en la indicación de mayor rango: **artritis reumatoide**.

---

# GEMFIBROZIL: De Hiperlipidemia a Artritis Reumatoide

## Resumen en Una Frase

Gemfibrozil es un fármaco de la clase de los fibratos, utilizado históricamente para el tratamiento de la hiperlipidemia y la hipertrigliceridemia mediante la activación del receptor PPARα, reduciendo triglicéridos y elevando el HDL-colesterol. El modelo TxGNN predice que podría ser efectivo para la **artritis reumatoide**, con **0 ensayos clínicos** y **4 publicaciones** que actualmente respaldan esta dirección. La evidencia se basa principalmente en modelos animales y estudios de clase farmacológica, situando esta predicción en una etapa de investigación exploratoria.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hiperlipidemia / Hipertrigliceridemia |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los sistemas locales consultados. Sin embargo, según la literatura disponible en este Evidence Pack, gemfibrozil actúa como agonista del receptor PPARα (Peroxisome Proliferator-Activated Receptor alpha). La activación de PPARα inhibe la vía de señalización NF-κB, lo que reduce la producción de citocinas proinflamatorias como IL-1β y TNF-α, ambas mediadores centrales de la destrucción articular y la inflamación sistémica en la artritis reumatoide.

La conexión mecanística va más allá del efecto hipolipemiante clásico: el eje PPARα también modula la proporción de células T reguladoras Foxp3⁺ (Treg), cuya función está comprometida en la artritis reumatoide activa. El estudio PMID 30074417 reportó directamente que la combinación de gemfibrozil con dosis reducidas de prednisolona produjo un manejo similar al esquema de corticoide a dosis plena en un modelo de artritis inducida por adyuvante en rata, lo que representa evidencia preclínica directa sobre el fármaco.

El estudio PMID 41207105 complementa esta hipótesis al demostrar que bezafibrate (otro fibrato pan-PPAR) atenúa la artritis reumatoide experimental a través de vías dependientes de PPARγ, sustentando un posible efecto de clase farmacológica para los fibratos en la inflamación articular. La extrapolación de modelos animales a uso clínico en humanos requiere validación, pero la plausibilidad biológica es coherente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para gemfibrozil en artritis reumatoide.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Experimental/Clínico | Modern Rheumatology | Gemfibrozil + prednisolona a dosis reducida logró control similar a dosis completa de esteroide en modelo de artritis inducida por adyuvante (rata); evidencia directa sobre gemfibrozil |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Animal/Experimental | International Immunopharmacology | Bezafibrate (pan-PPAR) atenúa la AR experimental mediante modulación PPARγ-dependiente de vías inflamatorias; apoya efecto de clase de los fibratos en AR |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Ciencia Básica | Journal of Immunology | La activación de PPARα regula la expresión de Foxp3 en células T reguladoras mediante óxido nítrico; mecanismo relevante para enfermedades autoinmunes como la AR |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revisión Clínica | American Journal of Clinical Dermatology | Eritema palmar como marcador de estados patológicos sistémicos incluyendo artritis reumatoide; contexto clínico de la enfermedad diana |

---

## Información de Mercado en Argentina

Gemfibrozil **no se encuentra comercializado en Argentina** según los datos regulatorios disponibles. No existen autorizaciones de comercialización registradas (total: 0 licencias). Cualquier uso clínico futuro requeriría gestión de registro ante ANMAT.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN posee plausibilidad biológica sustentada en el mecanismo PPARα/NF-κB antiinflamatorio, respaldada por estudios preclínicos directos sobre gemfibrozil (PMID 30074417) y por efecto de clase demostrado con otros fibratos en modelos de AR (PMID 41207105); sin embargo, la ausencia total de ensayos clínicos en artritis reumatoide, la falta de datos de seguridad locales y el estatus de no comercializado en Argentina impiden avanzar a etapas de desarrollo clínico sin trabajo preparatorio adicional.

**Para avanzar se necesita:**
- Diseño de ensayos clínicos Fase 1/2 que evalúen gemfibrozil en artritis reumatoide en pacientes humanos
- Obtención de datos completos de mecanismo de acción (MOA) desde DrugBank API
- Acceso a la ficha técnica/prospecto para completar advertencias, contraindicaciones e interacciones farmacológicas relevantes
- Evaluación comparativa con otros fibratos (bezafibrate, fenofibrate) para determinar si el efecto antiartrítico es específico de gemfibrozil o un efecto de clase
- Inicio de gestiones regulatorias ante ANMAT para evaluar viabilidad de comercialización en Argentina
---

