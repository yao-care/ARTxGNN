---
layout: default
title: Omeprazol
parent: Solo Predicción del Modelo (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
drugbank_id: DB00338
monitor_inn: "Omeprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-16
description: "Omeprazol: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 11 (en el listado vigente: 11)"
---

# Omeprazol
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

## Omeprazol: obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Omeprazol es un inhibidor de la bomba de protones que suprime la secreción de ácido gástrico.
El modelo TxGNN predice que podría ser útil para **obstrucción duodenal (duodenal obstruction)**, pero ningún estudio citado la evalúa directamente: hay **1 ensayo clínico** de relevancia baja y **5 publicaciones** (reportes de caso, revisiones y una serie pequeña) de apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0.9964 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (11 de 11) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 11 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Omeprazol es un inhibidor de la bomba de protones (IBP) que reduce la secreción de ácido gástrico. Actualmente no se dispone de datos detallados sobre su mecanismo de acción en los datos compilados para este informe; lo anterior corresponde al conocimiento general de la clase.

La obstrucción (estenosis) duodenal es con frecuencia una complicación de la enfermedad ulcerosa péptica. Suprimir el ácido podría disminuir la actividad de la úlcera, la inflamación y el edema que contribuyen a la obstrucción. Es un vínculo indirecto, basado en una enfermedad cercana y no en la obstrucción en sí.

Hay límites importantes: los IBP no resuelven una estenosis fibrótica fija, y no se esperaría respuesta en obstrucciones de origen estructural o maligno (por ejemplo, estenosis por enfermedad de Crohn). El puntaje alto (0,9964) es una predicción computacional y no sustituye la evidencia clínica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00557921](https://clinicaltrials.gov/study/NCT00557921) | Fase 3 | Terminado | 5000 | COGENT-1: clopidogrel + omeprazol frente a clopidogrel para reducir sangrado gastrointestinal y úlcera sintomática en pacientes con aspirina. No estudia obstrucción duodenal y fue terminado antes de tiempo; relevancia baja. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7795284](https://pubmed.ncbi.nlm.nih.gov/7795284/) | 1995 | Cohorte (caso clínico) | Ital J Gastroenterol | Adolescente con úlcera duodenal y estenosis del bulbo; 4 meses de omeprazol 40 mg no modificaron el cuadro, y la erradicación de *H. pylori* con triple terapia resolvió úlcera y estenosis. |
| [1475769](https://pubmed.ncbi.nlm.nih.gov/1475769/) | 1992 | Revisión | Ther Umsch | Diagnóstico de la úlcera péptica; menciona la obstrucción de salida gástrica y el papel de la endoscopia y los estudios contrastados. |
| [9005711](https://pubmed.ncbi.nlm.nih.gov/9005711/) | 1996 | Revisión (caso) | Acta Med Port | Enfermedad de Crohn gastroduodenal con obstrucción de salida gástrica; prednisolona y omeprazol fracasaron y se requirió cirugía. |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Reporte de caso | Surg Today | Crohn duodenal con obstrucción persistente de salida gástrica, resuelta con cirugía. |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Reporte de caso | Surg Endosc | Úlcera marginal gigante tras gastroenterostomía; la obstrucción es una de sus complicaciones. |

En conjunto, esta literatura no muestra beneficio de omeprazol en la obstrucción duodenal; en dos casos el omeprazol no resolvió el cuadro.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 53945 | ULCOZOL 20 | Polvo para suspensión oral x 30 sobres |
| 24356 | OMEPRAZOL RICHET | 40 mg IV, frasco ampolla x 1 |
| 46116 | DIOXAFLEX PROTECT | Cápsulas x 10 |
| 50468 | BLOKIUM PROTECT | Cápsulas x 30 |
| 52115 | BLOKIUM PROTECT | Cápsulas x 10 |

Se muestran 5 de las 11 autorizaciones vigentes (todas de producto de un solo principio activo).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado evalúa directamente la obstrucción duodenal: el único ensayo es de relevancia baja y fue terminado, y la literatura son casos aislados donde omeprazol no resolvió la obstrucción. El puntaje alto del modelo no basta por sí solo.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen omeprazol específicamente en obstrucción duodenal, distinguiendo causa péptica de causas fibróticas o malignas
- Datos de seguridad del prospecto de ANMAT (advertencias y contraindicaciones)
- Datos del mecanismo de acción para analizar mejor el vínculo mecanístico
- Texto de indicaciones aprobadas en los registros locales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

