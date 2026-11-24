---
layout: default
title: Diosmin
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Diosmin: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "diosmin"
predicted_indications: ["amenorrhea (disease)"]
---

# Diosmin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Diosmina: De Indicación Original No Especificada a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

La diosmina es un flavonoide comercializado en Argentina en múltiples presentaciones (comprimidos, sobres y crema), aunque los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Diosmin es (traducción no oficial): «Desconocido». Texto original en inglés: "Unknown" ([ChEMBL CHEMBL231884 (diosmin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL231884), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general (no proveniente de los datos compilados), la diosmina es un flavonoide venoactivo, asociado a efectos sobre el tono vascular y la microcirculación, además de actividad antiinflamatoria y antioxidante.

No hay un vínculo mecanístico establecido entre estas propiedades y la amenorrea, ni con la regulación menstrual o el eje hipotálamo-hipófiso-ovárico. El puntaje de 0.9942 proviene exclusivamente del modelo y no está respaldado por estudios reales. Una hipótesis especulativa sería un posible efecto sobre la función venosa o microvascular pélvica, que requeriría validación independiente.

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto único, ninguna cancelada). Los textos de indicación aprobada no están disponibles en los datos compilados.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 51186 | DIOSMIN CREMA | pomo x 30 g | Craveri | Vigente |
| 14737 | FLEBON 500 | 500 mg comp.x 30 | Teva Argentina | Vigente |
| 52849 | DIOSMIN CREMA | pomo x 90 g | Craveri | Vigente |
| 944 | FLEBOTROPIN 300 | comp.x 40 | Bagó | Vigente |
| 943 | FLEBOTROPIN 300 | comp.x 20 | Bagó | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, sin mecanismo de acción documentado ni vínculo biológico plausible con la amenorrea. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar los prospectos de ANMAT (advertencias y contraindicaciones) y las indicaciones aprobadas
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una revisión sistemática de literatura y de registros de ensayos clínicos sobre diosmina y trastornos menstruales
- Evaluar la plausibilidad biológica (por ejemplo, función microvascular pélvica) con estudios preclínicos o de mecanismo
- Verificar la compatibilidad de vías de administración, dado que las presentaciones disponibles son principalmente orales y una crema

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL231884 (diosmin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL231884) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

