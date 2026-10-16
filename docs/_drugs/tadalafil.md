---
layout: default
title: Tadalafil
parent: Solo Predicción del Modelo (L5)
nav_order: 231
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Tadalafil: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: Hiperplasia prostática benigna (según el grafo de conocimiento"
monitor_inn: "tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tadalafilo: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Tadalafilo es un inhibidor de la fosfodiesterasa tipo 5 (PDE5), originalmente utilizado para la hiperplasia prostática benigna, la hipertensión pulmonar y la disfunción eréctil, entre otras indicaciones.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, tadalafilo es un inhibidor de PDE5: al bloquear esta enzima aumenta el GMP cíclico (cGMP), lo que produce vasodilatación. Su eficacia en disfunción eréctil, hiperplasia prostática benigna e hipertensión pulmonar está establecida.

Un vínculo posible, pero no verificado, es que el aumento de cGMP influya en la vasodilatación y la señalización folicular. Sin embargo, el síndrome de Ambras es un trastorno genético raro (reordenamientos en la región reguladora de *TRPS1*), por lo que es improbable que un inhibidor de PDE5 corrija la causa de fondo.

Además, la dirección del efecto es dudosa: otro vasodilatador, el minoxidil, puede causar hipertricosis. La predicción podría reflejar una asociación de tipo efecto adverso y no terapéutica. Las demás predicciones de mayor puntaje (hipertricosis, anomalías del tallo piloso, tricomegalia familiar) comparten el mismo vecindario de fenotipos capilares en el grafo, por lo que no constituyen apoyo independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Como dato contextual, para la octava predicción (migraña con aura de tronco encefálico) existe un único reporte de caso (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), 2006, *Cephalalgia*) que describe aura migrañosa típica sin cefalea asociada a tadalafilo. Esto sugiere un posible efecto desencadenante y no terapéutico.

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de monodroga, ninguna cancelada). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 58124 | DROTAQ | 20 mg comp. rec. x 4 | Baliarda |
| 52111 | TADAL 20 | 20 mg comp. rec. x 4 | Finadiet |
| 57636 | TADALAFILO RICHET | 20 mg comp. x 4 | Richet |
| 51991 | MOMENTUM | 5 mg comp. rec. x 15 | Panalab |
| 54338 | TADALAFILO TEVA | 5 mg comp. x 28 | Teva Argentina |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, epilepsia, estenosis aórtica y enfermedades de la válvula aórtica, trastornos hipotensivos, trastornos de la coagulación, síndrome coronario agudo, infarto de miocardio, accidente cerebrovascular y trastornos cerebrovasculares, anemia falciforme y hemoglobinopatías, mieloma de células plasmáticas, leucemia, priapismo, enfermedad de Peyronie, pérdida auditiva, y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas:** se identificaron 132 interacciones. Entre las de nivel moderado figuran aprepitant, dexametasona, lorcaserina, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, cimetidina, claritromicina, miconazol, clotrimazol, sapropterina y troglitazona. Papaverina es de nivel menor.
- **Señal relevante para la predicción:** el reporte de caso de aura migrañosa asociada a tadalafilo debe considerarse una señal de seguridad.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos ni literatura, y el mecanismo es dudoso: la vasodilatación podría empeorar, y no tratar, el exceso de vello. No hay base para avanzar con esta indicación.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción de tadalafilo (DrugBank).
- Descargar y analizar el prospecto de ANMAT para completar la revisión de seguridad.
- Revisar la literatura sobre PDE5/cGMP y el folículo piloso, y confirmar la dirección del efecto (terapéutico vs. adverso).
- Evaluar si otras predicciones de menor rango, como la cardiopatía kifoescoliótica (por extrapolación desde la hipertensión pulmonar), tienen un fundamento más sólido.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

