---
layout: default
title: Diltiazem
parent: Solo Predicción del Modelo (L5)
nav_order: 126
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Diltiazem: nueva indicación predicha, Susceptibilidad obsoleta al accidente cerebrovascular isquémico (nivel de evidencia L5). Indicación original: Hipertensión (trastorno hipertensivo), fibrilación …"
---

# Diltiazem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Diltiazem: De Hipertensión a Susceptibilidad Obsoleta al Accidente Cerebrovascular Isquémico

## Resumen en Una Frase

Diltiazem es un bloqueador de los canales de calcio no dihidropiridínico, utilizado originalmente para el tratamiento de la hipertensión, la fibrilación auricular, la angina de Prinzmetal y la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectivo para la **susceptibilidad al accidente cerebrovascular isquémico** (término obsoleto en la ontología), pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión (trastorno hipertensivo), fibrilación auricular, angina de Prinzmetal, taquicardia ventricular |
| Nueva Indicación Predicha | Susceptibilidad obsoleta al accidente cerebrovascular isquémico |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, diltiazem es un bloqueador de los canales de calcio no dihidropiridínico, con eficacia comprobada en hipertensión y arritmias, y mecanísticamente podría ser aplicable al riesgo de accidente cerebrovascular isquémico.

Los vínculos plausibles son: (1) la reducción de la presión arterial, ya que la hipertensión es el principal factor de riesgo modificable del ictus; (2) el control de la frecuencia y el ritmo cardíaco en la fibrilación auricular, una causa mayor de ictus cardioembólico; y (3) posibles efectos vasodilatadores o cerebrovasculares.

Estos vínculos se infieren a partir de las indicaciones ya aprobadas y no han sido demostrados para esta entidad específica. Además, el término de la enfermedad está marcado como "obsoleto", es decir, la entrada en la ontología está en desuso y puede corresponder de forma imprecisa a los fenotipos actuales de ictus. El puntaje alto (0.991) es solo una predicción computacional, probablemente influida por las indicaciones cardiovasculares conocidas del fármaco.

## Informacion de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17872 | ACALIX CD | 240 mg cápsulas x 30 | No disponible en los datos compilados |
| 7577 | ACALIX | 60 mg comprimidos x 50 | No disponible en los datos compilados |
| 8691 | HART | 60 mg comprimidos x 50 | No disponible en los datos compilados |
| 9274 | INCORIL AP 120 | 120 mg comprimidos x 30 | No disponible en los datos compilados |
| 38108 | ACALIX CRONOS | 300 mg cápsulas x 30 | No disponible en los datos compilados |

Se muestran 5 de las 17 autorizaciones vigentes (todas de producto único).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de PrimeKG, no texto de prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (incluido el hereditario), neutropenia, agranulocitosis, estenosis aórtica, hipotensión, miocardiopatía hipertrófica, taquicardia ventricular, bloqueo auriculoventricular, síndrome de Wolff-Parkinson-White, síndrome de Lown-Ganong-Levine y síndrome del seno enfermo.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales, de gravedad **mayor**: loperamida. De gravedad **moderada**: hidrocortisona, pioglitazona, bupropión, aprepitant, triamcinolona, morfina, ácido acetilsalicílico, dexametasona, betametasona, budesonida, canagliflozina y varias sales de calcio (fosfato, acetato, carbonato, cloruro, citrato).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y la enfermedad predicha figura como término obsoleto en la ontología, lo que limita su interpretación.

**Para avanzar se necesita:**
- Mapear el término obsoleto a fenotipos vigentes de ictus isquémico (p. ej., prevención primaria o secundaria).
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisar el prospecto de ANMAT (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Realizar una búsqueda sistemática de literatura y ensayos clínicos sobre diltiazem y riesgo de ictus.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

