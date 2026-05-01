---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: De Prevención Trombótica Cardiovascular a Migraña con Aura de Tronco Encefálico

## Resumen en Una Frase

Clopidogrel es un antiagregante plaquetario de la clase tienopiridina, ampliamente utilizado para la prevención de eventos aterotrombóticos en pacientes con síndrome coronario agudo, ictus isquémico y enfermedad arterial periférica.
El modelo TxGNN predice que podría ser efectivo para **Migraña con Aura de Tronco Encefálico**, con **16 publicaciones** —incluyendo 3 estudios de Tier 1 (ECA o revisión sistemática)— que respaldan esta dirección, principalmente en el contexto de foramen oval permeable (PFO) y comunicación interauricular (CIA), aunque sin ensayos clínicos registrados específicamente para este subtipo.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Prevención de eventos aterotrombóticos (síndrome coronario agudo, ictus isquémico, enfermedad arterial periférica) |
| Nueva Indicación Predicha | Migraña con aura de tronco encefálico |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales de mecanismo de acción en este pack de evidencia. Sin embargo, Clopidogrel es farmacológicamente reconocido como un inhibidor irreversible del receptor plaquetario P2Y12: bloquea la agregación plaquetaria dependiente de ADP y suprime la liberación de sustancias vasoactivas —serotonina y tromboxano A2 (TXA2)— almacenadas en los gránulos plaquetarios. Este doble efecto antitrombótico y antiserotonérgico plaquetario constituye el eje central de la hipótesis de reposicionamiento en migraña.

La conexión entre Clopidogrel y la migraña con aura de tronco encefálico se sustenta en la asociación bien documentada entre el shunt cardíaco derecha-izquierda (PFO o CIA) y la migraña con aura. En presencia de estos defectos, microémbolos y sustancias vasoactivas eluden el filtro pulmonar e ingresan directamente a la circulación cerebral, donde pueden desencadenar la depresión cortical propagada (CSD), el mecanismo electrofisiológico subyacente del aura. La circulación posterior —territorio vertebrobasilar, del que depende el tronco encefálico— es especialmente vulnerable a émbolos paradójicos por su anatomía, lo cual otorga plausibilidad biológica particular para el subtipo "aura de tronco encefálico" (antes denominado migraña basilar): síntomas como vértigo, disartria, diplopia y ataxia reflejan precisamente disfunción del tronco encefálico irrigado por ese territorio.

Al inhibir la activación plaquetaria mediada por P2Y12, Clopidogrel podría reducir simultáneamente la formación de microémbolos paradójicos, la liberación de serotonina plaquetaria (con acción vasoconstrictora cerebral) y la señalización neuroinflamentoria trigeminal modulada por receptores P2Y12 en microglia. No obstante, toda la evidencia disponible fue generada en el contexto de PFO/CIA, y no existe ningún ensayo clínico diseñado específicamente para el subtipo de aura de tronco encefálico, lo que constituye la principal limitación de esta predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para migraña con aura de tronco encefálico.

> **Nota:** Para la indicación relacionada de **Migraña en general (rank 2)**, existen 8 ensayos clínicos incluyendo el ensayo CANOA completado (NCT00799045, n=220, Fase 4, JAMA 2015/2021), que demostró que la adición de Clopidogrel a aspirina reduce la incidencia de migraña de inicio post-cierre percutáneo de CIA. Ese cuerpo de evidencia eleva la confianza en el mecanismo, aunque no es directamente extensible al subtipo de tronco encefálico sin investigación específica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisión Sistemática | *Headache* | Explora la evidencia de antitrombóticos (incluyendo Clopidogrel) como prevención de migraña; síntesis más actualizada disponible |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | ECA | *European Heart Journal* | Ensayo PRIMA: cierre percutáneo de PFO en migraña con aura refractaria; Clopidogrel como antiagregante adjunto en ambos brazos |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | ECA Piloto | *Cephalalgia* | Primer ensayo piloto aleatorizado de Clopidogrel como profiláctico específico para migraña; datos de señal prometedores |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohorte Retrospectiva | *J Investigative Medicine* | Clopidogrel 75 mg/día como profiláctico complementario en migraña refractaria con PFO confirmado: reducción de frecuencia a 3 y 6 meses |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observacional | *Heart* | Primer reporte de que Clopidogrel reduce migraña con aura tras cierre percutáneo de PFO y CIA |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Piloto Abierto | *Neurology* | Estudio TRACTOR: ticagrelor en migraña refractaria/PFO, motivado por hallazgos previos positivos con Clopidogrel; valida la hipótesis de clase P2Y12 |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Revisión Retrospectiva | *Neurology* | Experiencia clínica con tienopiridinas en migrañosos con PFO: reducción de ataques con Clopidogrel y prasugrel en uso off-label |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Revisión Retrospectiva | *Cephalalgia* | Clopidogrel como terapia primaria en migrañosos con shunt derecha-izquierda; vincula activación plaquetaria y embolia paradójica |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Serie de Casos | *J Interventional Cardiology* | Migraña intensa de inicio agudo tras cierre de CIA: alivio casi inmediato con carga de 300 mg de Clopidogrel |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Reporte/Serie | *Cephalalgia* | Migraña de novo tras cierre de CIA; antiagregantes como Clopidogrel asociados con mejoría; ticlopidina como alternativa de clase |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe un mecanismo biológico plausible y coherente (inhibición de P2Y12 → reducción de microémbolos paradójicos y activación plaquetaria en contexto de shunt cardíaco), con nivel de evidencia L3 para el espectro migraña-PFO/CIA; sin embargo, la ausencia total de ensayos clínicos específicamente diseñados para el subtipo **migraña con aura de tronco encefálico**, sumada a la falta de registro de Clopidogrel en Argentina, impide avanzar sin investigación adicional dirigida.

**Para avanzar se necesita:**
- Obtención del mecanismo de acción formal (DrugBank API / prospecto oficial) para completar el análisis de seguridad
- Diseño de un estudio prospectivo que incluya criterios diagnósticos explícitos de migraña con aura de tronco encefálico (según ICHD-3) y confirmación de PFO mediante ecocardiografía con contraste o Doppler transcraneal
- Consulta y análisis del prospecto ANMAT/TFDA para extraer advertencias clave, contraindicaciones e interacciones farmacológicas relevantes (especialmente con anticoagulantes y AINEs)
- Seguimiento del resultado publicado del ensayo NCT02938182 (Phase 4, n=50, Clopidogrel en migraña con shunt derecha-izquierda) para verificar si es extensible a este subtipo
- Evaluación del ensayo activo SPRING (NCT04946734, Phase 3, n=440) cuya finalización en 2025 podría aportar evidencia L1 para el espectro migraña-PFO, informando indirectamente sobre este subtipo
- Consideración de registro inicial en Argentina como condición habilitante para cualquier desarrollo clínico local
---

