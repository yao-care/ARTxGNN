---
layout: default
title: Allopurinol
parent: Solo Predicción del Modelo (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-30
description: "Allopurinol: nueva indicación predicha, porfiria hepática (hepatic porphyria) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Allopurinol
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

## Alopurinol: inhibidor de la xantina oxidasa → porfiria hepática (hepatic porphyria)
{: .text-alpha }

## Resumen en Una Frase

Alopurinol es un inhibidor de la xantina oxidasa que se comercializa en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática (hepatic porphyria)**,
pero actualmente **no hay ensayos clínicos** y solo **2 publicaciones** indirectamente relacionadas (una hipótesis y un estudio en ratas) respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | porfiria hepática (hepatic porphyria) |
| Puntaje de Predicción TxGNN | 0,9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Allopurinol (traducción no oficial): «El alopurinol es un análogo estructural de la base púrica natural hipoxantina. El alopurinol y su metabolito oxipurinol inhiben la xantina oxidasa, la enzima responsable de la conversión de hipoxantina en xantina y de xantina en ácido úrico, el producto final del metabolismo de las purinas en los seres humanos.» Texto original en inglés: "Allopurinol is a structural analogue of the natural purine base, hypoxanthine. Allopurinol and its oxypurinol metabolite inhibitor xanthine oxidase, the enzyme responsible for the conversion of hypoxanthine to xanthine and of xanthine to uric acid, the end product of purine metabolism in humans." ([DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449), versión del 2022-02-18; consultado el 2026-11-19). Según la información conocida, alopurinol inhibe la xantina oxidasa, enzima clave en la producción de ácido úrico.

La relación con la porfiria hepática es incierta. Un artículo de hipótesis de 2019 propone dirigirse al metabolismo del hemo (5-aminolevulinato sintasa y utilización del hemo por la triptófano 2,3-dioxigenasa) como terapia de las porfirias hepáticas agudas. Ese trabajo no estudia el alopurinol y no aporta datos clínicos.

Además, en la literatura experimental antigua se describe que alopurinol podría perturbar el metabolismo del hemo hepático, por lo que la dirección del efecto es incierta y podría ser perjudicial. Esta posible señal de seguridad debe resolverse antes de cualquier consideración clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisión (hipótesis) | Medical Hypotheses | Propone la regulación metabólica de la 5-ALAS mediante triptófano o inhibidores de la TDO como terapia de porfirias hepáticas agudas; no evalúa alopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclínico (animal) | Biochemical Pharmacology | Carbamazepina a dosis muy bajas agrava el metabolismo del hemo en hígado de rata, con relevancia para el mecanismo de exacerbación de porfirias; relación solo indirecta con alopurinol. |

Ninguno de estos estudios evalúa directamente el alopurinol en porfiria hepática, por lo que el nivel de evidencia se mantiene en L5.

## Información de Mercado en Argentina

El listado de autorizaciones puede ser parcial. Se registran al menos 20 autorizaciones vigentes de productos de un solo principio activo.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 48995 | ALLOPURINOL 300 CRAVERI | 300 mg comp. x 60 | Craveri |
| 49651 | ALLOPURINOL GADOR RETARD | 300 mg comp. x 30 | Gador |
| 22580 | PURITENK | 300 mg comp. x 20 | Biotenk |
| 35535 | ALLOPURINOL GADOR | 100 mg comp. x 30 | Gador |
| 44167 | COLPURIL A RETARD | cáps. con microgránulos x 50 | Siegfried |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (se registraron 100 interacciones; se muestran las de nivel moderado): hidróxido de aluminio, attapulgita, caolín, magaldrato y sucralfato.
- Interacciones de nivel menor: amoxicilina y clorpropamida.
- **Señal de seguridad específica**: en la literatura experimental antigua el alopurinol se ha descrito como un agente que puede perturbar el metabolismo del hemo; esto es especialmente relevante en una enfermedad como la porfiria.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en literatura indirecta (una hipótesis y un estudio animal con otro fármaco). No hay estudios que evalúen directamente el alopurinol en porfiria hepática, y existe una posible señal de seguridad por perturbación del metabolismo del hemo.

**Para avanzar se necesita:**
- Revisión sistemática de la evidencia preclínica y clínica sobre el efecto del alopurinol en el metabolismo del hemo y su carácter porfirinogénico.
- Datos detallados del mecanismo de acción y de las advertencias y contraindicaciones del prospecto aprobado por ANMAT.
- Estudios preclínicos específicos en modelos de porfiria hepática antes de considerar ensayos clínicos.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

