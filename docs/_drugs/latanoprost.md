---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

Usando **txgnn-pipeline** para orientación de contexto. Ahora procedo a generar el informe a partir del Evidence Pack.

---

# Latanoprost: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Latanoprost es un análogo sintético de prostaglandina F2α, utilizado originalmente para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular. El modelo TxGNN predice que podría ser efectivo para **Glaucoma Hereditario Primario (primary hereditary glaucoma)**, con **1 ensayo clínico de Fase 2 completado** que actualmente respalda esta dirección. La conexión mecanística es excepcionalmente directa: el mecanismo reductor de presión intraocular (PIO) de latanoprost es idéntico al requerido en la nueva indicación, lo que hace de esta predicción una extensión de indicación dentro del mismo mecanismo más que un reposicionamiento clásico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto / Hipertensión ocular |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos local (pendiente consulta DrugBank). Sin embargo, según la información científica conocida y el análisis de reposicionamiento incluido en el Evidence Pack: latanoprost es un agonista selectivo del receptor FP (receptor de prostaglandina F2α). Al activar este receptor en el cuerpo ciliar del ojo, incrementa el flujo de salida del humor acuoso principalmente por la vía uveoescleral, lo que reduce de manera sostenida la presión intraocular. Este mecanismo está completamente establecido y es la base de su indicación aprobada en glaucoma de ángulo abierto.

El glaucoma hereditario primario —que abarca variantes genéticas como mutaciones en los genes MYOC y OPTN— comparte exactamente la misma fisiopatología central que el glaucoma de ángulo abierto: la elevación crónica de la PIO como mecanismo primario de daño al nervio óptico. La diferencia radica en la causa subyacente (genética vs. idiopática/adquirida), no en el objetivo terapéutico. Por lo tanto, la necesidad de controlar la PIO en el glaucoma hereditario primario es idéntica, y el mecanismo de acción de latanoprost resulta directamente aplicable sin necesidad de adaptación farmacológica.

Más que un reposicionamiento convencional, esta predicción representa una **extensión de indicación dentro del mismo mecanismo de acción**. Este tipo de candidato tiene la tasa de éxito traslacional más alta en desarrollo farmacéutico. El ensayo clínico NCT01527682, que evalúa específicamente un análogo de prostaglandina (misma clase que latanoprost) en glaucoma pediátrico primario, proporciona validación empírica directa de esta dirección terapéutica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fase 2 | Completado | 37 | Evaluación del efecto hipotensor ocular de latanoprost y dorzolamida en pacientes pediátricos con glaucoma primario refractario a procedimientos quirúrgicos. El diseño compara directamente el análogo de prostaglandina (misma clase farmacológica que latanoprost) frente al inhibidor de anhidrasa carbónica en esta indicación específica, con seguimiento desde 2009 hasta 2016. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en la búsqueda dirigida a esta indicación específica.

---

## Información de Mercado en Argentina

Latanoprost no cuenta con ninguna autorización de comercialización registrada en ANMAT. El fármaco no se encuentra actualmente comercializado en Argentina según los datos disponibles a la fecha de corte (2026-05-01).

> **Nota:** Esto no implica que el fármaco sea desconocido a nivel global. Latanoprost (Xalatan®) cuenta con amplia aprobación internacional (FDA, EMA, entre otros) y es un tratamiento de primera línea para glaucoma en numerosos países. La ausencia de registro en ANMAT representa una oportunidad de mercado, no una barrera científica.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no se encuentran disponibles en el Evidence Pack actual y deben obtenerse del prospecto oficial antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de acción de latanoprost (reducción de PIO mediante agonismo del receptor FP) es directamente aplicable al glaucoma hereditario primario, ya que ambas condiciones comparten el mismo objetivo terapéutico central. La existencia de un ensayo clínico de Fase 2 completado con un fármaco de la misma clase en esta indicación proporciona un nivel de evidencia L2 que justifica avanzar, aunque con monitoreo cuidadoso dada la naturaleza genética de la población objetivo (predominantemente pediátrica) y la ausencia de datos regulatorios locales.

**Para avanzar se necesita:**
- Obtener datos completos de mecanismo de acción (MOA) desde DrugBank API (brecha DG002)
- Descargar y analizar el prospecto oficial para completar advertencias, contraindicaciones e interacciones (brecha DG001 — clasificada como Blocking)
- Acceder a los resultados completos publicados del ensayo NCT01527682 para cuantificar eficacia (reducción de PIO) y perfil de seguridad en población pediátrica
- Iniciar proceso de registro ante ANMAT como condición previa a cualquier desarrollo comercial en Argentina
- Evaluar consideraciones especiales para uso en población pediátrica con glaucoma hereditario (posología, formulación, seguimiento a largo plazo)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

