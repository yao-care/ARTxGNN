---
layout: default
title: Griseofulvina
parent: Solo Predicción del Modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
drugbank_id: DB00400
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "creeping myiasis", "furuncular myiasis", "wound myiasis", "echinococcus granulosus infectious disease"]
last_modified_at: 2026-11-24
description: "Griseofulvina: nueva indicación predicha, miasis (myiasis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Griseofulvina
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

## Griseofulvina: miasis (myiasis)
{: .text-alpha }

## Resumen en Una Frase

Griseofulvina es un antifúngico que interfiere con la función de los microtúbulos de los hongos.
El modelo TxGNN predice que podría ser efectivo para **miasis (myiasis)**, con un puntaje de 0.9941, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | miasis (myiasis) |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Griseofulvina (traducción no oficial): «El mecanismo de la griseofulvina consiste en la unión a proteínas microtubulares, que son necesarias para la mitosis. […] El mecanismo de la griseofulvina consiste en la unión a proteínas microtubulares, que son necesarias para la mitosis. Actividad in vivo La griseofulvina puede ser activa contra la mayoría de las cepas de los siguientes dermatofitos, según se describe en la sección INDICACIONES Y USO: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans y Trichophyton verrucosum.» Texto original en inglés: "The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. […] The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. Activity In Vivo Griseofulvin may be active against most strains of the following dermatophytes as described in the INDICATIONS AND USAGE section: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans and Trichophyton verrucosum." ([DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d), versión del 2025-05-14; consultado el 2026-11-19). Según la información conocida, la griseofulvina se une a la tubulina e inhibe la mitosis de las células fúngicas.

La miasis es una infestación por larvas de moscas (dípteros). Su tratamiento habitual consiste en la extracción de las larvas, el cuidado de la herida y, en algunos casos, ivermectina. No existe evidencia clínica ni preclínica que vincule a la griseofulvina con esta enfermedad.

Una hipótesis meramente especulativa es que la actividad sobre la tubulina podría afectar a las células de larvas de artrópodos. Sin embargo, esto no ha sido probado y se desconoce la selectividad del fármaco por la tubulina fúngica frente a la de los artrópodos. El puntaje alto del modelo es solo una predicción computacional y no establece una base mecanística.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 3883 | GRISOVIN FP | 500 mg comp.x 24 | Siegfried | Vigente |

La tabla muestra el único producto de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se registraron interacciones farmacológicas en los datos compilados para este informe.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos, literatura ni mecanismo plausible que la respalde (nivel de evidencia L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Estudios in vitro o preclínicos que muestren actividad contra larvas causantes de miasis
- Revisión bibliográfica dirigida que identifique cualquier estudio directo sobre miasis

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

