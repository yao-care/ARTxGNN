---
layout: default
title: Memantine
parent: Solo Predicción del Modelo (L5)
nav_order: 186
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Memantine: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos de ANMAT (el texto de indicación está vací…"
---

# Memantine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Memantina: De Indicación Original No Especificada a Trastorno de Migraña

## Resumen en Una Frase

Memantina es un antagonista del receptor NMDA comercializado en Argentina con 20 autorizaciones vigentes. Los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para el **trastorno de migraña**, con **1 ensayo clínico** de Fase 3 y **19 publicaciones** que respaldan esta dirección. La evidencia es limitada: el ensayo es pequeño (n=33) y compara con valproato, no con placebo.

> Nota: la predicción de mayor puntaje TxGNN es hipertensión pulmonar (99.54%), pero sin evidencia que la respalde. Este informe se centra en la migraña, que tiene la evidencia más sólida entre las cuatro predicciones.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de ANMAT (el texto de indicación está vacío en todas las autorizaciones) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.52% |
| Nivel de Evidencia | L1 (nominal; la certeza efectiva es menor por el tamaño pequeño del ensayo) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la memantina es un antagonista no competitivo del receptor NMDA de glutamato, utilizado en el tratamiento sintomático de la demencia (esta indicación no figura en los datos de ANMAT recibidos y se menciona solo como conocimiento general).

En la migraña, la depresión cortical propagada y la sensibilización central están mediadas por glutamato. Al antagonizar el receptor NMDA, la memantina podría reducir la hiperexcitabilidad neuronal. Las revisiones disponibles (PMID 36869904, 29508147) y los receptores NMDA en el sistema trigeminovascular (PMID 36983158) respaldan esta hipótesis.

Existe cautela: el comentario "Memantine for migraine: Big promise but little evidence" (PMID 34510445) advierte que la base de evidencia es limitada. Además, un ensayo aleatorizado controlado con placebo en migraña sin aura (PMID 26638119) apoya la dirección, aunque se trata de una indicación vecina.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Fase 3 | Completado | 33 | Memantina vs. valproato de sodio en profilaxis de migraña episódica. Directamente en la indicación, pero con muestra pequeña y comparador activo, lo que limita las conclusiones sobre eficacia absoluta |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Metaanálisis de ECA | Clin Neuropharmacol | Eficacia de memantina vs. placebo en migraña; el efecto sigue siendo controvertido |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Revisión sistemática | Headache | Eficacia y seguridad de memantina en profilaxis de migraña episódica |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | ECA | Headache | Memantina vs. placebo, doble ciego, en migraña sin aura (evidencia indirecta para otros subtipos) |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Revisión | Naunyn-Schmiedeberg's Arch Pharmacol | Memantina y ketamina como posibles agentes antimigrañosos |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Metaanálisis en red | Front Pharmacol | Comparación de fármacos orales preventivos de migraña en adultos de 18 a 65 años |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Guía de práctica clínica | Ann Intern Med | Guía VA/DoD 2023 para el tratamiento y la prevención de migraña y cefalea tensional |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Estudio retrospectivo (60 casos) | J Headache Pain | Memantina como tratamiento preventivo en pacientes con migraña frecuente |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Revisión | Ann Pharmacother | Datos de eficacia y seguridad de memantina en la prevención de cefaleas primarias |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Comentario/Editorial | Headache | "Gran promesa pero poca evidencia" |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Revisión | Neurotherapeutics | El glutamato y sus receptores como dianas terapéuticas en migraña |

## Información de Mercado en Argentina

Se listan 5 de las 20 autorizaciones vigentes (todas de monofármaco). Los datos compilados no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55079 | CARRIER XR (Casasco) | 21 mg comprimidos x 30 | No disponible |
| 51633 | NEUROPLUS XR (Baliarda) | 7 mg comprimidos de liberación prolongada x 30 | No disponible |
| 51921 | TONIBRAL XR (Ariston) | 14 mg cápsulas x 30 | No disponible |
| 30251 | FENTINA (Megalabs) | 10 mg comprimidos x 30 | No disponible |
| 45317 | CONEXINE 20 (Beta) | 20 mg comprimidos recubiertos x 30 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar y función renal deteriorada.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las principales):
  - Moderadas: anticolinérgicos como hioscina (hiosciamina), atropina, glicopirronio, clidinio, diciclomina, metescopolamina, propantelina, escopolamina, trospio y mepenzolato.
  - Leves: ranitidina, metformina, cimetidina y citrato de potasio.
  - Nivel no clasificado: glimepirida, doxiciclina, lansoprazol, loperamida, famotidina y ácido acetilsalicílico.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado, un metaanálisis, una revisión sistemática y un ECA en un subtipo cercano, además de un perfil de seguridad bien caracterizado por su uso comercializado. Sin embargo, la evidencia directa es pequeña (n=33, comparador activo) y la literatura es heterogénea, por lo que se avanza con cautela y no con un "Go" pleno.

**Para avanzar se necesita:**
- Ensayos confirmatorios más grandes, controlados con placebo, en migraña
- Obtener del prospecto de ANMAT las indicaciones, advertencias y contraindicaciones oficiales (hoy no disponibles)
- Datos detallados del mecanismo de acción desde DrugBank
- Revisar el riesgo de interacción con anticolinérgicos y el uso en insuficiencia hepática o renal
- Evaluar la compatibilidad de vías y formas farmacéuticas con la profilaxis de migraña

**Otras predicciones (para seguimiento):** hipertensión pulmonar (L5, Hold; las publicaciones recuperadas no respaldan a la memantina, y MN-08 es un compuesto distinto), cardiopatía cifoescoliótica (L5, Hold; sin evidencia ni lógica mecanística) y migraña con aura de tronco encefálico (L4, pregunta de investigación; evidencia extrapolada de la migraña general).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

