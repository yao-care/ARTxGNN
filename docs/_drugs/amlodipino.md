---
layout: default
title: Amlodipino
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
---

# Amlodipino
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

# AMLODIPINO: Informe de Evaluación de Reposicionamiento

## Resumen en Una Frase

Amlodipino es un bloqueante de los canales de calcio dihidropiridínico, ampliamente utilizado a nivel mundial para el tratamiento de la hipertensión arterial y la angina de pecho. En esta evaluación, el modelo TxGNN **no generó predicciones de nuevas indicaciones** para este fármaco. Además, no se encontraron autorizaciones de comercialización vigentes en Argentina, lo que limita significativamente la viabilidad de cualquier estrategia de reposicionamiento en este mercado.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (conocida: hipertensión arterial, angina de pecho) |
| Nueva Indicación Predicha | **Sin predicciones generadas por TxGNN** |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | **L5** — Solo evaluación del modelo, sin resultados predictivos |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué No Se Generaron Predicciones?

Amlodipino (DCI en español: AMLODIPINO) es un antagonista de los canales de calcio de tipo L del grupo de las dihidropiridinas. Su mecanismo de acción principal consiste en inhibir el flujo de iones calcio a través de los canales de calcio dependientes de voltaje en el músculo liso vascular y el miocardio, produciendo vasodilatación periférica y coronaria. Es uno de los antihipertensivos más prescritos a nivel global.

El modelo TxGNN no generó indicaciones predichas para AMLODIPINO en esta ejecución. Esto puede deberse a múltiples factores: (1) el fármaco no fue mapeado correctamente al grafo de conocimiento del modelo (el campo `drugbank_id` se encuentra vacío); (2) las indicaciones conocidas de amlodipino ya cubren un amplio espectro cardiovascular, lo que reduce el espacio de predicción novedoso; o (3) la consulta se realizó con la denominación en español "AMLODIPINO" en lugar de la DCI en inglés "amlodipine", lo que pudo haber afectado el mapeo.

Cabe señalar que el campo de mecanismo de acción (`original_moa`) tampoco fue recuperado del Evidence Pack, lo cual constituye una brecha de datos de severidad alta (DG002) que impacta directamente en el análisis de relación mecanística con posibles nuevas indicaciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones predichas, dado que el modelo TxGNN no generó predicciones para este fármaco.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones predichas disponible en este Evidence Pack.

---

## Información de Mercado en Argentina

AMLODIPINO **no posee autorizaciones de comercialización vigentes** registradas en el sistema consultado para Argentina. No se identificaron productos con licencia activa.

> **Nota:** Esto no significa necesariamente que amlodipino no esté disponible en Argentina bajo otras denominaciones comerciales o combinaciones. Se recomienda verificar directamente en el registro de ANMAT con variantes de búsqueda (e.g., "amlodipina", "amlodipine", nombres comerciales como "Norvasc", "Amlodipin").

---

## Consideraciones de Seguridad

No se recuperaron datos de seguridad (advertencias, contraindicaciones ni interacciones farmacológicas) en este Evidence Pack.

> Consultar el prospecto aprobado por la autoridad regulatoria correspondiente para información completa de seguridad. Para amlodipino, las precauciones generalmente conocidas incluyen: hipotensión, edema periférico, precaución en insuficiencia hepática grave y en estenosis aórtica severa.

---

## Brechas de Datos Identificadas

Las siguientes brechas de datos fueron registradas durante la generación del Evidence Pack y deben resolverse antes de cualquier avance:

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Nivel de Fármaco | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede iniciar la evaluación de seguridad S1 | Sitio web de la autoridad regulatoria — descargar y analizar PDF del prospecto |
| DG002 | Nivel de Fármaco | Mecanismo de Acción (MOA) | **Alta** | Afecta el análisis de relación mecanística | DrugBank — consultar vía API |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El modelo TxGNN no generó predicciones de nuevas indicaciones para AMLODIPINO. Adicionalmente, el fármaco no está registrado como comercializado en Argentina según los datos consultados, y existen brechas de datos críticas (bloqueantes) sin resolver. No existe base suficiente para avanzar en una estrategia de reposicionamiento en este momento.

**Para avanzar se necesita:**
- **Resolver el mapeo del fármaco**: Verificar que "AMLODIPINO" se mapee correctamente a su entrada en DrugBank (DB00381) y re-ejecutar la predicción TxGNN con el `drugbank_id` correcto
- **Confirmar estado regulatorio en Argentina**: Buscar en ANMAT con variantes de nombre ("amlodipina", "amlodipine", marcas comerciales) para confirmar si realmente no está comercializado o si se trata de un problema de búsqueda
- **Obtener datos del prospecto**: Resolver la brecha DG001 (severidad bloqueante) descargando el prospecto de la autoridad regulatoria
- **Obtener mecanismo de acción desde DrugBank**: Resolver la brecha DG002 consultando la API de DrugBank con el ID correcto
- **Re-ejecutar pipeline TxGNN**: Una vez resueltas las brechas anteriores, re-ejecutar el modelo predictivo para obtener indicaciones candidatas válidas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

