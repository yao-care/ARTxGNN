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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Argentina: datos de este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en el listado de precios de medicamentos de [PAMI: Medicamentos para entidades](https://datos.pami.org.ar/dataset/medicamentos-para-entidades) (Argentina).

Conjunto de datos: [PAMI: Medicamentos para entidades](https://datos.pami.org.ar/dataset/medicamentos-para-entidades); se descarga y se compara automáticamente cada semana (los lunes). Detalles: [Fuentes de Datos]({{ '/sources/' | relative_url }}).

Informes por nivel de evidencia:

| Nivel de evidencia | Informes | Proporción |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

1 pares medicamento–enfermedad predichos en este sitio no aparecen en ningún otro de los 30 sitios TxGNN.

<!-- site-data:end -->

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

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
