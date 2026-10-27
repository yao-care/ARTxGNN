---
layout: default
title: Sotalol
parent: Solo Predicción del Modelo (L5)
nav_order: 229
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Sotalol: nueva indicación predicha, Síndrome del seno enfermo tipo 2, autosómico dominante (nivel de evidencia L5). Indicación original: Fibrilación auricular"
monitor_inn: "SOTALOL"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation", "obsolete susceptibility to ischemic stroke"]
---

# Sotalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Sotalol: De Fibrilación Auricular a Síndrome del Seno Enfermo Tipo 2 (Autosómico Dominante)
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
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, sotalol es un antiarrítmico de clase III que además bloquea los receptores beta-adrenérgicos. Su eficacia en la fibrilación auricular está establecida y, en teoría, podría relacionarse con otras alteraciones del ritmo cardíaco.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 29548 | SOTACOR | Comprimidos de 160 mg x 20 | Siegfried |
| 29546 | SOTACOR | Comprimidos de 80 mg x 20 | Siegfried |

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

**Nota adicional:** entre las demás predicciones del modelo, "trastorno de accidente cerebrovascular" (puntaje 99.44%) tiene un ensayo de Fase 3 completado (NCT00007605, n=706) y literatura de apoyo. Esa evidencia trata del manejo de la fibrilación auricular, no de la prevención o el tratamiento del ACV como desenlace, y se superpone con la indicación original. Por lo tanto, no constituye una oportunidad de reposicionamiento diferenciada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

