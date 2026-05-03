---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

El skill de TxGNN pipeline es de gestión de modelos/deployment — no aplica específicamente a la generación de reportes. Procedo directamente según el formato del sistema de prompts.

---

Analizando el Evidence Pack:

- **Indicaciones rankeadas 1-8**: Todas son enfermedades genéticas raras con cero evidencia (L5, Hold)
- **Indicación rank 9 (Artritis Idiopática Juvenil)**: La única con evidencia real — L3, 2 ensayos clínicos, 18 publicaciones, recomendación "Proceed with Guardrails"
- **Regulatorio Argentina**: Sin autorizaciones registradas (0 licencias)
- **MOA**: [Data Gap] — pero Diclofenac es un AINE COX-1/COX-2 de conocimiento universal
- **No es antineoplásico** → sección Citotoxicidad se omite

El reporte se centra en la indicación con mayor evidencia clínica real (JIA/AIJ).

---

# DICLOFENAC: De Anti-inflamatorio No Esteroideo a Artritis Idiopática Juvenil

## Resumen en Una Frase

Diclofenac es un antiinflamatorio no esteroideo (AINE) ampliamente utilizado para el tratamiento del dolor agudo y crónico, la osteoartritis y la artritis reumatoide en adultos a nivel global.
El modelo TxGNN predice que podría ser efectivo para la **Artritis Idiopática Juvenil (AIJ)**, la forma más frecuente de enfermedad reumática crónica en niños, con un puntaje de predicción del **99.25%**.
Esta dirección cuenta con **2 ensayos clínicos registrados** y **18 publicaciones científicas** — incluyendo ensayos clínicos cruzados con diclofenac específicamente en población pediátrica — que respaldan esta aplicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor e inflamación (AINE; artritis reumatoide y osteoartritis en adultos) |
| Nueva Indicación Predicha | Artritis Idiopática Juvenil (AIJ) |
| Puntaje de Predicción TxGNN | 99.25% (Rank #9 entre las predicciones) |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado (sin registros en la base consultada) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Diclofenac actúa como inhibidor no selectivo de las ciclooxigenasas COX-1 y COX-2, bloqueando la conversión del ácido araquidónico en prostaglandinas — principalmente PGE2 — que son los mediadores centrales de la inflamación, el dolor y la fiebre. Este mecanismo está directamente implicado en la fisiopatología articular inflamatoria y constituye la base de la eficacia de diclofenac en artritis reumatoide y osteoartritis en adultos. Aunque los datos detallados de MOA no están disponibles en la base de datos consultada, el mecanismo farmacológico de diclofenac es uno de los más caracterizados en medicina.

La Artritis Idiopática Juvenil comparte el mismo mecanismo patológico central que las artritis adultas: sinovitis crónica mediada por sobreproducción de PGE2, con infiltración de células inmunes en la membrana sinovial que genera inflamación articular, dolor y daño articular progresivo en niños menores de 16 años. La extensión farmacológica de diclofenac hacia la AIJ es directa: la inhibición de COX reduce localmente la producción de PGE2 sinovial, aliviando la sinovitis y el dolor articular. Esta continuidad mecanística desde la indicación adulta hacia la población pediátrica tiene sólida justificación farmacodinámica y no requiere un salto conceptual significativo.

Cabe señalar que entre las 10 principales predicciones de TxGNN para diclofenac, las posiciones 1 a 8 corresponden a enfermedades genéticas raras (displasias esqueléticas, hipotricosis hereditarias, WHIM syndrome) donde el vínculo mecanístico con los AINEs es débil o inexistente y la evidencia es nula (nivel L5). La AIJ en posición 9, en cambio, posee la mayor coherencia mecanística y la más abundante evidencia clínica directa para diclofenac, convirtiéndola en la indicación más accionable del conjunto.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00688545](https://clinicaltrials.gov/study/NCT00688545) | N/A | Terminado | 275 | Registro observacional multicéntrico (SINCERE™) de seguridad a largo plazo de NSAIDs no selectivos vs. Celecoxib en pacientes con AIJ; diclofenac potencialmente incluido como NSAID de referencia. Provee datos de seguridad en práctica clínica real. |
| [NCT05871086](https://clinicaltrials.gov/study/NCT05871086) | Fase 2/3 | Desconocido | 60 | Evaluación de suplementación con Coenzima Q10 en AIJ; NSAIDs (incluyendo diclofenac potencialmente) utilizados como terapia de fondo estándar. La relevancia directa para diclofenac es limitada dado que es terapia concomitante, no el brazo experimental. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3052965](https://pubmed.ncbi.nlm.nih.gov/3052965/) | 1988 | ECA Cruzado | Clinical and Experimental Rheumatology | Comparación de naproxeno, diclofenac (2 mg/kg/día) y tolmetina en 28 niños con AIJ seronegativa durante 12 semanas; eficacia clínica y laboratorial comparable entre los tres NSAIDs. Primer ECA cruzado con diclofenac en población pediátrica artrítica. |
| [6361986](https://pubmed.ncbi.nlm.nih.gov/6361986/) | 1983 | Ensayo Clínico (abierto) | Scandinavian Journal of Rheumatology | Farmacocinética y eficacia de diclofenac sódico en artritis reumatoide juvenil; evaluación de niveles plasmáticos y eliminación renal en niños de 2-7 años tras dosis única (25 mg Voltaren entérico). |
| [2235663](https://pubmed.ncbi.nlm.nih.gov/2235663/) | 1990 | Ensayo Clínico | La Pediatria Medica e Chirurgica | Estudio no comparativo abierto de eficacia de diclofenac sódico en AIJ poliarticular en 26 pacientes pediátricos de 2-16 años, incluyendo casos refractarios a otras terapias antiinflamatorias previas. |
| [10756785](https://pubmed.ncbi.nlm.nih.gov/10756785/) | 1997 | Revisión Comparativa | Revista Medico-Chirurgicala | Estudio comparativo de NSAIDs (diclofenac, ibuprofeno y aspirina) en 100 niños con artritis crónica juvenil durante hasta 3 años; análisis de evolución clínica y parámetros de laboratorio en seguimiento prolongado. |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Revisión | British Journal of Rheumatology | Revisión del uso de NSAIDs en enfermedades reumáticas pediátricas; diclofenac citado como equivalente en eficacia y tolerabilidad a ibuprofeno, naproxeno y tolmetina para el control de síntomas articulares en AIJ. |
| [11735667](https://pubmed.ncbi.nlm.nih.gov/11735667/) | 2001 | Revisión Comparativa | Paediatric Drugs | Análisis de riesgos y beneficios de NSAIDs vs. paracetamol en niños; diclofenac evaluado en AIJ, fiebre y dolor postoperatorio; revisión de farmacocinética pediátrica y perfil de seguridad. |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Revisión PK | Clinical Pharmacokinetics | Farmacología clínica de NSAIDs en artritis juvenil; incluye datos de farmacocinética de diclofenac en niños con recomendaciones de dosificación basadas en peso. |
| [17474954](https://pubmed.ncbi.nlm.nih.gov/17474954/) | 2007 | Encuesta Clínica | Paediatric Anaesthesia | Encuesta sobre uso de NSAIDs en pediatría; confirma que diclofenac está actualmente autorizado para mayores de 1 año para el tratamiento de artritis reumatoide juvenil (uso off-label en otras indicaciones pediátricas). |
| [6761640](https://pubmed.ncbi.nlm.nih.gov/6761640/) | 1982 | Ensayo Clínico | Pediatriia | Evaluación de Voltaren® (diclofenac sódico) en el tratamiento de niños con artritis reumatoide; datos de eficacia clínica en muestra pediátrica con seguimiento estructurado. |
| [723822](https://pubmed.ncbi.nlm.nih.gov/723822/) | 1978 | Ensayo Clínico | Minerva Pediatrica | Uno de los primeros reportes del uso de diclofenac sódico en artritis reumatoide infantil; datos pioneros de eficacia y tolerabilidad en población pediátrica. |

---

## Información de Mercado en Argentina

Diclofenac **no posee autorizaciones de comercialización registradas en Argentina** en la base de datos consultada (0 licencias, estado: no comercializado).

> **Nota importante sobre brecha de datos**: Diclofenac es uno de los AINEs de mayor uso global y se encuentra ampliamente comercializado en la mayoría de los países del mundo bajo marcas como Voltaren®, Cataflam® y otras. La ausencia de registros en esta base de datos debe interpretarse con precaución: es probable que refleje una brecha en la fuente de datos consultada antes que la ausencia real de comercialización en Argentina. Se recomienda verificar directamente en el sistema ANMAT o vademécum argentino oficial.

---

## Consideraciones de Seguridad

Los datos de advertencias, contraindicaciones e interacciones farmacológicas específicas no están disponibles en la base de datos consultada para este análisis.

Consultar el prospecto oficial aprobado para información de seguridad completa. Como referencia general para diclofenac como AINE, los aspectos de seguridad típicamente relevantes en uso pediátrico incluyen:

- **Riesgo gastrointestinal**: úlcera y sangrado (considerar gastroprotección en tratamientos prolongados)
- **Riesgo renal**: monitoreo de función renal en pacientes pediátricos con AIJ activa o enfermedad sistémica
- **Riesgo cardiovascular**: consideración en uso crónico
- **Función hepática**: monitoreo recomendado en tratamientos prolongados en niños
- **Dosificación pediátrica**: 2 mg/kg/día según datos disponibles en literatura; ajuste por peso obligatorio

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Diclofenac presenta una extensión farmacológica directamente justificada hacia la Artritis Idiopática Juvenil: el mecanismo COX/PGE2 que explica su eficacia en adultos opera igualmente en la sinovitis juvenil. La evidencia disponible —aunque históricamente concentrada en las décadas de 1980-90— incluye ensayos clínicos controlados cruzados y estudios abiertos con diclofenac específicamente en niños con artritis, y fuentes regulatorias internacionales confirman su autorización pediátrica en al menos una jurisdicción para esta indicación. El nivel de evidencia L3 es suficiente para considerar avanzar con precauciones específicas.

**Para avanzar se necesita:**
- Verificar el estado regulatorio real de diclofenac en Argentina a través de ANMAT (probable brecha de datos en la fuente consultada)
- Obtener datos completos de MOA desde DrugBank (actualmente no disponibles en el pack)
- Consultar el prospecto oficial argentino o internacional para advertencias y contraindicaciones en uso pediátrico
- Identificar ensayos clínicos modernos (post-2000) de diclofenac específicamente en AIJ, dado que la evidencia directa existente data de los años 80-90
- Definir formulación pediátrica apropiada (suspensión oral u otras formas de dosis ajustable por peso)
- Establecer plan de monitoreo para uso prolongado en niños: hemograma, función hepática, función renal y evaluación gastrointestinal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

