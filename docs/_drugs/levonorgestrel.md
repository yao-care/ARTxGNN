---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Con base en el Evidence Pack proporcionado, procedo a generar el informe de evaluación de reposicionamiento.

---

# Levonorgestrel: De Anticoncepción Hormonal a Acné

## Resumen en Una Frase

Levonorgestrel es un progestágeno sintético ampliamente utilizado a nivel mundial como anticonceptivo hormonal (anticonceptivo oral combinado, DIU liberador de hormonas, implante subdérmico y anticoncepción de emergencia), aunque actualmente no cuenta con registro en Argentina (ANMAT).
El modelo TxGNN predice que podría ser efectivo para el **Acné (enfermedad)**, con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Sin embargo, la relación mecanística es compleja y bidireccional, lo que requiere una evaluación cautelosa antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción hormonal (no registrado en Argentina) |
| Nueva Indicación Predicha | Acné (enfermedad) |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de levonorgestrel en este Evidence Pack. Sin embargo, a partir de la literatura recopilada es posible reconstruir el fundamento mecanístico. Levonorgestrel es un progestágeno de 19-nortestosterona con actividad androgénica significativa (PMID 7825629). El acné es una enfermedad multifactorial en la que los andrógenos juegan un rol central al estimular la hipersecreción sebácea y la proliferación folicular, lo que crea una conexión directa entre la farmacología de levonorgestrel y la fisiopatología del acné.

La relación es, no obstante, **bidireccional**: cuando levonorgestrel se administra en solitario (DIU, implante subdérmico), su actividad androgénica residual puede **empeorar** el acné, como se documentó en reportes clínicos del sistema LNG-IUS. En cambio, cuando se combina con etinilestradiol (EE) en anticonceptivos orales combinados, el efecto del estrógeno —que incrementa la globulina transportadora de hormonas sexuales (SHBG) y reduce los andrógenos libres circulantes— supera al efecto androgénico de LNG, resultando en una **mejoría neta del acné** (PMID 12196750, PMID 10717776).

Esta dualidad mecanística implica que la predicción TxGNN no captura un efecto directo de levonorgestrel sobre el acné, sino el efecto de la **combinación EE/LNG como entidad farmacológica**. La pregunta de reposicionamiento debe reformularse para especificar la formulación (combinación oral vs. formulación solo-progestágeno) antes de poder avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminado | 44 | Estudio de LNG-IUS para prevención de cáncer endometrial; el protocolo menciona el acné como efecto adverso de progestinas orales, pero el estudio fue terminado prematuramente y no aporta evidencia de eficacia para acné |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completado | 101,498 | Estudio de cohorte de gran escala que compara NOMAC-E2 vs. anticonceptivos orales combinados con LNG; el acné puede estar incluido como endpoint de seguridad secundario. Datos comparativos de relevancia indirecta |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Fase 2 | Desconocido | 60 | Comparación de Mirena vs. megestrol para hiperplasia endometrial atípica; el objetivo principal es la preservación de fertilidad, sin relación directa con acné |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completado | 131 | Anticonceptivos orales continuos combinados con doxiciclina (antibiótico estándar para acné); los datos podrían contener información sobre el impacto cutáneo, pero el endpoint primario es el sangrado uterino irregular |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Fase 2 | Completado | 100 | Implante de gestrinone (derivado de 19-nortestosterona, clase similar a LNG) para dolor pélvico por endometriosis; diseño doble ciego multicéntrico de alta calidad, aunque el agente activo no es levonorgestrel |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | Ensayo Clínico | J Am Acad Dermatol | ECA de EE 20 µg / LNG 100 µg para acné moderado; demuestra mejoría de marcadores bioquímicos de androgenicidad y reducción de lesiones de acné. Evidencia más directa disponible para EE/LNG en acné |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | Ensayo Clínico | Contraception | Estudio multicéntrico aleatorizado de OC de baja dosis con EE 20 µg + LNG vs. otro progestágeno; compara perfiles androgénicos bioquímicos y resultados clínicos incluyendo acné |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Revisión | Drugs | EE/clormadinona demostró mayor eficacia que EE/LNG 0.03/0.15 mg para acné papulopustular leve-moderado; posiciona al LNG como comparador activo de menor eficacia antiandrogénica |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Revisión | J Women's Health | Revisión comparativa de drospirenona vs. medroxiprogesterona, LNG y progesterona micronizada; documenta que las propiedades antiandrogénicas de drospirenona reducen acné vulgaris en comparación con LNG |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Revisión | Am J Medicine | Análisis del índice androgénico de progestágenos; documenta explícitamente el alto índice androgénico de LNG como progestágeno de serie 19-nortestosterona, base mecanística para los efectos cutáneos |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Revisión | Am J Clin Dermatol | Revisión de beneficios dermatológicos de EE/clormadinona en acné, hirsutismo y seborrea; contextualiza el rol del exceso androgénico en la unidad pilosebácea y el papel de los OC combinados |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Revisión | Semin Reprod Med | Revisión del sistema intrauterino liberador de LNG; documenta el acné como efecto adverso reportado asociado al efecto androgénico sistémico residual del LNG-IUS |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Revisión Cochrane | Cochrane Database Syst Rev | Revisión sistemática de LNG-IUS para hiperplasia endometrial; incluye perfil de seguridad cutánea como efecto adverso relevante |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Observacional | Human Reproduction | Estudio de LNG-IUS para endometriosis; evalúa efectos sistémicos del LNG administrado intrauterinamente, incluyendo efectos adversos androgénicos sobre piel |
| [2403935](https://pubmed.ncbi.nlm.nih.gov/2403935/) | 1990 | Revisión | Fertility and Sterility | Perspectiva sobre lípidos, enfermedad cardiovascular y anticonceptivos orales; analiza el impacto diferencial de distintos progestágenos (incluido LNG) sobre parámetros metabólicos y endocrinos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN no refleja un efecto de levonorgestrel *per se* sobre el acné, sino el efecto de la combinación EE/LNG, dado que el componente androgénico de LNG puede en realidad empeorar el acné cuando se administra sin estrógeno. Además, la falta de registro en Argentina (0 autorizaciones ANMAT) y la ausencia de datos MOA confirmados impiden una evaluación mecanística completa.

**Para avanzar se necesita:**
- Reformular la pregunta de reposicionamiento especificando la formulación exacta (¿LNG solo o EE/LNG combinado?)
- Confirmar el mecanismo de acción detallado (MOA) mediante consulta a DrugBank API
- Descargar e interpretar el prospecto para obtener advertencias, contraindicaciones e interacciones farmacológicas
- Evaluar si existe factibilidad regulatoria en Argentina para anticonceptivos orales combinados con LNG para la indicación de acné
- Identificar ensayos clínicos específicos que testen LNG (no la combinación) para acné moderado-severo como endpoint primario
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

