---
layout: default
title: Desloratadina
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 4
drugbank_id: DB00967
monitor_inn: "Desloratadine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
last_modified_at: 2026-11-16
description: "Desloratadina: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Desloratadina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Desloratadina: Nasal cavity disease
{: .text-alpha }

## Resumen en Una Frase

Desloratadina es un antihistamínico de segunda generación, antagonista selectivo de los receptores H1 periféricos, comercializado en Argentina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Nasal cavity disease |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción de forma detallada. Según la información conocida, desloratadina es un agonista inverso selectivo del receptor H1 periférico, es decir, bloquea la acción de la histamina liberada por los mastocitos.

La urticaria por frío es una urticaria física mediada por mastocitos e histamina: el frío desencadena la liberación de histamina, que produce ronchas y picazón. Bloquear el receptor H1 reduce directamente estos síntomas, por lo que el mecanismo es biológicamente coherente.

Además, las guías recomiendan aumentar la dosis de antihistamínicos de segunda generación (hasta 4 veces la estándar) en pacientes con urticaria por frío que no responden a la dosis habitual, lo que respalda el uso de desloratadina en esta enfermedad.

**Nota sobre el nivel de evidencia:** los ensayos registrados son de Fase 4 (no Fase 3), aunque son aleatorizados, comparan dosis y/o usan placebo, y estudian directamente la enfermedad. Se asigna L1 por la solidez y relevancia directa de la evidencia; estrictamente según la definición basada en fases, podría clasificarse como L2.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Fase 4 | Completado | 30 | Estudio multicéntrico, doble ciego, con escalada de dosis (5, 10 y 20 mg) en urticaria por frío adquirida; busca la dosis suficiente para inhibir los síntomas |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Fase 4 | Completado | 33 | Estudio cruzado, aleatorizado, doble ciego y controlado con placebo; compara 5 mg vs. 20 mg en lesiones de urticaria inducidas experimentalmente |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECA | J Allergy Clin Immunol | Estudio aleatorizado, controlado con placebo y cruzado: la dosis alta de desloratadina reduce el volumen de las ronchas y mejora los umbrales de provocación por frío frente a la dosis estándar |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECA | Br J Dermatol | Ensayo aleatorizado de escalada de dosis de antihistamínicos H1, con medición del umbral crítico de temperatura en urticaria por frío |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | ECA | J Dermatol Treat | Desloratadina 5 mg durante 4 días, probada con cubos de hielo antes y después del tratamiento en 12 pacientes con urticaria por frío |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisión | Drugs | Revisión sobre etiología, manejo y opciones de tratamiento de la urticaria crónica |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revisión | Allergy | Revisión de ebastina (otro antihistamínico) en rinitis alérgica y urticaria crónica idiopática; relevancia indirecta |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Reporte de caso | Qatar Med J | Primer caso de urticaria por frío tras anafilaxia por picadura de hormiga negra |

## Información de Mercado en Argentina

El medicamento está comercializado en Argentina. Se registran al menos 20 autorizaciones vigentes (la lista puede ser parcial). Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52847 | TERALMINA | 5 mg comprimidos recubiertos x 7 | — |
| 35738 | HEXALER | Jarabe x 60 ml | — |
| 37706 | NOVO ALERPRIV | 5 mg comprimidos recubiertos x 20 | — |
| 32833 | FRENALER | 5 mg comprimidos recubiertos x 7 | — |
| 31797 | AERIUS | Jarabe x 60 ml | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Dos ensayos de Fase 4 completados y tres ECA publicados estudian directamente desloratadina en urticaria por frío, con resultados coherentes con el mecanismo H1. Sin embargo, las muestras son pequeñas y no hay datos locales de seguridad.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones del prospecto aprobado por ANMAT.
- Completar los datos de mecanismo de acción.
- Definir y justificar la pauta de dosis elevada (superior a la ficha técnica) y su monitoreo de seguridad.
- Confirmar la indicación aprobada localmente para delimitar el uso fuera de prospecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

