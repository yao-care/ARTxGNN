---
layout: default
title: Prasterone
parent: Solo Predicción del Modelo (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Prasterone: nueva indicación predicha, Deficiencia de cofactor 2 de la heparina (nivel de evidencia L5). Indicación original: Lupus eritematoso sistémico…"
---

# Prasterone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Prasterona: De Lupus Eritematoso Sistémico a Deficiencia de Cofactor 2 de la Heparina

## Resumen en Una Frase

Prasterona (DHEA) es un esteroide precursor de hormonas sexuales, cuyas indicaciones originales incluyen el lupus eritematoso sistémico (incluido el pediátrico) y la dispareunia psicológica.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de cofactor 2 de la heparina**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lupus eritematoso sistémico, lupus eritematoso sistémico pediátrico y dispareunia psicológica (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Deficiencia de cofactor 2 de la heparina |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la prasterona (DHEA) es un precursor de andrógenos y estrógenos, y se ha utilizado en lupus eritematoso sistémico y en dolor durante las relaciones sexuales asociado a atrofia vulvovaginal.

La relación entre estas indicaciones y la deficiencia de cofactor 2 de la heparina es débil. No se conoce un mecanismo establecido por el cual la prasterona influya en la función del cofactor II de la heparina (SERPIND1). El vínculo probablemente es un artefacto de vecindad en la red del grafo de conocimiento, en un agrupamiento de términos relacionados con la coagulación.

Por ello, el puntaje alto (99.99%) debe interpretarse con cautela: refleja una predicción basada en el grafo, sin respaldo clínico ni bibliográfico. Otras predicciones de la lista tienen una plausibilidad mecanística indirecta algo mayor (por ejemplo, la esclerodermia, por su relación con enfermedades autoinmunes del tejido conectivo como el lupus), pero tampoco cuentan con evidencia en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35633 | SUPLIGOL NF | Inyectable IM, 1 x 1 ml | No especificada en los datos |
| 980 | LONGEVITAL | Comprimidos de 5000 mcg, x 30 | No especificada en los datos |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología:** se registró una interacción farmacológica de tipo farmacológico: la prasterona (deshidroepiandrosterona) actúa sobre el receptor de glicina (todos los subtipos). No se dispone de nivel de gravedad.
- **Consideración adicional:** según el análisis de las predicciones, al ser un precursor de andrógenos y estrógenos, debería evaluarse el posible riesgo trombótico antes de cualquier avance en indicaciones relacionadas con trombofilia o coagulación.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la deficiencia de cofactor 2 de la heparina es solo computacional (nivel L5), sin ensayos ni literatura, y no existe un mecanismo plausible conocido. Además, el perfil hormonal de la prasterona plantea una posible preocupación en trastornos trombóticos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la prasterona
- Búsqueda dirigida de literatura y ensayos clínicos, priorizando candidatas con mayor plausibilidad indirecta (por ejemplo, esclerodermia)
- Advertencias y contraindicaciones del prospecto de ANMAT
- Evaluación del riesgo trombótico asociado a metabolitos androgénicos/estrogénicos
- Confirmación de la indicación aprobada en las autorizaciones locales y de la compatibilidad de vías de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

