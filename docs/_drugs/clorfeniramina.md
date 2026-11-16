---
layout: default
title: Clorfeniramina
parent: Solo Predicción del Modelo (L5)
nav_order: 121
evidence_level: L5
indication_count: 1
drugbank_id: DB01114
monitor_inn: "Chlorpheniramine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-16
description: "Clorfeniramina: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Clorfeniramina
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

## Clorfeniramina: Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Clorfeniramina es un antihistamínico de primera generación que actúa bloqueando los receptores H1 de histamina.
El modelo TxGNN predice que podría ser útil para **enfermedad de la cavidad nasal (nasal cavity disease)**, pero la evidencia disponible se limita a **8 publicaciones**, todas de estudios preclínicos o mecanísticos, y **ningún ensayo clínico** registrado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9953 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (14 de 14) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 14 (vigentes: 14) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción

Clorfeniramina es un antagonista de los receptores H1 de histamina de primera generación. La histamina provoca vasodilatación nasal, aumento de la permeabilidad vascular, edema de la mucosa, secreción glandular y estornudos. Por ello, el bloqueo H1 podría aliviar síntomas como rinorrea, estornudos y picazón. No se dispone de datos detallados del mecanismo de acción en los datos compilados para este informe; la descripción anterior corresponde a la farmacología conocida de la clase.

La literatura recuperada se refiere a modelos animales (perro, rata, gato) de rinitis alérgica y congestión nasal, donde los antihistamínicos H1 se usaron como herramientas farmacológicas, y a un estudio fisiológico sobre secreciones nasales inducidas por histamina. Un estudio en gato (PMID 10582118) sugiere que la descongestión nasal requeriría bloqueo combinado H1 y H3, por lo que el bloqueo H1 por sí solo podría aliviar solo parcialmente la congestión.

El puntaje de TxGNN (0,9953) es una predicción computacional y no constituye evidencia clínica. Ninguno de los estudios citados evalúa de forma directa clorfeniramina como tratamiento en pacientes con enfermedad de la cavidad nasal; por esa razón el nivel de evidencia se establece en L5. Además, la clorfeniramina es un fármaco ampliamente utilizado en cuadros respiratorios y alérgicos, de modo que esta predicción podría reflejar un uso ya establecido más que una indicación realmente nueva, algo que debe verificarse contra el prospecto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Modelo animal preclínico | Am J Rhinol | Modelo de congestión nasal alérgica en perros sensibilizados a ambrosía, medida con rinometría acústica |
| [1705288](https://pubmed.ncbi.nlm.nih.gov/1705288/) | 1990 | Modelo animal preclínico | J Pharmacobiodyn | Modelo de rinitis alérgica en rata Brown Norway y evaluación de fármacos antialérgicos |
| [10822083](https://pubmed.ncbi.nlm.nih.gov/10822083/) | 2000 | Modelo animal preclínico | Immunopharmacology | Nuevo modelo de rinitis alérgica en ratas y evaluación de antagonistas H1 |
| [2923378](https://pubmed.ncbi.nlm.nih.gov/2923378/) | 1989 | Estudio mecanístico/fisiológico | Am Rev Respir Dis | Origen de las proteínas en secreciones nasales inducidas por histamina en sujetos atópicos y no atópicos |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Modelo animal preclínico | J Pharmacol Toxicol Methods | Caracterización farmacológica de un modelo crónico de congestión nasal en perros |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | Modelo animal preclínico | Am J Rhinol | Cambios en resistencia y geometría nasal en un modelo felino de congestión nasal |
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | Modelo animal preclínico | Am J Rhinol | El bloqueo combinado H1 y H3 produjo descongestión nasal en el modelo felino |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Modelo animal preclínico | Am J Rhinol | Rinometría acústica en perros como modelo de congestión nasal |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 3525 | ALERGITRAT | Jarabe x 120 ml | No registrada en los datos locales |
| 3524 | ALERGITRAT | Comprimidos x 20 | No registrada en los datos locales |
| 8666 | DEXALERGIN | Comprimidos recubiertos x 20 | No registrada en los datos locales |
| 8670 | DEXALERGIN | Jarabe x 100 ml | No registrada en los datos locales |
| 8766 | ASEPTOBRON | Jarabe x 150 ml | No registrada en los datos locales |

Se muestran 5 de las 14 autorizaciones vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en modelos animales y estudios fisiológicos, sin ensayos clínicos que evalúen directamente la enfermedad de la cavidad nasal; por ello el nivel de evidencia es L5. El puntaje alto de TxGNN no sustituye la evidencia clínica.

**Para avanzar se necesita:**
- Verificar en los prospectos de ANMAT las indicaciones y la información de seguridad (advertencias y contraindicaciones), hoy ausentes en los datos locales
- Completar los datos del mecanismo de acción
- Buscar estudios clínicos en humanos que evalúen directamente clorfeniramina en enfermedades de la cavidad nasal
- Aclarar si la predicción representa una nueva indicación o un uso ya establecido
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

