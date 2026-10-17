---
layout: default
title: Salmeterol
parent: Evidencia Alta (L1-L2)
nav_order: 227
evidence_level: L1
indication_count: 7
last_modified_at: 2026-10-13
description: "Salmeterol: nueva indicación predicha, Bronquitis (nivel de evidencia L1). Indicación original: Enfisema pulmonar, asma intrínseca y asma alérgica"
monitor_inn: "SALMETEROL"
predicted_indications: ["bronchitis", "respiratory malformation", "obstructive lung disease", "Rienhoff syndrome", "asthma-related traits, susceptibility to", "atopic eczema"]
---

# Salmeterol
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **7** 
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

# Salmeterol: De Enfisema Pulmonar y Asma a Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista beta2-adrenérgico de acción prolongada, originalmente utilizado para el tratamiento del enfisema pulmonar y del asma (intrínseca y alérgica).
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe aclarar que esta indicación forma parte de la misma familia de enfermedades (EPOC/enfermedad pulmonar obstructiva), por lo que se trata más de una extensión que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfisema pulmonar, asma intrínseca y asma alérgica (según las indicaciones originales registradas en el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico establecido, salmeterol es un agonista beta2-adrenérgico de acción prolongada que relaja el músculo liso de las vías aéreas y produce broncodilatación sostenida. Además, podría favorecer la depuración mucociliar.

La bronquitis crónica es un fenotipo de la EPOC, muy cercano a la indicación original de enfisema pulmonar. Por ello, la predicción es en gran medida una extensión dentro de la misma familia de enfermedades. Un estudio publicado sobre depuración mucociliar y de la tos en bronquitis crónica respalda un mecanismo plausible.

Cabe señalar que, en la mayoría de los ensayos clínicos, salmeterol se evaluó en combinación con fluticasona o como comparador activo, por lo que parte de la evidencia es indirecta.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Tiotropio, salmeterol en aerosol y placebo durante 6 meses en EPOC; comparación directa de eficacia broncodilatadora y seguridad |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Salmeterol/fluticasona 50/500 mcg vs. placebo durante 13 semanas; efecto antiinflamatorio bronquial en EPOC |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Fase 3 | Completado | 122 | Seguridad a largo plazo (56 semanas) de salmeterol/fluticasona 50/500 µg en EPOC (bronquitis crónica y enfisema) |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Comparación de dos medicamentos en EPOC durante hasta 18 semanas; relevancia por confirmar por título poco informativo |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Fase 3 | Completado | 799 | Seguridad crónica de arformoterol durante 12 meses en EPOC; salmeterol probablemente como control activo (evidencia indirecta) |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Efecto broncodilatador de arformoterol durante 12 semanas; salmeterol probablemente como comparador activo |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | Búsqueda de dosis de fluticasona/formoterol frente a Advair Diskus en EPOC; salmeterol solo como referencia |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Fase 4 | Desconocido | 20 | Arformoterol nebulizado vs. salmeterol en polvo seco en EPOC; estudio pequeño en un solo centro |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | NA | Terminado | 20 | Expresión de mediadores inflamatorios en esputo inducido como biomarcador de respuesta a fármacos en EPOC; exploratorio |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | ECA/Mecanístico | Pulm Pharmacol Ther | Efecto agudo de salmeterol vs. placebo sobre la depuración mucociliar y de la tos en bronquitis crónica leve a moderada (n=14) |
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | ECA | Thorax | Efecto de salmeterol/fluticasona sobre la inflamación de las vías aéreas en EPOC |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Metaanálisis | Respir Res | Resultados mejorados con salmeterol 50 mcg dos veces al día frente a placebo/tratamiento habitual en EPOC |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | Ensayo clínico | Chest | Eficacia y seguridad de fluticasona 250 µg/salmeterol 50 µg en Diskus frente a placebo y componentes individuales en EPOC |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Revisión | Drugs | Uso de salmeterol/fluticasona en EPOC; aprobado en EE. UU. para EPOC asociada a bronquitis crónica |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Ensayo clínico | Ther Adv Respir Dis | Seguridad y tolerancia de arformoterol y salmeterol durante un año en EPOC |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | Ensayo abierto | Clin Ther | Salmeterol inhalado vs. teofilina oral en EPOC leve a moderada: eficacia, tolerabilidad y calidad de vida |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte | Curr Med Res Opin | Uso de servicios de salud y costos en bronquitis crónica con fluticasona/salmeterol vs. otras terapias de mantenimiento |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía | Basic Clin Pharmacol Toxicol | Guía finlandesa de diagnóstico y farmacoterapia de la EPOC estable |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Revisión | Br J Clin Pharmacol | Antagonismo de la agonía beta2 de acción prolongada; efecto ahorrador de corticoide en asma |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43666 | PROAIR BRONQUIAL | 250/25 mcg aerosol x 120 dosis | No disponible en los datos |
| 54355 | VETALONE | 250/25 mcg aerosol x 120 dosis | No disponible en los datos |
| 45233 | PROAIR BRONQUIAL 500/50 | Cápsulas para inhalación x 60 + aplicador | No disponible en los datos |
| 47968 | FLUTIVENT HFA | 250/25 mcg x 120 dosis | No disponible en los datos |
| 26250 | SERETIDE DISKUS | 50/500 mcg x 60 dosis | No disponible en los datos |

Se registran 20 autorizaciones vigentes, todas de productos de principio activo único (salmeterol asociado a fluticasona según los nombres comerciales), sin autorizaciones canceladas. Se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): hipertensión, síndrome de QT largo (incluida la forma familiar), epilepsia, hiperglucemia, queratitis por herpes simple, osteoporosis, enfermedades del timo y varias deficiencias hipofisarias o hipogonadismos hipogonadotrópicos (por ejemplo, síndrome de Kallmann, síndrome de Sheehan). Estas relaciones deben verificarse contra el prospecto.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales:
  - **Mayor**: claritromicina.
  - **Moderada**: acarbosa, isometepteno, famotidina, epinefrina, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dietilpropión, dolasetrón, dulaglutida, empagliflozina.
  - **Menor**: corticoides como hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona y budesonida.
- **Advertencia de clase (según las revisiones Cochrane de la evidencia)**: en asma, los agonistas beta2 de acción prolongada en monoterapia se asocian con mayor riesgo de eventos adversos graves; deben usarse siempre junto con un corticoide inhalado.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados (con comparación directa de salmeterol en EPOC) y numerosas publicaciones respaldan su uso en enfermedad pulmonar obstructiva, incluida la bronquitis crónica. Sin embargo, la indicación es una extensión dentro de la misma familia de enfermedades y parte de la evidencia es indirecta, por lo que se requieren salvaguardas de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Confirmar que la indicación de bronquitis queda cubierta por la indicación de EPOC ya aprobada localmente (los textos de indicación de las autorizaciones están vacíos).
- Verificar los títulos truncados o poco informativos (NCT00268177, NCT00269126) y la relevancia de los ensayos donde salmeterol es solo comparador.
- Definir directrices de uso en combinación con corticoide inhalado y evaluar las contraindicaciones cardiovasculares (hipertensión, QT largo) y las interacciones relevantes (por ejemplo, claritromicina).

---

### Otras indicaciones predichas (referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Decisión |
|------|------|------|------|
| Enfermedad pulmonar obstructiva | 99.89% | L1 | Proceed with Guardrails (coincide con las indicaciones ya aprobadas) |
| Asma | 99.78% | L1 | Proceed with Guardrails (indicación ya aprobada; usar siempre con corticoide inhalado) |
| Eccema atópico | 99.39% | L4 | Research Question (solo evidencia mecanística y preclínica) |
| Malformación respiratoria | 99.91% | L4 | Hold (sin vínculo mecanístico claro) |
| Síndrome de Rienhoff | 99.89% | L5 | Hold (solo predicción computacional) |
| Rasgos relacionados con asma (susceptibilidad) | 99.52% | L5 | Hold (rasgo genético, sin datos clínicos) |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

