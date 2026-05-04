---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 5
---

# Perindopril
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

La habilidad `txgnn-pipeline` confirma el contexto del proyecto. Procedo a generar el informe siguiendo el template v5.

---

# Perindopril: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (IECA), originalmente utilizado para el tratamiento de la hipertensión arterial y la insuficiencia cardíaca.
El modelo TxGNN predice que podría ser efectivo para la **Enfermedad Renal Hipertensiva Maligna**,
con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en registros argentinos (Perindopril es un IECA para hipertensión arterial) |
| Nueva Indicación Predicha | Enfermedad Renal Hipertensiva Maligna |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack. Según la información disponible en el análisis de reposicionamiento, Perindopril es un inhibidor de la ECA (enzima convertidora de angiotensina) cuyo efecto principal consiste en bloquear la conversión de Angiotensina I a Angiotensina II, reduciendo así la actividad del sistema RAAS (renina-angiotensina-aldosterona).

El vínculo mecanístico con la enfermedad renal hipertensiva maligna es fisiopatológicamente coherente: al disminuir los niveles de Angiotensina II, Perindopril provoca vasodilatación de la arteriola eferente glomerular, reduciendo la presión intraglomerular y enlenteciendo la progresión de la proteinuria y la fibrosis renal. Adicionalmente, la acumulación de bradicinina resultante del bloqueo de la ECA aporta una capa adicional de protección renal a través de la liberación de óxido nítrico. Este mecanismo es precisamente el fundamento farmacológico por el que los IECAs son el pilar del tratamiento nefroprotector en hipertensión severa con daño renal.

La enfermedad renal hipertensiva maligna comparte con las indicaciones clásicas de los IECAs el componente central de hipertensión arterial grave con lesión renal secundaria mediada por Angiotensina II. Sin embargo, la evidencia clínica directa para esta indicación específica es aún escasa, y los datos disponibles en este paquete de evidencia no permiten confirmar eficacia diferencial en el contexto "maligno" de esta entidad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Observacional/Clínico | Urologiia (Moscow) | Evalúa la función renal tras nefrectomía radical por cáncer renal; aborda la pérdida de función renal postquirúrgica y la importancia de preservar el riñón contralateral, contexto de relevancia indirecta para el manejo nefroprotector en hipertensión severa |

---

## Información de Mercado en Argentina

Perindopril **no cuenta con autorizaciones de comercialización registradas en Argentina**. No se dispone de datos de productos aprobados, nombres comerciales ni formas farmacéuticas registradas ante ANMAT.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el mecanismo de acción de Perindopril (bloqueo RAAS / inhibición de la ECA) posee una base fisiopatológica teóricamente coherente con la enfermedad renal hipertensiva maligna, la ausencia total de ensayos clínicos directos y la existencia de solo una publicación tangencialmente relacionada sitúan la evidencia en nivel L4. Esto no es suficiente para avanzar hacia una recomendación de uso o desarrollo clínico activo en este momento.

**Para avanzar se necesita:**
- Recuperar el mecanismo de acción completo (MOA) desde DrugBank (DG002) y las advertencias de seguridad del prospecto (DG001)
- Confirmar si existen ensayos clínicos internacionales con IECAs en hipertensión maligna con afectación renal (búsqueda ampliada en ClinicalTrials.gov e ICTRP)
- Evaluar el estado regulatorio de Perindopril en Argentina ante ANMAT para determinar viabilidad de comercialización
- Obtener literatura específica que vincule Perindopril (o IECAs en general) con outcomes clínicos en enfermedad renal hipertensiva maligna, como estudios observacionales o series de casos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

