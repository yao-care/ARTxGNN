---
layout: default
title: Nepafenac
parent: Evidencia Alta (L1-L2)
nav_order: 202
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Nepafenac: nueva indicación predicha, Enfermedad ocular (eye disease) (nivel de evidencia L1). Indicación original: No disponible en la autorización de ANMAT (el texto de indicación est…"
monitor_inn: "NEPAFENAC"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
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

## Nepafenac: De Uso Oftálmico Postoperatorio a Enfermedad Ocular (Predicción Amplia)
{: .text-alpha }

## Resumen en Una Frase

Nepafenac es un antiinflamatorio no esteroideo (AINE) de uso tópico oftálmico, comercializado en Argentina como NEVANAC en colirio al 0,1 %. El modelo TxGNN predice que podría ser efectivo para **enfermedad ocular** (una categoría muy amplia), con **40 ensayos clínicos** y **20 publicaciones** registrados. Cabe señalar que esta categoría se solapa en gran medida con su uso ya conocido, por lo que no constituye un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de ANMAT (el texto de indicación está vacío); uso conocido: inflamación y dolor oculares tras cirugía de catarata |
| Nueva Indicación Predicha | Enfermedad ocular (eye disease) |
| Puntaje de Predicción TxGNN | 99,85 % |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información compilada, nepafenac es un profármaco que los tejidos oculares convierten, mediante hidrolasas, en amfenac, un inhibidor de COX-1 y COX-2. Al reducirse la síntesis de prostaglandinas, disminuyen la inflamación ocular, el dolor y la ruptura de la barrera hematorretiniana.

Este mecanismo concuerda con su uso comercializado en la inflamación y el dolor posteriores a la cirugía de catarata, y con la evidencia de penetración al segmento posterior del ojo. Por ello, la predicción de "enfermedad ocular" es coherente, pero tan general que coincide en buena medida con el uso oftálmico ya establecido. Las subindicaciones específicas (por ejemplo, edema macular o inflamación posvitrectomía) deberían evaluarse por separado.

Entre las demás predicciones del modelo, "papilitis óptica" (L4, Hold) y "desprendimiento vítreo" (L4, pregunta de investigación) tienen apoyo limitado o indirecto. Las restantes, como hipotricosis, queratosis seborreica o lagoftalmos, carecen de vínculo mecanístico y de evidencia, y parecen artefactos de la predicción basada en grafos.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 40 registrados), priorizando los de mayor fase, tamaño y calificación de relevancia.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Fase 3 | Completado | 2120 | Nepafenac 0,3 % en la prevención y el tratamiento de inflamación y dolor tras cirugía de catarata |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Fase 2 | Completado | 1342 | Nepafenac 0,3 % vs. 0,1 % vs. vehículo en inflamación y dolor poscatarata |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Fase 3 | Completado | 881 | Nepafenac 0,3 % vs. vehículo en pacientes diabéticos tras cirugía de catarata |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Fase 3 | Completado | 819 | Estudio gemelo del anterior: superioridad de nepafenac 0,3 % una vez al día en diabéticos |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Fase 2 | Completado | 263 | NEVANAC 0,1 % vs. vehículo para reducir el edema macular poscatarata en retinopatía diabética |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Fase 3 | Completado | 267 | Nevanac 0,1 % vs. Acular LS en inflamación ocular asociada a cirugía de catarata |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Fase 3 | Completado | 227 | Nepafenac 0,1 % vs. ketorolaco 0,5 % y placebo (estudio europeo) |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Fase 3 | Completado | 260 | Nepafenac 0,1 % vs. placebo en adultos chinos tras cirugía de catarata |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Fase 3 | Completado | 448 | Estudio de bioequivalencia de nepafenac 0,3 % frente a Ilevro en dolor e inflamación poscatarata |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Fase 4 | Completado | 126 | Comparación de la inhibición de PGE2 entre Acuvail, Xibrom y Nevanac en facoemulsificación |

Otros ensayos relevantes incluyen NCT07736690 (cirugía de membrana epirretiniana, Fase 4, n=60) y NCT07162818 (biomarcadores vítreos en desprendimiento de retina, Fase 4, n=61).

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes (de 20 registradas), priorizando revisiones sistemáticas y ECA.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Revisión sistemática con metaanálisis en red | Eye (London) | Compara AINE tópicos, con o sin esteroides, para prevenir el engrosamiento macular y su efecto en la agudeza visual tras facoemulsificación |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | ECA | Korean J Ophthalmol | Nepafenac 0,1 % vs. prednisolona 1 % en el control de la inflamación tras cirugía de catarata microincisional |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | ECA | Ophthalmology Glaucoma | Nepafenac 0,1 % vs. prednisolona 1 % tras iridotomía periférica con láser |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | Estudio comparativo | BMC Ophthalmology | Eficacia analgésica de 7 AINE tópicos en el dolor por panfotocoagulación retiniana |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Revisión | Clin Exp Optom | Nepafenac en cirugía de catarata: alta penetración ocular, reducción de la inflamación, el dolor y el edema macular, con bajo perfil de efectos adversos |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | AINE tópicos para el edema macular quístico diabético |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclínico (farmacocinética) | Exp Eye Res | Distribución de nepafenac y de su metabolito amfenac al segmento posterior del ojo |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclínico (animal) | Diabetes | El nepafenac tópico inhibió la enfermedad microvascular retiniana inducida por diabetes en ratas |
| [12506103](https://pubmed.ncbi.nlm.nih.gov/12506103/) | 2003 | Preclínico (animal) | Invest Ophthalmol Vis Sci | El nepafenac tópico inhibió la neovascularización ocular en tres modelos murinos |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Reporte de caso | J Cataract Refract Surg | Perforación corneal asociada a nepafenac en un paciente con enfermedad de injerto contra huésped tras cirugía de catarata |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38114 | NEVANAC (Novartis) | 0,1 % frasco gotero x 5 ml | Texto de indicación no disponible en el registro |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de PrimeKG, no texto del prospecto): artritis reumatoide, diabetes mellitus, cetoacidosis diabética, trastornos de la coagulación, queratitis, queratoconjuntivitis, síndrome de ojo seco, xeroftalmia y úlcera corneal.
- **Alerta de la literatura**: se ha descrito un caso de perforación corneal ("corneal melt") asociado a nepafenac en un paciente con enfermedad de injerto contra huésped. Otro reporte vincula el uso crónico de AINE y esteroides tópicos con complicaciones oculares en un paciente con uveítis.
- **Interacciones farmacológicas**: no se encontraron registros.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados, con cientos de participantes, que respaldan el uso de nepafenac en inflamación y dolor oculares. Sin embargo, "enfermedad ocular" es una categoría tan amplia que no constituye un reposicionamiento genuino, y no se dispone de los datos de seguridad del prospecto local.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), un vacío de datos de severidad bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Definir subindicaciones concretas (por ejemplo, edema macular diabético, inflamación posvitrectomía) y evaluarlas individualmente.
- Revisar con especial cuidado las contraindicaciones del grafo de conocimiento (queratitis, úlcera corneal, ojo seco, diabetes), dado el riesgo descrito de afectación corneal.
- Confirmar el texto de la indicación aprobada en la licencia 38114.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

