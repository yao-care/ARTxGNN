---
layout: default
title: Enoxaparin
parent: Solo Predicción del Modelo (L5)
nav_order: 133
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Enoxaparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (nivel de evidencia L5). Indicación original: Embolia pulmonar, coagulación intravascular disemin…"
monitor_inn: "enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
---

# Enoxaparin
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

# Enoxaparina: De Embolia Pulmonar a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)

## Resumen en Una Frase

Enoxaparina es una heparina de bajo peso molecular, originalmente utilizada en el tratamiento de la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectiva para la **trombofilia por deficiencia de proteína C autosómica recesiva**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección: se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar, coagulación intravascular diseminada, púrpura fulminante (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99,58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica conocida, la enoxaparina es una heparina de bajo peso molecular que potencia la antitrombina III e inhibe el factor Xa (y, en menor grado, la trombina).

En la deficiencia grave congénita de proteína C se pierde la vía anticoagulante de esta proteína, lo que lleva a una generación de trombina sin control. Inhibir el factor Xa y la trombina ofrece, por tanto, una justificación plausible para controlar el fenotipo trombótico. Además, la enfermedad es mecanísticamente cercana a la púrpura fulminante y a la coagulación intravascular diseminada, que son manifestaciones clínicas típicas de la deficiencia grave neonatal de proteína C y figuran entre las indicaciones originales del fármaco.

Conviene tener presente una limitación importante: la anticoagulación actúa de forma sintomática y no repone la proteína C ausente. El tratamiento estándar es el concentrado o reemplazo de proteína C, y los anticoagulantes se usan como terapia complementaria o a largo plazo. El puntaje de 0,996 es únicamente una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se listan 5 de las 12 autorizaciones vigentes (todas de producto único). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 13528 | CLEXANE | 20 mg, jeringa prellenada x 10 | Sanofi-Aventis |
| 13530 | CLEXANE | 40 mg, jeringa prellenada x 10 | Sanofi-Aventis |
| 18693 | CLEXANE | 60 mg, jeringa prellenada x 10 | Sanofi-Aventis |
| 18694 | CLEXANE | 80 mg, jeringa prellenada x 10 | Sanofi-Aventis |
| 56201 | OMATEX | 40 mg, jeringa prellenada x 2 | Elea |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedades hematológicas, trombocitopenia (incluida la inducida por heparina), trastornos de la coagulación, hemofilia, deficiencia de antitrombina III, defectos plaquetarios cualitativos (p. ej., trombastenia de Glanzmann), hemorragia intracraneal e intracerebral, desprendimiento de placenta, úlcera péptica activa, colitis ulcerosa y enfermedad inflamatoria intestinal, endocarditis infecciosa, retinopatías (diabética, hipertensiva), osteoporosis, enfermedad de las vías biliares e ictericia obstructiva.
- **Interacciones farmacológicas**: se identificaron 174 interacciones en total. Entre las de nivel **mayor** figuran ácido acetilsalicílico, ibuprofeno, ketorolaco, alteplasa, abciximab, acalabrutinib, deferasirox, trastuzumab emtansina, ibritumomab tiuxetán y tositumomab (incluido el marcado con I-131). Entre las de nivel moderado: dexfenfluramina, fenfluramina, sibutramina, aliskiren, sugammadex y yoduros radiactivos (I-123, I-131).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y literatura de respaldo (nivel L5). Además, el estándar de tratamiento es el reemplazo de proteína C, y la enoxaparina solo sería un complemento sintomático.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre el uso de heparinas de bajo peso molecular en la deficiencia congénita de proteína C
- Datos formales del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de ANMAT, necesarias para el análisis de seguridad
- Evaluación de la posición de la enoxaparina frente al concentrado de proteína C (monoterapia, complemento o terapia a largo plazo)
- Análisis de compatibilidad de vía y forma farmacéutica con la población pediátrica/neonatal
- Evaluación de riesgos hemorrágicos y de las interacciones relevantes para esta población
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

