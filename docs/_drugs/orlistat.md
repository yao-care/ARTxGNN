---
layout: default
title: Orlistat
parent: Solo Predicción del Modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Orlistat: nueva indicación predicha, Hipervitaminosis (nivel de evidencia L5). Indicación original: Trastorno de obesidad / obesidad monogénica"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Orlistat: De Trastorno de Obesidad a Hipervitaminosis
{: .text-alpha }

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
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (16 de 16) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 16 (vigentes: 16) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Orlistat inhibe las lipasas gástrica y pancreática y reduce la absorción de grasa de la dieta en aproximadamente un 30%. Como las vitaminas liposolubles (A, D, E y K) se absorben junto con la grasa dietética, orlistat disminuye también su absorción. Este es un efecto adverso bien documentado (hipovitaminosis), y por eso se aconseja suplementar vitaminas durante el tratamiento.

La relación con la nueva indicación es, por lo tanto, indirecta: una menor absorción de vitaminas liposolubles (sobre todo A y D) podría, en teoría, limitar su acumulación en casos de exceso. Es un mecanismo plausible pero no validado. Además, la hipervitaminosis suele deberse a suplementación excesiva, por lo que el manejo principal sería suspender el suplemento y cualquier beneficio de orlistat probablemente sería modesto y secundario.

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Orlistat (traducción no oficial): «El orlistat es un inhibidor reversible de las lipasas gastrointestinales. Ejerce su actividad terapéutica en la luz del estómago y del intestino delgado mediante la formación de un enlace covalente con el sitio del residuo de serina activo de las lipasas gástrica y pancreática.» Texto original en inglés: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), versión del 2026-09-30; consultado el 2026-11-19). El puntaje alto de TxGNN (0.9942) es solo una predicción del modelo. Además, el efecto malabsortivo de orlistat podría agregar riesgo en pacientes que necesitan mantener niveles adecuados de vitaminas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 41192 | CRISPLUS | 120 mg cáps.x 60 | Elea | Vigente |
| 21840 | XENICAL | 120 mg caps.x 84 | Siegfried | Vigente |
| 47587 | ORLIST | 60 mg cáps.x 30 | Wunder Pharm | Vigente |
| 42070 | OLEOFIN | 120 mg cáps.x 30 | Casasco | Vigente |
| 41191 | CRISPLUS | 120 mg cáps.x 30 | Elea | Vigente |

La tabla muestra 5 de los 16 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Todas las autorizaciones están vigentes y son de monofármaco.

<!-- review:begin ar-lic-20261125-orlistat-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «Se muestran 5 de las 15 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).» Corregido: desde el 2026-11-25 se incorporan a los datos los productos del listado vigente de PAMI posteriores a marzo de 2026, con el mismo criterio de recogida; la frase ya no coincidía con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125-orlistat-1 -->

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

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |
| 2026-11-25 | «5 de las 15» → todas | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

