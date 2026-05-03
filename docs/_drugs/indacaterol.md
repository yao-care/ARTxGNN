---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

La skill TxGNN Pipeline está orientada a infraestructura. La tarea actual es generar un informe clínico desde un Evidence Pack JSON, lo cual está completamente definido en el system prompt. Procedo directamente a generar el informe.

---

> **Nota metodológica:** El Evidence Pack contiene 10 predicciones ordenadas por score TxGNN. La predicción #1 por score (NSIAD, 99.54%) no cuenta con ninguna evidencia clínica (L5, Hold). La predicción con mayor nivel de evidencia clínica es **Enfermedad Bronquial / Asma** (rank TxGNN #7, score 99.18%), con L1 de evidencia y recomendación "Proceed with Guardrails". El presente informe se centra en esta indicación por ser la única clínicamente accionable del conjunto.

---

# Indacaterol: De EPOC a Enfermedad Bronquial (Asma)

## Resumen en Una Frase

Indacaterol es un agonista β₂-adrenérgico de ultra-larga duración (ultra-LABA), aprobado globalmente como monoterapia para la enfermedad pulmonar obstructiva crónica (EPOC), aunque actualmente no está comercializado en Argentina. El modelo TxGNN predice que podría ser efectivo para la **Enfermedad Bronquial (Asma)**, con una sólida base de evidencia que incluye **múltiples ensayos de Fase 3 completados con más de 3.000 pacientes** y **20 publicaciones científicas** que respaldan esta dirección, reflejando el desarrollo clínico activo de sus formulaciones combinadas (QMF149 y QVM149 / Enerzair®) en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | EPOC (aprobación global; no registrado en Argentina) |
| Nueva Indicación Predicha | Enfermedad Bronquial (Asma) |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Indacaterol es un agonista β₂-adrenérgico altamente selectivo y de acción ultraprolong­ada. Su mecanismo consiste en unirse a los receptores β₂ del músculo liso bronquial, activar la adenilato ciclasa, elevar el AMPc intracelular, activar la PKA y producir relajación sostenida del músculo liso —con broncodilatación que dura más de 24 horas con una sola dosis. Adicionalmente, la señalización β₂ inhibe la degranulación de mastocitos y la activación de eosinófilos, aportando un efecto antiinflamatorio auxiliar que resulta directamente relevante en asma.

La relación entre EPOC y asma bronquial es estrecha: ambas son enfermedades obstructivas de la vía aérea que comparten el fenómeno de broncoespasmo como mecanismo central. Los LABAs constituyen una pieza fundamental en el manejo de ambas patologías, con la diferencia crítica de que en asma deben administrarse siempre combinados con un corticosteroide inhalado (ICS) para evitar el riesgo de exacerbaciones graves. Precisamente en torno a esta premisa se desarrollaron las formulaciones fijas QMF149 (indacaterol/mometasona) y QVM149 (indacaterol/glicopirronio/mometasona, Enerzair® Breezhaler®), ambas aprobadas por la EMA para mantenimiento del asma en adultos inadecuadamente controlados.

El mecanismo de indacaterol es por tanto directamente aplicable al asma: la broncodilatación β₂-AR es un objetivo terapéutico de primera línea en esta enfermedad, y los grandes ensayos de Fase 3 han confirmado que sus combinaciones fijas son superiores o no inferiores a los estándares comparadores activos. La predicción del modelo TxGNN captura con precisión esta relación fisiológica y el nodo compartido entre EPOC y asma en el grafo de conocimiento biomédico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Fase 3 | Completado | 3.092 | QVM149 vs QMF149 en asma mal controlada; 52 semanas; mayor estudio de la serie — evalúa superioridad de la triple terapia fija sobre doble terapia ICS/LABA |
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Fase 3 | Completado | 2.216 | QMF149 (dos dosis) vs mometasona sola en asma persistente mal controlada; 52 semanas; evaluación de función pulmonar y control de síntomas |
| [NCT00941798](https://clinicaltrials.gov/study/NCT00941798) | Fase 2 | Completado | 2.283 | Ensayo de seguridad impulsado por eventos graves (hospitalizaciones/intubaciones/muerte) de QMF149 vs mometasona en asma |
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Fase 3 | Completado | 1.426 | QVM149 no inferior a triple terapia libre (salmeterol/fluticasona + tiotropio) en asma moderada-severa no controlada; 24 semanas |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Fase 3 | Completado | 805 | Seguridad de indacaterol (300/600 µg) vs salmeterol en asma moderada-severa; 26 semanas; ensayo de seguridad a largo plazo |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Fase 3 | Completado | 511 | Eficacia broncodilatadora de 14 días de indacaterol vs placebo y salmeterol como control activo en asma persistente |
| [NCT03100825](https://clinicaltrials.gov/study/NCT03100825) | Fase 3 | Completado | 96 | Seguridad a 52 semanas de QVM149 en pacientes japoneses con asma; relevante para extrapolación a poblaciones asiáticas |
| [NCT05562466](https://clinicaltrials.gov/study/NCT05562466) | Fase 3 | En curso | 200 | QMF149 vs budesonida en niños de 6 a <12 años con asma; diseño cruzado, 12 semanas; superioridad en función pulmonar |
| [NCT05776927](https://clinicaltrials.gov/study/NCT05776927) | Fase 3 | No iniciado | 304 | QVM149 vs salmeterol/fluticasona en adolescentes de 12 a <18 años con asma; diseño paralelo activo-controlado |
| [NCT00403637](https://clinicaltrials.gov/study/NCT00403637) | Fase 2/3 | Completado | 45 | Comparación directa de indacaterol (150/300/600 µg) vs formoterol (estándar LABA) en asma persistente; establece el perfil de eficacia relativa cabeza a cabeza |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | ECA (Fase 3) | Lancet Respiratory Medicine | IRIDIUM: MF/IND/GLY una vez al día superior a ICS-LABA en reducción de exacerbaciones y mejoría del FEV₁ en asma inadecuadamente controlada |
| [35348408](https://pubmed.ncbi.nlm.nih.gov/35348408/) | 2023 | ECA extensión (52 sem.) | J Asthma | Seguridad a largo plazo de IND/GLY/MF e IND/MF en pacientes japoneses con asma; perfil favorable sin señales de seguridad nuevas |
| [33711782](https://pubmed.ncbi.nlm.nih.gov/33711782/) | 2021 | Subestudio de seguridad (ECA) | Respiratory Medicine | Análisis agrupado de Fase 3: seguridad cardiovascular de mometasona/indacaterol y combinación triple confirmada; sin exceso de eventos adversos cardíacos |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Revisión sistemática | Drugs | Revisión integral de indacaterol/glicopirronio/mometasona (Enerzair® Breezhaler®): eficacia, seguridad y posicionamiento en asma moderada-severa tras aprobación EMA |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | Revisión de expertos | Expert Review of Respiratory Medicine | IND/GLY/MF en asma moderada-severa: nueva vía terapéutica con triple terapia fija; impacto sobre exacerbaciones y control de síntomas |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Revisión | Respiratory Medicine | Ultra-LABAs (indacaterol, olodaterol, vilanterol, abediterol) en asma: evidencia de eficacia, perfil de seguridad y rol obligatorio de combinación con ICS |
| [32967685](https://pubmed.ncbi.nlm.nih.gov/32967685/) | 2020 | Estudio PK/PD | Respiratory Research | Comparación de farmacocinética, función pulmonar y tolerabilidad de indacaterol maleato vs acetato en pacientes con asma; base para selección de sal en FDC |
| [28768531](https://pubmed.ncbi.nlm.nih.gov/28768531/) | 2017 | ECA cruzado | Respiratory Research | Glicopirronio e indacaterol —solos y combinados— sobre la curva dosis-respuesta a metacolina en asmáticos leves; confirmación de broncoproteción aditiva |
| [31404293](https://pubmed.ncbi.nlm.nih.gov/31404293/) | 2019 | Cohorte/Observacional | Frontiers in Pharmacology | Eosinofilia e hiperreactividad en EPOC vs asma: utilidad de ICS y broncodilatadores de larga acción en fenotipos superpuestos |
| [24247039](https://pubmed.ncbi.nlm.nih.gov/24247039/) | 2014 | Revisión narrativa | Current Opinion in Pulmonary Medicine | Broncodilatadores actuales y novedosos en enfermedad respiratoria: farmacología comparada de β₂-agonistas y antagonistas muscarínicos, incluyendo indacaterol |

---

## Información de Mercado en Argentina

Indacaterol **no cuenta con ningún registro sanitario en Argentina**. La consulta a la base de datos de ANMAT realizada el 29/03/2026 no arrojó resultados para este principio activo. No existen formulaciones de indacaterol —ni como monoterapia ni en combinación fija (QMF149/QVM149)— autorizadas para comercialización en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto oficial para información completa de seguridad.

Como referencia del contexto clínico conocido en la indicación de asma:
- **Uso en asma**: los LABAs como indacaterol están contraindicados como monoterapia en asma sin corticosteroide inhalado concomitante; las formulaciones combinadas QMF149 y QVM149 son las formas aprobadas para esta indicación.
- **Seguridad cardiovascular**: el análisis agrupado de los ensayos de Fase 3 (PMID 33711782) no identificó exceso de eventos cardíacos adversos con las combinaciones fijas.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia clínica para indacaterol en enfermedad bronquial (asma) alcanza nivel L1: existen múltiples ensayos de Fase 3 completados con hasta 3.092 pacientes, y las formulaciones combinadas QMF149 (Atectura®) y QVM149 (Enerzair®) ya cuentan con aprobación en la Unión Europea y Japón para mantenimiento del asma en adultos inadecuadamente controlados. La barrera principal en Argentina no es la evidencia clínica, sino la ausencia de registro sanitario local.

**Para avanzar se necesita:**
- Gestionar el registro sanitario ante ANMAT para indacaterol o sus combinaciones fijas (QMF149 / QVM149), aportando el expediente técnico de la aprobación EMA como referencia regulatoria
- Obtener y revisar el prospecto oficial aprobado (EMA/FDA) para compilar el perfil completo de advertencias, contraindicaciones e interacciones farmacológicas
- Verificar la disponibilidad local del dispositivo de inhalación Breezhaler® y su cadena de distribución en Argentina
- Diseñar un plan de farmacovigilancia post-comercialización específico para asma, con monitoreo de exacerbaciones graves y eventos cardiovasculares
- Confirmar la estrategia de desarrollo pediátrico (ensayos NCT05562466 y NCT05776927 en curso para niños y adolescentes) como potencial extensión futura de indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

