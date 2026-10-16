---
layout: default
title: Bisoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 58
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Bisoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Bisoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bisoprolol: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Bisoprolol es un bloqueador beta-1 adrenérgico selectivo, originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, bisoprolol es un bloqueador beta-1 adrenérgico cardioselectivo, con eficacia comprobada en hipertensión, y mecanísticamente podría ser aplicable a complicaciones hipertensivas.

La enfermedad renal hipertensiva maligna es una complicación grave de órgano blanco de la hipertensión. El bloqueo beta-1 reduce la presión arterial y la liberación de renina, lo que ofrece un fundamento plausible. El puntaje alto de TxGNN probablemente refleja la cercanía de este nodo con la indicación original de hipertensión en el grafo de conocimiento.

Sin embargo, la hipertensión maligna es una emergencia hipertensiva que suele manejarse con fármacos intravenosos, y los betabloqueantes orales no son de primera línea. La predicción no está respaldada por evidencia clínica.

Otras predicciones del modelo, también con evidencia limitada:
- **Hipertensión renovascular maligna** (99.94%, L5): la reducción de renina es plausible, pero los inhibidores del sistema renina-angiotensina y la revascularización son las opciones estándar.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (99.93%, L4): solo hay estudios preclínicos y fisiológicos indirectos; los betabloqueantes pueden reducir el gasto cardíaco y la capacidad de ejercicio, lo que plantea un riesgo.
- **Hipertensión pulmonar de mecanismo multifactorial incierto** (99.93%, L5): sin vínculo mecanístico directo; el bloqueo beta puede ser perjudicial para la función del ventrículo derecho.
- **Síndrome de Braddock** (99.91%, L5): enfermedad muy rara sin fundamento mecanístico evidente; probablemente un artefacto del grafo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (enfermedad renal hipertensiva maligna).

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55671 | PROBLOCK | 5 mg, comprimidos recubiertos x 30 | No especificada |
| 57506 | PROBLOCK | 10 mg, comprimidos recubiertos x 30 | No especificada |
| 25417 | CORBIS | 10 mg, comprimidos recubiertos x 30 | No especificada |
| 58967 | CORBIS | 10 mg, comprimidos recubiertos x 60 | No especificada |
| 53329 | BISOPIL | 2.5 mg, comprimidos recubiertos x 30 | No especificada |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada). Otras marcas: Bisoprolol Teva, Bisofec, Bicardil y Lostaprolol.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, asma (intrínseca y alérgica), deficiencia de potasio, psoriasis, diabetes mellitus, cetoacidosis diabética, hiperuricemia, hiperparatiroidismo, coma y encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo y miastenia gravis.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales de nivel moderado figuran epinefrina, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), anticolinérgicos (atropina, hiosciamina, metescopolamina), bupropión, morfina, acetohexamida y sales de calcio. De nivel menor: ácido acetilsalicílico, hidróxido de aluminio y attapulgita.

Las advertencias y contraindicaciones del prospecto no estaban disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos ni literatura. Además, la hipertensión maligna se maneja habitualmente con fármacos intravenosos, por lo que un betabloqueante oral no es una opción de primera línea.

**Para avanzar se necesita:**
- Estudios clínicos o literatura que evalúen bisoprolol en enfermedad renal hipertensiva maligna
- Datos del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT, necesarias para el análisis de seguridad
- Evaluación de la compatibilidad de la vía de administración y comparación con los tratamientos estándar
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

