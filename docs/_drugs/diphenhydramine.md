---
layout: default
title: Diphenhydramine
parent: Solo Predicción del Modelo (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
monitor_inn: "diphenhydramine"
predicted_indications: ["rosacea conjunctivitis"]
last_modified_at: 2026-11-24
description: "Diphenhydramine: nueva indicación predicha, conjuntivitis rosácea (rosacea conjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 11 (en el listado vigente: 11)"
---

# Diphenhydramine
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

## Difenhidramina: antihistamínico H1 de primera generación → conjuntivitis rosácea (rosacea conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Difenhidramina es un antihistamínico H1 de primera generación, comercializado en Argentina en jarabe, comprimidos, cápsulas e inyectable.
El modelo TxGNN predice que podría ser útil para **conjuntivitis rosácea (rosacea conjunctivitis)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | conjuntivitis rosácea (rosacea conjunctivitis) |
| Puntaje de Predicción TxGNN | 0,9920 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (11 de 11) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Difenhidramina bloquea los receptores H1 de histamina. En los datos compilados para este informe no hay una descripción detallada del mecanismo de acción, por lo que no se puede afirmar más detalle mecanístico. La reducción de la picazón, el enrojecimiento y la hiperemia ocular mediados por histamina es un efecto plausible de este tipo de fármaco en cuadros conjuntivales de naturaleza alérgica.

El puntaje alto (0,9920) refleja la cercanía del fármaco con otras afecciones conjuntivales en el modelo. Sin embargo, la enfermedad ocular asociada a rosácea depende sobre todo de la disfunción de las glándulas de Meibomio, la inestabilidad de la película lagrimal, factores microbianos (como Demodex) y la inflamación innata (metaloproteinasas, IL-1, vías de calicreína/catelicidina), más que de la histamina. El ajuste mecanístico es, por tanto, solo parcial y no está validado.

Además, la actividad anticolinérgica de la difenhidramina podría empeorar el ojo seco, un problema frecuente en esta población. Esto es una preocupación relevante para cualquier uso ocular.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El fármaco figura como comercializado, como único principio activo y en asociaciones (BENADRYL ANTITUSIVO, BENADRYL DM COMPUESTO, CORIZINA CETUS).

<!-- review:begin ar-lic-20261124-diphenhydramine-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «El fármaco figura como comercializado, con 11 autorizaciones vigentes, todas de productos de un solo principio activo.» Corregido: según los datos (listado de medicamentos de PAMI), BENADRYL ANTITUSIVO, BENADRYL DM COMPUESTO y CORIZINA CETUS son asociaciones; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-diphenhydramine-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 49698 | BENADRYL | cáps.x 30 | Elea | Vigente |
| 41413 | FADALEX | 2.5 mg/ml jbe.x 120 ml | Biosintex Retai | Vigente |
| 20854 | DIFENHIDRAMINA DENVER FARMA | jbe.x 120 ml | Denver Farma | Vigente |
| 30218 | DIFENHIDRAMINA DENVER FARMA | 50 mg comp.x 20 | Denver Farma | Vigente |
| 49749 | BENADRYL | jbe.x 240 ml | Elea | Vigente |

La tabla muestra 5 de los 11 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 394 interacciones. Entre las principales:
  - Gravedad **mayor**: citrato de potasio y eliglustat.
  - Gravedad **moderada**: hiosciamina, atropina, glicopirronio, dicliclomina, clidinio, metscopolamina y mepenzolato (efectos anticolinérgicos aditivos); loperamida, morfina, dronabinol, nabilona, bupropión, lorcaserina, metoclopramida y eluxadolina, entre otros.
- Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni publicaciones sobre la conjuntivitis rosácea. El mecanismo histamínico encaja solo de forma parcial con la fisiopatología de la enfermedad, y el efecto anticolinérgico podría ser perjudicial para el ojo seco.

**Para avanzar se necesita:**
- Revisión de la literatura y de registros de ensayos sobre antihistamínicos en enfermedad ocular por rosácea.
- Datos detallados del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto de ANMAT.
- Evaluación de la vía de administración (ocular o tópica) y de la tolerabilidad en ojo seco.
- Estudios preclínicos o piloto que justifiquen un ensayo clínico.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «todas de un solo principio activo» → también asociaciones | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

