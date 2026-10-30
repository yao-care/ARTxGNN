---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
last_modified_at: 2026-10-30
description: "Imipenem: nueva indicación predicha, esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Imipenem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Imipenem: antibiótico carbapenémico → esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico de uso intravenoso, con una autorización vigente en Argentina. El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa (diffuse scleroderma)**, pero no hay ensayos clínicos ni publicaciones que respalden esta dirección; la predicción se apoya únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Por conocimiento general, imipenem es un carbapenémico que inhibe la síntesis de la pared celular bacteriana mediante la unión a proteínas fijadoras de penicilina (PBP), con amplio espectro frente a bacterias Gram-negativas, Gram-positivas y anaerobias.

La esclerodermia difusa es una enfermedad autoinmune y fibrótica, sin un componente infeccioso bacteriano que un antibiótico pueda tratar. El análisis de los datos compilados no identifica ningún vínculo mecanístico plausible entre la acción antibacteriana de imipenem y la fisiopatología de esta enfermedad.

El puntaje alto del modelo (0,9999) probablemente refleja un artefacto de las asociaciones del modelo y no una señal biológica. No hay ensayos clínicos ni literatura que lo sustenten, por lo que debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38546 | IMIPENEM FABRA | 500 mg IV polvo para inyección x 1 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (15 interacciones registradas):
  - **Mayores**: bupropión, iohexol, iopamidol.
  - **Moderadas**: warfarina, dicumarol, teofilina, aminofilina, dilfilina, oxtrifilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexed, lindano, polietilenglicol (3350 con electrolitos).

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción carece de ensayos clínicos y de literatura, y no existe un mecanismo plausible que vincule un antibiótico con una enfermedad autoinmune fibrótica. Con evidencia en nivel L5, no se justifica avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que conecte la acción de imipenem con la fisiopatología de la esclerodermia difusa.
- Datos preclínicos que respalden dicha hipótesis.
- Revisión del prospecto aprobado para completar la información de seguridad (advertencias y contraindicaciones).
- Confirmar con los datos del mecanismo de acción (MOA) de DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

