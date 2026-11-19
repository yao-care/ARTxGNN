---
layout: default
title: Mesalazina
parent: Solo Predicción del Modelo (L5)
nav_order: 247
evidence_level: L5
indication_count: 6
drugbank_id: DB00244
monitor_inn: "Mesalazine"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
last_modified_at: 2026-11-16
description: "Mesalazina: nueva indicación predicha, hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy) (nivel de evidencia L5)."
---

# Mesalazina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Mesalazina: hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy)
{: .text-alpha }

## Resumen en Una Frase

Mesalazina (ácido 5-aminosalicílico) es un antiinflamatorio aminosalicilato que se comercializa en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectiva para **hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy) |
| Puntaje de Predicción TxGNN | 0.9965 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Mesalazina (traducción no oficial): «El mecanismo de acción de la mesalamina no se conoce por completo, pero parece tener un efecto antiinflamatorio tópico sobre las células epiteliales del colon. La producción mucosa de metabolitos del ácido araquidónico, tanto por la vía de la ciclooxigenasa como por la de la lipooxigenasa, está aumentada en los pacientes con colitis ulcerosa, y es posible que la mesalamina disminuya la inflamación al bloquear la ciclooxigenasa e inhibir la producción de prostaglandinas en el colon.» Texto original en inglés: "The mechanism of action of mesalamine is not fully understood, but it appears to have a topical anti-inflammatory effect on the colonic epithelial cells. Mucosal production of arachidonic acid metabolites, both through the cyclooxygenase and lipoxygenase pathways, is increased in patients with ulcerative colitis, and it is possible that mesalamine diminishes inflammation by blocking cyclooxygenase and inhibiting prostaglandin production in the colon." ([DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7), versión del 2026-10-26; consultado el 2026-11-19). En términos generales, la mesalazina es un aminosalicilato con acción antiinflamatoria (inhibición de vías de ciclooxigenasa y lipooxigenasa, activación de PPAR-gamma y modulación de NF-kB).

La enfermedad predicha es un trastorno monogénico ultra raro, asociado a mutaciones en CDH3 que afectan la adhesión celular. No se identifica un vínculo mecanístico plausible entre la acción antiinflamatoria de la mesalazina y esta fisiopatología.

El puntaje de TxGNN es alto (0,9965), pero se trata únicamente de una predicción computacional, sin respaldo clínico ni bibliográfico. Debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

La mesalazina tiene al menos 20 autorizaciones vigentes en Argentina (la lista puede ser parcial). Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 18874 | PENTASA | 500 mg comprimidos x 50 | No registrada en los datos locales |
| 18875 | PENTASA | 500 mg comprimidos x 100 | No registrada en los datos locales |
| 11105 | 5-ASA 400 | 400 mg comprimidos x 30 | No registrada en los datos locales |
| 33568 | YOLECOL | 800 mg comprimidos x 60 | No registrada en los datos locales |
| 53164 | 5-ASA 1000 | 1 g sobres x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional: no hay ensayos clínicos, no hay literatura y no se identifica un vínculo mecanístico plausible con una enfermedad genética ultra rara de adhesión celular.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la mesalazina para analizar posibles vínculos con la vía de CDH3
- Estudios preclínicos que respalden alguna relación biológica con esta enfermedad
- Información de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Evaluación de la compatibilidad de vías de administración, hoy pendiente

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lialda (mesalamine) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3098a080-be86-4265-9818-7fc4beab77b7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

