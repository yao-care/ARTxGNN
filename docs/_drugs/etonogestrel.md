---
layout: default
title: Etonogestrel
parent: Solo Predicción del Modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Etonogestrel: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones registradas"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Etonogestrel: De Indicación Original No Especificada a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Etonogestrel es un progestágeno (metabolito activo del desogestrel) comercializado en Argentina en forma de anillo vaginal; en los datos compilados no figura el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero no hay **ensayos clínicos** y la única publicación asociada no guarda relación con el fármaco ni con la enfermedad.
La predicción probablemente refleja un efecto farmacodinámico conocido (la amenorrea como efecto del fármaco) y no una indicación terapéutica real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones registradas |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, etonogestrel es un progestágeno que suprime la ovulación y adelgaza el endometrio.

La alta puntuación del modelo probablemente refleja una asociación farmacodinámica o de efecto adverso: la amenorrea es un efecto bien conocido de los métodos con etonogestrel. Sin embargo, usar un fármaco para inducir amenorrea (por ejemplo, para controlar el sangrado) es un objetivo distinto de tratar la amenorrea patológica, que normalmente exige corregir la causa subyacente (hipotalámica, hormonal o anatómica). Por ello, un vínculo terapéutico no está respaldado.

Otras predicciones del modelo TxGNN (aprendizaje profundo), todas con nivel L5, sin ensayos ni literatura, son enfermedad fibroquística de la mama (0.9961), adenosis apocrina de la mama (0.9929), adenosis de conductos romos de la mama (0.9929) y displasia mamaria benigna (0.9921). Su fundamento es débil: las puntuaciones provienen del modelo TxGNN (aprendizaje profundo) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Protocolo de ECA | Trials | Protocolo del estudio COVA sobre BIO101 para prevenir el deterioro respiratorio en COVID-19. No guarda relación con etonogestrel ni con amenorrea. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55887 | ELLERING | Anillo vaginal (sobre x 1) | No especificada |
| 51084 | CIRCLET | Anillo vaginal (sobre x 1) | No especificada |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (asociaciones fármaco-enfermedad del grafo de conocimiento, no texto del prospecto): hipertensión, epilepsia, trastornos de ansiedad y distimia, porfiria, enfermedad renal, enfermedad hepática y de la vesícula biliar, lupus eritematoso sistémico, asma, diabetes mellitus y cetoacidosis diabética, hipertrigliceridemia e hiperlipidemia, carcinoma de mama femenino, tromboflebitis, migraña, enfermedad arterial coronaria y obesidad.
- **Interacciones farmacológicas**: se identificaron 100 interacciones, de las que se muestran las principales, todas de nivel moderado: antidiabéticos (acarbosa, metformina, clorpropamida, glimepirida, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina), agonistas de GLP-1 (albiglutida, dulaglutida, semaglutida), insulinas (aspart, degludec, detemir, glargina, glulisina), aprepitant, claritromicina y linaclotida.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta solo en el modelo (L5), sin ensayos clínicos y con una única publicación irrelevante. Además, la amenorrea parece ser un efecto del fármaco y no un objetivo terapéutico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicación aprobada), indispensable para el cribado de seguridad
- Completar los datos del mecanismo de acción
- Definir si el objetivo es tratar la amenorrea patológica o inducir amenorrea de forma controlada (por ejemplo, control del sangrado)
- Realizar una búsqueda bibliográfica dirigida a etonogestrel y las afecciones mamarias benignas o los trastornos menstruales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

