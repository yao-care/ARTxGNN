---
layout: default
title: Evidencia Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "16 medicamentos con nivel de evidencia L1–L2 en este sitio (Argentina), p. ej. Bromfenac, Bupropión, Dapsona, con la nueva indicación principal predicha, los productos del listado de PAMI y las revisiones de cada uno."
---

# Evidencia Alta (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Esta página incluye **{{ site.data.evidence_tier_facts.high.count }}** de los **{{ site.data.drug_stats.total_drugs }}** medicamentos con informe publicado en este sitio ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Proporción mediana en L1–L2 en los 30 sitios TxGNN: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Este sitio está por encima de la mediana.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Este sitio está por debajo de la mediana.{% else %}Este sitio está en la mediana.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
En los datos locales (productos del listado de PAMI), **{{ site.data.evidence_tier_facts.high.with_current }}** de estos medicamentos tienen al menos un registro vigentes, **{{ site.data.evidence_tier_facts.high.none_current }}** tienen registros pero ninguno vigentes y **{{ site.data.evidence_tier_facts.high.without_data }}** no figuran en los datos locales. **{{ site.data.evidence_tier_facts.high.with_reviews }}** tienen entradas en el registro de revisiones (correcciones de datos regulatorios en la página del medicamento). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** tienen una indicación predicha que ningún otro sitio TxGNN incluye para el mismo medicamento.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Con registros pero ninguno vigentes: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definición de todos los niveles: [Metodología]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} medicamentos)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nivel | Nueva indicación principal predicha | productos del listado de PAMI: vigentes / total | Registro de revisiones | Solo en este sitio |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sí ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} medicamentos)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nivel | Nueva indicación principal predicha | productos del listado de PAMI: vigentes / total | Registro de revisiones | Solo en este sitio |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sí ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
