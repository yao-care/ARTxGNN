---
layout: default
title: Chlorzoxazone
parent: Solo Predicción del Modelo (L5)
nav_order: 96
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Chlorzoxazone: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones de ANMAT (los textos de indicació…"
monitor_inn: "chlorzoxazone"
predicted_indications: ["migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine with brainstem aura", "pulmonary hypertension", "atrophoderma vermiculata", "ulerythema ophryogenesis", "kyphoscoliotic heart disease", "rheumatoid arthritis"]
---

# Chlorzoxazone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Clorzoxazona: De Relajante Muscular a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Clorzoxazona es un relajante muscular de acción central, comercializado en Argentina principalmente en productos asociados a ibuprofeno (línea Ibupirac Flex). El modelo TxGNN predice que podría ser efectiva para **trastorno de migraña**, aunque hasta ahora no existen ensayos clínicos registrados y solo se dispone de **3 publicaciones** indirectas (dos revisiones y un estudio en ratones) que no abordan la migraña con clorzoxazona de forma directa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de ANMAT (los textos de indicación están vacíos); uso conocido como relajante muscular en dolor y espasmo musculoesquelético |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (7 de 7) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorizaciones | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según la información conocida, la clorzoxazona es un relajante muscular de acción central que además se describe como activador de canales de potasio dependientes de calcio (tipo SK/BK). Su uso en dolor musculoesquelético está establecido, pero no hay datos que respalden su uso en migraña.

La conexión propuesta es indirecta. Mutaciones en el gen CACNA1A (canal CaV2.1) se asocian con ataxia cerebelosa, migraña hemipléjica familiar y epilepsia. En un modelo murino con ganancia de función de CaV2.1, los activadores de canales de K⁺ dependientes de Ca²⁺ aliviaron la ataxia. En teoría, un efecto similar podría atenuar la hiperexcitabilidad neuronal en ciertas formas de migraña con componente de canalopatía.

Es importante subrayar que esta lógica es especulativa: la literatura recuperada trata de ataxia cerebelosa y vértigo, no de migraña tratada con clorzoxazona. El puntaje alto de TxGNN (0,9973) es únicamente una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Revisión | Journal of Neurology | Panorama de la farmacoterapia de trastornos cerebelosos y vestibulares centrales; la 4-aminopiridina se recomienda para el nistagmo. No trata la clorzoxazona en migraña |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Revisión | Deutsches Ärzteblatt International | Tratamiento y evolución natural del vértigo periférico y central; la migraña vestibular representa cerca del 11 % de los casos |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclínico (modelo animal) | The Journal of Neuroscience | En ratones con mutación Cacna1a, los activadores de canales de K⁺ dependientes de Ca²⁺ aliviaron la ataxia cerebelosa causada por corrientes CaV2.1 aumentadas |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51613 | Ibupirac Flex Cápsulas Blandas | 400 mg cápsulas blandas x 20 | No especificada en los datos |
| 15696 | Ibupirac Flex | 400 mg comprimidos recubiertos x 20 | No especificada en los datos |
| 51612 | Ibupirac Flex Cápsulas Blandas | 400 mg cápsulas blandas x 10 | No especificada en los datos |
| 36771 | Ibupirac Flex 600 | Comprimidos recubiertos x 10 | No especificada en los datos |
| 49033 | Ibupirac Flex 600 | Comprimidos recubiertos x 20 | No especificada en los datos |

Hay 7 autorizaciones vigentes en total (6 de Pfizer y 1 de Siegfried, Flexina 600); se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, abuso/dependencia de sustancias, lesión hepática inducida por fármacos e intoxicación por paracetamol.
- **Interacciones farmacológicas**: se identificaron 72 interacciones potenciales. Entre las principales:
  - **Mayores**: morfina y morfina liposomal.
  - **Moderadas**: dronabinol, metoclopramida, nabilona, naltrexona, opio, sibutramina, etanol y prometazina.
  - Otras con nivel no clasificado: doxiciclina, metformina, omeprazol, lansoprazol, prednisona, simvastatina, ranitidina, bupropión, ácido fólico y warfarina.

Para el resto de la información de seguridad (advertencias y contraindicaciones oficiales), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para migraña se apoya solo en el puntaje computacional de TxGNN y en una relación mecanística indirecta, sin ensayos clínicos ni literatura que evalúe la clorzoxazona en migraña (nivel L5). Además, el perfil hepático de la clorzoxazona y las interacciones con depresores del sistema nervioso central requieren cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones oficiales), indispensable para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank) y verificar la activación de canales de K⁺ relevante para migraña.
- Realizar estudios preclínicos en modelos de migraña y una revisión sistemática dirigida.
- Evaluar la seguridad hepática en la población con migraña antes de considerar ensayos clínicos.
- Otras predicciones del modelo (p. ej., artritis reumatoide, nivel L4) solo respaldarían un uso sintomático complementario del dolor; el resto carece de evidencia (L5).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

