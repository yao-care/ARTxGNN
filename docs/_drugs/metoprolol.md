---
layout: default
title: Metoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (según las indicaciones originales del grafo de…"
monitor_inn: "METOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "posteroinferior myocardial infarction", "posterolateral myocardial infarction", "septal myocardial infarction", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Metoprolol: De Hipertensión arterial a Enfermedad renal hipertensiva maligna

## Resumen en Una Frase

Metoprolol es un betabloqueante, utilizado originalmente para el tratamiento de la hipertensión arterial, el síndrome coronario agudo y el infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, metoprolol es un bloqueante selectivo de los receptores beta-1 adrenérgicos. Su eficacia en hipertensión arterial está establecida, y mecanísticamente podría ser aplicable a formas graves de hipertensión con compromiso renal.

El bloqueo beta-1 reduce la frecuencia cardíaca, el gasto cardíaco y la liberación de renina. Por eso la predicción es plausible como una extensión de gravedad de la indicación original, la hipertensión.

Sin embargo, no se encontraron ensayos ni literatura sobre la nefropatía hipertensiva maligna en particular. El manejo agudo de la hipertensión maligna se realiza normalmente con fármacos intravenosos, y los betabloqueantes cumplen un papel complementario. Se trata esencialmente de una extensión dentro de la misma clase de la indicación existente, no de una verdadera señal reposicionamiento. El puntaje alto del modelo, por sí solo, no basta para respaldarla.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 55478 | BELOZOK | 25 mg, comprimidos de liberación prolongada x 28 | AstraZeneca |
| 55479 | BELOZOK | 50 mg, comprimidos de liberación prolongada x 28 | AstraZeneca |
| 55480 | BELOZOK | 100 mg, comprimidos de liberación prolongada x 28 | AstraZeneca |

Las tres autorizaciones están vigentes y corresponden a productos de un solo principio activo.

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de precaución (según el grafo de conocimiento, no según el texto del prospecto)**: trastornos de ansiedad y trastornos neuróticos, distimia, pancreatitis, enfermedad hepática (incluidos coma y encefalopatía hepática), enfermedad de la vesícula biliar, lupus eritematoso sistémico, psoriasis, diabetes mellitus y cetoacidosis diabética, gota e hiperuricemia, hipotensión, hiperparatiroidismo, hipercalcemia y nefrocalcinosis, trastornos del metabolismo del fósforo, deficiencia de potasio, anuria, ictericia neonatal, miastenia gravis y enfermedades de la unión neuromuscular, y feocromocitoma.
- **Interacciones Farmacológicas**: la consulta identificó 100 interacciones. Entre las principales:
  - Interacciones moderadas: epinefrina, bupropión, morfina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, lorcaserina, atropina, hioscina, glicopirronio, fosfato y acetato de calcio, y corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida).
  - Interacciones leves: ácido acetilsalicílico y óxido de magnesio.
- **Precaución adicional**: en hipertensión pulmonar y en enfermedad pulmonar crónica, los betabloqueantes requieren cautela. El ensayo BLOCK COPD (metoprolol) no mostró reducción de exacerbaciones y se asoció con más exacerbaciones que requirieron hospitalización.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.91%), pero no existe ningún ensayo ni publicación específica para la enfermedad renal hipertensiva maligna (nivel L5). Además, es una extensión de gravedad de una indicación ya aprobada, no un reposicionamiento genuino.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones oficiales).
- Revisión sistemática de la literatura sobre betabloqueantes en hipertensión maligna con compromiso renal.
- Evaluación nefrológica y cardiológica sobre el papel de metoprolol frente a los fármacos de primera línea en crisis hipertensivas.
- Confirmar que la nueva indicación aporta valor más allá de la indicación de hipertensión ya autorizada.
- Como referencia, otras predicciones del modelo con más literatura (por ejemplo, infartos de miocardio por localización o cardiopatía pulmonar crónica, ambas nivel L3) son subtipos de indicaciones existentes o tienen señales de seguridad desfavorables, por lo que también requieren análisis independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

