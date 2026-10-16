---
layout: default
title: Triamcinolone
parent: Evidencia Moderada (L3-L4)
nav_order: 241
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Triamcinolone: nueva indicación predicha, Alopecia mucinosa (nivel de evidencia L4). Indicación original: No disponible en los textos de indicación aprobados en Argentina (cam…"
---

# Triamcinolone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Triamcinolona: De Enfermedades Autoinmunes e Inflamatorias a Mucinosis Folicular (Alopecia Mucinosa)

## Resumen en Una Frase

Triamcinolona es un corticosteroide que, según el conocimiento del modelo, se asocia a indicaciones originales como enfermedades autoinmunes, enfermedad de Crohn, enfermedad inflamatoria intestinal, insuficiencia suprarrenal y leucemia linfoblástica aguda.
El modelo TxGNN predice que podría ser efectivo para **alopecia mucinosa (mucinosis folicular)**,
pero actualmente hay **0 ensayos clínicos** y solo **2 publicaciones** (reportes de caso, ninguno específico de triamcinolona) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de indicación aprobados en Argentina (campos vacíos). Según el grafo de conocimiento: enfermedades autoinmunes, enfermedad de Crohn, insuficiencia suprarrenal, entre otras |
| Nueva Indicación Predicha | Alopecia mucinosa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, triamcinolona es un corticosteroide con acción antiinflamatoria e inmunosupresora, y su eficacia en enfermedades inflamatorias y autoinmunes es conocida.

La mucinosis folicular se caracteriza por un infiltrado linfocítico perifolicular. Los corticosteroides intralesionales y tópicos, como la triamcinolona, son plausiblemente útiles por su acción antiinflamatoria sobre ese infiltrado. Es una hipótesis mecanística, no una conclusión demostrada.

Cabe subrayar que la evidencia disponible es muy limitada: consiste solo en reportes de caso, y el caso de 2014 trata sobre gel de bexaroteno, no sobre triamcinolona. No existe evidencia directa de eficacia de triamcinolona en esta enfermedad en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | Reporte de caso | International Journal of Dermatology | Primer caso de mucinosis folicular idiopática tratada con éxito con gel de bexaroteno tópico al 1% (no es triamcinolona) |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | Reporte de caso | Hifuka Kiyo. Acta Dermatologica | Caso de alopecia mucinosa de Pinkus (mucinosis folicular de Jablonska); sin resumen disponible |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21316 | GLYTOP | Crema, 30 g | No disponible |
| 21317 | GLYTOP-F | Crema, 30 g | No disponible |
| 17884 | MANTUS | Pomada/polvo, 30 g | No disponible |
| 896 | BAGOVIT A PLUS | Crema, 100 g | No disponible |
| 17883 | MANTUS | Pomada/polvo, 10 g | No disponible |

Las cinco autorizaciones son de formulaciones de un solo principio activo, vigentes, y corresponden a presentaciones de uso tópico.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, sarampión, insuficiencia cardíaca congestiva, queratitis por virus del herpes simple, hipopituitarismo y otras deficiencias hipofisarias, y algunos trastornos del ciclo de la urea (deficiencia de carbamoil fosfato sintetasa I, hiperargininemia, citrulinemia).
- **Interacciones farmacológicas**: se identificaron 696 interacciones. Entre las de mayor relevancia figura **adalimumab (Mayor)**. Se reportan también interacciones de nivel moderado con zidovudina, isotretinoína, acarbosa, acebutolol, acetazolamida, ketorolac, ibuprofeno, nifedipino, etinilestradiol, aldesleukina, alemtuzumab y aliskiren, entre otros; con formoterol y salbutamol son de nivel menor.

Para advertencias y contraindicaciones de prospecto, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en dos reportes de caso, uno de 1964 y otro sobre un fármaco distinto (bexaroteno), sin ensayos clínicos. El puntaje alto del modelo no sustituye la evidencia clínica directa.

**Para avanzar se necesita:**
- Revisión de literatura específica sobre triamcinolona (intralesional o tópica) en mucinosis folicular
- Datos del mecanismo de acción
- Texto de indicaciones y advertencias del prospecto de ANMAT
- Evaluación de compatibilidad de vía de administración (las presentaciones locales son tópicas; la vía intralesional requeriría confirmación)
- Plan de monitoreo de seguridad, considerando las contraindicaciones del grafo y las interacciones relevantes

**Nota sobre otras predicciones:** de las demás indicaciones predichas, la foliculitis decalvante (Quinquaud) tiene el respaldo más sólido (nivel L3, revisión retrospectiva de 23 pacientes), aunque sin datos específicos de triamcinolona. El resto carece de evidencia o presenta un vínculo mecanístico débil.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

