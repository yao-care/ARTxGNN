---
layout: default
title: Amiodarona
parent: Solo Predicción del Modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
drugbank_id: DB01118
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-11-16
description: "Amiodarona: nueva indicación predicha, taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia) (nivel de evidencia L5)."
---

# Amiodarona
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

## Amiodarona: taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia)
{: .text-alpha }

## Resumen en Una Frase

Amiodarona es un antiarrítmico de clase III que bloquea múltiples canales iónicos y tiene efecto antagonista beta-adrenérgico.
El modelo TxGNN predice que podría ser efectivo para **taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia)**,
pero actualmente no hay ensayos clínicos registrados y la literatura recopilada (9 publicaciones) consiste en reportes de caso, cohortes y revisiones en los que la amiodarona aparece solo como fármaco de rescate o comparador, sin evidencia directa de eficacia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | taquicardia ventricular polimórfica catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia) |
| Puntaje de Predicción TxGNN | 0.9978 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la amiodarona bloquea canales de potasio, sodio y calcio y tiene antagonismo beta-adrenérgico, lo que en principio podría suprimir arritmias ventriculares desencadenadas por catecolaminas.

Sin embargo, esta taquicardia surge de una fuga diastólica de calcio mediada por RYR2/CASQ2, y el tratamiento de referencia son los betabloqueantes junto con flecainida. La plausibilidad mecanística es por lo tanto limitada y el puntaje elevado (0,9978) no está respaldado por datos clínicos.

Aunque algunas publicaciones sobre otras arritmias ventriculares pediátricas describen uso de amiodarona, ninguna estudia directamente esta enfermedad con amiodarona como tratamiento. Por ello el nivel de evidencia se fija en L5, pese a que la clasificación interna previa sugería L4.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revisión sistemática | Life (Basel) | Características clínicas, genética y desenlaces arrítmicos de pacientes con esta enfermedad en China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte | Reviews in Cardiovascular Medicine | Características clínicas, base genética y costos sanitarios en una ciudad china |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revisión | Expert Opinion on Pharmacotherapy | Avances en el tratamiento farmacológico de arritmias ventriculares |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Reporte de caso | Frontiers in Cardiovascular Medicine | Resolución con denervación simpática cardíaca derecha tras la izquierda en un adolescente |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Reporte de caso | PACE | Flecainida suprime las tormentas inducidas por el desfibrilador en un niño de 14 años |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Reporte de caso | Medicine | Diagnóstico retrasado seis años en un niño de 9 años con mutación de RYR2 |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Reporte de caso | Turk Pediatri Arşivi | Paro cardíaco súbito en un niño de 2 años |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Reporte de caso | BMJ Case Reports | Supervivencia de un niño con paro extrahospitalario y taquicardia/fibrilación ventricular recurrente |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Reporte de caso | Anesthesia & Analgesia | Neonato con síndrome de QT largo y arritmias refractarias tratado con lidocaína, esmolol y amiodarona |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 7639 | ATLANSIL | comp. x 50 | — |
| 37428 | MIODARONA | 200 mg comp. x 40 | — |
| 37427 | MIODARONA | 200 mg comp. x 20 | — |
| 7638 | ATLANSIL | comp. x 20 | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación que estudie directamente la amiodarona en esta enfermedad, y el tratamiento de referencia (betabloqueantes y flecainida) está bien establecido. El puntaje del modelo no se corresponde con datos clínicos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y comparación mecanística con las terapias actuales
- Estudios que evalúen directamente la amiodarona en esta enfermedad
- Información de seguridad del prospecto (advertencias y contraindicaciones) para el análisis de seguridad inicial

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «No se identificaron autorizaciones de comercialización vigentes (0 licencias)» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

