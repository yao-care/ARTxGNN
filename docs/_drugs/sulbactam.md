---
layout: default
title: Sulbactam
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 1
---

# Sulbactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

---

# Sulbactam: De Inhibidor de β-Lactamasa a Artritis Bacteriana

## Resumen en Una Frase

Sulbactam es un inhibidor irreversible de β-lactamasas, utilizado exclusivamente en combinación con ampicilina (Unasyn) para ampliar el espectro antibacteriano frente a gérmenes resistentes productores de esta enzima. El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, con **0 ensayos clínicos registrados** pero **20 publicaciones** que respaldan esta dirección, incluyendo ensayos comparativos randomizados que documentan la eficacia del complejo ampicilina/sulbactam en infecciones óseas y articulares.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin aprobación independiente en Argentina; empleado como adyuvante antibiótico en combinación con ampicilina |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Sulbactam es un inhibidor irreversible de β-lactamasas de amplio espectro (clases B/C/D) que, por sí solo, carece de actividad antibacteriana clínicamente relevante frente a la mayoría de los microorganismos. Su importancia reside en la combinación con ampicilina (Unasyn), donde protege al antibiótico compañero de la hidrólisis enzimática mediada por β-lactamasas, extendiendo el espectro de cobertura hacia cepas que de otro modo serían resistentes. Los agentes etiológicos más frecuentes de la artritis bacteriana —*Staphylococcus aureus*, enterobacterias y anaerobios como el grupo *Bacteroides fragilis*— son productores habituales de estas enzimas, por lo que sulbactam cumple un rol inhibidor crítico que justifica mecánicamente su aplicación en esta indicación.

Adicionalmente, sulbactam posee actividad antibacteriana directa e independiente sobre *Acinetobacter baumannii* mediante la unión a la proteína ligadora de penicilina PBP2. Aunque *A. baumannii* no es el patógeno más frecuente en artritis bacteriana comunitaria, su participación en casos de origen nosocomial lo convierte en un objetivo de relevancia creciente, especialmente en pacientes inmunodeprimidos u hospitalizados.

El modelo TxGNN asignó un puntaje de 99.79%, cuya trayectoria en el grafo de conocimiento se estima como: **sulbactam → inhibición de β-lactamasas → cobertura gram-positiva/gram-negativa → artritis séptica**. Esta predicción es biológicamente coherente y está respaldada por literatura clínica que incluye ensayos comparativos randomizados y estudios prospectivos abiertos en poblaciones pediátricas y adultas con infecciones óseas y articulares tratadas con el complejo ampicilina/sulbactam.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | Ensayo Comparativo Randomizado | Pediatric Infectious Disease Journal | 105 niños hospitalizados con artritis supurativa y osteomielitis; ampicilina/sulbactam (n=84) mostró eficacia comparable a ceftriaxona (n=41), con patógenos como *S. aureus* y *Streptococcus pyogenes* |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | Estudio Comparativo Abierto | Reviews of Infectious Diseases | Sulbactam/ampicilina vs cefotaxima en infecciones óseas, articulares y de tejidos blandos; curación o mejoría clínica en los 13 pacientes del grupo sulbactam/ampicilina a las 2 semanas del fin del tratamiento |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Estudio Clínico Prospectivo Abierto | Reviews of Infectious Diseases | 9 niños con osteomielitis y/o artritis séptica tratados con sulbactam/ampicilina parenteral seguido de sultamicilina oral; títulos bactericidas séricos ≥1:8 alcanzados en todos los pacientes durante la fase parenteral |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Ensayo Clínico | Mikrobiyoloji Bulteni | 84 pacientes con diversas infecciones graves (incluyendo 5 casos de artritis séptica/osteomielitis) tratados con ampicilina/sulbactam parenteral; resultados clínicos y microbiológicos favorables |
| [16269877](https://pubmed.ncbi.nlm.nih.gov/16269877/) | 2005 | Guía Clínica / Revisión | Acta Orthopaedica et Traumatologica Turcica | Protocolo de diagnóstico y tratamiento antibiótico inicial para artritis séptica en niños y adultos; evalúa perfil etiológico y establece pautas de cobertura empírica incluyendo inhibidores de β-lactamasas |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Estudio Observacional Retrospectivo | Clinical Laboratory | Análisis de distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños menores de 4 años; orienta la selección antibiótica empírica según prevalencia local |
| [9263267](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Reporte de Caso | Journal of Rheumatology | Artritis infecciosa por *Pasteurella multocida* post-mordedura felina resuelta exitosamente con ampicilina/sulbactam, aspiración articular y esteroides intrarticulares en paciente con leucemia linfocítica crónica |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión Narrativa | International Journal of Antimicrobial Agents | Uso off-label versus recomendaciones formales de antibióticos para infecciones por bacterias MDR/XDR; contextualiza el papel de sulbactam en el escenario de resistencia antimicrobiana actual |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | Revisión / Farmacología In Vitro | Pharmacotherapy | Comparación de ampicilina/sulbactam vs ticarcilina/clavulánico; actividad in vitro contra productores de β-lactamasas incluyendo *S. aureus*, *H. influenzae* y anaerobios del grupo *Bacteroides fragilis* |
| [36550469](https://pubmed.ncbi.nlm.nih.gov/36550469/) | 2022 | Reporte de Caso | BMC Infectious Diseases | Artritis séptica por *Ureaplasma parvum* con hiperamonemia en paciente séptico; subraya la importancia de considerar patógenos atípicos en artritis bacteriana refractaria al tratamiento inicial |

---

## Información de Mercado en Argentina

Sulbactam **no cuenta con autorizaciones de comercialización propias en Argentina**. No se registran licencias independientes ante ANMAT para este principio activo como monofármaco. Sulbactam se comercializa habitualmente en combinación fija con ampicilina (nombre comercial: Unasyn); las autorizaciones corresponden a la combinación y no al componente aislado, por lo que no figuran en el presente registro.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La literatura disponible incluye ensayos comparativos randomizados y estudios clínicos prospectivos que documentan la eficacia del complejo ampicilina/sulbactam en infecciones óseas y articulares bacterianas, respaldando con evidencia L3 la predicción del modelo TxGNN (99.79%). La racionalidad mecanística es sólida: la inhibición de β-lactamasas amplía la cobertura frente a los principales patógenos de la artritis bacteriana, y la actividad directa anti-*Acinetobacter* agrega valor en contextos nosocomiales.

**Para avanzar se necesita:**
- Obtener datos del mecanismo de acción formal (MOA) desde DrugBank para completar el análisis de relación mecanística
- Revisar la ficha técnica/prospecto de sulbactam (o de Unasyn) para evaluación completa de advertencias, contraindicaciones e interacciones farmacológicas
- Ampliar la búsqueda de ensayos clínicos incluyendo la combinación ampicilina/sulbactam explícitamente en artritis bacteriana (no solo sulbactam aislado)
- Evaluar disponibilidad de formulaciones intravenosas de la combinación ampicilina/sulbactam en el mercado argentino
- Analizar el perfil de resistencia local a β-lactamasas en los patógenos articulares más prevalentes en Argentina para validar la pertinencia del esquema
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

