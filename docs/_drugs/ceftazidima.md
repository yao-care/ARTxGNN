---
layout: default
title: Ceftazidima
parent: Solo Predicción del Modelo (L5)
nav_order: 91
evidence_level: L5
indication_count: 9
drugbank_id: DB00438
monitor_inn: "Ceftazidime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
last_modified_at: 2026-11-20
description: "Ceftazidima: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Ceftazidima
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

## Ceftazidima: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Ceftazidima es un antibiótico cefalosporínico de tercera generación con autorizaciones vigentes en Argentina. El modelo TxGNN predice como principal nueva indicación el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción sin sustento real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ceftazidima (traducción no oficial): «La ceftazidima es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. La ceftazidima tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Ceftazidime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftazidime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93), versión del 2026-08-03; consultado el 2026-11-19). Por conocimiento general, ceftazidima es una cefalosporina de tercera generación con actividad antibacteriana, en particular frente a *Pseudomonas aeruginosa*.

El síndrome de hiperviscosidad policlonal es una condición de la sangre asociada a exceso de proteínas o inmunoglobulinas, y no una infección bacteriana. No se identifica un vínculo mecanístico entre un antibiótico y esta enfermedad. El puntaje alto del modelo parece ser un artefacto de la predicción y no refleja una base biológica o clínica.

Por lo tanto, la predicción no es razonable desde el punto de vista farmacológico con la información disponible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 13320 | CEFTAZIDIMA RICHET | 1 g iny.f.a. (C/u) | No registrada en los datos locales |
| 4007 | FORTUM | 1000 mg f.a.x 1 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe ceftazidima en el síndrome de hiperviscosidad policlonal, no hay vínculo mecanístico plausible y el nivel de evidencia es L5 (solo predicción del modelo).

**Para avanzar se necesita:**
- Una hipótesis mecanística biológicamente fundamentada que justifique el uso de un antibiótico en esta condición
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de las autorizaciones locales
- Evidencia preclínica o clínica directa en la indicación predicha, hoy inexistente

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

