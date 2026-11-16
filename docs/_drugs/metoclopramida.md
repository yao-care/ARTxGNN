---
layout: default
title: Metoclopramida
parent: Solo Predicción del Modelo (L5)
nav_order: 250
evidence_level: L5
indication_count: 2
drugbank_id: DB01233
monitor_inn: "Metoclopramide"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
last_modified_at: 2026-11-16
description: "Metoclopramida: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Metoclopramida
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Metoclopramida: Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

Metoclopramida es un fármaco procinético y antiemético que actúa sobre los receptores de dopamina D2 y de serotonina 5-HT4, y que se comercializa en Argentina con múltiples autorizaciones vigentes.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (19 de 19) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 19 (vigentes: 19) |
| Decisión Recomendada | Hold |

## ¿Por qué es razonable esta predicción?

Metoclopramida antagoniza los receptores D2 de dopamina y estimula los receptores 5-HT4. Con ello acelera el vaciamiento gástrico y mejora la coordinación antroduodenal. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción; esta descripción proviene del análisis de la predicción.

La relación con la úlcera gástrica es débil e indirecta. El fármaco podría ayudar cuando la úlcera se acompaña de vaciamiento gástrico retardado o de reflujo duodenogástrico, y también para limpiar sangre y restos alimentarios antes de una endoscopia. Sin embargo, no suprime la acidez ni promueve la cicatrización de la mucosa, por lo que un efecto modificador de la enfermedad no tiene respaldo mecanístico.

Además, un estudio preclínico en ratas (PMID 3816940) mostró que antagonistas dopaminérgicos, incluida la metoclopramida, provocaron lesiones gástricas. Esto va en sentido contrario a la hipótesis de beneficio. Por todo ello, la alta puntuación del modelo debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Fase 4 | Desconocido | 60 | Metoclopramida como premedicación en hemorragia digestiva alta; evalúa la necesidad de repetir la endoscopia y la visibilidad de la pared gástrica. No mide la cicatrización de la úlcera. Relevancia indirecta. |

## Evidencia de Literatura

La mayor parte de las publicaciones recuperadas trata temas relacionados (gastroparesia, dispepsia, reflujo) y no estudia directamente la úlcera gástrica. Se listan las más pertinentes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Revisión | Drugs | Propiedades farmacológicas y uso clínico de metoclopramida; facilita la endoscopia de urgencia en hemorragia digestiva alta. |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Revisión sistemática | Paediatric Drugs | Tratamiento farmacológico del reflujo gastroesofágico en niños; tema relacionado, no úlcera. |
| [3816940](https://pubmed.ncbi.nlm.nih.gov/3816940/) | 1986 | Preclínico (rata) | European Journal of Pharmacology | Los antagonistas dopaminérgicos, incluida la metoclopramida, provocaron lesiones gástricas en ratas. |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Revisión | Drugs | Gastroparesia diabética; tema relacionado. |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Revisión | Current Treatment Options in Gastroenterology | Dispepsia funcional (no ulcerosa); tema relacionado. |
| [7215380](https://pubmed.ncbi.nlm.nih.gov/7215380/) | 1981 | Estudio retrospectivo | European Journal of Nuclear Medicine | Vaciamiento gástrico retardado que respondió a metoclopramida en gastroenteropatía diabética; sin respuesta en obstrucción de salida gástrica. |
| [7017896](https://pubmed.ncbi.nlm.nih.gov/7017896/) | 1981 | Revisión | Scand J Gastroenterol Suppl | Implicaciones terapéuticas del reflujo duodenogástrico. |

## Información de Mercado en Argentina

Se listan 5 de las 19 autorizaciones vigentes (todas de productos con un único principio activo).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 2217 | RELIVERAN | Gotas pediátricas, 20 ml | No registrada |
| 48614 | RILAQUIN SL | Comprimidos sublinguales 10 mg x 10 | No registrada |
| 2219 | RELIVERAN | Gotas para adultos, 20 ml | No registrada |
| 21308 | RILAQUIN | Comprimidos 10 mg x 20 | No registrada |
| 2220 | RELIVERAN | Gotas para adultos, 60 ml | No registrada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay estudios que evalúen directamente la metoclopramida en el tratamiento de la úlcera gástrica; el único ensayo evalúa la visualización endoscópica en hemorragia digestiva alta, y los datos preclínicos apuntan en sentido contrario. El fármaco no tiene acción antisecretora ni de protección de la mucosa, por lo que el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Resultados publicados del ensayo NCT05746377 y estudios que evalúen la cicatrización de la úlcera como criterio principal.
- Datos del mecanismo de acción verificados en fuentes farmacológicas.
- Información de seguridad del prospecto (advertencias y contraindicaciones) de ANMAT.
- Aclarar el riesgo señalado por los datos preclínicos de lesión gástrica antes de cualquier planteamiento clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

