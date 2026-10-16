---
layout: default
title: Calcitriol
parent: Solo Predicción del Modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Calcitriol: nueva indicación predicha, Deficiencia de vitamina D (término obsoleto) (nivel de evidencia L5). Indicación original: Trastornos del metabolismo del calcio y el fósforo (hipercalcemia…"
---

# Calcitriol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Calcitriol: De Osteodistrofia Renal e Hipoparatiroidismo a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D y se utiliza en trastornos del metabolismo del calcio y el fósforo, como el hipoparatiroidismo y la osteodistrofia renal.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de vitamina D (término clasificado como obsoleto en la ontología)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción puntual: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos del metabolismo del calcio y el fósforo (hipercalcemia, hipoparatiroidismo, hipofosfatemia, osteodistrofia renal, entre otros, según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están informados) |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Calcitriol es la forma hormonalmente activa de la vitamina D. Por eso existe un vínculo biológico plausible con la deficiencia de vitamina D. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe.

Sin embargo, la plausibilidad es débil en términos prácticos. El término de la enfermedad está marcado como obsoleto en la ontología. Además, para una deficiencia nutricional simple el tratamiento habitual es la vitamina D nativa (colecalciferol o ergocalciferol), no calcitriol. Es probable que el puntaje alto refleje un artefacto de la ontología y no una verdadera oportunidad de reposicionamiento.

No se encontraron ensayos clínicos ni literatura asociados a esta predicción concreta. El puntaje de 99.96% (posición 409 en el ranking del modelo) debe interpretarse solo como una señal computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46020 | CALCIRAQUIFEROL (Roemmers) | Cápsulas blandas x 30 | No informada en los datos |
| 7483 | CALCITRIOL (Siegfried) | Cápsulas 0.25 mcg x 30 | No informada en los datos |
| 24450 | CALCITRIOL MEGALABS (Megalabs Argent) | Cápsulas x 30 | No informada en los datos |

Las tres autorizaciones están vigentes y corresponden a productos de un solo principio activo.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el texto del prospecto)**: enfermedad renal, sarcoidosis, hipercalcemia, nefrocalcinosis, nefrolitiasis (incluida la susceptibilidad asociada a SLC26A1), nefropatía aguda por uratos, hiperfosfatemia, hipervitaminosis, piouréter y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - **Gravedad mayor**: colecalciferol, calcifediol y burosumab.
  - **Gravedad moderada**:
    - Diuréticos tiazídicos (hidroclorotiazida, bendroflumetiazida, clortalidona, clorotiazida, benztiazida).
    - Anticonvulsivantes y barbitúricos (fosfenitoína, carbamazepina, amobarbital, butalbital, butabarbital).
    - Resinas secuestrantes de ácidos biliares (colestiramina, colesevelam, colestipol).
    - Digoxina y digitoxina.
    - Hidróxido de aluminio.
    - Calcipotriol tópico.

Consultar el prospecto para información de seguridad adicional (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni literatura. El término de la enfermedad es obsoleto y, para la deficiencia nutricional de vitamina D, existen alternativas preferidas. Probablemente se trata de un artefacto de la ontología y no de una señal real de reposicionamiento.

**Para avanzar se necesita:**
- Confirmar si existe un equivalente vigente del término de enfermedad y si tiene relevancia clínica real frente a la vitamina D nativa.
- Obtener y revisar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas de cada autorización).
- Obtener datos detallados del mecanismo de acción.

**Nota sobre otras predicciones del mismo análisis:** la mejor respaldada es el **raquitismo hipofosfatémico hereditario** (puntaje TxGNN 99.28%, nivel L2, decisión *Proceed with Guardrails*). Cuenta con 2 ensayos clínicos: uno de Fase temprana 1 completado con 16 participantes (NCT03748966) y uno de Fase 4 con 100 participantes y estado desconocido (NCT03820518). Además, calcitriol con fosfato ya es terapia convencional en esta enfermedad, por lo que es más una alineación de indicación que un reposicionamiento novedoso. Esta candidata merece una evaluación específica, con monitoreo de hipercalciuria, nefrocalcinosis e hiperparatiroidismo. Otras predicciones, como la subforma familiar aislada de hipoparatiroidismo, se consideran subconjuntos de indicaciones ya establecidas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

