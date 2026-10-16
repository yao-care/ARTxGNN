---
layout: default
title: Ethosuximide
parent: Solo Predicción del Modelo (L5)
nav_order: 137
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Ethosuximide: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: Epilepsia de ausencia"
---

# Ethosuximide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Etosuximida: De Epilepsia de Ausencia a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

La etosuximida (ZARONTIN) es un fármaco antiepiléptico utilizado originalmente para el tratamiento de la epilepsia de ausencia.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (SNAI)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia de ausencia |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la etosuximida actúa en la epilepsia de ausencia bloqueando los canales de calcio tipo T de las neuronas talámicas, y su eficacia en esa indicación está bien establecida.

El SNAI es causado por mutaciones de ganancia de función en el receptor V2 de vasopresina (AVPR2, por ejemplo R137C/R137L) o en GNAS, que provocan activación constitutiva del receptor y retención de agua independiente de la arginina vasopresina. No existe una conexión establecida entre el bloqueo de canales de calcio tipo T y esta fisiopatología.

Cualquier vínculo sería especulativo (por ejemplo, a través de la modulación del manejo renal del agua o de la señalización cAMP/acuaporina-2), y los datos compilados no lo respaldan. El puntaje muy alto del modelo (99.91%) es solo una predicción computacional, sin corroboración clínica ni bibliográfica.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6357 | ZARONTIN | Líquido x 120 ml | No disponible en los datos compilados |
| 6356 | ZARONTIN | Cápsulas x 25 | No disponible en los datos compilados |

Ambas autorizaciones están vigentes (fabricante: Elea).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, piouréter, enfermedad hematológica, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), neutropenia, agranulocitosis y porfiria aguda intermitente.
- **Interacciones Farmacológicas**: se identificaron 92 interacciones en total. Las primeras 20 listadas son todas de nivel moderado, entre ellas: aprepitant, morfina (incluida la liposomal), dronabinol, nabilona, metoclopramida, opio, sibutramina, etanol, cobicistat, ácido fólico, deferasirox, prometazina, levoleucovorina, leucovorina, fostamatinib, cloroquina, mefloquina, hidroxicloroquina y clorfeniramina.

Las advertencias y contraindicaciones del prospecto de ANMAT no están disponibles; consultar el prospecto para confirmar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, y no hay un vínculo mecanístico plausible entre el bloqueo de canales de calcio tipo T y la activación constitutiva del receptor V2 que causa el SNAI. Además, la etosuximida tiene contraindicaciones en el grafo de conocimiento relacionadas con enfermedad renal y hematológica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos o de mecanismo que evalúen un posible efecto sobre la vía AVPR2/cAMP/acuaporina-2.
- Revisar la literatura y los registros de ensayos para detectar cualquier evidencia relacionada con SNAI.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

