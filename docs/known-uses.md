---
layout: default
title: "Solo usos conocidos (sin nuevas predicciones)"
nav_order: 24
permalink: /known-uses/
description: "En estos medicamentos, todos los candidatos del modelo TxGNN ya son usos conocidos (registrados en el grafo de conocimiento o en un registro sanitario), po…"
---

# Solo usos conocidos (sin nuevas predicciones)

En estos medicamentos, todos los candidatos del modelo TxGNN ya son usos conocidos (registrados en el grafo de conocimiento o en un registro sanitario), por lo que no hay ninguna nueva indicación predicha. Cada página muestra los usos conocidos y la situación de comercialización local.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} medicamentos**

| Medicamento | Informe |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Ver página]({{ drug.url | relative_url }}) |
{% endfor %}
