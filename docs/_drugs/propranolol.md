---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Analizando el Evidence Pack de Propranolol. La indicación principal predicha es **distal myopathy, Tateyama type** (rank 1, score 99.40%), con nivel de evidencia L5 y recomendación Hold. Procediendo a generar el informe completo.

---

# Propranolol: De Hipertensión Arterial y Arritmias Cardíacas a Miopatía Distal Tipo Tateyama

## Resumen en Una Frase

Propranolol es un bloqueante beta-adrenérgico no selectivo (β1/β2) con décadas de uso clínico para el tratamiento de hipertensión arterial, arritmias cardíacas, angina de pecho y cardiomiopatía hipertrófica obstructiva.
El modelo TxGNN predice que podría ser efectivo para la **Miopatía Distal Tipo Tateyama**,
sin embargo, **no existe ningún ensayo clínico ni publicación científica** que respalde actualmente esta dirección específica — la evidencia es exclusivamente la predicción computacional del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial, arritmias cardíacas, angina de pecho (beta-bloqueante no selectivo de amplio uso cardiovascular) |
| Nueva Indicación Predicha | Miopatía Distal Tipo Tateyama (*Distal myopathy, Tateyama type*) |
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Propranolol es un bloqueante de los receptores β-adrenérgicos β1 y β2 de amplio espectro. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack de este candidato. Según la información conocida, Propranolol reduce la frecuencia cardíaca, el gasto cardíaco y la presión arterial al antagonizar los efectos de las catecolaminas, con aplicaciones adicionales en portal hypertension, profilaxis de hemorragia variceal y taquiarritmias supraventriculares.

La Miopatía Distal Tipo Tateyama es una enfermedad musculoesquelética de extrema rareza, causada por mutaciones en el gen MYH2 (cadena pesada de miosina IIa), que produce debilidad y atrofia selectiva del músculo esquelético distal. Existe cierta evidencia en literatura general de que el bloqueo β-adrenérgico puede modular parcialmente la atrofia del músculo esquelético mediada por catecolaminas —vía señalización β2-AR/cAMP/PKA sobre la proteólisis muscular—, lo cual podría explicar que el grafo de conocimiento de TxGNN conecte a Propranolol con nodos de miopatía.

Sin embargo, la alta puntuación del modelo para este subtipo específico muy probablemente refleja **generalización topológica del grafo** hacia nodos genéricos de enfermedad muscular, más que una relación mecanística directa con la mutación MYH2. No existe ningún estudio clínico ni preclínico que vincule Propranolol con la Miopatía Distal Tipo Tateyama. Esta predicción debe considerarse como señal exploratoria de nivel L5, sin respaldo empírico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para Miopatía Distal Tipo Tateyama carece completamente de respaldo empírico: cero ensayos clínicos, cero publicaciones, y el vínculo mecanístico con la mutación MYH2 es especulativo. Adicionalmente, Propranolol no está comercializado en Argentina, lo que suma una barrera regulatoria adicional para cualquier exploración clínica local.

**Para avanzar se necesita:**
- **Estudios preclínicos**: evaluar si el bloqueo β-AR modifica el fenotipo muscular en modelos de Miopatía Distal Tipo Tateyama (modelos *in vitro* con células MYH2-mutadas o modelos animales)
- **Revisión mecanística**: literatura sobre el efecto de beta-bloqueantes en enfermedades del músculo esquelético vinculadas a miosina (para descartar o confirmar señal real)
- **Datos de MOA de DrugBank**: completar la información de mecanismo de acción de Propranolol para análisis formal de conectividad mecanística
- **Datos de seguridad (prospecto ANMAT)**: obtener advertencias y contraindicaciones para evaluación de perfil de riesgo antes de cualquier avance
- **Considerar indicaciones con mayor evidencia**: en este mismo Evidence Pack, *cardiomiopatía* (rank 6) cuenta con 3 ensayos clínicos y 20 publicaciones (L3, Proceed with Guardrails), representando una oportunidad de reposicionamiento mucho mejor respaldada para evaluación prioritaria
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

