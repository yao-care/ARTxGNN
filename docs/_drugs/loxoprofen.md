---
layout: default
title: Loxoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 183
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Loxoprofen: nueva indicación predicha, Síndrome de microftalmía colobomatosa-displasia rizomélica (nivel de evidencia L5). Indicación original: Artritis reumatoide (según la base de conocimiento del …"
monitor_inn: "loxoprofen"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Loxoprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Loxoprofeno: De Artritis Reumatoide a Síndrome de Microftalmía Colobomatosa-Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

Loxoprofeno es un antiinflamatorio no esteroideo (AINE) originalmente utilizado para el tratamiento de la artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa-displasia rizomélica**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según la base de conocimiento del modelo; el texto de indicación de la autorización local está vacío) |
| Nueva Indicación Predicha | Síndrome de microftalmía colobomatosa-displasia rizomélica |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el loxoprofeno es un profármaco de la clase de los AINE; su metabolito activo (forma trans-alcohol) inhibe las ciclooxigenasas (COX-1 y COX-2), reduciendo la síntesis de prostaglandinas. Esto explica su eficacia en cuadros inflamatorios y dolorosos como la artritis reumatoide.

Sin embargo, los datos compilados **no respaldan un vínculo mecanístico** con la nueva indicación predicha. El síndrome de microftalmía colobomatosa-displasia rizomélica es un trastorno congénito raro del desarrollo (coloboma y microftalmía ocular junto con displasia esquelética rizomélica), sin patología inflamatoria ni dependiente de COX establecida. La inhibición de prostaglandinas no se espera que corrija un defecto estructural del desarrollo.

El puntaje alto de TxGNN (0.9980) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; por sí solo, no ofrece una justificación biológica. En el mejor de los casos, el uso de un AINE podría ser sintomático (dolor), pero no modificaría la enfermedad.

Como referencia, el segundo candidato predicho es el **síndrome de braquidactilia-sindactilia** (puntaje 0.9975), una malformación congénita de las extremidades de origen genético, con las mismas limitaciones: sin ensayos, sin literatura y sin vínculo mecanístico respaldado.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50496 | TABE | 60 mg comp. x 20 | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre la inhibición de COX y una malformación congénita del desarrollo. No hay base para avanzar en esta etapa.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del loxoprofeno, por ejemplo desde DrugBank
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias, contraindicaciones e indicaciones autorizadas)
- Una hipótesis biológica que vincule la vía de prostaglandinas/COX con la fisiopatología de la enfermedad predicha
- Búsqueda de estudios preclínicos o de series de casos que respalden la predicción
- Evaluación de compatibilidad de vías de administración y similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

