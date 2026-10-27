---
layout: default
title: Dimenhydrinate
parent: Evidencia Moderada (L3-L4)
nav_order: 127
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-13
description: "Dimenhydrinate: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Vértigo de origen en el sistema nervioso central"
monitor_inn: "dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

## Dimenhidrinato: De Vértigo de Origen en el Sistema Nervioso Central y Cinetosis a Urticaria Alérgica
{: .text-alpha }

## Resumen en Una Frase

El dimenhidrinato es un antihistamínico de primera generación (sal de difenhidramina y 8-cloroteofilina), utilizado originalmente para el vértigo de origen central y la cinetosis (mareo por movimiento).
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**,
pero por ahora solo hay **1 publicación** relacionada (un estudio farmacocinético preliminar en perros) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vértigo de origen en el sistema nervioso central; cinetosis (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El dimenhidrinato es una sal de difenhidramina y 8-cloroteofilina. Tras su administración, el componente activo principal es la difenhidramina, un antagonista del receptor H1 de primera generación. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los registros compilados para este informe, por lo que el razonamiento se apoya en la farmacología conocida de la difenhidramina y no en datos específicos del dimenhidrinato.

El bloqueo del receptor H1 reduce los habones, el eritema y el prurito mediados por histamina. Este es el fundamento establecido para el uso de antihistamínicos de primera generación en la urticaria alérgica. Por ello, el vínculo mecanístico es plausible y farmacológicamente coherente, aunque se trata de una inferencia a partir del componente difenhidramina.

La relación con las indicaciones originales (vértigo y cinetosis) es indirecta: ambas comparten el bloqueo de receptores H1 como mecanismo, pero en contextos fisiopatológicos distintos (vestibular frente a mediado por mastocitos). La única publicación disponible es un estudio piloto farmacocinético en perros sanos que midió el efecto sobre la formación de habones inducidos por histamina; es un estudio preclínico y no demuestra eficacia en humanos.

Una segunda predicción, **urticaria por frío** (puntaje 99.24%), tiene el mismo fundamento de clase, pero sin ningún estudio disponible. Las guías favorecen los antihistamínicos de segunda generación, por lo que el agente de primera generación no muestra ventaja demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Estudio farmacocinético piloto (preclínico, en perros) | Veterinary Dermatology | Compara la farmacocinética de la difenhidramina tras administración oral e intravenosa y tras dimenhidrinato oral en perros sanos, y su efecto farmacodinámico sobre la formación de habones inducidos por histamina. El dimenhidrinato se describe como una posible mejor absorción oral de difenhidramina. |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 13287 | DRAMAMINE (Kenvue Argentina) | Comprimidos x 24 | No disponible |
| 1352 | DRAMAMINE (Kenvue Argentina) | Comprimidos x 12 | No disponible |
| 40018 | VERTIGMINE (Lafedar) | Solución x 100 ml | No disponible |
| 39843 | AGIRAX (Montpellier) | Comprimidos x 10 | No disponible |
| 37686 | DR. AMIN (Eurolab) | 50 mg, comprimidos recubiertos x 6 | No disponible |

Hay 10 autorizaciones vigentes en total, todas de monofármaco; se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): hipertensión, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, diabetes mellitus, cetoacidosis diabética, úlcera péptica, hiperplasia prostática benigna, hipotensión, gota, abuso o dependencia de sustancias, trastornos de la coagulación, síndrome coronario agudo, enfermedad coronaria, infarto de miocardio, hemoglobinopatías, hipertensión ocular, glaucoma de ángulo cerrado, estenosis pilórica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción del cuello vesical e hipofosfatemia.
- **Interacciones farmacológicas**: se identificaron 67 interacciones. Las de nivel **mayor** son con **cloruro de potasio** y **citrato de potasio**. Las de nivel moderado incluyen principalmente anticolinérgicos (atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, trospio, propantelina, metescopolamina, clidinio, mepenzolato), opioides (morfina, opio, loperamida, eluxadolina), nabilona, metoclopramida y prucaloprida.

La información sobre advertencias y contraindicaciones del prospecto de ANMAT no está disponible; consultar el prospecto para completar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible por el componente difenhidramina, pero la evidencia se limita a un estudio farmacocinético preclínico en perros (nivel L4) y no existen ensayos clínicos. Además, las guías prefieren antihistamínicos de segunda generación para la urticaria, y el perfil de seguridad (efectos anticolinérgicos y múltiples contraindicaciones) no está verificado con el prospecto local.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), pendiente para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios clínicos en humanos sobre dimenhidrinato o difenhidramina en urticaria alérgica.
- Comparar con antihistamínicos de segunda generación para determinar si el dimenhidrinato aporta alguna ventaja.
- Verificar los textos de indicación aprobados en las autorizaciones locales y la compatibilidad de las vías de administración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

