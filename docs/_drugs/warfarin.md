---
layout: default
title: Warfarin
parent: Solo Predicción del Modelo (L5)
nav_order: 246
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Warfarin: nueva indicación predicha, Trombofilia (nivel de evidencia L5). Indicación original: Embolia pulmonar, enfermedad trombótica…"
---

# Warfarin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Warfarina: De Enfermedad Tromboembólica a Trombofilia

## Resumen en Una Frase

Warfarina (comercializada en Argentina como CIRCUVIT) es un anticoagulante antagonista de la vitamina K, utilizado originalmente en la embolia pulmonar, la enfermedad trombótica y la embolia intracraneal.
El modelo TxGNN predice que podría ser efectiva para **trombofilia**, con **1 ensayo clínico** de Fase 3 (estado desconocido) y **19 publicaciones** que respaldan esta dirección, la mayoría revisiones y guías de manejo.
Se trata de una extensión dentro de la misma clase terapéutica más que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar, enfermedad trombótica, embolia intracraneal (según el grafo de conocimiento; el texto de indicación aprobado por ANMAT no está disponible) |
| Nueva Indicación Predicha | Trombofilia (candidata principal por nivel de evidencia; el primer lugar del ranking de TxGNN es la deficiencia de cofactor II de la heparina) |
| Puntaje de Predicción TxGNN | 99.75% (trombofilia); 99.87% para la deficiencia de cofactor II de la heparina |
| Nivel de Evidencia | L1 (condicional: depende de un ensayo de Fase 3 con estado desconocido y no específico de warfarina) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** el L1 asignado a trombofilia es nominal. El único ensayo de Fase 3 no está completado (estado desconocido), evalúa una estrategia guiada por dímero D y no compara warfarina específicamente. Con criterios estrictos, la evidencia equivaldría a L4. Por ello se recomienda cautela.

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la warfarina es un antagonista de la vitamina K que reduce la síntesis de los factores de coagulación dependientes de esta vitamina (II, VII, IX y X). Su eficacia en la enfermedad trombótica y la embolia pulmonar está bien establecida.

La trombofilia (hereditaria o adquirida) se caracteriza por un estado de hipercoagulabilidad con riesgo de tromboembolismo venoso recurrente. La anticoagulación oral prolongada es una opción estándar de profilaxis secundaria, por lo que el uso es mecanísticamente coherente y cercano a la indicación original ya conocida.

Hay que considerar que la trombofilia queda en gran medida cubierta por la indicación de enfermedad trombótica, por lo que se trata de una extensión adyacente a la etiqueta. Además, la literatura incluye comparaciones con anticoagulantes orales directos (DOAC), que podrían reducir el papel relativo de la warfarina.

Otras predicciones del modelo, con evidencia más débil:
- **Deficiencia de cofactor II de la heparina** (99.87%, L4): solo tres reportes de casos o de familias, sin ensayos.
- **Exceso de factor V con trombosis espontánea** (99.84%, L5): sin ensayos ni literatura.
- **Deficiencia de antitrombina tipo 2** (99.84%, L4): un único reporte de caso.
- **Artritis reumatoide** (99.21%, L4), **enfermedad fibroquística de mama** (99.20%, L5) y **displasia mamaria benigna** (99.10%, L5): no existe un mecanismo terapéutico plausible. Las señales provienen de estudios de interacción farmacológica (la warfarina se usó como sustrato de prueba de CYP2C9 o interactúa con otros fármacos) y no indican beneficio. No deben considerarse para acción.

---

## Evidencia de Ensayos Clínicos

Ensayos para trombofilia:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Fase 3 | Desconocido | 300 | Estrategia guiada por dímero D para ajustar la duración de la anticoagulación oral en pacientes tras un primer episodio de trombosis venosa profunda no provocada (2008-2012) |

Para artritis reumatoide existen cuatro ensayos de Fase 1 (NCT01311622, NCT04246762, NCT01636557, NCT05392127), todos de interacción farmacocinética con warfarina como sustrato de prueba. No evalúan eficacia de la warfarina en artritis reumatoide y no se incluyen como evidencia de respaldo.

---

## Evidencia de Literatura

Publicaciones seleccionadas para trombofilia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revisión | JAMA | Diagnóstico y tratamiento del tromboembolismo venoso de miembros inferiores; recurrencia del 20-36% en 10 años |
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Revisión | J Thromb Haemost | Uso de DOAC en prevención secundaria de TEV en trombofilia grave; la evidencia actual proviene solo de cohortes o estudios de un centro |
| [39244017](https://pubmed.ncbi.nlm.nih.gov/39244017/) | 2024 | Revisión | Presse Med | Impacto de la trombofilia en el manejo del tromboembolismo venoso |
| [20008203](https://pubmed.ncbi.nlm.nih.gov/20008203/) | 2009 | Revisión | Hematology Am Soc Hematol Educ Program | Síndrome antifosfolípido; el tratamiento antitrombótico es la base del manejo |
| [12871277](https://pubmed.ncbi.nlm.nih.gov/12871277/) | 2003 | Revisión | J Thromb Haemost | Manejo de la trombofilia; incertidumbre sobre cómo usar la información genética |
| [15706484](https://pubmed.ncbi.nlm.nih.gov/15706484/) | 2005 | Revisión | Semin Thromb Hemost | Opciones de manejo; la trombofilia hereditaria no debería modificar la intensidad de la anticoagulación |
| [12787539](https://pubmed.ncbi.nlm.nih.gov/12787539/) | 2003 | Revisión | Best Pract Res Clin Obstet Gynaecol | Tromboprofilaxis en embarazo con trombofilias hereditarias (heparina de bajo peso molecular) |
| [22740145](https://pubmed.ncbi.nlm.nih.gov/22740145/) | 2012 | Comparación indirecta | Thromb Haemost | Dabigatrán, rivaroxabán y apixabán frente a warfarina en fibrilación auricular (no específico de trombofilia) |
| [10718793](https://pubmed.ncbi.nlm.nih.gov/10718793/) | 2000 | No clasificado | Br J Surg | Necrosis cutánea inducida por warfarina: complicación rara (0.01-0.1%) |
| [3046272](https://pubmed.ncbi.nlm.nih.gov/3046272/) | 1988 | No clasificado | Am Fam Physician | Síndrome de Trousseau; la heparina es preferible y la warfarina no parece beneficiosa |

Para deficiencias hereditarias específicas solo hay reportes de casos: [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) (1990, deficiencia familiar de cofactor II de la heparina), [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) (1991) y [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) (2001), además de [29582922](https://pubmed.ncbi.nlm.nih.gov/29582922/) (2017, deficiencia de antitrombina tipo IIB).

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20634 | CIRCUVIT (Ariston) | Comprimidos 5 mg x 20 | No disponible en los datos compilados |
| 38257 | CIRCUVIT (Ariston) | Comprimidos 5 mg x 50 | No disponible en los datos compilados |
| 20633 | CIRCUVIT (Ariston) | Comprimidos 2 mg x 20 | No disponible en los datos compilados |
| 38256 | CIRCUVIT (Ariston) | Comprimidos 2 mg x 50 | No disponible en los datos compilados |

Las cuatro autorizaciones están vigentes y corresponden a monofármaco.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipotiroidismo, síndrome nefrótico, trastornos psicóticos y mentales, enfermedades del tejido conectivo, enfermedades óseas y del cartílago, abuso de sustancias, enfermedades de la coagulación, hiperlipidemia, anemia, insuficiencia renal, colestasis y enfermedad diarreica crónica.
- **Interacciones farmacológicas:** se registran 865 interacciones. Entre las principales:
  - **Mayores:** ácido acetilsalicílico, metronidazol.
  - **Moderadas:** ranitidina, rabeprazol, doxiciclina, hidrocortisona, metformina, amoxicilina, bupropión, aprepitant, mesalazina, triamcinolona, balsalazida, dexametasona, betametasona, budesonida y ácido quenodesoxicólico.
  - **Menores:** acarbosa, albiglutida, ácido ascórbico.
- **Riesgos documentados en la literatura:** necrosis cutánea inducida por warfarina (rara) y potenciación del efecto anticoagulante con otros fármacos, con riesgo de sangrado (por ejemplo, danazol y leflunomida).

No se dispone de advertencias ni contraindicaciones del prospecto de ANMAT. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La trombofilia es una extensión cercana a la indicación ya existente (enfermedad trombótica), con un único ensayo de Fase 3 de estado desconocido y no específico de warfarina, y literatura compuesta sobre todo por revisiones. Las demás predicciones carecen de evidencia o se explican por artefactos de interacción farmacológica. Además, no se dispone del prospecto de ANMAT, lo que impide completar el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas).
- Confirmar los resultados específicos de warfarina en NCT00895505 y su estado actual.
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar el papel de la warfarina frente a los DOAC en trombofilia grave.
- Verificar si la trombofilia ya está cubierta por la indicación aprobada local, para determinar si hay valor real de reposicionamiento.
- Descartar de la evaluación las predicciones de artritis reumatoide y de enfermedad mamaria benigna.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

