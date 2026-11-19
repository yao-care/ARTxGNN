---
layout: default
title: Fluorometholone
parent: Solo Predicción del Modelo (L5)
nav_order: 147
evidence_level: L5
indication_count: 9
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
last_modified_at: 2026-10-30
description: "Fluorometholone: nueva indicación predicha, Vasculitis postinfecciosa (postinfectious vasculitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 3 (en el listado vigente: 3)"
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
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 3 (vigentes: 3) |
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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11935 | FLAREX | Suspensión oftálmica x 5 ml |
| 241 | F M L LIQUIFILM | Suspensión oftálmica x 10 ml |
| 242 | F M L NEO LIQUIFILM | Suspensión oftálmica x 5 ml |

Las tres autorizaciones están vigentes y son de productos de un solo principio activo.

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

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

