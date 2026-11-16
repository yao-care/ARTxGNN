---
layout: default
title: Itraconazol
parent: Solo Predicción del Modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
drugbank_id: DB01167
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
last_modified_at: 2026-11-16
description: "Itraconazol: nueva indicación predicha, Neumocistosis (pneumocystosis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Itraconazol
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

## Itraconazol: Neumocistosis (pneumocystosis)
{: .text-alpha }

## Resumen en Una Frase

Itraconazol es un antifúngico triazólico comercializado en Argentina en varias presentaciones.
El modelo TxGNN predice que podría ser efectivo para **Neumocistosis (pneumocystosis)**,
pero no hay **ningún ensayo clínico** y las **20 publicaciones** recuperadas solo mencionan al itraconazol de forma indirecta, por lo que la evidencia directa es nula.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neumocistosis (pneumocystosis) |
| Puntaje de Predicción TxGNN | 0.9934 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (20 de 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 20 (vigentes: 20) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Itraconazol es un antifúngico triazólico que inhibe la enzima lanosterol 14-alfa-desmetilasa (CYP51) de los hongos, bloqueando la síntesis de ergosterol de la membrana celular.

Sin embargo, *Pneumocystis jirovecii* carece de ergosterol en su membrana y utiliza colesterol y otros esteroles, por lo que el mecanismo clásico de los azoles no se espera que sea eficaz. El puntaje alto (0,9934) probablemente refleja la cercanía en la red de relaciones con otras infecciones fúngicas y oportunistas, y no un mecanismo validado.

La literatura recuperada menciona al itraconazol sobre todo en la profilaxis o el tratamiento de otras infecciones fúngicas (histoplasmosis, infección por *Emmonsia*, infecciones fúngicas invasivas en pacientes trasplantados y neutropénicos), en poblaciones que también tienen riesgo de neumocistosis. Esto es coincidencia indirecta, no evidencia de actividad contra *Pneumocystis*. El tratamiento y la profilaxis de primera línea es trimetoprima-sulfametoxazol, con alternativas como pentamidina, atovacuona y dapsona.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de las publicaciones estudia directamente el itraconazol en neumocistosis. Se destacan las más relevantes (el tipo indicado es el clasificado en los datos compilados):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisión | Clin Infect Dis | Profilaxis antimicrobiana en neutropenia febril; trimetoprima-sulfametoxazol es muy eficaz para prevenir la neumonía por *Pneumocystis* |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones sistémicas por protozoos, incluido *Pneumocystis carinii* |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisión | Semin Respir Infect | Infecciones tras trasplante pulmonar y estrategias de prevención |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisión | BMJ Clin Evid | Profilaxis primaria y secundaria de infecciones oportunistas en VIH |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplant Proc | Infecciones fúngicas invasivas tras trasplante renal en un centro |
| [7859871](https://pubmed.ncbi.nlm.nih.gov/7859871/) | 1995 | Cohorte | Eur J Haematol | Tratamiento de soporte ambulatorio en leucemia mieloide aguda con ciprofloxacino, cotrimoxazol e itraconazol |
| [29374650](https://pubmed.ncbi.nlm.nih.gov/29374650/) | 2018 | Reporte de caso | BMJ Case Rep | Coinfección de *P. jirovecii* e histoplasmosis pulmonar en un paciente con VIH |
| [14760976](https://pubmed.ncbi.nlm.nih.gov/14760976/) | 2003 | Reporte de caso | Int J Med Microbiol | Infección granulomatosa pulmonar por *Emmonsia* inicialmente interpretada como neumonía por *Pneumocystis* |
| [8187612](https://pubmed.ncbi.nlm.nih.gov/8187612/) | 1994 | Reporte de caso | Dtsch Med Wochenschr | Histoplasmosis diseminada en SIDA, inicialmente tratada como neumonía por *Pneumocystis* |

## Información de Mercado en Argentina

El itraconazol está comercializado en Argentina con 20 autorizaciones vigentes, todas de productos de un solo principio activo. Principales presentaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28998 | SPORANOX | Cápsulas x 10 | No registrada |
| 21742 | SPORANOX PULSO | Cápsulas x 28 | No registrada |
| 25700 | SPORANOX | Solución oral x 150 ml | No registrada |
| 35342 | MICOTENK | Comprimidos recubiertos 100 mg x 30 | No registrada |
| 52804 | SALIMIDIN 200 | Cápsulas 200 mg x 21 | No registrada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen directamente el itraconazol en neumocistosis, y el mecanismo conocido (inhibición de ergosterol) no es plausible porque *Pneumocystis* carece de ergosterol. El puntaje alto del modelo no está respaldado por evidencia real, y existen tratamientos de primera línea bien establecidos.

**Para avanzar se necesita:**
- Estudios preclínicos que demuestren actividad del itraconazol contra *Pneumocystis jirovecii*
- Datos del mecanismo de acción que justifiquen una vía alternativa a la inhibición de CYP51
- Información de seguridad del prospecto de ANMAT (advertencias, contraindicaciones e interacciones)
- Comparación con trimetoprima-sulfametoxazol, pentamidina, atovacuona y dapsona antes de considerar cualquier ensayo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

