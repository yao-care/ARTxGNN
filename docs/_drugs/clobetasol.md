---
layout: default
title: Clobetasol
parent: Evidencia Moderada (L3-L4)
nav_order: 112
evidence_level: L3
indication_count: 1
last_modified_at: 2026-11-25
description: "Clobetasol: nueva indicación predicha, Linfoma cutáneo primario de células T (nivel de evidencia L3). Indicación original: No disponible en los registros de ANMAT compilados (todos los textos…"
monitor_inn: "CLOBETASOL"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Clobetasol
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

## Clobetasol: De Indicación Original No Registrada a Linfoma Cutáneo Primario de Células T
{: .text-alpha }

## Resumen en Una Frase

Clobetasol es un corticosteroide tópico de muy alta potencia, comercializado en Argentina en cremas, ungüentos, lociones, champús y espuma. Los registros de ANMAT compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **linfoma cutáneo primario de células T**, con **0 ensayos clínicos** y **15 publicaciones** que respaldan esta dirección. Cabe aclarar que el uso tópico en micosis fungoide en estadio temprano ya está descrito en la literatura, por lo que se trata más de respaldar un uso existente que de un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros de ANMAT compilados (todos los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Linfoma cutáneo primario de células T |
| Puntaje de Predicción TxGNN | 0,9951 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clobetasol (traducción no oficial): «Al igual que otros corticosteroides tópicos, el propionato de clobetasol tiene propiedades antiinflamatorias, antipruriginosas y vasoconstrictoras. En general, el mecanismo de la actividad antiinflamatoria de los esteroides tópicos no está claro.» Texto original en inglés: "Like other topical corticosteroids, clobetasol propionate has anti-inflammatory, antipruritic, and vasoconstrictive properties. The mechanism of the anti-inflammatory activity of the topical steroids, in general, is unclear." ([DailyMed: Clobetasol Propionate (Emollient) (clobetasol propionate) prescribing information, The J. Molner Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=26ccb1d8-c466-e238-e063-6394a90a0069), versión del 2026-11-10; consultado el 2026-11-19). Según la farmacología general, el clobetasol propionato es un corticosteroide tópico de potencia muy alta que actúa activando el receptor de glucocorticoides, con efectos antiinflamatorios e inmunosupresores. Estos efectos pueden además inducir apoptosis de linfocitos T, tanto malignos como reactivos, en la piel.

En el linfoma cutáneo primario de células T, y en particular en la micosis fungoide (su variante más común), la carga de linfocitos T en la lesión es el blanco terapéutico. Por ello, reducirla en lesiones en parche o placa es mecanísticamente plausible. Esta explicación es una inferencia de farmacología general y no proviene del registro suministrado.

La literatura describe a los corticosteroides tópicos como terapia dirigida a la piel ya establecida en la enfermedad temprana. Un informe de la UCSF con unos 200 pacientes reporta respuestas superiores al 90 % y señala al clobetasol tópico como tratamiento de primera línea en micosis fungoide temprana. El puntaje alto de TxGNN es coherente con esto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se priorizan los estudios de cohorte y observacionales sobre los reportes de caso (no hay ECA ni revisiones sistemáticas en los datos).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14686970](https://pubmed.ncbi.nlm.nih.gov/14686970/) | 2003 | Cohorte | Dermatologic Therapy | Experiencia de la UCSF con corticosteroides tópicos de alta potencia en micosis fungoide en estadio parche (~200 pacientes). Respuesta >90 %, efectos adversos menores; clobetasol es tratamiento de primera línea |
| [32603400](https://pubmed.ncbi.nlm.nih.gov/32603400/) | 2020 | Cohorte (observacional) | Cutis | Evaluación del riesgo de efectos adversos cutáneos con clobetasol crema 0,05 % en micosis fungoide temprana, ante la necesidad de tratamiento prolongado |
| [39741016](https://pubmed.ncbi.nlm.nih.gov/39741016/) | 2025 | Cohorte | Anais Brasileiros de Dermatologia | Comparación de eficacia entre clobetasol propionato y bexaroteno en micosis fungoide temprana |
| [25027222](https://pubmed.ncbi.nlm.nih.gov/25027222/) | 2014 | Reporte de caso | Ned Tijdschr Geneeskd | Niña de 9 años con micosis fungoide hipopigmentada tratada con éxito con clobetasol 0,05 % en ungüento 4 días por semana |
| [8987063](https://pubmed.ncbi.nlm.nih.gov/8987063/) | 1996 | Serie de casos | Pediatric Dermatology | Papulosis linfomatoide en tres niños tratados con corticosteroides tópicos superpotentes en pulsos semanales |
| [28031140](https://pubmed.ncbi.nlm.nih.gov/28031140/) | 2016 | Reporte de caso | Skinmed | Linfoma angioinmunoblástico de células T con presentación cutánea; empeoró bajo metotrexato y clobetasol tópico, tratado inicialmente como psoriasis |
| [36846176](https://pubmed.ncbi.nlm.nih.gov/36846176/) | 2023 | Reporte de caso | Clinical Case Reports | Micosis fungoide con placas psoriasiformes, inicialmente confundida con psoriasis y sin respuesta a esteroides tópicos |
| [23773745](https://pubmed.ncbi.nlm.nih.gov/23773745/) | 2013 | Reporte de caso | Ann Dermatol Venereol | Micosis fungoide papular, nueva forma de enfermedad incipiente, con revisión de la literatura |

Las demás publicaciones recuperadas son reportes de caso sobre diagnóstico diferencial o variantes de linfoma cutáneo, con relevancia limitada para la eficacia del clobetasol.

---

## Información de Mercado en Argentina

Las autorizaciones recopiladas en los datos están vigentes y son todas de producto único; los datos solo incluyen una parte de los productos (las cifras están en el resumen rápido). Ninguna tiene texto de indicación aprobada en los registros.

<!-- review:begin ar-lic-20261125b-clobetasol-1 -->

> **Corrección de verificación (2026-11-25)**: Texto original: «Se listan 5 de las 20 autorizaciones vigentes (todas de producto único).» Corregido: los datos de este medicamento solo incluyen una parte de los productos del listado de PAMI, y la frase daba como total o como número de filas mostradas una cifra fija que no coincide con ellos. Las cifras actuales están en el resumen rápido y en la tabla de Información de Mercado en Argentina. El estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261125b-clobetasol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 43829 | SALAC | shamp.x 140 ml | Andrómaco | Vigente |
| 28767 | RIBATRA | 0.05% loc.x 30 ml | Panalab | Vigente |
| 23212 | SALAC | cr.x 20 g | Andrómaco | Vigente |
| 28765 | RIBATRA | 0.05% cr.x 30 g | Panalab | Vigente |
| 44511 | CLOBESOL | cr.x 20 g | Siegfried | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Todas las presentaciones son de uso tópico (cremas, ungüentos, lociones, champús y espuma).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones identificó 100 posibles interacciones, sin nivel de gravedad clasificado. Entre las listadas figuran otros corticosteroides (triamcinolona, prednisona, prednisolona, hidrocortisona), calcitriol, vitamina A, inhibidores de la bomba de protones (omeprazol, pantoprazol, lansoprazol), doxiciclina, clotrimazol y metronidazol, entre otros. La relevancia clínica de estas interacciones con el uso tópico no está establecida.
- **Efectos adversos cutáneos**: la literatura señala que el tratamiento prolongado de una enfermedad crónica plantea preocupación por efectos adversos cutáneos inducidos por corticosteroides, aunque los efectos secundarios descritos en micosis fungoide temprana son menores.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La literatura observacional (cohortes y series de casos) respalda el uso de clobetasol tópico en micosis fungoide temprana, con un puntaje TxGNN muy alto (0,9951). No hay ensayos clínicos registrados ni ECA, por lo que el nivel de evidencia es L3 y se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), un vacío que bloquea la evaluación de seguridad.
- Confirmar las indicaciones aprobadas en Argentina, ya que los textos de indicación están vacíos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar estudios comparativos o ECA en micosis fungoide temprana.
- Definir un plan de monitoreo de efectos adversos cutáneos y de absorción sistémica con el uso prolongado.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Clobetasol Propionate (Emollient) (clobetasol propionate) prescribing information, The J. Molner Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=26ccb1d8-c466-e238-e063-6394a90a0069) |
| 2026-11-25 | «5 de las 20» → sin cifra | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

