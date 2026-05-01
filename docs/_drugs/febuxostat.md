---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Usando **txgnn-pipeline** para guiar la generación del informe de reposicionamiento farmacológico con formato estándar.

---

# Febuxostat: De Hiperuricemia Gotosa a Hipouricemia Renal

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo y no purínico de la xantina oxidorreductasa (XOR), utilizado globalmente para el tratamiento de la hiperuricemia crónica en pacientes con gota, aunque no se encuentra actualmente registrado en Argentina.
El modelo TxGNN predice que podría ser efectivo para la **Hipouricemia Renal**, una condición en la que la excreción excesiva de urato por el riñón genera estrés oxidativo local y lesión renal aguda inducida por ejercicio (EIAKI).
Esta predicción cuenta con **1 ensayo clínico** y **2 publicaciones** científicas que aportan sustento mecanístico y clínico a esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia crónica en pacientes con gota (indicación global reconocida; sin registro en Argentina) |
| Nueva Indicación Predicha | Hipouricemia Renal (*hypouricemia, renal*) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No Comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales del mecanismo de acción desde la fuente DrugBank en este paquete de evidencia. Sin embargo, según la información disponible en el análisis de reposicionamiento, Febuxostat es un inhibidor selectivo no purínico de la xantina oxidorreductasa (XOR), una enzima clave en la síntesis final de ácido úrico. Su eficacia para reducir la producción de urato ha sido comprobada ampliamente en el tratamiento de la hiperuricemia gotosa en múltiples mercados internacionales (EE.UU., UE, Japón).

La hipouricemia renal (RHUC) representa una situación fisiopatológica aparentemente opuesta: los transportadores renales de urato (principalmente URAT1/SLC22A12) pierden función, causando excreción masiva de urato por vía renal y niveles séricos muy bajos. Sin embargo, esta alta carga de urato a nivel tubular activa la XOR localmente, elevando el estrés oxidativo en el epitelio renal y predisponiendo a lesión renal aguda inducida por ejercicio (EIAKI). En este contexto, Febuxostat actuaría **aguas arriba** en la vía metabólica: al reducir la producción total de urato mediante inhibición de XOR, disminuye la carga de urato que llega al túbulo renal y, por ende, el estrés oxidativo local, sin necesidad de elevar el urato sérico.

La publicación PMID 36754409 (*Internal Medicine*, 2023) discute explícitamente el uso de inhibidores XOR no purínicos —como Febuxostat— para la prevención de EIAKI en un paciente pediátrico con RHUC familiar por mutaciones en URAT1, aportando sustento mecanístico directo a la predicción del modelo TxGNN. Este reposicionamiento es biológicamente plausible, aunque la evidencia clínica prospectiva aún es escasa y requiere validación formal.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado para explorar el efecto del control del ácido úrico sobre la recurrencia de cálculos y la función renal en pacientes con nefrolitiasis asociada a hiperuricemia; la inclusión de pacientes con alteraciones del manejo renal de urato aporta relevancia indirecta a la hipouricemia renal. Estado de seguimiento no confirmado. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Hipótesis / Opinión experta | *Internal Medicine* (Tokyo) | Reporta uso de Febuxostat como profilaxis de EIAKI en un futbolista de 16 años con RHUC familiar (mutaciones compuestas en URAT1); discute el mecanismo por el cual los inhibidores XOR no purínicos reducen el estrés oxidativo renal local, con referencia directa a Febuxostat como agente candidato |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión narrativa | *Clinical Rheumatology* | Revisión actualizada sobre hipouricemia para el reumatólogo clínico; cubre definición, etiologías (incluida RHUC), consecuencias clínicas y estrategias de manejo; contextualiza el rol de la modulación del metabolismo del urato en esta condición |

---

## Información de Mercado en Argentina

Febuxostat **no cuenta con ninguna autorización de comercialización registrada en Argentina** a la fecha de corte de datos (2026-05-01). El fármaco no está disponible en el mercado local bajo ninguna forma farmacéutica.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de inhibición XOR de Febuxostat es biológicamente coherente con la reducción del estrés oxidativo renal en la hipouricemia renal, y existe evidencia publicada que respalda específicamente este uso en pacientes con RHUC; sin embargo, la base de evidencia clínica prospectiva es aún limitada (1 ensayo con estado desconocido, sin datos de resultados publicados, y publicaciones de nivel 3), y el fármaco carece de registro en Argentina.

**Para avanzar se necesita:**
- Completar los datos formales de mecanismo de acción (MOA) y advertencias de seguridad desde DrugBank y el prospecto de mercados aprobados (EE.UU./UE/Japón)
- Verificar si el ensayo NCT04398251 concluyó y obtener sus resultados primarios
- Diseñar un estudio piloto prospectivo específico para RHUC con endpoints de función renal (incidencia de EIAKI, creatinina sérica, TFGe)
- Evaluar la viabilidad regulatoria de solicitar registro en Argentina bajo la categoría de enfermedad rara/indicación huérfana
- Consultar con nefrólogos y especialistas en metabolismo del urato para validación clínica independiente del racional mecanístico
---

