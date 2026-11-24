---
layout: default
title: Sulpirida
parent: Solo Predicción del Modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 9
drugbank_id: DB00391
monitor_inn: "Sulpiride"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia X-linked", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "syndromic myopia", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-24
description: "Sulpirida: nueva indicación predicha, distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) (nivel de evidencia L5)."
---

# Sulpirida
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Sulpirida: distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies)
{: .text-alpha }

## Resumen en Una Frase

Sulpirida es un antagonista selectivo de los receptores de dopamina de tipo D2 que se comercializa actualmente en Argentina. El modelo TxGNN predice que podría ser útil para **distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies)**. Hoy esta predicción cuenta con **0 ensayos clínicos** y **2 publicaciones preclínicas** en modelos animales de retinosis pigmentaria.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 5) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Lo que se sabe es que la sulpirida bloquea los receptores de dopamina D2. En la retina, la dopamina regula la actividad de las células ganglionares, que son las neuronas que envían la señal visual al cerebro. En modelos animales de retinosis pigmentaria, el sistema dopaminérgico retiniano parece estar alterado. Por eso se ha estudiado si bloquear los receptores D2 modifica la respuesta de esas células a la luz.

Los dos estudios disponibles se hicieron en ratas con retinosis pigmentaria (modelo P23H). Describen que antagonistas D2 como la sulpirida y la eticloprida parecen mejorar las respuestas visuales de las células ganglionares. Lo hacen aumentando su sensibilidad a la luz y transformando células ON de latencia larga y anómala en células OFF. Esto aporta una plausibilidad mecanística indirecta de que el bloqueo D2 podría modular la señal visual residual en una retina degenerada.

Esta plausibilidad tiene límites importantes. Se trata de registros electrofisiológicos en animales, no de evidencia de modificación de la enfermedad ni de beneficio clínico en personas. Ninguno de los estudios muestra con claridad un efecto terapéutico de la sulpirida en sí. El puntaje TxGNN muy alto es solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26717015](https://pubmed.ncbi.nlm.nih.gov/26717015/) | 2015 | Preclínico (electrofisiología animal) | PLoS One | Se evaluaron antagonistas de receptores D2 sobre las respuestas a la luz de células ganglionares en retinas de ratas normales y de ratas P23H, modelo de retinosis pigmentaria. |
| [27788033](https://pubmed.ncbi.nlm.nih.gov/27788033/) | 2016 | Preclínico (electrofisiología animal) | J Ocul Pharmacol Ther | Se comparó el efecto de haloperidol y clozapina sobre las respuestas visuales en ratas P23H. El estudio recuerda que sulpirida y eticloprida parecían mejorar la sensibilidad a la luz de estas células. |

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 7955 | VIPRAL | comp.x 50 | Teva Argentina | Vigente |
| 10135 | ALPLAX DIGEST | caplets x 30 | Gador | Vigente |
| 17561 | TRANQUINAL SOMA | comp.x 30 | Bagó | Vigente |
| 11010 | VEGESTABIL | comp.x 30 | Siegfried | Vigente |
| 10136 | ALPLAX DIGEST | caplets x 60 | Gador | Vigente |

La tabla muestra los 5 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

VIPRAL contiene sulpirida como único principio activo; los demás productos son asociaciones con alprazolam (ALPLAX DIGEST, TRANQUINAL SOMA) o con clorazepato dipotásico (VEGESTABIL).

<!-- review:begin ar-lic-20261124-sulpirida-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Las cinco autorizaciones listadas están vigentes y corresponden a productos con sulpirida como único principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), ALPLAX DIGEST, TRANQUINAL SOMA y VEGESTABIL son asociaciones; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-sulpirida-1 -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única base son dos estudios electrofisiológicos en animales, que no estudian la entidad predicha en personas. El puntaje alto del modelo (0,9995) es una señal computacional y no reemplaza la evidencia clínica. Por eso la predicción se mantiene como pregunta de investigación.

**Para avanzar se necesita:**
- Estudios preclínicos que midan un efecto funcional o estructural de la sulpirida sobre la retina degenerada, y no solo cambios en la actividad eléctrica.
- Datos detallados del mecanismo de acción y su relación con la vía dopaminérgica retiniana.
- Información de seguridad del prospecto (advertencias, contraindicaciones e interacciones), que no estaba disponible, para evaluar la viabilidad de un uso prolongado.
- Una evaluación de la vía de administración y de la exposición ocular antes de plantear estudios en humanos.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «como único principio activo» → la mayoría asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

