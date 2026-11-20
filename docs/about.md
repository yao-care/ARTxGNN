---
layout: default
title: Acerca de
nav_order: 90
permalink: /about/
description: "ARTxGNN es una plataforma de predicción de reposicionamiento de medicamentos desarrollada por 藥提醒科技有限公司 (yao.care), construida sobre el modelo TxGNN de Harvard, que abarca los medicamentos del listado de PAMI en Argentina."
---

# Acerca de

<div class="key-takeaway">
Acelerar la validación de evidencia del reposicionamiento de medicamentos con IA: de la predicción a la evidencia de un vistazo.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Argentina: los datos de este sitio en cifras

Datos locales: [PAMI: Medicamentos para entidades](https://datos.pami.org.ar/dataset/medicamentos-para-entidades). Los datos locales son el listado de precios de PAMI «Medicamentos para entidades» (códigos ALFABETA). Que un producto ya no figure en el listado de PAMI no significa que su registro en ANMAT esté dado de baja: el estado del registro en ANMAT no está incluido en estos datos.

| Concepto | Valor |
|---|---|
| Medicamentos con informe publicado | {{ site.data.local_facts.drugs_total }} |
| Medicamentos presentes en los datos locales | {{ site.data.local_facts.licence.drugs_with_data }} |
| …con al menos un registro vigentes | {{ site.data.local_facts.licence.drugs_with_current }} |
| …con registros pero ninguno vigentes | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicamentos ausentes de los datos locales | {{ site.data.local_facts.licence.drugs_without_data }} |
| Registros locales (productos del listado de PAMI) | {{ site.data.local_facts.licence.items_total }} |
| …de ellos vigentes | {{ site.data.local_facts.licence.items_current }} |
| Entradas del registro de revisiones | {{ site.data.local_facts.reviews.records }} |
| Páginas con entradas de revisión | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Pares medicamento–enfermedad predichos que no figuran en ningún otro sitio TxGNN | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Medicamentos con más productos del listado de PAMI vigentes: {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Últimas correcciones del registro de revisiones: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Ejemplos de predicciones que ningún otro sitio TxGNN incluye para el mismo medicamento: [Candesartán]({{ '/drugs/candesartán/' | relative_url }}) → trastorno de migraña, [Beclometasona]({{ '/drugs/beclometasona/' | relative_url }}) → Eccema atópico, [Aniracetam]({{ '/drugs/aniracetam/' | relative_url }}) → insomnia (disease), [Acetilcarnitina]({{ '/drugs/acetilcarnitina/' | relative_url }}) → porfiria aguda intermitente, [Candesartán Cilexetil]({{ '/drugs/candesartán-cilexetil/' | relative_url }}) → Enfermedad renal hipertensiva maligna, [Carboximetilcisteína]({{ '/drugs/carboximetilcisteína/' | relative_url }}) → gota, [Ciprofibrato]({{ '/drugs/ciprofibrato/' | relative_url }}) → Deficiencia de la proteína de transferencia de ésteres de colesterol, [Idoxuridina]({{ '/drugs/idoxuridina/' | relative_url }}) → candidiasis vulvovaginal.

<!-- local-facts:end -->

## Antecedentes

<p class="key-answer" data-question="¿Qué es ARTxGNN?">
<strong>ARTxGNN</strong> es una plataforma de apoyo a la investigación en reposicionamiento de
medicamentos, construida sobre el modelo TxGNN publicado en <em>Nature Medicine</em> por el
Zitnik Lab de la Universidad de Harvard. Predice la ampliación de indicaciones de los medicamentos
del listado de medicamentos de PAMI en Argentina. Además de los puntajes de predicción de la IA, la plataforma
integra evidencia clínica de ClinicalTrials.gov y PubMed para que los investigadores puedan
evaluar rápidamente qué tan creíble es cada predicción.
</p>

---

## ¿Los datos son abiertos y gratuitos?

<p class="key-answer" data-question="¿Hay datos abiertos de predicciones de reposicionamiento de medicamentos que se puedan descargar gratis?">
Sí. Todas las predicciones de reposicionamiento de medicamentos de ARTxGNN y la evidencia clínica que las acompaña son datos abiertos: se publican gratuitamente en el sitio y como conjuntos de datos descargables, sin coste. Vea <a href="{{ '/sources/' | relative_url }}">Fuentes de Datos</a> para las licencias y formatos de descarga, y el repositorio público en <a href="https://github.com/yao-care/ARTxGNN">GitHub</a> para el código y los datos estructurados.
</p>

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Acerca del Desarrollador

Esta plataforma la desarrolla y opera **藥提醒科技有限公司** (yao.care, registro 83620786, Taichung, Taiwán) como uno de los 30 sitios por país y región de su línea de productos TxGNN ([presentación del producto](https://www.yao.care/medical/txgnn/)).

---

## El método en breve

Las predicciones provienen de TxGNN, un modelo de redes neuronales de grafos del Zitnik Lab de la Facultad de Medicina de Harvard (Huang et al., *Nature Medicine* 2024, [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)); cada indicación predicha se clasifica de L1 a L5 con ClinicalTrials.gov y PubMed. Modelo, niveles y reglas: [Metodología]({{ '/methodology/' | relative_url }}). Conjuntos de datos, descargas y licencias: [Fuentes de Datos]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

---

## Contacto

- **GitHub Issues**: <https://github.com/yao-care/ARTxGNN/issues>
- **Desarrollador**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Descripción del producto**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
