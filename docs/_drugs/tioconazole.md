---
layout: default
title: Tioconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 237
evidence_level: L5
indication_count: 2
monitor_inn: "tioconazole"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-03
description: "Tioconazole: nueva indicación predicha, Vulvitis (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tioconazole
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

## Tioconazole: Vulvitis
{: .text-alpha }

## Resumen en Una Frase

Tioconazol es un antifúngico imidazólico de uso tópico, comercializado en Argentina en soluciones para uñas y cápsulas vaginales.
El modelo TxGNN predice que podría ser efectivo para **Vulvitis (vulvitis)**,
pero no hay ensayos clínicos registrados para esta enfermedad y la literatura disponible es indirecta (**20 publicaciones**, centradas en candidiasis vaginal).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Vulvitis |
| Puntaje de Predicción TxGNN | 0.9920 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (3 de 3) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El tioconazol inhibe la enzima lanosterol 14-α desmetilasa (CYP51 o ERG11) de hongos y levaduras. Esta enzima convierte el lanosterol en ergosterol, un componente esencial de la pared celular, y sin él el patógeno no sobrevive. Además, inhibe la enzima humana CYP8B1, que participa en la síntesis de ácidos biliares.

La vulvitis puede superponerse con cuadros de origen fúngico (por Candida), y en ese caso la actividad antifúngica del tioconazol sería plausiblemente relevante. Sin embargo, la literatura recuperada trata sobre candidiasis vaginal y no sobre la vulvitis como entidad separada, por lo que el vínculo es indirecto.

La eficacia en vulvitis de origen no fúngico no tiene respaldo. Por ello, el puntaje del modelo debe interpretarse como una hipótesis computacional y no como evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna publicación estudia directamente la vulvitis; las siguientes son las más relevantes por proximidad (candidiasis vaginal y revisiones del fármaco).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | ECA | Antimicrob Agents Chemother | Tioconazol en dosis única vs. clotrimazol 3 días (80 pacientes): 84 % vs. 85 % asintomáticas a las 4 semanas |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECA | Gynakol Rundsch | Comparación doble ciego de tioconazol vs. placebo en candidiasis vaginal, con evaluación de absorción sistémica |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revisión | Drugs | Amplio espectro in vitro; ensayos abiertos y controlados muestran eficacia y seguridad tópica en micosis superficiales y candidiasis vaginal |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revisión | Expert Rev Anti Infect Ther | Opciones azólicas no invasivas para candidiasis vulvovaginal, incluidas formas recurrentes |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Estudio clínico | Acta Obstet Gynecol Scand | Crema vaginal al 2 % durante 3 días: curación micológica del 88,5 % |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Estudio aleatorizado abierto | J Int Med Res | Tioconazol tópico en dosis única vs. ketoconazol oral 5 días (40 pacientes): ambos erradican la infección; los síntomas mejoran más rápido con el tópico |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Estudio abierto no comparativo | J Int Med Res | Crema al 2 % en infección por T. vaginalis o mixta (20 pacientes): 95 % de curación |
| [30553009](https://pubmed.ncbi.nlm.nih.gov/30553009/) | 2019 | Preclínico | Int J Pharm | Películas vaginales de quitosano-HPMC con tioconazol como forma farmacéutica alternativa |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 22628 | TIOMICOL (Panalab) | Solución para uñas x 12 ml | No registrada en los datos locales |
| 18628 | HONGUIL (Megalabs Argent) | Cápsulas vaginales x 1 | No registrada en los datos locales |
| 13596 | TROSYD (Pfizer) | Solución para uñas al 28% x 12 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

**Interacciones Farmacológicas:**
- Omeprazol (nivel de interacción no clasificado).
- CYP8B1: el tioconazol inhibe esta enzima humana, que participa en la síntesis de ácidos biliares.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen directamente la vulvitis; la evidencia es indirecta y proviene de candidiasis vaginal. El puntaje de 0,9920 es una predicción computacional sin respaldo clínico propio, por lo que corresponde nivel L5.

**Para avanzar se necesita:**
- Estudios que evalúen la vulvitis como entidad separada, diferenciando las formas de origen fúngico de las no fúngicas
- Advertencias y contraindicaciones del prospecto de ANMAT
- Datos de compatibilidad de vía de administración para la indicación propuesta

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

