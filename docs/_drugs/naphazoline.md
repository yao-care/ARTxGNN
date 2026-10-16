---
layout: default
title: Naphazoline
parent: Solo Predicción del Modelo (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Naphazoline: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

# Nafazolina: De Indicación Original No Registrada a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Nafazolina es un vasoconstrictor simpaticomimético (agonista alfa-adrenérgico) de uso tópico, comercializado en Argentina en gotas nasales, colirios y gel nasal; los datos compilados no incluyen el texto de la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional (nivel L5) sin sustento mecanístico creíble.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos). Según DrugBank/farmacología, se usa como vasoconstrictor para reducir el enrojecimiento ocular |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en la base de datos. Según la información farmacológica compilada, la nafazolina es un agonista de los receptores adrenérgicos α1A, α2A y α2C (también se registra interacción con un receptor TAAR en ratón). Su efecto es la vasoconstricción, que reduce temporalmente el enrojecimiento ocular al estrechar los vasos sanguíneos inflamados, y la descongestión nasal.

**En este caso la prediccion no resulta mecanisticamente razonable.** La hipotricosis simple del cuero cabelludo es un trastorno de origen genético del folículo piloso, sin relación conocida con la vía alfa-adrenérgica. Además, la vasoconstricción de la microvasculatura del cuero cabelludo cabría esperarla como contraproducente para la perfusión folicular. El puntaje alto probablemente refleja la cercanía en el grafo de conocimiento entre nodos de fenotipos relacionados con el cabello, y no una farmacología real.

Las demás predicciones del modelo siguen el mismo patrón: otras condiciones capilares (hipotricosis congénita con milia, alopecia areata difusa, alopecia, hipertricosis, hipertricosis de Ambras), glaucoma (hereditario primario y de ángulo abierto) y síndromes malformativos (con componente dental/periodontal y con malformación de Dandy-Walker). Ninguna cuenta con ensayos ni literatura que evalúe la nafazolina; la única publicación recuperada (PMID 1295525, glaucoma de ángulo abierto) trata de corticoides tópicos tras trabeculoplastia láser y no estudia nafazolina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha (hipotricosis simple del cuero cabelludo).

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 39532 | NAFAZOLEX | Envase gotero x 20 ml | No disponible |
| 28599 | RHINAL | Gotas x 30 ml | No disponible |
| 174 | MIRUS | Solución oftálmica x 15 ml | No disponible |
| 12536 | RINOGEL | Gel nasal x 15 ml | No disponible |
| 42850 | MIRA KLONAL | Frasco gotero x 5 ml | No disponible |

Se muestran 5 de las 9 autorizaciones vigentes (todas de monodroga, ninguna cancelada). Las restantes corresponden a DRYNISAN, REFENAX COLIRIO, VISUCLAR y REFENAX (gotas nasales).

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de precaución según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, glaucoma de ángulo cerrado, enfermedad cardiovascular y cardiopatías, hipertiroidismo (enfermedad de Graves, tirotoxicosis), enfermedades infecciosas oculares y conjuntivitis.
- **Interacciones farmacológicas**: se registraron 4 interacciones de tipo farmacológico (sin nivel de gravedad asignado), correspondientes a la unión a los receptores adrenérgicos α1A, α2A y α2C, y a un receptor TAAR en ratón. No se identificaron interacciones con otros fármacos.
- **Relevancia para las indicaciones predichas**: el efecto midriático simpaticomimético puede precipitar cierre angular, por lo que la nafazolina no sería adecuada para glaucoma.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura de apoyo, y el mecanismo vasoconstrictor no ofrece una vía plausible hacia el crecimiento del cabello; incluso podría ser desfavorable. No se recomienda avanzar con esta indicación ni con las demás predichas.

**Para avanzar se necesita:**
- Obtener el texto de las indicaciones aprobadas y las advertencias/contraindicaciones del prospecto de ANMAT
- Completar los datos del mecanismo de acción desde DrugBank
- Evidencia preclínica o mecanística que justifique un efecto sobre el folículo piloso (hoy ausente)
- Revisión de literatura dirigida que confirme o descarte la hipótesis
- Evaluar la compatibilidad de vía de administración y formulación para el cuero cabelludo (pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

