---
layout: default
title: Cetirizina
parent: Solo Predicción del Modelo (L5)
nav_order: 95
evidence_level: L5
indication_count: 3
drugbank_id: DB00341
monitor_inn: "Cetirizine"
predicted_indications: ["nasal cavity disease", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
last_modified_at: 2026-11-16
description: "Cetirizina: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cetirizina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Cetirizina: Nasal cavity disease
{: .text-alpha }

## Resumen en Una Frase

Cetirizina es un antihistamínico de segunda generación que actúa sobre el receptor H1 de la histamina.
Esta dirección está respaldada por **1 ensayo clínico** (Fase 3 piloto, completado) y por literatura científica, en su mayoría revisiones y reportes indirectos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Nasal cavity disease |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (18 de 18) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 18 (vigentes: 18) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información farmacológica conocida, cetirizina es un agonista inverso del receptor H1 de la histamina con selectividad periférica. Bloquea la vía mediada por histamina que produce el habón, el eritema y el prurito, que son las manifestaciones centrales de la urticaria.

El mecanismo es directamente relevante para esta predicción. La histamina liberada por los mastocitos es el mediador principal de la urticaria, y los antihistamínicos H1 son el tratamiento de primera línea habitual. Por eso la predicción se parece más a un uso farmacológicamente esperable que a un reposicionamiento de fondo.

Los datos disponibles no permiten confirmar si este uso figura en la información de uso aprobada localmente. Esa concordancia con el prospecto debe verificarse manualmente.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Fase 3 | Completado | 36 | Estudio piloto multicéntrico, aleatorizado y doble ciego. Compara cetirizina inyectable IV 10 mg con difenhidramina IV 50 mg en urticaria aguda atendida en urgencias, centros de atención inmediata y clínicas de alergia. Evalúa la factibilidad de un ensayo de Fase 3 posterior. |

Este ensayo es un piloto de factibilidad con 36 participantes. No es un ensayo confirmatorio con poder estadístico suficiente. Además, evalúa la vía intravenosa, que debe confirmarse frente a las presentaciones disponibles en Argentina.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Revisión narrativa | Advances in Therapy | Describe el papel de cetirizina IV entre los antihistamínicos intravenosos. Señala que en 2019 se aprobó la cetirizina IV para urticaria aguda (en EE. UU.). |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Revisión | Allergy | Estudios clínicos con cetirizina en rinitis alérgica y urticaria crónica (sin resumen disponible). |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Revisión | Current Medicinal Chemistry | Actualización sobre levocetirizina, enantiómero R de cetirizina, con baja metabolización hepática. |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Revisión comparativa | Drugs | Compara antihistamínicos de segunda generación, incluida cetirizina, en cuanto a sedación y características para elegir entre ellos. |
| [29565188](https://pubmed.ncbi.nlm.nih.gov/29565188/) | 2018 | Revisión de seguridad / observacional | J Obstet Gynaecol | Resultados de embarazos con exposición materna a cetirizina, a partir de una base de datos de seguridad del fabricante. |
| [27650241](https://pubmed.ncbi.nlm.nih.gov/27650241/) | 2016 | Revisión | Am J Med Sci | Uso de medicamentos para alergia durante el embarazo. |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Reporte de caso | J Clin Gastroenterol | Colestasis inducida por cetirizina en un hombre de 28 años. |
| [19348661](https://pubmed.ncbi.nlm.nih.gov/19348661/) | 2009 | Reporte de caso | J Dermatol | Urticaria exacerbada por antihistamínicos H1 en una paciente, un fenómeno poco frecuente. |
| [32853084](https://pubmed.ncbi.nlm.nih.gov/32853084/) | 2021 | Estudio de farmacocinética | J Hum Lact | Transferencia de cetirizina a la leche humana. |
| [8477125](https://pubmed.ncbi.nlm.nih.gov/8477125/) | 1993 | Revisión | Ann Pharmacother | Presentación de cetirizina como antihistamínico no sedante: mecanismo, ensayos y efectos adversos. |

La literatura recuperada es mayormente indirecta: revisiones generales y reportes de seguridad. No se identificó un ensayo aleatorizado publicado que estudie directamente cetirizina en urticaria alérgica.

## Información de Mercado en Argentina

El fármaco se encuentra comercializado en Argentina con autorizaciones vigentes como producto de un solo principio activo. El texto de indicación aprobada no figura en los registros locales. A continuación se listan 5 de las autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 32730 | CETIZINE | 10 mg comp. rec. x 10 |
| 9691 | ZYRTEC | 10 mg comp. x 10 |
| 9692 | ZYRTEC | 10 mg comp. x 30 |
| 28355 | CABAL | Gotas x 10 ml |
| 51838 | DEXALERGIN NOVO CB | 10 mg cáps. blanda x 30 |

## Consideraciones de Seguridad

Los datos compilados no incluyen advertencias, contraindicaciones ni interacciones del prospecto local. Consultar el prospecto para información de seguridad.

La literatura recuperada aporta estas observaciones complementarias:
- Se han descrito elevaciones transitorias y reversibles de transaminasas hepáticas en menos del 2 % de los pacientes en ensayos de EE. UU., y un caso de colestasis (PMID 11034010).
- Un artículo de 2021 señala que la FDA no recomienda su uso durante la lactancia por falta de estudios suficientes (PMID 32853084).
- Existen reportes aislados de urticaria desencadenada por antihistamínicos H1 (PMID 19348661).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado en urticaria aguda, aunque es un piloto de factibilidad pequeño. Falta evidencia confirmatoria directa y datos de seguridad locales, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias, contraindicaciones, interacciones).
- Verificar manualmente la concordancia del uso predicho con la información de uso aprobada localmente.
- Complementar los datos de mecanismo de acción desde una fuente farmacológica de referencia.
- Revisar los resultados completos del ensayo NCT02023164 (vía de administración, comparador y desenlaces) y buscar ensayos controlados adicionales.
- Confirmar qué presentaciones y vías de administración están disponibles en Argentina para el uso propuesto.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «La ausencia de resultados puede deberse a variaciones en el nombre comercial, formato de búsqueda, o a que la consulta fue realizada contra » | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «No se encontraron autorizaciones de comercialización para **CETIRIZINA** en el sistema consultado» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «[ ] **Verificar la fuente regulatoria**: Confirmar si la búsqueda debe realizarse en ANMAT (Argentina) en lugar de TFDA (Taiwán), dado que e» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

