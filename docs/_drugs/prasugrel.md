---
layout: default
title: Prasugrel
parent: Solo Predicción del Modelo (L5)
nav_order: 217
evidence_level: L5
indication_count: 9
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
last_modified_at: 2026-11-24
description: "Prasugrel: nueva indicación predicha, Hipertensión pulmonar (pulmonary hypertension) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 8 (en el listado vigente: 8)"
---

# Prasugrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Prasugrel: antiagregante plaquetario inhibidor del receptor P2Y12 → Hipertensión pulmonar (pulmonary hypertension)
{: .text-alpha }

## Resumen en Una Frase

Prasugrel es un antiagregante plaquetario que inhibe el receptor P2Y12.
El modelo TxGNN predice que podría ser útil para **hipertensión pulmonar (pulmonary hypertension)**, pero actualmente **no hay ensayos clínicos** y las **2 publicaciones** recuperadas no estudian directamente esta enfermedad, por lo que la predicción carece de respaldo clínico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertensión pulmonar (pulmonary hypertension) |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (8 de 8) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 8 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Prasugrel (traducción no oficial): «El prasugrel es un inhibidor de la activación y la agregación plaquetarias mediante la unión irreversible de su metabolito activo a la clase P2Y 12 de receptores de ADP en las plaquetas.» Texto original en inglés: "Prasugrel is an inhibitor of platelet activation and aggregation through the irreversible binding of its active metabolite to the P2Y 12 class of ADP receptors on platelets." ([DailyMed: Effient (prasugrel hydrochloride) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69ea2d58-5353-4222-b61f-cab976fa7e5e), versión del 2022-09-07; consultado el 2026-11-19). Según la información conocida, prasugrel es un inhibidor del receptor plaquetario P2Y12 que reduce la agregación plaquetaria.

Existe una justificación biológica plausible: la activación plaquetaria y la trombosis in situ participan en el remodelado vascular pulmonar, por lo que bloquear la agregación podría, en teoría, ser relevante en la hipertensión pulmonar.

Sin embargo, las dos publicaciones recuperadas tratan sobre la adherencia al clopidogrel tras un síndrome coronario agudo y sobre la influencia de tratamientos de base en la mortalidad por COVID-19. Ninguna evalúa prasugrel en hipertensión pulmonar. El puntaje alto del modelo, por tanto, no está respaldado por evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Current Medical Research and Opinion | Factores asociados al uso, adherencia y persistencia de clopidogrel en pacientes con síndrome coronario agudo tras intervención coronaria percutánea; no estudia hipertensión pulmonar. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte | Kardiologiia | Influencia del tratamiento de base de comorbilidades previo a la infección sobre el riesgo de desenlace letal por COVID-19 (registro ACTIVE); no estudia hipertensión pulmonar. |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 45310 | TROCAL | 10 mg comp.x 30 | Nova Argentia | Vigente |
| 48863 | FLUIDIN | 10 mg comp.rec.x 28 | Lazar | Vigente |
| 45642 | CORILUM | 10 mg comp.rec.x 30 | Teva Argentina | Vigente |
| 45641 | CORILUM | 5 mg comp.rec.x 30 | Teva Argentina | Vigente |
| 44343 | PROCARDIA | 5 mg comp.x 30 | Roemmers | Vigente |

La tabla muestra 5 de los 8 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Las 8 autorizaciones registradas están vigentes; se muestran las 5 principales.

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (100 interacciones registradas; ejemplos):
  - Mayores: deferasirox, ibritumomab tiuxetán.
  - Moderadas: morfina, ácido acetilsalicílico, opio, fenfluramina, dexfenfluramina, sibutramina.
  - Menores: antiácidos y gastroprotectores como famotidina, ranitidina, cimetidina, omeprazol, esomeprazol, lansoprazol, pantoprazol, rabeprazol, bupropión.
- **Enfermedades con relación de contraindicación registrada en los datos compilados** (no proviene del texto del prospecto): insuficiencia hepática, trastornos hipotensivos, enfermedades de la coagulación, accidente cerebrovascular, trastornos cerebrovasculares, infarto cerebral, ataque isquémico transitorio, hemorragia intracraneal, púrpura trombocitopénica, lesiones e insuficiencia vertebrobasilar.

Consultar el prospecto para la información completa de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ninguna publicación ni ensayo recuperado estudia prasugrel en hipertensión pulmonar, por lo que el nivel de evidencia es L5. El puntaje alto de TxGNN (0,9988) es solo una predicción computacional, y el riesgo hemorrágico de prasugrel exige cautela.

**Para avanzar se necesita:**
- Revisión de literatura preclínica sobre antiagregantes P2Y12 en hipertensión pulmonar (modelos animales, estudios de plaquetas).
- Datos del mecanismo de acción detallados del fármaco.
- Texto del prospecto de ANMAT (advertencias y contraindicaciones) para evaluar la seguridad.
- Evaluación del balance beneficio-riesgo hemorrágico en esta población antes de plantear cualquier estudio clínico.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Effient (prasugrel hydrochloride) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69ea2d58-5353-4222-b61f-cab976fa7e5e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

