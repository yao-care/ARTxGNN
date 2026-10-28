---
layout: default
title: Mosapride
parent: Solo Predicción del Modelo (L5)
nav_order: 196
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Mosapride: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: Trastornos gastrointestinales (uso procinético"
monitor_inn: "MOSAPRIDE"
predicted_indications: ["insomnia (disease)"]
---

# Mosapride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Mosaprida: De Trastornos Gastrointestinales a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Mosaprida es un agonista selectivo del receptor 5-HT4, utilizado como procinético gastrointestinal para acelerar el vaciamiento gástrico en los países donde está autorizado.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos gastrointestinales (uso procinético; el texto de indicación no figura en las autorizaciones locales) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 10 de 10) |
| Número de Autorizaciones | 10 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Mosaprida es un agonista selectivo del receptor 5-HT4 (gen HTR4) con actividad procinética gastrointestinal. Su metabolito activo principal (M1) también presenta actividad antagonista sobre el receptor 5-HT3. Actualmente no se dispone de datos detallados y verificados sobre el mecanismo de acción dentro de los datos compilados para este informe.

Un vínculo plausible, pero no validado, pasaría por la modulación serotoninérgica del eje intestino-cerebro: las molestias gastrointestinales pueden alterar el sueño y la señalización por serotonina participa en la regulación del ciclo sueño-vigilia.

Sin embargo, no existe en los datos disponibles un mecanismo directo que conecte el agonismo 5-HT4 con una mejora del sueño, y este no es un mecanismo hipnótico reconocido. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no constituye evidencia clínica, y la predicción debe tratarse solo como generadora de hipótesis.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 31829 | VAGANTYL (Sidus) | 5 mg comprimidos recubiertos x 30 | No especificada |
| 42057 | GASTROKIN (Sanitas) | 5 mg comprimidos recubiertos x 30 | No especificada |
| 37453 | LEVUSID (Eurofarma) | 5 mg comprimidos x 30 | No especificada |
| 37452 | LEVUSID (Eurofarma) | 5 mg comprimidos x 20 | No especificada |
| 27070 | INTESUL (Beta) | 5 mg comprimidos recubiertos x 60 | No especificada |

Existen 10 autorizaciones vigentes en total, todas de monofármaco (también hay MOSAR de Elea y una presentación en gotas de VAGANTYL, 5 mg/ml x 20 ml).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la predicción es un puntaje computacional alto, sin ensayos clínicos, literatura ni mecanismo directo que la sustente (nivel L5). Además, no se dispone de información de seguridad del prospecto local.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura preclínica y clínica sobre receptores 5-HT4/5-HT3 y regulación del sueño
- Establecer una hipótesis mecanística verificable antes de plantear estudios exploratorios
- Evaluar la compatibilidad de vías de administración y el perfil de seguridad en la población con insomnio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

