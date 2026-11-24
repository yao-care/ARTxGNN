---
layout: default
title: Pregabalina
parent: Solo Predicción del Modelo (L5)
nav_order: 306
evidence_level: L5
indication_count: 6
drugbank_id: DB00230
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-11-24
description: "Pregabalina: nueva indicación predicha, Tendinitis (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Pregabalina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Pregabalina: Tendinitis
{: .text-alpha }

## Resumen en Una Frase

Pregabalina es un fármaco que se comercializa en Argentina con numerosas autorizaciones vigentes. El modelo TxGNN predice que podría ser efectivo para **tendinitis (tendinitis)**, pero no hay ensayos clínicos registrados y la literatura recuperada (6 publicaciones) no evalúa directamente su uso en esta enfermedad. La evidencia actual es, por lo tanto, solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Pregabalina se une a la subunidad alfa2-delta de los canales de calcio dependientes de voltaje y reduce la liberación de glutamato, sustancia P y CGRP. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento farmacológico general.

Mecanísticamente, esta acción podría atenuar los componentes neuropáticos o de sensibilización central del dolor tendinoso crónico. Es una hipótesis plausible, pero no está demostrada en esta enfermedad.

Conviene ser claro: la literatura recuperada no muestra evidencia directa de tratamiento en tendinitis. Pregabalina aparece solo como analgesia perioperatoria (por ejemplo, tras reparación artroscópica del manguito rotador), en reportes de casos de atrapamiento nervioso o discapacidad asociada a fluoroquinolonas, y en un estudio preclínico de neuropatía. El puntaje alto del modelo (0,9971) no está respaldado por datos clínicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECA (dolor posoperatorio, indirecto) | Arthroscopy | Pregabalina oral perioperatoria logró puntuaciones de dolor posoperatorio equivalentes al bloqueo interescalénico tras reparación artroscópica del manguito rotador. No evalúa tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Cohorte retrospectiva (indirecto) | J Orthop Sci | Evalúa el efecto analgésico y ahorrador de opioides de pregabalina tras reparación del manguito rotador. Indirecto. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Reporte de caso | Praxis | Discapacidad asociada a fluoroquinolonas (ciprofloxacino), con tendinopatía como efecto adverso del antibiótico. No evalúa pregabalina como tratamiento. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Reporte de caso | Pain Pract | Atrapamiento del nervio cutáneo femoral posterior tras maratón, por tendinitis de isquiotibiales. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Comentario editorial | Arthroscopy | Síndrome piriforme y su diagnóstico y tratamiento quirúrgico. No evalúa pregabalina en tendinitis. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclínico (ratas) | Adv Pharmacol Pharm Sci | Un extracto vegetal atenúa la neuropatía periférica inducida por vincristina. No involucra a pregabalina en tendinitis. |

## Información de Mercado en Argentina

Pregabalina se comercializa en Argentina con al menos 20 autorizaciones vigentes (la lista puede ser parcial). Algunas de las principales:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 42932 | AXUAL | 75 mg caps.x 15 | Teva Argentina | Vigente |
| 49154 | PREBICTAL | 100 mg cáps.x 28 | Adium | Vigente |
| 53931 | GAVANEURAL | 25 mg caps.x 30 | Denver Farma | Vigente |
| 50363 | LYRICA | 300 mg cáps.x 30 | Aspen Pharma | Vigente |
| 52070 | PLENICA | 50 mg cáps.x 15 | Roemmers | Vigente |

La tabla muestra 5 de los 20 productos recopilados de este medicamento en los datos (listado de medicamentos para entidades de PAMI); los datos solo incluyen una parte de los productos y la lista puede estar incompleta; el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tendinitis se basa solo en el modelo: no hay ensayos clínicos y ninguna publicación estudia directamente pregabalina en esta enfermedad. Por eso el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios clínicos o de mecanismo que evalúen directamente pregabalina en tendinitis (especialmente dolor tendinoso crónico con componente neuropático)
- Datos del mecanismo de acción y de seguridad (advertencias y contraindicaciones del prospecto de ANMAT)
- Revisión del texto de indicaciones de las autorizaciones locales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

