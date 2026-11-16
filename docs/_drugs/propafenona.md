---
layout: default
title: Propafenona
parent: Solo Predicción del Modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 6
drugbank_id: DB01182
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
last_modified_at: 2026-11-16
description: "Propafenona: nueva indicación predicha, trastorno afectivo bipolar maníaco (manic bipolar affective disorder) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Propafenona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Propafenona: trastorno afectivo bipolar maníaco (manic bipolar affective disorder)
{: .text-alpha }

## Resumen en Una Frase

Propafenona es un antiarrítmico comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **trastorno afectivo bipolar maníaco (manic bipolar affective disorder)**, pero no hay ensayos clínicos ni estudios que respalden un beneficio terapéutico: la literatura disponible (3 publicaciones) describe casos de manía **provocada** por propafenona y una interacción farmacológica con psicosis, es decir, una señal de efecto adverso y no de tratamiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno afectivo bipolar maníaco (manic bipolar affective disorder) |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general, propafenona es un antiarrítmico de clase IC que bloquea canales de sodio cardíacos.

Para la manía no se identifica un mecanismo terapéutico plausible. Los datos compilados indican lo contrario: un reporte de caso de 1985 describe manía secundaria a propafenona, y se plantea que, por su parecido químico con bupropión, podría tener actividad afectiva. Otro reporte describe una psicosis orgánica por interacción con venlafaxina en un paciente con trastorno bipolar.

Por lo tanto, el puntaje alto probablemente sea un artefacto del modelo y no debe interpretarse como una predicción terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Reporte de caso | J Clin Psychiatry | Caso de manía secundaria a propafenona; posible complicación afectiva no reconocida previamente |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Reporte de caso | Int J Psychiatry Med | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar |
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacol Rep | Interacciones adversas entre antipsicóticos y fármacos cardiovasculares en pacientes con comorbilidad |

Ninguno de estos estudios evalúa a propafenona como tratamiento de la manía; por ello el nivel de evidencia se fija en L5.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 7781 | NORMORYTMIN | 150 mg comp. rec. x 50 | — |
| 7783 | NORMORYTMIN | 300 mg comp. rec. x 50 | — |
| 4652 | NORMORYTMIN | 150 mg comp. rec. x 20 | — |
| 4653 | NORMORYTMIN | 300 mg comp. rec. x 20 | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal relevante para esta predicción, la literatura compilada describe manía inducida por propafenona y psicosis por interacción con venlafaxina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni estudios que respalden un efecto terapéutico en la manía; la evidencia disponible apunta a un efecto adverso neuropsiquiátrico. El puntaje alto del modelo no compensa la ausencia de plausibilidad mecanística.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del prospecto (advertencias y contraindicaciones)
- Un fundamento mecanístico que justifique un beneficio, y no un daño, en la manía
- Estudios preclínicos o clínicos que evalúen directamente esta indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

