---
layout: default
title: Haloperidol
parent: Solo Predicción del Modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Haloperidol: nueva indicación predicha, Trastorno congénito de la glicosilación con fucosilación defectuosa (nivel de evidencia L5). Indicación original: Trastorno psicótico (también esquizofrenia…"
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Haloperidol
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

# Haloperidol: De Trastorno Psicótico a Trastorno Congénito de la Glicosilación con Fucosilación Defectuosa

## Resumen en Una Frase

Haloperidol es un antipsicótico clásico, utilizado originalmente para el tratamiento de trastornos psicóticos, esquizofrenia y síndrome de Tourette.
El modelo TxGNN predice que podría ser efectivo para el **trastorno congénito de la glicosilación con fucosilación defectuosa**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno psicótico (también esquizofrenia, trastorno esquizoafectivo y síndrome de Tourette, según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Trastorno congénito de la glicosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, haloperidol es un antagonista del receptor de dopamina D2 y su eficacia en psicosis y esquizofrenia está bien establecida.

Sin embargo, el análisis no identifica ningún vínculo mecanístico entre el bloqueo dopaminérgico y las vías de fucosilación de proteínas. El puntaje alto del modelo (99.91%) refleja únicamente la estructura del grafo de conocimiento, no evidencia biológica ni clínica. No hay similitud evidente entre la indicación original (un trastorno psiquiátrico) y la nueva (un trastorno metabólico congénito de la glicosilación).

Por lo tanto, esta predicción debe considerarse una hipótesis sin respaldo mecanístico. Entre las demás predicciones del modelo, la de trastorno bipolar maníaco sí cuenta con evidencia sustancial, aunque corresponde a un uso ya establecido en la práctica clínica y no a un reposicionamiento novedoso. Ese caso requeriría un informe propio.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se listan 5 de las 20 autorizaciones vigentes (todas de producto único, ninguna cancelada). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 9662 | HALOPERIDOL MEDIPHARMA | 10 mg comprimidos x 30 | Medipharma |
| 26686 | NEUPRAM | 1 mg comprimidos x 30 | Sidus |
| 32796 | ENABRAN | 10 mg comprimidos x 60 | Casasco |
| 3974 | HALOPIDOL | 1 mg comprimidos x 100 | Janssen-Cilag |
| 26690 | NEUPRAM | 10 mg comprimidos x 30 | Sidus |

El portafolio local incluye además formas inyectables (decanoato de haloperidol), solución oral y gotas.

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): síndrome de QT largo (incluida la forma familiar), torsades de pointes, epilepsia, enfermedades de los ganglios basales, distonía focal de la mano, blefaroespasmo, enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo y mixedema, deficiencia de potasio, neutropenia y agranulocitosis (incluidas múltiples formas congénitas), leucopenia, trastornos hipotensivos, carcinoma de mama femenino y síndrome neuroléptico maligno.
- **Interacciones farmacológicas**: se registran 100 interacciones. Las de nivel **mayor** entre las primeras listadas son:
  - Bupropión
  - Morfina
  - Claritromicina
  - Dolasetrón

  Hay además interacciones de nivel moderado, por ejemplo con famotidina, epinefrina, hidrocortisona, anfotericina B, loperamida, aprepitant, atropina y varios anticolinérgicos o laxantes.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en el modelo, pero no cuenta con ningún ensayo clínico, publicación ni vínculo mecanístico plausible (nivel de evidencia L5). Además, el perfil de seguridad de haloperidol (riesgo de QT largo, neutropenia, efectos extrapiramidales) exige una justificación sólida antes de explorar un uso nuevo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que permitan evaluar una conexión con las vías de glicosilación y fucosilación
- Estudios preclínicos que justifiquen la hipótesis
- Revisión del prospecto aprobado por ANMAT para completar la información de advertencias y contraindicaciones
- Considerar la evaluación por separado de la indicación de manía bipolar, que cuenta con mayor respaldo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

