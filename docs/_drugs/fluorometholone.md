---
layout: default
title: Fluorometholone
parent: Solo Predicción del Modelo (L5)
nav_order: 147
evidence_level: L5
indication_count: 9
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
last_modified_at: 2026-11-25
description: "Fluorometholone: nueva indicación predicha, Vasculitis postinfecciosa (postinfectious vasculitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 4 (en el listado vigente: 4)"
---

# Fluorometholone
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

## Fluorometholone: corticosteroide oftálmico tópico (agonista del receptor de glucocorticoides) → vasculitis postinfecciosa (postinfectious vasculitis)
{: .text-alpha }

## Resumen en Una Frase

Fluorometholona es un corticosteroide oftálmico tópico con efectos antiinflamatorios e inmunosupresores, comercializado en Argentina en suspensiones oftálmicas.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa (postinfectious vasculitis)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Vasculitis postinfecciosa (postinfectious vasculitis) |
| Puntaje de Predicción TxGNN | 0,9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fluorometholone (traducción no oficial): «Los corticosteroides inhiben la respuesta inflamatoria a diversos agentes desencadenantes y probablemente retrasan o enlentecen la cicatrización. Inhiben el edema, el depósito de fibrina, la dilatación capilar, la migración de leucocitos, la proliferación capilar, la proliferación de fibroblastos, el depósito de colágeno y la formación de cicatrices asociados con la inflamación. […] En estudios clínicos de pacientes con respuesta documentada a los esteroides, la fluorometolona demostró un tiempo promedio significativamente más largo para producir un aumento de la presión intraocular que el fosfato de dexametasona; sin embargo, en un pequeño porcentaje de individuos, se produjo un aumento significativo de la presión intraocular en el plazo de una semana.» Texto original en inglés: "Corticosteroids inhibit the inflammatory response to a variety of inciting agents and probably delay or slow healing. They inhibit the edema, fibrin deposition, capillary dilation, leukocyte migration, capillary proliferation, fibroblast proliferation, deposition of collagen, and scar formation associated with inflammation. […] In clinical studies of documented steroid-responders, fluorometholone demonstrated a significantly longer average time to produce a rise in intraocular pressure than dexamethasone phosphate; however, in a small percentage of individuals, a significant rise in intraocular pressure occurred within one week." ([DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01), versión del 2026-08-12; consultado el 2026-11-19). Según la información farmacológica disponible, la fluorometholona actúa sobre el receptor de glucocorticoides (NR3C1), y se usa para tratar la conjuntivitis inflamatoria.

Un glucocorticoide podría, en teoría, atenuar la vasculitis mediada por inmunocomplejos. Sin embargo, la fluorometholona está formulada para uso ocular, con exposición sistémica mínima, por lo que el vínculo con una vasculitis sistémica es débil.

El puntaje del modelo es solo una predicción: no existen ensayos ni literatura que la sustenten. La relación con el uso oftálmico actual es indirecta y requeriría validación preclínica y clínica antes de cualquier consideración.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 11935 | FLAREX | susp.oft.x 5 ml | Novartis | Vigente |
| 241 | F M L LIQUIFILM | susp.oft.x 10 ml | Abbvie | Vigente |
| 242 | F M L NEO LIQUIFILM | susp.oft.x 5 ml | Abbvie | Vigente |

La tabla muestra 3 de los 4 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

FLAREX y F M L LIQUIFILM contienen fluorometolona como único principio activo; F M L NEO LIQUIFILM es una asociación.

<!-- review:begin ar-lic-20261124-fluorometholone-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Las tres autorizaciones están vigentes y son de productos de un solo principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), F M L NEO LIQUIFILM es una asociación de fluorometolona con otros principios activos; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-fluorometholone-1 -->

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron 12 entradas en la consulta, sin nivel de gravedad clasificado (nivel desconocido) para las interacciones con doxiciclina, salbutamol, ciclosporina, paracetamol, digoxina, brimonidina, cefalexina, ácido alendrónico, aciclovir, diazepam y fenofibrato. Además, se registra su unión al receptor de glucocorticoides.
- Por tratarse de un corticosteroide, el uso en infecciones oculares requiere evaluación específica de riesgo-beneficio.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos ni literatura, y la formulación oftálmica con mínima exposición sistémica hace poco plausible su aplicación en una vasculitis sistémica.

**Para avanzar se necesita:**
- Estudios (preclínicos o clínicos) que evalúen directamente la vasculitis postinfecciosa
- Datos del mecanismo de acción y de exposición sistémica con la formulación actual
- Revisión del prospecto de ANMAT para advertencias y contraindicaciones
- Análisis de viabilidad de una vía de administración adecuada para esta indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01) |
| 2026-11-24 | «de un solo principio activo» → F M L NEO LIQUIFILM es asociación | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

