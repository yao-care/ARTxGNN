---
layout: default
title: Formoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 3
monitor_inn: "FORMOTEROL"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
last_modified_at: 2026-10-30
description: "Formoterol: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Formoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Formoterol: agonista beta2 adrenérgico de acción prolongada → malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Formoterol es un agonista beta2 adrenérgico de acción prolongada que relaja el músculo liso de las vías respiratorias. El modelo TxGNN predice que podría ser útil para **malformación respiratoria (respiratory malformation)**, pero actualmente **no hay ensayos clínicos** registrados y ninguna de las publicaciones recopiladas estudia directamente esta enfermedad, por lo que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según la información conocida, formoterol es un agonista beta2 adrenérgico de acción prolongada: activa la señalización de AMPc y relaja el músculo liso bronquial.

En teoría, este efecto podría aliviar la obstrucción del flujo de aire secundaria a anomalías estructurales de las vías respiratorias. Sin embargo, no hay evidencia de que formoterol modifique la malformación subyacente; solo podría actuar sobre el síntoma obstructivo.

El puntaje elevado (0,9992) refleja la proximidad en la red del modelo con nodos de enfermedades respiratorias, no datos específicos de esta enfermedad. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Las publicaciones recopiladas tratan sobre EPOC, asma y otras condiciones respiratorias; ninguna estudia directamente la malformación respiratoria. Se listan como contexto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Revisión sistemática y metaanálisis | J Am Pharm Assoc | Seguridad y eficacia de budesonida/glicopirronio/formoterol frente a glicopirronio/formoterol en EPOC |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | ECA cruzado | Eur Respir J | Budesonida/formoterol frente a salbutamol en asma estable |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | ECA | J Allergy Clin Immunol | Seguridad a largo plazo de budesonida/formoterol en pacientes afroamericanos con asma |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Budesonida/formoterol en inhalador presurizado para asma persistente |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Estudio de cohorte/fisiología | Eur J Appl Physiol | Respuestas compensatorias a la carga mecánica en EPOC durante el sueño |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Estudio mecanístico clínico | Eur Respir J | Formoterol protege frente a los efectos del factor activador de plaquetas en asma |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Reporte de caso | J Med Case Rep | Enfermedad de vía aérea pequeña en síndrome post-COVID-19 |

## Información de Mercado en Argentina

Formoterol figura como comercializado en Argentina, con al menos 20 autorizaciones vigentes (la lista puede ser parcial). Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 20365 | OXIS TURBUHALER | 9 mcg, envase x 60 dosis |
| 28199 | SYMBICORT TURBUHALER | 160/4,5 mcg, 120 dosis |
| 43180 | FREVIA | 160/4,5 mcg, 120 dosis |
| 57938 | NEUMOTEROL AEROSOL | 160/4,5, 120 dosis |
| 49181 | HEXALER BRONQUIAL DUO | 200/10 mcg, cápsulas para inhalar x 60 |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las de nivel moderado figuran acarbosa, famotidina, claritromicina, cisaprida, dolasetrón, efedrina, isometepteno, dietilpropión y varios antidiabéticos (albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina). Con corticoides (beclometasona, betametasona, budesonida, dexametasona) las interacciones son de nivel menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen directamente formoterol en malformación respiratoria; el puntaje alto del modelo no basta como respaldo. Por ello el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de ANMAT
- Definir qué población y vía de administración serían relevantes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

