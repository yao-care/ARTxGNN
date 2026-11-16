---
layout: default
title: Ampicilina
parent: Solo Predicción del Modelo (L5)
nav_order: 32
evidence_level: L5
indication_count: 9
drugbank_id: DB00415
monitor_inn: "Ampicillin"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
last_modified_at: 2026-11-16
description: "Ampicilina: nueva indicación predicha, laringitis (laryngitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ampicilina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ampicilina: laringitis (laryngitis)
{: .text-alpha }

## Resumen en Una Frase

Ampicilina es un antibiótico betalactámico de uso antibacteriano, comercializado en Argentina en varias presentaciones.
El modelo TxGNN predice que podría ser útil para **laringitis (laryngitis)**, pero no hay ensayos clínicos registrados y la literatura recuperada trata sobre entidades relacionadas pero distintas (epiglotitis, crup, infecciones profundas del cuello), por lo que la evidencia directa es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | laringitis (laryngitis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (13 de 13) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 13 (vigentes: 13) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento general, la ampicilina es un betalactámico que inhibe la síntesis de la pared celular bacteriana y es activa contra bacterias sensibles como *Haemophilus influenzae* tipo b, causa de epiglotitis e infecciones supraglóticas.

El vínculo con la laringitis es indirecto. La mayoría de las laringitis son virales, por lo que un antibiótico solo tendría un papel en un subconjunto bacteriano. La literatura recuperada se centra en epiglotitis (donde la ampicilina aparece como parte del tratamiento en series de casos antiguas), crup y abscesos del cuello, que son enfermedades relacionadas pero diferentes.

Además, la resistencia a ampicilina en *H. influenzae* (18,7 % de los casos en una serie de 1977) limita su uso como agente único.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ningún estudio recuperado evalúa directamente la laringitis. Se listan los más cercanos (epiglotitis y entidades relacionadas):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Serie de casos/Revisión | West J Med | 9 adultos con epiglotitis aguda; 4 requirieron intubación; en 6 el diagnóstico inicial fue incorrecto |
| [7010270](https://pubmed.ncbi.nlm.nih.gov/7010270/) | 1980 | Revisión | Otolaryngol Head Neck Surg | 53 niños con epiglotitis, mayormente por *H. influenzae* b; resistencia a ampicilina del 18,7 % en 1977 |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Revisión | Anaesth Intensive Care | 161 niños con epiglotitis; 45 complicaciones y 5 muertes; énfasis en el manejo de la vía aérea |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | Cohorte | Anesth Analg | 23 niños con epiglotitis tratados con ampicilina o cloranfenicol; duración de intubación y fiebre |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Revisión | Rev Infect Dis | Sulbactam/ampicilina en epiglotitis pediátrica ante cepas de Hib productoras de betalactamasa |
| [7045555](https://pubmed.ncbi.nlm.nih.gov/7045555/) | 1982 | Reporte de caso | Laryngoscope | Epiglotitis por *Klebsiella* en un adulto que no respondió a ampicilina |
| [6969397](https://pubmed.ncbi.nlm.nih.gov/6969397/) | 1980 | Reporte de caso | Postgrad Med J | Epiglotitis por *H. influenzae* en un adulto, tratada con ampicilina e hidrocortisona |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Cohorte | Eur Arch Otorhinolaryngol | Microbiología y selección de antibióticos en abscesos de cuello en pacientes con diabetes |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 999 | AMPICILINA RICHET | 1 g comp. x 16 | No registrada |
| 928 | AMPICILINA RICHET | 1 g comp. x 8 | No registrada |
| 1039 | TRIFACILINA FORTE | jarabe x 120 ml | No registrada |
| 7153 | AMPICILINA RICHET | 500 mg comp. x 16 | No registrada |
| 1044 | TRIFACILINA | 1000 mg iny. liof. x 1 + solvente | No registrada |

Existen 13 autorizaciones en total, todas vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado evalúa directamente la laringitis y no hay ensayos clínicos, por lo que el nivel de evidencia es L5. La mayoría de las laringitis son virales y la literatura disponible corresponde a epiglotitis y otras infecciones, con resistencia documentada a ampicilina.

**Para avanzar se necesita:**
- Estudios que evalúen directamente la laringitis bacteriana y definan el subgrupo que podría beneficiarse
- Datos del mecanismo de acción y del perfil de resistencia local
- Información de seguridad del prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Revisión de las indicaciones registradas en los prospectos locales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

