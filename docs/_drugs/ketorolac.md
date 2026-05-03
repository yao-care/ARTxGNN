---
layout: default
title: Ketorolac
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 3
---

# Ketorolac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Usando `txgnn-pipeline` para generar el informe de evaluación de reposicionamiento a partir del Evidence Pack de KETOROLAC.

---

# Ketorolac: De Analgesia Aguda a Trastorno de Cefalea

## Resumen en Una Frase

Ketorolac es un antiinflamatorio no esteroideo (AINE) no selectivo que inhibe las enzimas COX-1 y COX-2, utilizado ampliamente para el manejo del dolor agudo de moderado a severo en entornos hospitalarios y de urgencias.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno de Cefalea** (incluyendo migraña aguda y cefalea tensional),
con **múltiples ensayos clínicos completados** y **19 publicaciones científicas** que actualmente respaldan esta dirección con un nivel de evidencia L1.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor agudo (AINE sistémico, uso parenteral/nasal) |
| Nueva Indicación Predicha | Trastorno de Cefalea (headache disorder) |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | ✗ No Comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Ketorolac es un inhibidor no selectivo de las enzimas COX-1 y COX-2, que bloquea la conversión del ácido araquidónico en prostaglandinas —particularmente PGE₂— reduciendo así la neuroinflamación periférica. Si bien los datos formales de mecanismo de acción no están disponibles en el sistema regulatorio argentino (el fármaco no tiene autorizaciones locales), la justificación mecanística está bien documentada en la literatura: en la fisiopatología de la migraña, la PGE₂ promueve la sensibilización de las terminaciones nerviosas del sistema trigémino-vascular y facilita la sensibilización central, cadena que Ketorolac interrumpe directamente.

La relación entre el uso analgésico original y el trastorno de cefalea es mecánicamente directa y no especulativa. La migraña y la cefalea tensional comparten un componente inflamatorio mediado por prostaglandinas que constituye el blanco farmacológico primario de los AINEs. Las formulaciones sistémicas (IV, IM) y nasal (spray intransal) de Ketorolac alcanzan concentraciones terapéuticas que inhiben la síntesis de PGE₂ tanto a nivel central como periférico, lo que es altamente compatible con la fisiopatología de los trastornos de cefalea primaria.

Más allá del mecanismo, la evidencia clínica ya ha validado esta indicación en la práctica: las Guías de la American Headache Society (2015, 2026) y la Canadian Headache Society (2015) reconocen a Ketorolac como una opción terapéutica establecida para el manejo agudo de la migraña en servicios de urgencias. Múltiples ensayos de Fase 2, 3 y 4 completados —en adultos y población pediátrica— y metaanálisis actualizados confirman su eficacia. La predicción de TxGNN (99.43%) refleja fielmente una indicación que ya cuenta con respaldo clínico robusto.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Fase 4 | Completado | 72 | Comparación directa de Ketorolac nasal vs Sumatriptán nasal vs placebo para el tratamiento abortivo agudo de la migraña, incluyendo náuseas y alodinia |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Fase 2 | Completado | 173 | Ensayo doble ciego randomizado controlado con placebo que evalúa seguridad, tolerabilidad y eficacia analgésica de Ketorolac intranasal para migraña aguda |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Fase 3 | Completado | 59 | Ensayo de no inferioridad: Ketorolac intranasal vs intravenoso en migraña pediátrica; la vía nasal ofrece administración sin punción venosa |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Fase 4 | Completado | 330 | Comparación aleatorizada de valproato IV, metoclopramida IV y Ketorolac IV para migraña aguda en urgencias |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Fase 4 | Completado | 123 | Metoclopramida/difenhidramina vs Ketorolac en monoterapia para cefalea tensional aguda en urgencias |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Fase 4 | Completado | 56 | Evaluación de la terapia combinada de Ketorolac IV + metoclopramida para migraña pediátrica en urgencias |
| [NCT05641363](https://clinicaltrials.gov/study/NCT05641363) | Fase 3 | Completado | 171 | Comparación de tres dosis de Ketorolac en niños con dolor agudo; proporciona datos de seguridad por rango de dosis en pediatría |
| [NCT05102591](https://clinicaltrials.gov/study/NCT05102591) | Fase 3 | Completado | 22 | Dispositivo de neuromodulación vs Ketorolac (control estándar) en ataques agudos de migraña pediátrica en urgencias; confirma el rol de Ketorolac como estándar de referencia |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Fase 3 | Completado | 80 | Ketamina intranasal vs terapia estándar (incluye Ketorolac) para cefalea primaria aguda en urgencias |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Fase 4 | Desconocido | 60 | Ketamina subdisociativa vs Ketorolac para cefalea tensional aguda en urgencias; evalúa NRS como desenlace primario |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía Clínica | Headache | Actualización 2025 de la American Headache Society sobre farmacoterapias parenterales para migraña en urgencias; incluye evaluación actualizada de Ketorolac |
| [39674934](https://pubmed.ncbi.nlm.nih.gov/39674934/) | 2025 | Revisión Sistemática / Metaanálisis | Annals of Emergency Medicine | Revisión sistemática con metaanálisis bayesiano en red sobre eficacia y seguridad de terapias farmacológicas para migraña en urgencias en adultos |
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Revisión Sistemática / Metaanálisis | Academic Emergency Medicine | Metaanálisis específico sobre la eficacia de Ketorolac parenteral en el tratamiento del ataque agudo de migraña |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Revisión Sistemática | Advances in Clinical and Experimental Medicine | Revisión sistemática actualizada que compara Ketorolac IV vs metoclopramida para migraña en adultos |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | ECA | Headache | ECA que evalúa monoterapia con metoclopramida IV vs combinación con Ketorolac IV en migraña pediátrica aguda en urgencias |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guía Clínica | Headache | Evaluación de evidencia de la American Headache Society para farmacoterapias agudas de migraña; reconoce a Ketorolac como opción evidenciada |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | ECA | Annals of Emergency Medicine | Ensayo prospectivo doble ciego: Ketorolac IM vs meperidina + hidroxizina para migraña aguda; estudio fundacional de la indicación |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | Estudio Comparativo | Neurological Sciences | ECA doble ciego que compara dexametasona, metoclopramida, Ketorolac y clorpromazina IV para alivio del dolor y prevención de recurrencia en migraña |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Metaanálisis en Red | BMC Neurology | Metaanálisis en red de ECAs que compara metoclopramida vs otros fármacos antimigrañosos, incluyendo Ketorolac como comparador activo |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revisión Sistemática | Cephalalgia | Revisión sistemática y recomendaciones de la Canadian Headache Society para el tratamiento del dolor en migraña en urgencias |

---

## Información de Mercado en Argentina

Ketorolac **no cuenta con autorizaciones de comercialización registradas** en Argentina (ANMAT) según los datos disponibles en el Evidence Pack. No es posible listar productos aprobados localmente.

> Este hallazgo no implica que el fármaco sea ineficaz o inseguro, sino que no ha sido registrado formalmente en el mercado argentino en los datos consultados. Globalmente, Ketorolac es un fármaco aprobado por la FDA (EE.UU.), la EMA (Europa) y múltiples agencias regulatorias bajo marcas como Toradol®, y es ampliamente utilizado en entornos hospitalarios a nivel mundial.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota de interés clínico identificada en la literatura**: Un reporte de caso (PMID [7928331](https://pubmed.ncbi.nlm.nih.gov/7928331/)) documentó toxicidad por litio inducida por Ketorolac en un paciente con cefalea en racimos tratado con litio. Aunque la interacción AINE–litio es conocida para la clase, este caso específico con Ketorolac debe tenerse en cuenta al evaluar pacientes con TAC que reciben litio como profilaxis.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción de TxGNN (99.43%) está respaldada por un nivel de evidencia L1: múltiples ensayos clínicos de Fase 3/4 completados, dos guías clínicas de sociedades de cefalea de primer nivel (AHS 2015/2026, CHS 2015) y al menos dos metaanálisis recientes confirman la eficacia de Ketorolac para la migraña aguda y la cefalea tensional en urgencias, tanto en adultos como en población pediátrica. La base mecanística (inhibición COX/PGE₂ en el sistema trigémino-vascular) es sólida y directamente alineada con la fisiopatología de los trastornos de cefalea. La única barrera significativa es la ausencia de autorización regulatoria local en Argentina.

**Para avanzar se necesita:**
- Iniciar proceso de registro ante ANMAT con respaldo de evidencia de Fase 3/4 ya disponible
- Obtener y analizar el prospecto formal (MOA, advertencias y contraindicaciones) para completar la evaluación de seguridad de Nivel S1
- Definir la población objetivo prioritaria (adultos en urgencias vs. uso pediátrico) y la vía de administración preferida (IV/IM vs. intranasal)
- Evaluar interacciones farmacológicas relevantes para la práctica clínica argentina (especialmente con litio en contexto de TAC, y con anticoagulantes dado el perfil AINE)
- Revisar si existen productos con Ketorolac registrados en países limítrofes (p. ej., Chile, Brasil) que puedan agilizar el expediente regulatorio por reconocimiento mutuo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

