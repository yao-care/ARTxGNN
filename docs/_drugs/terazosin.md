---
layout: default
title: Terazosin
parent: Solo Predicción del Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Terazosin: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Hipertensión arterial e hiperplasia prostática benigna (según las ind…"
---

# Terazosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Terazosina: De Hipertensión e Hiperplasia Prostática Benigna a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Terazosina es un bloqueante alfa-1 adrenérgico, originalmente utilizado para el tratamiento de la hipertensión arterial y la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial e hiperplasia prostática benigna (según las indicaciones originales del grafo de conocimiento; las autorizaciones locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 18 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, terazosina es un antagonista alfa-1 adrenérgico que relaja el músculo liso vascular y prostático, lo que explica su eficacia en hipertensión e hiperplasia prostática benigna.

Para la hipotricosis simple del cuero cabelludo, **no se conoce un vínculo mecanístico validado**. Esta enfermedad es un trastorno genético hereditario (por ejemplo, variantes en CDSN o APCDD1) y no hay relación establecida entre el bloqueo alfa-1 y la biología del folículo piloso. El puntaje alto probablemente refleja la cercanía en la red de conocimiento con otros fármacos relacionados con el cabello (por ejemplo, minoxidil, un vasodilatador), más que un mecanismo comprobado.

Por lo tanto, la predicción debe considerarse una hipótesis exploratoria de baja plausibilidad biológica.

### Otras predicciones del modelo

Entre las diez principales predicciones, algunas tienen más respaldo que la principal:

| Enfermedad | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Enfermedad de Raynaud | 99.83% | L3 (tentativo) | Mecanismo sólido (bloqueo alfa-1 de la vasoconstricción digital); un estudio clínico de 1997 (PMID 9273472) con diseño no especificado |
| Trastorno de migraña | 99.92% | L4 | Estudio pequeño de 1994 (PMID 7911406) y revisión de 1997 (PMID 9074296); datos antiguos y no confirmados |
| Migraña con aura de tronco encefálico | 99.91% | L4 | Evidencia indirecta (el estudio incluye migraña sin aura) |
| Alopecia | 99.95% | L4 | Solo una revisión general (PMID 34779371), no específica de terazosina |

Las demás predicciones (hipotricosis milia congénita, alopecia areata difusa, hipertricosis universal de tipo Ambras, trastorno bipolar maníaco, cardiopatía kifoscoliótica) solo cuentan con la predicción del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipotricosis simple del cuero cabelludo).

---

## Información de Mercado en Argentina

Se identificaron 18 autorizaciones vigentes de producto único (ninguna cancelada). Las autorizaciones no incluyen texto de indicación aprobada en los datos compilados. A continuación, las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 32798 | ANDRIN (Casasco) | 2 mg comp. x 30 | No disponible |
| 32799 | ANDRIN (Casasco) | 5 mg comp. x 30 | No disponible |
| 32800 | ANDRIN (Casasco) | 10 mg comp. x 30 | No disponible |
| 18283 | BLAVIN (Baliarda) | 2 mg comp. x 30 | No disponible |
| 34230 | GERIPROST (Teva Argentina) | 2 mg comp. ran. x 20 | No disponible |

Otras marcas con autorización vigente: BLAVIN (otras presentaciones), FOSFOMIK, GERIPROST, BENAPROST y PANAPROST.

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no del prospecto)**: atrofia multisistémica, síndrome de taquicardia ortostática postural, hipotensión ortostática, priapismo y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas**: se identificaron 137 interacciones potenciales. Las principales de nivel moderado incluyen corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona), bupropión, morfina (incluida la liposomal), opio, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), dronabinol y nabilona. Con nivel desconocido: calcitriol, pantoprazol y glimepirida.
- **Riesgo clínico relevante**: la hipotensión es especialmente importante en pacientes que reciben vasodilatadores o bloqueantes de canales de calcio.

Para advertencias y contraindicaciones según el prospecto, consultar el prospecto aprobado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se basa solo en el modelo (L5), sin ensayos ni literatura, y carece de plausibilidad mecanística para un trastorno genético del cabello. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Si se desea explorar el reposicionamiento, priorizar candidatas con mayor respaldo: **enfermedad de Raynaud** (mecanismo sólido, estudio clínico de 1997) y **migraña** (datos antiguos, requieren ensayos controlados modernos)
- Para cualquier indicación nueva, evaluar el riesgo de hipotensión y las interacciones con antihipertensivos y vasodilatadores
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

