---
layout: default
title: Indacaterol
parent: Solo Predicción del Modelo (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Indacaterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Indacaterol: De Agonista Beta2 de Acción Ultra-Prolongada a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Indacaterol es un agonista beta2-adrenérgico de acción ultra-prolongada, comercializado en Argentina como Onbrize Breezhaler en cápsulas para inhalación. Las autorizaciones locales no consignan el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consignada en las autorizaciones de ANMAT (fármaco broncodilatador inhalado) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Indacaterol es un agonista beta2-adrenérgico de acción ultra-prolongada. Activa los receptores beta2 del músculo liso de las vías aéreas, aumenta el AMPc y produce broncodilatación sostenida. No se dispone de datos detallados del mecanismo de acción en las fuentes consultadas; esta descripción corresponde al conocimiento farmacológico general de la clase.

El NSIAD está causado por mutaciones activadoras del receptor V2 de vasopresina (AVPR2), que señaliza a través de la vía Gs/AMPc. Mecanísticamente, el agonismo beta2 no suprimiría esta vía y, de hecho, podría sumar señalización de AMPc. **Por lo tanto, no existe una justificación clara de beneficio.** El puntaje alto del modelo no está respaldado por un vínculo biológico identificable.

Hay que interpretar la predicción con cautela. Probablemente refleja asociaciones del grafo de conocimiento y no un efecto terapéutico real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45706 | ONBRIZE BREEZHALER | 300 mcg cáps. p/inh. x30 | No consignada |
| 45705 | ONBRIZE BREEZHALER | 150 mcg cáps. p/inh. x30 | No consignada |

Ambas autorizaciones están vigentes, son de monofármaco y pertenecen a Novartis.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (PrimeKG, no texto de prospecto)**: hipertensión, síndrome de QT largo (incluido el familiar), epilepsia, hiperglucemia, diabetes mellitus, cetoacidosis diabética, déficit de potasio, paro cardíaco súbito, enfermedad de la conducción cardíaca, tirotoxicosis/hipertiroidismo/enfermedad de Graves y enfermedad coronaria.
- **Interacciones farmacológicas** (100 registradas; se resumen las principales):
  - **Moderadas**: antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, saxagliptina), epinefrina, isometepteno, famotidina y claritromicina.
  - **Menores**: corticoides (hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida) y aprepitant.
- Además, la cefalea es un efecto adverso conocido de los agonistas beta2.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para NSIAD carece de ensayos, literatura y mecanismo plausible (L5). Además, el agonismo beta2 podría reforzar la señalización de AMPc que impulsa la enfermedad.

**Para avanzar se necesita:**
- Una hipótesis mecanística sólida que explique cómo un agonista beta2 podría beneficiar el NSIAD, o la descartaría.
- Estudios preclínicos (por ejemplo, en modelos celulares con AVPR2 activado).
- El texto de la indicación aprobada y las advertencias y contraindicaciones del prospecto de ANMAT.
- Datos formales del mecanismo de acción.

**Nota complementaria:** entre las otras predicciones del modelo, la de **enfermedad bronquial** (puntaje 99.18%) tiene respaldo clínico amplio, con ensayos de Fase 3 y literatura sobre asma. Sin embargo, corresponde en gran parte a un uso ya conocido de indacaterol. En asma se respalda sobre todo mediante combinaciones con corticoide inhalado, no como monoterapia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

