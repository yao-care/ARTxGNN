---
layout: default
title: Flunitrazepam
parent: Evidencia Moderada (L3-L4)
nav_order: 146
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Flunitrazepam: nueva indicación predicha, Insomnio (nivel de evidencia L3). Indicación original: No disponible en los datos de ANMAT compilados"
---

# Flunitrazepam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Flunitrazepam: De Indicación Original No Registrada a Insomnio

## Resumen en Una Frase

Flunitrazepam es una benzodiazepina con efecto hipnótico-sedante, comercializada en Argentina, aunque los datos compilados no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero esta es una indicación ya establecida en el uso clínico del fármaco, por lo que no constituye un reposicionamiento genuino.
La evidencia consiste en **0 ensayos clínicos** y **10 publicaciones** (estudios clínicos pequeños, revisiones y estudios en animales).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de ANMAT compilados |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, flunitrazepam es una benzodiazepina que actúa como modulador alostérico positivo de los receptores GABA-A, lo que produce efectos sedantes e hipnóticos. Los datos farmacológicos compilados confirman su interacción con las subunidades α1, α2, α3 y α5 del receptor GABA-A, y describen su uso clínico en algunos casos de insomnio grave.

El insomnio es una indicación ya establecida de este fármaco en muchos países, por lo que la predicción del modelo es coherente con el uso conocido, pero no representa un hallazgo nuevo. La literatura incluye comparaciones clínicas con triazolam y zolpidem, revisiones polisomnográficas y reportes de insomnio de rebote tras la suspensión.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Estudio clínico | Sleep Med Rev | Los hipnóticos alteran el equilibrio corporal y la estabilidad al estar de pie; se asocian a caídas y fracturas de cadera |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | Estudio clínico | Eur Respir J | Efectos agudos de zolpidem, triazolam y flunitrazepam sobre gases arteriales y respiración en EPOC grave |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | Estudio clínico | JAMA | Insomnio de rebote tras suspender flunitrazepam, triazolam y nitrazepam |
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | Estudio clínico | La Nouvelle Presse Médicale | Acción de flunitrazepam en trastornos del sueño orgánicos y funcionales |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Revisión | Drugs | Revisión de triazolam en insomnio; lo considera más adecuado que hipnóticos de acción más larga como flunitrazepam |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Mayor respuesta a benzodiazepinas en ancianos, incluido flunitrazepam |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Uso clínico de hipnóticos y necesidad de contar con distintos perfiles farmacocinéticos |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | Estudio animal | Psychopharmacology | Efectos de tres hipnóticos sobre el ciclo sueño-vigilia en ratas con alteración del sueño |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49248 | MIRPAW | 1 mg comprimidos x 30 | No disponible |
| 16287 | ROHYPNOL | 1 mg comprimidos laqueados x 30 | No disponible |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: los datos compilados registran 4 interacciones farmacológicas con subunidades del receptor GABA-A (α1, α2, α3 y α5), que corresponden a su mecanismo de acción y no a interacciones con otros medicamentos.
- **Precauciones señaladas en la literatura**: dependencia, insomnio de rebote, potencial de abuso, alteración del equilibrio y de la respiración, y mayor sensibilidad en ancianos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El insomnio es un uso ya establecido de flunitrazepam y la literatura clínica lo respalda de forma consistente, aunque es antigua, de bajo grado y sin ensayos registrados. El perfil de riesgo (dependencia, abuso, depresión respiratoria) exige condiciones estrictas de uso.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT para confirmar la indicación aprobada, las advertencias y las contraindicaciones
- Completar los datos del mecanismo de acción en DrugBank
- Definir medidas de control en poblaciones de riesgo (ancianos, pacientes con EPOC, personas con antecedentes de abuso de sustancias)

**Otras predicciones del modelo (resumen):**
- **Delirium por abstinencia alcohólica** (L3, Research Question): existen reportes clínicos pequeños de flunitrazepam intravenoso (1979–1993), con respaldo mecanístico sólido pero evidencia específica antigua y de bajo grado.
- **Ansiedad y trastorno de ansiedad** (L3, Research Question): la literatura se centra en abuso, toxicidad y eventos adversos, sin estudios de eficacia específicos; primero debe evaluarse la seguridad.
- **Migraña (y variantes), agoraphobia, tortícolis paroxística benigna de la infancia y atrofodermia vermiculada** (L4–L5, Hold): solo hay predicción del modelo o evidencia indirecta, sin respaldo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

