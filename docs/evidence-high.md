---
layout: default
title: Evidencia Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidatos a reposicionamiento de medicamentos L1-L2 en ARTxGNN, respaldados por ensayos clínicos o revisiones sistemáticas."
---

# Evidencia Alta (L1-L2)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
Esta página incluye **{{ pd_m }}** de los **{{ site.data.drug_stats.total_drugs }}** medicamentos con informe publicado en este sitio ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definición de los niveles: [Metodología]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos que pueden priorizarse para evaluación clínica
</p>

¿Cuáles de estos medicamentos tienen evidencia de ensayos para su nueva indicación predicha y cuántos ensayos registrados se citan? Vea [Medicamentos del listado PAMI con evidencia de ensayos clínicos para una nueva indicación]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Criterios

| Nivel | Definición | Significado clínico |
|-------|------------|------------------|
| **L1** | Múltiples ECA de fase 3 / revisiones sistemáticas | Respaldo sólido; puede considerarse el uso clínico |
| **L2** | Un solo ECA o múltiples ensayos de fase 2 | Respaldo moderado; pueden diseñarse ensayos de validación |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ l1_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
