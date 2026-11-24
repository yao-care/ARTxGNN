---
layout: default
title: Celecoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Celecoxib: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide"
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
---

# Celecoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Celecoxib: De Artritis Reumatoide a Displasia Acromesomélica tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Celecoxib es un antiinflamatorio no esteroideo (inhibidor selectivo de la COX-2), utilizado originalmente para tratar enfermedades articulares inflamatorias como la artritis reumatoide, la espondilitis anquilosante y la artrosis.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, una displasia esquelética rara de origen genético.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que se apoya únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según la base de conocimiento; el registro local no detalla el texto de indicación) |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Celecoxib (traducción no oficial): «El celecoxib tiene propiedades analgésicas, antiinflamatorias y antipiréticas. Se cree que el mecanismo de acción del celecoxib se debe a la inhibición de la síntesis de prostaglandinas, principalmente mediante la inhibición de la COX-2. El celecoxib es un potente inhibidor de la síntesis de prostaglandinas in vitro.» Texto original en inglés: "Celecoxib has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of celecoxib is believed to be due to inhibition of prostaglandin synthesis, primarily via inhibition of COX-2. Celecoxib is a potent inhibitor of prostaglandin synthesis in vitro." ([DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d), versión del 2025-07-31; consultado el 2026-11-19). Según la información conocida, celecoxib es un inhibidor selectivo de la COX-2 que reduce la inflamación y el dolor mediados por prostaglandinas. Su eficacia en enfermedades articulares inflamatorias está comprobada.

Sin embargo, el análisis mecanístico **no encuentra un vínculo claro** con la nueva indicación. La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético raro causado por variantes de pérdida de función en *CDMP1/GDF5*, que alteran la señalización de un factor de crecimiento. La inhibición de la COX-2 no corrige ese defecto.

El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, derivadas de características musculoesqueléticas compartidas, y no evidencia biológica. Esta predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 23356 | CELEBREX | 200 mg cáps.x 20 | Aspen Pharma | Vigente |

La tabla muestra el único producto de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según la base de conocimiento, no el prospecto)**:
  - Cardiovasculares: hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, enfermedad cardiovascular, enfermedad cerebrovascular y accidente cerebrovascular.
  - Digestivas: úlcera péptica (incluida la activa) y enfermedad de la vesícula biliar.
  - Renales y hepáticas: enfermedad renal y enfermedad hepática.
  - Respiratorias: asma (intrínseca y alérgica).
  - Hematológicas: anemia y hemoglobinopatías.
  - Otras: abuso o dependencia de sustancias.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total.
  - Interacción **mayor**: eliglustat.
  - Interacciones **moderadas** destacadas: hidrocortisona, metformina, antidiabéticos sulfonilureicos (glimepirida, glipizida, glibenclamida, clorpropamida, acetohexamida), nateglinida, exenatida, cimetidina, levofloxacino, metronidazol, naltrexona, kanamicina, y salicilatos de colon (mesalazina, balsalazida, olsalazina).

Para las advertencias formales, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible. El puntaje alto del modelo parece un artefacto de red y no justifica avanzar. Como contexto, entre las demás predicciones de este análisis, la de *espondilopatía inflamatoria* (nivel L1, con ensayos de Fase 3 y 4 completados) corresponde a una indicación que celecoxib ya cubre, por lo que valida un uso existente y no es un reposicionamiento real.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de ANMAT.
- Estudios preclínicos que muestren alguna relación entre la inhibición de la COX-2 y la señalización de GDF5/CDMP1.
- Priorizar otras predicciones del análisis con mayor respaldo antes de invertir recursos en esta.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

