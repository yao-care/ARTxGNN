---
layout: default
title: Doxiciclina
parent: Solo Predicción del Modelo (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
drugbank_id: DB00254
monitor_inn: "Doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
last_modified_at: 2026-11-16
description: "Doxiciclina: nueva indicación predicha, queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 9 (en el listado vigente: 9)"
---

# Doxiciclina
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

## Doxiciclina: queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Doxiciclina es un antibiótico de la familia de las tetraciclinas, comercializado en Argentina. El modelo TxGNN predice que podría ser efectiva para **queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)**, pero actualmente solo existe **1 publicación** (un reporte de casos de 1992) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (9 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Doxiciclina (traducción no oficial): «La doxiciclina inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosómica 30S. La doxiciclina tiene actividad bacteriostática contra una amplia variedad de bacterias grampositivas y gramnegativas.» Texto original en inglés: "Doxycycline inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit. Doxycycline has bacteriostatic activity against a broad range of Gram-positive and Gram-negative bacteria." ([DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8), versión del 2026-07-09; consultado el 2026-11-19). Según la información conocida, la doxiciclina es una tetraciclina con actividad frente a *Chlamydia trachomatis*, y se le atribuyen además efectos antiinflamatorios y de inhibición de metaloproteinasas de matriz (MMP) en la superficie ocular.

La única publicación disponible describe dos casos de queratitis epitelial punteada persistente tras la resolución de una conjuntivitis folicular por clamidia, tratada inicialmente con tetraciclina o doxiciclina. Las lesiones reaparecieron después de que los folículos se resolvieron, lo que sugiere un componente inmunomediado que un antibiótico podría no abordar.

Mecanísticamente la hipótesis es plausible (efecto antiinflamatorio sobre la superficie ocular), pero no hay ensayos ni evidencia clínica directa de beneficio. El puntaje alto del modelo es una predicción computacional, no una prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Reporte de casos | Cornea | Dos casos de queratitis epitelial punteada recurrente y bilateral tras conjuntivitis folicular por clamidia, tratada con tetraciclina o doxiciclina; las lesiones persistieron después de resolverse los folículos |

Esta publicación describe una condición relacionada, pero no demuestra un beneficio de la doxiciclina sobre la queratoconjuntivitis epitelial punteada. Por ello el nivel de evidencia se establece en L5.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 23754 | VERBORIL | 100 mg comp. rec. x 8 | No registrada |
| 9887 | VIBRAMICINA | 100 mg tab. x 16 | No registrada |
| 23502 | DOXIBIOT | 100 mg comp. x 10 | No registrada |
| 31677 | ASOLMICINA.DOX | 100 mg comp. rec. x 15 | No registrada |
| 10048 | VIBRAMICINA | 100 mg tab. x 5 | No registrada |

Se listan las 5 primeras autorizaciones; todas las autorizaciones registradas son de producto de un solo principio activo y se encuentran vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero solo cuenta con un reporte de casos de 1992 y ningún ensayo clínico. No hay evidencia directa de que la doxiciclina beneficie esta enfermedad.

**Para avanzar se necesita:**
- Estudios clínicos (idealmente ensayos controlados) que evalúen la doxiciclina en queratoconjuntivitis epitelial punteada
- Datos del mecanismo de acción y de la plausibilidad inmunomediada en superficie ocular
- Definir la vía de administración (sistémica u ocular) y evaluar su compatibilidad con las presentaciones disponibles en Argentina
- Obtener la información de advertencias y contraindicaciones del prospecto de ANMAT para una evaluación de seguridad

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

