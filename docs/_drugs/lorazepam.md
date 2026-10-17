---
layout: default
title: Lorazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lorazepam: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Ansiedad y epilepsias (según el grafo de conocimiento"
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
---

# Lorazepam
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

# Lorazepam: De Trastornos de Ansiedad y Epilepsia a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Lorazepam es una benzodiazepina utilizada originalmente para el tratamiento de la ansiedad y de distintos cuadros epilépticos (por ejemplo, el estado epiléptico, la epilepsia de ausencia y el síndrome de Lennox-Gastaut).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, con una puntuación muy alta pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ansiedad y epilepsias (según el grafo de conocimiento; los textos de indicación aprobados en las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, lorazepam pertenece a la clase de las benzodiazepinas, que potencian la inhibición mediada por el receptor GABA-A. Su eficacia en ansiedad y en convulsiones está bien establecida.

Sin embargo, no existe un vínculo mecanístico plausible entre la modulación alostérica positiva del receptor GABA-A y el tratamiento de una neoplasia. En el mejor de los casos, lorazepam podría ofrecer alivio sintomático (ansiedad o convulsiones asociadas), lo cual no modifica la enfermedad. La puntuación alta del modelo debe interpretarse como una señal estadística del grafo de conocimiento, no como una hipótesis terapéutica respaldada.

> **Nota sobre otras predicciones:** el modelo también predijo otras 9 indicaciones. La mayoría son epilepsias reflejas (convulsiones de lectura, sobresalto, audiogénicas, por alimentación, por micción, por pensamiento, inducidas por orgasmo), cuya plausibilidad mecanística es mayor por compartir el fenotipo convulsivo con las indicaciones conocidas. El **insomnio** es la única predicción con evidencia clínica directa (nivel L3), aunque se trata más bien de un uso establecido fuera de indicación que de un reposicionamiento novedoso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes (todas de monodroga, ninguna cancelada). Principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 9243 | TRAPAX (Pfizer) | 1 mg, comprimidos x 50 | No disponible |
| 41050 | CALMATRON (Savant Generic) | 2.5 mg, comprimidos x 50 | No disponible |
| 11733 | EMOTIVAL (Teva Argentina) | 2 mg, comprimidos x 30 | No disponible |
| 28209 | TRAPAX (Pfizer) | 2.5 mg, comprimidos x 30 | No disponible |
| 8026 | LORAZEPAN CHOBET (Soubeiran Chobet) | 2 mg, comprimidos x 100 | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedad hepática, encefalopatía hepática, coma hepático, enfermedad renal, enfermedad de la vesícula biliar, porfiria (hereditaria y otros trastornos del metabolismo de porfirinas), glaucoma de ángulo abierto y de ángulo cerrado, síndrome de apnea obstructiva del sueño y otras apneas, síndrome de hipoventilación central congénita, insuficiencia respiratoria, trastornos relacionados con sustancias y abuso/dependencia de sustancias.
- **Interacciones farmacológicas** (se identificaron 100 en total; se muestran las más relevantes):
  - **Graves:** morfina y morfina liposomal (depresión del sistema nervioso central y respiratoria).
  - **Moderadas:** bupropión, dronabinol, nabilona, teduglutida, metoclopramida, opio y sibutramina.
  - **Leves:** antiácidos como óxido, carbonato e hidróxido de magnesio, hidróxido de aluminio, carbonato de calcio y magaldrato.
- **Consideración adicional:** la literatura describe dependencia, tolerancia y deterioro al día siguiente con el uso crónico, así como toxicidad por propilenglicol con formulaciones intravenosas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino se basa únicamente en la puntuación del modelo (L5), sin ensayos, sin publicaciones y sin un mecanismo plausible que respalde un efecto modificador de la enfermedad.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del texto de indicaciones aprobadas en ANMAT.
- Prospecto de ANMAT con advertencias y contraindicaciones, para completar el análisis de seguridad.
- Evidencia preclínica o clínica que vincule la modulación GABA-A con la biología de esta neoplasia.
- Evaluar de forma prioritaria otras predicciones con mayor respaldo, como el insomnio (L3), considerando su perfil de riesgo y las alternativas no benzodiazepínicas recomendadas en guías.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

