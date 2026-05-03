---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 7
---

# Ibuprofen
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

# Ibuprofen: De Antiinflamatorio/Analgesia a Displasia Acromesomélica Tipo Hunter-Thompson

## Resumen en Una Frase

Ibuprofen es un inhibidor de COX (ciclooxigenasa) ampliamente utilizado como analgésico, antipirético y antiinflamatorio no esteroideo (AINE), aunque los datos regulatorios disponibles para Argentina no registran indicaciones aprobadas en este sistema. El modelo TxGNN predice que podría ser efectivo para la **Displasia Acromesomélica Tipo Hunter-Thompson**, con **0 ensayos clínicos** y **0 publicaciones** que respaldan esta dirección. La evidencia es exclusivamente computacional (Nivel L5), sin respaldo empírico que sustente la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos regulatorios registrados en Argentina |
| Nueva Indicación Predicha | Displasia Acromesomélica Tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado (0 registros) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este sistema. Según la información disponible en las racionalizaciones de reposicionamiento del pack, Ibuprofen actúa como inhibidor de la COX (ciclooxigenasa), suprimiendo la producción de prostaglandinas y mediadores inflamatorios. Su eficacia en condiciones de dolor agudo e inflamación está ampliamente documentada en la literatura médica global.

La displasia acromesomélica tipo Hunter-Thompson es una enfermedad rara causada por mutaciones en el gen **GDF5/CDMP1**, que compromete el desarrollo normal del cartílago y resulta en acortamiento desproporcionado de las extremidades. Este defecto opera a nivel genético-estructural del desarrollo esquelético, un proceso que está completamente fuera del alcance del mecanismo antiinflamatorio de Ibuprofen.

La alta puntuación TxGNN (99.74%) probablemente no refleja una conexión farmacológica genuina, sino **proximidad topológica en el grafo de conocimiento** entre el perfil de Ibuprofen y el clúster de enfermedades esqueléticas. El propio análisis del sistema califica esta predicción como falso positivo de alto riesgo, ya que la inhibición de COX no tiene mecanismo directo para modificar defectos de desarrollo óseo de origen genético.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ninguna evidencia clínica, preclínica ni bibliográfica que respalde el uso de Ibuprofen en displasia acromesomélica tipo Hunter-Thompson. El mecanismo de inhibición de COX no tiene conexión directa con los defectos genéticos del gen GDF5/CDMP1 que caracterizan esta enfermedad, y la predicción del modelo es consistente con un artefacto de agrupación topológica en el grafo de conocimiento.

**Para avanzar se necesita:**
- Completar los datos de mecanismo de acción (MOA) desde DrugBank (brecha DG002)
- Obtener datos de seguridad completos: advertencias y contraindicaciones de prospecto oficial (brecha DG001)
- Realizar búsqueda bibliográfica ampliada sobre AINEs/NSAIDs en displasias esqueléticas raras
- Evaluar si estudios preclínicos en modelos GDF5/CDMP1 podrían justificar un ensayo exploratorio
- Aclarar el estado regulatorio real de Ibuprofen en Argentina (resultado "0 registros" es atípico para un AINE de uso masivo y podría reflejar un error en la consulta a la base de datos regulatoria)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

