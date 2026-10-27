---
layout: default
title: Etoricoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Etoricoxib: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en las licencias de ANMAT (uso clínico conocido: artrit…"
monitor_inn: "ETORICOXIB"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Etoricoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Etoricoxib: De Indicación No Especificada en la Licencia a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Etoricoxib es un inhibidor selectivo de la COX-2 comercializado en Argentina, aunque los registros de ANMAT compilados para este informe no incluyen el texto de la indicación aprobada. Su uso clínico conocido abarca artritis reumatoide, artrosis, lumbalgia crónica, espondilitis anquilosante, dolor agudo y gota.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente no hay **ningún ensayo clínico** registrado y solo **1 publicación** vinculada (una revisión de alcance no específica del fármaco). La predicción se apoya esencialmente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las licencias de ANMAT (uso clínico conocido: artritis reumatoide, artrosis, lumbalgia crónica, espondilitis anquilosante, dolor agudo y gota) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Etoricoxib es un inhibidor selectivo de la COX-2 que reduce la síntesis de prostaglandina E2 (PGE2). Actualmente no se dispone de datos detallados del mecanismo de acción en la base de datos consultada, pero el objetivo farmacológico registrado es la COX-2 (gen PTGS2), lo que concuerda con esta clase de fármacos.

La PGE2 contribuye a la inflamación neurogénica y a la sensibilización trigeminovascular en la migraña, por lo que el mecanismo es plausible. Un estudio preclínico en ganglios trigeminales de rata (PMID 29209105, asociado a una entrada relacionada de susceptibilidad a migraña) evaluó el efecto de AINE, incluido etoricoxib, sobre la liberación de CGRP y PGE2, lo que ofrece apoyo mecanístico indirecto.

Sin embargo, la única publicación vinculada directamente a esta predicción es una revisión de alcance sobre cefalea inducida por ayuno en Ramadán, que no aporta datos de eficacia de etoricoxib en migraña. El puntaje elevado de TxGNN es solo una predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Revisión | Pain management | Revisión de alcance sobre la cefalea atribuida al ayuno durante Ramadán; no ofrece datos específicos de etoricoxib en migraña |

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de monofármaco (sin combinaciones ni canceladas). Los textos de indicación aprobada no figuran en los datos compilados. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33993 | ARCOXIA (Organon Arg.) | 60 mg comp. rec. x 28 | No disponible |
| 36921 | ARCOXIA (Organon Arg.) | 120 mg comp. rec. x 7 | No disponible |
| 54070 | BLOKIUM COX (Casasco) | 60 mg comp. x 28 | No disponible |
| 54048 | DORICOXIB 120 (Roemmers) | 120 mg comp. rec. x 10 | No disponible |
| 54154 | KEMPO (Teva Argentina) | 90 mg comp. rec. x 30 | No disponible |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó con un único registro, que corresponde a la diana farmacológica (COX-2) y no a una interacción con otro medicamento; no hay interacciones clínicas detalladas.
- **Señales de seguridad en la literatura vinculada a indicaciones relacionadas**:
  - Un reporte de caso describe hiperpotasemia potencialmente mortal y disfunción renal aguda con etoricoxib en un paciente tratado con telmisartán.
  - Un reporte de caso describe un posible síndrome de vasoconstricción cerebral reversible inducido por etoricoxib.
  - Como clase, los inhibidores de la COX-2 se asocian a riesgo cardiovascular y renal.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para migraña se basa únicamente en el modelo (nivel L5): no hay ensayos clínicos y la única publicación vinculada no aporta datos de eficacia. Aunque el mecanismo COX-2/PGE2 es plausible, no hay evidencia directa que justifique avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión sistemática de la literatura sobre inhibidores de COX-2 en migraña, incluyendo comparaciones con AINE establecidos
- Estudios clínicos controlados que evalúen eficacia en migraña, con evaluación del perfil de riesgo cardiovascular y renal

**Nota complementaria:** entre las demás predicciones, la **cefalea (headache disorder)** y la **cefalea autonómica trigeminal** tienen evidencia nivel L4 con serie de casos y reportes de caso (etoricoxib en cefalea punzante primaria, cefaleas sensibles a indometacina y cefalea tusígena secundaria). Podrían ser líneas de investigación más sólidas que la migraña, aunque aún sin ensayos controlados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

