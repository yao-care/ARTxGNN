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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Argentina: un ejemplo de este sitio

Leer un informe de este sitio supone tres comprobaciones, en este orden: nivel de evidencia, datos locales de mercado y registro de revisiones.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Abra [{{ gx.t }}]({{ gx.u | relative_url }}): la cabecera muestra el nivel de evidencia **{{ gx.l }}**; la nueva indicación principal predicha es **{{ gx.i }}**; los datos locales tienen **{{ gx.lt }}** productos del listado de PAMI, **{{ gx.lv }}** de ellos vigentes; el registro de revisiones de la página tiene **{{ gx.r }}** entradas.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Medicamentos con más entradas en el registro de revisiones: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Últimas correcciones del registro de revisiones: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Ejemplos de predicciones que ningún otro sitio TxGNN incluye para el mismo medicamento: [Insulina Glulisina]({{ '/drugs/insulina-glulisina/' | relative_url }}) → síndrome de disfunción sensible a tiamina.

<!-- local-facts:end -->

## Cómo buscar un medicamento

<ol class="actionable-steps">
<li>Use el buscador en la parte superior de la página (los nombres genéricos de los principios activos coinciden mejor que los nombres comerciales).</li>
<li>O recorra la lista completa en <a href="{{ '/drugs/' | relative_url }}">Todos los Medicamentos</a>.</li>
<li>También puede navegar por nivel de evidencia: <a href="{{ '/evidence-high/' | relative_url }}">alta</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo predicción del modelo</a>.</li>
</ol>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Cómo leer un informe

<p class="key-answer" data-question="¿Qué significan los niveles de evidencia L1 a L5?">
Cada indicación predicha lleva un nivel de <strong>L1</strong> (varios ensayos de fase 3) a <strong>L5</strong> (solo predicción del modelo). Cada evidencia cita un número NCT o PMID que se puede abrir; las predicciones son pistas de investigación, no consejo clínico. Definiciones y reglas: <a href="{{ '/methodology/' | relative_url }}">Metodología</a>.
</p>
<!-- local-condensed:end -->

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
