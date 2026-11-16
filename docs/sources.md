---
layout: default
title: Fuentes de Datos
nav_order: 93
permalink: /sources/
description: "Fuentes de datos detrás de ARTxGNN: listado de medicamentos de PAMI, TxGNN, ClinicalTrials.gov, PubMed y DrugBank."
---

# Fuentes de Datos

<div class="key-takeaway">
Cada conclusión se remonta a una fuente de datos pública: nada es una caja negra.
</div>

---

## Panorama de las fuentes

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Se usa para</th></tr>
</thead>
<tbody>
<tr><td>Listado local de medicamentos</td><td><a href="https://datos.pami.org.ar/dataset/medicamentos-para-entidades">PAMI: Medicamentos para entidades</a></td><td>Medicamentos y principios activos de Argentina; estado en el listado de cada producto</td></tr>
<tr><td>Modelo de predicción</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Predicción de asociaciones fármaco&ndash;enfermedad</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Gradación de evidencia (NCT)</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Gradación de evidencia (PMID)</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mapeo de principios activos y datos de blancos terapéuticos</td></tr>
<tr><td>Interacciones</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Datos de interacciones entre fármacos</td></tr>
</tbody>
</table>

---

## Datos locales de este sitio

Los medicamentos de Argentina y su estado de mercado provienen del listado de precios de medicamentos
que publica PAMI en su portal de datos abiertos. Es un listado de cobertura y precios, **no** el registro sanitario de ANMAT: el estado del
registro en ANMAT no está incluido en estos datos.

| Ítem | Detalle |
|------|---------|
| Conjunto de datos | Medicamentos para entidades (listado de precios de medicamentos, CSV) |
| Publicador | PAMI, portal de datos abiertos datos.pami.org.ar |
| Descarga | <https://datos.pami.org.ar/dataset/medicamentos-para-entidades> (se toma el CSV más reciente del conjunto de datos) |
| Identificador de producto | Código ALFABETA |
| Actualización | Descarga automática semanal (cada lunes); un producto que deja de figurar en el listado conserva su estado anterior |

---

## Licencias

Cada fuente tiene su propia licencia; revísela antes de citar:

- **TxGNN**: uso académico; citar a Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: datos públicos de los NIH de Estados Unidos
- **DrugBank**: uso no comercial sujeto a sus términos de licencia
- **PAMI**: sujeto a los términos de uso del portal de datos abiertos datos.pami.org.ar

---

## Frecuencia de actualización

| Datos | Frecuencia |
|------|-----------|
| Listado de medicamentos de PAMI | Semanal (cada lunes) |
| Evidencia de ensayos / literatura | Se recolecta nuevamente en forma periódica |
| Datos de interacciones | Revisados trimestralmente |

---

## Citación académica

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
