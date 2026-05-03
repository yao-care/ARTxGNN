---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Imipenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando **txgnn-pipeline** para guiar la generación del informe de evaluación. Procedo a redactar el reporte completo en español a partir del Evidence Pack de IMIPENEM.

---

# IMIPENEM: De Infecciones Bacterianas Graves a Infección por Staphylococcus aureus

## Resumen en Una Frase

IMIPENEM es un antibiótico carbapenem de amplio espectro reconocido por su eficacia en el tratamiento de infecciones bacterianas graves causadas por patógenos gram-negativos y gram-positivos.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Staphylococcus aureus** — en particular como terapia de rescate para cepas resistentes a meticilina (MRSA) en combinación con fosfomicina —,
con **13 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

> **Nota clínica:** La predicción TxGNN de mayor puntaje (Rango 1: esclerodermia difusa, 99.99%) carece de cualquier respaldo biológico o clínico y es atribuible a un artefacto del grafo neuronal (*graph artifact*). La indicación con mayor evidencia real y relevancia clínica es la **Infección por Staphylococcus aureus** (Rango 9 por puntaje TxGNN, pero Nivel de Evidencia L2 con recomendación *Proceed with Guardrails*).

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Infecciones bacterianas graves por patógenos susceptibles (carbapenem de amplio espectro) |
| Nueva Indicación Predicha | Infección por Staphylococcus aureus (MRSA/MSSA) |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, IMIPENEM es un antibiótico carbapenem que inhibe la síntesis de la pared bacteriana mediante unión covalente a las proteínas fijadoras de penicilina (PBPs). Su espectro de actividad abarca bacterias gram-negativas y gram-positivas, incluyendo *Staphylococcus aureus*, contra el cual exhibe una potente actividad bactericida — con MBC90 de 0.06 mg/L, siendo cuatro a ocho veces más activo que nafcilina contra cepas MSSA (PMID 6421794).

Para las cepas resistentes a meticilina (MRSA), el uso de imipenem en monoterapia es limitado debido a la baja afinidad del fármaco por PBP2a, la proteína responsable de la resistencia. Sin embargo, la combinación imipenem/fosfomicina supera esta barrera mediante un doble bloqueo sinérgico de la biosíntesis de la pared celular. Esta estrategia fue validada directamente en el ensayo de Fase 4 NCT00871104 (fosfomicina + imipenem vs. vancomicina en endocarditis infecciosa por MRSA, n=50, completado) y en el estudio clínico multicéntrico de del Río et al. (PMID 25048851, 2014), que demostró su eficacia como terapia de rescate en bacteriemia complicada y endocarditis refractaria a vancomicina.

La predicción de TxGNN resulta mecanísticamente coherente dentro del espectro antibacteriano del fármaco: imipenem tiene actividad documentada contra *S. aureus* tanto en modelos experimentales como en series clínicas, y su aplicación en infecciones difíciles de tratar — especialmente MRSA en terapia de combinación — cuenta con evidencia de Fase 4 que la sustenta. La principal restricción práctica es que IMIPENEM no se encuentra actualmente comercializado en Argentina, lo que implica la necesidad de gestión regulatoria previa ante ANMAT.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|-----------------|------|--------|-------------|----------------------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Fase 4 | Completado | 50 | Fosfomicina + Imipenem vs. Vancomicina en endocarditis infecciosa por MRSA; ensayo de rescate más directamente relevante |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Fase 3 | Completado | 274 | IMI/Cilastatina/Relebactam (MK-7655A) vs. Piperacilina/Tazobactam en neumonía nosocomial y asociada a ventilador (HABP/VABP); mortalidad a 28 días como desenlace primario |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Desconocido | 60 | Linezolid solo o en combinación con carbapenem contra MRSA en neumonía asociada a ventilador (VAP); basado en sinergia in vitro/in vivo documentada |
| [NCT03012360](https://clinicaltrials.gov/study/NCT03012360) | Fase 4 | Terminado | 103 | Tratamiento antimicrobiano en traqueobronquitis asociada a ventilador; Imipenem como fármaco de tratamiento, terminado anticipadamente |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Fase 2 | Terminado | 108 | Tigeciclina vs. Imipenem/Cilastatina en neumonía nosocomial (VAP ≥70%); terminado anticipadamente, debilita las conclusiones |
| [NCT06743529](https://clinicaltrials.gov/study/NCT06743529) | N/A | Reclutando | 686 | RCT que evalúa inicio antibiótico inmediato vs. confirmado en VAP no grave; Imipenem como opción de amplio espectro |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [25048851](https://pubmed.ncbi.nlm.nih.gov/25048851/) | 2014 | Estudio clínico multicéntrico | Clin Infect Dis | Fosfomicina + Imipenem como terapia de rescate en bacteriemia complicada y endocarditis por MRSA; eficacia y seguridad demostradas en pacientes refractarios a vancomicina |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Estudio clínico retrospectivo | Antimicrob Agents Chemother | Imipenem-Cilastatina en 23 pacientes con infecciones por MSSA y MRSA; eficaz en infecciones de tejidos blandos, endovasculares y esqueléticas, incluyendo bacteriemia |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Modelo animal (endocarditis) | J Antimicrob Chemother | Imipenem muy activo in vitro contra 36 aislamientos de S. aureus (MBC90 = 0.06 mg/L); validado en modelo de endocarditis experimental en conejos vs. nafcilina |
| [23089756](https://pubmed.ncbi.nlm.nih.gov/23089756/) | 2013 | Modelo animal | Antimicrob Agents Chemother | Fosfomicina + Imipenem en infección de cuerpo extraño por MRSA; actividad comparable a daptomicina-rifampicina en modelo de jaula tisular |
| [20680368](https://pubmed.ncbi.nlm.nih.gov/20680368/) | 2010 | In Vitro / In Vivo | Eur J Clin Microbiol Infect Dis | Linezolid + Vancomicina + Imipenem evaluados contra S. aureus con susceptibilidad reducida a glucopéptidos; combinaciones con Imipenem muestran ventaja frente a monoterapias |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In Vitro / In Vivo | J Antimicrob Chemother | Vancomicina + Imipenem: efecto sinérgico o aditivo en 36/36 aislamientos de MRSA y reducción bacteriana significativa en modelo murino neutropénico |
| [15616274](https://pubmed.ncbi.nlm.nih.gov/15616274/) | 2005 | In Vitro / In Vivo | Antimicrob Agents Chemother | Linezolid + concentraciones subinhibitorias de Imipenem: efecto sinérgico contra MRSA, confirmado tanto in vitro como en modelo animal de peritonitis |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Reporte de caso | Antimicrob Agents Chemother | Imipenem/Cilastatina + Fosfomicina para infección refractaria por MRSA; comentario sobre la identificación individualizada de terapias de rescate |
| [11581241](https://pubmed.ncbi.nlm.nih.gov/11581241/) | 2001 | In Vitro | J Antimicrob Chemother | Roxitromicina + Imipenem: reducción significativa de células viables en biofilm de S. aureus in vivo (día 8, p<0.01), con infiltración de PMN documentada |
| [39548455](https://pubmed.ncbi.nlm.nih.gov/39548455/) | 2024 | In Vitro | Ann Clin Microbiol Antimicrob | Gentamicina + Imipenem + fucoidano contra biofilm dual S. aureus/A. baumannii en úlceras de pie diabético; actividad antibiofilm sinérgica documentada |

---

## Información de Mercado en Argentina

IMIPENEM no se encuentra actualmente comercializado en Argentina. No se registran autorizaciones de comercialización ante la ANMAT (total de autorizaciones: 0). Para su utilización en el país se requeriría tramitar el registro del producto ante la autoridad regulatoria competente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La combinación Imipenem/Fosfomicina ha sido validada en un ensayo de Fase 4 completado (NCT00871104) para endocarditis infecciosa por MRSA, y múltiples estudios clínicos retrospectivos, modelos animales y estudios in vitro respaldan su actividad frente a infecciones graves por *S. aureus* resistente. Sin embargo, la ausencia de registro comercial en Argentina es una limitación operativa crítica que debe resolverse antes de cualquier aplicación clínica local.

**Para avanzar se necesita:**
- Tramitar el registro de Imipenem/Cilastatina ante ANMAT para comercialización en Argentina
- Obtener datos formales de MOA, advertencias y contraindicaciones desde DrugBank y el prospecto autorizado (brechas DG001 y DG002 del Evidence Pack)
- Verificar disponibilidad de Fosfomicina IV en Argentina para sustentar la estrategia de combinación
- Diseñar protocolo de uso compasivo o investigación clínica para la combinación Imipenem/Fosfomicina en MRSA refractaria
- Establecer plan de monitoreo: función renal (creatinina, TFG), hemograma completo con diferencial y vigilancia de convulsiones en pacientes con SNC comprometido
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

