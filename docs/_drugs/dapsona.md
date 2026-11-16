---
layout: default
title: Dapsona
parent: Evidencia Alta (L1-L2)
nav_order: 127
evidence_level: L1
indication_count: 1
drugbank_id: DB00250
monitor_inn: "Dapsone"
predicted_indications: ["pneumocystosis"]
last_modified_at: 2026-11-16
description: "Dapsona: nueva indicación predicha, neumocistosis (pneumocystosis) (nivel de evidencia L1). Indicación original: No consta en los datos locales"
---

# Dapsona
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

## Dapsona: neumocistosis (pneumocystosis)
{: .text-alpha }

## Resumen en Una Frase

Dapsona es un antibacteriano del grupo de las sulfonas, comercializado actualmente en Argentina.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis (pneumocystosis)**, con **10 ensayos clínicos** y **19 publicaciones** compilados en los datos de este informe, que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | neumocistosis (pneumocystosis) |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (2 de 2) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 2 (vigentes: 2) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción de forma detallada. Según el conocimiento farmacológico general, la dapsona es una sulfona que inhibe la dihidropteroato sintasa (DHPS) en la vía de síntesis de folatos, el mismo blanco que las sulfonamidas como el sulfametoxazol.

*Pneumocystis jirovecii* posee la enzima DHPS, por lo que la dapsona (habitualmente combinada con trimetoprima en el tratamiento) bloquea la síntesis de folatos del organismo. Esto es coherente con el puntaje alto de TxGNN y con su uso clínico establecido como alternativa para la profilaxis y el tratamiento de la neumonía por *Pneumocystis* leve a moderada en pacientes que no toleran trimetoprima-sulfametoxazol.

Esta explicación mecanística proviene de conocimiento farmacológico general y no de un registro suministrado, por lo que debe confirmarse con una fuente como DrugBank.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Fase 3 | Completado | 700 | Dapsona diaria vs. atovacuona diaria en profilaxis de PCP en pacientes con VIH intolerantes a trimetoprima/sulfonamidas |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Fase 3 | Completado | 400 | Pentamidina en aerosol mensual vs. dapsona tres veces por semana en profilaxis de PCP |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fase 3 | Completado | 290 | Dapsona/trimetoprima y clindamicina/primaquina vs. trimetoprima-sulfametoxazol en PCP leve a moderada |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fase 3 | Completado | 600 | Tres regímenes anti-Pneumocystis más zidovudina en prevención primaria en VIH avanzado |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Fase 1 | Completado | 96 | Dapsona diaria vs. semanal en profilaxis de PCP en niños con VIH (toxicidad y farmacocinética) |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Fase 1 | Completado | 20 | Trimetrexato con leucovorina más dapsona vs. TMP/SMX en PCP moderadamente grave |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | No reportada | Completado | No disponible | Dapsona 100 mg vs. 50 mg en profilaxis primaria de PCP en pacientes con complejo relacionado con el SIDA |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | No reportada | Completado | No disponible | Dapsona más trimetoprima vs. TMP/SMX en el primer episodio de PCP en SIDA |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Fase 4 | Desconocido | 3130 | Tamizaje genético HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona (evidencia de seguridad, no de eficacia) |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Fase 4 | Retirado | 0 | Corticoides orales y fibrosis intersticial en PCP; no evalúa dapsona |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revisión sistemática y metaanálisis en red de ECA | Clin Microbiol Infect | Compara eficacia y seguridad de regímenes de profilaxis de PCP (TMP-SMX, regímenes con dapsona, pentamidina en aerosol, atovacuona) en personas con VIH |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revisión sistemática y metaanálisis en red de ECA | Clin Microbiol Infect | Compara regímenes de tratamiento de PCP en personas con VIH; TMP-SMX sigue siendo el tratamiento principal |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guía | J Antimicrob Chemother | Guías ECIL para prevenir PCP en neoplasias hematológicas y trasplante de progenitores; TMP-SMX es de elección |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revisión | Expert Opin Pharmacother | Revisión de *P. jirovecii* con foco en prevención y tratamiento |
| [28782390](https://pubmed.ncbi.nlm.nih.gov/28782390/) | 2017 | Revisión | Expert Rev Anti Infect Ther | Tratamiento de la neumonía por *Pneumocystis* en pacientes con VIH; resistencia por mutaciones en DHPS |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Revisión | J Formos Med Assoc | Neumonía por *Pneumocystis* como principal infección oportunista en el SIDA |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revisión | Dermatol Clin | Dapsona y sulfapiridina; útil en la profilaxis de neumonía por *Pneumocystis* en VIH |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Revisión retrospectiva de casos | Pediatr Transplant | Metahemoglobinemia por dapsona en niños trasplantados renales que la usan como profilaxis |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Reporte de caso | Ann Pharmacother | Metahemoglobinemia en paciente con dapsona como profilaxis de PCP |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Reporte de caso | Cureus | Hipoxia por metahemoglobinemia inducida por dapsona |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 51571 | DAPSONA LAZAR | 100 mg comprimidos x 50 |
| 8465 | D.A.P.S. | 100 mg comprimidos x 100 |

## Consideraciones de Seguridad

Consultar el prospecto para obtener la información de seguridad de la autorización local.

Según la literatura compilada, se recomienda como medidas de resguardo el tamizaje de deficiencia de G6PD antes del uso y el monitoreo de metahemoglobinemia, hemólisis e hipoxia, además de eventos raros como pancreatitis. El estudio NCT02550080 evalúa además el tamizaje de HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados evalúan dapsona o regímenes con dapsona en la profilaxis y el tratamiento de la neumonía por *Pneumocystis*, y metaanálisis recientes comparan estos regímenes. Sin embargo, la dapsona es una alternativa para pacientes que no toleran TMP-SMX y exige controles de seguridad hematológica.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto aprobado por ANMAT (advertencias y contraindicaciones)
- Confirmar el mecanismo de acción con una fuente como DrugBank
- Definir un plan de tamizaje de G6PD y monitoreo de metahemoglobinemia y hemólisis
- Verificar la indicación autorizada localmente frente al uso propuesto
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

