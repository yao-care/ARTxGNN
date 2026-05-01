---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Diazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Diazepam: De Ansiedad y Epilepsia a Insomnio

## Resumen en Una Frase

Diazepam es una benzodiazepina reconocida globalmente por el tratamiento de la ansiedad, convulsiones y espasmos musculares, aunque actualmente no cuenta con registro en Argentina (ANMAT).
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con un puntaje de 99.999%, respaldado por **24 ensayos clínicos** y **18 publicaciones** que exploran esta dirección.
Cabe destacar que el uso de Diazepam como hipnótico en insomnio ya tiene respaldo en la literatura científica internacional, incluyendo un ensayo clínico controlado aleatorizado directo publicado en 1981 (PMID 6113175).

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No registrado en Argentina (ANMAT); globalmente conocido para ansiedad, convulsiones y sedación |
| Nueva Indicacion Predicha | Insomnio (insomnia disease) |
| Puntaje de Prediccion TxGNN | 99.999% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos formales sobre el mecanismo de acción procedentes de DrugBank. Sin embargo, la literatura científica incluida en este paquete de evidencia confirma que Diazepam es un **modulador alostérico positivo (PAM) del receptor GABA-A**, la principal vía inhibitoria del sistema nervioso central (PMID 39581171). Al unirse al sitio benzodiazepínico del receptor GABA-A, Diazepam potencia el efecto del ácido gamma-aminobutírico (GABA), incrementando la frecuencia de apertura de los canales de cloro y produciendo efectos ansiolíticos, sedantes, hipnóticos, anticonvulsivantes y miorrelajantes.

La relación entre las indicaciones clásicas de Diazepam y el insomnio es directa y mecanísticamente coherente: el insomnio se asocia frecuentemente a hiperactivación del sistema nervioso central (*hyperarousal*), y la modulación GABAérgica aborda precisamente este sustrato fisiopatológico. Este vínculo queda confirmado por el hecho de que múltiples estudios preclínicos utilizan a Diazepam como **control positivo estándar** en modelos animales de insomnio (PMID 32240473, 40347763, 41525914, 40350874, 37776625), lo cual refleja su reconocida eficacia hipnótica de referencia en la comunidad científica.

No obstante, el uso prolongado de Diazepam para el insomnio plantea riesgos clínicos significativos que justifican los guardarraíles. Un estudio publicado en *Nature Neuroscience* (PMID 35228700, 2022) demostró que el tratamiento crónico deteriora la plasticidad de espinas dendríticas a través de la proteína TSPO mitocondrial en microglía, causando deterioro cognitivo persistente en modelos murinos. Adicionalmente, evidencia clínica reciente vincula el uso prolongado de benzodiazepinas con mayor riesgo de cáncer de mama (PMID 40583063, 2025), lo que subraya la necesidad de uso a corto plazo con protocolos de reducción gradual supervisada.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Fase 2 | Completado | 74 | Evalúa cómo la velocidad de reducción y rasgos individuales influyen en la discontinuación de hipnóticos (incluyendo BZD como Diazepam) en pacientes con insomnio; confirma el uso amplio de benzodiazepinas como base farmacológica en esta población |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Fase 3 | Activo, sin reclutamiento | 260 | Compara protocolo ciego de reducción de hipnóticos combinado con Terapia Cognitivo-Conductual para el Insomnio (TCC-I); proporciona el marco de seguridad para el uso de benzodiazepinas en insomnio y su discontinuación controlada |
| [NCT00287794](https://clinicaltrials.gov/study/NCT00287794) | N/A | Desconocido | 1,000 | Estudio prospectivo de calidad de sueño en pacientes con artritis reumatoide; analiza características del sueño perturbado y el uso de hipnóticos (incluyendo benzodiazepinas) en esta población |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completado | 188 | Mecanismo novedoso para ayudar a adultos mayores a discontinuar el uso de pastillas para dormir; aborda directamente la dependencia a hipnóticos incluyendo benzodiazepinas como Diazepam |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Fase 4 | Completado | 17 | ECA multicéntrico sobre uso combinado de Ramelteon para facilitar la reducción de hipnóticos BZD y no-BZD en insomnio crónico; directamente relevante para el manejo de Diazepam como hipnótico a largo plazo |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1,400 | Evaluación de riesgo-beneficio de hipnóticos para trastornos del sueño en adultos mayores; incluye análisis de patrones de uso, eficacia y seguridad de Diazepam y otras benzodiazepinas en esta indicación |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completado | 128 | ECA sobre estrategias óptimas de retiro de benzodiazepinas en adultos con insomnio dependiente de hipnóticos, comparando apoyo psicológico vs. Terapia de Aceptación y Compromiso (ACT) |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Fase 2 | Desconocido | 58 | Evalúa Adepsique® —combinación que contiene Diazepam— más antioxidantes en pacientes con tinnitus crónico subjetivo; constituye uso directo de Diazepam en un contexto sintomático con componente ansioso/insomnio |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Fase 2/3 | En reclutamiento | 93 | Evalúa Baclofeno como complemento para facilitar la reducción de benzodiazepinas en pacientes dependientes; evidencia indirecta del problema de dependencia a Diazepam en el contexto del insomnio |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Fase 1 | Completado | 12 | Estudio farmacológico de moduladores GABA selectivos; menciona explícitamente a Diazepam como tratamiento establecido para el insomnio y referencia para comparación de nuevos compuestos GABAérgicos |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | ECA | J Int Medical Research | ECA doble ciego comparando Lormetazepam 1 mg vs. **Diazepam 5 mg** en 100 pacientes con trastornos del sueño como síntoma concomitante de enfermedad general; Lormetazepam superó a Diazepam en tiempo para conciliar el sueño y duración del sueño ininterrumpido (p<0.05), estableciendo la eficacia directa de Diazepam como hipnótico |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Experimental | Nature Neuroscience | El tratamiento prolongado con **Diazepam** deteriora la plasticidad estructural de espinas dendríticas vía proteína TSPO mitocondrial en microglía, causando deterioro cognitivo persistente en ratones; alerta de seguridad crítica para el uso crónico en insomnio |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Revisión | Bioorganic Chemistry | Revisión de moduladores de pequeña molécula del receptor GABA-A; confirma que **Diazepam** es un PAM clásico con eficacia terapéutica documentada en insomnio, ansiedad y epilepsia, aunque asociado a sedación, deterioro mnésico y adicción con uso prolongado |
| [32240473](https://pubmed.ncbi.nlm.nih.gov/32240473/) | 2020 | Experimental | Chin J Integrative Med | Estudio de efectos sedantes-hipnóticos de *Polygala tenuifolia* en ratas con insomnio senil; utiliza **Diazepam** como control positivo de referencia, confirmando su eficacia hipnótica estándar en modelos animales de insomnio por envejecimiento |
| [40347763](https://pubmed.ncbi.nlm.nih.gov/40347763/) | 2025 | Experimental | J Pharm Biomed Analysis | Estudio de efectos sedantes-hipnóticos del granulado Yiyin Anshen en ratones con privación de sueño inducida por PCPA; emplea **Diazepam** como control positivo en pruebas de sedación-hipnosis inducidas por pentobarbital sódico |
| [41525914](https://pubmed.ncbi.nlm.nih.gov/41525914/) | 2026 | Experimental | J Ethnopharmacology | Modelo de comorbilidad insomnio-ansiedad en ratones evaluando la fórmula Zhi-Gan mediante señalización PACAP en corteza prefrontal medial; emplea **Diazepam** como control positivo para efectos ansiolíticos e hipnóticos combinados |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Experimental | China J Chinese Materia Medica | Modelo de depresión/insomnio inducido por estrés crónico imprevisible (CUMS) en ratones; **Diazepam 2 mg/kg** utilizado como grupo de control positivo, con evaluación de comportamiento y marcadores neurobiológicos del sueño |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Experimental | J Pharm Biomed Analysis | Metabolómica de espectro de masas para evaluar eficacia de Naoling Pian en ratas con insomnio inducido por PCPA; **Diazepam** usado como control positivo estándar, con análisis de metabolitos y vías metabólicas alteradas en insomnio |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clínico/Molecular | Cell Mol Biol Letters | Evidencia clínica y mecanismos moleculares que vinculan el uso prolongado de BZD/Z-drugs (incluyendo **Diazepam**) con mayor riesgo de cáncer de mama; relevante para la evaluación del perfil de riesgo a largo plazo en el insomnio crónico |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Revisión Sistemática | Frontiers in Pharmacology | Revisión sistemática de ECAs sobre formulaciones de Suanzaoren para el insomnio; contextualiza la complejidad del tratamiento farmacológico y los mecanismos GABAérgicos, serotonérgicos y de melatonina involucrados en el insomnio como indicación terapéutica |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
Existe al menos un ECA directo (PMID 6113175, 1981, N=100) y múltiples estudios preclínicos que confirman la eficacia hipnótica de Diazepam en insomnio, con coherencia mecanística clara (modulación GABAérgica del *hyperarousal*). Sin embargo, la ausencia de registro en Argentina (ANMAT), las brechas en datos formales de seguridad, y la evidencia de daño cognitivo crónico (PMID 35228700) y riesgo oncológico a largo plazo (PMID 40583063) imponen la necesidad de guardarraíles estrictos antes de cualquier aplicación clínica local.

**Para avanzar se necesita:**
- Completar la ficha técnica de MOA desde DrugBank (brecha de datos activa)
- Obtener datos de advertencias, contraindicaciones e interacciones farmacológicas desde fuentes regulatorias argentinas (ANMAT) o prospecto internacional (ej. FDA, EMA)
- Diseñar protocolo de uso a corto plazo con criterios de exclusión explícitos para población geriátrica, pacientes con historial de abuso de sustancias y pacientes con riesgo oncológico
- Evaluar estrategia de registro ante ANMAT para la indicación de insomnio, incluyendo requisitos de prescripción controlada (Ley 19.303 de psicotrópicos en Argentina)
- Comparar perfil riesgo-beneficio frente a alternativas más modernas con mejor seguridad crónica (antagonistas duales de orexina, agonistas de melatonina) para orientar la posición clínica del producto
---

