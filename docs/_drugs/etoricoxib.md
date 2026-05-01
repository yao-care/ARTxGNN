---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Etoricoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Analizando el Evidence Pack de ETORICOXIB. El top predicted indication es **migraine disorder** (Rank 1, L5). No hay ensayos clínicos ni literatura directa para esta indicación. Etoricoxib no es antineoplásico → omito sección de citotoxicidad. Sin licencias ANMAT → adapto esa sección.

---

# Etoricoxib: De Dolor e Inflamación Articular a Trastorno de Migraña

## Resumen en Una Frase

Etoricoxib es un inhibidor selectivo de la ciclooxigenasa-2 (COX-2), ampliamente utilizado en el tratamiento del dolor e inflamación asociados a osteoartritis, artritis reumatoide, espondilitis anquilosante y artritis gotosa aguda, aunque actualmente no se encuentra comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno de Migraña (migraine disorder)**, con una puntuación de predicción del **99,90%**.
Sin embargo, a la fecha **no existen ensayos clínicos ni publicaciones científicas específicas** que validen directamente esta indicación, por lo que la evidencia se clasifica en el nivel más bajo posible (L5).

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Dolor e inflamación articular (osteoartritis, artritis reumatoide, espondilitis anquilosante, artritis gotosa aguda) |
| Nueva Indicacion Predicha | Trastorno de Migraña (migraine disorder) |
| Puntaje de Prediccion TxGNN | 99,90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información disponible, etoricoxib es un inhibidor selectivo de la COX-2 (ciclooxigenasa-2) de la clase de los AINEs; su eficacia en el manejo del dolor e inflamación articular ha sido comprobada en múltiples ensayos clínicos de Fase 3, y mecanísticamente podría ser aplicable al trastorno de migraña.

La conexión mecanística parte de la siguiente cadena bioquímica: la inhibición selectiva de COX-2 reduce la síntesis de prostaglandina E2 (PGE2). Durante las crisis de migraña, la PGE2 es liberada en grandes cantidades por los vasos sanguíneos de las meninges, actuando como mediador pro-nociceptivo que sensibiliza las terminaciones del nervio trigémino y contribuye a la hipersensibilidad central característica del episodio migrañoso. Desde una perspectiva biológica, bloquear este mediador inflamatorio es plausible como abordaje para modular la intensidad o la frecuencia de las crisis.

No obstante, esta plausibilidad mecanística no ha sido validada en estudios clínicos formales en pacientes con trastorno de migraña. La predicción de TxGNN se basa en relaciones estructurales del grafo de conocimiento biológico, y en este caso no existe respaldo de ensayos clínicos ni literatura específica dirigida a esta indicación, lo que limita significativamente la solidez de la recomendación.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados para etoricoxib en trastorno de migraña.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para etoricoxib en trastorno de migraña.

---

## Informacion de Mercado en Argentina

Etoricoxib no cuenta con autorizaciones de comercialización vigentes en Argentina (ANMAT). No se registran licencias activas a la fecha de corte de datos (2026-05-01).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Se identificaron dos brechas de datos (DG001: advertencias/contraindicaciones de ficha técnica; DG002: mecanismo de acción completo). Ambas requieren remediación antes de cualquier evaluación de seguridad formal.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
A pesar de la alta puntuación del modelo TxGNN (99,90%) y la existencia de una plausibilidad mecanística COX-2/PGE2 biológicamente razonable, la ausencia total de ensayos clínicos y literatura científica específica para esta indicación sitúa la evidencia en nivel L5. Esto impide avanzar hacia evaluación clínica sin investigación previa. La condición de fármaco no comercializado en Argentina añade una barrera regulatoria adicional que debe resolverse en paralelo.

**Para avanzar se necesita:**
- Revisión sistemática de estudios preclínicos que evalúen inhibidores de COX-2 en modelos experimentales de migraña (animales o celulares)
- Diseño de un estudio observacional o piloto (Fase 2) para evaluar la eficacia de etoricoxib en migraña episódica, como alternativa a indometacina cuando hay intolerancia gastrointestinal
- Obtención de datos completos de MOA y advertencias desde DrugBank y ficha técnica oficial (remediación de brechas DG001 y DG002)
- Evaluación del perfil de riesgo cardiovascular de los inhibidores selectivos de COX-2, especialmente en pacientes con migraña con aura (población con mayor riesgo cerebrovascular)
- Inicio del proceso de registro ante ANMAT para poder comercializar el fármaco en Argentina en caso de que la evidencia clínica avance favorablemente
---

