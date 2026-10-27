---
layout: default
title: Diazoxide
parent: Solo Predicción del Modelo (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diazoxide: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Hipoglucemia hiperinsulinémica e insulinoma pancreático (según el gra…"
monitor_inn: "diazoxide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "autosomal dominant hyperinsulinism due to Kir6.2 deficiency"]
---

# Diazoxide
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

## Diazóxido: De Hiperinsulinismo/Insulinoma a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Diazóxido es un abridor de canales de potasio sensibles a ATP (KATP), utilizado originalmente para el tratamiento de la hipoglucemia hiperinsulinémica y del insulinoma pancreático.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica (solo predicción del modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipoglucemia hiperinsulinémica e insulinoma pancreático (según el grafo de conocimiento; el texto de indicación aprobado en ANMAT no está disponible) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, el diazóxido abre los canales KATP (a través de SUR1/Kir6.2), lo que reduce la secreción de insulina; por eso es eficaz en el hiperinsulinismo.

La relación con la nueva indicación es indirecta: la apertura de canales KATP en el folículo piloso es el mecanismo que se asocia con el crecimiento del cabello, compartido con el minoxidil. El hipertricosis es un efecto adverso conocido del diazóxido de uso sistémico, lo que sugiere un vínculo plausible a nivel de clase farmacológica.

Sin embargo, esta relación no está validada para la hipotricosis simple genética. El efecto observado como reacción adversa sistémica no demuestra eficacia terapéutica, y no existe evidencia directa en esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la hipotricosis simple del cuero cabelludo.

A modo de contexto, para la indicación predicha de rango 4 (**alopecia**, nivel L4), existe evidencia indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Estudio animal (primate) | J Dermatol Sci | El diazóxido tópico en macacos con calvicie frontal evaluó el efecto sobre el crecimiento folicular y la fisiología, aprovechando el efecto hipertricótico del fármaco |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Revisión | J Invest Dermatol | El minoxidil y el diazóxido tópicos indujeron un rebrote significativo en macacos con alopecia androgenética |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Revisión | Drug Safety | Revisión de la caída y el crecimiento del cabello inducidos por fármacos |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Reporte de caso | Pediatr Dermatol | Hipertricosis generalizada por exposición al minoxidil (no diazóxido); menciona al diazóxido como causa de hipertricosis |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51104 | PROGLICEM | 100 mg x 5 cáps. x 20 | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad renal, insuficiencia renal, uremia, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, insuficiencia cardíaca congestiva, enfermedad coronaria, trastorno cerebrovascular, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, deficiencia de potasio, gota, hiperuricemia y piouréter.
- **Interacciones farmacológicas**: se identificaron 209 interacciones, las 20 mostradas son de nivel moderado. Destacan los antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida, dulaglutida, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, clorpropamida, acetohexamida), corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida), y también bupropión, morfina y dronabinol. Es esperable que el diazóxido reduzca la eficacia de los antidiabéticos al elevar la glucemia.
- **Efectos adversos descritos en la literatura**: hipertricosis, retención de líquidos, insuficiencia cardíaca y enterocolitis necrosante en neonatos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipotricosis simple del cuero cabelludo se basa solo en el modelo (L5), sin ensayos ni literatura. Además, el efecto piloso del diazóxido es un efecto adverso sistémico y no una demostración terapéutica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto de ANMAT (advertencias y contraindicaciones)
- Estudios preclínicos de formulación tópica en modelos de hipotricosis genética
- Evaluación de la seguridad sistémica de una formulación tópica, considerando la absorción
- Priorizar la indicación de **alopecia** (L4, "pregunta de investigación"), que cuenta con un estudio preclínico en primates, antes que las demás predicciones

**Observaciones sobre otras predicciones del modelo:**
- **Hipertricosis** y **Ambras (hipertricosis universal congénita)**: la asociación refleja probablemente el efecto adverso del fármaco; no se recomienda el reposicionamiento.
- **Alopecia areata difusa**: la patología autoinmune no se abordaría con este mecanismo.
- **Hiperinsulinismo autosómico dominante por deficiencia de Kir6.2**: coincide con las indicaciones ya establecidas y no es un reposicionamiento; la respuesta depende de la variante genética.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

