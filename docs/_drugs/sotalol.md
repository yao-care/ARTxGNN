---
layout: default
title: Sotalol
parent: Solo Predicción del Modelo (L5)
nav_order: 229
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Sotalol: nueva indicación predicha, Síndrome del seno enfermo tipo 2, autosómico dominante (nivel de evidencia L5). Indicación original: Fibrilación auricular"
monitor_inn: "SOTALOL"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
---

# Sotalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Sotalol: De Fibrilación Auricular a Síndrome del seno enfermo tipo 2, autosómico dominante
{: .text-alpha }

## Resumen en Una Frase

Sotalol es un antiarrítmico de clase III con acción betabloqueante, originalmente utilizado para el tratamiento de la fibrilación auricular.
El modelo TxGNN predice que podría ser efectivo para el **síndrome del seno enfermo tipo 2, autosómico dominante**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación auricular |
| Nueva Indicación Predicha | Síndrome del seno enfermo tipo 2, autosómico dominante |
| Puntaje de Predicción TxGNN | 0.9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sotalol (traducción no oficial): «El sotalol tiene propiedades antiarrítmicas tanto de bloqueo de los receptores beta-adrenérgicos (clase II de Vaughan Williams) como de prolongación de la duración del potencial de acción cardíaco (clase III de Vaughan Williams). Los dos isómeros del sotalol tienen efectos antiarrítmicos de clase III similares, mientras que el isómero l es responsable de prácticamente toda la actividad betabloqueante.» Texto original en inglés: "Sotalol has both beta-adrenoreceptor blocking (Vaughan Williams Class II) and cardiac action potential duration prolongation (Vaughan Williams Class III) antiarrhythmic properties. The two isomers of sotalol have similar Class III antiarrhythmic effects, while the l-isomer is responsible for virtually all of the beta-blocking activity." ([DailyMed: Betapace (sotalol hydrochloride) prescribing information, Legacy Pharma USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6a7702f-36c9-45db-b640-453dc324baee), versión del 2024-12-16; consultado el 2026-11-19). Según la información conocida, sotalol es un antiarrítmico de clase III que además bloquea los receptores beta-adrenérgicos. Su eficacia en la fibrilación auricular está establecida y, en teoría, podría relacionarse con otras alteraciones del ritmo cardíaco.

Sin embargo, la relación mecanística con el nuevo candidato es **débil y potencialmente desfavorable**. El síndrome del seno enfermo es una disfunción del nodo sinusal. Sotalol suprime la actividad del nodo sinusal y puede causar bradicardia, por lo que en esta enfermedad suele estar contraindicado si no hay marcapasos.

El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento con genes de arritmias (por ejemplo, HCN4), y no un beneficio terapéutico real. Esta predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 29548 | SOTACOR | 160 mg comp.x 20 | Siegfried | Vigente |
| 29546 | SOTACOR | 80 mg comp.x 20 | Siegfried | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Las dos autorizaciones están vigentes y corresponden a productos de principio activo único. Los registros disponibles no incluyen el texto de la indicación aprobada.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): síndrome de QT largo (incluida la forma familiar), torsades de pointes, asma (intrínseca y alérgica), enfermedad bronquial, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, trastornos hipotensivos, insuficiencia renal, bloqueo auriculoventricular, **síndrome del seno enfermo (incluida la forma familiar)** y anafilaxia.
  - La contraindicación en el síndrome del seno enfermo coincide con la indicación predicha, lo que es una señal de alerta importante.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las de nivel **mayor** que aparecen en los datos disponibles están:
  - Epinefrina
  - Claritromicina
  - Ácido picosulfúrico
  - Polietilenglicol 3350 con electrolitos

  También hay numerosas interacciones de nivel moderado (por ejemplo, famotidina, atropina, hioscina, loperamida, bupropión, morfina, cimetidina, canagliflozina, dapagliflozina y clorpropamida) y una menor (ácido acetilsalicílico).

Para advertencias y precauciones completas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura. El mecanismo de sotalol (supresión del nodo sinusal, bradicardia) va en contra de un beneficio en el síndrome del seno enfermo, que además figura como contraindicación. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde fuentes como DrugBank
- Advertencias y contraindicaciones del prospecto de ANMAT
- Estudios preclínicos o clínicos que justifiquen un beneficio en esta enfermedad, algo poco probable dado el perfil farmacológico

**Nota adicional:** entre las demás predicciones del modelo, "trastorno de accidente cerebrovascular" (puntaje 0.9944) tiene un ensayo de Fase 3 completado (NCT00007605, n=706) y literatura de apoyo. Esa evidencia trata del manejo de la fibrilación auricular, no de la prevención o el tratamiento del ACV como desenlace, y se superpone con la indicación original. Por lo tanto, no constituye una oportunidad de reposicionamiento diferenciada.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Betapace (sotalol hydrochloride) prescribing information, Legacy Pharma USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6a7702f-36c9-45db-b640-453dc324baee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

