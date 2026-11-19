---
layout: default
title: Evidencia Moderada (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "25 medicamentos con nivel de evidencia L3–L4 en este sitio (Argentina), p. ej. Alprazolam, Beclometasona, Calcipotriol, con la nueva indicación principal predicha, los productos del listado de PAMI y las revisiones de cada uno."
---

# Evidencia Moderada (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Esta página incluye **{{ site.data.evidence_tier_facts.medium.count }}** de los **{{ site.data.drug_stats.total_drugs }}** medicamentos con informe publicado en este sitio ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Proporción mediana en L3–L4 en los 30 sitios TxGNN: {{ site.data.evidence_tier_facts.medium.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Este sitio está por encima de la mediana.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Este sitio está por debajo de la mediana.{% else %}Este sitio está en la mediana.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
En los datos locales (productos del listado de PAMI), **{{ site.data.evidence_tier_facts.medium.with_current }}** de estos medicamentos tienen al menos un registro vigentes, **{{ site.data.evidence_tier_facts.medium.none_current }}** tienen registros pero ninguno vigentes y **{{ site.data.evidence_tier_facts.medium.without_data }}** no figuran en los datos locales. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** tienen entradas en el registro de revisiones (correcciones de datos regulatorios en la página del medicamento). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** tienen una indicación predicha que ningún otro sitio TxGNN incluye para el mismo medicamento.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Con registros pero ninguno vigentes: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definición de todos los niveles: [Metodología]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} medicamentos)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nivel | Nueva indicación principal predicha | productos del listado de PAMI: vigentes / total | Registro de revisiones | Solo en este sitio |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sí ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} medicamentos)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nivel | Nueva indicación principal predicha | productos del listado de PAMI: vigentes / total | Registro de revisiones | Solo en este sitio |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sí ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
