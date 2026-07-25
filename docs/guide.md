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

## Cómo buscar un medicamento

<ol class="actionable-steps">
<li>Use el buscador en la parte superior de la página (los nombres genéricos de los principios activos coinciden mejor que los nombres comerciales).</li>
<li>O recorra la lista completa en <a href="{{ '/drugs/' | relative_url }}">Todos los Medicamentos</a>.</li>
<li>También puede navegar por nivel de evidencia: <a href="{{ '/evidence-high/' | relative_url }}">alta</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo predicción del modelo</a>.</li>
</ol>

---

## Cómo leer un informe

<p class="key-answer" data-question="¿Qué significan los niveles de evidencia L1 a L5?">
Cada informe de medicamento enumera las nuevas indicaciones predichas, y cada indicación lleva un
nivel de evidencia L1&ndash;L5. <strong>L1 significa que ya la respaldan múltiples ensayos clínicos
aleatorizados de fase 3; L5 significa solo predicción del modelo, sin evidencia en humanos.</strong>
Los criterios completos están en la página de
<a href="{{ '/methodology/' | relative_url }}">Metodología</a>.
</p>

| Si aparece | Significa | Acción sugerida |
|-----------|----------|------------------|
| L1 / L2 | Existe evidencia de ensayos clínicos | Revisar los registros NCT y PMID de origen |
| L3 / L4 | Evidencia observacional o preclínica | Tratarlo como una pista de investigación |
| L5 | Solo predicción del modelo | Únicamente para generar hipótesis; no sirve como referencia clínica |

---

## Citación y trazabilidad

Cada pieza de evidencia de un informe lleva un identificador trazable:

- **Número NCT**: enlaza al registro en ClinicalTrials.gov
- **PMID**: enlaza al registro en PubMed
- **DrugBank ID**: enlaza a los datos del fármaco y sus blancos terapéuticos

Antes de citar cualquier conclusión de esta plataforma, lea la literatura de origen para confirmar el contexto.

---

## Preguntas frecuentes

<p class="key-answer" data-question="¿Se pueden usar las predicciones en la práctica clínica?">
<strong>No.</strong> Las predicciones de esta plataforma son pistas de investigación, no consejo
clínico. Toda aplicación clínica del reposicionamiento de medicamentos debe pasar por una validación
completa mediante ensayos clínicos y por una revisión regulatoria.
</p>

<p class="key-answer" data-question="¿Por qué no encuentro un medicamento en particular?">
Para que se incluya en la predicción, un principio activo debe mapearse al vocabulario de DrugBank.
Los extractos herbales, las vacunas, los excipientes y otros ítems no catalogados por DrugBank no
aparecen en esta plataforma.
</p>

---

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
de empresa 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ARTxGNN es el sitio de Argentina de la línea de productos "TxGNN Drug Repurposing" de la empresa.
El mismo sistema está desplegado en 30 países y regiones, cada uno denominado `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, y así sucesivamente) en `{cc}txgnn.yao.care`.
Descripción del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN en sí fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado
en *Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 construyó
sobre ese modelo, y abarca la integración de los datos nacionales de registro de medicamentos, la
predicción dual por grafo de conocimiento y aprendizaje profundo, la gradación de evidencia con
PubMed / ClinicalTrials y la integración con la historia clínica electrónica mediante SMART on FHIR.

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
