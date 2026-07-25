---
layout: default
title: Descargas
nav_order: 94
permalink: /downloads/
description: "Descargas de datos abiertos de ARTxGNN: recursos FHIR, resultados de predicción e índice de búsqueda."
---

# Descargas

<div class="key-takeaway">
Las predicciones se publican en formato FHIR R4, listas para integrarse con sistemas de historia clínica electrónica.
</div>

---

## Recursos FHIR

Este sitio publica las predicciones como recursos FHIR R4, que las aplicaciones SMART on FHIR pueden consumir directamente:

| Recurso | Ruta | Descripción |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Declaración de capacidades del servidor FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Recursos de medicamentos |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Indicaciones predichas |
| Bundle | `/fhir/Bundle/all-predictions.json` | Todas las predicciones agrupadas |

---

## Índice de búsqueda

`/data/search-index.json` provee un índice de búsqueda de medicamentos e indicaciones para armar su
propia interfaz de consulta.

---

## Términos de uso

<ol class="actionable-steps">
<li>Los datos de este sitio son <strong>solo para referencia de investigación</strong> y no deben usarse como base para decisiones médicas.</li>
<li>Al citarlos, acredite a ARTxGNN (藥提醒科技有限公司) y cite el artículo original de TxGNN.</li>
<li>Los datos derivados siguen sujetos a los términos de licencia de cada fuente original (vea <a href="{{ '/sources/' | relative_url }}">Fuentes de Datos</a>).</li>
</ol>

---

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
de empresa 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ARTxGNN es el sitio de Argentina de la línea de productos "TxGNN Drug Repurposing" de la empresa.
El mismo sistema está desplegado en 30 países y regiones, cada uno denominado `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, y así sucesivamente) en `{cc}txgnn.yao.care`.
Descripción del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN en sí fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado
en *Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 construyó
sobre ese modelo, y abarca la integración de los datos nacionales de registro de medicamentos, la
predicción dual por grafo de conocimiento y aprendizaje profundo, la gradación de evidencia con
PubMed / ClinicalTrials y la integración con la historia clínica electrónica mediante SMART on FHIR.

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
