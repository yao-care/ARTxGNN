---
layout: default
title: Carisoprodol
parent: Solo Predicción del Modelo (L5)
nav_order: 83
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Carisoprodol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "CARISOPRODOL"
predicted_indications: ["insomnia (disease)"]
---

# Carisoprodol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Carisoprodol: De Indicación Original No Especificada a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Carisoprodol es un relajante muscular de acción central, comercializado en Argentina en múltiples presentaciones, aunque los datos compilados no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**,
con **0 ensayos clínicos** y **1 publicación** (indirectamente relacionada) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9902 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (10 de 10) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 10 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Carisoprodol (traducción no oficial): «No se ha identificado con claridad el mecanismo de acción del carisoprodol para aliviar las molestias asociadas a afecciones musculoesqueléticas agudas dolorosas. En estudios en animales, la relajación muscular inducida por el carisoprodol se asocia a una alteración de la actividad interneuronal en la médula espinal y en la formación reticular descendente del encéfalo.» Texto original en inglés: "The mechanism of action of carisoprodol in relieving discomfort associated with acute painful musculoskeletal conditions has not been clearly identified. In animal studies, muscle relaxation induced by carisoprodol is associated with altered interneuronal activity in the spinal cord and in the descending reticular formation of the brain." ([DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa), versión del 2026-11-03; consultado el 2026-11-19). Según la información farmacológica general, carisoprodol es un relajante muscular de acción central. Su metabolito activo, el meprobamato, tiene efectos sedantes y ansiolíticos de tipo barbitúrico, y el propio carisoprodol modula los receptores GABA-A. Esto es una inferencia a partir de farmacología general y no proviene de los datos proporcionados.

Esa actividad sedante ofrece una justificación biológica plausible para promover el sueño. Además, los calambres musculares nocturnos pueden alterar el sueño, lo que conecta de forma indirecta el uso como relajante muscular con el insomnio.

Debe tenerse en cuenta que el puntaje de 0.9902 es una predicción computacional y no constituye evidencia clínica. La similitud entre la indicación original y la nueva no pudo evaluarse por falta de datos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Revisión | American Family Physician | Revisión sobre calambres nocturnos en las piernas, que pueden causar insomnio intenso. Trata los calambres, no el tratamiento del insomnio, por lo que la relevancia es solo indirecta |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49423 | LISTAFLEX | Comprimidos x 30 | No especificada |
| 15750 | LISTAFLEX | Comprimidos x 20 | No especificada |
| 40275 | NAPRUX DISTEN | Comprimidos x 30 | No especificada |
| 8367 | FLEXICAMIN | Comprimidos x 20 | No especificada |
| 8258 | SOLOCALM FLEX | Comprimidos x 20 | No especificada |

Se muestran 5 de las 10 autorizaciones vigentes (todas de monofármaco).

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo, úlcera péptica, enfermedad inflamatoria intestinal, hiperplasia prostática benigna, trastornos hipotensivos, gota, abuso/dependencia de sustancias, hemofilia, anemias, colitis por *Clostridium difficile*, paro cardíaco súbito, enfermedades de la conducción cardíaca, insuficiencia respiratoria e insuficiencia suprarrenal (incluida la enfermedad de Addison), entre otras.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las principales:
  - Gravedad **mayor**: morfina y morfina liposomal.
  - Gravedad **moderada**: dronabinol, metoclopramida, nabilona, opio, sibutramina, difenoxina y difenoxilato.
  - Otras interacciones de gravedad no determinada: fentermina, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, metformina, omeprazol, sucralfato, rosiglitazona y lansoprazol.
- **Consideraciones adicionales** (según el análisis de la predicción): potencial de abuso y dependencia, síndrome de abstinencia y depresión aditiva del sistema nervioso central, especialmente combinado con opioides, benzodiacepinas y otros sedantes.

No se dispone de las advertencias ni contraindicaciones del prospecto de ANMAT; consultar el prospecto para completar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos y con una sola publicación de relevancia indirecta. Además, el perfil de seguridad (abuso, dependencia, depresión del SNC e interacciones con opioides y sedantes) pesa de forma importante en contra de un uso hipnótico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada)
- Datos del mecanismo de acción (MOA) desde DrugBank
- Búsqueda de estudios clínicos y literatura específicos sobre carisoprodol o meprobamato en insomnio
- Evaluación del riesgo de abuso y dependencia frente a alternativas existentes para el insomnio
- Análisis de compatibilidad de vía de administración y similitud con la indicación original

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

