---
layout: default
title: Triamcinolone
parent: Solo Predicción del Modelo (L5)
nav_order: 241
evidence_level: L5
indication_count: 8
monitor_inn: "triamcinolone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
last_modified_at: 2026-11-20
description: "Triamcinolone: nueva indicación predicha, alopecia mucinosa (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 5 (en el listado vigente: 5)"
---

# Triamcinolone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Triamcinolona: corticosteroide de uso tópico → alopecia mucinosa (alopecia mucinosa)
{: .text-alpha }

## Resumen en Una Frase

Triamcinolona es un corticosteroide con acción antiinflamatoria, comercializado en Argentina en presentaciones de uso tópico.
El modelo TxGNN predice que podría ser efectivo para **alopecia mucinosa (alopecia mucinosa)**, con **0 ensayos clínicos** y **2 publicaciones** (ambas reportes de caso, sin datos directos de triamcinolona) que actualmente se relacionan con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | alopecia mucinosa (alopecia mucinosa) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (5 de 5) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Triamcinolone (traducción no oficial): «Los estudios indican que, tras una dosis intramuscular única de 60 mg a 100 mg de acetónido de triamcinolona, la supresión suprarrenal se produce en un plazo de 24 a 48 horas y luego vuelve gradualmente a la normalidad, por lo general en 30 a 40 días. Este hallazgo se correlaciona estrechamente con la duración prolongada de la acción terapéutica que se logra con el fármaco.» Texto original en inglés: "Studies indicate that following a single intramuscular dose of 60 mg to 100 mg of triamcinolone acetonide, adrenal suppression occurs within 24 to 48 hours and then gradually returns to normal, usually in 30 to 40 days. This finding correlates closely with the extended duration of therapeutic action achieved with the drug." ([DailyMed: Kenalog-40 (triamcinolone acetonide) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ce116aa-b330-4da9-9cdd-ba8e6be0c4ad), versión del 2026-01-05; consultado el 2026-11-19). Según la información conocida, la triamcinolona es un corticosteroide potente que suprime la inflamación local y la respuesta inmunitaria.

La alopecia mucinosa (mucinosis folicular) se caracteriza por un infiltrado linfocitario perifolicular y acumulación de mucina en los folículos. Mecanísticamente, un antiinflamatorio como la triamcinolona (por ejemplo, intralesional) podría reducir ese componente inflamatorio, y esto es consistente con la práctica dermatológica habitual. Sin embargo, se trata de un razonamiento plausible y no de una demostración.

Es importante subrayar que el puntaje de TxGNN es una predicción computacional. La literatura aportada no documenta resultados con triamcinolona en esta enfermedad: un reporte de caso de 1964 y otro de 2014 que describe el éxito de bexaroteno tópico en gel, un fármaco distinto. Por ello, ningún estudio citado evalúa directamente triamcinolona en alopecia mucinosa y el nivel de evidencia se establece en L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | Reporte de caso | International Journal of Dermatology | Primer caso de mucinosis folicular idiopática persistente tratado con éxito con bexaroteno tópico en gel; no evalúa triamcinolona |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | Reporte de caso | Hifuka Kiyo. Acta Dermatologica | Reporte de un caso de alopecia mucinosa de Pinkus (mucinosis folicular de Jablonska); sin resumen disponible |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21316 | GLYTOP | Crema, 30 g | No registrada |
| 21317 | GLYTOP-F | Crema, 30 g | No registrada |
| 17884 | MANTUS | Pomada/polvo, 30 g | No registrada |
| 896 | BAGOVIT A PLUS | Crema, 100 g | No registrada |
| 17883 | MANTUS | Pomada/polvo, 10 g | No registrada |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 696 interacciones registradas. Entre las incluidas en los datos compilados, la de **adalimumab** es de nivel mayor. Hay además numerosas de nivel moderado, por ejemplo con zidovudina, isotretinoína, acarbosa, acebutolol, acetazolamida, ketorolaco, nifedipino, ibuprofeno, etinilestradiol, aldesleucina, alemtuzumab y aliskiren. Las interacciones con formoterol y salbutamol son de nivel menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto, pero no existen ensayos clínicos y la literatura disponible son solo dos reportes de caso que no estudian triamcinolona en alopecia mucinosa. La evidencia se limita a la predicción del modelo (L5).

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre el uso de corticosteroides (intralesionales o tópicos) en mucinosis folicular
- Series de casos o estudios observacionales que documenten resultados con triamcinolona en esta enfermedad
- Datos del mecanismo de acción y del prospecto aprobado en ANMAT (advertencias y contraindicaciones)
- Confirmación de la compatibilidad de la vía de administración (intralesional vs. tópica) con las presentaciones disponibles en Argentina

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Kenalog-40 (triamcinolone acetonide) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ce116aa-b330-4da9-9cdd-ba8e6be0c4ad) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

