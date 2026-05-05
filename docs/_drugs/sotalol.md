---
layout: default
title: Sotalol
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

La habilidad `txgnn-pipeline` no modifica las instrucciones del sistema prompt para la generación del informe. Procedo a generar el informe de evaluación de reposicionamiento para Sotalol según el Evidence Pack proporcionado.

---

# Sotalol: De Arritmias Cardiacas a Sick Sinus Syndrome 2, Autosómica Dominante

## Resumen en Una Frase

Sotalol es un antiarrítmico de clase II/III (bloqueador beta con acción adicional sobre canales de potasio IKr) utilizado clásicamente para el tratamiento de arritmias ventriculares y el control del ritmo en fibrilación auricular. El modelo TxGNN predice que podría ser efectivo para el **Síndrome del Nodo Sinusal Enfermo tipo 2, Autosómico Dominante (SSS2)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación, y la racionalidad mecanística es altamente cuestionable dado que el efecto bloqueador beta de Sotalol representa una contraindicación relativa para este cuadro.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin indicación aprobada registrada en Argentina (fármaco no comercializado) |
| Nueva Indicación Predicha | Sick sinus syndrome 2, autosómica dominante |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por Qué es Razonable Esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Sotalol en la fuente consultada. Según la información conocida, Sotalol es un antiarrítmico dual: ejerce bloqueo beta-adrenérgico no selectivo (clase II) que reduce la frecuencia cardíaca y la conducción en el nodo AV, y simultáneamente inhibe la corriente rectificadora de potasio IKr (clase III), prolongando el período refractario y el intervalo QT. Esta combinación lo hace efectivo para mantener el ritmo sinusal en fibrilación auricular y para suprimir taquiarritmias ventriculares.

El Síndrome del Nodo Sinusal Enfermo tipo 2 (SSS2) de herencia autosómica dominante está asociado frecuentemente a mutaciones en el gen HCN4, que codifica canales iónicos responsables de la corriente If ("funny current") del nodo sinoauricular. La disfunción de estos canales genera bradicardia sinusal progresiva, pausas sinusales y disfunción cronotrópica. El tratamiento convencional se orienta hacia la estimulación eléctrica (marcapasos) y la reversión de la bradiarritmia.

El efecto bloqueador beta de Sotalol **suprime activamente la automaticidad del nodo sinoauricular**, lo que lo convierte en una **contraindicación relativa** para este síndrome, no en una oportunidad terapéutica. El elevado puntaje TxGNN (99.76%) refleja con mayor probabilidad la proximidad topológica en el grafo de conocimiento entre nodos de enfermedades de la conducción cardíaca, más que una relación causal terapéutica real. Esta predicción debe interpretarse como un artefacto del modelo y no debería avanzar sin una revisión mecanística exhaustiva.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Sotalol en Sick Sinus Syndrome 2, autosómica dominante.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Sotalol en Sick Sinus Syndrome 2, autosómica dominante.

---

## Información de Mercado en Argentina

Sotalol no cuenta con autorizaciones de comercialización registradas en Argentina. No se encontraron licencias activas en el período de consulta (corte: 2026-05-05).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo bloqueador beta-adrenérgico de Sotalol es fisiopatológicamente incompatible con el tratamiento del SSS2, dado que agrava la bradicardia sinusal que define esta condición; la ausencia total de evidencia clínica o preclínica directa confirma que esta predicción no representa una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Obtener datos detallados del mecanismo de acción (MOA) desde DrugBank API (brecha de datos DG002)
- Descargar y analizar el prospecto oficial para revisar contraindicaciones formales en bradicardia sinusal y SSS (brecha de datos DG001)
- Revisión mecanística alternativa: identificar si existe alguna subpoblación de SSS2 donde la regulación del IKr pudiera ser beneficiosa independientemente del bloqueo beta
- Investigación preclínica específica (modelos de HCN4 mutante) antes de considerar cualquier estudio en humanos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

