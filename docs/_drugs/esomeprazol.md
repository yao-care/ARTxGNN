---
layout: default
title: Esomeprazol
parent: Solo Predicción del Modelo (L5)
nav_order: 158
evidence_level: L5
indication_count: 1
drugbank_id: DB00736
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-24
description: "Esomeprazol: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 3 (en el listado vigente: 3)"
---

# Esomeprazol
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

## Esomeprazol: obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones que reduce la secreción de ácido gástrico y se comercializa en Argentina.
El modelo TxGNN predice que podría ser efectivo para **obstrucción duodenal (duodenal obstruction)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Esomeprazol (traducción no oficial): «El esomeprazol pertenece a una clase de compuestos antisecretores, los bencimidazoles sustituidos, que suprimen la secreción de ácido gástrico mediante la inhibición específica del sistema enzimático H+/K+ ATPasa en la superficie secretora de la célula parietal gástrica. El esomeprazol se protona y se convierte en el compartimento ácido de la célula parietal, formando el inhibidor activo, la sulfenamida aquiral.» Texto original en inglés: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), versión del 2025-12-19; consultado el 2026-11-19). Según la información conocida, esomeprazol pertenece a la clase de los inhibidores de la bomba de protones, que suprimen la secreción de ácido gástrico.

Mecanísticamente, reducir el ácido podría disminuir la lesión de la mucosa, la ulceración y la inflamación del duodeno. Esto podría ayudar en casos de estenosis péptica u obstrucción asociada a úlcera, y en el alivio de síntomas.

Sin embargo, el fármaco no aliviaría una obstrucción mecánica causada por una neoplasia, un páncreas anular u otras causas estructurales. El puntaje alto (0,9945) podría reflejar la cercanía del fármaco con enfermedades duodenales relacionadas con el ácido (por ejemplo, úlcera duodenal o reflujo) y no un efecto terapéutico específico sobre la obstrucción. Esta relación no pudo verificarse con datos de origen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 45426 | NEXIUM | 10 mg sobres x 28 | AstraZeneca | Vigente |
| 47956 | VIMOVO | comp.lib.modif.x 30 | AstraZeneca | Vigente |
| 54068 | XINA | comp.lib.modif.x 30 | Finadiet | Vigente |

La tabla muestra los 3 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura que estudien directamente la obstrucción duodenal, y el efecto del fármaco no alcanzaría las causas mecánicas de obstrucción.

**Para avanzar se necesita:**
- Revisar la literatura y los registros de ensayos sobre esomeprazol en obstrucción duodenal
- Obtener los datos del mecanismo de acción
- Descargar y analizar los prospectos de ANMAT (advertencias y contraindicaciones), necesarios para el análisis de seguridad
- Definir qué causas de obstrucción (p. ej., péptica o por úlcera) podrían responder a la supresión ácida

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

