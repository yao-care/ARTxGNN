---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

A seguir está el informe generado a partir del Evidence Pack. La indicación destacada es **Artritis Idiopática Juvenil (JIA)** — única candidata con nivel de evidencia L1 y recomendación "Proceed with Guardrails" entre las 10 predicciones evaluadas. Las restantes 9 indicaciones corresponden a síndromes genético-estructurales con evidencia L5/Hold, identificados como falsos positivos topológicos del grafo de conocimiento.

---

# Piroxicam: De Artritis Reumatoide del Adulto a Artritis Idiopática Juvenil

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) no selectivo, empleado clásicamente en el tratamiento de la artritis reumatoide del adulto, osteoartritis y otros trastornos inflamatorios musculoesqueléticos.
El modelo TxGNN predice que podría ser efectivo para la **Artritis Idiopática Juvenil (JIA)**,
con **0 ensayos clínicos registrados** y **13 publicaciones** que actualmente respaldan esta dirección — incluyendo ensayos clínicos directos de piroxicam en artritis crónica juvenil y meta-análisis de red recientes que confirman su posicionamiento de primera línea en la clase AINE.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Artritis reumatoide, osteoartritis, trastornos musculoesqueléticos inflamatorios (sin registro ANMAT en base de datos consultada) |
| Nueva Indicación Predicha | Artritis Idiopática Juvenil (JIA) |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Aunque los datos detallados de mecanismo de acción no están disponibles en la base de datos consultada, el mecanismo de piroxicam es farmacológicamente bien establecido: inhibe de forma no selectiva las isoenzimas COX-1 y COX-2, bloqueando la conversión del ácido araquidónico en prostaglandinas —principalmente PGE2 y PGI2—, los principales mediadores del dolor, la inflamación y la fiebre articular. Su semivida plasmática de aproximadamente 50 horas permite la administración una vez al día, lo que representa una ventaja cinética relevante.

La Artritis Idiopática Juvenil (JIA) es la enfermedad reumática crónica más frecuente en la infancia. Su fisiopatología central es una sinovitis crónica mediada por linfocitos T y macrófagos, en la que la sobreexpresión de COX-2 en la membrana sinovial genera cantidades elevadas de PGE2 y PGI2, amplificando la tumefacción articular, la rigidez matutina y las manifestaciones sistémicas febriles. Piroxicam actúa directamente sobre este eje COX→PGE2, el mismo mecanismo que opera en la artritis reumatoide del adulto, lo que fundamenta mecánicamente la extrapolación a la población pediátrica.

Esta predicción cuenta con respaldo clínico directo: el PMID 3510686 es un ensayo multicéntrico doble ciego cruzado de nivel Phase 3 que comparó piroxicam con naproxeno en 47 niños con JCA seronegativa sin diferencias significativas entre ambos —lo que implica no inferioridad de piroxicam—; el PMID 2957205 es un ensayo clínico aleatorizado con 26 pacientes pediátricos con JRA en el que piroxicam redujo significativamente el número de articulaciones dolorosas e inflamadas. El meta-análisis en red de 2024 (PMID 38680254) confirma la clase AINE como tratamiento de primera línea en JIA dentro de un marco comparativo sistemático de 9 agentes. Adicionalmente, el estudio farmacocinético pediátrico (PMID 1782984) caracterizó el perfil de piroxicam específicamente en niños con artritis, documentando una semivida media de 32.6 h en este grupo etario.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en ClinicalTrials.gov ni en ICTRP para la combinación piroxicam + artritis idiopática juvenil.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | ECA Multicéntrico | Br J Rheumatology | Ensayo doble ciego cruzado, 47 niños con JCA seronegativa (5–16 años), 8 semanas; piroxicam vs. naproxeno sin diferencia significativa → no inferioridad de piroxicam |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Ensayo Clínico | Eur J Rheumatol Inflamm | Piroxicam vs. naproxeno en 26 pacientes pediátricos con JRA (3–25 años); reducción significativa de articulaciones dolorosas e inflamadas (p < umbral) |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Revisión Sistemática / NMA | World J Clin Cases | Meta-análisis en red de múltiples AINEs en JIA; confirma el rol de primera línea de los AINEs y ofrece comparaciones indirectas de eficacia relativa |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Meta-análisis Comparativo | Indian Pediatrics | Análisis comparativo de eficacia y seguridad de 9 AINEs en JIA; piroxicam incluido en el marco comparativo |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Revisión de Seguridad | Clin Rheumatology | Toxicidad a largo plazo de AINEs y DMARDs en 117 niños con enfermedades reumáticas, seguimiento medio 8.6 años; perfil de seguridad documentado para piroxicam |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Estudio Farmacocinético | Eur J Clin Pharmacol | Farmacocinética en estado estable de piroxicam en 10 niños con artritis reumatoide (7–16 años, 20–63 kg); semivida media 32.6 h, Cmax media 6.6 mg/L |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Revisión | Crit Rev Ther Drug Carrier Syst | Microencapsulación de AINEs (incluyendo piroxicam) para el tratamiento de OA, AR, JIA y espondilitis anquilosante |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Estudio de Cohorte | Int Ophthalmology | Iridociclitis crónica en JCA ANA-positiva; 56% de frecuencia; uso de AINEs como parte del manejo, con seguimiento favorable sin complicaciones oculares |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Revisión Clínica | Kinderarztliche Praxis | Aspectos actuales del tratamiento farmacológico de la JCA; piroxicam y sulfasalazina presentados como agentes más recientes disponibles |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Revisión | Drugs | Nabumetona en OA y AR; piroxicam citado como comparador estándar de clase NSAID en el contexto del perfil de inhibición COX |

---

## Información de Mercado en Argentina

Piroxicam no cuenta con autorizaciones de comercialización registradas en la base de datos consultada para Argentina (0 registros ANMAT). No se dispone de información de licencias o formas farmacéuticas locales aprobadas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen al menos dos ensayos clínicos directos de piroxicam en artritis crónica juvenil/JRA (PMID 3510686: ECA multicéntrico doble ciego; PMID 2957205: ECA aleatorizado), ambos con resultados favorables y equivalentes a naproxeno —el comparador de referencia pediátrico. La semivida larga (~50 h en adultos, ~32.6 h en niños) permite dosificación una vez al día con ventaja en adherencia pediátrica. Los meta-análisis de red de 2021 y 2024 reconfirman la clase AINE como tratamiento de primera línea en JIA. La ausencia de registro ANMAT y la falta de datos de seguridad locales son los principales obstáculos para avanzar.

**Para avanzar se necesita:**
- Completar datos de mecanismo de acción (DG002) vía DrugBank API para el análisis mecanístico formal
- Obtener prospecto oficial con advertencias regulatorias (DG001) y evaluar específicamente la seguridad en población pediátrica (riesgo GI, función renal, tiempo de sangrado)
- Verificar si piroxicam posee o puede obtener aprobación pediátrica en Argentina (ANMAT) o bajo normativas de referencia (EMA/FDA)
- Evaluar disponibilidad de formulaciones pediátricas adecuadas (suspensión oral, cápsulas en dosis por peso corporal)
- Diseñar protocolo de monitoreo de seguridad específico para niños: hemograma, función hepática y renal, evaluación gastrointestinal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

