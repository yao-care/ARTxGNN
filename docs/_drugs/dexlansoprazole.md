---
layout: default
title: Dexlansoprazole
parent: Solo Predicción del Modelo (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dexlansoprazole: nueva indicación predicha, Enfermedad ulcerosa péptica activa (nivel de evidencia L5). Indicación original: Enfermedad ulcerosa péptica (según el grafo de conocimiento"
monitor_inn: "dexlansoprazole"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
---

# Dexlansoprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Dexlansoprazol: De Enfermedad Ulcerosa Péptica a Enfermedad Ulcerosa Péptica Activa

## Resumen en Una Frase

Dexlansoprazol es un inhibidor de la bomba de protones, originalmente utilizado para la enfermedad ulcerosa péptica, la enfermedad por reflujo gastroesofágico y la esofagitis.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ulcerosa péptica activa**, aunque esta indicación se superpone con la ya conocida y no constituye un reposicionamiento genuino.
Para esta predicción hay **2 ensayos clínicos de Fase 3** vinculados (realizados en esofagitis erosiva, no en úlcera) y **3 publicaciones** de apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad ulcerosa péptica (según el grafo de conocimiento; los textos de indicación aprobada de ANMAT están vacíos) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L4 (los ensayos de Fase 3 no evaluaron úlcera de forma directa) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, dexlansoprazol es un inhibidor de la bomba de protones (enantiómero de lansoprazol, de liberación modificada) que suprime la secreción de ácido gástrico al inhibir la H+/K+-ATPasa.

La supresión ácida es coherente con la cicatrización de úlceras. Sin embargo, la enfermedad ulcerosa péptica ya figura entre las indicaciones originales del fármaco, por lo que esta predicción es una **confirmación de una indicación existente** más que un reposicionamiento real.

Los ensayos de Fase 3 disponibles (TAK-390MR) se realizaron en poblaciones con esofagitis erosiva y ERGE. Demuestran eficacia y seguridad de la supresión ácida, pero no demuestran directamente la cicatrización de úlceras.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Fase 3 | Completado | 2054 | Dexlansoprazol MR (60 y 90 mg) vs lansoprazol 30 mg en la cicatrización de esofagitis erosiva durante 8 semanas |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Fase 3 | Completado | 2038 | Estudio gemelo del anterior: dexlansoprazol MR vs lansoprazol en cicatrización de esofagitis erosiva |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática / metaanálisis en red | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potasio (P-CAB) con IBP en la cicatrización de esofagitis grado C/D |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Revisión | Curr Opin Investig Drugs | Desarrollo de dexlansoprazol, formulación de liberación modificada de un enantiómero de lansoprazol, para esofagitis por reflujo |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclínico / mecanístico | J Chin Med Assoc | Mecanismo por el que los IBP suprimen la ATPasa vacuolar e inducen estrés del retículo endoplásmico, en relación con el riesgo de cáncer gástrico |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53829 | IBEPRAL 60 | Cápsulas x 15 | No disponible |
| 53830 | IBEPRAL 60 | Cápsulas x 30 | No disponible |
| 50098 | APATRIX 30 | Cápsulas x 30 | No disponible |
| 50099 | APATRIX 60 | Cápsulas x 15 | No disponible |
| 59411 | ARIGASTRIL 30 | Cápsulas x 30 | No disponible |

Se muestran 5 de las 15 autorizaciones vigentes, todas de producto de un solo principio activo.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, osteoporosis, osteoporosis posmenopáusica y fractura ósea.
- **Interacciones Farmacológicas**: se identificaron 118 interacciones potenciales. Entre las de nivel **mayor** figuran acalabrutinib y atazanavir. Entre las de nivel moderado figuran furosemida, hidroclorotiazida, gefitinib, bosutinib, anfetamina y anfotericina B. Entre las de nivel menor figuran ácido acetilsalicílico, cianocobalamina y axitinib.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción coincide con una indicación ya conocida, por lo que no aporta un reposicionamiento nuevo. Los ensayos de Fase 3 vinculados se realizaron en esofagitis erosiva y no confirman eficacia específica en úlcera péptica activa, por lo que el nivel de evidencia es L4.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas), actualmente sin datos.
- Completar los datos del mecanismo de acción.
- Evidencia directa de eficacia en úlcera péptica (por ejemplo, resultados del ensayo NCT07344506, en curso, centrado en erradicación de *H. pylori*).
- Evaluar el riesgo de las interacciones de nivel mayor y de las contraindicaciones del grafo de conocimiento (hepáticas, óseas y biliares).

## Otras Predicciones del Modelo (Referencia)

Las demás predicciones tienen evidencia limitada:

- **Úlcera duodenal** y **úlcera gástrica**: nivel L1 asignado por ensayos de Fase 3 en esofagitis, con eficacia específica no confirmada. Es la dirección más prometedora tras la principal.
- **Úlcera gastroyeyunal** (L4): único ensayo retirado, sin participantes.
- **Perforación de úlcera péptica, gastroduodenitis, obstrucción duodenal, reflujo duodenogástrico** (L5): solo predicción del modelo.
- **Aclorhidria**: probable falso positivo, ya que suprimir más el ácido no tiene justificación terapéutica.
- **Estómago en bota de cuero**: sin respaldo mecanístico ni clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

