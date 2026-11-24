---
layout: default
title: Naphazoline
parent: Solo Predicción del Modelo (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Nafazolina: De Indicación Original No Registrada a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Nafazolina es un vasoconstrictor simpaticomimético (agonista alfa-adrenérgico) de uso tópico, comercializado en Argentina en gotas nasales, colirios y gel nasal; los datos compilados no incluyen el texto de la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional (nivel L5) sin sustento mecanístico creíble.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos). Según DrugBank/farmacología, se usa como vasoconstrictor para reducir el enrojecimiento ocular |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 9 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en la base de datos. Según la información farmacológica compilada, la nafazolina es un agonista de los receptores adrenérgicos α1A, α2A y α2C (también se registra interacción con un receptor TAAR en ratón). Su efecto es la vasoconstricción, que reduce temporalmente el enrojecimiento ocular al estrechar los vasos sanguíneos inflamados, y la descongestión nasal.

**En este caso la prediccion no resulta mecanisticamente razonable.** La hipotricosis simple del cuero cabelludo es un trastorno de origen genético del folículo piloso, sin relación conocida con la vía alfa-adrenérgica. Además, la vasoconstricción de la microvasculatura del cuero cabelludo cabría esperarla como contraproducente para la perfusión folicular. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas con el cabello, no evidencia biológica ni una farmacología real.

Las demás predicciones del modelo siguen el mismo patrón: otras condiciones capilares (hipotricosis congénita con milia, alopecia areata difusa, alopecia, hipertricosis, hipertricosis de Ambras), glaucoma (hereditario primario y de ángulo abierto) y síndromes malformativos (con componente dental/periodontal y con malformación de Dandy-Walker). Ninguna cuenta con ensayos ni literatura que evalúe la nafazolina; la única publicación recuperada (PMID 1295525, glaucoma de ángulo abierto) trata de corticoides tópicos tras trabeculoplastia láser y no estudia nafazolina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha (hipotricosis simple del cuero cabelludo).

---

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 39532 | NAFAZOLEX | env.gotero x 20 ml | Biosintex Retai | Vigente |
| 28599 | RHINAL | gts.x 30 ml | Microsules Arg. | Vigente |
| 174 | MIRUS | sol.oft.x 15 ml | Alcon | Ya no figura en el listado de PAMI |
| 12536 | RINOGEL | gel nasal x 15 ml | Cassará | Vigente |
| 42850 | MIRA KLONAL | fco.gotero x 5 ml | Klonal | Ya no figura en el listado de PAMI |

La tabla muestra 5 de los 9 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Varios productos, entre ellos MIRUS y MIRA KLONAL de la tabla, ya no figuran en el listado vigente de PAMI (el estado de cada producto figura en la tabla y las cifras en el resumen rápido). Fuera de la tabla figuran DRYNISAN, REFENAX COLIRIO, VISUCLAR y REFENAX (gotas nasales); REFENAX COLIRIO y VISUCLAR tampoco figuran ya en el listado vigente de PAMI.

<!-- review:begin ar-lic-20261117-naphazoline-1 -->

> **Corrección de verificación (2026-11-24)**: Texto original: «Se muestran 5 de las 9 autorizaciones vigentes (todas de monodroga, ninguna cancelada). Las restantes corresponden a DRYNISAN, REFENAX COLIRIO, VISUCLAR y REFENAX (gotas nasales).» Corregido: los productos 174 (MIRUS), 42850 (MIRA KLONAL), 18650 (REFENAX COLIRIO) y 43809 (VISUCLAR) figuraban en el listado de PAMI del 01/03/2026 y ya no figuran en el listado vigente (05/11/2026); varios productos son asociaciones de nafazolina (con feniramina, cromoglicato disódico u otros), no de monodroga. Que un producto ya no figure en el listado de PAMI no significa que su registro en ANMAT esté dado de baja: el estado del registro en ANMAT no está incluido en estos datos. Fuente: [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261117-naphazoline-1 -->

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

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «9 autorizaciones vigentes, ninguna cancelada» → varias ya no figuran en PAMI | Corregido (revisado el 2026-11-24; versión anterior conservada en el registro) | [PAMI – Listado de precios de medicamentos para entidades (datos abiertos; CSV gavade_20261105_024225, PVP PAMI al 05/11/2026)](https://datos.pami.org.ar/dataset/b7a2600f-94e0-48ba-8042-0cd4b556423b/resource/59b035cf-09b3-4058-b06b-8e49b99fa698/download/gavade_20261105_024225.csv); [PAMI – Medicamentos para entidades (ficha del conjunto de datos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

