---
layout: default
title: Aciclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
drugbank_id: DB00787
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-11-20
description: "Aciclovir: nueva indicación predicha, queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Aciclovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Aciclovir: queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Aciclovir es un antiviral análogo de nucleósidos que se comercializa en Argentina en comprimidos, cápsulas, suspensión y liofilizado inyectable.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)**, pero no hay ensayos clínicos y las **2 publicaciones** recuperadas no estudian directamente esta enfermedad, por lo que la predicción carece de respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Aciclovir (traducción no oficial): «El aciclovir es un análogo sintético de nucleósido de purina con actividad inhibitoria in vitro e in vivo contra los virus del herpes simple tipo 1 (VHS-1) y tipo 2 (VHS-2) y el virus de la varicela-zóster (VVZ). La actividad inhibitoria del aciclovir es altamente selectiva debido a su afinidad por la enzima timidina cinasa (TK) codificada por el VHS y el VVZ.» Texto original en inglés: "Acyclovir is a synthetic purine nucleoside analogue with in vitro and in vivo inhibitory activity against herpes simplex virus types 1 (HSV-1), 2 (HSV-2), and varicella-zoster virus (VZV). The inhibitory activity of acyclovir is highly selective due to its affinity for the enzyme thymidine kinase (TK) encoded by HSV and VZV." ([DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4), versión del 2026-06-26; consultado el 2026-11-19). Por conocimiento general, aciclovir es un análogo de nucleósidos que, tras ser activado por la timidina quinasa viral, inhibe la ADN polimerasa de los herpesvirus (HSV, VZV).

La queratoconjuntivitis epitelial punteada puede tener causa viral (por ejemplo, HSV o adenovirus), por lo que existe un vínculo plausible solo en los casos de origen herpético. Los adenovirus carecen de timidina quinasa viral, por lo que no cabe esperar eficacia en ese contexto.

La literatura recuperada trata de queratoconjuntivitis microsporidial y de lipidosis corneal en pacientes con SIDA, dos cuadros que no responden a aciclovir. El puntaje alto del modelo no está respaldado por evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Serie de casos | Indian J Pathol Microbiol | Características de la queratoconjuntivitis microsporidial en una cohorte del este de la India; no evalúa aciclovir ni la enfermedad predicha |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Serie de casos | Am J Ophthalmol | Lipidosis corneal inducida por fármacos en dos pacientes con SIDA; no aborda la enfermedad predicha |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 15577 | LISOVYR 800 | comp.rec.x 20 | No registrada en los datos locales |
| 17127 | XICLOVIR 800 | comp.x 40 | No registrada en los datos locales |
| 17126 | XICLOVIR 800 | comp.x 20 | No registrada en los datos locales |
| 50570 | XICLOVIR | 400 mg comp. x 20 | No registrada en los datos locales |
| 49805 | VIROSTATIC 800 | comp.x 20 | No registrada en los datos locales |

La lista puede ser parcial: se registran al menos 20 autorizaciones, todas vigentes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen aciclovir en queratoconjuntivitis epitelial punteada; la literatura recuperada se refiere a otras enfermedades. Por ello el nivel de evidencia es L5 y el puntaje del modelo no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Definir si el cuadro predicho corresponde a casos de etiología herpética, único escenario con mecanismo plausible.
- Búsqueda dirigida de estudios clínicos de aciclovir en queratoconjuntivitis viral epitelial.
- Datos del mecanismo de acción y del prospecto aprobado por ANMAT (advertencias y contraindicaciones).
- Evaluar la vía de administración (por ejemplo, oftálmica), ya que las presentaciones locales son orales y un liofilizado inyectable.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «3. **Ausencia de datos regulatorios en Argentina**: El fármaco no cuenta con autorizaciones de comercialización registradas en Argentina (0 » | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «No se identificaron autorizaciones de comercialización vigentes (total de licencias: 0)» | Ya no aparece tras regenerar el informe (2026-11-16: The report was regenerated on 2026-11-16 with new predictions; this sentence is no longer on the page; antes: Corregido) | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

