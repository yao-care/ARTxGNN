---
layout: default
title: Bencidamina
parent: Solo Predicción del Modelo (L5)
nav_order: 45
evidence_level: L5
indication_count: 1
drugbank_id: DB09084
monitor_inn: "Benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
last_modified_at: 2026-11-20
description: "Bencidamina: nueva indicación predicha, hiperplasia prostática benigna (benign prostatic hyperplasia (disease)) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: 1 (en el listado vigente: 1)"
---

# Bencidamina
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

## Bencidamina: hiperplasia prostática benigna (benign prostatic hyperplasia (disease))
{: .text-alpha }

## Resumen en Una Frase

Bencidamina es un antiinflamatorio no esteroideo de acción local, con propiedades analgésicas y anestésicas locales.
El modelo TxGNN predice que podría ser útil para **hiperplasia prostática benigna (benign prostatic hyperplasia (disease))**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperplasia prostática benigna (benign prostatic hyperplasia (disease)) |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de Autorización | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Bencidamina es (traducción no oficial): «Inhibidor de la ciclooxigenasa» Texto original en inglés: "Cyclooxygenase inhibitor" ([ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la bencidamina actúa localmente como antiinflamatorio: inhibe citocinas proinflamatorias (TNF-alfa e IL-1beta), tiene efecto estabilizador de membrana y una inhibición débil de la síntesis de prostaglandinas.

Una posible vía hacia la hiperplasia prostática benigna sería la modulación de la inflamación prostática crónica, que se considera un factor que contribuye a la progresión de la enfermedad y a los síntomas urinarios bajos. Esto es solo una hipótesis: no hay evidencia clínica ni preclínica recuperada que la respalde.

El puntaje del modelo es muy alto, pero por sí solo no basta para establecer plausibilidad biológica. La predicción debe tratarse como una señal para explorar, no como una conclusión.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 12612 | BUCHEX FORTE | fco.x 200 ml | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo, sin ensayos clínicos, literatura ni mecanismo documentado. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), actualmente faltante y bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank)
- Buscar estudios preclínicos o clínicos que vinculen la bencidamina con la hiperplasia prostática benigna o con la inflamación prostática
- Evaluar la compatibilidad de la vía de administración, dado que el producto local registrado es de otra forma farmacéutica (frasco de 200 ml)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

