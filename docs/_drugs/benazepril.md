---
layout: default
title: Benazepril
parent: Solo Predicción del Modelo (L5)
nav_order: 44
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Benazepril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Benazepril
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

# Benazepril: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Benazepril es un inhibidor de la enzima convertidora de angiotensina (IECA), originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; se trata de una predicción del modelo, en gran parte una extensión de la indicación ya existente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

> Nota: los datos compilados asignan a esta predicción un nivel L4 (evidencia indirecta, basada en mecanismo). Sin embargo, al no existir estudios reales sobre benazepril en esta condición, según los criterios del informe corresponde L5. La decisión Hold coincide en ambos casos.

> Nota sobre la indicación original: las autorizaciones locales no incluyen texto de indicación aprobada; la indicación original se tomó de la base de conocimiento utilizada por el modelo.

## ¿Por qué es Razonable esta Predicción?

Benazepril es un IECA que reduce la formación de angiotensina II y, con ello, la vasoconstricción y la secreción de aldosterona. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados; esta descripción se basa en la clase farmacológica conocida del fármaco.

La enfermedad renal hipertensiva maligna es una forma grave de hipertensión con daño renal, en la que la activación del sistema renina-angiotensina-aldosterona (SRAA) tiene un papel central. Por ello, el ajuste mecanístico es plausible y el puntaje alto del modelo (99.65%) refleja la cercanía con la indicación aprobada. Es más una extensión de la indicación de hipertensión que una oportunidad de reposicionamiento distinta.

Cabe señalar que no se aportaron ensayos ni literatura para esta condición, por lo que la evidencia es indirecta y de carácter predictivo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 36106 | ILDUC DUO (Baliarda) | Cápsulas 5/10 mg x 30 | No especificada |
| 31897 | ARTERIOSAN PLUS (Laboratorios Be) | Cápsulas 5/10 mg x 30 | No especificada |
| 46167 | ARTERIOSAN PLUS (Laboratorios Be) | Cápsulas 5/20 mg x 30 | No especificada |
| 36107 | ILDUC DUO (Baliarda) | Cápsulas 2.5/10 mg x 30 | No especificada |
| 39462 | ILDUC DUO (Baliarda) | Cápsulas 5/20 mg x 30 | No especificada |

Se muestran 5 de las 12 autorizaciones vigentes (también hay TERLOC DUO de Siegfried y PELMEC DUO de Casasco). Ninguna está cancelada.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: insuficiencia hepática, enfermedad renal, angioedema (adquirido, hereditario e inducido por bloqueadores del SRAA), pancreatitis, lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, hipotensión, hiperparatiroidismo, encefalopatía hepática, anuria, deficiencia de potasio, enfermedades del tejido conectivo, entre otras.
- **Riesgo renal específico**: en la estenosis bilateral de la arteria renal o con riñón único, los IECA pueden causar deterioro agudo de la función renal. Esto es relevante para la enfermedad renal hipertensiva y la hipertensión renovascular.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las 20 mostradas son de nivel moderado e incluyen antidiabéticos (alogliptina, acetohexamida, clorpropamida, dapagliflozina, exenatida, glimepirida, glipizida, gliburida), múltiples insulinas e hidrocortisona. El riesgo principal es la potenciación del efecto hipoglucemiante.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente coherente, pero no existe ningún ensayo ni publicación que la respalde, y se solapa en gran medida con la indicación ya aprobada de hipertensión. Además, la información de seguridad oficial no está disponible.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisión de literatura clínica específica sobre IECA en hipertensión maligna con daño renal.
- Evaluar la seguridad renal (estenosis de arteria renal, función renal basal, potasio).
- Definir si la indicación representa un reposicionamiento real o solo un subtipo de la indicación actual.

**Otras predicciones del modelo (todas en Hold):**
- Hipertensión renovascular maligna (99.65%, L4): coherente con el SRAA, con riesgo de deterioro renal agudo.
- Hipertensión pulmonar multifactorial (99.60%, L5) e hipertensión pulmonar por enfermedad pulmonar o hipoxia (99.60%, L5): sin respaldo clínico; las tres publicaciones recuperadas son estudios preclínicos de fibrosis renal y miocárdica que no involucran benazepril y no apoyan esta indicación. La vasodilatación sistémica podría ser perjudicial.
- Síndrome de Braddock (99.44%, L5): no se puede establecer una relación mecanística; solo sirve como hipótesis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

