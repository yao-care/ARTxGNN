---
layout: default
title: Mupirocin
parent: Solo Predicción del Modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Mupirocin: nueva indicación predicha, Empiema pleural (nivel de evidencia L5). Indicación original: Impétigo e impétigo ampollar (según las relaciones de indicación del…"
monitor_inn: "mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Mupirocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Mupirocina: De Impétigo a Empiema Pleural
{: .text-alpha }

## Resumen en Una Frase

Mupirocina es un antibiótico de uso tópico, originalmente utilizado para el tratamiento del impétigo y del impétigo ampollar.
El modelo TxGNN predice que podría ser efectivo para **Empiema Pleural**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Impétigo e impétigo ampollar (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Empiema pleural |
| Puntaje de Predicción TxGNN | 99.49% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, la mupirocina inhibe la isoleucil-tRNA sintetasa bacteriana y actúa principalmente contra cocos grampositivos como *Staphylococcus aureus* (incluido el SARM) y *Streptococcus pyogenes*.

Estos mismos microorganismos son causas frecuentes de empiema pleural, lo que ofrece un vínculo plausible pero solo teórico entre la indicación original (infecciones cutáneas bacterianas) y la nueva indicación predicha.

Sin embargo, existe una limitación importante: la mupirocina se formula únicamente para uso tópico, tiene biodisponibilidad sistémica insignificante y se metaboliza rápidamente a ácido monico inactivo. Por ello, es poco probable que alcance concentraciones terapéuticas en el espacio pleural. El puntaje alto de TxGNN es una predicción computacional, y la compatibilidad de vía de administración aún no ha sido evaluada.

**Otra predicción del modelo:** queratoconjuntivitis epitelial punteada (puntaje 99.10%, nivel L5, decisión Hold). Su plausibilidad es baja: esta condición suele ser viral o asociada a enfermedad de la superficie ocular, la mupirocina no tiene actividad antiviral, y la base del ungüento (polietilenglicol) no está formulada para uso oftálmico y podría irritar la superficie ocular.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se muestran 5 de las 10 autorizaciones vigentes (todas de producto único, ninguna cancelada).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28302 | MUPIROX NASAL | Ungüento 2% x 5 g | No disponible |
| 17082 | BACTROBAN NASAL | Ungüento x 3 g | No disponible |
| 28358 | BACTROBAN CREMA | Pomada x 15 g | No disponible |
| 48667 | QUEMICETINA NF NASAL | Ungüento 2% x 3 g | No disponible |
| 30464 | MUPIROX | Ungüento 2% x 15 g | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): dermatitis.
- **Interacciones Farmacológicas**: se identificaron 118 posibles interacciones, todas con nivel de gravedad no clasificado. Entre las primeras listadas figuran calcitriol, clotrimazol, morfina, metformina, pantoprazol, omeprazol, sucralfato, vancomicina, lactulosa y triamcinolona. Dado que la mupirocina es de uso tópico con absorción sistémica mínima, la relevancia clínica de estas interacciones debe verificarse.

Para el resto de la información de seguridad (advertencias y contraindicaciones del prospecto), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni literatura de respaldo. Además, la formulación tópica con absorción sistémica insignificante hace improbable alcanzar concentraciones eficaces en el espacio pleural.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de ANMAT con advertencias y contraindicaciones
- Evaluación de compatibilidad de vía de administración (formulación tópica vs. necesidad de acceso pleural)
- Búsqueda de estudios preclínicos o clínicos sobre mupirocina en infecciones pleurales
- Textos de indicación aprobada de las autorizaciones locales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

