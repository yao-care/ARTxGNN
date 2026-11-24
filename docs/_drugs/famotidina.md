---
layout: default
title: Famotidina
parent: Solo Predicción del Modelo (L5)
nav_order: 168
evidence_level: L5
indication_count: 4
drugbank_id: DB00927
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-11-24
description: "Famotidina: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 10 (en el listado vigente: 10)"
---

# Famotidina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Famotidina: obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Famotidina es un antagonista de los receptores H2 de histamina que reduce la secreción de ácido gástrico y se comercializa en Argentina.
El modelo TxGNN predice que podría ser útil para **obstrucción duodenal (duodenal obstruction)**, pero no hay ensayos clínicos y solo 2 publicaciones (reportes de caso) que lo abordan de forma indirecta, por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (10 de 10) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 10 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Famotidina bloquea los receptores H2 de histamina y con ello disminuye la secreción de ácido gástrico. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Famotidina (traducción no oficial): «La famotidina es un inhibidor competitivo de los receptores de histamina-2 (H2). La principal actividad farmacológica clínicamente importante de la famotidina es la inhibición de la secreción gástrica. La famotidina suprime tanto la concentración de ácido como el volumen de la secreción gástrica, mientras que los cambios en la secreción de pepsina son proporcionales al volumen secretado.» Texto original en inglés: "Famotidine is a competitive inhibitor of histamine-2 (H2) receptors. The primary clinically important pharmacologic activity of famotidine is inhibition of gastric secretion. Both the acid concentration and volume of gastric secretion are suppressed by famotidine, while changes in pepsin secretion are proportional to volume output." ([DailyMed: Pepcid (famotidine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a06502d9-7903-4f37-833e-e5763d502def), versión del 2024-06-01; consultado el 2026-11-19).

La supresión ácida podría ayudar a controlar la enfermedad ulcerosa péptica que en ocasiones provoca estenosis u obstrucción duodenal (por ejemplo, estenosis asociada a úlcera o úlcera marginal). Sin embargo, famotidina no alivia una obstrucción mecánica. El puntaje alto probablemente refleja la proximidad en la red de relaciones con la úlcera péptica y las enfermedades duodenales, más que un efecto terapéutico directo sobre la obstrucción.

En conjunto, la relevancia es indirecta en el mejor de los casos y debe considerarse una hipótesis computacional que requiere validación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Reporte de caso | Surgery Today | Mujer de 29 años con enfermedad de Crohn duodenal y obstrucción persistente de la salida gástrica; se describe el tratamiento quirúrgico. No evalúa famotidina. |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Reporte de caso | Surgical Endoscopy | Úlcera marginal gigante como complicación de la gastroenterostomía, con posibles complicaciones como obstrucción, hemorragia y perforación. No evalúa famotidina. |

Ninguna de las publicaciones estudia directamente el efecto de famotidina sobre la obstrucción duodenal.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 57735 | GASTROSEDOL NF | 40 mg comp.x 30 | Siegfried | Vigente |
| 57104 | TAURAL F 20 | 20 mg comp.x 60 | Roemmers | Vigente |
| 58340 | LAZARTIDINA | 40 mg comp.rec.x 30 | Lazar | Vigente |
| 57103 | TAURAL F 20 | 20 mg comp.x 30 | Roemmers | Vigente |
| 58338 | LAZARTIDINA | 20 mg comp.rec.x 30 | Lazar | Vigente |

La tabla muestra 5 de los 10 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Se muestran 5 de las 10 autorizaciones vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni con estudios que evalúen directamente famotidina en obstrucción duodenal, y el mecanismo (supresión ácida) no resuelve una obstrucción mecánica. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente faltante
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar estudios que evalúen directamente famotidina u otros antisecretores en obstrucción duodenal de origen ulceroso
- Definir si el posible beneficio sería solo sintomático o adyuvante frente al tratamiento endoscópico o quirúrgico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Pepcid (famotidine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a06502d9-7903-4f37-833e-e5763d502def) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

