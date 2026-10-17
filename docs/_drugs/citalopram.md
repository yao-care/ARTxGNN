---
layout: default
title: Citalopram
parent: Solo Predicción del Modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Citalopram: nueva indicación predicha, Trastorno obsesivo-compulsivo (nivel de evidencia L5). Indicación original: Trastorno de ansiedad, trastorno neurótico, trastorno distímico…"
monitor_inn: "CITALOPRAM"
predicted_indications: ["paranoid personality disorder", "schizoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)"]
---

# Citalopram
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Citalopram: De Trastorno de Ansiedad y Depresión a Trastorno Obsesivo-Compulsivo

## Resumen en Una Frase

Citalopram es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado originalmente para tratar trastornos depresivos y de ansiedad.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Obsesivo-Compulsivo (TOC)**,
con **4 ensayos clínicos** (ninguno específico de citalopram) y **15 publicaciones** que actualmente respaldan esta dirección, varias de ellas con estudios abiertos o de cohorte con citalopram en TOC.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de ansiedad, trastorno neurótico, trastorno distímico, depresión unipolar, depresión endógena y trastorno depresivo mayor (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Trastorno obsesivo-compulsivo |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 (evidencia asignada en los datos compilados; los ensayos clínicos disponibles son indirectos, de clase ISRS, y la literatura específica de citalopram es mayormente abierta o de cohorte) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, citalopram pertenece a la clase de los ISRS, su eficacia en trastornos depresivos y de ansiedad está comprobada, y mecanísticamente podría ser aplicable al TOC.

La disfunción serotoninérgica es central en la fisiopatología del TOC, y los ISRS son tratamiento farmacológico de primera línea para esta condición. El puntaje muy alto de TxGNN (0.997) es coherente con este solapamiento de mecanismo a nivel de clase, así como con la frecuente coexistencia de TOC con trastornos de ansiedad y depresivos.

Es importante tener en cuenta que citalopram no es un fármaco aprobado para TOC en la mayoría de las jurisdicciones, por lo que su uso sería fuera de indicación (off-label), sustentado por evidencia de clase y por estudios pequeños.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Fase 4 | Completado | 78 | Eficacia de la terapia de exposición y prevención de respuesta (ERP) y de ISRS, solos o combinados, en TOC en población china; apoyo indirecto a nivel de clase |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Fase 3 | Completado | 124 | Terapia cognitivo-conductual como complemento en niños con TOC con respuesta parcial a inhibidores de recaptación de serotonina; no evalúa citalopram directamente |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Fase 4 | Completado | 158 | TCC grupal vs. fluoxetina en TOC; el ISRS comparador no es citalopram |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | Completado | 43 | Estudio piloto de microbiota intestinal en TOC antes y después de 12 semanas de ISRS; no aporta evidencia de eficacia |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Ensayo aleatorizado abierto (cohorte) | European Psychiatry | Citalopram solo vs. citalopram más clomipramina en TOC resistente al tratamiento (16 pacientes, 90 días) |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Cohorte | CNS Drugs | Relación preliminar entre concentraciones de citalopram y respuesta clínica en TOC |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Cohorte (abierto) | Psychiatry and Clinical Neurosciences | Citalopram en 15 niños y adolescentes con TOC durante 8 semanas; eficacia y tolerabilidad |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Cohorte (abierto) | J Child Adolesc Psychopharmacol | 23 niños y adolescentes con TOC tratados con citalopram 10-40 mg; mejoría significativa en Y-BOCS (30 a 21) |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Estudio simple ciego | J Clin Psychopharmacol | Comparación de la eficacia antiobsesiva de fluvoxamina, paroxetina y citalopram |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | Estudio piloto abierto | Acta Psychiatr Scand | Estudio piloto de 24 semanas de citalopram en TOC |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Revisión | Int Clin Psychopharmacol | Revisión del uso de citalopram más allá de la depresión, en TOC |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Revisión | BMJ Clinical Evidence | Revisión general sobre TOC: prevalencia, curso y tratamientos |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Revisión | Current Medicinal Chemistry | Fármacos pasados, presentes y futuros para el TOC; papel central de los ISRS |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Revisión | World J Biol Psychiatry | Serotonina y otros sistemas implicados en el TOC |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51103 | CITTA (Eurofarma) | 20 mg, comprimidos x 28 | No disponible en los datos compilados |
| 30387 | PSICONOR (Teva Argentina) | 20 mg, comprimidos x 30 | No disponible en los datos compilados |
| 24696 | ZENTIUS (Roemmers) | Comprimidos recubiertos x 30 | No disponible en los datos compilados |
| 51102 | CITTA (Eurofarma) | 20 mg, comprimidos x 14 | No disponible en los datos compilados |
| 33725 | HUMORAP 40 | 40 mg, comprimidos x 28 | No disponible en los datos compilados |

Hay 7 autorizaciones vigentes en total, todas de monofármaco; se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento, no texto del prospecto)**: síndrome de QT largo (incluido el familiar), torsades de pointes, epilepsia, trastorno bipolar y trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de potasio, trastornos de la coagulación, enfermedad cardíaca y cardiovascular, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH (incluida la forma nefrogénica) y síndrome serotoninérgico.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las de nivel **mayor** figuran bupropión, omeprazol, lorcaserina, cimetidina, cisaprida, claritromicina, dexfenfluramina, dietilpropión y dolasetrón. Entre las de nivel moderado: famotidina, loperamida, morfina, ácido acetilsalicílico (por riesgo de sangrado), bisacodilo, clorpropamida, acetohexamida, aceite de ricino y dronabinol. De nivel menor: aprepitant y clotrimazol.

Para advertencias principales y contraindicaciones del prospecto, consultar el prospecto aprobado por ANMAT, ya que no se dispone de esa información en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La plausibilidad mecanística a nivel de clase ISRS es sólida y existen varios estudios abiertos y de cohorte con citalopram en TOC (adultos y población pediátrica), además de un puntaje TxGNN muy alto. Sin embargo, los ensayos clínicos registrados no evalúan citalopram directamente y el uso sería off-label.

**Para avanzar se necesita:**
- Revisar el prospecto de ANMAT (advertencias y contraindicaciones) y los textos de indicación aprobados.
- Confirmar los datos de mecanismo de acción desde DrugBank.
- Ensayos controlados aleatorizados con citalopram específicamente en TOC.
- Evaluación del riesgo de prolongación del QT y de interacciones farmacológicas de nivel mayor antes de cualquier uso.
- Plan de monitoreo en poblaciones específicas (pediátrica, con enfermedad cardíaca o hepática, y con trastorno bipolar).

**Otras predicciones (decisión: Hold):** trastorno de personalidad paranoide (evidencia L4, solo literatura indirecta sobre comorbilidad), y trastornos de personalidad esquizoide, esquizotípico e histriónico (L5, solo predicción del modelo sin ensayos ni literatura).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

