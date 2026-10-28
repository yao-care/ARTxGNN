---
layout: default
title: Misoprostol
parent: Solo Predicción del Modelo (L5)
nav_order: 193
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Misoprostol: nueva indicación predicha, Amenorrea (nivel de evidencia L4). Indicación original: No disponible en los datos compilados"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Misoprostol: De Indicación Original No Especificada a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Misoprostol es un análogo de la prostaglandina E1 comercializado en Argentina; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero no hay **ensayos clínicos** registrados y las **7 publicaciones** recuperadas tratan sobre el manejo de embarazos (aborto médico, aborto retenido), no sobre el tratamiento de la amenorrea en sí.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las licencias de ANMAT no incluyen texto de indicación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9964 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información general conocida, misoprostol es un análogo de la prostaglandina E1 que induce contracciones uterinas y maduración cervical, y mecanísticamente podría relacionarse con causas de amenorrea vinculadas al embarazo (aborto retenido, embarazo anembrionario, restos ovulares).

Sin embargo, la relación es indirecta. Las publicaciones recuperadas describen el uso de misoprostol (con frecuencia combinado con mifepristona) para la interrupción médica del embarazo o el manejo del aborto retenido. En ellas la amenorrea aparece como criterio de inclusión (por ejemplo, embarazo de ≤35 días de amenorrea), no como la enfermedad tratada. Ningún estudio muestra que misoprostol restablezca la menstruación o trate la amenorrea primaria o secundaria.

Por lo tanto, el puntaje alto de TxGNN (0.9964) es solo una predicción computacional y no está respaldado por evidencia clínica directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reproductive Sciences | 744 mujeres con embarazo ultratemprano (amenorrea ≤35 días); evalúa eficacia, seguridad y aceptabilidad de mifepristona en dosis baja con misoprostol autoadministrado para aborto médico |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA (dosis-respuesta) | Reproductive Sciences | 2500 mujeres con embarazo ultratemprano; compara dosis decrecientes de mifepristona (150 a 50 mg) seguidas de 200 µg de misoprostol oral; criterio principal: aborto completo sin cirugía |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohorte | Human Reproduction | Prevención de embarazo no deseado con mifepristona en dosis baja más misoprostol antes de la menstruación esperada |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohorte | J Obstet Gynaecol Res | Seguridad y eficacia de mifepristona en dosis baja con misoprostol autoadministrado para terminación de embarazo temprano |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto retenido y del embarazo anembrionario |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Ablación endometrial en el manejo del sangrado uterino anormal; relación indirecta con misoprostol |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de caso | Cureus | Hígado graso agudo del embarazo; la amenorrea figura como síntoma de presentación, sin relación terapéutica con misoprostol |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 18299 | OXAPROST 75 | Comprimidos x 16 | No especificada en los datos |
| 10930 | OXAPROST | Comprimidos x 16 | No especificada en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no texto de prospecto)**: hipertensión, enfermedad hepática o insuficiencia hepática (incluida lesión hepática inducida por fármacos), enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, enfermedad cardiovascular y cardíaca, infarto de miocardio, trombosis coronaria, accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, trastornos de la coagulación, hemoglobinopatías, anemia (incluida la macrocítica), enfermedad inflamatoria intestinal, asma (intrínseco y alérgico), abuso o dependencia de sustancias, úlcera péptica activa y meningitis no infecciosa.
- **Interacciones Farmacológicas** (100 interacciones registradas; principales):
  - **Mayor**: dinoprostona (tópica).
  - **Moderada**: antiácidos con magnesio (óxido, carbonato e hidróxido de magnesio, magaldrato) y quinapril.
  - **Menor**: citrato de sodio, hidróxido de aluminio, carbonato de calcio, bicarbonato de sodio y naproxeno.
  - **Nivel no determinado**: goserelina, ciclosporina, cianocobalamina, calcitriol, ácido fólico, pravastatina, valsartán, ramipril y lorazepam.

No se dispone de advertencias ni contraindicaciones del prospecto de ANMAT; es necesario consultarlo.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura recuperada trata sobre la interrupción del embarazo, no sobre el tratamiento de la amenorrea. El puntaje de TxGNN es solo una predicción computacional (nivel L4). Además, el perfil de contraindicaciones y la falta de datos del prospecto impiden avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios que evalúen directamente misoprostol en amenorrea primaria o secundaria, y no solo en el contexto de embarazo.
- Definir si la indicación es clínicamente plausible, dado que el uso de un uterotónico en amenorrea requiere descartar embarazo y evaluar riesgos.

**Nota sobre la segunda predicción (coartación atípica de la aorta, puntaje 0.9930):** no hay ensayos ni literatura (nivel L5) y no se identificó un vínculo mecanístico claro. La prostaglandina E1 (alprostadil) se usa para mantener permeable el conducto arterioso, pero misoprostol no se utiliza con ese fin. La coartación es una anomalía estructural que requiere reparación quirúrgica o intervencionista. Se recomienda mantener **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

