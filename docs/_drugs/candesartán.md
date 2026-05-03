---
layout: default
title: Candesartán
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 0
---

# Candesartán
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

# CANDESARTÁN: Evaluación de Reposicionamiento — Sin Predicciones TxGNN Disponibles

## Resumen en Una Frase

Candesartán es un bloqueante del receptor de angiotensina II tipo 1 (ARA-II), ampliamente utilizado para el tratamiento de la hipertensión arterial y la insuficiencia cardíaca con fracción de eyección reducida.
En este Evidence Pack **no se encontraron predicciones de nuevas indicaciones por parte del modelo TxGNN**, por lo que no es posible presentar un candidato de reposicionamiento en esta iteración.
Se recomienda completar los datos faltantes (INN normalizado, DrugBank ID, MOA estructurado) y re-ejecutar el pipeline antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial; Insuficiencia cardíaca |
| Nueva Indicación Predicha | No disponible (sin predicciones TxGNN en este pack) |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | N/A |
| Estado de Mercado en Argentina | No registrado en la consulta realizada |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué hay Ausencia de Predicciones?

Candesartán pertenece a la clase de los antagonistas del receptor AT1 de angiotensina II. Su mecanismo de acción implica el bloqueo competitivo de la unión de angiotensina II al receptor AT1, lo que reduce la vasoconstricción periférica, la liberación de aldosterona y la retención de sodio y agua. Esta acción lo convierte en uno de los pilares del tratamiento antihipertensivo y de la insuficiencia cardíaca.

Como clase, los ARA-II han sido investigados en múltiples áreas más allá de la cardiología: nefroprotección, neuroprotección en enfermedades degenerativas, modulación del sistema renina-angiotensina intratumoral, e incluso investigaciones en el contexto de infecciones virales. Esto sugiere que el potencial de reposicionamiento existe a nivel de clase farmacológica.

Sin embargo, el campo `predicted_indications` del Evidence Pack se encuentra vacío. La causa más probable es que la grafía empleada en la consulta — **"CANDESARTÁN"** (con tilde, forma en español) — no coincida con el INN normalizado **"candesartan"** utilizado en la base de conocimiento del modelo TxGNN. Esto habría impedido el mapeo correcto al grafo de conocimiento y la generación de predicciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene predicciones TxGNN ni datos de seguridad estructurados. Sin una indicación predicha validada por el modelo, no es posible completar el análisis de reposicionamiento ni emitir una recomendación clínica.

**Para avanzar se necesita:**

- **[Crítico]** Re-ejecutar el pipeline usando el INN normalizado en inglés: `candesartan` (sin tilde), para asegurar el mapeo correcto al grafo TxGNN
- **[Crítico]** Completar el DrugBank ID — el identificador probable es `DB00762` (candesartan cilexetil); verificar y añadir al Evidence Pack
- **[Alto]** Obtener el MOA estructurado desde DrugBank para habilitar el análisis de relacionamiento mecanístico
- **[Alto]** Verificar el estado de comercialización real en Argentina vía ANMAT: Candesartán sí está comercializado históricamente (Atacand® y genéricos), por lo que los 0 resultados probablemente reflejan un problema de grafía en la consulta, no ausencia real de registro
- **[Medio]** Recopilar advertencias, contraindicaciones y perfil de interacciones del prospecto ANMAT para completar la sección de seguridad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

