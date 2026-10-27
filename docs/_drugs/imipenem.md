---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imipenem: nueva indicación predicha, Esclerodermia difusa (nivel de evidencia L5). Indicación original: Neumonía bacteriana (según el grafo de conocimiento"
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
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

## Imipenem: De Neumonía Bacteriana a Esclerodermia Difusa
{: .text-alpha }

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico de amplio espectro, originalmente utilizado para tratar infecciones bacterianas como neumonía bacteriana, peritonitis, endocarditis y endometritis.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa** (la predicción de mayor puntaje), pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.
Entre las predicciones con respaldo parcial destacan la infección por *Staphylococcus aureus* (2 ensayos clínicos y 19 publicaciones), la fiebre tifoidea y la salmonelosis (solo literatura indirecta).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumonía bacteriana (según el grafo de conocimiento; el texto de indicación aprobado en ANMAT no está disponible) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

> **Nota:** la esclerodermia difusa es la predicción de mayor puntaje, pero carece de toda evidencia. La candidata con respaldo más sólido es la **infección por *Staphylococcus aureus*** (nivel L3). Véase la sección de conclusión.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, imipenem es un carbapenémico que inhibe la síntesis de la pared celular bacteriana mediante la unión a proteínas fijadoras de penicilina, y su eficacia en infecciones bacterianas graves es conocida.

**Esclerodermia difusa (predicción principal):** no existe un mecanismo antibacteriano plausible que vincule imipenem con la esclerosis sistémica, una enfermedad autoinmune y fibrótica. El alto puntaje es una predicción computacional sin respaldo en ensayos ni literatura, por lo que debe interpretarse con mucha cautela.

**Predicciones con plausibilidad biológica:**
- **Fiebre paratifoidea, salmonelosis y fiebre tifoidea:** los carbapenémicos tienen actividad *in vitro* contra *Salmonella*, incluidas cepas resistentes a fluoroquinolonas y cefalosporinas, y se usan como opción de reserva en tifoidea extensamente resistente (XDR). La literatura consiste sobre todo en estudios de resistencia, sin ensayos clínicos con imipenem.
- **Infección por *S. aureus*:** imipenem actúa sobre *S. aureus* sensible a meticilina, pero por sí solo suele ser ineficaz frente a MRSA; los ensayos lo evalúan en combinación (fosfomicina o linezolid).
- **Sinusitis, rinosinusitis crónica y sinusitis etmoidal crónica:** el vínculo es débil e indirecto; los carbapenémicos no son tratamiento de primera línea.
- **Neoplasia de senos paranasales y síndrome de eosinofilia-mialgia:** sin mecanismo conocido; probablemente reflejan cercanía en el grafo de enfermedades.

---

## Evidencia de Ensayos Clínicos

Para la predicción principal (esclerodermia difusa) actualmente no hay ensayos clínicos relacionados registrados.

Para la predicción con más respaldo (infección por *S. aureus*):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Fase 4 | Completado | 50 | Fosfomicina más imipenem frente a vancomicina (tratamiento estándar) en endocarditis infecciosa por MRSA; muestra pequeña |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Desconocido | 60 | Linezolid solo o combinado con un carbapenémico contra MRSA en neumonía asociada a ventilador; el carbapenémico podría no ser imipenem |

---

## Evidencia de Literatura

Para la predicción principal (esclerodermia difusa) actualmente no hay literatura relacionada disponible.

A continuación, la literatura más relevante para la infección por *S. aureus* y la fiebre tifoidea:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Cohorte | Antimicrob Agents Chemother | Imipenem-cilastatina evaluado en 23 pacientes con infecciones por *S. aureus* (MSSA y MRSA) |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Modelo animal | J Antimicrob Chemother | Imipenem en endocarditis experimental por *S. aureus* y *S. faecalis*; alta actividad *in vitro* |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Reporte de caso | Antimicrob Agents Chemother | Comentario sobre imipenem/cilastatina más fosfomicina en infección refractaria por MRSA |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Revisión | Int J Antimicrob Agents | Patogénesis, tratamiento y resistencia de MRSA |
| [3890533](https://pubmed.ncbi.nlm.nih.gov/3890533/) | 1985 | Revisión | Am J Med | Patogénesis y tratamiento de la endocarditis; papel del imipenem en el modelo de conejo |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro/in vivo | J Antimicrob Chemother | Efecto sinérgico de vancomicina e imipenem contra MRSA en 34 de 36 aislados |
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Observacional | Cureus | Carbapenémicos como última línea de defensa en tifoidea MDR/XDR en Peshawar |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Reporte de caso | J Med Liban | Rabdomiólisis e infección por *Salmonella typhi* tratada con éxito con imipenem/cilastatina y hemodiálisis |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | In vitro | J Med Microbiol | CIM de carbapenémicos y tigeciclina frente a 210 aislados de *Salmonella* |
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | In vitro | JPMA | Susceptibilidad de *Salmonella* Typhi y Paratyphi a nuevos antimicrobianos, incluido imipenem |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38546 | IMIPENEM FABRA (Fabra) | 500 mg IV polvo para inyección x 1 | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas:** se identificaron 15 interacciones.
  - **Mayores:** bupropión, iohexol, iopamidol.
  - **Moderadas:** polietilenglicol (3350 con electrolitos), dicumarol, warfarina, lindano, aminofilina, dixifilina, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexed.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, ya que no se dispone de ellas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para la predicción principal, esclerodermia difusa)

**Justificación:**
- La esclerodermia difusa no tiene ensayos, literatura ni mecanismo plausible; el alto puntaje de TxGNN es solo una predicción computacional (L5).
- Entre las demás predicciones, la infección por *S. aureus* (L3) tiene el mejor respaldo, aunque limitado a combinaciones en MRSA. Fiebre tifoidea, paratifoidea y salmonelosis (L4) son líneas de investigación razonables basadas en datos de susceptibilidad *in vitro*. Sinusitis, rinosinusitis crónica, sinusitis etmoidal crónica, neoplasia de senos paranasales y síndrome de eosinofilia-mialgia se mantienen en espera.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas), actualmente sin datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Para *S. aureus*: revisar los resultados del ensayo NCT00871104 y evaluar si el beneficio de las combinaciones justifica un estudio de mayor tamaño.
- Para tifoidea y salmonelosis: generar evidencia clínica específica de imipenem (series de casos o estudios comparativos) en cepas XDR.
- Evaluar la seguridad en poblaciones con epilepsia o enfermedad renal y revisar las interacciones mayores.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

