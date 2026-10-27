---
layout: default
title: Levetiracetam
parent: Evidencia Moderada (L3-L4)
nav_order: 175
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Levetiracetam: nueva indicación predicha, Epilepsia visual (nivel de evidencia L3). Indicación original: Epilepsia parcial"
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Levetiracetam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

## Levetiracetam: De Epilepsia Parcial a Epilepsia Visual
{: .text-alpha }

## Resumen en Una Frase

Levetiracetam es un antiepiléptico de segunda generación, originalmente utilizado para el tratamiento de la epilepsia parcial.
El modelo TxGNN predice que podría ser efectivo para **epilepsia visual**, aunque para esta indicación no hay ensayos clínicos registrados y la literatura recuperada (20 publicaciones) solo respalda un efecto antiepiléptico general, sin estudios específicos de epilepsia visual o fotosensible.

Cabe destacar que, entre las 10 indicaciones predichas, **estado epiléptico** es la que cuenta con la evidencia más sólida (varios ensayos de Fase 3), por lo que se incluye una sección comparativa al final.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia parcial |
| Nueva Indicación Predicha | Epilepsia visual |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold (pregunta de investigación; no hay evidencia específica para esta indicación) |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, levetiracetam se une a la proteína de la vesícula sináptica SV2A y modula la liberación de neurotransmisores, y es un fármaco antiepiléptico de amplio espectro con eficacia comprobada en la epilepsia parcial.

Mecanísticamente, es plausible que actúe sobre convulsiones desencadenadas por estímulos visuales o fotosensibles, ya que son crisis reflejas con hiperexcitabilidad neuronal. Sin embargo, ninguna de las publicaciones recuperadas trata específicamente de epilepsia visual o fotosensible: abordan convulsiones neonatales, profilaxis de crisis, estado epiléptico y epilepsia felina.

El puntaje TxGNN tan elevado probablemente refleja la cercanía del fármaco a los nodos de epilepsia en el grafo de conocimiento, y no evidencia específica de la enfermedad. Por ello, esta predicción debe considerarse una pregunta de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para epilepsia visual.

## Evidencia de Literatura

Se seleccionaron las publicaciones más relevantes (priorizando ECA y revisiones sistemáticas). Ninguna es específica de epilepsia visual.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | ECA | Pediatrics | Levetiracetam frente a fenobarbital en convulsiones neonatales |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | ECA Fase 3 | Lancet Neurol | Levetiracetam profiláctico para prevenir crisis agudas en hemorragia intracerebral (PEACH) |
| [28528211](https://pubmed.ncbi.nlm.nih.gov/28528211/) | 2017 | ECA | Seizure | Levetiracetam IV frente a fenitoína en estado epiléptico y crisis en racimo |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | ECA | Seizure | Fenitoína y levetiracetam en crisis sintomáticas agudas en niños con síndrome de encefalitis aguda |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Metaanálisis | Neurocrit Care | Profilaxis de crisis con levetiracetam en cuidados neurocríticos |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Metaanálisis en red | Neurology | Fármacos antiepilépticos en crisis postictus |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Revisión | CNS Drugs | Panorama de levetiracetam en epilepsia |
| [12915343](https://pubmed.ncbi.nlm.nih.gov/12915343/) | 2003 | Revisión | Epileptic Disord | Perfil de seguridad favorable de levetiracetam |
| [22133815](https://pubmed.ncbi.nlm.nih.gov/22133815/) | 2012 | Cohorte | J Clin Neurosci | Levetiracetam frente a fenitoína para crisis posoperatorias tras craneotomía |
| [35848684](https://pubmed.ncbi.nlm.nih.gov/35848684/) | 2022 | Reporte de caso | J Postgrad Med | Hiperplasia gingival inducida por levetiracetam |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59203 | KEPPRA (GlaxoSmithKline) | 500 mg comp. x 30 | No disponible en los datos |
| 43270 | CALLEXE (Casasco) | 500 mg comp. rec. x 50 | No disponible en los datos |
| 48497 | LEVAXON (Adium) | 500 mg comp. x 20 | No disponible en los datos |
| 48527 | LEVECOM XR 750 (Baliarda) | 750 mg comp. lib. prol. x 30 | No disponible en los datos |
| 54825 | LEVETIRACETAM RICHET (Richet) | 100 mg/ml susp. x 300 ml | No disponible en los datos |

Hay 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), con presentaciones de comprimidos, liberación prolongada, suspensión y solución oral.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según prospecto)**: ansiedad, trastornos neuróticos, trastorno distímico, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trastornos psicóticos y esquizoafectivos, trastorno mental, neutropenia, agranulocitosis, leucopenia, pancitopenia y trastorno de despersonalización.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado incluyen morfina (también liposomal), dronabinol, nabilona, metoclopramida, opio y sibutramina. Otras (calcitriol, pantoprazol, glimepirida, metformina, omeprazol, doxiciclina, vancomicina, entre otras) tienen nivel desconocido.
- **Reportes de la literatura**: hiponatremia, hiperplasia gingival, irritabilidad y agravamiento de crisis en algunos pacientes. Un estudio preclínico sugiere vigilar la función auditiva.

Consultar el prospecto para información de seguridad completa.

## Comparación con Otras Indicaciones Predichas

| Indicación | Puntaje TxGNN | Nivel | Recomendación | Evidencia clave |
|------|------|------|------|------|
| **Estado epiléptico** | 99.91% | L1 | Proceed with Guardrails | Ensayos de Fase 3 completados: [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) (ESETT, n=478) y [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) (n=203); ECA en [PMID 31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) |
| Epilepsia sobresalto | 99.96% | L3 | Proceed with Guardrails | Series pequeñas y casos ([PMID 18486495](https://pubmed.ncbi.nlm.nih.gov/18486495/), [17401745](https://pubmed.ncbi.nlm.nih.gov/17401745/)) |
| Crisis audiogénicas | 99.96% | L4 | Research Question | Modelos animales y ECA veterinario en gatos |
| Epilepsia de lectura | 99.94% | L4 | Research Question | Solo apoyo indirecto (seletracetam, fármaco relacionado) |
| Crisis al comer, miccionales, orgásmicas, de pensamiento y deficiencia de beta-cetotiolasa | 99.90–99.96% | L5 | Hold | Sin evidencia específica |

En estado epiléptico, ESETT no mostró superioridad clara entre levetiracetam, fosfenitoína y valproato, por lo que respalda a levetiracetam como una de varias opciones de segunda línea equivalentes, no como agente preferido.

## Conclusión y Próximos Pasos

**Decisión: Hold** (para epilepsia visual, la indicación principal)

**Justificación:**
No hay ensayos clínicos ni literatura específica para epilepsia visual o fotosensible; el puntaje TxGNN refleja proximidad en el grafo y no evidencia real. El nivel de evidencia es L3 y la etapa es de pregunta de investigación. En cambio, estado epiléptico (L1) y epilepsia por sobresalto (L3) tienen un respaldo mucho más sólido y podrían priorizarse.

**Para avanzar se necesita:**
- Búsqueda dirigida de estudios sobre levetiracetam en epilepsia fotosensible o inducida por estímulos visuales.
- Datos del mecanismo de acción (consulta a DrugBank).
- Prospecto de ANMAT con advertencias, contraindicaciones e indicaciones aprobadas (actualmente ausentes).
- Considerar priorizar la evaluación de estado epiléptico como posible extensión de indicación, con atención a dosis, grupo etario y función renal.
- Aclarar la distinción fenotípica con hiperekplexia en el caso de epilepsia por sobresalto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

