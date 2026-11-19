---
layout: default
title: Pheniramine
parent: Solo Predicción del Modelo (L5)
nav_order: 212
evidence_level: L5
indication_count: 1
monitor_inn: "pheniramine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-17
description: "Pheniramine: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Pheniramine
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

## Feniramina: antihistamínico H1 de primera generación → enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Feniramina es un antihistamínico H1 de primera generación (clase de las alquilaminas), presente en Argentina en gotas oftálmicas.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal (nasal cavity disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados para este reporte que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0,9928 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No figura en el listado vigente de PAMI (los 4 productos de estos datos ya no figuran) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la feniramina es un antihistamínico H1 de primera generación, y mecanísticamente podría ser aplicable a afecciones de la cavidad nasal.

El bloqueo del receptor H1 y los efectos anticolinérgicos leves podrían reducir la congestión nasal, la rinorrea y la inflamación de la mucosa. Esto es una inferencia a partir de la farmacología conocida y no está respaldada por evidencia específica recuperada para esta indicación.

Cabe señalar que el puntaje elevado probablemente refleje que "enfermedad de la cavidad nasal" es una categoría amplia que agrupa afecciones nasales cercanas a los usos ya conocidos del fármaco, más que una oportunidad de reposicionamiento realmente nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43809 | VISUCLAR | Frasco gotero x 10 ml | No registrada en los datos locales |
| 18650 | REFENAX COLIRIO | Solución oftálmica x 15 ml | No registrada en los datos locales |
| 42850 | MIRA KLONAL | Frasco gotero x 5 ml | No registrada en los datos locales |
| 174 | MIRUS | Solución oftálmica x 15 ml | No registrada en los datos locales |

Los 4 productos ya no figuran en el listado vigente de PAMI (el listado del 05/11/2026 no incluye ningún producto con feniramina, aparte de clorfeniramina y dexclorfeniramina, que son otros principios activos).

<!-- review:begin ar-lic-20261117-pheniramine-1 -->

> **Corrección de verificación (2026-11-17)**: Texto original: «Las 4 autorizaciones son de producto de un solo principio activo y se encuentran vigentes.» Corregido: los 4 productos (174 MIRUS, 18650 REFENAX COLIRIO, 42850 MIRA KLONAL, 43809 VISUCLAR) figuraban en el listado de PAMI del 01/03/2026 y ya no figuran en el listado vigente (05/11/2026). Que un producto ya no figure en el listado de PAMI no significa que su registro en ANMAT esté dado de baja: el estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261117-pheniramine-1 -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni publicaciones que estudien directamente esta enfermedad, y sin datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción
- Definir con mayor precisión qué afecciones concretas de la cavidad nasal serían el objetivo
- Buscar estudios clínicos o publicaciones que evalúen directamente esta indicación
- Evaluar la compatibilidad de la vía de administración, ya que los productos locales son formulaciones oftálmicas

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-17 | «se encuentran vigentes» → ya no figuran en PAMI | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

