---
layout: default
title: Tadalafil
parent: Solo Predicción del Modelo (L5)
nav_order: 231
evidence_level: L5
indication_count: 8
monitor_inn: "tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-10-30
description: "Tadalafil: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita) (nivel de evidencia L5). Indicación original: No consta en los d…"
---

# Tadalafil
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

## Tadalafilo: inhibidor de la fosfodiesterasa tipo 5 (PDE5) → Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita)
{: .text-alpha }

## Resumen en Una Frase

Tadalafilo es un inhibidor de la fosfodiesterasa tipo 5 que se comercializa actualmente en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras (Ambras type hypertrichosis universalis congenita) |
| Puntaje de Predicción TxGNN | 0,9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tadalafil (traducción no oficial): «La erección del pene durante la estimulación sexual se produce por el aumento del flujo sanguíneo peniano resultante de la relajación de las arterias del pene y del músculo liso de los cuerpos cavernosos. Esta respuesta está mediada por la liberación de óxido nítrico (NO) desde las terminaciones nerviosas y las células endoteliales, que estimula la síntesis de cGMP en las células del músculo liso. […] El tadalafilo inhibe la PDE5.» Texto original en inglés: "Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5." ([DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895), versión del 2026-06-03; consultado el 2026-11-19). Por conocimiento general, el tadalafilo inhibe la PDE5, lo que aumenta el GMP cíclico (cGMP) y produce vasodilatación.

Un vínculo con la biología del folículo piloso es posible en teoría, pero especulativo. La hipertricosis de Ambras es un trastorno genético raro, asociado a reordenamientos cromosómicos que afectan la regulación del gen TRPS1. No hay motivo para esperar que la inhibición de PDE5 corrija esa causa de fondo.

Además, la hipertricosis es un efecto adverso conocido de otros vasodilatadores, como el minoxidil. Esto genera la preocupación de que la vía del cGMP/óxido nítrico pudiera inducir crecimiento de vello en lugar de tratarlo. La dirección del efecto no está clara ni verificada. El puntaje alto del modelo (0,9998) no sustituye a la evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

El estado de mercado es **comercializado**: los datos compilados registran al menos 20 autorizaciones vigentes (la lista puede ser parcial). No se dispone del texto de indicación aprobada en los registros locales. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58124 | DROTAQ | 20 mg comp. rec. x 4 | No registrada |
| 52111 | TADAL 20 | 20 mg comp. rec. x 4 | No registrada |
| 57636 | TADALAFILO RICHET | 20 mg comp. x 4 | No registrada |
| 51691 | VIRILON MAX | 20 mg comp. rec. x 2 | No registrada |
| 51991 | MOMENTUM | 5 mg comp. rec. x 15 | No registrada |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron 132 interacciones. Entre las de nivel moderado figuran aprepitant, dexametasona, cimetidina, claritromicina, miconazol, clotrimazol y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina). También se listan lorcaserina, sapropterina y troglitazona (moderadas) y papaverina (leve).
- **Señal de seguridad relacionada con otra predicción**: un reporte de caso de 2006 (PMID 17059442) describe aura migrañosa asociada al tadalafilo, lo que sugiere un posible efecto adverso vinculado a la vasodilatación mediada por óxido nítrico/cGMP.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni publicaciones, y el mecanismo es especulativo. Existe además un riesgo teórico de que la vía de acción favorezca la hipertricosis en vez de tratarla.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica coherente con la causa genética (TRPS1)
- Estudios preclínicos (modelos de folículo piloso) que aclaren la dirección del efecto
- Revisión del prospecto aprobado en ANMAT para completar la información de seguridad
- Evaluación de la necesidad clínica y de la seguridad en una población pediátrica o con enfermedad genética rara

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

