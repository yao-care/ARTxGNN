---
layout: default
title: Solo Predicción del Modelo (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidatos L5 en ARTxGNN: solo predicción del modelo, todavía sin evidencia clínica ni de literatura."
---

# Solo Predicción del Modelo (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Esta página incluye **{{ pd_m }}** de los **{{ site.data.drug_stats.total_drugs }}** medicamentos con informe publicado en este sitio ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definición de los niveles: [Metodología]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos con solo predicción del modelo y todavía sin evidencia en humanos
</p>

---

## Criterios

| Nivel | Definición | Significado clínico |
|-------|------------|------------------|
| **L5** | Solo predicción del modelo | Etapa de hipótesis; todavía sin evidencia en humanos |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ l5_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
