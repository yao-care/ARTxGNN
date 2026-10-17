---
layout: default
title: Metodología
nav_order: 91
permalink: /methodology/
description: "Cómo ARTxGNN genera y valida sus predicciones: predicción por grafo de conocimiento TxGNN, recolección de evidencia, gradación L1-L5 y recomendaciones de decisión."
---

# Metodología

<div class="key-takeaway">
De la predicción por IA a la gradación de evidencia: cada candidato tiene una base trazable que respalda su calificación.
</div>

---

## Flujo general

<p class="key-answer" data-question="¿Cómo genera ARTxGNN sus predicciones?">
La plataforma utiliza un flujo de cuatro etapas: el modelo de grafo de conocimiento TxGNN predice
asociaciones potenciales entre fármacos y enfermedades, luego se recolecta automáticamente evidencia
para cada par predicho, la evidencia se gradúa de L1 a L5 y, por último, se emite una recomendación
de decisión.
</p>

<ol class="actionable-steps">
<li><strong>Predicción TxGNN</strong>: relaciones fármaco&ndash;enfermedad predichas con un grafo de conocimiento combinado con redes neuronales de grafos.</li>
<li><strong>Recolección de evidencia</strong>: para cada par predicho se reúne evidencia de ClinicalTrials.gov, PubMed, DrugBank y ANMAT.</li>
<li><strong>Gradación de evidencia</strong>: se gradúa de L1 a L5, donde L1 es la más sólida (múltiples ECA de fase 3) y L5 es solo predicción del modelo.</li>
<li><strong>Recomendación de decisión</strong>: Go, Proceed, Consider, Explore o Hold, según el nivel de evidencia.</li>
</ol>

---

## Criterios de gradación de evidencia

<table class="comparison-table">
<thead>
<tr><th>Nivel</th><th>Definición</th><th>Significado clínico</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Múltiples ECA de fase 3 / revisiones sistemáticas</td><td>Respaldo sólido; puede considerarse el uso clínico</td></tr>
<tr><td><strong>L2</strong></td><td>Un solo ECA o múltiples ensayos de fase 2</td><td>Respaldo moderado; pueden diseñarse ensayos de validación</td></tr>
<tr><td><strong>L3</strong></td><td>Estudios observacionales / series de casos amplias</td><td>Respaldo preliminar; requiere validación adicional</td></tr>
<tr><td><strong>L4</strong></td><td>Estudios preclínicos / mecanísticos</td><td>Respaldo teórico; lejos del uso clínico</td></tr>
<tr><td><strong>L5</strong></td><td>Solo predicción del modelo</td><td>Etapa de hipótesis; todavía sin evidencia en humanos</td></tr>
</tbody>
</table>

---

## Cómo se generan las predicciones

El modelo de aprendizaje profundo (DL) de TxGNN asigna una puntuación a cada par fármaco–enfermedad. Después se eliminan las indicaciones y contraindicaciones ya registradas para el fármaco en el grafo de conocimiento (KG) de TxGNN, de modo que las páginas de fármacos solo muestran nuevas indicaciones predichas con una puntuación de al menos 0,99 (hasta 10 por fármaco).

| Paso | Función |
|------|---------|
| Aprendizaje profundo (DL) | La red neuronal de grafos de TxGNN puntúa cada par fármaco–enfermedad |
| Verificación de usos conocidos (KG) | Elimina las indicaciones y contraindicaciones ya registradas en el grafo de conocimiento; no se cuentan como nuevas predicciones |
| Recopilación de evidencia | Busca en ClinicalTrials.gov y PubMed cada predicción restante y asigna un nivel de evidencia (L1–L5) |

---

## Integración de datos regulatorios

Los datos de aprobación de medicamentos de Argentina provienen de ANMAT. Los nombres de los
principios activos se mapean al vocabulario de DrugBank; los principios activos que no pueden
mapearse &mdash; extractos herbales, vacunas, excipientes y otros no catalogados por DrugBank &mdash;
quedan excluidos de la predicción.

---

## Limitaciones

<ol class="actionable-steps">
<li>Las predicciones son asociaciones estadísticas y <strong>no implican causalidad ni eficacia clínica</strong>.</li>
<li>Una calificación L5 significa solo predicción del modelo, sin evidencia en humanos que la respalde.</li>
<li>La recolección de evidencia depende de bases de datos públicas; los estudios no publicados o no indexados no quedan capturados.</li>
<li>El mapeo de principios activos puede omitir ítems por diferencias de nomenclatura.</li>
</ol>

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
predicción por aprendizaje profundo que excluye los usos ya registrados en el grafo de conocimiento, la gradación de evidencia con
PubMed / ClinicalTrials y la integración con la historia clínica electrónica mediante SMART on FHIR.

---

<div class="disclaimer">
<strong>Descargo de Responsabilidad</strong><br>
Este informe es solo para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Toda decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
