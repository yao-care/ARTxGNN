---
layout: default
title: Ginseng
parent: Solo Predicción del Modelo (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Ginseng: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los registros (las autorizaciones no incluyen texto…"
monitor_inn: "GINSENG"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy", "amenorrhea (disease)", "immature cataract", "craniostenosis cataract"]
---

# Ginseng
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

## Ginseng: De Indicación Original No Especificada a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Ginseng es un producto de origen vegetal comercializado en Argentina en 6 autorizaciones de producto único, para el cual los registros disponibles no detallan una indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero esta predicción no cuenta con ensayos clínicos ni publicaciones que la respalden.
Entre las demás indicaciones predichas, la **retinopatía diabética** es la que reúne más literatura (20 publicaciones, casi todas preclínicas o revisiones, y un estudio clínico prospectivo de 2026).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 0,9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 6 de 6) |
| Número de Autorizaciones | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

> Nota: la indicación con mayor respaldo en la literatura es la retinopatía diabética (nivel L3, puntaje TxGNN 0,9955), que se describe más abajo como alternativa prioritaria.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, Ginseng es un extracto vegetal cuyos principios activos son los ginsenósidos. Se les atribuyen efectos antioxidantes, antiinflamatorios y moduladores del metabolismo, y se ha propuesto que podrían influir en la remodelación ósea. Sin embargo, los datos compilados para este informe no incluyen evidencia que sustente esta hipótesis.

El puntaje del modelo es muy alto (0,9995), pero se trata únicamente de una predicción computacional. No hay ensayos ni publicaciones vinculados a la osteoporosis inducida por fármacos, y tampoco se dispone de una indicación original con la cual comparar similitud.

Para la **retinopatía diabética**, la hipótesis es más sólida: múltiples estudios preclínicos describen que los ginsenósidos Rg1, Rg3, Rd y Re actúan sobre la lesión endotelial retiniana mediante las vías AMPK, estrés del retículo endoplásmico/ROS, efectos antiangiogénicos y antipiroptosis. Un estudio prospectivo de 2026 en humanos aporta una señal clínica inicial.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para osteoporosis inducida por fármacos.

Como dato contextual, para otra indicación predicha (enfermedad hemorrágica del recién nacido) existe un ensayo que no aporta evidencia para esa indicación:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00719563](https://clinicaltrials.gov/study/NCT00719563) | Fase 3 | Completado | 364 | Ginseng americano vs. placebo en fatiga relacionada con el cáncer; solo aporta información general de seguridad y tolerabilidad en adultos |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para osteoporosis inducida por fármacos.

A modo de referencia, estas son las publicaciones más relevantes para la indicación con mayor respaldo (retinopatía diabética):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42395017](https://pubmed.ncbi.nlm.nih.gov/42395017/) | 2026 | Estudio clínico prospectivo, aleatorizado y doble ciego | J Ginseng Res | Efecto del extracto de ginseng rojo coreano sobre los parámetros del plexo capilar profundo en retinopatía diabética |
| [32095091](https://pubmed.ncbi.nlm.nih.gov/32095091/) | 2020 | Revisión | J Ginseng Res | Efectos del ginseng en enfermedades oculares, incluidas retinopatía diabética, cataratas y glaucoma |
| [34583224](https://pubmed.ncbi.nlm.nih.gov/34583224/) | 2021 | Revisión | Phytomedicine | Fitoquímica, farmacocinética y efecto antidiabético del ginseng |
| [39892311](https://pubmed.ncbi.nlm.nih.gov/39892311/) | 2025 | Revisión | Phytomedicine | Ginseng y piroptosis en la diabetes y sus complicaciones crónicas |
| [41067201](https://pubmed.ncbi.nlm.nih.gov/41067201/) | 2025 | Revisión | Phytomedicine | Efectos y mecanismos de los ginsenósidos sobre la angiogénesis |
| [22566158](https://pubmed.ncbi.nlm.nih.gov/22566158/) | 2013 | Preclínico (animal) | Phytother Res | El ginseng norteamericano previene la retinopatía y la miocardiopatía diabéticas en modelos de ratón |
| [39579577](https://pubmed.ncbi.nlm.nih.gov/39579577/) | 2024 | Preclínico (ratón T2DM) | Phytomedicine | Rg3 alivia la lesión retiniana diabética mediante el eje Nrf2/HO-1 |
| [32309379](https://pubmed.ncbi.nlm.nih.gov/32309379/) | 2020 | Preclínico (animal) | Ann Transl Med | Rg1 previene la retinopatía diabética temprana reduciendo la apoptosis celular en ratones db/db |
| [35150861](https://pubmed.ncbi.nlm.nih.gov/35150861/) | 2022 | Preclínico (in vitro) | Pharmacol Res | Ginsenósido Rd protege el endotelio retiniano frente a alta glucosa vía AMPK |
| [41164346](https://pubmed.ncbi.nlm.nih.gov/41164346/) | 2025 | Farmacología de redes | Appl Bionics Biomech | Compuestos bioactivos y dianas moleculares del ginseng en retinopatía diabética |

Para acné, la única publicación es un estudio preclínico/in vitro de 2019 ([30506753](https://pubmed.ncbi.nlm.nih.gov/30506753/), Phytother Res) sobre las propiedades antiacné de la fracción hidrofóbica del ginseng rojo.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 15431 | TANVIMIL GINSENG | Cápsulas x 60 | No especificada |
| 18042 | MARATHON | Cápsulas x 60 | No especificada |
| 45694 | TOTAL MAGNESIANO GINSENG | Polvo en sobres x 30 | No especificada |
| 18041 | MARATHON | Cápsulas x 30 | No especificada |
| 31593 | MARATHON | Cápsulas x 20 | No especificada |

Existe una sexta autorización vigente (15430, TANVIMIL GINSENG, cápsulas x 30). Las 6 autorizaciones son de producto único y están vigentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 83 interacciones, todas de nivel moderado en los registros mostrados. Destacan los **antidiabéticos**: acarbosa, metformina, pioglitazona, glimepirida, clorpropamida, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), inhibidores de DPP-4 (alogliptina, linagliptina), agonistas de GLP-1 (albiglutida, dulaglutida, semaglutida, lixisenatida) y diversas insulinas (aspart, degludec, detemir, glargina, glulisina). También interactúa con el **ácido acetilsalicílico**. En general, conviene vigilar el riesgo de hipoglucemia al combinar con antidiabéticos.
- **Consideración adicional**: para la indicación de enfermedad hemorrágica del recién nacido se señalan preocupaciones por posibles efectos antiplaquetarios y anticoagulantes, lo que plantea dudas de seguridad en neonatos.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para osteoporosis inducida por fármacos solo existe una predicción del modelo (nivel L5), sin ensayos ni literatura. La retinopatía diabética es la indicación más prometedora (nivel L3, pregunta de investigación formal), pero su evidencia es sobre todo preclínica y falta un ECA confirmatorio.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas) para completar el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Para osteoporosis: revisión de literatura y estudios preclínicos que sustenten la hipótesis
- Para retinopatía diabética: ECA de mayor tamaño que confirme el estudio de 2026, con evaluación de la interacción con antidiabéticos
- Definir la compatibilidad de vía de administración y la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

