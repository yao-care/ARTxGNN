---
layout: default
title: Evidencia Moderada (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Candidatos a reposicionamiento de medicamentos L3-L4 en ARTxGNN, respaldados por evidencia observacional o preclínica."
---

# Evidencia Moderada (L3-L4)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L3 | plus: site.data.drug_stats.level_counts.L4 %}
Esta página incluye **{{ pd_m }}** de los **{{ site.data.drug_stats.total_drugs }}** medicamentos con informe publicado en este sitio ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definición de los niveles: [Metodología]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos con evidencia preliminar que requieren validación adicional
</p>

---

## Criterios

| Nivel | Definición | Significado clínico |
|-------|------------|------------------|
| **L3** | Estudios observacionales / series de casos amplias | Respaldo preliminar; requiere validación adicional |
| **L4** | Estudios preclínicos / mecanísticos | Respaldo teórico; lejos del uso clínico |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ l3_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
