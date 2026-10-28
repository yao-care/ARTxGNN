---
layout: default
title: Febuxostat
parent: Evidencia Moderada (L3-L4)
nav_order: 141
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Febuxostat: nueva indicación predicha, Hipouricemia renal (nivel de evidencia L4). Indicación original: Hiperuricemia (según la base de conocimiento del modelo"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Febuxostat: De Hiperuricemia a Hipouricemia Renal
{: .text-alpha }

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa, utilizado originalmente para el tratamiento de la hiperuricemia.
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, pero la evidencia es muy limitada: **1 ensayo clínico** de relevancia baja y **2 publicaciones** (revisiones), sin estudios que demuestren eficacia directa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa que reduce la producción de ácido úrico, y su eficacia en la hiperuricemia está comprobada.

Sin embargo, la hipouricemia renal es una condición en la que el ácido úrico sérico ya es bajo por una reabsorción renal deficiente de urato (por ejemplo, pérdida de función de URAT1/SLC22A12 o GLUT9). Reducir aún más el urato es mecanísticamente contraintuitivo y no ofrece una justificación terapéutica para la enfermedad en sí.

El único vínculo plausible es indirecto: se ha planteado que los inhibidores de la xantina oxidorreductasa podrían ayudar a prevenir la lesión renal aguda inducida por ejercicio asociada a la hipouricemia renal (PMID 36754409), donde la sobrecarga de urato urinario sería el motor del daño. Es un concepto profiláctico, no un tratamiento de la hipouricemia. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una señal terapéutica real.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control del ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis e hiperuricemia. Relevancia baja: probablemente corresponde a hiperuricemia convencional y no a hipouricemia renal; requiere verificación manual. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) para el reumatólogo, con su etiología y abordaje. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Revisión (reporte de caso según el contenido) | Internal Medicine | Futbolista de 16 años con hipouricemia renal familiar (mutaciones en URAT1) y lesión renal aguda recurrente inducida por ejercicio; se plantea el uso de inhibidores de xantina oxidorreductasa no purínicos como profilaxis. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 47762 | DUTRINOL (Teva Argentina) | Comprimidos 80 mg x 30 | No disponible |
| 46249 | FEBUXTAT (Ariston) | Comprimidos recubiertos/ranurados 80 mg x 30 | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según la base de conocimiento del modelo (no es texto de prospecto)**: accidente cerebrovascular, trastornos cerebrovasculares, infarto cerebral, infarto de miocardio, trombosis coronaria y hemoglobinopatía.
- **Interacciones Farmacológicas** (22 registradas en total; se listan las de mayor gravedad):
  - **Mayores**: mercaptopurina, azatioprina, leflunomida, teriflunomida.
  - **Moderadas** (selección): teofilina, aminofilina, difilina, oxtrifilina, metotrexato, naltrexona, tioguanina, epirrubicina, clofarabina, trabectedina, asparaginasa, pegaspargasa, brentuximab vedotina, interferón beta-1a/1b y peginterferón beta-1a.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe una justificación mecanística directa para reducir aún más el ácido úrico en la hipouricemia renal, y la evidencia se limita a un ensayo de baja relevancia y a literatura de revisión/caso. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una señal terapéutica real.

**Para avanzar se necesita:**
- Verificar manualmente el ensayo NCT04398251 en ClinicalTrials.gov para confirmar su relación con la hipouricemia renal.
- Definir si la hipótesis útil es la profilaxis de la lesión renal aguda inducida por ejercicio (y no el tratamiento de la hipouricemia), con estudios clínicos específicos.
- Obtener los datos del mecanismo de acción y las advertencias/contraindicaciones del prospecto de ANMAT.
- Considerar que las otras dos indicaciones predichas (deficiencia parcial de HPRT y síndrome de Lesch-Nyhan) tienen un fundamento mecanístico más sólido para el control de la hiperuricemia, aunque con evidencia limitada a reportes de casos, y podrían priorizarse como preguntas de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

