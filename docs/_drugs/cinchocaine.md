---
layout: default
title: Cinchocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 102
evidence_level: L5
indication_count: 7
monitor_inn: "cinchocaine"
predicted_indications: ["bronchitis", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis"]
last_modified_at: 2026-11-24
description: "Cinchocaine: nueva indicación predicha, Bronquitis (bronchitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Cinchocaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Cinchocaína: anestésico local bloqueador de canales de sodio → Bronquitis (bronchitis)
{: .text-alpha }

## Resumen en Una Frase

Cinchocaína (dibucaína) es un anestésico local de tipo amida que se comercializa en Argentina como producto de uso tópico (PROCTYL).
El modelo TxGNN predice que podría ser efectiva para **Bronquitis (bronchitis)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bronquitis (bronchitis) |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la cinchocaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, lo que interrumpe la conducción del impulso nervioso.

Un vínculo teórico con la bronquitis sería la supresión de la actividad de las fibras sensoriales (fibras C) de las vías respiratorias y del reflejo de la tos, como ocurre con otros anestésicos tópicos. Es una hipótesis especulativa: no existen estudios que la respalden y el puntaje alto del modelo (0.9977) es solo una predicción computacional.

Además, el uso sistémico o inhalado de cinchocaína plantearía preocupaciones de seguridad (toxicidad de anestésicos locales, riesgo de broncoespasmo), y el producto disponible es de uso tópico. La compatibilidad de vías de administración con la nueva indicación aún no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 27593 | PROCTYL | pda.x 10 g | Nolter | Vigente |
| 24920 | PROCTYL | pda.x 30 g | Nolter | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Los productos (PROCTYL) son asociaciones de cincocaína con otros principios activos.

<!-- review:begin ar-lic-20261124-cinchocaine-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Ambas autorizaciones son de producto de un solo principio activo y están vigentes.» Corregido: según los datos (listado de medicamentos de PAMI), PROCTYL es una asociación de cincocaína clorhidrato con otros principios activos; las cifras actualizadas y el estado de cada producto están en el resumen rápido y en la tabla de la información de mercado. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261124-cinchocaine-1 -->

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados; consultar el prospecto para la información de seguridad completa. No se encontraron interacciones farmacológicas registradas.

Como referencia adicional, los datos compilados señalan posibles contraindicaciones relacionadas con las siguientes condiciones (no provienen del texto del prospecto y deben verificarse): epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, paro cardíaco súbito, enfermedad de la conducción cardíaca, insuficiencia respiratoria, miastenia gravis, enfermedades de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y cardiopatía.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para bronquitis se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, con un vínculo mecanístico especulativo y preocupaciones de seguridad si se usara por vía sistémica o inhalada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto aprobado (advertencias y contraindicaciones)
- Revisión de literatura y estudios preclínicos sobre anestésicos locales en tos y bronquitis
- Evaluación de la vía de administración y de la viabilidad de una formulación adecuada para vía respiratoria
- Evaluación de seguridad cardiovascular, neuromuscular y respiratoria antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «de un solo principio activo» → asociación | Corregido | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

