---
layout: default
title: Cefoxitin
parent: Solo Predicción del Modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
description: "Cefoxitin: nueva indicación predicha, Otitis media infecciosa (infectious otitis media) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Cefoxitin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefoxitin: Otitis media infecciosa (infectious otitis media)
{: .text-alpha }

## Resumen en Una Frase

Cefoxitina es una cefamicina de segunda generación, un antibiótico con actividad contra bacterias grampositivas, gramnegativas y anaerobias.
El modelo TxGNN predice que podría ser efectiva para **otitis media infecciosa (infectious otitis media)**,
pero actualmente **no hay ensayos clínicos** y solo **1 publicación** (una revisión general sobre MRSA) se vincula con esta predicción, por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Otitis media infecciosa (infectious otitis media) |
| Puntaje de Predicción TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cefoxitin (traducción no oficial): «La cefoxitina es un fármaco antibacteriano. […] La cefoxitina es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. La cefoxitina tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Cefoxitin is an antibacterial drug. […] Cefoxitin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefoxitin has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864), versión del 2019-07-29; consultado el 2026-11-19). Según la información conocida, la cefoxitina es una cefamicina de segunda generación con actividad contra bacterias grampositivas, gramnegativas y anaerobias, por lo que existe un vínculo antibacteriano plausible con los patógenos que causan otitis media.

Sin embargo, la única publicación recuperada es una revisión general sobre *Staphylococcus aureus* resistente a meticilina (MRSA) desde la perspectiva "Una Salud", que menciona la otitis media solo como una de las infecciones que este patógeno puede causar. Además, la cefoxitina se usa habitualmente como marcador de laboratorio para detectar resistencia a meticilina, y no como tratamiento en este contexto.

No hay evidencia clínica que respalde esta indicación. La predicción se apoya únicamente en la plausibilidad antibacteriana general.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revisión | Infection and Drug Resistance | Revisión sobre epidemiología, factores de virulencia, resistencia a antibióticos e impacto zoonótico de MRSA; menciona la otitis media entre las infecciones que causa en humanos. No evalúa cefoxitina como tratamiento. |

## Información de Mercado en Argentina

Estado de mercado: Comercializado. Hay 1 autorización vigente.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 17797 | CEFOXITINA RICHET | 1 g iny.f.a.+a.sol. | Richet | Vigente |

La tabla muestra el único producto de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 35 interacciones en total. Las de nivel moderado incluyen kanamicina, neomicina, estreptomicina, ácido picosulfúrico y dicumarol. Con heparina la interacción es menor. Otras (por ejemplo vancomicina, metronidazol, claritromicina, omeprazol, morfina) figuran con nivel no clasificado.
- **Condiciones con relación de contraindicación registrada**: enfermedad renal, piouréter, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y colitis. Estas relaciones no provienen del texto del prospecto y deben verificarse en él.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación vinculada es una revisión general sobre MRSA que no evalúa cefoxitina para otitis media. La evidencia se clasifica como L5 y la predicción se apoya solo en la plausibilidad antibacteriana.

**Para avanzar se necesita:**
- Estudios clínicos o de eficacia que evalúen directamente la cefoxitina en otitis media infecciosa
- Datos de mecanismo de acción y de sensibilidad de los patógenos típicos del oído medio frente a cefoxitina
- Información de advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Evaluación de la compatibilidad de la vía de administración (la presentación local es inyectable) con esta indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

