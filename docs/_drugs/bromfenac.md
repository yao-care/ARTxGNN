---
layout: default
title: Bromfenac
parent: Evidencia Alta (L1-L2)
nav_order: 63
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-30
description: "Bromfenac: nueva indicación predicha, Enfermedad ocular (eye disease) (nivel de evidencia L1). Indicación original: No disponible (los textos de indicación de las autorizaciones están v…"
monitor_inn: "BROMFENAC"
predicted_indications: ["eye disease", "optic papillitis", "von Hippel anomaly", "mcpherson robertson cammarano syndrome", "vulvar inverted follicular keratosis", "lagophthalmos", "microblepharon-ablephara syndrome", "seborrheic keratosis", "conjunctival degeneration", "luxation of globe"]
---

# Bromfenac
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

## Bromfenaco: De Indicación Original No Registrada a Enfermedad Ocular
{: .text-alpha }

## Resumen en Una Frase

Bromfenaco es un antiinflamatorio no esteroideo (AINE) de uso oftálmico, comercializado en Argentina en solución oftálmica. Los datos compilados no incluyen el texto de la indicación aprobada en ANMAT.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ocular** (categoría amplia), con **38 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe aclarar que gran parte de esa evidencia corresponde a usos oftálmicos ya establecidos, como la cirugía de cataratas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Enfermedad ocular (eye disease) |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 4 (vigentes: 4) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, el bromfenaco es un AINE tópico que inhibe la ciclooxigenasa (COX-1/COX-2) y reduce la síntesis de prostaglandina E2, un mediador clave de la inflamación ocular.

La etiqueta "enfermedad ocular" es muy amplia y abarca sobre todo usos oftálmicos ya establecidos: inflamación y dolor tras cirugía de cataratas y edema macular cistoide. Las subindicaciones más claramente relevantes para el reposicionamiento son el **ojo seco** (ensayo de Fase 3 NCT01212471, n=840) y las **maculopatías impulsadas por VEGF** (ensayo de Fase 2 NCT00805233 y un metaanálisis de 2024). Como el campo de indicaciones originales está vacío, no es posible confirmar cuáles de estos usos ya figuran en la etiqueta local.

Otras predicciones del modelo con puntajes igualmente altos (papilitis óptica, anomalía de von Hippel, queratosis seborreica, entre otras) tienen evidencia nula o solo indirecta. Por ello, deben considerarse únicamente como señales del modelo, sin respaldo mecanístico en los datos.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes (de un total de 38 registrados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01212471](https://clinicaltrials.gov/study/NCT01212471) | Fase 3 | Completado | 840 | Estudio de rango de dosis de seguridad y eficacia de bromfenaco oftálmico en ojo seco; evidencia directa más sólida |
| [NCT00198445](https://clinicaltrials.gov/study/NCT00198445) | Fase 3 | Completado | 527 | Bromfenaco vs. placebo en inflamación ocular tras cirugía de cataratas |
| [NCT01367249](https://clinicaltrials.gov/study/NCT01367249) | Fase 3 | Completado | 440 | Bromfenaco vs. placebo en inflamación y dolor asociados a cirugía de cataratas |
| [NCT01774474](https://clinicaltrials.gov/study/NCT01774474) | Fase 3 | Completado | 1127 | Prevención de edema macular tras cirugía de cataratas, en pacientes con y sin diabetes |
| [NCT00805233](https://clinicaltrials.gov/study/NCT00805233) | Fase 2 | Completado | 30 | Ranibizumab + bromfenaco vs. ranibizumab solo en DMAE neovascular; prueba directa de hipótesis de reposicionamiento |
| [NCT00758784](https://clinicaltrials.gov/study/NCT00758784) | Fase 2 | Completado | 38 | Solución oftálmica en ojo seco; pequeño, debe confirmarse que corresponda a bromfenaco |
| [NCT00423007](https://clinicaltrials.gov/study/NCT00423007) | Fase 3 | Completado | 90 | Bromfenaco vs. placebo en pacientes con antecedente de conjuntivitis alérgica |
| [NCT03521791](https://clinicaltrials.gov/study/NCT03521791) | Fase 4 | Completado | 166 | PRO-155 (bromfenaco 0.09%) vs. placebo en inflamación conjuntival por pterigión grado I-III |
| [NCT00520260](https://clinicaltrials.gov/study/NCT00520260) | Fase 4 | Completado | 42 | Bromfenaco vs. ketorolaco durante la inducción con ciclosporina tópica en ojo seco crónico |
| [NCT07090044](https://clinicaltrials.gov/study/NCT07090044) | Fase 4 | Completado | 77 | Dolor tras inyección intravítrea: loteprednol, bromfenaco y lágrimas artificiales |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39180057](https://pubmed.ncbi.nlm.nih.gov/39180057/) | 2024 | Metaanálisis | BMC Ophthalmology | Bromfenaco tópico como adyuvante del tratamiento anti-VEGF en maculopatías |
| [31343372](https://pubmed.ncbi.nlm.nih.gov/31343372/) | 2019 | ECA | Expert Opin Pharmacother | Eficacia y seguridad de bromfenaco 0.075% (DuraSite) en dolor e inflamación tras cataratas |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Revisión sistemática | Cochrane Database Syst Rev | AINE tópicos para edema macular quístico diabético |
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Revisión sistemática con metaanálisis en red | Eye | Comparación de AINE tópicos sobre edema macular y resultado visual tras facoemulsificación |
| [19735215](https://pubmed.ncbi.nlm.nih.gov/19735215/) | 2009 | Revisión | Expert Opin Pharmacother | Utilidad oftálmica del bromfenaco tópico con dosificación dos veces al día |
| [26068607](https://pubmed.ncbi.nlm.nih.gov/26068607/) | 2015 | Estudio clínico | Asia Pac J Ophthalmol | Eficacia del bromfenaco en ojo seco insuficientemente controlado con lágrimas artificiales |
| [37083870](https://pubmed.ncbi.nlm.nih.gov/37083870/) | 2023 | Estudio clínico | Int Ophthalmol | Bromfenaco tópico adyuvante con ranibizumab intravítreo en edema macular diabético |
| [17445902](https://pubmed.ncbi.nlm.nih.gov/17445902/) | 2007 | Estudio clínico | Ophthalmology | Bromfenaco 0.09% en dolor e inflamación postoperatorios tras extracción de catarata |
| [38920673](https://pubmed.ncbi.nlm.nih.gov/38920673/) | 2024 | Preclínico (animal) | Cells | Reducción de la neuroinflamación en un modelo de glaucoma por isquemia-reperfusión |
| [30908581](https://pubmed.ncbi.nlm.nih.gov/30908581/) | 2019 | Preclínico (in vitro) | Invest Ophthalmol Vis Sci | Inhibición de efectos fibróticos inducidos por TGF-β1 en fibroblastos de pterigión y conjuntiva |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51088 | BERLOFEN (Elea) | Solución oftálmica x 5 ml | No disponible |
| 49273 | FENAC (Max Vision) | Solución oftálmica estéril x 5 ml | No disponible |
| 40085 | NATAX (Poen) | Frasco gotero x 5 ml | No disponible |
| 58196 | OFTALFENAC (Denver Farma) | Solución oftálmica x 5 ml | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: artritis reumatoide, diabetes mellitus y cetoacidosis diabética.
- **Señales de seguridad en la literatura**: casos de fusión y perforación corneal (incluso en síndrome de Stevens-Johnson y síndrome de Sjögren no diagnosticado) y un caso de necrólisis epidérmica tóxica con gotas de bromfenaco sódico. El bromfenaco sistémico fue retirado del mercado por hepatotoxicidad grave; este riesgo se describe para la vía oral y no está demostrado para el uso tópico.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - Moderadas: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), ácido acetilsalicílico, mesalazina, balsalazida, metformina, clorpropamida, glimepirida, vancomicina, kanamicina, citrato y bicarbonato de potasio.
  - Leves: cimetidina, linaclotida.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados con bromfenaco oftálmico, incluido uno en ojo seco (n=840), lo que respalda un nivel de evidencia L1. Sin embargo, la categoría "enfermedad ocular" es amplia y se solapa con usos ya establecidos, y existen señales de seguridad corneal y cutánea que exigen cautela.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT para confirmar indicaciones aprobadas, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar los resultados de eficacia del ensayo de Fase 3 en ojo seco (NCT01212471), ya que no es una indicación estándar en la etiqueta.
- Definir una subindicación específica (por ejemplo, ojo seco o maculopatías con anti-VEGF) en lugar de la categoría general.
- Establecer un plan de monitoreo de seguridad corneal, especialmente en superficies oculares comprometidas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

