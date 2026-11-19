---
layout: default
title: Levodopa
parent: Solo Predicción del Modelo (L5)
nav_order: 177
evidence_level: L5
indication_count: 1
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
last_modified_at: 2026-10-30
description: "Levodopa: nueva indicación predicha, Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Levodopa
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

## Levodopa: precursor de dopamina → Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumen en Una Frase

Levodopa es un precursor de la dopamina que se utiliza para reponer la dopamina estriatal en los trastornos parkinsonianos. El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Puntaje de Predicción TxGNN | 0,9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Levodopa (traducción no oficial): «La levodopa, el precursor metabólico de la dopamina, atraviesa la barrera hematoencefálica y presumiblemente se convierte en dopamina en el cerebro. Se cree que este es el mecanismo por el cual la levodopa alivia los síntomas de la enfermedad de Parkinson.» Texto original en inglés: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), versión del 2026-07-20; consultado el 2026-11-19). Según la información conocida, la levodopa es un precursor de la dopamina que se convierte en el cerebro en dopamina, lo que permite reponer la que falta en los trastornos parkinsonianos.

La encefalitis de Rasmussen es una enfermedad rara, unilateral y de origen inmunitario. Se caracteriza por citotoxicidad mediada por linfocitos T, activación microglial, atrofia progresiva de un hemisferio cerebral y convulsiones focales refractarias (epilepsia parcial continua).

El vínculo mecanístico es débil y se apoya solo en el puntaje de predicción (0,9906), que refleja cercanía entre datos del modelo y no una biología demostrada. Una conexión plausible sería la coincidencia de fenotipos neurológicos (trastornos del movimiento, compromiso de los ganglios basales) o de anotaciones neuroinflamatorias. No hay datos de que reponer dopamina modifique la patología inmunitaria ni la carga de convulsiones de esta enfermedad. Además, los agentes dopaminérgicos podrían empeorar teóricamente las convulsiones o los síntomas psiquiátricos en algunos pacientes, lo que exigiría una revisión de seguridad previa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

El fármaco figura como comercializado, con al menos 20 autorizaciones vigentes (la lista puede ser parcial). Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 37910 | PARKINEL 250/25 | 250 mg/25 mg comp. x 60 |
| 20074 | LECARGE | 250/25 mg comp. x 30 |
| 19636 | MADOPAR DISPERSABLE | 62,5 mg tab. dispers. x 100 |
| 11017 | LEBOCAR | 250/25 comp. x 60 |
| 49290 | SINEMET 250/25 | comp. x 50 |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel moderado figuran epinefrina, efedrina, bupropión, metronidazol, piridoxina, metoclopramida y varios anticolinérgicos (atropina, hioscianina, glicopirronio, diciclomina, metescopolamina, clidinio, mepenzolato). Los antiácidos (hidróxido de aluminio, carbonato de calcio, compuestos de magnesio) presentan interacciones de nivel menor, y el hierro, de nivel moderado.
- **Contraindicaciones**: no hay texto de prospecto disponible en los datos compilados; consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura sobre esta enfermedad, y con un vínculo mecanístico débil. Además, existe una posible preocupación de seguridad por el efecto de los dopaminérgicos sobre las convulsiones.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la levodopa
- Estudios preclínicos o de mecanismo que vinculen la reposición dopaminérgica con la patología de la encefalitis de Rasmussen
- Revisión de seguridad centrada en el riesgo de convulsiones y síntomas psiquiátricos
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

