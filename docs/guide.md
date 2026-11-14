---
layout: default
title: Guía de Usuario
nav_order: 92
permalink: /guide/
description: "Guía de usuario de ARTxGNN: cómo buscar medicamentos, leer los niveles de evidencia e interpretar las recomendaciones."
---

# Guía de Usuario

<div class="key-takeaway">
Primero mire el nivel de evidencia, después la recomendación y por último lea la literatura de origen.
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

## Cómo buscar un medicamento

<ol class="actionable-steps">
<li>Use el buscador en la parte superior de la página (los nombres genéricos de los principios activos coinciden mejor que los nombres comerciales).</li>
<li>O recorra la lista completa en <a href="{{ '/drugs/' | relative_url }}">Todos los Medicamentos</a>.</li>
<li>También puede navegar por nivel de evidencia: <a href="{{ '/evidence-high/' | relative_url }}">alta</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo predicción del modelo</a>.</li>
</ol>

---

## Cómo leer un informe

<p class="key-answer" data-question="¿Qué significan los niveles de evidencia L1 a L5?">
Cada informe de medicamento enumera las nuevas indicaciones predichas, y cada indicación lleva un
nivel de evidencia L1&ndash;L5. <strong>L1 significa que ya la respaldan múltiples ensayos clínicos
aleatorizados de fase 3; L5 significa solo predicción del modelo, sin evidencia en humanos.</strong>
Los criterios completos están en la página de
<a href="{{ '/methodology/' | relative_url }}">Metodología</a>.
</p>

| Si aparece | Significa | Acción sugerida |
|-----------|----------|------------------|
| L1 / L2 | Existe evidencia de ensayos clínicos | Revisar los registros NCT y PMID de origen |
| L3 / L4 | Evidencia observacional o preclínica | Tratarlo como una pista de investigación |
| L5 | Solo predicción del modelo | Únicamente para generar hipótesis; no sirve como referencia clínica |

---

## Citación y trazabilidad

Cada pieza de evidencia de un informe lleva un identificador trazable:

- **Número NCT**: enlaza al registro en ClinicalTrials.gov
- **PMID**: enlaza al registro en PubMed
- **DrugBank ID**: enlaza a los datos del fármaco y sus blancos terapéuticos

Antes de citar cualquier conclusión de esta plataforma, lea la literatura de origen para confirmar el contexto.

---

## Preguntas frecuentes

<p class="key-answer" data-question="¿Se pueden usar las predicciones en la práctica clínica?">
<strong>No.</strong> Las predicciones de esta plataforma son pistas de investigación, no consejo
clínico. Toda aplicación clínica del reposicionamiento de medicamentos debe pasar por una validación
completa mediante ensayos clínicos y por una revisión regulatoria.
</p>

<p class="key-answer" data-question="¿Por qué no encuentro un medicamento en particular?">
Para que se incluya en la predicción, un principio activo debe mapearse al vocabulario de DrugBank.
Los extractos herbales, las vacunas, los excipientes y otros ítems no catalogados por DrugBank no
aparecen en esta plataforma.
</p>

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
