---
layout: default
title: Travoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Travoprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Travoprost: De Glaucoma de Ángulo Abierto a Calcifilaxis Visceral

## Resumen en Una Frase

Travoprost es un análogo de la prostaglandina F2-alfa (agonista del receptor FP) de uso oftálmico tópico, utilizado originalmente para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **calcifilaxis visceral**, pero hasta ahora **no existen ensayos clínicos ni publicaciones** que respalden esta dirección específica, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Calcifilaxis visceral |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, travoprost es un análogo de la prostaglandina F2-alfa que actúa como agonista del receptor FP; en el ojo reduce la presión intraocular, principalmente al aumentar el flujo de salida uveoescleral. Su eficacia en glaucoma e hipertensión ocular está bien establecida.

Respecto de la calcifilaxis visceral (arteriolopatía urémica calcificante), los datos compilados no sustentan un vínculo mecanístico plausible. Aunque los análogos de prostanoides tienen efectos vasoactivos locales, travoprost se administra por vía tópica ocular con baja exposición sistémica, y la relación entre la indicación original y la nueva sigue sin evaluarse.

Por ello, la puntuación alta del modelo (99.99%) debe interpretarse con cautela: refleja una asociación dentro del grafo de conocimiento, no evidencia clínica. Otras predicciones del mismo farmaco (síndromes del desfiladero torácico, enfermedad vascular, angiodisplasia gástrica, síndrome del dedo azul, entre otras) presentan la misma situación: ausencia de ensayos y de sustento mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para calcifilaxis visceral.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para calcifilaxis visceral.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38893 | ARVO (Elea) | Solución oftálmica x 2.5 ml | No disponible en los datos |
| 43391 | GLAUNOT (Lab Internacion) | Solución oftálmica x 2.5 ml | No disponible en los datos |
| 32252 | GLAUCOPROST (Max Vision) | Solución oftálmica x 3 ml | No disponible en los datos |
| 56010 | TRAVOPLOS (Novoplos) | Solución oftálmica x 5 ml | No disponible en los datos |
| 52151 | GLAUNOT SC (Lab Internacion) | Solución oftálmica x 2.5 ml | No disponible en los datos |

Se muestran 5 de las 8 autorizaciones vigentes (todas de tipo monofármaco y ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, panuveítis, iritis, edema macular cistoide y edema macular retiniano.
- **Interacciones farmacológicas**: se identificaron 49 posibles interacciones, todas con nivel de gravedad no clasificado. Entre las listadas figuran calcitriol, pantoprazol, sucralfato, morfina, metformina, omeprazol, prednisona, prednisolona, triamcinolona, simvastatina y ácido acetilsalicílico.
- **Señal de seguridad relevante**: un reporte de caso describe efusión uveal con desprendimiento de retina exudativo inducido por travoprost tópico en un paciente con síndrome de Sturge-Weber-Krabbe (trastorno de malformación vascular), lo que sugiere cautela en pacientes con malformaciones vasculares.
- En la bibliografía, la hiperemia conjuntival es un efecto adverso frecuente de travoprost (hasta cerca del 50% de los pacientes en una revisión).

Para advertencias y contraindicaciones del prospecto, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para calcifilaxis visceral se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y los datos no respaldan un mecanismo plausible dada la vía tópica ocular y la baja exposición sistémica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del farmaco y análisis de su relación con la fisiopatología de la calcifilaxis
- Estudios preclínicos que justifiquen un efecto en calcificación vascular
- Evaluación de la compatibilidad de vía de administración (la presentación actual es solo oftálmica)
- Obtención y revisión del prospecto de ANMAT (advertencias y contraindicaciones)
- Revisión de las demás predicciones de mayor rango, ninguna de las cuales cuenta actualmente con evidencia directa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

