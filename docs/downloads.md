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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Argentina: qué contienen hoy los archivos

| Archivo | Contenido actual |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} medicamentos con sus indicaciones predichas |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} medicamentos con nivel de evidencia e indicación original |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} recursos MedicationKnowledge (uno por medicamento) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} recursos ClinicalUseDefinition (uno por indicación predicha) |

Reutilización del conjunto de datos local: [PAMI: Medicamentos para entidades](https://datos.pami.org.ar/dataset/medicamentos-para-entidades): Creative Commons Atribución 4.0 (CC BY 4.0), según el portal datos.pami.org.ar (https://datos.pami.org.ar/dataset/medicamentos-para-entidades).

{% if site.data.local_facts.top_licensed.size > 0 %}Medicamentos con más productos del listado de PAMI vigentes: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Últimas correcciones del registro de revisiones: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## FHIR, índice de búsqueda y reutilización

La declaración de capacidades FHIR R4 está en `/fhir/metadata`, todas las predicciones se agrupan en `/fhir/Bundle/all-predictions.json` y `/data/search-index.json` contiene los medicamentos e indicaciones del buscador del sitio. Los datos son solo de referencia para investigación; cite el sitio y el artículo de TxGNN, y revise la licencia de cada fuente en [Fuentes de Datos]({{ '/sources/' | relative_url }}).
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
