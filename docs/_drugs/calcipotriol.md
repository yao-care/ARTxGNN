---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: Evaluación de Candidato para Reposicionamiento — Datos Insuficientes

## Resumen en Una Frase

Calcipotriol (DB02300) es un análogo sintético de la vitamina D3, reconocido por su uso tópico en el tratamiento de la psoriasis a través de la modulación del receptor de vitamina D (VDR). En este ciclo de evaluación, **el modelo TxGNN no generó predicciones de nuevas indicaciones**, por lo que no es posible identificar un candidato de reposicionamiento. Se identificaron brechas de datos bloqueantes en mecanismo de acción y seguridad que impiden avanzar en la evaluación formal.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos registrados en este paquete |
| Nueva Indicación Predicha | Sin predicciones generadas en este ciclo |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | N/D — Sin predicciones del modelo |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por Qué No Hay Predicción Disponible?

El modelo TxGNN no devolvió predicciones de indicaciones nuevas para Calcipotriol en este ciclo. Esto puede deberse a:

1. **Brecha de MOA (DG002 — Severidad Alta):** El mecanismo de acción formal no fue recuperado desde DrugBank. Sin este dato, el grafo de conocimiento no pudo establecer las relaciones biológicas necesarias para la predicción.
2. **Sin indicaciones originales registradas:** El campo `original_indications` está vacío, lo que limita el contexto de entrada al modelo.
3. **Sin presencia regulatoria en Argentina:** Calcipotriol no cuenta con autorizaciones de comercialización ante ANMAT, lo que reduce la información regulatoria disponible para el análisis.

De acuerdo con la literatura farmacológica general, Calcipotriol actúa como agonista del receptor VDR, regulando la proliferación y diferenciación celular — mecanismo con interés documentado en investigación oncológica y dermatológica. Sin embargo, sin predicciones formales del modelo, esta información no puede traducirse en un candidato de reposicionamiento evaluable en el marco actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados, dado que no se generaron predicciones de indicación nueva en este ciclo.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el contexto de las predicciones del modelo.

---

## Información de Mercado en Argentina

Calcipotriol no cuenta con autorizaciones de comercialización registradas en Argentina según los datos consultados (0 licencias ANMAT).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** La brecha de datos DG001 (Severidad: Bloqueante) impide la evaluación de advertencias y contraindicaciones formales desde el prospecto TFDA/ANMAT. Esta brecha bloquea la entrada al proceso de evaluación de seguridad S1.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Calcipotriol presenta dos brechas de datos críticas — una bloqueante (advertencias del prospecto TFDA) y una de alta severidad (mecanismo de acción) — y el modelo TxGNN no generó predicciones de nuevas indicaciones en este ciclo. No existe base de evidencia sobre la cual construir un análisis de reposicionamiento.

**Para avanzar se necesita:**
- **[DG002 — Alta]** Recuperar el mecanismo de acción (MOA) completo desde la API de DrugBank (DB02300)
- **[DG001 — Bloqueante]** Descargar y analizar el prospecto TFDA para obtener advertencias, contraindicaciones y perfil de seguridad formal
- Verificar el estado del pipeline TxGNN para este candidato: confirmar si la ausencia de predicciones es un resultado válido o un error de procesamiento
- Confirmar el estado regulatorio en Argentina (ANMAT) para Calcipotriol con búsqueda directa en el registro de especialidades medicinales
- Registrar las indicaciones originales conocidas (psoriasis) en el campo `original_indications` para enriquecer el contexto de entrada al modelo
---

