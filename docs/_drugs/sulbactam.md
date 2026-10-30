---
layout: default
title: Sulbactam
parent: Solo Predicción del Modelo (L5)
nav_order: 230
evidence_level: L5
indication_count: 1
monitor_inn: "SULBACTAM"
predicted_indications: ["bacterial arthritis"]
last_modified_at: 2026-10-30
description: "Sulbactam: nueva indicación predicha, artritis bacteriana (bacterial arthritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Sulbactam
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

## Sulbactam: inhibidor de beta-lactamasas → artritis bacteriana (bacterial arthritis)
{: .text-alpha }

## Resumen en Una Frase

Sulbactam es un inhibidor irreversible de beta-lactamasas que se usa junto con aminopenicilinas como la ampicilina.
El modelo TxGNN predice que podría ser útil para **artritis bacteriana (bacterial arthritis)**,
pero los datos compilados para este informe no incluyen ensayos clínicos registrados y la literatura es mayormente de apoyo indirecto: **20 publicaciones**, entre ellas estudios antiguos de la combinación ampicilina/sulbactam en infecciones óseas y articulares.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | artritis bacteriana (bacterial arthritis) |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (9 de 9) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción original del fármaco. Según la farmacología conocida, sulbactam es un inhibidor irreversible de beta-lactamasas con actividad intrínseca contra *Acinetobacter* spp. Combinado con ampicilina, amplía la cobertura a *Staphylococcus aureus* y *Escherichia coli* productores de beta-lactamasas y a bacterias anaerobias.

Estos microorganismos son patógenos frecuentes en infecciones óseas y articulares, lo que hace plausible un papel antibacteriano en la artritis séptica. El puntaje alto del modelo es coherente con esa superposición mecanística, pero es una predicción del modelo y no constituye evidencia clínica.

Cabe señalar que los estudios disponibles evalúan sobre todo la combinación ampicilina/sulbactam y no sulbactam como único principio activo. Además, ningún estudio citado se centra de forma directa y específica en la artritis bacteriana como objetivo principal: los trabajos que la tocan son series pequeñas de infecciones esqueléticas y de tejidos blandos en general, o reportes de caso. Por ello el nivel de evidencia se fija en L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | ECA | Pediatr Infect Dis J | Ampicilina/sulbactam vs. ceftriaxona en 105 niños con infecciones de tejidos blandos, artritis supurada (11) y osteomielitis (9) |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión | Int J Antimicrob Agents | Uso fuera de indicación vs. recomendaciones formales de antibióticos en infecciones por bacterias multirresistentes |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Cohorte | Rev Infect Dis | Tratamiento secuencial con sulbactam/ampicilina parenteral y sultamicilina oral en 9 niños con osteomielitis o artritis séptica; patógenos sensibles a la combinación |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | Estudio comparativo abierto | Rev Infect Dis | Sulbactam + ampicilina vs. cefotaxima en infecciones graves de tejidos blandos, óseas y articulares (22 pacientes) |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Ensayo clínico | Mikrobiyol Bul | Ampicilina y sulbactam parenterales en 84 pacientes con diversas infecciones, incluidos 5 con artritis séptica u osteomielitis |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | Comparación in vitro y revisión | Pharmacotherapy | Actividad in vitro y eficacia clínica de ampicilina-sulbactam frente a ticarcilina-clavulánico |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Reporte de caso | J Rheumatol | Artritis por *Pasteurella multocida* tras mordedura de gato, resuelta con ampicilina/sulbactam |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños pequeños |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 26362 | TRIFAMOX IBL DUO 200/50 | Suspensión 20 g x 60 ml | No registrada en los datos locales |
| 1074 | TRIFAMOX IBL | Jarabe 500 mg x 60 ml | No registrada en los datos locales |
| 26356 | TRIFAMOX IBL DUO 875/125 | Comprimidos 875 mg x 14 | No registrada en los datos locales |
| 3635 | TRIFAMOX IBL 1500 | Inyectable 1500 mg x 1 | No registrada en los datos locales |
| 10002 | TRIFAMOX IBL 500 | Comprimidos 500 mg x 16 | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución registradas en los datos compilados** (no provienen del texto del prospecto): enfermedad renal, piouréter, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (0.9979) y la farmacología es coherente con los patógenos habituales de la artritis séptica. Sin embargo, no hay ensayos clínicos registrados, ningún estudio citado evalúa directamente la artritis bacteriana como objetivo principal, y la evidencia existente es antigua y trata de la combinación con ampicilina.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente la artritis bacteriana (séptica) con sulbactam o con ampicilina/sulbactam.
- Datos del mecanismo de acción original y de las advertencias y contraindicaciones del prospecto de ANMAT.
- Revisión de las interacciones farmacológicas (la consulta no devolvió resultados).
- Confirmación de la compatibilidad de vías y formas farmacéuticas con el uso propuesto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

