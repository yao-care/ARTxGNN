---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el skill `txgnn-pipeline` como referencia de contexto. Ahora genero el informe de evaluación de reposicionamiento para Entacapone basándome en el Evidence Pack proporcionado.

---

# Entacapone: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapone es un inhibidor de la COMT (catecol-O-metiltransferasa), utilizado originalmente como terapia adyuvante a levodopa en la enfermedad de Parkinson para prolongar su efecto terapéutico al reducir la degradación periférica de levodopa. El modelo TxGNN predice que podría ser efectivo para la **Neurodegeneración Asociada a PLA2G6 (PLAN)**, sin embargo, **no existen ensayos clínicos ni publicaciones** que respalden actualmente esta dirección. La evidencia disponible es exclusivamente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (adyuvante a levodopa/carbidopa) |
| Nueva Indicación Predicha | Neurodegeneración Asociada a PLA2G6 (PLAN / PARK14) |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, Entacapone es un inhibidor selectivo y reversible de la COMT, enzima responsable de la metilación y degradación periférica de levodopa y dopamina. Al inhibir la COMT, Entacapone prolonga la vida media de levodopa en plasma, aumenta su biodisponibilidad cerebral y amplifica la señalización dopaminérgica en el estriado. Este mecanismo está ampliamente establecido para la enfermedad de Parkinson.

La Neurodegeneración Asociada a PLA2G6 (PLAN), también denominada PARK14, es una forma atípica de parkinsonismo causado por mutaciones en el gen *PLA2G6*, que codifica una fosfolipasa A2 independiente del calcio. La patología incluye degeneración progresiva de neuronas dopaminérgicas, acumulación de hierro cerebral y formación de cuerpos de Lewy atípicos, compartiendo fenotipo parcial con la enfermedad de Parkinson clásica. Esta similitud fenotípica es probablemente la base que el grafo de conocimiento de TxGNN utilizó para proponer esta asociación.

No obstante, el vínculo mecanístico es **indirecto e inferencial**: la vía de la fosfolipasa A2 afectada en PLAN no tiene intersección directa conocida con la inhibición de COMT. Adicionalmente, los pacientes con PLAN presentan una respuesta inconsistente e impredecible a levodopa, lo que limita significativamente el beneficio potencial de potenciar su biodisponibilidad mediante Entacapone. El elevado puntaje de TxGNN probablemente refleja efectos de propagación en la red del grafo biológico más que una relación farmacológica directa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Entacapone en Neurodegeneración Asociada a PLA2G6.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Entacapone en Neurodegeneración Asociada a PLA2G6.

---

## Información de Mercado en Argentina

Entacapone no cuenta con ninguna autorización de comercialización registrada en Argentina (ANMAT). El fármaco no está disponible en el mercado local bajo ninguna forma farmacéutica ni nombre comercial registrado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para PLAN carece por completo de respaldo empírico: no existen ensayos clínicos ni publicaciones científicas que exploren esta indicación, el vínculo mecanístico entre la inhibición de COMT y la vía de PLA2G6 es puramente inferencial, y Entacapone no está disponible en Argentina, lo que suma una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción (MOA) completo mediante consulta a la API de DrugBank (DG002 pendiente)
- Obtener las advertencias, contraindicaciones e interacciones farmacológicas mediante descarga del prospecto oficial (DG001 pendiente)
- Realizar una revisión narrativa de la literatura sobre respuesta a levodopa y al eje dopaminérgico en pacientes con mutaciones *PLA2G6*, para evaluar plausibilidad terapéutica
- Diseñar estudios preclínicos en modelos de déficit de PLA2G6 que evalúen el efecto de la inhibición de COMT antes de considerar cualquier exploración clínica
- Evaluar la viabilidad regulatoria de acceso en Argentina (importación, uso compasivo u otras vías ante la ausencia de registro ANMAT)
---

