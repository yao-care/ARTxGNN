---
layout: default
title: Flurbiprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 149
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-20
monitor_inn: "flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Flurbiprofen: nueva indicación predicha, displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5)."
---

# Flurbiprofen
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

## Flurbiprofen: displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Flurbiprofeno es un antiinflamatorio no esteroideo que se comercializa en Argentina en varias presentaciones.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Flurbiprofen (traducción no oficial): «El flurbiprofeno tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción del flurbiprofeno, al igual que el de otros AINE, no se conoce por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Flurbiprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of flurbiprofen, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763), versión del 2026-10-05; consultado el 2026-11-19). Por conocimiento general, el flurbiprofeno inhibe las enzimas ciclooxigenasa (COX), lo que reduce la producción de prostaglandinas y, con ello, el dolor y la inflamación.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética muy poco frecuente, vinculada a la vía CDMP1/GDF5. No se identificó un vínculo mecanístico plausible: la inhibición de la COX no actúa sobre el defecto genético de fondo.

El puntaje elevado debe interpretarse como una señal computacional sin respaldo clínico ni mecanístico. En el mejor de los casos, un antiinflamatorio podría aliviar síntomas como el dolor, pero no modificaría la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 18400 | CLINADOL FORTE (Gador) | Comprimidos de 100 mg x 8 |
| 18401 | CLINADOL FORTE (Gador) | Comprimidos de 100 mg x 16 |
| 41619 | CLINADOL FORTE AP (Gador) | Comprimidos recubiertos de liberación prolongada de 200 mg x 8 |
| 45673 | CLINADOL COLUTORIO (Gador) | Frasco de 150 ml |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en los datos compilados** (no proviene del texto del prospecto): hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad ulcerosa péptica (incluida la activa), trastornos de la coagulación sanguínea, infarto de miocardio, trombosis coronaria, hemoglobinopatías, enfermedad cardiovascular y cardíaca, y abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: se registraron 352 interacciones. Entre las de nivel moderado figuran ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), metformina, glimepirida, clorpropamida, mesalazina, balsalazida y aprepitant. Famotidina, cimetidina y linaclotida son de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni publicaciones sobre esta enfermedad, no se identificó un vínculo mecanístico plausible y el puntaje alto parece un artefacto computacional. El perfil de seguridad del flurbiprofeno en una población con displasia esquelética tampoco está caracterizado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que conecte la COX con la vía CDMP1/GDF5
- Estudios preclínicos que respalden algún efecto sobre la enfermedad
- Revisión de las advertencias y contraindicaciones del prospecto de ANMAT

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

