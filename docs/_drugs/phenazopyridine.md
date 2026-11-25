---
layout: default
title: Phenazopyridine
parent: Solo Predicción del Modelo (L5)
nav_order: 211
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Phenazopyridine: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: No disponible en la licencia de ANMAT (el fármaco se describe como an…"
monitor_inn: "phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
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

## Fenazopiridina: De Analgésico Urinario a Bronquitis
{: .text-alpha }

## Resumen en Una Frase

La fenazopiridina es un analgésico del tracto urinario, comercializado en Argentina como CISTALGINA (monofármaco) y UROTEM DOL (asociación con norfloxacina); el texto de indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

<!-- review:begin ar-lic-20261125-phenazopyridine-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «comercializado en Argentina como UROTEM DOL;» Corregido: desde el 2026-11-25 se incorporan a los datos los productos del listado vigente de PAMI posteriores a marzo de 2026, con el mismo criterio de recogida; la frase ya no coincidía con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125-phenazopyridine-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la licencia de ANMAT (el fármaco se describe como analgésico del tracto urinario) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 0.9923 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fenazopiridina es un analgésico que actúa localmente sobre la mucosa del tracto urinario, aunque su mecanismo exacto no está bien caracterizado.

No se ha establecido un vínculo mecanístico con la bronquitis. No se conoce una vía farmacológica que conecte a este fármaco con la inflamación bronquial o la infección respiratoria. Su uso original (alivio sintomático urinario) y la nueva indicación (enfermedad de las vías respiratorias) son áreas terapéuticas muy distintas.

El puntaje alto de TxGNN (0.9923) proviene únicamente de la predicción del modelo TxGNN (aprendizaje profundo) y no está respaldado por evidencia clínica ni bibliográfica. Podría reflejar artefactos de la red, como vecinos compartidos con otros fármacos o genes, y no una relación biológica real. Esta predicción debe interpretarse con mucha cautela.

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
| 30587 | UROTEM DOL | comp.x 10 + 10 | Temis-Lostaló | Vigente |

La tabla muestra 1 de los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provienen del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática (incluida encefalopatía/coma hepático), enfermedad renal, porfiria, enfermedad pulmonar obstructiva crónica, apnea del sueño, enfermedad arterial coronaria, hiperplasia prostática benigna, trastornos de ansiedad y neuróticos, abuso/dependencia de sustancias, enfermedad de la vesícula biliar, y trastornos hematológicos (anemia, trombocitopenia, neutropenia, agranulocitosis). Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 24 interacciones, de las cuales se listan 20 en los datos disponibles.
  - **Mayores**: ácido nitroso, leflunomida.
  - **Moderadas** (principales): naltrexona, anestésicos locales (lidocaína, benzocaína, tetracaína, oxibuprocaína, cinchocaína, cocaína), metotrexato, asparaginasa, pegaspargasa, brentuximab vedotina, clofarabina, idelalisib e interferón beta-1a/1b.

Para las advertencias y contraindicaciones del prospecto, consultar el prospecto oficial de ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible entre un analgésico urinario local y la bronquitis. Además, el perfil de seguridad no está completo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica y de ensayos específica para fenazopiridina y enfermedades respiratorias.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original.
- Reconsiderar la decisión solo si se identifica evidencia preclínica o mecanística que sustente la hipótesis.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-25 | Se añade CISTALGINA | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

