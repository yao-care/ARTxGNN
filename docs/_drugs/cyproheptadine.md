---
layout: default
title: Cyproheptadine
parent: Solo Predicción del Modelo (L5)
nav_order: 118
evidence_level: L5
indication_count: 1
monitor_inn: "cyproheptadine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-30
description: "Cyproheptadine: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cyproheptadine
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

## Ciproheptadina: antihistamínico con acción antiserotoninérgica y anticolinérgica → Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Ciproheptadina es un antihistamínico de primera generación con actividad antagonista de serotonina (5-HT2) y anticolinérgica, comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Enfermedad de la cavidad nasal (nasal cavity disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados para este informe que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0,9921 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción. Según el conocimiento farmacológico general, la ciproheptadina bloquea receptores H1 de histamina, antagoniza receptores de serotonina (5-HT2) y tiene actividad anticolinérgica. Estas acciones se relacionan de forma plausible con síntomas de la mucosa nasal como rinorrea, estornudos y congestión.

La categoría predicha, "enfermedad de la cavidad nasal", es muy amplia y se superpone en gran medida con los cuadros nasales para los que este tipo de fármaco ya se emplea. Por ello, no representa con claridad una oportunidad nueva de reposicionamiento, sino más bien una generalización de usos conocidos.

El puntaje del modelo es muy alto, pero no está respaldado por estudios concretos en los datos disponibles. Por lo tanto, el vínculo mecanístico descansa en conocimiento general y no en evidencia aportada específicamente para esta predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49668 | CIPROVIT CALCICO | comp. blíster x 60 | No registrada en los datos locales |
| 158 | CIPROVIT MAGNESICO | gránulos sobres x 20 | No registrada en los datos locales |
| 50366 | CIPROVIT CALCICO | jarabe x 150 ml | No registrada en los datos locales |

Dos de los tres productos (fabricante: Beta) siguen en el listado de medicamentos de PAMI; el tercero (50366, CIPROVIT CALCICO jarabe x 150 ml) ya no figura en el listado vigente de PAMI.

<!-- review:begin ar-lic-20261117-cyproheptadine-1 -->

> **Corrección de verificación (2026-11-17)**: Texto original: «Las tres autorizaciones son de producto de un solo principio activo y se encuentran vigentes (fabricante: Beta).» Corregido: el producto 50366 (CIPROVIT CALCICO jarabe) figuraba en el listado de PAMI del 01/03/2026 y ya no figura en el listado vigente (05/11/2026); 2 de los 3 productos siguen en el listado. Que un producto ya no figure en el listado de PAMI no significa que su registro en ANMAT esté dado de baja: el estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261117-cyproheptadine-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 308 interacciones. Las de nivel **mayor** incluyen cloruro de potasio y citrato de potasio. Entre las de nivel **moderado** figuran anticolinérgicos y antiespasmódicos (atropina, hiosciamina, escopolamina, glicopirronio, diciclomina, trospio, propantelina, metescopolamina, mepenzolato), opioides (morfina, opio, loperamida, eluxadolina), cannabinoides (dronabinol, nabilona), metoclopramida y fenfluramina. Se esperan efectos anticolinérgicos y sedantes aditivos con varios de ellos.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9921), pero no cuenta con ningún ensayo clínico ni publicación que estudie directamente esta enfermedad, por lo que el nivel de evidencia es L5. Además, la categoría es amplia y no constituye una indicación claramente nueva.

**Para avanzar se necesita:**
- Definir una indicación nasal más específica (por ejemplo, un subtipo concreto) que permita buscar estudios directos
- Revisión sistemática de ensayos clínicos y literatura sobre ciproheptadina en patología nasal
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Plan de monitoreo de seguridad, en especial por los efectos anticolinérgicos y las interacciones identificadas

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-17 | «se encuentran vigentes» → 2 de 3 siguen en el listado de PAMI | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

