---
layout: default
title: Amlodipina
parent: Solo Predicción del Modelo (L5)
nav_order: 29
evidence_level: L5
indication_count: 9
drugbank_id: DB00381
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-20
description: "Amlodipina: nueva indicación predicha, Infarto del tronco encefálico (brain stem infarction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Amlodipina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Amlodipina: Infarto del tronco encefálico (brain stem infarction)
{: .text-alpha }

## Resumen en Una Frase

Amlodipino es un bloqueador de canales de calcio dihidropiridínico con efecto vasodilatador y reductor de la presión arterial, y se comercializa en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para **infarto del tronco encefálico (brain stem infarction)**.
Hasta ahora no hay **ningún ensayo clínico ni publicación** que estudie directamente esta indicación, por lo que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infarto del tronco encefálico (brain stem infarction) |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amlodipina (traducción no oficial): «La amlodipina es un antagonista del calcio de tipo dihidropiridínico (antagonista de los iones calcio o bloqueante de los canales lentos) que inhibe el flujo transmembrana de entrada de iones calcio al músculo liso vascular y al músculo cardíaco. Los datos experimentales sugieren que la amlodipina se une tanto a los sitios de unión dihidropiridínicos como a los no dihidropiridínicos.» Texto original en inglés: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), versión del 2026-09-28; consultado el 2026-11-19). Por conocimiento general, amlodipino bloquea los canales de calcio de tipo L en el músculo liso vascular. Esto produce vasodilatación y reduce la resistencia vascular periférica y la presión arterial.

Como la hipertensión es un factor de riesgo central de la enfermedad cerebrovascular isquémica, es plausible que un fármaco que reduce la presión arterial disminuya el riesgo de eventos como el infarto del tronco encefálico. Este razonamiento es hipotético. Los datos compilados no incluyen estudios que lo confirmen para esta enfermedad en particular.

El puntaje 0.9994 es una salida del modelo y no sustituye la evidencia clínica. No hay ensayos ni literatura que respalden la predicción, por lo que el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

La lista puede ser parcial. El texto de indicación aprobada no figura en los datos locales. A continuación se muestran cinco autorizaciones como ejemplo:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 13687 | TERLOC | 5 mg comp. x 30 | Siegfried |
| 52012 | BRANCILINA | 5 mg comp. x 30 | Fecofar |
| 41319 | AMLODIPINA DENVER FARMA | 10 mg comp. x 30 | Denver Farma |
| 27041 | ZUNDIC | 5 mg comp. x 30 | Nolter |
| 28048 | ILDUC | 5 mg comp. ran. x 30 | Baliarda |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para infarto del tronco encefálico no cuenta con ensayos clínicos ni publicaciones que la respalden (nivel L5). El puntaje alto del modelo no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Revisar la literatura y los registros de ensayos en busca de estudios que evalúen amlodipino específicamente en infarto del tronco encefálico o isquemia de la circulación posterior.
- Obtener datos del mecanismo de acción desde una fuente de referencia farmacológica.
- Descargar y analizar el prospecto de ANMAT para completar la evaluación de advertencias y contraindicaciones.
- Definir un plan de seguridad (control de hipotensión y eventos adversos) antes de cualquier evaluación clínica.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

