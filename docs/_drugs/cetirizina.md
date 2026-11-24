---
layout: default
title: Cetirizina
parent: Solo Predicción del Modelo (L5)
nav_order: 95
evidence_level: L5
indication_count: 3
drugbank_id: DB00341
monitor_inn: "Cetirizine"
predicted_indications: ["nasal cavity disease", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
last_modified_at: 2026-11-24
description: "Cetirizina: nueva indicación predicha, enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 18 (en el listado vigente: 18)"
---

# Cetirizina
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

## Cetirizina: enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Cetirizina es un antihistamínico de segunda generación que actúa bloqueando el receptor H1 de histamina.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal (nasal cavity disease)**, pero actualmente no hay ensayos clínicos registrados y solo se dispone de **5 publicaciones** (revisiones y estudios preclínicos) relacionadas de forma indirecta con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (18 de 18) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 18 (vigentes: 18) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cetirizina es un antagonista selectivo del receptor H1 de histamina. Al bloquear este receptor, reduce la vasodilatación, el aumento de la permeabilidad vascular, la estimulación de las terminaciones nerviosas sensitivas y el edema de la mucosa, procesos que dependen de la histamina. Además, se le atribuyen efectos antiinflamatorios modestos, como menor quimiotaxis de eosinófilos y menor expresión de moléculas de adhesión. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento farmacológico general.

Estos mecanismos son biológicamente plausibles en afecciones nasales de tipo alérgico o inflamatorio, como la rinitis alérgica. Sin embargo, "enfermedad de la cavidad nasal" es una categoría muy amplia: el efecto se esperaría sobre todo en los subtipos dependientes de histamina, y no en la enfermedad no alérgica o estructural.

Cabe señalar que, como los datos locales no traen texto de indicación, esta predicción podría reflejar un uso ya conocido del fármaco y no un reposicionamiento genuino. Esto no se puede confirmar con la información disponible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de las publicaciones estudia directamente la enfermedad de la cavidad nasal como tal con cetirizina; se refieren a rinitis alérgica, inflamación nasal en general o modelos animales.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11291777](https://pubmed.ncbi.nlm.nih.gov/11291777/) | 2000 | Revisión | Allergy | Describe el antagonismo del receptor H1 como mecanismo principal de los antihistamínicos en enfermedades alérgicas, y analiza posibles efectos antialérgicos adicionales. |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Revisión | Vestnik otorinolaringologii | Enfoque patogénico del tratamiento de enfermedades inflamatorias de la nariz y los senos paranasales, con énfasis en reducir la hiperemia, el edema y la mucosidad. |
| [35818943](https://pubmed.ncbi.nlm.nih.gov/35818943/) | 2022 | Revisión | Vestnik otorinolaringologii | Antihistamínicos H1 modernos en pacientes con rinitis alérgica e infecciones respiratorias agudas concomitantes. |
| [36116201](https://pubmed.ncbi.nlm.nih.gov/36116201/) | 2022 | Preclínico (ratón) | Phytomedicine | Una cápsula herbal mejora la disfunción olfatoria en un modelo murino de rinitis alérgica; la intervención no es cetirizina. |
| [9301130](https://pubmed.ncbi.nlm.nih.gov/9301130/) | 1997 | Preclínico (animal) | Arerugi | Betotastina en rinitis alérgica experimental; cetirizina se usó como comparador y inhibió de forma dependiente de la dosis el aumento de la respuesta. |

## Información de Mercado en Argentina

Cetirizina cuenta con 18 autorizaciones, todas vigentes y de producto de un solo principio activo. Se listan las 5 principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 32730 | CETIZINE | 10 mg comp.rec.x 10 | Lazar | Vigente |
| 32340 | CABAL | comp.x 30 | Dallas | Vigente |
| 28354 | CABAL | comp.x 10 | Dallas | Vigente |
| 56957 | ALIDIAL | comp.rec.x 10 | Siegfried | Vigente |
| 33080 | CETIRIZINA CETUS | comp.x 10 | Cetus | Vigente |

La tabla muestra 5 de los 18 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado evalúa directamente la enfermedad de la cavidad nasal con cetirizina y no hay ensayos clínicos registrados, por lo que el nivel de evidencia es L5 y la predicción (0,9977) se apoya solo en el modelo y en plausibilidad mecanística. Además, la amplitud de la categoría y la falta de texto de indicación local impiden distinguir un reposicionamiento real de un uso ya establecido.

**Para avanzar se necesita:**
- Obtener el texto de indicación de los prospectos de ANMAT para aclarar si la predicción es un uso ya existente.
- Obtener advertencias y contraindicaciones del prospecto, que hoy faltan.
- Completar los datos de mecanismo de acción desde DrugBank.
- Definir un subtipo nasal concreto (por ejemplo, rinitis alérgica) y buscar ensayos clínicos o estudios que lo evalúen directamente con cetirizina.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «La ausencia de resultados puede deberse a variaciones en el nombre comercial, formato de búsqueda, o a que la consulta fue realizada contra » | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-24 | Eliminado: «No se encontraron autorizaciones de comercialización para **CETIRIZINA** en el sistema consultado» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido (revisado el 2026-11-24; versión anterior conservada en el registro)) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «[ ] **Verificar la fuente regulatoria**: Confirmar si la búsqueda debe realizarse en ANMAT (Argentina) en lugar de TFDA (Taiwán), dado que e» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

