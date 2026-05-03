---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

El skill confirma que estoy en el contexto correcto de TxGNN. Procedo a redactar el informe a partir del Evidence Pack proporcionado.

---

# Metoprolol: De Hipertensión Arterial a Nefropatía Hipertensiva Maligna

## Resumen en Una Frase

Metoprolol es un bloqueador selectivo de los receptores β1-adrenérgicos, ampliamente utilizado en el tratamiento de la hipertensión arterial, angina de pecho e insuficiencia cardíaca.
El modelo TxGNN predice que podría ser efectivo para la **Nefropatía Hipertensiva Maligna** (malignant hypertensive renal disease),
sin embargo, actualmente **no se registran ensayos clínicos ni publicaciones** que respalden directamente esta indicación específica.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial (indicación reconocida internacionalmente; sin registro en Argentina) |
| Nueva Indicación Predicha | Nefropatía Hipertensiva Maligna |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en el Evidence Pack. No obstante, metoprolol pertenece a la clase de los bloqueadores β1-adrenérgicos selectivos (beta-bloqueantes cardioselectivos): su eficacia antihipertensiva está comprobada en múltiples países y en grandes ensayos clínicos. Mecanísticamente, actúa inhibiendo los receptores β1 de las células yuxtaglomerulares renales, reduciendo la secreción de renina y, por ende, la activación del sistema renina-angiotensina-aldosterona (SRAA). Esto se traduce en menor presión de perfusión renal y menor resistencia vascular periférica.

La nefropatía hipertensiva maligna se caracteriza patológicamente por necrosis fibrinoide arteriolar y lesión endotelial acelerada. Dado que metoprolol atenúa la activación simpática crónica y reduce la presión intraglomerular a través del bloqueo β1 renal, existe una base mecanística plausible para considerar su rol protector en esta entidad. La hipertensión maligna y la nefropatía hipertensiva ordinaria comparten la misma vía final de daño endovascular, lo que justifica extrapolar el efecto antihipertensivo conocido hacia la variante maligna con afectación renal.

Sin embargo, esta extrapolación debe tomarse con cautela: el bloqueo β puede reducir el filtrado glomerular (FGR) en presencia de daño renal grave, y en la fase aguda de hipertensión maligna se requieren agentes de acción rápida y controlada (nitroprusiato, labetalol IV). El rol de metoprolol oral en el manejo crónico de esta entidad carece de evidencia clínica directa. El alto puntaje de TxGNN (99.91%) probablemente refleja la cercanía nódular entre hipertensión y patología renal hipertensiva en el grafo de conocimiento, más que una relación terapéutica validada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Metoprolol no cuenta con ninguna autorización de comercialización registrada en Argentina según los datos disponibles. El estado de mercado es **No comercializado** (0 autorizaciones).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es biológicamente plausible —el bloqueo β1 reduce la secreción de renina y la presión intraglomerular—, pero no existe ningún ensayo clínico ni publicación que evalúe directamente metoprolol en nefropatía hipertensiva maligna. El nivel de evidencia L4 refleja únicamente soporte mecanístico indirecto; sin datos clínicos propios de esta indicación, avanzar sin investigación adicional no es recomendable.

**Para avanzar se necesita:**
- Obtener datos formales de mecanismo de acción (MOA) vía DrugBank API y ficha técnica TFDA/EMA
- Revisar información de seguridad completa (advertencias, contraindicaciones, interacciones) desde ANMAT y prospectos internacionales
- Realizar búsqueda bibliográfica específica en PubMed con términos: *metoprolol* + *malignant hypertension* + *renal* para descartar literatura no capturada
- Evaluar si los estudios sobre metoprolol en hipertensión grave con daño renal agudo (MAHA, encefalopatía) proporcionan evidencia trasladable
- Considerar si el perfil de seguridad renal permite el uso en pacientes con FGR reducido antes de diseñar cualquier protocolo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

