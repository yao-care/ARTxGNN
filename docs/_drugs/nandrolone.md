---
layout: default
title: Nandrolone
parent: Solo Predicción del Modelo (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Nandrolone: nueva indicación predicha, Enfermedad fibroquística de la mama (nivel de evidencia L4). Indicación original: No disponible en la licencia de ANMAT (texto de indicación vacío). Co…"
monitor_inn: "nandrolone"
predicted_indications: ["breast fibrocystic disease", "benign mammary dysplasia", "blunt duct adenosis of breast", "apocrine adenosis of breast", "fetal erythroblastosis", "breast abscess", "fat necrosis of breast", "lactation disease", "breast adenosis", "renal osteodystrophy"]
---

# Nandrolone
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

## Nandrolona: De Indicación Original No Registrada a Enfermedad Fibroquística de la Mama
{: .text-alpha }

## Resumen en Una Frase

Nandrolona (decanoato de nandrolona, comercializada en Argentina como DECA-DURABOLIN) es un esteroide anabólico-androgénico; la licencia de ANMAT disponible no incluye un texto de indicación aprobada. El modelo TxGNN predice que podría ser efectiva para la **enfermedad fibroquística de la mama**, pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** de 1964 que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la licencia de ANMAT (texto de indicación vacío). Como referencia farmacológica, se usa en anemias refractarias por producción deficiente de glóbulos rojos y en otras situaciones (cáncer de mama, angioedema hereditario, síndrome de Turner, entre otras) |
| Nueva Indicación Predicha | Enfermedad fibroquística de la mama |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la nandrolona es un esteroide anabólico-androgénico que actúa sobre el receptor de andrógenos (AR) y tiene efectos antiestrogénicos y antigonadotrópicos. Además, aumenta la producción de eritropoyetina, por lo que se utiliza en anemias refractarias.

Históricamente, los andrógenos se emplearon para contrarrestar la proliferación impulsada por estrógenos en la patología mamaria benigna. Esto ofrece un fundamento mecanístico plausible, pero no verificado, para la enfermedad fibroquística de la mama y sus entidades relacionadas (displasia mamaria benigna, adenosis).

Debe tenerse cautela: el único respaldo es un artículo de 1964 sobre el tratamiento médico de las displasias mamarias, que no es un estudio controlado moderno. El puntaje de 0.999 es una predicción computacional, no una validación clínica. Además, existe riesgo de virilización.

### Otras predicciones del modelo (todas con evidencia débil)

| Enfermedad predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Displasia mamaria benigna | 0.9983 | L5 | Sinónimo cercano; sin literatura directa |
| Adenosis de conductos romos de mama | 0.9979 | L5 | Subtipo histológico; solo predicción |
| Adenosis apocrina de mama | 0.9979 | L5 | Subtipo histológico; solo predicción |
| Eritroblastosis fetal | 0.9977 | L5 | Ajuste mecanístico débil y riesgo de virilización fetal |
| Absceso mamario | 0.9970 | L5 | Probable artefacto del modelo |
| Necrosis grasa de mama | 0.9970 | L5 | Probable artefacto del modelo |
| Enfermedad de la lactancia | 0.9968 | L5 | Supresión de lactancia conceptualmente posible; indicación imprecisa |
| Adenosis mamaria | 0.9963 | L5 | Mismo artículo de 1964, relevancia incierta |
| Osteodistrofia renal | 0.9954 | L5 | Efecto anabólico óseo plausible; sin datos vinculados; pregunta de investigación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14150264](https://pubmed.ncbi.nlm.nih.gov/14150264/) | 1964 | Revisión | Revista de la Asociación Médica Argentina | "Displasias mamarias: tratamiento médico". No se dispone de resumen; es un artículo histórico sin datos de un estudio controlado moderno |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6181 | DECA-DURABOLIN (Aspen Pharma) | 50 mg inyectable x 1 x 1 ml | No especificada en la licencia |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la nandrolona con contraindicación en las siguientes condiciones:
  - Hepáticas y biliares: enfermedad hepática, colestasis (incluida la colestasis intrahepática recurrente benigna y familiar), enfermedad de la vesícula biliar.
  - Cardiovasculares: enfermedad cardíaca, enfermedad cardiovascular, enfermedad coronaria, infarto de miocardio, trombosis coronaria.
  - Próstata: cáncer, neoplasia y carcinoma de próstata, hiperplasia prostática benigna.
  - Renales: insuficiencia renal, uremia, síndrome nefrótico (incluidos el familiar y la nefrosis lipoidea).
  - Metabólicas y del calcio: hipercalcemia (incluida la hipercalcemia humoral de neoplasias malignas), nefrocalcinosis, trastornos del metabolismo del fósforo, diabetes mellitus, cetoacidosis diabética.
  - Hematológicas: hemoglobinopatía.
- **Interacciones farmacológicas**: solo se identificó la interacción farmacológica con el receptor de andrógenos (AR), que es su mecanismo de acción principal; no hay interacciones medicamentosas clínicas con nivel de gravedad registradas.
- **Riesgos señalados en el análisis**: virilización, y efectos cardiovasculares, hepáticos y lipídicos. Es especialmente desfavorable su uso durante el embarazo por el riesgo de virilización fetal.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto del modelo, pero la única evidencia es un artículo de 1964 sin resumen y no hay ensayos clínicos. Además, el perfil de seguridad (virilización, riesgos hepáticos y cardiovasculares) es desfavorable para una condición benigna como la enfermedad fibroquística de la mama.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT para completar la indicación aprobada, las advertencias y las contraindicaciones.
- Completar los datos detallados del mecanismo de acción (MOA).
- Realizar una búsqueda sistemática de literatura moderna y de ensayos clínicos sobre andrógenos en patología mamaria benigna.
- Comparar con las alternativas terapéuticas actuales para la enfermedad fibroquística de la mama y evaluar la relación beneficio-riesgo.
- Explorar por separado la osteodistrofia renal como pregunta de investigación (efectos óseos y sobre la anemia en pacientes en diálisis), con evaluación de seguridad cardiovascular y hepática.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

