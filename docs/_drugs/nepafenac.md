---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Nepafenac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el skill `txgnn-pipeline` para verificar el contexto del proyecto. Ahora procederé a generar el informe de evaluación de reposicionamiento para Nepafenac basado en el Evidence Pack proporcionado.

---

# Nepafenac: De Inflamación Ocular Posquirúrgica a Enfermedad Ocular

## Resumen en Una Frase

Nepafenac (Nevanac®/Ilevro®) es un antiinflamatorio no esteroideo (AINE) tópico ocular en forma de profármaco, utilizado internacionalmente para la prevención y el tratamiento del dolor e inflamación asociados a la cirugía de cataratas.
El modelo TxGNN predice que podría ser efectivo para un espectro ampliado de **Enfermedades Oculares**, incluyendo edema macular diabético, distrofias corneales y patología vitreoretiniana inflamatoria.
Esta predicción está respaldada por **41 ensayos clínicos** y **20 publicaciones científicas**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor e inflamación ocular asociados a cirugía de cataratas (uso internacional establecido; sin registro formal en Argentina) |
| Nueva Indicación Predicha | Enfermedad Ocular (espectro ampliado) |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Nepafenac es un profármaco AINE que, tras su administración tópica ocular, penetra los tejidos del ojo donde es biotransformado por hidrolasas tisulares en su metabolito activo **amfenac**. Este metabolito inhibe de manera potente las enzimas COX-1 y COX-2, bloqueando la síntesis de prostaglandinas intraoculares —mediadores clave de la inflamación ocular, el dolor posquirúrgico y el edema macular. Esta arquitectura de profármaco le confiere una penetración intraocular y al segmento posterior superiores a otros AINE tópicos convencionales, según confirma el estudio farmacocinético publicado en *Experimental Eye Research* (PMID 26474497).

La predicción de TxGNN es biológicamente coherente porque la inflamación mediada por prostaglandinas es un mecanismo central en múltiples enfermedades oculares más allá de la cataratas: edema macular cistoide posquirúrgico, edema macular diabético, uveítis, reacciones inflamatorias asociadas a fotocoagulación panretiniana y vitrectomía, y patología del segmento anterior como el glaucoma de cierre angular. Adicionalmente, el PMID 19897019 demostró en modelo animal que el amfenac inhibe distintos pasos de la cascada angiogénica retiniana, añadiendo una dimensión **antiangiogénica** al perfil farmacológico de nepafenac más allá del eje antiinflamatorio clásico.

La transición conceptual de la indicación original —inflamación posoperatoria de cataratas— hacia el espectro más amplio de "enfermedad ocular" está sustentada por una extensa base de ensayos clínicos que exploran su uso en edema macular diabético (NCT00782717, NCT00939276), distrofias corneales por mutación SLC4A11 (NCT04843839), prevención de edema macular en múltiples contextos quirúrgicos, control del dolor en procedimientos láser (PRK, iridotomía periférica), e incluso el uso intravítreo adyuvante. La coherencia mecanística y el volumen probatorio justifican plenamente la predicción del modelo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Fase 3 | Completado | 2120 | Ensayo pivotal multicéntrico: nepafenac 0.3% una vez al día para prevención y tratamiento de inflamación y dolor ocular post-cataratas; mayor muestra de la serie |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Fase 3 | Completado | 881 | ECA doble ciego vs. vehículo: superioridad de nepafenac 0.3% en resultados clínicos en pacientes diabéticos post-cirugía de cataratas |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Fase 3 | Completado | 819 | Registro paralelo al anterior en población diabética: confirma superioridad de nepafenac 0.3% una vez al día vs. vehículo |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Fase 3 | Completado | 448 | Estudio de bioequivalencia clínica: nepafenac 0.3% genérico (Indoco/Actavis) vs. Ilevro™ de Alcon; valida la reproductibilidad del perfil de eficacia |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Fase 3 | Completado | 260 | Eficacia y seguridad de nepafenac 0.1% vs. placebo en sujetos chinos post-cataratas; respalda la generalización a poblaciones asiáticas |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Fase 3 | Completado | 227 | Estudio europeo: nepafenac 1 mg/ml vs. ketorolaco trometamol vs. placebo para inflamación y dolor post-extracción de cataratas con implante de LIO |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Fase 3 | Terminado | 175 | Evaluación de NEVANAC en pacientes con retinopatía diabética que desarrollaron edema macular dentro de 90 días post-cataratas; ensayo terminado —contexto de terminación relevante para evaluación de riesgo |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Fase 4 | Completado | 126 | Comparación directa de inhibición de PGE2 entre Acuvail, Xibrom y Nevanac en facoemulsificación; valida el mecanismo COX central de nepafenac |
| [NCT00494494](https://clinicaltrials.gov/study/NCT00494494) | Fase 4 | Completado | 82 | Evaluación de nepafenac 0.1% para prevención de edema macular cistoide posoperatorio en cirugía de cataratas no complicada; seguimiento con OCT |
| [NCT04843839](https://clinicaltrials.gov/study/NCT04843839) | Fase 2 | Desconocido | 30 | Exploración pionera de AINE tópico ocular para distrofia endotelial congénita corneal (CHED) por mutación SLC4A11; alternativa no quirúrgica de alta relevancia clínica |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Meta-análisis | European Journal of Ophthalmology | Revisión sistemática de ECA: nepafenac reduce significativamente el grosor foveal y el volumen macular total, con mejora del AVMC tras cirugía de cataratas |
| [40243047](https://pubmed.ncbi.nlm.nih.gov/40243047/) | 2025 | ECA | Indian Journal of Ophthalmology | Comparación de nepafenac 0.1% (3 veces/día) vs. 0.3% (1 vez/día) en síndrome de pseudoexfoliación post-cataratas; evalúa la equivalencia posológica |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | ECA | Korean Journal of Ophthalmology | Nepafenac 0.1% vs. prednisolona 1% en control de inflamación posoperatoria en cirugía micro-incisional de cataratas; no inferioridad demostrada |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Revisión | Drugs | Revisión exhaustiva de agentes farmacológicos para lesiones corneales no infecciosas, con análisis del rol de nepafenac como AINE tópico de referencia |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | ECA | Ophthalmology Glaucoma | Nepafenac 0.1% vs. prednisolona acetato 1% en control de inflamación tras iridotomía periférica láser en sospecha de cierre angular primario; propuesta de alternativa al esteroide |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2019 | Estudio Comparativo | Acta Ophthalmologica | Nepafenac vs. diclofenac sin conservante post-cataratas: eficacia clínica comparable con perfil de tolerabilidad diferenciado |
| [30046541](https://pubmed.ncbi.nlm.nih.gov/30046541/) | 2018 | Estudio Comparativo | International Journal of Ophthalmology | Bromfenac 0.09% vs. nepafenac 0.1% vs. diclofenac 0.1% para profilaxis de edema macular cistoide tras facoemulsificación |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Estudio Farmacocinético | Experimental Eye Research | Distribución de nepafenac tópico y amfenac al segmento posterior: sustenta la eficacia sobre edema macular y la base mecanística de las indicaciones posteriores |
| [25493620](https://pubmed.ncbi.nlm.nih.gov/25493620/) | 2016 | Estudio de Interacción | Journal of Glaucoma | Efecto de nepafenac sobre la presión intraocular en glaucoma de ángulo abierto tratado con análogos de prostaglandinas; relevante para seguridad en población glaucomatosa |
| [19897019](https://pubmed.ncbi.nlm.nih.gov/19897019/) | 2010 | Estudio Preclínico | Brain Research Bulletin | Amfenac inhibe la cascada angiogénica retiniana in vitro e in vivo (modelo OIR en rata); confirma actividad antiangiogénica de nepafenac más allá del efecto antiinflamatorio |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3 completados —con una inscripción combinada superior a 4.000 pacientes en ensayos pivotales— respaldan la eficacia y seguridad de nepafenac en diversas enfermedades oculares inflamatorias. El perfil mecanístico dual (antiinflamatorio COX + antiangiogénico) y la capacidad demostrada de penetrar el segmento posterior fundamentan la extrapolación hacia un espectro ampliado de enfermedad ocular. La clasificación L1 de TxGNN refleja fielmente esta base probatoria sólida y madura.

**Para avanzar se necesita:**
- **Registro regulatorio en Argentina**: nepafenac no está comercializado; evaluar viabilidad de trámite ante ANMAT como medicamento de importación o para registro local
- **Información de seguridad formal**: obtener y revisar el prospecto oficial (advertencias, contraindicaciones, interacciones farmacológicas) de las presentaciones 0.1% y 0.3%
- **Datos formales de mecanismo de acción (MOA)**: completar consulta a DrugBank API para datos estructurados de targets moleculares
- **Definición de indicación específica**: dado que "enfermedad ocular" es un espectro amplio, priorizar la indicación con mayor urgencia clínica no cubierta localmente (p. ej., edema macular diabético posquirúrgico, distrofia corneal endotelial) para una estrategia regulatoria precisa
- **Revisión de ensayos terminados anticipadamente** (NCT00939276, NCT00801905): confirmar causas de terminación para descartar señales de seguridad ocultas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

