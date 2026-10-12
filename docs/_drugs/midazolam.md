---
layout: default
title: Midazolam
parent: Evidencia Moderada (L3-L4)
nav_order: 189
evidence_level: L3
indication_count: 1
---

# Midazolam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Midazolam: De Ansiedad a Insomnio

## Resumen en Una Frase

Midazolam es una benzodiazepina de acción corta, originalmente utilizada para el tratamiento de la ansiedad.
El modelo TxGNN predice que podría ser efectivo para **insomnio**,
con **2 ensayos clínicos** (ambos de relevancia indirecta o nula) y **10 publicaciones** (de las cuales 4 son ensayos aleatorizados específicos de midazolam en trastornos del sueño) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ansiedad (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, midazolam es una benzodiazepina que modula positivamente los receptores GABA-A, aumentando la neurotransmisión inhibitoria. Esto produce efectos sedantes e hipnóticos.

La ansiedad y el insomnio comparten una base de hiperactivación del sistema nervioso central, y ambos responden a la potenciación de la inhibición GABAérgica. Por ello, el mecanismo de clase es coherente con el uso en insomnio. De hecho, midazolam por vía oral fue estudiado históricamente como hipnótico (estudios de las décadas de 1980 y 1990), por lo que esta predicción se parece más a un restablecimiento de un uso conocido que a un reposicionamiento novedoso.

Las preocupaciones principales son la vida media corta (posible insomnio de rebote), la tolerancia, la dependencia, el deterioro al día siguiente y una gran carga de interacciones farmacológicas.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Compara la calidad del sueño posoperatorio tras sedación con dexmedetomidina vs. midazolam en resección transuretral de próstata. Evidencia indirecta (contexto perioperatorio, no insomnio primario). |
| [NCT00886314](https://clinicaltrials.gov/study/NCT00886314) | No aplica | Desconocido | 80 | Payasos médicos vs. premedicación sedante (midazolam) para reducir la ansiedad preoperatoria en niños. No es relevante para insomnio. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | ECA | J Clin Psychopharmacol | Estudio multicéntrico, doble ciego, de sueño, rendimiento y niveles plasmáticos en insomnes crónicos durante 14 días con flurazepam vs. midazolam. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA | J Clin Psychopharmacol | Resumen ejecutivo del estudio multicéntrico anterior (flurazepam vs. midazolam en insomnes crónicos). |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | ECA | Br J Clin Pharmacol | Midazolam 15 mg vs. Vesparax en 30 mujeres con insomnio secundario a enfermedad neuromuscular; ambos fueron hipnóticos eficaces, y midazolam fue mejor tolerado y sin resaca. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | ECA | Arzneimittel-Forschung | Estudio piloto de búsqueda de dosis (10–30 mg por vía oral) en 75 pacientes hospitalizados con insomnio leve a moderado. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Indicaciones de uso de hipnóticos y necesidad de variedad de benzodiazepinas con distintos perfiles farmacocinéticos. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Revisión | Orv Hetil | Revisión sobre insomnio e hipoperfusión cerebral (contexto general, sin midazolam específico). |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 32660 | REM CHOBET | 15 mg/3 ml, ampollas x 2 | No disponible |
| 52500 | REM CHOBET | 15 mg, comprimidos x 30 | No disponible |
| 30321 | REM CHOBET | 50 mg/10 ml, ampollas x 25 | No disponible |
| 52499 | REM CHOBET | 15 mg, comprimidos x 10 | No disponible |
| 52501 | REM CHOBET | 15 mg, comprimidos x 50 | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** enfermedad pulmonar obstructiva crónica (incluida la de inicio temprano grave), cirrosis hepática, glaucoma de ángulo cerrado, enfermedad renal crónica, insuficiencia renal crónica e insuficiencia renal terminal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total. Entre las listadas, de nivel moderado: ranitidina, bupropión, aprepitant, morfina, omeprazol, cimetidina, claritromicina, dronabinol, eluxadolina, teduglutida, nabilona, metoclopramida, miconazol, clotrimazol y glicerol fenilbutirato. De nivel menor: dexametasona, betametasona, óxido de magnesio, hidróxido de aluminio y carbonato de calcio. Cabe destacar los inhibidores de CYP3A4 y los depresores del sistema nervioso central.
- **Riesgos de clase a considerar:** tolerancia, dependencia, insomnio de rebote y deterioro al día siguiente.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de clase es coherente, y existen varios ensayos aleatorizados históricos de midazolam oral en insomnio, pero son antiguos y los ensayos clínicos registrados aportan solo evidencia indirecta. Dado el perfil de riesgo (dependencia, interacciones, contraindicaciones respiratorias, hepáticas y renales), se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas), que hoy es un vacío de información bloqueante.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Verificar si la indicación de insomnio ya figura en las autorizaciones locales (las formas orales de 15 mg) y la compatibilidad de vías de administración.
- Revisar críticamente los ensayos históricos de midazolam oral en insomnio y definir si se requieren estudios modernos.
- Plan de manejo de riesgos: control de dependencia, duración limitada de tratamiento, revisión de interacciones con inhibidores de CYP3A4 y depresores del SNC, y precaución en pacientes con EPOC, cirrosis, glaucoma de ángulo cerrado o enfermedad renal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

