---
layout: default
title: Amitriptilina
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Amitriptilina
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

# Amitriptilina: Evaluación Preliminar — Sin Indicación Predicha Disponible

## Resumen en Una Frase

Amitriptilina es un antidepresivo tricíclico clásico, ampliamente utilizado a nivel mundial para el tratamiento de la depresión, dolor neuropático y profilaxis de migraña. Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y **no se han identificado autorizaciones de comercialización en Argentina**. La evidencia disponible es insuficiente para avanzar en una evaluación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en el Evidence Pack (conocida: depresión mayor, dolor neuropático) |
| Nueva Indicación Predicha | — Sin predicción disponible — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos preliminares, sin predicción ni estudios asociados) |
| Estado de Mercado en Argentina | ✗ No comercializado (según datos disponibles) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicción Disponible?

Amitriptilina es un antidepresivo tricíclico (TCA) que actúa principalmente inhibiendo la recaptación de serotonina y noradrenalina en la hendidura sináptica. Adicionalmente, posee actividad antagonista sobre receptores histamínicos H1, muscarínicos y alfa-adrenérgicos, lo que explica tanto su perfil terapéutico amplio como sus efectos adversos característicos. A nivel mundial, se utiliza para depresión mayor, dolor neuropático crónico, profilaxis de migraña, insomnio y trastornos de ansiedad.

El Evidence Pack actual presenta **vacíos de datos críticos** que impidieron al modelo TxGNN generar predicciones:
- **No se encontró DrugBank ID** asociado a la búsqueda con el término "AMITRIPTILINA" (posiblemente por diferencia en la denominación: la DCI en inglés es *amitriptyline*).
- **No se registraron indicaciones originales** en el paquete de datos, lo cual limita el punto de partida para el análisis de reposicionamiento.
- **El mecanismo de acción (MOA) figura como dato faltante** en el JSON, aunque es ampliamente conocido en la literatura farmacológica.

Sin la integración correcta del fármaco en el grafo de conocimiento (Knowledge Graph), el modelo TxGNN no puede calcular puntajes de predicción para nuevas indicaciones. Esto no significa que Amitriptilina carezca de potencial de reposicionamiento — de hecho, es uno de los fármacos con mayor historia de uso fuera de indicación (off-label) — sino que los datos de entrada requieren corrección antes de ejecutar el modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack, dado que no se generó una predicción de nueva indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack, dado que no se generó una predicción de nueva indicación.

---

## Información de Mercado en Argentina

No se encontraron autorizaciones de comercialización vigentes para Amitriptilina en la base de datos consultada.

> **Nota:** Amitriptilina es un fármaco ampliamente comercializado a nivel mundial bajo múltiples marcas (Elavil, Tryptanol, entre otros). La ausencia de registros podría deberse a una discrepancia en el término de búsqueda utilizado ("AMITRIPTILINA") o a limitaciones en la fuente de datos consultada. Se recomienda verificar en el registro de ANMAT con variantes del nombre.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el Evidence Pack actual. Como referencia general para Amitriptilina:

- **Advertencias conocidas**: Riesgo de prolongación del intervalo QT, ideación suicida en pacientes jóvenes (Black Box Warning de la FDA), síndrome serotoninérgico en combinación con ISRS/IMAO, efectos anticolinérgicos significativos.
- **Contraindicaciones conocidas**: Uso concomitante con IMAO, fase aguda de recuperación post-infarto de miocardio, hipersensibilidad a antidepresivos tricíclicos.
- **Interacciones relevantes**: IMAO, inhibidores de CYP2D6, depresores del SNC, anticolinérgicos, simpaticomiméticos.

> ⚠️ Consultar el prospecto oficial para información de seguridad completa y actualizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack presenta vacíos de datos críticos (DrugBank ID no vinculado, indicaciones originales ausentes, MOA no cargado) que impidieron al modelo TxGNN generar predicciones de nuevas indicaciones. No es posible evaluar el potencial de reposicionamiento sin resolver estos vacíos.

**Para avanzar se necesita:**
1. **Corregir la vinculación con DrugBank** — Buscar con el término en inglés "amitriptyline" (DrugBank ID esperado: **DB00321**) y re-ejecutar la consulta.
2. **Cargar las indicaciones originales** — Depresión mayor, dolor neuropático, profilaxis de migraña, entre otras.
3. **Incorporar el MOA** — Inhibidor de la recaptación de serotonina-noradrenalina, antagonista H1/muscarínico/alfa-adrenérgico.
4. **Verificar el registro en ANMAT** — Consultar con variantes del nombre (amitriptilina, amitriptyline, clorhidrato de amitriptilina).
5. **Re-ejecutar el pipeline TxGNN** — Una vez corregidos los datos de entrada, generar nuevas predicciones y recopilar evidencia asociada.

---

> ⚠️ *Este informe es solo para fines de investigación y no constituye consejo médico. Los candidatos a reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

