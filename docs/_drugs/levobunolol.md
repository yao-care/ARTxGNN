---
layout: default
title: Levobunolol
parent: Solo Predicción del Modelo (L5)
nav_order: 176
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Levobunolol: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: Glaucoma de ángulo abierto e hipertensión ocular"
---

# Levobunolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Levobunolol: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Levobunolol es un betabloqueante no selectivo de uso oftálmico, utilizado originalmente para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**, con un puntaje muy alto (99,98%), pero **sin ensayos clínicos ni publicaciones** vinculados a esta indicación específica; la predicción se apoya solo en la cercanía con las indicaciones ya aprobadas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (según el grafo de conocimiento; el texto de indicación de la licencia local está vacío) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según el conocimiento general de la clase, levobunolol es un betabloqueante no selectivo que reduce la producción de humor acuoso en el cuerpo ciliar y, con ello, la presión intraocular (PIO). Su eficacia en el glaucoma de ángulo abierto y la hipertensión ocular está bien documentada.

La relación entre la indicación original y la nueva es de proximidad: ambas son formas de glaucoma en las que la PIO elevada es un factor central. Esto explica el puntaje alto del modelo, que probablemente refleja la cercanía en la red de conocimiento con las indicaciones aprobadas.

Sin embargo, hay reservas importantes. El glaucoma hereditario primario (por ejemplo, las formas congénita o juvenil) suele implicar anomalías del desarrollo del ángulo y se maneja habitualmente con cirugía. Además, el uso pediátrico de betabloqueantes tópicos conlleva preocupaciones de seguridad sistémica (bradicardia, broncoespasmo). Por ello, la aplicabilidad mecanística es plausible, pero no está respaldada por datos específicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el glaucoma hereditario primario.

*Nota:* para las indicaciones ya aprobadas (glaucoma de ángulo abierto), sí existe literatura abundante, que se resume a continuación como contexto. Se trata de un uso dentro de la indicación aprobada, no de un reposicionamiento propiamente dicho.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Revisión sistemática / Metaanálisis en red | Ophthalmology | Eficacia comparativa de los tratamientos de primera línea en glaucoma primario de ángulo abierto e hipertensión ocular |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | Estudio clínico aleatorizado, doble ciego (4 años) | Ophthalmology | 391 pacientes; descenso de PIO de ~7 mmHg con levobunolol 0,5% y 1%, similar a timolol 0,5%, con poca atenuación del efecto |
| [2865710](https://pubmed.ncbi.nlm.nih.gov/2865710/) | 1985 | Estudio clínico doble ciego | Ophthalmology | Levobunolol redujo la PIO media un 27% durante dos años, de forma sostenida, frente a timolol |
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | Estudio clínico comparativo | Am J Ophthalmol | 162 pacientes; reducción de PIO de ~8 mmHg, sin diferencias significativas con timolol |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Revisión | Drugs | Revisión farmacodinámica y farmacocinética; reducción de la PIO de ~30%, superior a placebo y comparable a otros betabloqueantes |
| [8123096](https://pubmed.ncbi.nlm.nih.gov/8123096/) | 1993 | Estudio clínico comparativo | J Ocul Pharmacol | Levobunolol frente a dipivefrina en 38 pacientes afroamericanos con glaucoma de ángulo abierto |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Revisión | Ann Pharmacother | Comparación de betabloqueantes oculares: efectos adversos sistémicos, tolerabilidad local y costo |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Revisión | Med Lett Drugs Ther | Revisión de fármacos para el glaucoma de ángulo abierto |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19724 | BETAGAN LIQUIFILM (Abbvie) | Solución 0,50% x 5 ml | No consta el texto de indicación en los datos compilados |

---

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación (según el grafo de conocimiento, no el prospecto):** asma (incluidos asma intrínseco y alérgico), diabetes mellitus, cetoacidosis diabética, miastenia gravis y enfermedades de la unión neuromuscular, bloqueo auriculoventricular, enfisema pulmonar y anafilaxia.
- **Interacciones farmacológicas:** se registraron 24 interacciones, todas con nivel de gravedad no clasificado. Entre las listadas figuran lansoprazol, pantoprazol, omeprazol, prednisona, triamcinolona, warfarina, clopidogrel, ibuprofeno, metronidazol y tacrolimus.
- **Uso pediátrico:** los betabloqueantes tópicos pueden causar efectos sistémicos (bradicardia, broncoespasmo), lo cual es especialmente relevante en formas hereditarias o congénitas de glaucoma.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- Pese al puntaje muy alto de TxGNN (99,98%), no existen ensayos clínicos ni literatura para el glaucoma hereditario primario (nivel L5), y esta forma se maneja típicamente con cirugía, con preocupaciones de seguridad en población pediátrica.
- Cabe señalar que las otras predicciones del modelo (glaucoma de ángulo abierto, incluida la forma genética GLC1) corresponden en esencia a la indicación ya aprobada, con evidencia de nivel L3 (conservador) y recomendación de *Proceed with Guardrails*; no constituyen reposicionamiento nuevo.

**Para avanzar se necesita:**
- Revisión bibliográfica específica sobre betabloqueantes tópicos en glaucoma hereditario/congénito/juvenil.
- Datos detallados del mecanismo de acción del fármaco.
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones) y el texto de la indicación aprobada.
- Evaluación de seguridad en poblaciones específicas, en particular pediátricas, y de las contraindicaciones respiratorias y cardiovasculares.
- Verificar el diseño y la fase de los estudios publicados mediante revisión de texto completo, lo que podría elevar el nivel de evidencia en las indicaciones ya aprobadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

