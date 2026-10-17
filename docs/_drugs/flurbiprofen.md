---
layout: default
title: Flurbiprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flurbiprofen: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide (según la base de conocimiento del modelo"
monitor_inn: "flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
---

# Flurbiprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Flurbiprofeno: De Artritis Reumatoide a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Flurbiprofeno es un antiinflamatorio no esteroideo (AINE), comercializado en Argentina como CLINADOL FORTE y utilizado originalmente en artritis reumatoide, artrosis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, una displasia esquelética genética muy rara, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.99% (posición 344 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, flurbiprofeno es un AINE no selectivo que inhibe la ciclooxigenasa (COX-1 y COX-2) y reduce la síntesis de prostaglandinas. Su eficacia sintomática en enfermedades articulares inflamatorias y degenerativas está comprobada.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético genético raro, relacionado con la vía CDMP1/GDF5. No existe un vínculo mecanístico plausible entre la inhibición de COX y la modificación de esta enfermedad. En el mejor de los casos, un AINE podría aliviar de forma sintomática el dolor o la inflamación articular.

El puntaje alto del modelo probablemente refleja la cercanía en el grafo de conocimiento con enfermedades musculoesqueléticas (artritis, artrosis), y no un mecanismo terapéutico real. Esta predicción debe tomarse como una hipótesis sin respaldo y no como una señal de reposicionamiento sólida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 18400 | CLINADOL FORTE (Gador) | Comprimidos de 100 mg x 8 |
| 18401 | CLINADOL FORTE (Gador) | Comprimidos de 100 mg x 16 |
| 41619 | CLINADOL FORTE AP (Gador) | Comprimidos recubiertos de liberación prolongada de 200 mg x 8 |
| 45673 | CLINADOL COLUTORIO (Gador) | Frasco de 150 ml |

Las 4 autorizaciones están vigentes y corresponden a productos de un solo principio activo.

---

## Consideraciones de Seguridad

- **Condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, hemoglobinopatías, piouréter y abuso o dependencia de sustancias.
- **Interacciones Farmacológicas**: se identificaron 352 interacciones potenciales. Entre las de nivel moderado destacan:
  - corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida);
  - ácido acetilsalicílico;
  - metformina y antidiabéticos como clorpropamida y glimepirida;
  - aprepitant;
  - mesalazina y balsalazida;
  - citrato y bicarbonato de potasio;
  - preparados laxantes de limpieza intestinal (picosulfato, polietilenglicol con electrolitos, sulfato de sodio).

  Famotidina, cimetidina y linaclotida figuran como interacciones de nivel menor.
- Las advertencias principales y las contraindicaciones del prospecto no están disponibles en los datos compilados. Consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y no existe un mecanismo plausible para una enfermedad genética del desarrollo esquelético. Además, el perfil de seguridad del AINE (riesgo gastrointestinal, cardiovascular, renal y hepático, y 352 interacciones) no se justifica sin una base de eficacia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (por ejemplo, desde DrugBank).
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT.
- Evidencia preclínica o clínica que vincule la inhibición de COX con la fisiopatología de esta displasia. Hoy no existe.

**Nota sobre otras predicciones del mismo análisis:** la predicción de **espondilitis anquilosante** (puntaje 99.97%) tiene un respaldo mucho más sólido. Incluye varios estudios comparativos de flurbiprofeno de los años 70 y 80, algunos descritos como doble ciego, frente a indometacina, fenilbutazona y naproxeno. Su nivel de evidencia es L3 y la recomendación es "Proceed with Guardrails". Sin embargo, este es un caso más cercano a una extensión de indicación dentro de enfermedades reumáticas que a un reposicionamiento genuino. Se recomienda evaluarla por separado, con vigilancia de riesgo gastrointestinal y cardiovascular y de interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

