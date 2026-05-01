---
layout: default
title: Agomelatina
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 0
---

# Agomelatina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# AGOMELATINA: Evaluación Preliminar — Sin Indicación Predicha Disponible

## Resumen en Una Frase

Agomelatina es un antidepresivo con mecanismo dual como agonista de receptores de melatonina (MT1/MT2) y antagonista del receptor de serotonina 5-HT2C, utilizado internacionalmente para el tratamiento del trastorno depresivo mayor. Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y **no se encuentra comercializado en Argentina** según los registros regulatorios disponibles, lo que limita significativamente la evaluación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en Argentina (uso internacional conocido: trastorno depresivo mayor) |
| Nueva Indicación Predicha | — Sin predicción disponible — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (sin evidencia de reposicionamiento) |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no se Generó una Predicción?

Agomelatina (INN: AGOMELATINA) es un antidepresivo atípico desarrollado por Servier, comercializado en Europa bajo las marcas Valdoxan® y Thymanax®. Su mecanismo de acción dual combina el agonismo de los receptores de melatonina MT1 y MT2 (involucrados en la regulación del ritmo circadiano) con el antagonismo del receptor serotoninérgico 5-HT2C, lo que contribuye a la liberación de noradrenalina y dopamina en la corteza frontal. Este perfil farmacológico único lo diferencia de los antidepresivos convencionales (ISRS, IRSN).

Sin embargo, el Evidence Pack actual presenta vacíos de datos críticos: no se dispone de un DrugBank ID registrado, el mecanismo de acción detallado figura como brecha de datos, y no existen autorizaciones de comercialización en Argentina. La ausencia de integración en la base de conocimiento del grafo TxGNN impide que el modelo genere predicciones de reposicionamiento.

Para que TxGNN pueda evaluar potenciales nuevas indicaciones, es necesario que el fármaco esté representado adecuadamente en el grafo de conocimiento con sus relaciones farmacológicas (targets, pathways, indicaciones aprobadas). Sin estos nodos y conexiones, el algoritmo no puede calcular puntajes de predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con reposicionamiento registrados, dado que no se ha generado una predicción de nueva indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con reposicionamiento disponible para este candidato.

---

## Información de Mercado en Argentina

Agomelatina **no se encuentra registrada ni comercializada en Argentina**. No se identificaron autorizaciones de comercialización vigentes en los registros regulatorios consultados (ANMAT).

> **Nota:** El fármaco sí cuenta con aprobación en la Unión Europea (EMA) y en otros mercados internacionales para el tratamiento del trastorno depresivo mayor en adultos.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad locales (advertencias, contraindicaciones ni interacciones farmacológicas) debido a la ausencia de registro en Argentina.

> **Información de referencia internacional:** Según la ficha técnica europea, las principales precauciones de agomelatina incluyen:
> - **Hepatotoxicidad**: se requiere monitoreo de función hepática antes del inicio, a las 3, 6, 12 y 24 semanas de tratamiento, y periódicamente después.
> - **Contraindicaciones**: insuficiencia hepática (cirrosis o enfermedad hepática activa), uso concomitante con inhibidores potentes de CYP1A2 (fluvoxamina, ciprofloxacino).
> - **Interacciones relevantes**: inhibidores de CYP1A2 (aumentan significativamente la exposición a agomelatina).
>
> *Esta información proviene de fuentes internacionales y no sustituye la evaluación regulatoria local.*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No es posible avanzar con la evaluación de reposicionamiento de Agomelatina en este momento. El fármaco no está comercializado en Argentina (0 autorizaciones), no tiene DrugBank ID asignado en el sistema, y el modelo TxGNN no ha generado predicciones de nuevas indicaciones debido a su insuficiente representación en el grafo de conocimiento.

**Para avanzar se necesita:**
- Confirmar e integrar el **DrugBank ID** correcto (DB06594) en el sistema
- Completar la representación del fármaco en el **grafo de conocimiento TxGNN** (targets moleculares: MT1, MT2, 5-HT2C; pathways: ritmo circadiano, neurotransmisión monoaminérgica)
- Obtener datos detallados del **mecanismo de acción (MOA)** desde DrugBank API
- Evaluar la viabilidad regulatoria: verificar si existe trámite de registro ante **ANMAT** en curso o si se prevé su comercialización en Argentina
- Una vez completados los datos anteriores, **re-ejecutar la predicción TxGNN** para obtener candidatos de reposicionamiento
- Obtener e integrar los datos de **advertencias y contraindicaciones** del prospecto autorizado por la autoridad regulatoria correspondiente
---

