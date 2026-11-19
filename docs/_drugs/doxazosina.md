---
layout: default
title: Doxazosina
parent: Evidencia Moderada (L3-L4)
nav_order: 146
evidence_level: L4
indication_count: 2
drugbank_id: DB00590
monitor_inn: "Doxazosin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-11-20
description: "Doxazosina: nueva indicación predicha, trastorno de migraña (migraine disorder) (nivel de evidencia L4). En Argentina, productos en el listado de PAMI: 3 (en el listado vigente: 3)"
---

# Doxazosina
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

## Doxazosina: trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Doxazosina es un antagonista selectivo de los receptores adrenérgicos alfa-1 que cuenta con autorizaciones vigentes en Argentina.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña (migraine disorder)**,
con **0 ensayos clínicos** y **1 publicación** (una revisión de 1997) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9920 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Doxazosina bloquea de forma selectiva los receptores adrenérgicos alfa-1. Este bloqueo podría modular el tono vascular cerebral y la señalización noradrenérgica central, dos procesos que se vinculan con la fisiopatología de la migraña. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Doxazosina (traducción no oficial): «Hiperplasia prostática benigna (HPB) Los síntomas asociados a la hiperplasia prostática benigna (HPB), como la polaquiuria, la nicturia, el chorro débil, la dificultad para iniciar la micción y el vaciado incompleto, están relacionados con dos componentes, uno anatómico (estático) y otro funcional (dinámico). El componente estático está relacionado con un aumento del tamaño de la próstata causado, en parte, por una proliferación de células de músculo liso en el estroma prostático. […] Los estudios en sujetos humanos sanos han demostrado que la doxazosina antagonizó de forma competitiva los efectos presores de la fenilefrina (un agonista alfa 1) y el efecto presor sistólico de la norepinefrina.» Texto original en inglés: "Benign Prostatic Hyperplasia (BPH) The symptoms associated with benign prostatic hyperplasia (BPH), such as urinary frequency, nocturia, weak stream, hesitancy, and incomplete emptying are related to two components, anatomical (static) and functional (dynamic). The static component is related to an increase in prostate size caused, in part, by a proliferation of smooth muscle cells in the prostatic stroma. […] Studies in normal human subjects have shown that doxazosin competitively antagonized the pressor effects of phenylephrine (an alpha 1 agonist) and the systolic pressor effect of norepinephrine." ([DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82), versión del 2023-10-15; consultado el 2026-11-19).

El único respaldo es una revisión de 1997 que comenta el posible papel de los bloqueantes alfa-1 en la profilaxis de la migraña, con una pequeña serie de 10 pacientes tratados con terazosina o doxazosina. Los bloqueantes alfa-1 no son profilácticos establecidos de la migraña, por lo que el mecanismo sigue siendo hipotético y el puntaje alto del modelo (0,9920) no está validado por estudios clínicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisión | Headache | Experiencia personal del autor con 10 pacientes con migraña tratados con terazosina o doxazosina: en casi todos disminuyó la frecuencia o la gravedad de las crisis, pero 5 suspendieron el tratamiento por efectos secundarios. No se notificaron reacciones adversas graves. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35927 | CARDURA | 4 mg tab. x 30 | No registrada en los datos locales |
| 23080 | DOXASIN | 4 mg comp. x 30 | No registrada en los datos locales |
| 35926 | CARDURA | 2 mg tab. x 30 | No registrada en los datos locales |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una revisión antigua basada en una serie muy pequeña, sin ensayos clínicos. El puntaje del modelo es alto, pero no hay estudios que lo validen, por lo que esta hipótesis se mantiene en etapa de pregunta de investigación.

**Para avanzar se necesita:**
- Datos del prospecto de ANMAT (advertencias y contraindicaciones), actualmente no disponibles
- Datos detallados del mecanismo de acción
- Estudios controlados que evalúen la doxazosina en la profilaxis de la migraña
- Evaluación de tolerabilidad, dado que la mitad de los pacientes de la serie suspendió el fármaco por efectos secundarios

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cardura (doxazosin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5e1f5e49-2da1-43ab-9795-228a8bcc5a82) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

