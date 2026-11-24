---
layout: default
title: Cefazolina
parent: Solo Predicción del Modelo (L5)
nav_order: 88
evidence_level: L5
indication_count: 8
drugbank_id: DB01327
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-11-24
description: "Cefazolina: nueva indicación predicha, Otitis media infecciosa (infectious otitis media) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 2 (en el listado vigente: 2)"
---

# Cefazolina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefazolina: Otitis media infecciosa (infectious otitis media)
{: .text-alpha }

## Resumen en Una Frase

Cefazolina es un antibiótico betalactámico inyectable de la familia de las cefalosporinas de primera generación.
El modelo TxGNN predice que podría ser útil para **Otitis media infecciosa (infectious otitis media)**, con un puntaje de 0,9944.
Hasta ahora no hay **ensayos clínicos** registrados y solo hay **2 publicaciones**, que no estudian directamente esta enfermedad, por lo que la predicción carece de respaldo empírico directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Otitis media infecciosa (infectious otitis media) |
| Puntaje de Predicción TxGNN | 0.9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción. Según el conocimiento farmacológico general, la cefazolina inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina, lo que produce un efecto bactericida.

Ese mecanismo es plausible frente a bacterias grampositivas como *Staphylococcus aureus* y los estreptococos, que pueden participar en la otitis media infecciosa. Como esta enfermedad es de origen bacteriano, la lógica del modelo tiene cierto sentido biológico.

Sin embargo, hay limitaciones importantes:
- La cefazolina tiene actividad limitada frente a *Haemophilus influenzae* y *Moraxella catarrhalis*, que son patógenos clave en la otitis media.
- Se administra solo por vía parenteral, lo que reduce su practicidad para una infección de manejo habitualmente ambulatorio.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Reporte de caso | Ann Otol Rhinol Laryngol | Terapia empírica combinada de ceftazidima y cefazolina en síndrome de Gradenigo pediátrico, una complicación de la otitis media. No es posible aislar la contribución de la cefazolina. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clin Pharm | Manejo del síndrome de Stevens-Johnson. No aporta información sobre la eficacia de la cefazolina en otitis media. |

Ninguna de estas publicaciones evalúa directamente la eficacia de la cefazolina en la otitis media infecciosa.

---

## Información de Mercado en Argentina

El fármaco se encuentra comercializado en Argentina, con autorizaciones vigentes.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 7171 | CEFAZOLINA RICHET | 1000 mg iny.f.a.x 1 | Richet | Vigente |
| 911 | CEFALOMICINA | 1000 mg iny.liof.f.a.x 1 | Bagó | Vigente |

La tabla muestra los 2 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa casi exclusivamente en el modelo: no hay ensayos clínicos y las dos publicaciones disponibles no estudian directamente la enfermedad (un reporte de caso con terapia combinada y una revisión no relacionada con la eficacia). Además, el espectro de la cefazolina no cubre bien los patógenos principales de la otitis media y solo existe en presentación inyectable. Por eso el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios clínicos o comparativos que evalúen directamente la cefazolina en otitis media infecciosa
- Datos de sensibilidad de los patógenos locales frente a la cefazolina
- Datos detallados del mecanismo de acción
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Análisis de compatibilidad de la vía de administración con el escenario clínico de uso
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

