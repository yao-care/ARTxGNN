---
layout: default
title: Formoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Formoterol: nueva indicación predicha, Malformación respiratoria (nivel de evidencia L5). Indicación original: Enfisema pulmonar, asma intrínseca y asma alérgica"
---

# Formoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Formoterol: De Enfisema Pulmonar y Asma a Malformación Respiratoria

## Resumen en Una Frase

Formoterol es un agonista beta2-adrenérgico de acción prolongada, utilizado originalmente para el enfisema pulmonar y el asma (intrínseca y alérgica).
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria**, pero **no hay ensayos clínicos** y las **9 publicaciones** recuperadas no estudian esta indicación, por lo que la predicción carece de respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfisema pulmonar, asma intrínseca y asma alérgica (según el grafo de conocimiento; los registros de ANMAT no incluyen el texto de indicación aprobada) |
| Nueva Indicación Predicha | Malformación respiratoria |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, formoterol es un broncodilatador agonista beta2 de acción prolongada que relaja el músculo liso de la vía aérea. Su eficacia en asma y enfisema está comprobada.

Mecanísticamente, este efecto podría aliviar la obstrucción secundaria del flujo de aire en personas con alteraciones estructurales de la vía respiratoria. Sin embargo, no hay evidencia de que el fármaco actúe sobre la malformación en sí.

El puntaje del modelo es muy alto, pero probablemente refleja la cercanía semántica entre términos de enfermedades respiratorias en el grafo y no una relación terapéutica real. Esta predicción debe tratarse como una hipótesis sin respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de las publicaciones recuperadas estudia formoterol en malformaciones respiratorias estructurales. Todas son indirectas o ajenas al tema.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | ECA cruzado | Eur Respir J | Compara salbutamol con budesonida/formoterol repetidos en asma estable (efecto broncodilatador, cardiovascular y eventos adversos). No es malformación |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | ECA (seguridad a largo plazo) | J Allergy Clin Immunol | Seguridad y control del asma con budesonida/formoterol en pacientes afroamericanos con asma. No es malformación |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Revisión sistemática y metaanálisis | J Am Pharm Assoc | Seguridad y eficacia de budesonida/glicopirronio/formoterol frente a glicopirronio/formoterol en EPOC |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Revisión de budesonida/formoterol en inhalador presurizado para asma persistente |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Estudio clínico mecanístico | Eur Respir J | Formoterol protege frente a los efectos del factor activador de plaquetas en asma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Estudio fisiológico | Eur J Appl Physiol | Respuestas compensatorias a las alteraciones mecánicas de la EPOC durante el sueño |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Revisión | Prog Neuropsychopharmacol Biol Psychiatry | Estrategias basadas en neurotransmisores para la disfunción cognitiva en síndrome de Down (fuera de tema) |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Reporte de caso | J Med Case Rep | Enfermedad de la vía aérea pequeña en síndrome post-COVID-19 agudo, seguimiento de tres años |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Reporte de caso y revisión | Medicine | Micosis broncopulmonar alérgica por *Schizophyllum commune* en un paciente con cáncer de pulmón operado |

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de productos con formoterol como único principio activo registrado. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 20365 | OXIS TURBUHALER | 9 mcg, envase x 60 dosis | AstraZeneca |
| 57567 | NEUMOCORT PLUS | Cápsulas con polvo x 120 + aplicador | Cassará |
| 47443 | FORMOVENT + BUDE | Cápsulas para inhalar x 60 sin aplicador | Lab Internacional |
| 57938 | NEUMOTEROL AEROSOL | 160/4.5 x 120 dosis | Elea |
| 43180 | FREVIA | 160/4.5 mcg x 120 dosis | AstraZeneca |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, síndrome de QT largo (incluida la forma familiar), epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, sarampión, queratitis por herpes simple y diversas deficiencias hormonales hipofisarias (hipopituitarismo, déficit de hormona de crecimiento, hipogonadismo hipogonadotrópico, síndrome de Kallmann, síndrome de Sheehan).
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las más relevantes son de nivel **moderado**:
  - Antidiabéticos: acarbosa, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dulaglutida y empagliflozina.
  - Fármacos con riesgo de prolongación del QT o efectos cardiovasculares: cisaprida, claritromicina, dolasetrón, efedrina, isometepteno y dietilpropión.
  - Famotidina.

  Los corticoides inhalados o sistémicos (beclometasona, betametasona, budesonida y dexametasona) figuran como interacciones de nivel **menor**.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje muy alto, pero no hay ensayos clínicos ni literatura que estudien formoterol en malformaciones respiratorias. El nivel de evidencia es L5 y no existe un vínculo mecanístico demostrado.

Cabe señalar que otras predicciones del modelo tienen más respaldo. Para bronquitis, enfermedad pulmonar obstructiva y asma hay numerosos ensayos de Fase 3 y publicaciones de alto nivel, pero son en su mayoría combinaciones con otros fármacos. Además, el asma y la enfermedad obstructiva coinciden con los usos ya aprobados, por lo que confirman el uso existente y no constituyen un reposicionamiento nuevo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que vincule formoterol con la malformación respiratoria.
- Estudios preclínicos o series de casos específicos en esta población.
- Obtener los textos de advertencias, contraindicaciones e indicaciones aprobadas desde los prospectos de ANMAT, para completar la evaluación de seguridad.
- Evaluar si el candidato más prometedor para el reposicionamiento es otro de los predichos (por ejemplo, bronquitis crónica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

