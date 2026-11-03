---
layout: default
title: Noticias de salud
nav_order: 30
permalink: /news/
has_children: true
description: "Health news coverage tracked by ARTxGNN for its drugs and indications."
---

# Noticias de salud

<div class="key-takeaway">
Automatically tracked news coverage for the drugs and predicted indications on this site.
</div>

---

## All coverage

{% assign items = site.news | where_exp: "n", "n.layout != 'id_redirect'" | sort: 'title' %}
{% if items.size == 0 %}
No matching coverage yet.
{% else %}
{% for item in items %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
{% endif %}

---

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
