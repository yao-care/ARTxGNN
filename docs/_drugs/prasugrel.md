---
layout: default
title: Prasugrel
parent: Solo Predicción del Modelo (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Prasugrel: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: Síndrome coronario agudo"
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "migraine with or without aura, susceptibility to", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
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

# Prasugrel: De Síndrome Coronario Agudo a Hipertensión Pulmonar

## Resumen en Una Frase

Prasugrel es un antiagregante plaquetario que antagoniza el receptor P2Y12 y se utiliza originalmente en el síndrome coronario agudo.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente hay **0 ensayos clínicos** y **2 publicaciones** de relevancia indirecta, por lo que la predicción no cuenta con respaldo clínico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información disponible, prasugrel es un antagonista del receptor plaquetario P2Y12. Su eficacia en el síndrome coronario agudo se basa en reducir la activación y agregación plaquetaria.

Existe una justificación teórica para la hipertensión pulmonar: la activación plaquetaria y la trombosis in situ contribuyen al remodelado vascular pulmonar. Bloquear P2Y12 podría atenuar ese componente.

Esta justificación es solo teórica. Ninguna de las publicaciones recuperadas evalúa prasugrel en hipertensión pulmonar, y no hay ensayos clínicos que respalden este uso. La predicción se apoya sobre todo en el puntaje del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Current Medical Research and Opinion | Estudia los factores asociados al uso y la adherencia a clopidogrel en pacientes con síndrome coronario agudo tras una intervención coronaria percutánea. No evalúa prasugrel ni hipertensión pulmonar. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte (registro) | Kardiologiia | Analiza cómo influye el tratamiento previo de comorbilidades sobre el riesgo de desenlace letal por COVID-19, con datos del registro ACTIV. No evalúa prasugrel en hipertensión pulmonar. |

Ambas publicaciones tienen relevancia solo indirecta para la indicación predicha.

## Información de Mercado en Argentina

Se muestran 5 de las 8 autorizaciones vigentes, todas de medicamentos de un solo principio activo. Los datos compilados no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 45310 | TROCAL | 10 mg comp. x 30 | Nova Argentia |
| 48863 | FLUIDIN | 10 mg comp. rec. x 28 | Lazar |
| 45642 | CORILUM | 10 mg comp. rec. x 30 | Teva Argentina |
| 45641 | CORILUM | 5 mg comp. rec. x 30 | Teva Argentina |
| 44343 | PROCARDIA | 5 mg comp. x 30 | Roemmers |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, trastornos hipotensivos, enfermedades de la coagulación, accidente cerebrovascular y trastornos cerebrovasculares, susceptibilidad al ictus isquémico, infarto cerebral, lesiones traumáticas, púrpura trombocitopénica, hemorragia intracraneal, ataque isquémico transitorio e insuficiencia vertebrobasilar.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las de mayor gravedad entre las revisadas):
  - **Mayor:** deferasirox, ibritumomab tiuxetán.
  - **Moderada:** ácido acetilsalicílico, morfina, opio, dexfenfluramina, fenfluramina, sibutramina.
  - **Menor:** inhibidores de la bomba de protones (omeprazol, esomeprazol, pantoprazol, lansoprazol, dexlansoprazol, rabeprazol), antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina) y bupropión.
- **Riesgo hemorrágico:** el perfil de contraindicaciones (hemorragia intracraneal, trastornos de la coagulación) indica que el sangrado es una preocupación central en cualquier uso nuevo.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que pruebe prasugrel en hipertensión pulmonar. El nivel de evidencia es L5 y la predicción se basa solo en el modelo y en un mecanismo teórico. A esto se suma un riesgo hemorrágico relevante.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen prasugrel en modelos de hipertensión pulmonar.
- Datos detallados del mecanismo de acción y del vínculo entre la vía plaquetaria P2Y12 y el remodelado vascular pulmonar.
- Las advertencias y contraindicaciones del prospecto de ANMAT para completar la evaluación de seguridad.
- Un análisis de la relación beneficio-riesgo hemorrágico en esta población.
- Valorar otras predicciones del mismo modelo con más respaldo. La **migraña** (con foramen oval permeable) cuenta con una revisión retrospectiva de tienopiridinas, un piloto abierto con ticagrelor y un ensayo de Fase 3 en curso. Ese ensayo evalúa terapia dirigida al foramen oval permeable, no prasugrel directamente. Su evidencia (L3) es más sólida que la de hipertensión pulmonar, aunque sigue siendo limitada e indirecta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

