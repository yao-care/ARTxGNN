---
layout: default
title: Medicamentos en Argentina con ensayos para nueva indicación
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Medicamentos del listado PAMI cuya nueva indicación predicha por TxGNN tiene evidencia de ensayos clínicos (L1-L2): indicación, nivel y ensayos."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答「阿根廷的藥裡，哪些有新適應症的臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字：
收錄＝公開藥物頁（排除轉址頁與 noindex 頁）中 evidence_level 為 L1 或 L2（methodology 的定義：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁 Resumen 表；試驗數＝該藥物頁引用的不重複 NCT 編號數。
清單來源是 PAMI 給付價格清單，不是 ANMAT 註冊，頁面用「listado PAMI」不說「aprobado」。
{%- endcomment -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Medicamentos del listado PAMI con evidencia de ensayos clínicos para una nueva indicación

<p class="key-answer" data-question="¿Qué medicamentos disponibles en Argentina tienen evidencia de ensayos clínicos para una nueva indicación?">
<strong>{{ trial_drugs.size }}</strong> de los {{ listed.size }} medicamentos con informe en ARTxGNN tienen una nueva indicación predicha por TxGNN con nivel de evidencia <strong>L1 o L2</strong> ({{ l1.size }} en L1, {{ l2.size }} en L2), es decir, se encontró evidencia de ensayos clínicos (ensayos aleatorizados, ensayos de fase 2–3 o revisiones sistemáticas).
</p>

Los medicamentos provienen del listado [PAMI: Medicamentos para entidades](https://datos.pami.org.ar/dataset/medicamentos-para-entidades) (un listado de cobertura y precios; el estado del registro en ANMAT no está incluido en estos datos), y la lista refleja los informes de medicamentos actualizados por última vez el {{ latest_date }}.

<div class="key-takeaway">
La evidencia de ensayos para una indicación predicha no demuestra eficacia. Todos los candidatos de esta lista <strong>requieren validación clínica</strong> y revisión regulatoria antes de cualquier uso clínico.
</div>

---

## Medicamentos con evidencia de ensayos (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Medicamento</th><th>Nueva indicación predicha</th><th>Nivel de evidencia</th><th>Ensayos registrados citados (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign qo = drug.content | split: "<td>Nueva Indicación Predicha</td>" -%}
{%- assign indication = "" -%}
{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}
{%- assign lv = drug.content | split: "<td>Nivel de Evidencia</td>" -%}
{%- assign level_cell = "" -%}
{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}ver informe{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(con salvedad)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Cómo leer esta lista

- **Nivel de evidencia** sigue la [metodología]({{ '/methodology/' | relative_url }}): L1 = múltiples ECA de fase 3 o revisiones sistemáticas; L2 = un solo ECA o múltiples ensayos de fase 2. «(con salvedad)» indica que el informe matiza el nivel; lea la nota del informe antes de basarse en él.
- **Nueva indicación predicha** es la predicción principal de cada informe. Se excluyen las indicaciones y contraindicaciones ya registradas en el grafo de conocimiento de TxGNN, por lo que algunas predicciones pueden coincidir con un uso ya establecido; el informe lo explica cuando corresponde.
- **Ensayos registrados citados** cuenta los números de ClinicalTrials.gov (NCT) citados en el informe. Los informes citan una selección de los ensayos encontrados; 0 significa que el informe no cita ningún ensayo registrado, y su sección de evidencia bibliográfica muestra el fundamento del nivel.
- Para todos los niveles, vea [Evidencia Alta (L1-L2)]({{ '/evidence-high/' | relative_url }}) y [Todos los Medicamentos]({{ '/drugs/' | relative_url }}).

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
