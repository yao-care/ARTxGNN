---
layout: default
title: Mupirocin
parent: Solo Predicción del Modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 2
monitor_inn: "mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-24
description: "Mupirocin: nueva indicación predicha, Empiema pleural (pleural empyema) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 10 (en el listado vigente: 10)"
---

# Mupirocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Mupirocina: antibiótico tópico inhibidor de la isoleucil-tRNA sintetasa → Empiema pleural (pleural empyema)
{: .text-alpha }

## Resumen en Una Frase

Mupirocina es un antibiótico de uso tópico que actúa inhibiendo la isoleucil-tRNA sintetasa bacteriana.
El modelo TxGNN predice que podría ser efectivo para **Empiema pleural (pleural empyema)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Empiema pleural (pleural empyema) |
| Puntaje de Predicción TxGNN | 0,9949 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (10 de 10) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 10 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Mupirocina inhibe la isoleucil-tRNA sintetasa bacteriana y es activa sobre todo contra cocos Gram positivos como *Staphylococcus aureus* (incluido el SARM) y *Streptococcus* spp. Estos microorganismos son causas frecuentes de empiema pleural, lo que ofrece una justificación antibacteriana plausible.

Sin embargo, existe una limitación importante de vía de administración: mupirocina está aprobada solo para uso tópico y su exposición sistémica es insignificante, porque se metaboliza rápidamente a ácido mónico inactivo. Por ello es poco probable que alcance concentraciones terapéuticas en el espacio pleural por vía sistémica, y no hay datos que respalden la administración intrapleural.

El puntaje elevado (0,9949) es una predicción computacional y probablemente refleja una asociación general con "infección bacteriana" más que una vía farmacológicamente viable. Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Mupirocin (traducción no oficial): «La mupirocina es un antibacteriano inhibidor de la ARN sintetasa. […] La mupirocina inhibe la síntesis de proteínas bacterianas mediante la unión reversible y específica a la isoleucil-ARN de transferencia (ARNt) sintetasa bacteriana. La mupirocina es bactericida a las concentraciones alcanzadas mediante la administración tópica.» Texto original en inglés: "Mupirocin is an RNA synthetase inhibitor antibacterial. […] Mupirocin inhibits bacterial protein synthesis by reversibly and specifically binding to bacterial isoleucyl-transfer RNA (tRNA) synthetase. Mupirocin is bactericidal at concentrations achieved by topical administration." ([DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870), versión del 2020-03-20; consultado el 2026-11-19).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |
|------|------|------|------|------|
| 28302 | MUPIROX NASAL | 2% ung.x 5 g | Fortbenton | Vigente |
| 17082 | BACTROBAN NASAL | ung.x 3 g | GlaxoSmithKline | Vigente |
| 28358 | BACTROBAN CREMA | pomo x 15 g | GlaxoSmithKline | Vigente |
| 48667 | QUEMICETINA NF NASAL | 2% ung.x 3 g | Lafedar | Vigente |
| 30464 | MUPIROX | 2% ung.x 15 g | Fortbenton | Vigente |

La tabla muestra 5 de los 10 productos de este medicamento en los datos (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.

<!-- licenses:end -->

Se muestran las 5 primeras de 10 autorizaciones vigentes (todas de producto de un solo principio activo).

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron 118 interacciones potenciales, todas de nivel no clasificado ("Unknown") en la fuente consultada. Entre ellas figuran calcitriol, clotrimazol, morfina, metformina, pantoprazol, omeprazol, vancomicina, prednisona y simvastatina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio clínico ni publicación sobre mupirocina en empiema pleural (nivel de evidencia L5). Además, su perfil tópico con exposición sistémica insignificante hace poco viable alcanzar concentraciones útiles en el espacio pleural.

**Para avanzar se necesita:**
- Datos sobre la viabilidad de una vía de administración que alcance el espacio pleural (por ejemplo, estudios farmacocinéticos o preclínicos de administración intrapleural)
- Estudios preclínicos o clínicos que evalúen directamente mupirocina en empiema pleural
- Datos detallados del mecanismo de acción y del prospecto (advertencias y contraindicaciones) desde ANMAT
- Evaluación de la relevancia de las interacciones farmacológicas registradas

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

