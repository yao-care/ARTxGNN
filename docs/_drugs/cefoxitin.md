---
layout: default
title: Cefoxitin
parent: Solo Predicción del Modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefoxitin: nueva indicación predicha, Otitis media infecciosa (nivel de evidencia L5). Indicación original: Infecciones bacterianas (neumonía bacteriana, peritonitis…"
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "urinary tract infection (disease)", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
---

# Cefoxitin
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

# Cefoxitina: De Infecciones Bacterianas a Otitis Media Infecciosa

## Resumen en Una Frase

Cefoxitina es una cefamicina de segunda generación, originalmente utilizada para tratar infecciones bacterianas como neumonía, peritonitis, gonorrea e infecciones por estafilococos, estreptococos y *Escherichia coli*.
El modelo TxGNN predice que podría ser efectiva para **otitis media infecciosa**, pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** (una revisión general sobre MRSA, sin datos clínicos de cefoxitina en esta indicación).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (neumonía bacteriana, peritonitis, infecciones por estafilococos y estreptococos, gonorrea, entre otras; el texto de indicación aprobado en ANMAT no está disponible) |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 99.30% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, cefoxitina es una cefamicina con actividad contra muchas bacterias Gram positivas, Gram negativas y anaerobias, y su eficacia en infecciones bacterianas ha sido comprobada. Mecanísticamente, podría ser aplicable a patógenos que causan otitis media.

Sin embargo, la relación es débil. La única publicación recuperada es una revisión general sobre *Staphylococcus aureus* resistente a meticilina (MRSA) desde la perspectiva "One Health". En la práctica, la cefoxitina se usa habitualmente como marcador de laboratorio de resistencia a meticilina, no como tratamiento. No hay evidencia clínica para esta indicación.

Por ello, la predicción del modelo debe considerarse una hipótesis basada en la cercanía en el grafo de conocimiento, no un hallazgo respaldado por estudios.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revisión | Infection and Drug Resistance | Revisión sobre MRSA (epidemiología, factores de virulencia, resistencia y impacto zoonótico); menciona la otitis media entre las infecciones que puede causar, sin datos de tratamiento con cefoxitina |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17797 | CEFOXITINA RICHET | 1 g iny.f.a.+a.sol. (inyectable, frasco ampolla con ampolla de solvente) | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad renal, piouréter, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y colitis.
- **Interacciones farmacológicas**: se identificaron 35 interacciones. Las de nivel moderado incluyen:
  - Aminoglucósidos: kanamicina, neomicina y estreptomicina.
  - Ácido picosulfúrico.
  - Dicumarol.

  Entre las de nivel desconocido figuran morfina, omeprazol, lansoprazol, vancomicina, simvastatina, hidrocortisona, cloruro de potasio, ranitidina, ondansetrón, metronidazol, famotidina, claritromicina, metoclopramida y dexametasona. La heparina tiene una interacción de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para otitis media infecciosa se apoya solo en el puntaje del modelo y en una revisión general sin datos clínicos de cefoxitina. No hay ensayos clínicos y el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios clínicos o datos de susceptibilidad de los patógenos de otitis media a cefoxitina.
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada).
- Datos del mecanismo de acción desde DrugBank.
- Evaluar la compatibilidad de la vía de administración (la presentación local es inyectable).

---

**Nota sobre otras predicciones**

Entre las demás indicaciones predichas hay dos con más evidencia, aunque corresponden a usos establecidos o históricos más que a un reposicionamiento novedoso:

- **Infección del tracto urinario (L3, puntaje 99.26%):** un ensayo de Fase 4 (NCT02474706) fue terminado con solo 6 pacientes y no permite conclusiones de eficacia. Hay estudios clínicos antiguos (1978-1979) y un modelo murino con *E. coli* productor de BLEE.
- **Uretritis gonocócica (L3, puntaje 99.09%):** varios estudios de 1979-1983 muestran curación en uretritis gonocócica. La gonorrea ya figura entre las indicaciones originales y hoy existen alternativas mejores, como la ceftriaxona.

Las predicciones de uretritis por *Ureaplasma* (carece de pared celular) y toxocariasis (parásito) carecen de plausibilidad mecanística y probablemente sean artefactos del grafo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

