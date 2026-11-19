---
layout: default
title: Felodipina
parent: Solo Predicción del Modelo (L5)
nav_order: 171
evidence_level: L5
indication_count: 5
drugbank_id: DB01023
monitor_inn: "Felodipine"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-20
description: "Felodipina: nueva indicación predicha, Hipertensión pulmonar de mecanismo multifactorial poco claro (pulmonary hypertension with unclear multifactorial mechanism) (nivel de evidencia L5)."
---

# Felodipina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Felodipina: Hipertensión pulmonar de mecanismo multifactorial poco claro (pulmonary hypertension with unclear multifactorial mechanism)
{: .text-alpha }

## Resumen en Una Frase

Felodipina es un antagonista de los canales de calcio de tipo L del grupo de las dihidropiridinas, que relaja el músculo liso vascular y produce vasodilatación.
El modelo TxGNN predice que podría ser útil para **hipertensión pulmonar de mecanismo multifactorial poco claro (pulmonary hypertension with unclear multifactorial mechanism)**, pero actualmente no hay ensayos clínicos ni publicaciones que respalden directamente esta predicción: el sustento es solo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertensión pulmonar de mecanismo multifactorial poco claro (pulmonary hypertension with unclear multifactorial mechanism) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (6 de 6) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Felodipina (traducción no oficial): «El felodipino pertenece a la clase de las dihidropiridinas de antagonistas de los canales de calcio (bloqueantes de los canales de calcio). Compite de forma reversible con el nitrendipino y/u otros bloqueantes de los canales de calcio por los sitios de unión de las dihidropiridinas, bloquea las corrientes de Ca ++ dependientes de voltaje en el músculo liso vascular y en células auriculares de conejo en cultivo, y bloquea la contractura inducida por potasio de la vena porta de rata.» Texto original en inglés: "Felodipine is a member of the dihydropyridine class of calcium channel antagonists (calcium channel blockers). It reversibly competes with nitrendipine and/or other calcium channel blockers for dihydropyridine binding sites, blocks voltage-dependent Ca ++ currents in vascular smooth muscle and cultured rabbit atrial cells, and blocks potassium-induced contracture of the rat portal vein." ([DailyMed: Felopdipine (felodipine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=129c48eb-29f2-462b-ad8a-b3bf1b193115), versión del 2024-08-07; consultado el 2026-11-19). Según la información conocida, felodipina es un bloqueador de los canales de calcio de tipo L que relaja el músculo liso vascular y causa vasodilatación. Este es un fundamento plausible, aunque poco específico, para una acción vasodilatadora pulmonar.

Los bloqueadores de los canales de calcio solo resultan útiles en un subgrupo pequeño de pacientes con hipertensión arterial pulmonar vasorreactiva, y la enfermedad predicha está mal definida. Por ello, el puntaje del modelo es muy alto, pero no existe evidencia clínica ni bibliográfica que lo confirme.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Los datos locales registran 6 autorizaciones vigentes de productos con felodipina, todas del laboratorio AstraZeneca.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 55481 | PLENDIL | 10 mg comprimidos de liberación prolongada x 28 |
| 55482 | PLENDIL | 5 mg comprimidos de liberación prolongada x 28 |
| 45022 | ATACAND DUO | 16 mg/5 mg comprimidos x 60 |
| 45019 | ATACAND DUO | 8 mg/2,5 mg comprimidos x 60 |
| 45021 | ATACAND DUO | 16 mg/2,5 mg comprimidos x 60 |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene un puntaje alto, pero carece de ensayos clínicos y de estudios que evalúen directamente esta enfermedad (nivel L5). Además, la indicación está mal definida y los bloqueadores de los canales de calcio solo benefician a un subgrupo reducido de pacientes con hipertensión pulmonar.

**Para avanzar se necesita:**
- Definir con precisión la entidad clínica predicha y el subgrupo de pacientes relevante.
- Revisión bibliográfica dirigida a la circulación pulmonar y a pacientes con hipertensión pulmonar.
- Datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT.
- Evaluar el riesgo de empeorar el equilibrio ventilación-perfusión por vasodilatación en pacientes con enfermedad pulmonar.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Felopdipine (felodipine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=129c48eb-29f2-462b-ad8a-b3bf1b193115) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

