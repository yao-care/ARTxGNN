---
layout: default
title: Podofilox
parent: Solo Predicción del Modelo (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Podofilox: nueva indicación predicha, Candidiasis vulvovaginal (nivel de evidencia L5). Indicación original: Infección anogenital por VPH (verrugas anogenitales) y verruga común"
monitor_inn: "PODOFILOX"
predicted_indications: ["vulvovaginal candidiasis", "photosensitivity disease", "herpes zoster", "benign neoplasm of tongue", "benign neoplasm of hypopharynx", "cystic neoplasm", "mesenchymoma", "nasal cavity inverting papilloma", "tumor of testis and paratestis"]
---

# Podofilox
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Podofilox: De Verrugas Anogenitales a Candidiasis Vulvovaginal
{: .text-alpha }

## Resumen en Una Frase

Podofilox es un agente antimitótico de uso tópico, originalmente utilizado para tratar las verrugas anogenitales causadas por el virus del papiloma humano (VPH) y la verruga común.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**, pero **no hay ensayos clínicos** y solo hay **1 publicación** (una revisión general de 1999) que no aporta evidencia específica para esta nueva indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección anogenital por VPH (verrugas anogenitales) y verruga común (según el grafo de conocimiento de TxGNN; el registro local no especifica el texto de indicación) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.47% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Podofilox es un antimitótico que inhibe la polimerización de la tubulina y detiene la división celular en el epitelio de proliferación rápida infectado por VPH, lo que produce necrosis del tejido de la verruga. No se dispone de datos detallados adicionales sobre su mecanismo de acción en la base de datos consultada.

**En este caso, la predicción no resulta razonable desde el punto de vista mecanístico.** La candidiasis es una infección fúngica y la inhibición de la tubulina por podofilox no tiene un papel antifúngico establecido. La única publicación asociada es una revisión general de 1999 sobre el tratamiento de infecciones de transmisión sexual, que trata juntas las infecciones vaginales y las verrugas genitales. Es probable que refleje una coincidencia temática y no evidencia a favor de podofilox en la candidiasis.

El puntaje alto de TxGNN probablemente se deba al contexto compartido de enfermedades del tracto genital (verrugas genitales y candidiasis vulvovaginal) y no a una relación terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Revisión | American Family Physician | Resume las guías de los CDC de 1998 para el tratamiento de infecciones de transmisión sexual (infecciones vaginales, enfermedad inflamatoria pélvica, verrugas genitales). No aporta evidencia específica del uso de podofilox en candidiasis. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 18640 | PODOXIN (Cassarß) | Solución tópica x 3.5 ml | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para candidiasis vulvovaginal se basa solo en el modelo, sin ensayos clínicos y sin vínculo mecanístico creíble. La única publicación es una revisión general que no respalda esta indicación.

*Nota:* entre las otras predicciones del modelo, la infección por VPH (puntaje 99.20%) tiene respaldo de ensayos publicados (por ejemplo, PMID 2186623, 8192173 y 9449907). Sin embargo, coincide con la indicación ya conocida del fármaco y por tanto no constituye un reposicionamiento real.

**Para avanzar se necesita:**
- Evidencia experimental de actividad antifúngica de podofilox frente a *Candida* (estudios *in vitro* o preclínicos).
- Datos del mecanismo de acción que justifiquen un vínculo con la candidiasis.
- Evaluación de la tolerabilidad en mucosa vulvovaginal, dado que podofilox es un irritante local.
- Obtención del prospecto de ANMAT para completar la información de advertencias y contraindicaciones.
- Evaluación de compatibilidad de la vía y la forma farmacéutica (solución tópica) con el uso propuesto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

