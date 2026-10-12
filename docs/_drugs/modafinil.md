---
layout: default
title: Modafinil
parent: Evidencia Moderada (L3-L4)
nav_order: 194
evidence_level: L4
indication_count: 1
---

# Modafinil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Modafinilo: De Narcolepsia a Insomnio

## Resumen en Una Frase

Modafinilo es un fármaco promotor de la vigilia, originalmente utilizado para el tratamiento de la narcolepsia y trastornos relacionados del sistema nervioso central.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, aunque con apenas **2 ensayos clínicos** de fase 4 (uno terminado con 2 participantes y otro completado con 40 participantes) y **ninguna publicación** que respalde esta dirección.
La predicción es, por ahora, esencialmente teórica y mecanísticamente cuestionable.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Narcolepsia (según las relaciones de indicación del grafo de conocimiento; los registros locales no incluyen texto de indicación aprobada) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los registros compilados. Según la información general conocida, el modafinilo es un agente promotor de la vigilia que se cree actúa mediante la inhibición del transportador de dopamina y efectos sobre los sistemas de vigilia de orexina, histamina y noradrenalina. Su eficacia en la narcolepsia está bien establecida.

Sin embargo, desde el punto de vista mecanístico, **usar un fármaco que promueve la vigilia para tratar el insomnio es contraintuitivo**: cabría esperar que empeore el inicio y el mantenimiento del sueño en lugar de mejorarlos. El puntaje alto de TxGNN (0.998) probablemente refleja una asociación en el grafo de conocimiento, impulsada por vecinos compartidos de los trastornos del sueño y la vigilia (por ejemplo, la narcolepsia), y no una justificación terapéutica real.

Los ensayos registrados parecen evaluar el modafinilo para la somnolencia diurna residual o las alteraciones del sueño/vigilia, no para tratar el insomnio en sí. Por ello, esta predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Modafinilo para alteraciones del sueño/vigilia en adultos mayores. Terminado con solo 2 participantes, sin datos interpretables de eficacia o seguridad. |
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Efectos del modafinilo, solo o combinado con terapia cognitivo-conductual para el insomnio (TCC-I), sobre el funcionamiento diurno y la gravedad del insomnio en personas con insomnio primario. No hay resultados disponibles que demuestren beneficio. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52079 | VISPER (Ariston) | Comprimidos 200 mg x 15 | No disponible en los registros |
| 49669 | VIGICER (Beta) | Comprimidos 200 mg x 15 | No disponible en los registros |
| 42592 | INTENSIT (Rontag) | Comprimidos 200 mg x 10 | No disponible en los registros |
| 49670 | VIGICER (Beta) | Comprimidos 200 mg x 30 | No disponible en los registros |
| 58762 | FORCILIN (Megalabs Argent) | Comprimidos 200 mg x 20 | No disponible en los registros |

Hay 7 autorizaciones vigentes en total (todas de monofármaco); aquí se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión arterial, insuficiencia hepática, trastornos de ansiedad, trastornos neuróticos, trastorno distímico, trastornos psicóticos (incluidos esquizofreniforme y esquizoafectivo), trastornos mentales, abuso/dependencia de sustancias, síndrome coronario agudo, infarto de miocardio, isquemia miocárdica, enfermedad arterial coronaria, prolapso de la válvula mitral, síndrome de taquicardia postural ortostática y hemoglobinopatías.
- **Interacciones farmacológicas**: se identificaron 249 interacciones potenciales. Entre las principales de nivel moderado figuran omeprazol, esomeprazol, rabeprazol, dexametasona, eliglustat, linagliptina y cisaprida. Otras, de nivel menor, incluyen hidrocortisona, pioglitazona, aprepitant, cimetidina y claritromicina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en una asociación del grafo de conocimiento, sin respaldo mecanístico plausible (un fármaco promotor de la vigilia para tratar el insomnio) y con evidencia clínica mínima: un ensayo terminado con 2 participantes y otro de 40 sin resultados que demuestren eficacia. No hay literatura de apoyo.

**Para avanzar se necesita:**
- Datos de mecanismo de acción confirmados (p. ej., desde DrugBank) y un análisis que explique cómo podría ser beneficioso en el insomnio
- Resultados publicados del ensayo NCT00124384 o nuevos ensayos controlados específicos en insomnio
- Prospecto oficial de ANMAT con advertencias, contraindicaciones e indicaciones aprobadas, para completar la revisión de seguridad
- Evaluación del perfil de riesgo cardiovascular y psiquiátrico, dado el número de contraindicaciones señaladas en el grafo de conocimiento
- Reconsiderar la prioridad de esta candidata frente a otras indicaciones con mayor plausibilidad mecanística
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

