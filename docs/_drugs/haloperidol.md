---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

Usando el skill **txgnn-pipeline** como contexto operativo, y aplicando el formato del **Prompt de Informe v5** sobre el Evidence Pack recibido.

> **Nota editorial**: Este Evidence Pack es de tipo `multi` con 10 indicaciones predichas. Las primeras 9 (rangos 1–9) son todas L5/Hold sin evidencia clínica. El rango 10 — **Trastorno Bipolar Afectivo Maníaco** — es el único candidato con nivel L1 y recomendación "Proceed with Guardrails". El informe se centra en este candidato, que es la única dirección clínicamente accionable del conjunto.

---

# Haloperidol: De Esquizofrenia a Trastorno Bipolar Afectivo Maníaco

## Resumen en Una Frase

Haloperidol es un antipsicótico típico de primera generación, utilizado globalmente en el tratamiento de la esquizofrenia, síndrome de Tourette y estados de agitación psicótica aguda.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Bipolar Afectivo Maníaco**,
con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Esquizofrenia y trastornos psicóticos (referencia global; sin registro local en Argentina) |
| Nueva Indicación Predicha | Trastorno Bipolar Afectivo Maníaco |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada (DG002 pendiente de resolución vía DrugBank API). Sin embargo, según la información farmacológica establecida en la literatura, Haloperidol es un antipsicótico típico con altísima afinidad por los receptores dopaminérgicos D2 y D1 del sistema nervioso central (Ki D2 ≈ 0.6 nM), lo que lo posiciona como uno de los antagonistas dopaminérgicos más potentes disponibles en terapéutica.

La relevancia mecanística para el trastorno bipolar maníaco es directa y sólida: los episodios maníacos agudos se asocian con una hiperdopaminergia en el sistema mesolímbico, que se expresa clínicamente como agitación, grandiosidad, pensamiento acelerado y reducción marcada de la necesidad de sueño. El bloqueo D2 de Haloperidol contrarresta de forma directa esta hiperactivación dopaminérgica, produciendo un control rápido de los síntomas maníacos más severos. Este es exactamente el mismo mecanismo que sustenta su eficacia en la esquizofrenia.

La predicción es, por tanto, mecanísticamente coherente: tanto la esquizofrenia como el episodio maníaco del trastorno bipolar comparten el substrato fisiopatológico de hiperdopaminergia mesolímbica. Lejos de ser una extrapolación especulativa, esta indicación está confirmada por múltiples ensayos de Fase 3 en los que Haloperidol fue incluido como brazo comparador activo —validando implícitamente su eficacia para la manía aguda— y por una revisión sistemática con metaanálisis en red publicada en *Molecular Psychiatry* (2022).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Fase 3 | Completado | 158 | Risperidona vs Placebo vs Haloperidol como terapia adyuvante a estabilizadores del ánimo en episodios maníacos de trastorno bipolar I; Haloperidol actúa como brazo activo de referencia estableciendo datos directos de eficacia |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Fase 3 | Completado | 615 | Aripiprazol vs Haloperidol (control activo) en monoterapia para manía aguda en bipolar I durante 12 semanas; es el estudio de mayor tamaño muestral disponible con datos de Haloperidol en manía |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Fase 3 | Completado | 439 | Risperidona vs Placebo vs Haloperidol en episodios maníacos de bipolar I; establece eficacia de Haloperidol a 3 semanas (agudo) y 12 semanas (mantenimiento) |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Fase 3 | Completado | 224 | Olanzapina vs Haloperidol vs Placebo en episodio maníaco o mixto de bipolar I; comparación directa cabeza a cabeza, confirmando eficacia antimaníaca de Haloperidol |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Fase 2 | Completado | 120 | Valproato + Amisulpride vs Valproato + Haloperidol (5–15 mg/día) en episodio maníaco de bipolar I a 3 meses; evalúa eficacia y seguridad de la combinación con Haloperidol |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Fase 3 | Completado | 22 | Antipsicótico inyectable de acción prolongada + programa conductual para adherencia en trastornos psicóticos crónicos (Tanzania); muestra pequeña, contexto de salud mental en África subsahariana |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | En reclutamiento | 200 | Estudio observacional sobre exposición antenatal a antipsicóticos en gestantes con enfermedad mental grave; no evalúa eficacia antimaníaca directamente |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Fase 4 | Terminado prematuramente | 11 | Olanzapina vs antipsicóticos convencionales en manía aguda (Suecia); terminado por reclutamiento insuficiente, datos no representativos |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Desconocido | 120 | Micronutrientes y omega-3 como tratamiento adyuvante en trastorno bipolar; Haloperidol no es el fármaco de interés principal |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Revisión Sistemática + NMA | Molecular Psychiatry | Metaanálisis en red de intervenciones farmacológicas para manía bipolar aguda; Haloperidol incluido como comparador activo de referencia; evalúa eficacia, aceptabilidad y seguridad |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | ECA doble ciego | Journal of Affective Disorders | Olanzapina vs Haloperidol vs Placebo en pacientes japoneses con bipolar I en episodio maníaco/mixto; confirma eficacia de Haloperidol en población asiática |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisión de Práctica Clínica | Acta Psychiatrica Scandinavica | Opciones terapéuticas basadas en evidencia para manía bipolar; recomienda Haloperidol en combinación con estabilizadores del ánimo para respondedores parciales |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Revisión Basada en Evidencia | CNS Neuroscience & Therapeutics | En manía aguda refractaria, añadir Haloperidol a litio o valproato es estrategia válida; revisión de manejo del trastorno bipolar resistente al tratamiento |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Análisis Comparativo | BMJ Mental Health | Comparación de equivalencias de dosis antipsicóticas entre manía aguda y esquizofrenia; incluye Haloperidol como referencia de potencia |
| [22161387](https://pubmed.ncbi.nlm.nih.gov/22161387/) | 2011 | Revisión Cochrane | Cochrane Database of Systematic Reviews | Oxcarbazepina en episodios afectivos de trastorno bipolar; contexto comparativo de eficacia de estabilizadores del ánimo frente a antipsicóticos clásicos |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Revisión Narrativa | BMJ Clinical Evidence | Trastorno bipolar: epidemiología, riesgo de suicidio, evolución clínica y opciones de tratamiento incluyendo antipsicóticos típicos como Haloperidol |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | ECA doble ciego | Journal of Clinical Psychiatry | Clonazepam vs Haloperidol en manía aguda; Haloperidol como comparador activo confirmado; datos de inicio de acción y perfil de tolerabilidad comparativo |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | ECA doble ciego | Archives of General Psychiatry | Litio + Haloperidol vs Placebo + Haloperidol en trastorno esquizoafectivo maníaco; diferencia estadísticamente significativa favorable a la combinación |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | Evaluación de Tecnología Sanitaria | Health Technology Assessment | Evaluación de eficacia y costo-efectividad de quetiapina, olanzapina y valproato en manía; Haloperidol empleado como comparador de referencia |

---

## Información de Mercado en Argentina

Haloperidol **no cuenta con autorizaciones de comercialización** registradas en Argentina según los datos consultados en ANMAT (fecha de corte: 2026-05-01, total de licencias: 0). No existe información de formas farmacéuticas aprobadas localmente.

> Se recomienda verificar directamente con ANMAT si existen registros vigentes no capturados en esta consulta, dado que Haloperidol es un fármaco de uso global ampliamente disponible en otros mercados regulados.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Cuatro ensayos clínicos de Fase 3 completados —con tamaños muestrales de 158 a 615 participantes— confirman la eficacia de Haloperidol en el control de episodios maníacos agudos del trastorno bipolar I, y el mecanismo D2-antagonista es directamente coherente con la fisiopatología hiperdopaminérgica de la manía. La predicción TxGNN (99.83%) y el nivel de evidencia L1 reflejan adecuadamente esta solidez. La ausencia de registro local en Argentina no invalida la evidencia clínica internacional, pero sí condiciona la vía de implementación.

**Para avanzar se necesita:**
- Resolver **DG001**: obtener información completa de seguridad (advertencias, contraindicaciones, advertencias de caja negra) del prospecto oficial o de ANMAT, con énfasis en síntomas extrapiramidales (EPS), discinesia tardía y síndrome neuroléptico maligno
- Resolver **DG002**: completar datos de mecanismo de acción vía DrugBank API (DB00502) para reforzar la sección de racionalidad mecanística
- Evaluar **vía de registro en Argentina** (ANMAT): determinar si aplica registro nuevo, extensión de indicación o importación bajo autorización especial
- Definir el **nicho terapéutico local**: comparar frente a antipsicóticos atípicos de segunda generación disponibles en Argentina (ej. risperidona, olanzapina, aripiprazol) para establecer ventajas diferenciales (costo, disponibilidad, perfil de EPS)
- Establecer **plan de monitoreo de seguridad** específico: escala AIMS para discinesia tardía, monitoreo de intervalo QTc y función hepática en uso prolongado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

