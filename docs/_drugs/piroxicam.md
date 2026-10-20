---
layout: default
title: Piroxicam
parent: Solo Predicción del Modelo (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Piroxicam: nueva indicación predicha, Síndrome de microftalmia colobomatosa con displasia rizomélica (nivel de evidencia L5). Indicación original: Artritis reumatoide y artrosis"
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
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

# Piroxicam: De Artritis Reumatoide a Síndrome de microftalmia colobomatosa con displasia rizomélica

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE), utilizado originalmente para el tratamiento de la artritis reumatoide y la artrosis.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa con displasia rizomélica**, un síndrome genético ultra raro del desarrollo.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, que se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide y artrosis (según el grafo de conocimiento; los registros locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 19 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Piroxicam es un AINE no selectivo que inhibe las enzimas COX-1 y COX-2, con lo que reduce la síntesis de prostaglandinas y, con ella, la inflamación y el dolor articular. Su eficacia en artritis reumatoide y artrosis está bien establecida.

**La predicción no tiene un fundamento mecanístico plausible.** La nueva indicación es una malformación ocular y esquelética del desarrollo, de origen genético. La inhibición de COX no puede corregir un defecto genético del desarrollo, y no se identificó ninguna relación farmacológica entre el mecanismo del fármaco y esta enfermedad.

El puntaje muy alto del modelo (99.996%) refleja una asociación computacional dentro del grafo de conocimiento, probablemente por vecindades compartidas con términos esqueléticos o de artropatía. No es evidencia biológica ni clínica. Como el mecanismo original tampoco está documentado, no es posible contrastar la predicción con la farmacología conocida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se registran 19 autorizaciones vigentes, todas de producto único (sin combinaciones) y ninguna cancelada. Los registros no incluyen texto de indicación aprobada. A continuación se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Laboratorio |
|---------|------|------|-----------|
| 5516 | SOLOCALM | 20 mg comprimidos x 40 | Laboratorios Be |
| 2824 | PIROXICAM DUPOMAR | 20 mg comprimidos x 10 | Siegfried |
| 2825 | PIROXICAM DUPOMAR | 20 mg comprimidos x 30 | Siegfried |
| 15483 | SOLOCALM GEL | Gel 1% envase x 30 g | Laboratorios Be |
| 2832 | PIROXICAM DUPOMAR | Gel x 50 g | Siegfried |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): hipertensión, enfermedad renal, enfermedad hepática (incluidas insuficiencia hepática aguda, hepatitis y lesión hepática inducida por fármacos), enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular, accidente cerebrovascular e infarto cerebral, trastornos de la coagulación, enfermedad trombótica, úlcera péptica activa, anemia y hemoglobinopatías, trastornos de la visión y ceguera, y abuso o dependencia de sustancias.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las listadas, las de nivel **moderado** incluyen:
  - ácido acetilsalicílico;
  - corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida);
  - metformina y sulfonilureas (clorpropamida, glimepirida);
  - mesalazina y balsalazida;
  - aprepitant;
  - sales de potasio (citrato y bicarbonato);
  - picosulfato y polietilenglicol con electrolitos.

  Las de nivel **menor** incluyen famotidina, ranitidina, cimetidina y linaclotida.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto pero carece de ensayos clínicos, de literatura y de un vínculo mecanístico plausible. Se trata de una enfermedad genética del desarrollo sobre la que un AINE no tendría efecto modificador. Además, el perfil de seguridad del fármaco (riesgos cardiovasculares, renales, hepáticos y gastrointestinales) no justifica explorar la indicación sin una base biológica.

**Para avanzar se necesita:**
- Un fundamento biológico que vincule la inhibición de COX con la fisiopatología de esta enfermedad, o bien descartar la predicción como artefacto del grafo.
- Datos del mecanismo de acción y del prospecto aprobado por ANMAT (advertencias y contraindicaciones oficiales).
- Estudios preclínicos, si se justifica una nueva evaluación.

**Nota adicional:** entre las demás predicciones del modelo, la **artritis idiopática juvenil** (puntaje 99.93%) es la única con literatura de respaldo. Incluye revisiones sistemáticas con metaanálisis en red de AINE y estudios pequeños y antiguos de piroxicam en niños. Su nivel de evidencia es L3, y se la podría evaluar como pregunta de investigación sobre el papel relativo de piroxicam entre los AINE. No es un candidato a nueva indicación, porque piroxicam no es un AINE pediátrico de primera línea y su vida media larga y su seguridad gastrointestinal en niños exigen cautela.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

