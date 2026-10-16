---
layout: default
title: Olopatadine
parent: Solo Predicción del Modelo (L5)
nav_order: 205
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Olopatadine: nueva indicación predicha, Conjuntivitis rosácea (nivel de evidencia L5). Indicación original: Rinitis alérgica…"
monitor_inn: "OLOPATADINE"
predicted_indications: ["rosacea conjunctivitis"]
---

# Olopatadine
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

# Olopatadina: De Rinitis Alérgica y Conjuntivitis Alérgica a Conjuntivitis Rosácea

## Resumen en Una Frase

Olopatadina es un antihistamínico de uso oftálmico, originalmente utilizado para el tratamiento de la rinitis alérgica y de distintas formas de conjuntivitis alérgica (atópica, papilar y primaveral).
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis rosácea**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora y conjuntivitis alérgica (atópica, papilar y primaveral) |
| Nueva Indicación Predicha | Conjuntivitis rosácea |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

Nota: las autorizaciones de ANMAT compiladas no incluyen el texto de indicación aprobada; la indicación original se tomó de la base de conocimiento del modelo TxGNN.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro compilado. Según el conocimiento farmacológico general, la olopatadina es un antagonista selectivo del receptor de histamina H1 con actividad estabilizadora de mastocitos, y su eficacia en las conjuntivitis alérgicas está establecida.

La rosácea ocular (conjuntivitis rosácea) se caracteriza por disfunción de las glándulas de Meibomio, inflamación del párpado y de la superficie ocular, y factores microbianos o de *Demodex*, con un componente inflamatorio principalmente no alérgico. Por ello, un posible beneficio de la olopatadina se limitaría a síntomas mediados por histamina o mastocitos, como el picor y el enrojecimiento. Este vínculo es teórico y no un mecanismo establecido.

El puntaje muy alto de TxGNN (0.994) probablemente refleja la cercanía en el grafo de conocimiento con las indicaciones aprobadas de conjuntivitis, y no está respaldado por datos clínicos. La similitud con la indicación original y la compatibilidad de vías de administración aún están pendientes de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay 10 autorizaciones vigentes, todas de producto único (sin combinaciones) y ninguna cancelada. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 41436 | PATANOL S (Novartis) | 0.2% frasco gotero x 2.5 ml | No disponible en el registro |
| 21143 | PATANOL (Novartis) | 0.1% frasco gotero x 5 ml | No disponible en el registro |
| 41039 | OLOPAT (Elea) | 0.1% solución oftálmica x 5 ml | No disponible en el registro |
| 57800 | TIMALERG (Max Vision) | 0.2% solución oftálmica x 5 ml | No disponible en el registro |
| 52910 | OLORATAN (Sidus) | 0.2% solución oftálmica x 2.5 ml | No disponible en el registro |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad de las vías respiratorias inferiores, enfermedad de los senos paranasales, enfermedad de la cavidad nasal y enfermedad de las vías respiratorias superiores.
- **Interacciones farmacológicas:** la consulta se completó y devolvió 100 interacciones, todas con nivel de gravedad "desconocido" (fuente: DDInter). Algunos ejemplos son pantoprazol, doxiciclina, clotrimazol, metformina, omeprazol, lansoprazol, cimetidina, triamcinolona, prednisona y simvastatina. Su relevancia clínica no está clasificada.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo de la rosácea ocular es mayormente no alérgico, por lo que el vínculo con la olopatadina es solo teórico. Además, faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), requisito previo para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura y de registros de ensayos sobre antihistamínicos o estabilizadores de mastocitos en rosácea ocular.
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración (ambas pendientes).
- Considerar, de haber sustento, estudios preclínicos o un piloto exploratorio centrado en síntomas de picor y enrojecimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

