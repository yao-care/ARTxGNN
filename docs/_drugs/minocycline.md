---
layout: default
title: Minocycline
parent: Solo Predicción del Modelo (L5)
nav_order: 191
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Minocycline: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Infección urinaria, bronquitis…"
monitor_inn: "minocycline"
predicted_indications: ["exposure keratitis"]
---

# Minocycline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Minociclina: De Infección Urinaria, Bronquitis y Acné a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La minociclina es un antibiótico del grupo de las tetraciclinas, utilizado originalmente para tratar infecciones urinarias, bronquitis, acné y otras infecciones bacterianas.
El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección urinaria, bronquitis, acné y otras infecciones bacterianas (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la minociclina es una tetraciclina cuya eficacia antibacteriana y en acné está comprobada, y mecanísticamente podría ser aplicable a enfermedades inflamatorias de la superficie ocular.

Como hipótesis basada en conocimiento general (no en los datos aportados), las tetraciclinas tienen actividad antiinflamatoria y de inhibición de metaloproteinasas de matriz (MMP). Se utilizan en afecciones inflamatorias de la superficie ocular como la disfunción de las glándulas de Meibomio y la blefaritis. Esto sugiere un posible vínculo con la queratoconjuntivitis epitelial punteada, aunque no puede verificarse frente al mecanismo documentado del fármaco.

También se predijo una segunda indicación, la **queratitis por exposición** (puntaje 99.20%, también nivel L5, decisión Hold). Allí el beneficio sería especulativo, ya que su manejo se basa principalmente en corregir el cierre palpebral y lubricar la superficie ocular.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55081 | LIMAFIL 50 | 50 mg comprimidos x 30 | No especificada |
| 32863 | SEBOCLEAR 100 | Comprimidos recubiertos x 30 | No especificada |
| 25427 | MEIBI | 50 mg comprimidos x 30 | No especificada |
| 47719 | MINOCICLINA RICHET | 100 mg comprimidos x 30 | No especificada |
| 32862 | SEBOCLEAR 100 | Comprimidos recubiertos x 10 | No especificada |

Se muestran 5 de las 8 autorizaciones vigentes (todas de producto único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, pseudotumor cerebral, hipertensión intracraneal y disquinesia del esófago.
- **Interacciones farmacológicas**: se identificaron 272 interacciones. Las más relevantes de gravedad **mayor** son:
  - Isotretinoína
  - Acitretina

  Entre las de gravedad **moderada** figuran etinilestradiol, amoxicilina, ampicilina, citrato de sodio, balsalazida, subcitrato de bismuto potásico, fosfato de calcio, acetato de calcio, cannabidiol, brentuximab vedotina y asparaginasas. Hay además interacciones **menores** con acetazolamida, hidroclorotiazida, amilorida y bumetanida.

Las advertencias y contraindicaciones del prospecto de ANMAT aún no se han incorporado; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin datos de mecanismo de acción ni de advertencias del prospecto que permitan un análisis de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), lo que actualmente bloquea el cribado de seguridad
- Completar los datos del mecanismo de acción (MOA) desde DrugBank
- Realizar una búsqueda sistemática de literatura y ensayos sobre tetraciclinas/minociclina en queratoconjuntivitis epitelial punteada
- Evaluar la compatibilidad de vía de administración (los productos locales son comprimidos orales y la indicación es ocular)
- Considerar la relevancia de las interacciones mayores y de las contraindicaciones (p. ej., hipertensión intracraneal) frente a la población objetivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

