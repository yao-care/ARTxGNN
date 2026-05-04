---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 7
---

# Salmeterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Salmeterol: De Asma Bronquial a Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista β2-adrenérgico de larga duración (LABA) utilizado internacionalmente como tratamiento de mantenimiento del asma bronquial y la enfermedad pulmonar obstructiva crónica (EPOC), si bien actualmente no cuenta con registro comercial en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con **16 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección.
La predicción alcanza una puntuación de confianza del 99.92% y está clasificada como nivel de evidencia L1, el más alto posible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma bronquial / EPOC (uso internacional establecido; sin registro en Argentina) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Salmeterol actúa como agonista selectivo del receptor β2-adrenérgico, activando la adenilil ciclasa a través de la proteína Gs. Este proceso eleva los niveles intracelulares de AMPc, desencadena la fosforilación de la quinasa de cadena ligera de miosina (MLCK) e inhibe su actividad, produciendo una relajación sostenida del músculo liso bronquial durante al menos 12 horas. De forma complementaria, suprime la liberación de histamina, leucotrienos y otros mediadores inflamatorios por parte de mastocitos y basófilos.

La bronquitis crónica es el subtipo principal de la EPOC: su patología central consiste en hipersecreción de moco, inflamación persistente de las vías aéreas y obstrucción progresiva al flujo de aire. Salmeterol actúa directamente sobre estos tres mecanismos al mejorar el aclaramiento mucociliar y reducir la resistencia de la vía aérea. El estudio PMID 15970448 (ECA cruzado, n=14) demostró específicamente que salmeterol mejora el aclaramiento mucociliar y tusígeno en pacientes con bronquitis crónica leve-moderada, lo que representa una validación clínica directa del vínculo mecanístico predicho por TxGNN.

La combinación FP/salmeterol (Seretide/Advair) está aprobada en Estados Unidos para el tratamiento de la EPOC asociada a bronquitis crónica, y en la Unión Europea para EPOC severa. Múltiples ensayos de Fase 3 con comparaciones directas head-to-head (NCT02173691, n=584; NCT00064402, n=741) confirman la eficacia y seguridad de salmeterol en esta población. La predicción del modelo TxGNN coincide plenamente con la práctica clínica internacional ya establecida.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Comparación directa de 6 meses entre Tiotropium, Salmeterol aerosol y placebo en EPOC/bronquitis crónica; evidencia head-to-head más sólida disponible para salmeterol en esta indicación |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Estudio doble ciego, aleatorizado, multicéntrico con salmeterol como control activo; evalúa efecto broncodilatador en EPOC durante 12 semanas con el mayor tamaño muestral del conjunto |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completado | 2000 | Investigación especial post-comercialización de ADOAIR (salmeterol+fluticasona) en EPOC/bronquitis crónica; foco en neumonía; proporciona datos de seguridad de mundo real a gran escala |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Fase 4 | Completado | 249 | FP/Salmeterol DISKUS 250/50mcg BID vs placebo en EPOC durante 16 semanas; evalúa rigidez arterial como marcador de riesgo cardiovascular asociado a bronquitis crónica |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Fase 4 | Completado | 247 | Comparación doble ciego, doble enmascarado de FSC HFA MDI vs FSC DISKUS en EPOC/bronquitis crónica durante 12 semanas; demuestra equivalencia de eficacia entre dispositivos |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Estudio doble ciego de 13 semanas evaluando actividad antiinflamatoria bronquial de salmeterol/fluticasona vs placebo; directamente relevante para la patología inflamatoria de la bronquitis |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | Búsqueda de dosis de FP/formoterol comparado con Advair Diskus (FP/salmeterol) como referencia en EPOC; evalúa rango de dosis seguras del componente salmeterol |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Comparación de dos medicamentos en EPOC durante 18 semanas con 5 visitas clínicas; pruebas de función pulmonar y registro diario de síntomas respiratorios |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Fase 4 | Completado | 639 | FP/salmeterol 250/50mcg BID vs salmeterol 50mcg BID en tasa de exacerbaciones de EPOC tras hospitalización; 29 semanas de seguimiento; compara el valor añadido del corticosteroide sobre el LABA solo |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Fase 4 | Desconocido | 20 | Comparación de arformoterol nebulizado vs salmeterol en polvo seco en EPOC; evaluación de apertura de pequeñas vías aéreas mediante pruebas espirométricas e imagen HRCT |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | ECA cruzado | Pulm Pharmacol Ther | Salmeterol mejora significativamente el aclaramiento mucociliar y tusígeno en bronquitis crónica leve-moderada (n=14) frente a placebo; validación mecanística directa en la indicación predicha |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | ECA | Chest | FP/salmeterol 250/50mcg vs placebo e individuales en EPOC; mejora significativa de FEV1, síntomas diurnos y calidad de vida en pacientes con bronquitis crónica |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | ECA | Clin Ther | Salmeterol inhalado 50mcg vs teofilina oral en EPOC leve-moderada (n múltiple); salmeterol superior en tolerabilidad, mejora de flujo espiratorio pico y calidad de vida |
| [31852314](https://pubmed.ncbi.nlm.nih.gov/31852314/) | 2020 | ECA / Meta-análisis | J Int Med Res | FP/formoterol vs FP/salmeterol en asma pediátrica durante 12 semanas; perfil de eficacia y seguridad equivalente entre ambas formulaciones LABA/ICS |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte retrospectiva | Curr Med Res Opin | FSC 250/50mcg reduce significativamente el riesgo de hospitalización y visitas a urgencias en bronquitis crónica frente a otras terapias inhaladas de mantenimiento |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Estudio comparativo retrospectivo | Ther Adv Respir Dis | Salmeterol durante 12 meses en EPOC: perfil de seguridad favorable, sin desarrollo de tolerancia broncodilatadora apreciable con el uso prolongado |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía clínica | Basic Clin Pharmacol Toxicol | Guías finlandesas de EPOC estable: salmeterol recomendado como broncodilatador de larga acción de elección en todos los estadios de la enfermedad |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Revisión | Drugs Today | Pacientes con EPOC y bronquitis crónica presentan mayor riesgo de exacerbaciones y deterioro de función pulmonar; revisión del contexto farmacológico de broncodilatadores vs antiinflamatorios |
| [21316553](https://pubmed.ncbi.nlm.nih.gov/21316553/) | 2010 | Revisión | Arch Bronconeumol | Los síntomas típicos de bronquitis crónica (tos y producción de esputo) se correlacionan con marcadores inflamatorios en EPOC y predicen mayor morbimortalidad por exacerbaciones |
| [20649375](https://pubmed.ncbi.nlm.nih.gov/20649375/) | 2010 | Revisión | Expert Rev Respir Med | Revisión de ensayos de Fase III en EPOC: salmeterol utilizado ampliamente como comparador activo de referencia en estudios de nuevos broncodilatadores para bronquitis crónica |

---

## Información de Mercado en Argentina

Salmeterol **no cuenta con ninguna autorización de comercialización registrada en Argentina**. El mercado local no dispone de presentaciones autorizadas bajo este principio activo, ni en formulación única (monoproducto) ni en combinaciones fijas (por ejemplo, salmeterol/fluticasona). La ausencia de registro es un factor crítico a considerar en cualquier estrategia de desarrollo o introducción de este fármaco en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3 con comparación directa head-to-head respaldan la eficacia de salmeterol en EPOC y bronquitis crónica, y la combinación FP/salmeterol ya cuenta con aprobación regulatoria internacional para esta indicación específica; el cuerpo de evidencia es suficiente para avanzar, con los controles de seguridad apropiados.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (MOA) desde la API de DrugBank (brecha de datos de severidad Alta identificada)
- Descargar y analizar el prospecto oficial para extraer advertencias, contraindicaciones y precauciones de uso (brecha de datos Bloqueante identificada)
- Evaluar la viabilidad de registro sanitario en Argentina: dado que no existe ninguna autorización vigente, se requiere una estrategia de registro completa desde cero
- Definir la estrategia de combinación obligatoria con corticosteroide inhalado (ICS): el uso de LABA como monoterapia en asma porta advertencia de caja negra FDA (estudio SMART); la combinación ICS+LABA es el estándar de cuidado
- Establecer un plan de monitoreo de seguridad cardiovascular para poblaciones con comorbilidades cardíacas, dado el efecto beta-adrenérgico sistémico residual
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

