---
layout: default
title: Varenicline
parent: Solo Predicción del Modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Varenicline: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

## Vareniclina: De Indicación Original No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Vareniclina (comercializada en Argentina como CHAMPIX) es un fármaco que cuenta con autorizaciones vigentes de ANMAT; los datos compilados para este informe no incluyen el texto de su indicación aprobada. Su uso conocido en la bibliografía es como ayuda para dejar de fumar.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero **no existen ensayos clínicos** ni publicaciones que respalden esta dirección: la única publicación vinculada es un reporte de caso sobre paro cardíaco, que es una señal de seguridad y no de eficacia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Varenicline (traducción no oficial): «La vareniclina se une con alta afinidad y selectividad a los receptores nicotínicos neuronales de acetilcolina α4β2. Se cree que la eficacia de CHANTIX para dejar de fumar es el resultado de la actividad de la vareniclina en el subtipo α4β2 del receptor nicotínico, donde su unión produce actividad agonista y, al mismo tiempo, impide la unión de la nicotina a estos receptores.» Texto original en inglés: "Varenicline binds with high affinity and selectivity at α4β2 neuronal nicotinic acetylcholine receptors. The efficacy of CHANTIX in smoking cessation is believed to be the result of varenicline's activity at α4β2 sub-type of the nicotinic receptor where its binding produces agonist activity, while simultaneously preventing nicotine binding to these receptors." ([DailyMed: Chantix (varenicline tartrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ff4f27-5185-4881-a749-c6b7a0ca5696), versión del 2026-01-23; consultado el 2026-11-19). Según la información conocida de la literatura, la vareniclina es un agonista parcial de los receptores nicotínicos de acetilcolina α4β2 y un agonista pleno de los receptores α7. Esta actividad ayuda a reducir el deseo de fumar y los síntomas de abstinencia.

Desde el punto de vista mecanístico, la señalización colinérgica nicotínica podría modular las vías trigeminovasculares y la depresión cortical propagada, por lo que un vínculo con la migraña es biológicamente plausible, aunque **no está demostrado**. El puntaje de TxGNN es muy alto (0.999), pero es solo una predicción del modelo.

Es necesario tener cautela: la cefalea y la migraña son efectos adversos conocidos de la vareniclina, por lo que la señal clínica podría apuntar en sentido opuesto. Además, la relación entre la indicación original y la nueva no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Reporte de caso | Therapie | Paro cardíaco asociado a vareniclina; es una señal de seguridad, no evidencia de eficacia en migraña |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43437 | CHAMPIX | Kit tratamiento completo | No disponible |
| 41101 | CHAMPIX | Comprimidos de 1 mg x 56 | No disponible |
| 43436 | CHAMPIX | Kit de inicio | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto)**: trastorno de ansiedad, trastorno neurótico, trastorno distímico, trastorno bipolar, trastorno afectivo mayor, abuso/dependencia de sustancias, síndrome coronario agudo, enfermedad vascular periférica, claudicación vascular intermitente, enfermedad arterial periférica y esquizofrenia.
- **Interacciones Farmacológicas**: se identificaron 104 interacciones en total. La mayoría no tiene nivel de gravedad clasificado. Entre las listadas figuran cimetidina (menor), y sin clasificar: vitamina A, fentermina, pantoprazol, glimepirida, mesalazina, doxiciclina, morfina, metformina, omeprazol, palonosetrón, rosiglitazona, lansoprazol, vancomicina, lactulosa, nizatidina, triamcinolona, prednisona, simvastatina y epinefrina.
- **Señales de la literatura**: reporte de paro cardíaco, cefalea inducida por el baño y exantema difuso asociados a vareniclina.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto de ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura de eficacia, y la cefalea/migraña figura como efecto adverso conocido del fármaco. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT para confirmar la indicación aprobada, las advertencias y las contraindicaciones.
- Completar los datos del mecanismo de acción y analizar su vínculo con la fisiopatología de la migraña.
- Revisar la señal de cefalea/migraña como evento adverso (por ejemplo, con datos de farmacovigilancia).
- Realizar estudios preclínicos o ensayos exploratorios que evalúen eficacia en migraña antes de considerar cualquier avance.
- Evaluar la compatibilidad de vía de administración y la relevancia de las contraindicaciones neuropsiquiátricas y cardiovasculares.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Chantix (varenicline tartrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ff4f27-5185-4881-a749-c6b7a0ca5696) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

