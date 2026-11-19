---
layout: default
title: Calcitriol
parent: Solo Predicción del Modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-20
description: "Calcitriol: nueva indicación predicha, Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 3 (en el listado vigente: 3)"
---

# Calcitriol
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

## Calcitriol: análogo activo de la vitamina D (agonista del receptor de vitamina D) → Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency)
{: .text-alpha }

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D, comercializada en Argentina en cápsulas.
El modelo TxGNN predice que podría ser efectivo para **Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency) |
| Puntaje de Predicción TxGNN | 0,9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Calcitriol (traducción no oficial): «La síntesis endógena y el catabolismo del calcitriol, así como los mecanismos de control fisiológico que afectan a estos procesos, desempeñan un papel fundamental en la regulación de la concentración sérica de calcitriol. La producción diaria fisiológica es normalmente de 0.5 a 1.0 mcg y es algo mayor durante los períodos de aumento de la síntesis ósea (p. ej., crecimiento o embarazo).» Texto original en inglés: "Endogenous synthesis and catabolism of calcitriol, as well as physiological control mechanisms affecting these processes, play a critical role regulating the serum level of calcitriol. Physiological daily production is normally 0.5 to 1.0 mcg and is somewhat higher during periods of increased bone synthesis (eg, growth or pregnancy)." ([DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e), versión del 2026-10-15; consultado el 2026-11-19). Según la información conocida, calcitriol es la forma activa (1,25-dihidroxivitamina D3) de la vitamina D y actúa sobre el metabolismo del calcio y del fosfato.

Dado que calcitriol es el metabolito activo de la vitamina D, una predicción relacionada con la deficiencia de vitamina D es biológicamente verosímil. Sin embargo, el término de la enfermedad está marcado como obsoleto, por lo que probablemente corresponde a una entrada desactualizada de la ontología y no a una entidad clínica vigente.

Además, para la deficiencia nutricional de vitamina D se usan habitualmente colecalciferol o ergocalciferol y no la forma activa. El puntaje alto del modelo refleja solo una predicción, no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta predicción.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta predicción.

## Información de Mercado en Argentina

El medicamento figura como comercializado, con 3 autorizaciones vigentes de productos de un solo principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46020 | CALCIRAQUIFEROL | Cápsulas blandas x 30 | No registrada en los datos locales |
| 7483 | CALCITRIOL | 0,25 mcg, cápsulas x 30 | No registrada en los datos locales |
| 24450 | CALCITRIOL MEGALABS | Cápsulas x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; principales):
  - Gravedad mayor: colecalciferol, burosumab, calcifediol.
  - Gravedad moderada: fosfenitoína, hidroclorotiazida y otras tiazidas (bendroflumetiazida, benztiazida, clorotiazida, clortalidona), barbitúricos (amobarbital, butalbital, butabarbital), carbamazepina, hidróxido de aluminio, calcipotriol tópico, resinas quelantes (colestiramina, colesevelam, colestipol) y digitálicos (digitoxina, digoxina).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no cuenta con ensayos clínicos ni literatura, el término de la enfermedad está marcado como obsoleto y, para la deficiencia nutricional, se prefieren otras formas de vitamina D. Solo existe una predicción del modelo (nivel L5).

**Para avanzar se necesita:**
- Aclarar a qué entidad clínica vigente corresponde el término obsoleto de la predicción.
- Estudios o literatura que evalúen directamente calcitriol en esa condición frente a colecalciferol o ergocalciferol.
- Datos del mecanismo de acción y del prospecto local (advertencias y contraindicaciones).

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

