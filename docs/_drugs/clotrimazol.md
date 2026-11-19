---
layout: default
title: Clotrimazol
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 2
drugbank_id: DB00257
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-16
description: "Clotrimazol: nueva indicación predicha, acné (acne (disease)) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 9 (en el listado vigente: 9)"
---

# Clotrimazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Clotrimazol: acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Clotrimazol es un antifúngico imidazólico de uso tópico, comercializado en Argentina en cremas, spray y polvo dérmico.
El modelo TxGNN predice que podría ser efectivo para **acné (acne (disease))**, pero la evidencia es muy limitada: **1 ensayo clínico** suspendido (con un producto combinado) y **ninguna publicación** respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (9 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clotrimazol (traducción no oficial): «El clotrimazol es un agente antifúngico de amplio espectro que inhibe el crecimiento de levaduras patógenas al alterar la permeabilidad de las membranas celulares. La acción del clotrimazol es fungistática a concentraciones del fármaco de hasta 20 mcg/mL y puede ser fungicida in vitro contra Candida albicans y otras especies del género Candida a concentraciones más altas.» Texto original en inglés: "Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations." ([DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f), versión del 2025-03-27; consultado el 2026-11-19). Según la información conocida, el clotrimazol es un antifúngico imidazólico que inhibe la síntesis de ergosterol fúngico (lanosterol 14-alfa-desmetilasa, CYP51). También se han descrito cierta actividad antibacteriana y antiinflamatoria, y acción frente a *Malassezia*, levadura implicada en algunas afecciones foliculares y acneiformes.

Este vínculo es indirecto y especulativo. No hay evidencia directa que relacione al clotrimazol con la fisiopatología del acné vulgar (*Cutibacterium acnes*, producción de sebo, hiperqueratinización folicular, inflamación). El puntaje elevado del modelo es una predicción computacional y no reemplaza la evidencia clínica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Eficacia comparativa de la combinación betametasona/beclometasona + gentamicina + clotrimazol en crema en dermatosis contaminada con lesiones bilaterales simétricas. Sin resultados disponibles. |

Este ensayo evalúa un producto combinado, por lo que cualquier efecto no puede atribuirse al clotrimazol solo. Además, la descripción apunta a una dermatosis contaminada y no necesariamente a acné vulgar. Su relevancia se considera débil e indirecta (grado C).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 34526 | MYCANDEN | Crema x 20 g |
| 2042 | MICOMAZOL | Crema dérmica x 30 g |
| 32028 | MYCANDEN | Spray x 60 ml |
| 20139 | IKOLAN | Crema 1% x 25 g |
| 32425 | MICOSEP | Pasta dérmica x 30 g |

Se muestran las 5 primeras de 9 autorizaciones vigentes, todas de productos de un solo principio activo.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo: no hay estudios que evalúen directamente el clotrimazol en acné, y el único ensayo registrado está suspendido y usa una combinación con corticoide y antibiótico. Por ello el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de ANMAT
- Estudios preclínicos o clínicos que evalúen clotrimazol solo en acné
- Confirmar la relevancia del único ensayo registrado y su indicación real
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

