---
layout: default
title: Pantoprazol
parent: Solo Predicción del Modelo (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
drugbank_id: DB00213
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-16
description: "Pantoprazol: nueva indicación predicha, Duodenal obstruction (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Pantoprazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Pantoprazol: Duodenal obstruction
{: .text-alpha }

## Resumen en Una Frase

Pantoprazol es un inhibidor de la bomba de protones que reduce la secreción de ácido gástrico.
De ellas, solo una parte estudia directamente la enfermedad; el resto son revisiones generales o estudios de otras condiciones.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Duodenal obstruction |
| Puntaje de Predicción TxGNN | 0.9921 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida y la literatura revisada, pantoprazol inhibe de forma irreversible la H+/K+ ATPasa de la célula parietal gástrica (la bomba de protones), con lo que produce una supresión intensa y sostenida del ácido gástrico.

Esa supresión ácida favorece la cicatrización de las úlceras y respalda los esquemas de erradicación de *Helicobacter pylori*. Mecanísticamente, por tanto, la aplicación a la úlcera péptica activa es directa. Se trata más de una confirmación de un uso farmacológico central que de un reposicionamiento novedoso.

Dado que el texto de indicaciones de las licencias locales está vacío, no es posible confirmar con esos datos si este uso figura en el prospecto. Debe verificarse contra el prospecto autorizado.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Fase 3 | Completado | 323 | Ensayo aleatorizado, doble ciego, con control activo: ilaprazol vs. pantoprazol en terapia triple de 7 días para erradicar *H. pylori* en pacientes con úlcera gástrica y/o duodenal. Debe confirmarse el comparador exacto, pues el título está truncado. |

## Evidencia de Literatura

La literatura asociada a esta predicción incluye sobre todo revisiones farmacológicas generales. Se destacan los estudios más cercanos a la enfermedad:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9692693](https://pubmed.ncbi.nlm.nih.gov/9692693/) | 1998 | ECA | Aliment Pharmacol Ther | Eficacia de la terapia triple de 10 días basada en pantoprazol para erradicar *H. pylori* (estudio piloto de un solo centro). |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática / metaanálisis en red | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potasio con IBP en esofagitis grado C/D (otra condición). |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisión | Clin Drug Investig | Revisión de pantoprazol como IBP: unión irreversible a la bomba de protones y larga duración de acción. |
| [16700898](https://pubmed.ncbi.nlm.nih.gov/16700898/) | 2006 | Revisión | Aliment Pharmacol Ther | Farmacología clínica de los IBP y diferencias en su velocidad de activación. |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Revisión | Pharmacotherapy | IBP en enfermedades relacionadas con el ácido; más eficaces que los antagonistas H2. |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Estudio clínico | Aliment Pharmacol Ther | Pantoprazol con amoxicilina y azitromicina o claritromicina para erradicar *H. pylori* en úlcera duodenal. |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Revisión | Expert Opin Investig Drugs | Enfoques terapéuticos en úlceras gástricas y duodenales; causas principales: *H. pylori* y AINE. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 23256 | PANTOP | IV iny.x 1 | No registrada en los datos locales |
| 32555 | PANTUS IV | 40 mg IV f.a.liof.x 1 | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. En los datos compilados no constan advertencias, contraindicaciones ni interacciones farmacológicas para este fármaco.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado (n=323) que estudia pacientes con úlcera gástrica y/o duodenal, y literatura clínica sobre pantoprazol en úlcera. Sin embargo, ese ensayo se centra en la erradicación de *H. pylori* y su comparador debe confirmarse. Por ello el nivel L1 asignado debe tomarse con cautela, ya que la regla de dos ECA de Fase 3 completados no queda claramente demostrada con los estudios dirigidos a esta enfermedad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente no disponible.
- Confirmar si la úlcera péptica activa figura en las indicaciones autorizadas localmente.
- Verificar el diseño y el comparador del ensayo NCT02084420.
- Obtener datos del mecanismo de acción desde una fuente de referencia (p. ej., DrugBank).
- Definir un plan de monitoreo de seguridad para uso intravenoso y poblaciones específicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

