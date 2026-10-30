---
layout: default
title: Fludrocortisone
parent: Solo Predicción del Modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Fludrocortisone: nueva indicación predicha, Linfoma cutáneo primario de células T (nivel de evidencia L5). Indicación original: No disponible en la licencia de ANMAT (texto de indicación vacío)"
monitor_inn: "fludrocortisone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "cystic teratoma", "spinal cord dermoid cyst", "dermoid cyst of ovary", "disease of orbital part of eye adnexa", "eye disease", "disease of orbital region", "exostosis"]
---

# Fludrocortisone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Fludrocortisona: De Indicación Original No Registrada a Linfoma cutáneo primario de células T (Predicción del Modelo)
{: .text-alpha }

> Nota: la primera indicación predicha por el modelo (rank 1) es el linfoma cutáneo primario de células T, pero no cuenta con ninguna evidencia. Por ello, esta evaluación se centra en la predicción con mayor respaldo documental (**enfermedad ocular**, rank 6) y menciona brevemente las demás.

## Resumen en Una Frase

La fludrocortisona es un mineralocorticoide con cierta actividad glucocorticoide, comercializado en Argentina como LONIKAN; la licencia de ANMAT no incluye el texto de la indicación aprobada.
El modelo TxGNN predice como primera posición el **linfoma cutáneo primario de células T** (sin evidencia alguna), y la predicción con mayor respaldo documental es **enfermedad ocular**, con **0 ensayos clínicos** y **20 publicaciones** (indirectas en su mayoría).
La evidencia es débil: solo hay un estudio preclínico y un estudio de fase 1B de seguridad en atrofia geográfica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la licencia de ANMAT (texto de indicación vacío) |
| Nueva Indicación Predicha | Linfoma cutáneo primario de células T (rank 1); enfermedad ocular (rank 6, con más literatura) |
| Puntaje de Prediccion TxGNN | 0.9958 (linfoma cutáneo primario de células T); 0.9914 (enfermedad ocular) |
| Nivel de Evidencia | L5 (linfoma cutáneo de células T); L4 (enfermedad ocular) |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Numero de Autorizaciones | 1 (vigentes: 1) |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fludrocortisona es un mineralocorticoide sintético con cierta actividad glucocorticoide, y su uso establecido es en la hipotensión ortostática y la insuficiencia suprarrenal (como se desprende de la literatura recuperada). Mecanísticamente, podría ser aplicable a algunas afecciones donde interviene la señalización de receptores de mineralocorticoides y glucocorticoides.

**Linfoma cutáneo primario de células T (rank 1):** no hay ensayos ni literatura. Los glucocorticoides tienen un papel conocido en neoplasias linfoides, pero no existe fundamento documentado para la fludrocortisona en esta enfermedad; el vínculo mecanístico es especulativo y el puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Enfermedad ocular (rank 6):** un estudio preclínico (PMID 34509498, 2021) describe propiedades antiinflamatorias y neuroprotectoras de la fludrocortisona en degeneración retiniana, mediante la modulación de citocinas de las células de Müller. Además, un estudio de fase 1B evaluó la seguridad de la inyección intravítrea en atrofia geográfica. También hay literatura sobre su uso en la hipotensión sistémica de pacientes con glaucoma. El vínculo es plausible pero indirecto.

**Otras predicciones** (quiste teratoma, quiste dermoide espinal, quiste dermoide de ovario, enfermedades de la región orbitaria y de los anexos oculares, exostosis): no hay ensayos ni literatura y no se identifica una base biológica plausible; probablemente reflejan artefactos de proximidad en la red.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la predicción de enfermedad ocular se recuperaron 20 publicaciones; se muestran las 10 más relevantes (la clasificación de varias está pendiente):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclínico/mecanístico | Experimental Eye Research | La fludrocortisona muestra efectos antiinflamatorios y neuroprotectores en degeneración retiniana, modulando citocinas de células de Müller |
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Estudio clínico fase 1B | BMJ Open Ophthalmology | Seguridad y tolerabilidad de acetato de fludrocortisona intravítreo (1 y 2 mg) en atrofia geográfica por DMAE |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Estudio clínico | International Ophthalmology | Efectos hemodinámicos sistémicos de la fludrocortisona en pacientes con glaucoma primario de ángulo abierto e hipotensión |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Revisión | Survey of Ophthalmology | Tratamientos del glaucoma más allá de la presión intraocular; la fludrocortisona se usa para evitar caídas de presión arterial |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Revisión | Klinische Monatsblätter für Augenheilkunde | Valor de terapias no hipotensoras oculares en glaucoma (magnesio, ginkgo, sal, fludrocortisona) |
| [31994621](https://pubmed.ncbi.nlm.nih.gov/31994621/) | 2019 | Revisión/caso | Rev Assoc Med Bras | Síndrome poliglandular autoinmune tipo 2 (enfermedad de Addison con enfermedad tiroidea autoinmune y/o diabetes tipo 1) |
| [15934882](https://pubmed.ncbi.nlm.nih.gov/15934882/) | 2005 | Revisión | Expert Opin Pharmacother | Tratamientos farmacológicos de la disautonomía familiar |
| [38831360](https://pubmed.ncbi.nlm.nih.gov/38831360/) | 2024 | Cohorte/observacional | Advances in Rheumatology | Hipocitraturia como biomarcador de acidosis tubular renal en enfermedad de Sjögren |
| [25354755](https://pubmed.ncbi.nlm.nih.gov/25354755/) | 2015 | Estudio de prevalencia | Rheumatology (Oxford) | Prevalencia de acidosis tubular renal distal en síndrome de Sjögren; prueba de acidificación con furosemida y fludrocortisona |
| [9775111](https://pubmed.ncbi.nlm.nih.gov/9775111/) | 1998 | Revisión | La Revue de Médecine Interne | Insuficiencia suprarrenal periférica en pacientes con SIDA |

## Informacion de Mercado en Argentina

| Numero de Autorizacion | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 22808 | LONIKAN (Elea) | Comprimidos x 50 | No especificada en el registro |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 446 interacciones en total. Entre las mostradas, la de nivel **Mayor** es con **bupropión**. Las de nivel **Moderado** incluyen antidiabéticos (acarbosa, albiglutida, alogliptina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, linagliptina), anfotericina B (y su complejo lipídico), aprepitant, ácido acetilsalicílico, bisacodilo, ácido picosulfúrico, claritromicina, oxandrolona y oximetolona.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
- La predicción de primera posición (linfoma cutáneo primario de células T) carece de ensayos y literatura, y su vínculo mecanístico es especulativo. La de enfermedad ocular (L4) solo cuenta con un estudio preclínico y un estudio de seguridad de fase 1B, por lo que se la considera una pregunta de investigación y no una candidata lista para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), una brecha de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción.
- Confirmar la indicación original aprobada de LONIKAN.
- Evaluar la compatibilidad de vías de administración (la vía intravítrea no corresponde a la forma oral comercializada).
- Para enfermedad ocular, ensayos de eficacia (fase 2) en atrofia geográfica u otras patologías retinianas específicas, y revisión de la relevancia de la literatura recuperada, ya que gran parte es indirecta.
- Para las demás predicciones (linfoma cutáneo, quistes, exostosis), no se recomienda inversión adicional salvo que surja evidencia biológica nueva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

