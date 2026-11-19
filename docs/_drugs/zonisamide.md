---
layout: default
title: Zonisamide
parent: Solo Predicción del Modelo (L5)
nav_order: 248
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Zonisamide: nueva indicación predicha, Síndrome de Tourette (nivel de evidencia L5). Indicación original: No especificada en las autorizaciones de ANMAT (el texto de indicació…"
monitor_inn: "ZONISAMIDE"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
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

## Zonisamida: De Antiepiléptico a Síndrome de Tourette
{: .text-alpha }

## Resumen en Una Frase

Zonisamida es un fármaco antiepiléptico (anticonvulsivante) comercializado en Argentina bajo la marca KINAPLASE. El modelo TxGNN predice que podría ser efectivo para el **síndrome de Tourette**, con un puntaje de 0.9985. Hasta ahora no hay **ningún ensayo clínico ni publicación** que respalde esta dirección, por lo que es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en las autorizaciones de ANMAT (el texto de indicación está vacío); la literatura la describe como fármaco antiepiléptico |
| Nueva Indicación Predicha | Síndrome de Tourette |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Zonisamide (traducción no oficial): «Se desconoce el mecanismo o los mecanismos precisos por los que la zonisamida ejerce su efecto anticonvulsivo. La zonisamida demostró actividad anticonvulsivante en varios modelos experimentales. En animales, la zonisamida fue eficaz contra las convulsiones de extensión tónica inducidas por electrochoque máximo, pero ineficaz contra las convulsiones clónicas inducidas por pentilenotetrazol subcutáneo.» Texto original en inglés: "The precise mechanism(s) by which zonisamide exerts its antiseizure effect is unknown. Zonisamide demonstrated anticonvulsant activity in several experimental models. In animals, zonisamide was effective against tonic extension seizures induced by maximal electroshock but ineffective against clonic seizures induced by subcutaneous pentylenetetrazol." ([DailyMed: Zonegran (zonisamide) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb), versión del 2026-09-23; consultado el 2026-11-19). Según la información conocida, zonisamida bloquea los canales de sodio dependientes de voltaje y los canales de calcio tipo T. También modula la transmisión dopaminérgica y serotoninérgica. Su eficacia como antiepiléptico está establecida, y mecanísticamente podría relacionarse con los circuitos de los tics, en los que participan la dopamina y la excitabilidad neuronal.

Esta relación es especulativa. No se aportaron ensayos ni literatura que la sustenten. Además, una revisión pragmática (PMID 36005856) sugiere que los medicamentos antiepilépticos pueden **inducir** trastorno de tics y trastorno obsesivo-compulsivo. Por eso la dirección del efecto es incierta: el fármaco podría incluso empeorar el cuadro.

El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No es evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 40729 | KINAPLASE | 100 mg cápsulas x 30 | Teva Argentina |
| 40728 | KINAPLASE | 50 mg cápsulas x 30 | Teva Argentina |

Ambas autorizaciones están vigentes y corresponden a productos de principio activo único.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (PrimeKG, no texto de prospecto)**: el grafo asocia zonisamida con contraindicación en las siguientes condiciones:
  - Trastornos psiquiátricos: ansiedad, trastorno neurótico, trastorno distímico, trastornos psicóticos, esquizofreniforme y esquizoafectivo, y trastorno mental en general.
  - Enfermedades renales y hepáticas: enfermedad renal, piouréter, nefrolitiasis (incluida la susceptibilidad por SLC26A1), nefropatía aguda por uratos, enfermedad hepática y enfermedad de la vesícula biliar.
  - Trastornos metabólicos y digestivos: acidosis metabólica y enfermedad diarreica.
  - Trastornos hematológicos: agranulocitosis y diversas formas de neutropenia (congénita grave, cíclica, idiopática del adulto, síndrome de Kostmann, entre otras).
- **Interacciones farmacológicas** (se identificaron 100; se muestran las principales):
  - **Mayores**: anticolinérgicos como atropina, escopolamina, hiosciamina, metescopolamina, glicopirronio, clidinio, diciclomina, trospio, mepenzolato y propantelina; también metformina.
  - **Moderadas**: aprepitant, morfina, dexametasona, cimetidina, claritromicina, dronabinol, nabilona, metoclopramida y miconazol.
- **Señal de seguridad específica**: hay un reporte de manía inducida por zonisamida (PMID 2109869) y una revisión que vincula los antiepilépticos con trastornos de tics (PMID 36005856). Ambos son relevantes para una población psiquiátrico-neurológica como la del síndrome de Tourette.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de Tourette se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, existe una señal de que los antiepilépticos pueden inducir tics, y el grafo de conocimiento registra varias contraindicaciones psiquiátricas. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Revisión de la literatura preclínica y clínica sobre zonisamida en trastornos de tics y síndrome de Tourette.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Obtención y análisis del prospecto de ANMAT (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Evaluación específica del riesgo de empeoramiento de tics o síntomas psiquiátricos.
- Si se prosigue, un estudio piloto bien diseñado antes de considerar cualquier uso.

**Nota:** entre las otras predicciones de zonisamida, la **epilepsia de ausencia** tiene mayor respaldo (nivel L3). Se apoya en estudios pequeños (PMID 15847848 y 24907183), pero tampoco incluye ensayos de Fase 3. Podría ser una alternativa a evaluar con mayor prioridad que el síndrome de Tourette.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zonegran (zonisamide) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

