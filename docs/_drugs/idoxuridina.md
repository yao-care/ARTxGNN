---
layout: default
title: Idoxuridina
parent: Solo Predicción del Modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
drugbank_id: DB00249
monitor_inn: "Idoxuridine"
predicted_indications: ["vulvovaginal candidiasis", "vaginitis (disease)", "trichomonal vulvovaginitis", "vulvitis", "herpetic vulvovaginitis", "vaginal discharge", "bacterial vaginosis", "leukoplakia of vagina", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-20
description: "Idoxuridina: nueva indicación predicha, candidiasis vulvovaginal (vulvovaginal candidiasis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Idoxuridina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Idoxuridina: candidiasis vulvovaginal (vulvovaginal candidiasis)
{: .text-alpha }

## Resumen en Una Frase

Idoxuridina es un análogo de la timidina que inhibe la síntesis de ADN viral y se comercializa en Argentina en formas de uso tópico (gotas y ungüento dérmico).
El modelo TxGNN predice que podría ser efectiva para **candidiasis vulvovaginal (vulvovaginal candidiasis)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | candidiasis vulvovaginal (vulvovaginal candidiasis) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Idoxuridina es (traducción no oficial): «Inhibidor del ADN». Texto original en inglés: "DNA inhibitor" ([ChEMBL CHEMBL788 (idoxuridine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL788), CC BY-SA 3.0; consultado el 2026-11-19). Por conocimiento general, la idoxuridina es un análogo de la timidina que se incorpora al ADN viral e inhibe su replicación, por lo que su actividad es antiviral.

*Candida*, el agente habitual de la candidiasis vulvovaginal, es un hongo. La idoxuridina no tiene actividad antifúngica reconocida, de modo que no se identifica un vínculo mecanístico plausible con esta enfermedad.

El puntaje muy alto (0,9992) probablemente refleja la cercanía del modelo entre enfermedades vulvovaginales y no una señal biológica. Esta predicción debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para candidiasis vulvovaginal.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 2930 | IDULEA CON ADHEFILM | Gotas, 10 ml |
| 2931 | IDULEA | Ungüento dérmico, 10 g |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se obtuvieron datos de advertencias, contraindicaciones ni interacciones farmacológicas para este informe.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe la idoxuridina en candidiasis vulvovaginal, y su mecanismo antiviral no explica un efecto sobre un hongo. El puntaje alto parece un artefacto del modelo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia de actividad antifúngica frente a *Candida* (estudios in vitro)
- Prospecto de ANMAT con advertencias y contraindicaciones
- Evaluación de la compatibilidad de las formas de uso tópico disponibles con la vía requerida
- Comparación con los tratamientos antifúngicos ya establecidos

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; versión anterior conservada en el registro) | [ChEMBL CHEMBL788 (idoxuridine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL788) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

