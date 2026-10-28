---
layout: default
title: Pridinol
parent: Solo Predicción del Modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Pridinol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "PRIDINOL"
predicted_indications: ["insomnia (disease)"]
---

# Pridinol
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

## Pridinol: De Indicación Original No Especificada a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Pridinol es un relajante muscular de acción central con propiedades anticolinérgicas, comercializado en Argentina principalmente en combinaciones con antiinflamatorios (por ejemplo, meloxicam o diclofenac) para el dolor muscular. En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; el sustento es únicamente la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: al menos 20) |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pridinol es un relajante muscular de acción central con propiedades anticolinérgicas (antimuscarínicas), utilizado en cuadros de dolor y espasmo muscular. Su uso en Argentina se observa sobre todo en asociaciones con antiinflamatorios no esteroides.

Existen dos vías plausibles, ninguna verificada. La primera: la actividad antimuscarínica central podría producir sedación. La segunda: el alivio del espasmo muscular doloroso podría mejorar el sueño de forma indirecta. Ninguna de las dos está documentada en los datos compilados.

Además, los fármacos anticolinérgicos también pueden empeorar la calidad del sueño y la función cognitiva, por lo que la dirección del efecto es incierta. El único respaldo es un puntaje alto del modelo (0.9989), un valor derivado del modelo sin validación clínica. La similitud con la indicación original está pendiente de evaluar y la compatibilidad de vías de administración también está pendiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de productos de un solo registro (sin cancelaciones). Se muestran las 5 principales; los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44309 | DIOXAFLEX PLUS | Inyectable x 6 | No disponible |
| 47973 | DICLOMAR FLEX POTASICO | Comprimidos x 15 | No disponible |
| 38086 | FLEXIDOL RELAX | Comprimidos recubiertos/ranurados x 20 | No disponible |
| 54325 | MELOXICAM + PRIDINOL TEVA | Comprimidos 15/4 mg x 10 | No disponible |
| 44208 | PRINIL | Comprimidos ranurados 4 mg x 10 | No disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una predicción del modelo sin ensayos clínicos ni literatura (nivel L5). Además, la dirección del efecto es incierta, ya que las propiedades anticolinérgicas podrían empeorar el sueño y la cognición.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente sin datos
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar las indicaciones aprobadas de las autorizaciones en Argentina
- Realizar una búsqueda sistemática de literatura y ensayos sobre pridinol (u otros antimuscarínicos centrales) en trastornos del sueño
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración
- Considerar estudios preclínicos o de mecanismo antes de cualquier ensayo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

