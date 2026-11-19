---
layout: default
title: Lansoprazol
parent: Solo Predicción del Modelo (L5)
nav_order: 225
evidence_level: L5
indication_count: 1
drugbank_id: DB00448
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-16
description: "Lansoprazol: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Lansoprazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Lansoprazol: obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Lansoprazol es un inhibidor de la bomba de protones que reduce la secreción de ácido gástrico.
El modelo TxGNN predice que podría ser efectivo para **obstrucción duodenal (duodenal obstruction)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0.9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lansoprazol es un inhibidor de la bomba de protones, es decir, disminuye la producción de ácido en el estómago. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lansoprazol (traducción no oficial): «El lansoprazol pertenece a una clase de compuestos antisecretores, los bencimidazoles sustituidos, que suprimen la secreción de ácido gástrico mediante la inhibición específica del sistema enzimático (H +, K + )-ATPasa en la superficie secretora de la célula parietal gástrica. Dado que este sistema enzimático se considera la bomba de ácido (de protones) dentro de la célula parietal, el lansoprazol se ha caracterizado como un inhibidor de la bomba de ácido gástrico, ya que bloquea el paso final de la producción de ácido.» Texto original en inglés: "Lansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the parietal cell, lansoprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84), versión del 2025-07-08; consultado el 2026-11-19).

Una posible relación es indirecta: al reducir la carga ácida, podría aliviar la lesión péptica (por ejemplo, úlcera duodenal con inflamación o edema asociados), que a veces contribuye a una obstrucción duodenal. En ese caso, la obstrucción sería una consecuencia secundaria de la enfermedad péptica y no un blanco directo del fármaco.

Es importante ser cautos: las obstrucciones de causa mecánica (tumores malignos, páncreas anular, estenosis fibrosas) no se esperaría que respondan a la supresión ácida. El puntaje alto es únicamente una predicción del modelo y no está respaldado por estudios reales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 32657 | LANZOPRAL (Roemmers) | Suspensión, sobres x 30 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones que estudien directamente la obstrucción duodenal, y el mecanismo propuesto es indirecto y no aplicable a obstrucciones mecánicas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), pendiente de forma bloqueante
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda de literatura y ensayos específicos sobre obstrucción duodenal
- Definir si existe una subpoblación (obstrucción de origen péptico) donde la hipótesis sea plausible
- Evaluar la compatibilidad de la vía de administración para la nueva indicación

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

