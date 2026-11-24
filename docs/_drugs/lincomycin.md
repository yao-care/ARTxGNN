---
layout: default
title: Lincomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
monitor_inn: "lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
last_modified_at: 2026-11-24
description: "Lincomycin: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Lincomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Lincomycin: antibiótico lincosamida → hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Lincomycin (comercializada en Argentina como FRADEMICINA) es un antibiótico de la clase de las lincosamidas, que inhibe la síntesis de proteínas en el ribosoma 50S bacteriano.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0,9914 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lincomycin (traducción no oficial): «La lincomicina inhibe la síntesis de proteínas bacterianas al unirse al ARN 23S de la subunidad 50S del ribosoma bacteriano. La lincomicina es predominantemente bacteriostática in vitro.» Texto original en inglés: "Lincomycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the bacterial ribosome. Lincomycin is predominantly bacteriostatic in vitro." ([DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263), versión del 2025-03-10; consultado el 2026-11-19). Según la información conocida, lincomycin es una lincosamida que inhibe la síntesis proteica bacteriana al unirse a la subunidad ribosomal 50S, y su actividad es antibacteriana.

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre), habitualmente secundario a causas pancreáticas, salivales o renales, y no una enfermedad que un antibiótico trate de forma directa. Con los datos compilados para este informe no se sostiene un vínculo mecanístico plausible entre el fármaco y esta condición.

El puntaje de 0,9914 es el resultado de un modelo computacional y no está corroborado por estudios reales. Cualquier asociación podría reflejar una señal de eventos adversos o un artefacto de confusión más que un efecto terapéutico. Por ello, el puntaje debe interpretarse con cautela y no como prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 6675 | FRADEMICINA | 500 mg caps.x 16 | Janssen-Cilag | Vigente |
| 2276 | FRADEMICINA | 300 mg a.x 4 x 1 ml | Janssen-Cilag | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 21 interacciones registradas. Las de nivel moderado incluyen balsalazida, ácido picosulfúrico, atapulgita, caolín, eritromicina y etinilestradiol. Otras (clotrimazol, cimetidina, morfina, metformina, omeprazol, lactulosa, triamcinolona, simvastatina, ranitidina, warfarina, lidocaína, cetirizina, montelukast, salmeterol) tienen nivel de gravedad no clasificado.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que estudien la hiperamilasemia con lincomycin, y el vínculo mecanístico no es plausible según los datos disponibles. El puntaje 0,9914 corresponde únicamente a una predicción del modelo.

**Para avanzar se necesita:**
- Revisión de la literatura para determinar si la señal corresponde a un evento adverso o a un artefacto de confusión
- Datos del prospecto de ANMAT (advertencias y contraindicaciones)
- Datos detallados del mecanismo de acción y de su posible relación con la condición predicha
- Estudios preclínicos o clínicos que evalúen directamente la hiperamilasemia antes de reconsiderar la decisión

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

