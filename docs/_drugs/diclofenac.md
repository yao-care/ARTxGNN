---
layout: default
title: Diclofenac
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenaco: De Queratosis Actínica y Artritis Reumatoide a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

El diclofenaco es un antiinflamatorio no esteroideo (AINE) que se usa originalmente para enfermedades articulares como la artritis reumatoide, la osteoartritis y la espondilitis anquilosante, y también para la queratosis actínica.
El modelo TxGNN predice que podría ser efectivo para la **hipotricosis simple del cuero cabelludo**, pero esta predicción cuenta con **0 ensayos clínicos** y **0 publicaciones** que la respalden, por lo que es solo una señal computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Queratosis actínica, artritis reumatoide, osteoartritis y espondilitis anquilosante (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el diclofenaco pertenece a la clase de los AINE, que inhiben las enzimas ciclooxigenasa (COX-1 y COX-2) y reducen la síntesis de prostaglandinas. Su eficacia sintomática en enfermedades inflamatorias articulares está comprobada, y en forma tópica se usa en lesiones cutáneas como la queratosis actínica.

La hipotricosis simple del cuero cabelludo, en cambio, es un trastorno monogénico del folículo piloso, asociado a variantes en genes como CDSN, APCDD1 y RPL21. No se identificó un vínculo mecanístico plausible entre la inhibición de COX y esta enfermedad. El uso tópico del diclofenaco en algunas enfermedades de la piel no se extiende a este trastorno.

Por lo tanto, el puntaje alto del modelo (99.69%) parece ser un artefacto del grafo de conocimiento y no está respaldado por evidencia clínica ni bibliográfica. Debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

El diclofenaco tiene 20 autorizaciones vigentes, todas de producto de un solo principio activo y ninguna cancelada. Se muestran las 5 primeras. Los textos de indicación aprobada no figuran en los datos disponibles.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 30268 | VESALION | 75 mg, comprimidos x 15 | Siegfried |
| 57006 | OXA 75 | Comprimidos recubiertos x 15 | Beta |
| 50302 | METAFLEX 75 CB | Cápsulas blandas x 15 | Montpellier |
| 37442 | OXA 100 | Comprimidos recubiertos x 30 | Beta |
| 2752 | CURINFLAM A.P. | Cápsulas x 15 | Duncan |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia cardíaca congestiva, enfermedad cardiovascular y cardiopatía, infarto de miocardio, accidente cerebrovascular e infarto cerebral, insuficiencia hepática, enfermedad hepática y daño hepático inducido por fármacos, enfermedad de la vesícula biliar, úlcera péptica activa, enfermedad inflamatoria intestinal, asma (intrínseca y alérgica), diabetes mellitus y cetoacidosis diabética, trastornos de la coagulación, hemoglobinopatías y anemias, abuso o dependencia de sustancias, y queratitis.
- **Interacciones farmacológicas**: se detectaron 100 interacciones en total. Entre las principales (según la base DDInter):
  - **Moderadas**:
    - Corticoides: hidrocortisona, triamcinolona, dexametasona, betametasona y budesonida.
    - Antidiabéticos: metformina, acetohexamida, clorpropamida, exenatida, glimepirida y glipizida.
    - Otros: ácido acetilsalicílico, mesalazina, balsalazida, aprepitant, fenfluramina y dexfenfluramina.
  - **Leves**: famotidina, ranitidina y cimetidina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipotricosis simple del cuero cabelludo es solo computacional (nivel L5). No hay ensayos ni publicaciones, y no existe un vínculo mecanístico plausible entre la inhibición de COX y un trastorno genético del folículo piloso. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del diclofenaco desde DrugBank y evidencia preclínica que justifique un efecto sobre el folículo piloso.
- Advertencias y contraindicaciones del prospecto de ANMAT, hoy no disponibles, para completar el análisis de seguridad.
- Los textos de indicación aprobada de las autorizaciones locales.

**Nota adicional:** entre las 10 indicaciones predichas, la única con respaldo bibliográfico es la **artritis idiopática juvenil** (nivel L3, recomendación *Proceed with Guardrails*). Hay estudios clínicos pediátricos con diclofenaco y revisiones sobre el uso de AINE en esta enfermedad. Su papel sería sintomático, no modificador de la enfermedad, y requeriría dosificación pediátrica y monitoreo gastrointestinal, renal y cardiovascular. Esa candidata merece una evaluación separada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

