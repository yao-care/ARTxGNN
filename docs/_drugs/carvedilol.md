---
layout: default
title: Carvedilol
parent: Solo Predicción del Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Carvedilol: De Hipertensión a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con bloqueo alfa-1, utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; la predicción se basa únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, carvedilol es un betabloqueante no selectivo con actividad bloqueadora alfa-1 adrenérgica, y su eficacia en hipertensión está establecida y está comercializado para ese fin.

La hipertensión renovascular maligna es una forma grave de hipertensión en la que la activación del sistema renina-angiotensina tiene un papel central. El bloqueo beta reduce la liberación de renina, por lo que mecanísticamente podría ser aplicable como extensión de su acción antihipertensiva.

Sin embargo, esta relación es puramente computacional: no se aportaron ensayos ni literatura para esta indicación. Esta predicción es en gran medida una extensión de la clase de indicación ya existente (hipertensión) más que un uso verdaderamente nuevo.

### Otras predicciones del modelo (para contexto)

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 99.55% | L5 | Solapa con la indicación existente; sin evidencia específica |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.54% | L5 | Fisiopatología distinta; los betabloqueantes se usan con cautela por el riesgo para la función del ventrículo derecho |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.54% | L4 | Solo evidencia indirecta, mayormente preclínica (ver abajo) |
| Síndrome de Braddock | 99.37% | L5 | Sin fundamento mecanístico evidente; probablemente proximidad en la red |

Entre estas, la hipertensión pulmonar por enfermedad pulmonar/hipoxia es la única con literatura recuperada, pero es indirecta: estudios en ratas muestran que carvedilol revirtió la hipertensión inducida por hipoxia intermitente crónica (PMID 26291659) y que inhibió la hipertrofia ventricular derecha por hipoxia crónica (PMID 16639551), además de efectos antioxidantes y antiapoptóticos cardioprotectores (PMID 25187802, PMID 28862654). Estos hallazgos no demuestran eficacia en enfermedad vascular pulmonar humana, y varias publicaciones recuperadas no guardan relación con el tema.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipertensión renovascular maligna).

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto único).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59509 | CARVEDIL 12.5 | 12.5 mg comprimidos x 60 | No disponible |
| 59512 | CARVEDIL 50 | 50 mg comprimidos x 30 | No disponible |
| 36205 | CORUBIN | 6.25 mg comprimidos x 28 | No disponible |
| 45532 | ENTARSOL 6.25 | 6.25 mg comprimidos x 28 | No disponible |
| 44594 | DILATREND AP | 80 mg cápsulas x 30 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: insuficiencia hepática, asma (incluidas formas intrínseca y alérgica), bronquitis, enfisema pulmonar y otras enfermedades bronquiales, diabetes mellitus, cetoacidosis diabética, trastornos hipotensivos, enfermedad vascular periférica (incluida claudicación intermitente y enfermedad arterial periférica), bloqueo auriculoventricular, síndrome del seno enfermo (incluida forma familiar), angina de Prinzmetal, anafilaxia y síndrome del iris flácido intraoperatorio.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales mostradas:
  - **Mayor**: epinefrina.
  - **Moderadas**: hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, hiosciamina, atropina, bupropión, morfina, lorcaserina, canagliflozina, acetohexamida, y sales de calcio (fosfato, acetato, carbonato, citrato).
  - **Menores**: ácido acetilsalicílico, hidróxido de aluminio, attapulgita.
- Las advertencias del prospecto de ANMAT no están disponibles; consultar el prospecto para información de seguridad adicional.
- Nota relevante: la revisión sobre efectos respiratorios de los betabloqueantes (PMID 19789971) y las contraindicaciones respiratorias anteriores exigen especial cautela si se considerara su uso en hipertensión pulmonar asociada a enfermedad pulmonar.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión renovascular maligna tiene un puntaje alto del modelo (99.55%), pero no cuenta con ensayos clínicos ni literatura (nivel L5), y en gran medida replica la indicación antihipertensiva ya existente. No hay base para avanzar por ahora.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (DrugBank)
- Prospecto de ANMAT con advertencias y contraindicaciones oficiales
- Revisión de literatura y ensayos específicos sobre hipertensión renovascular maligna y su relación con el bloqueo beta/alfa-1
- Evaluación de si esta indicación representa realmente un uso nuevo o es una extensión de la indicación actual de hipertensión
- Para la hipertensión pulmonar por hipoxia: estudios clínicos que superen la evidencia preclínica indirecta y una evaluación cuidadosa de la seguridad respiratoria y del ventrículo derecho
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

