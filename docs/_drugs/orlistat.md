---
layout: default
title: Orlistat
parent: Solo Predicción del Modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Orlistat: nueva indicación predicha, Hipervitaminosis (nivel de evidencia L5). Indicación original: Trastorno de obesidad / obesidad monogénica"
---

# Orlistat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Orlistat: De Trastorno de Obesidad a Hipervitaminosis

## Resumen en Una Frase

Orlistat es un inhibidor de las lipasas gástrica y pancreática, originalmente utilizado para el tratamiento de la obesidad (incluida la obesidad monogénica).
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de obesidad / obesidad monogénica |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Orlistat inhibe las lipasas gástrica y pancreática y reduce la absorción de grasa de la dieta en aproximadamente un 30%. Como las vitaminas liposolubles (A, D, E y K) se absorben junto con la grasa dietética, orlistat disminuye también su absorción. Este es un efecto adverso bien documentado (hipovitaminosis), y por eso se aconseja suplementar vitaminas durante el tratamiento.

La relación con la nueva indicación es, por lo tanto, indirecta: una menor absorción de vitaminas liposolubles (sobre todo A y D) podría, en teoría, limitar su acumulación en casos de exceso. Es un mecanismo plausible pero no validado. Además, la hipervitaminosis suele deberse a suplementación excesiva, por lo que el manejo principal sería suspender el suplemento y cualquier beneficio de orlistat probablemente sería modesto y secundario.

Cabe señalar que los datos detallados del mecanismo de acción no estaban disponibles en los datos compilados para este informe; la explicación anterior se basa en el conocimiento farmacológico general. El puntaje alto de TxGNN (0.994) es solo una predicción del modelo. Además, el efecto malabsortivo de orlistat podría agregar riesgo en pacientes que necesitan mantener niveles adecuados de vitaminas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 41192 | CRISPLUS | 120 mg cápsulas x 60 | No especificada en los datos |
| 21840 | XENICAL | 120 mg cápsulas x 84 | No especificada en los datos |
| 47587 | ORLIST | 60 mg cápsulas x 30 | No especificada en los datos |
| 42070 | OLEOFIN | 120 mg cápsulas x 30 | No especificada en los datos |
| 41191 | CRISPLUS | 120 mg cápsulas x 30 | No especificada en los datos |

Se muestran 5 de las 15 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: insuficiencia hepática, hiperoxaluria primaria, anorexia nerviosa, bulimia nerviosa, trastorno por deficiencia de vitaminas, colestasis (incluidas la colestasis intrahepática recurrente benigna y la familiar) y daño hepático inducido por fármacos.
- **Interacciones Farmacológicas** (100 registradas; se listan las principales):
  - Moderadas: abacavir, lamivudina, acarbosa, albiglutida, alogliptina, metformina, amiodarona, asparaginasa (E. coli y Erwinia chrysanthemi), atazanavir, emtricitabina, brentuximab vedotina, calaspargasa pegol, canagliflozina, cannabidiol, clorpropamida, clofarabina.
  - Menores: colecalciferol, calcifediol, calcitriol (relevantes por su vínculo con las vitaminas liposolubles).

Para las advertencias y contraindicaciones del prospecto, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura. El mecanismo propuesto es teórico, y la propia acción de orlistat (reducir la absorción de vitaminas liposolubles) y varias contraindicaciones hepáticas y de deficiencia vitamínica plantean dudas sobre su utilidad en esta indicación.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Revisión bibliográfica dirigida sobre orlistat e hipervitaminosis A/D
- Advertencias y contraindicaciones del prospecto de ANMAT
- Evidencia preclínica o clínica que demuestre un beneficio real frente a suspender la suplementación
- Evaluación de la relación riesgo-beneficio en pacientes con riesgo de deficiencia vitamínica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

