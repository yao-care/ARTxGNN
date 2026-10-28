---
layout: default
title: Prasugrel
parent: Solo Predicción del Modelo (L5)
nav_order: 217
evidence_level: L5
indication_count: 9
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
last_modified_at: 2026-10-27
description: "Prasugrel: nueva indicación predicha, Hipertensión pulmonar (pulmonary hypertension) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 8 de 8) |
| Número de Autorizaciones | 8 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, prasugrel es un inhibidor del receptor plaquetario P2Y12 que reduce la agregación plaquetaria.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45310 | TROCAL | 10 mg comp. x 30 | No registrada en los datos locales |
| 48863 | FLUIDIN | 10 mg comp. rec. x 28 | No registrada en los datos locales |
| 45642 | CORILUM | 10 mg comp. rec. x 30 | No registrada en los datos locales |
| 45641 | CORILUM | 5 mg comp. rec. x 30 | No registrada en los datos locales |
| 44343 | PROCARDIA | 5 mg comp. x 30 | No registrada en los datos locales |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

