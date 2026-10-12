---
layout: default
title: Latanoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Latanoprost: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Latanoprost es un análogo de la prostaglandina F2-alfa, originalmente utilizado para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se apoya solo en el modelo y en un razonamiento mecanístico indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (según el grafo de conocimiento; los textos de las autorizaciones no incluyen indicación) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L4 (solo razonamiento mecanístico; sin estudios reales) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Latanoprost es un análogo de la prostaglandina F2-alfa que reduce la presión intraocular (PIO) al aumentar el flujo de salida uveoescleral del humor acuoso. Este es el mecanismo que sustenta su uso en el glaucoma de ángulo abierto. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción; lo anterior corresponde al conocimiento farmacológico general del fármaco.

El glaucoma hereditario primario (por ejemplo, el glaucoma congénito primario o el glaucoma juvenil de ángulo abierto) comparte con la indicación original la fisiopatología de la PIO elevada, por lo que el vínculo es plausible. El puntaje tan alto del modelo se explica en gran parte por esta similitud con la indicación ya aprobada.

Existe, sin embargo, una limitación importante: las formas congénitas se originan en una disgenesia de la malla trabecular o del ángulo, y a menudo responden mal al tratamiento médico (con frecuencia requieren cirugía). Como no hay ensayos ni literatura, el respaldo es solo indirecto y basado en el mecanismo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se registran 14 autorizaciones vigentes (todas de producto único, ninguna cancelada). Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19634 | XALATAN (Aspen Pharma) | Gotas oftálmicas x 2.5 ml | No consta en el registro |
| 34716 | LATANOPROST DORF (PharmaDorf) | Solución oftálmica 50 mcg/ml x 2.5 ml | No consta en el registro |
| 37736 | LATANOFLAX (Sidus) | Gotas oftálmicas 50 mcg/ml x 2.5 ml | No consta en el registro |
| 30424 | KLONAPROST (Klonal) | Solución oftálmica 50 mcg/ml x 2.5 ml | No consta en el registro |
| 31282 | GLAUCOSTAT (Max Vision) | Solución oftálmica 50 mcg/ml x 2.5 ml | No consta en el registro |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, panuveítis, edema macular retiniano, edema macular quístico, iritis y conjuntivitis (incluida la conjuntivitis contagiosa aguda).
- **Interacciones farmacológicas**: se identificaron 100 posibles interacciones, todas con nivel de gravedad no especificado. Entre las que aparecen en la lista inicial figuran calcitriol, glimepirida, doxiciclina, clotrimazol, lansoprazol, cimetidina, atropina, pantoprazol, mesalazina, acarbosa, morfina, metformina, omeprazol, sucralfato, rosiglitazona, vancomicina, lactulosa, triamcinolona, prednisona y simvastatina. Al no haber clasificación de gravedad, deben interpretarse con cautela.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN y un vínculo mecanístico plausible, pero no cuenta con ningún ensayo clínico ni publicación que la respalde, y las formas congénitas del glaucoma suelen responder poco al tratamiento médico. Además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre prostaglandinas tópicas en glaucoma congénito y juvenil.
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones oficiales).
- Datos detallados del mecanismo de acción desde DrugBank.
- Evaluación de la respuesta según el subtipo genético y la edad (especialmente población pediátrica).
- Si la evidencia indirecta resulta favorable, diseñar un estudio exploratorio con seguimiento de PIO y seguridad ocular.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

