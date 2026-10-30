---
layout: default
title: Quinidine
parent: Solo Predicción del Modelo (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Quinidine: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: Fibrilación auricular y malaria"
monitor_inn: "quinidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Quinidine
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

## Quinidina: De Fibrilación Auricular y Malaria a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Quinidina es un antiarrítmico de clase IA que se utiliza originalmente para el tratamiento de la fibrilación auricular y la malaria.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación auricular y malaria |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9927 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la quinidina es un antiarrítmico de clase IA (bloqueante de canales de sodio y potasio) con actividad antimalárica. Su eficacia en la fibrilación auricular y la malaria es conocida, pero no existe un vínculo mecanístico establecido con la nueva indicación.

El NSIAD se debe a mutaciones con ganancia de función en el gen del receptor 2 de la arginina vasopresina (AVPR2). Esto produce una activación constitutiva del receptor V2, retención de agua e hiponatremia. No se conoce que la quinidina antagonice el receptor V2 ni que inhiba la señalización posterior de AMPc/acuaporina-2, por lo que no hay una explicación plausible de cómo contrarrestaría esta alteración.

El puntaje elevado de TxGNN (0.9927) es solo una predicción computacional del modelo TxGNN (deep learning), que puede reflejar similitudes aprendidas por el modelo entre enfermedades relacionadas, no evidencia biológica, y no ha sido validado mecanística ni clínicamente. Cualquier vínculo propuesto (por ejemplo, mediante la modulación de canales iónicos en células del túbulo colector) es especulativo.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51706 | QUINIDINA | Grageas x 20 | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, deficiencia de potasio, psoriasis y parapsoriasis, trastornos hipotensivos, miastenia gravis (incluida la del adulto) y enfermedades de la unión neuromuscular, bloqueo auriculoventricular, bloqueo cardíaco familiar progresivo, bloqueo de rama izquierda, enfisema pulmonar, disquinesia esofágica, insuficiencia cardíaca e intoxicación digitálica.
- **Interacciones farmacológicas:** se registraron 345 interacciones. Entre las de nivel **mayor** figuran loperamida, claritromicina, ácido picosulfúrico, polietilenglicol 3350 con electrolitos, dolasetrón, eliglustat y palonosetrón. Entre las de nivel moderado figuran famotidina, ranitidina, cimetidina, metformina, aprepitant, ácido acetilsalicílico, bisacodilo, glicopirronio, clorpropamida, citrato de potasio, eluxadolina, glimepirida y trospio.
- **Riesgo específico para la nueva indicación:** la quinidina puede prolongar el intervalo QT y causar proarritmia. Esto es especialmente preocupante en pacientes con hiponatremia crónica, en quienes las alteraciones electrolíticas aumentan aún más el riesgo de arritmias. Además, la enfermedad renal figura entre las contraindicaciones.

Consultar el prospecto para información de seguridad completa, ya que no se dispone del texto oficial de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la quinidina y la activación constitutiva del receptor V2. Además, el perfil de seguridad (prolongación del QT, numerosas interacciones, riesgo con hiponatremia) es una barrera importante.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la quinidina y análisis de un posible vínculo con la vía V2/AMPc/acuaporina-2.
- Estudios preclínicos que evalúen un efecto sobre la actividad del receptor V2 mutado.
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Revisión sistemática de la literatura y de registros de ensayos sobre NSIAD.
- Evaluar alternativas terapéuticas existentes y la relación riesgo-beneficio cardiovascular en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

