---
layout: default
title: Labetalol
parent: Evidencia Moderada (L3-L4)
nav_order: 172
evidence_level: L4
indication_count: 4
---

# Labetalol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Labetalol: De Hipertensión a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Labetalol es un bloqueante adrenérgico combinado (alfa-1 y beta no selectivo), originalmente utilizado para el tratamiento de la hipertensión y los trastornos hipertensivos.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente no hay ensayos clínicos registrados y solo **1 publicación** (un reporte de caso de 1981) respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión (trastorno hipertensivo; según el grafo de conocimiento, ya que las autorizaciones locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, labetalol bloquea los receptores alfa-1 (provocando vasodilatación) y los receptores beta-adrenérgicos no selectivos (reduciendo la frecuencia cardíaca y la liberación de renina mediada por el sistema simpático). Su eficacia en la hipertensión está comprobada y se utiliza también en emergencias hipertensivas.

La hipertensión renovascular maligna es una forma grave de hipertensión con activación del sistema renina-angiotensina. Reducir la presión arterial y la liberación de renina mediada por receptores beta es biológicamente plausible en este contexto.

Es importante señalar que esta indicación es más bien un subtipo de la indicación ya existente que un reposicionamiento genuino. El puntaje alto del modelo probablemente refleja la cercanía en la ontología con la hipertensión. No se dispone de ningún ensayo o estudio directo en enfermedad renovascular.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Reporte de caso | The Medical Journal of Australia | Hombre de 20 años con hipertensión maligna asociada al consumo de drogas alucinógenas, con cambios arteríticos y aneurismas en vasos renales. Se usaron minoxidil y labetalol para el control inicial de la presión arterial, y la arteritis se resolvió con prednisona. |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 30277 | BIASCOR | 200 mg comprimidos x 20 | No especificada en los datos |
| 61054 | BIASCOR | 200 mg comprimidos x 60 | No especificada en los datos |
| 51245 | BLOCAMINE | 200 mg comprimidos x 20 | No especificada en los datos |
| 30278 | BIASCOR | 5 mg/ml ampollas x 10 x 4 ml | No especificada en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedad hepática, encefalopatía hepática y coma hepático, enfermedad renal, anuria, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, gota, hiperuricemia, hipotensión, bloqueo auriculoventricular, enfisema pulmonar y enfermedad bronquial, trastornos de ansiedad y neuróticos, distimia, hiperparatiroidismo, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, deficiencia de potasio, ictericia neonatal, piouréter y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las principales):
  - **Mayores**: epinefrina, dolasetrón.
  - **Moderadas**: hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, morfina, atropina, hiosciamina, metescopolamina, diciclomina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, fosfato de calcio, acetato de calcio.
  - **Menores**: ácido acetilsalicílico, óxido de magnesio.
- En el caso específico del uso en enfermedad pulmonar, el bloqueo beta no selectivo puede agravar el broncoespasmo, lo que es relevante para las indicaciones de hipertensión pulmonar también predichas.

Consultar el prospecto para obtener las advertencias y contraindicaciones oficiales, que no estaban disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha es un subtipo de la hipertensión, ya aprobada, por lo que no constituye un reposicionamiento genuino. El puntaje de TxGNN refleja principalmente la proximidad con la hipertensión, y la única evidencia disponible es un reporte de caso de 1981 sin ensayos clínicos. Las otras predicciones de mayor rango (nefropatía hipertensiva maligna e hipertensión pulmonar) tienen nivel L5, y para la hipertensión pulmonar el vínculo mecanístico es débil y existe un posible riesgo de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), ya que su ausencia impide el cribado de seguridad.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Confirmar si la indicación aprobada localmente ya cubre las crisis hipertensivas y la hipertensión maligna, lo que haría innecesario un nuevo reposicionamiento.
- Buscar estudios clínicos o series de casos específicos en hipertensión renovascular maligna.
- Evaluar la relevancia de las predicciones de hipertensión pulmonar solo si surge evidencia directa, dado el riesgo del bloqueo beta no selectivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

