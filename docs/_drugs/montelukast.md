---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 5
---

# Montelukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Los skills específicos no están disponibles como herramientas diferidas en este entorno. Procedo directamente a generar el informe basándome en las instrucciones del sistema y el Evidence Pack proporcionado.

---

# Montelukast: De Asma y Rinitis Alérgica a Bronquitis

## Resumen en Una Frase

Montelukast es un antagonista selectivo de los receptores de leucotrienos cisteinílicos (CysLT1), ampliamente utilizado en el mundo para el tratamiento del asma bronquial y la rinitis alérgica, aunque sin registro vigente en Argentina. El modelo TxGNN predice que podría ser efectivo para la **bronquitis**, con **23 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. La predicción es biológicamente coherente, dado que los leucotrienos son mediadores centrales en la inflamación bronquial que subyace tanto al asma como a la bronquitis obstructiva.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Asma bronquial y rinitis alérgica (aprobación global; sin registro en Argentina) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Montelukast es un antagonista selectivo y oralmente activo del receptor CysLT1, que bloquea la acción de los leucotrienos cisteinílicos LTC4, LTD4 y LTE4. Estas moléculas son potentes mediadores proinflamatorios producidos por mastocitos y eosinófilos que inducen broncoconstricción, hipersecreción de moco, aumento de la permeabilidad vascular y reclutamiento de eosinófilos hacia las vías aéreas. Su eficacia en el asma bronquial ha sido comprobada en múltiples estudios de Fase 3 con gran tamaño muestral, lo que sirve como base mecanística para extender su uso a otras condiciones bronquiales inflamatorias.

La bronquitis comparte con el asma varios componentes fisiopatológicos clave: inflamación de la mucosa bronquial, edema, hipersecreción mucosa y obstrucción del flujo aéreo, todos mediados parcialmente por leucotrienos. En particular, la bronquitis obstructiva recurrente en niños pequeños y la bronquiolitis viral por VRS (virus respiratorio sincitial) se acompañan de elevación de leucotrienos urinarios, lo que justifica el uso de un antagonista del receptor CysLT1. Adicionalmente, estudios preclínicos en modelos animales han demostrado que LTB4 participa activamente en el remodelado bronquial crónico post-trasplante, y que montelukast puede atenuar este proceso.

Existe evidencia clínica directa de que montelukast reduce la duración y severidad de la bronquiolitis viral aguda por VRS, previene las sibilancias post-bronquiolitis, mejora el control de la bronquitis eosinofílica no asmática como adyuvante a corticoides inhalados, y ha mostrado beneficio en el síndrome de bronquiolitis obliterante post-trasplante (tanto pulmonar como hematopoyético). Este amplio espectro de evidencia en patología bronquial respalda la predicción del modelo TxGNN con solidez biológica y clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Fase 3 | Completado | 1 125 | Montelukast (MK0476) vs. placebo para síntomas respiratorios asociados a bronquiolitis por VRS en niños de 3 a 24 meses; el mayor ECA en su clase |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Fase 4 | Desconocido | 100 | Efectividad de montelukast sódico en el tratamiento y prevención de bronquitis obstructiva recurrente en niños de 1 a 7 años; evaluación directa en bronquitis |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Fase 4 | Completado | 30 | ECA doble ciego placebo-controlado de montelukast en síndrome de bronquiolitis obliterante (BOS) post-trasplante pulmonar; evalúa si ralentiza la progresión del rechazo crónico |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Fase 2 | Completado | 25 | Estudio prospectivo multicéntrico de montelukast para bronquiolitis obliterante post-trasplante de células madre en niños y adultos; analiza mecanismos patogénicos de BOS |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Fase 2 | Completado | 36 | Régimen FAM (fluticasona + azitromicina + montelukast) para bronquiolitis obliterante de nueva aparición post-HSCT; punto primario: tasa de fracaso terapéutico |
| [NCT03072849](https://clinicaltrials.gov/study/NCT03072849) | N/A | Completado | 23 | Detección espirométrica precoz y tratamiento FAM para enfermedad pulmonar obstructiva post-HSCT pediátrico; evalúa si el tratamiento precoz previene el BOS |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completado | 146 | Efecto de montelukast en bronquiolitis aguda y sibilancias virales post-bronquiolitis en lactantes de 3 a 12 meses |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completado | 141 | Montelukast diario vs. placebo para reducir la duración de la enfermedad aguda en el primer episodio de bronquiolitis en lactantes |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Fase 4 | Completado | 49 | Utilidad de feNO en diagnóstico diferencial de tos crónica: comparación de respuesta a montelukast vs. prednisolona durante dos semanas |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Fase 4 | Desconocido | 63 | Montelukast como terapia adyuvante a budesonida en bronquitis eosinofílica no asmática; punto primario: score VAS de tos y eosinofilia en esputo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Estudio Fase II prospectivo | Transplantation and Cellular Therapy | Ensayo multicéntrico de brazo único: montelukast interrumpe la actividad CysLT y podría reducir el declive de FEV1 en BOS post-trasplante hematopoyético; explora mecanismos patogénicos |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Revisión | Therapeutic Advances in Respiratory Disease | Revisión integral del potencial terapéutico de montelukast en BOS post-trasplante pulmonar y hematopoyético; analiza vías TH-1/TH-2, NF-κB y TGF-β como mecanismos relevantes |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Estudio Fase II | Biology of Blood and Marrow Transplantation | Régimen FAM con pulso breve de esteroides: 36 pacientes con BOS de nueva aparición post-HCT; 75% evitó fracaso terapéutico a 6 meses |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Estudio clínico | Respiratory Research | Budesonida/formoterol + montelukast + N-acetilcisteína en BOS post-HSCT: mejora de FEV1 y reducción de corticosteroides sistémicos |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | ECA | Chinese Medical Journal | Montelukast adyuvante a budesonida en bronquitis eosinofílica no asmática (NAEB): mejora significativa de calidad de vida, reducción de eosinofilia en esputo y control de tos |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Revisión sistemática | Pediatric Allergy and Immunology | Revisión sistemática: evaluación de montelukast para prevenir sibilancias post-bronquiolitis por VRS; analiza el papel de los cisteinil leucotrienos en la patogenia |
| [20442434](https://pubmed.ncbi.nlm.nih.gov/20442434/) | 2010 | Estudio experimental | Am J Respir Crit Care Med | Modelo murino de VRS: montelukast durante la infección primaria previene hiperreactividad bronquial, inflamación eosinofílica e hipersecreción mucosa en la reinfección |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Estudio preclínico | Journal of Cardiothoracic Surgery | LTB4 y montelukast en bronquiolitis obliterante por trasplante en ratas: LTB4 elevado en rechazo crónico; montelukast reduce la lesión bronquial post-trasplante |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Estudio piloto | Respiratory Medicine | Montelukast adyuvante vs. doble dosis de budesonida en NAEB: efecto antiinflamatorio aditivo sobre eosinofilia bronquial |
| [25846070](https://pubmed.ncbi.nlm.nih.gov/25846070/) | 2016 | Estudio clínico | World Journal of Pediatrics | Bronquiolitis por VRS con co-infección por M. pneumoniae: la terapia adyuvante con montelukast reduce la severidad y duración de síntomas |

---

## Información de Mercado en Argentina

Montelukast **no cuenta con autorizaciones de comercialización registradas en Argentina** (ANMAT). El total de licencias vigentes es 0 y el estado de mercado es no comercializado.

> **Contexto global:** A nivel internacional, montelukast está aprobado como Singulair® (Merck) y numerosos genéricos en más de 100 países — incluidos EE.UU. (FDA), Unión Europea (EMA) y Japón — para asma bronquial (desde 6 meses de edad en EE.UU.) y rinitis alérgica. La ausencia de registro en Argentina representa una barrera regulatoria significativa para cualquier estrategia de reposicionamiento local.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa.

> **Alerta prioritaria:** La FDA emitió en 2020 una **advertencia de recuadro negro (Black Box Warning)** sobre eventos adversos neuropsiquiátricos asociados a montelukast: cambios de conducta, agitación, ansiedad, depresión, alucinaciones, pensamientos suicidas y pesadillas. Múltiples estudios de cohorte publicados entre 2019 y 2025 (PMID: 30905424, 37758273, 36948487, 35608857, 39836401, 39578088) han investigado esta asociación, con resultados heterogéneos pero que confirman el riesgo real, especialmente en niños. Esta advertencia debe ser considerada obligatoriamente en cualquier plan de desarrollo clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un cuerpo de evidencia clínica de Nivel L2 — incluyendo un ECA de Fase 3 completado (NCT00076973, n=1 125), múltiples estudios de Fase 2/4 completados y 20 publicaciones revisadas — que respalda el uso de montelukast en diversas formas de patología bronquial (bronquiolitis viral, bronquitis obstructiva recurrente, bronquitis eosinofílica no asmática y bronquiolitis obliterante). La sólida base mecanística mediante el bloqueo de CysLT1 fundamenta razonablemente la predicción del modelo TxGNN; sin embargo, la ausencia de registro en Argentina, la heterogeneidad de los subtipos de bronquitis estudiados y la advertencia neuropsiquiátrica Black Box de la FDA exigen guardrails específicos antes de avanzar.

**Para avanzar se necesita:**
- Obtener los datos completos de mecanismo de acción (MOA) y perfil de seguridad desde DrugBank (DG002) y el prospecto oficial (DG001)
- Definir el subtipo de bronquitis objetivo con mayor potencial de beneficio (bronquitis obstructiva recurrente pediátrica es el candidato más sólido según la evidencia disponible)
- Evaluar factibilidad y cronograma de registro ante ANMAT, considerando la posibilidad de uso bajo el marco de indicación no aprobada o de desarrollo clínico local
- Diseñar un protocolo de monitoreo prospectivo de eventos adversos neuropsiquiátricos acorde a la advertencia FDA 2020, con especial atención en población pediátrica
- Realizar una revisión sistemática focalizada en bronquitis recurrente obstructiva para cuantificar el tamaño del efecto en ese subtipo específico
- Confirmar disponibilidad de formulaciones pediátricas (gránulos 4 mg, comprimidos masticables 5 mg) en el mercado de proveedores para Argentina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

