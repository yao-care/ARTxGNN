---
layout: default
title: Ceftriaxona
parent: Solo Predicción del Modelo (L5)
nav_order: 92
evidence_level: L5
indication_count: 5
drugbank_id: DB01212
monitor_inn: "Ceftriaxone"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-16
description: "Ceftriaxona: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 7 (en el listado vigente: 7)"
---

# Ceftriaxona
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Ceftriaxona: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Ceftriaxona es un antibiótico betalactámico de la clase de las cefalosporinas de tercera generación, que actúa inhibiendo la síntesis de la pared celular bacteriana.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ceftriaxona (traducción no oficial): «La ceftriaxona es un fármaco antibacteriano. […] La ceftriaxona es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. La ceftriaxona tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Ceftriaxone is an antibacterial drug. […] Ceftriaxone is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftriaxone has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467), versión del 2022-01-13; consultado el 2026-11-19). Según la información conocida, la ceftriaxona es una cefalosporina de tercera generación que inhibe la síntesis de la pared celular bacteriana, con actividad antibacteriana de amplio espectro.

El síndrome de hiperviscosidad policlonal está causado por una elevación de las inmunoglobulinas y no tiene ninguna diana antibacteriana conocida. No se identificó un vínculo mecanístico plausible entre ambos.

El puntaje alto (0,9939) parece ser un artefacto de la predicción basada en el modelo, sin respaldo de ensayos clínicos ni literatura. Por ello, esta predicción no debe interpretarse como una hipótesis terapéutica sólida sin evidencia adicional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 48555 | ACANTEX | 500 mg IM, frasco ampolla x 1 |
| 13323 | CEFTRIAXONA RICHET | 1 g IV, frasco ampolla + solvente |
| 13807 | CEFTRIAXONA FABRA | 1 g, frasco ampolla x 1 |
| 13324 | CEFTRIAXONA RICHET | 1 g IM, frasco ampolla + solvente |
| 48516 | ACANTEX | 1 g IM, frasco ampolla x 1 |

Se muestran 5 de las 7 autorizaciones vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, no existe un vínculo mecanístico plausible y el nivel de evidencia es L5 (solo predicción del modelo).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos o clínicos que evalúen directamente el síndrome de hiperviscosidad policlonal, antes de considerar cualquier avance

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

