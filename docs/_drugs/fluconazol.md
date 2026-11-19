---
layout: default
title: Fluconazol
parent: Solo Predicción del Modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 1
drugbank_id: DB00196
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-16
description: "Fluconazol: nueva indicación predicha, queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Fluconazol
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

## Fluconazol: queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Fluconazol es un antifúngico de tipo azol. El modelo TxGNN predice que podría ser útil para **queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)**, pero actualmente no hay ensayos clínicos ni publicaciones que respalden esta dirección; el único sustento es el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fluconazol (traducción no oficial): «El fluconazol es un inhibidor altamente selectivo de la enzima fúngica dependiente del citocromo P450 lanosterol 14-α-desmetilasa. Esta enzima tiene la función de convertir el lanosterol en ergosterol. La consiguiente pérdida de esteroles normales se correlaciona con la acumulación de 14-α-metilesteroles en los hongos y puede ser responsable de la actividad fungistática del fluconazol.» Texto original en inglés: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), versión del 2026-04-02; consultado el 2026-11-19). Según la información farmacológica conocida, el fluconazol es un azol que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa) y bloquea la síntesis de ergosterol, un componente esencial de la membrana de los hongos.

La queratoconjuntivitis epitelial punteada suele ser de origen viral (adenovirus) o estar asociada a otras alteraciones de la superficie ocular; solo en algunos casos interviene un componente fúngico o microbiano. Un vínculo mecanístico plausible existiría únicamente en esos casos de etiología fúngica, y aun así sería indirecto.

El puntaje alto (0,9924) no constituye evidencia clínica por sí mismo y podría reflejar artefactos del modelo, como la cercanía con otros nodos de antifúngicos o de infecciones oculares. Por ello la predicción no puede contrastarse con la farmacología conocida a partir de los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El fluconazol está comercializado en Argentina. Se registran al menos 20 autorizaciones vigentes de productos de un solo principio activo; la lista puede ser parcial. Las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 31519 | DAMICOL | 150 mg caps. x 1 | Biol |
| 50783 | FUNGOCINA | 150 mg comp. x 8 | Lazar |
| 23526 | MUTUM | 150 mg comp. x 4 | Adium |
| 46179 | NIMIC 150 | 150 mg comp. x 8 | Géminis Farmacéutica |
| 21766 | FLUZOL | 150 mg comp. x 4 | Megalabs Argentina |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo, sin ensayos clínicos ni literatura que estudien directamente esta enfermedad (nivel de evidencia L5). El vínculo mecanístico sería indirecto y limitado a una posible etiología fúngica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado en ANMAT (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción
- Revisión de literatura y de registros de ensayos sobre fluconazol u otros azoles en queratoconjuntivitis, especialmente de origen fúngico
- Evaluar la viabilidad de una vía de administración ocular, ya que no se ha confirmado la compatibilidad de vías
- Una vez completados estos puntos, reevaluar la decisión

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

