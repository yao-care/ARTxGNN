---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: De Artritis Reumatoide a Displasia Acromesomélica Tipo Hunter-Thompson

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) con preferencia selectiva por COX-2, ampliamente utilizado a nivel mundial para el tratamiento del dolor musculoesquelético, osteoartritis, artritis reumatoide y espondilitis anquilosante. El modelo TxGNN predice que podría ser efectivo para **Displasia Acromesomélica Tipo Hunter-Thompson**, sin embargo, actualmente no existen **ensayos clínicos ni publicaciones científicas** que respalden directamente esta dirección de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide y osteoartritis (aprobación global reconocida; sin registro en Argentina según datos consultados) |
| Nueva Indicación Predicha | Displasia Acromesomélica Tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Sin embargo, Meloxicam es un inhibidor preferencial de la ciclooxigenasa-2 (COX-2) perteneciente a la clase de los AINEs. Su mecanismo central consiste en reducir la síntesis de prostaglandinas proinflamatorias, lo que se traduce en efectos analgésicos y antiinflamatorios ampliamente documentados en múltiples contextos clínicos, especialmente enfermedades articulares inflamatorias.

La displasia acromesomélica tipo Hunter-Thompson es una enfermedad ósea hereditaria causada por mutaciones en el gen **GDF5**, que compromete el desarrollo normal del cartílago y produce acortamiento característico de los segmentos distales de las extremidades. Se trata de una condición de origen genético-estructural, cuya fisiopatología principal no es la inflamación crónica mediada por prostaglandinas. En este contexto, Meloxicam no tiene capacidad de modificar la progresión de la enfermedad ni de corregir el defecto molecular subyacente.

La inhibición de COX-2 podría teóricamente ofrecer alivio sintomático del dolor en pacientes con esta displasia, pero este beneficio sería estrictamente paliativo. El alto puntaje TxGNN (99.92%) probablemente refleja una co-ocurrencia estructural en el grafo de conocimiento entre el nodo "enfermedades óseas/musculoesqueléticas" y la clase "AINEs", más que una predicción sustentada en mecanismos biológicos específicos de esta enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Meloxicam en displasia acromesomélica tipo Hunter-Thompson.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Meloxicam en displasia acromesomélica tipo Hunter-Thompson.

---

## Información de Mercado en Argentina

Meloxicam no cuenta con autorizaciones de comercialización registradas en la base de datos consultada para Argentina (0 registros encontrados).

> **Nota importante:** Meloxicam es un medicamento ampliamente comercializado a nivel internacional bajo nombres comerciales como *Mobic*, *Movalis* y *Melox*, con aprobación en numerosos países para artritis reumatoide, osteoartritis y espondilitis anquilosante. La ausencia de registro en esta consulta puede reflejar una limitación de la fuente de datos local, y no implica que el fármaco sea desconocido o sin historial clínico.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La displasia acromesomélica tipo Hunter-Thompson es una enfermedad genética estructural sin mecanismo farmacológico plausible para Meloxicam más allá del manejo sintomático del dolor. No existe ningún ensayo clínico ni publicación científica que respalde este uso, y el alto puntaje TxGNN parece originarse en la generalización del modelo hacia el grupo amplio de enfermedades óseas, no en evidencia biológica específica de esta entidad.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción (MOA) completo de Meloxicam mediante consulta a la API de DrugBank (DG002 pendiente)
- Obtener información de seguridad, advertencias y contraindicaciones del prospecto oficial (DG001 pendiente)
- Registrar autorizaciones ANMAT si existen, para completar el perfil regulatorio local
- Considerar priorizar indicaciones alternativas con mayor plausibilidad mecanística identificadas en este mismo análisis:
  - **Rank 6 — Espondiloartropatía** (L4): Meloxicam es tratamiento de primera línea según guías ASAS/EULAR; la ausencia de evidencia en esta base de datos se atribuye a un déficit de cobertura documental, no a ausencia de evidencia clínica real
  - **Rank 8 — Artritis Idiopática Juvenil Poliarticular RF+** (L4): existe 1 publicación de seguridad (PMID: [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/)) y uso clínico establecido en Europa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

