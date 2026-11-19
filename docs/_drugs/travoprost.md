---
layout: default
title: Travoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
last_modified_at: 2026-10-30
description: "Travoprost: nueva indicación predicha, calcifilaxis visceral (visceral calciphylaxis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 8 (en el listado vigente: 8)"
---

# Travoprost
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

## Travoprost: análogo de prostaglandina F2-alfa (agonista del receptor FP) → calcifilaxis visceral (visceral calciphylaxis)
{: .text-alpha }

## Resumen en Una Frase

Travoprost es un análogo de prostaglandina F2-alfa que se comercializa en Argentina como colirio.
El modelo TxGNN predice que podría ser efectivo para **calcifilaxis visceral (visceral calciphylaxis)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que estudien directamente esta enfermedad; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | calcifilaxis visceral (visceral calciphylaxis) |
| Puntaje de Predicción TxGNN | 1,0000 (0,99999845 sin redondear a 4 decimales: 1,0000) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (8 de 8) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 8 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Travoprost (traducción no oficial): «El ácido libre de travoprost, un análogo de prostaglandina, es un agonista selectivo del receptor prostanoide FP que, según se cree, reduce la PIO al aumentar el flujo de salida uveoescleral. En este momento se desconoce el mecanismo de acción exacto.» Texto original en inglés: "Travoprost free acid, a prostaglandin analog is a selective FP prostanoid receptor agonist, which is believed to reduce IOP by increasing uveoscleral outflow. The exact mechanism of action is unknown at this time." ([DailyMed: Travoprost Ophthalmic Soluton (travoprost) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498a376e-a74e-48d8-a022-ad15a1ecadb5), versión del 2026-09-28; consultado el 2026-11-19). Por su clase, travoprost es un análogo de prostaglandina F2-alfa que actúa sobre el receptor FP, y se usa por vía oftálmica tópica.

No se identifica un vínculo mecanístico establecido entre la agonía del receptor FP y las vías de calcificación vascular que caracterizan a la calcifilaxis visceral. Además, la administración ocular tópica genera una exposición sistémica baja, lo que vuelve poco verosímil un efecto vascular sistémico relevante.

El puntaje elevado del modelo debe interpretarse como una señal exploratoria y no como una justificación biológica. Sin estudios que lo respalden, la hipótesis no puede evaluarse más allá de su plausibilidad computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para calcifilaxis visceral.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para calcifilaxis visceral.

## Información de Mercado en Argentina

Todas las autorizaciones registradas están vigentes (8 de 8). Productos principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38893 | ARVO | Solución oftálmica x 2,5 ml | No registrada en los datos locales |
| 43391 | GLAUNOT | Solución oftálmica x 2,5 ml | No registrada en los datos locales |
| 32252 | GLAUCOPROST | Solución oftálmica x 3 ml | No registrada en los datos locales |
| 56010 | TRAVOPLOS | Solución oftálmica x 5 ml | No registrada en los datos locales |
| 52151 | GLAUNOT SC | Solución oftálmica x 2,5 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 49 posibles interacciones, todas con nivel de gravedad sin clasificar (por ejemplo, con calcitriol, pantoprazol, metformina, prednisona y ácido acetilsalicílico). No hay información sobre su relevancia clínica para el uso oftálmico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ningún ensayo ni publicación que estudie la calcifilaxis visceral, no existe un vínculo mecanístico plausible, y la exposición sistémica con el uso ocular tópico es mínima. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de travoprost y análisis de su relación con la calcificación vascular
- Estudios preclínicos que evalúen un efecto sobre la calcificación vascular
- Evaluación de la viabilidad de la vía de administración, dada la formulación oftálmica y la baja exposición sistémica
- Texto del prospecto con advertencias y contraindicaciones (actualmente no disponible)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Travoprost Ophthalmic Soluton (travoprost) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498a376e-a74e-48d8-a022-ad15a1ecadb5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

