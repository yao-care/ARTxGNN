---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

El skill confirma el contexto del pipeline TxGNN. Procedo a generar el informe de evaluación basado en el Evidence Pack proporcionado.

---

# Glimepiride: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

Glimepiride es una sulfonilurea de tercera generación, originalmente utilizada para el tratamiento de la Diabetes Mellitus Tipo 2, que actúa estimulando la secreción de insulina por las células β pancreáticas.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de la Persona Rígida Clásico (classic stiff person syndrome)**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes Mellitus Tipo 2 (conocimiento médico establecido; sin registro en Argentina) |
| Nueva Indicación Predicha | Síndrome de la Persona Rígida Clásico (classic stiff person syndrome) |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales del mecanismo de acción desde DrugBank (Data Gap DG002). Según el conocimiento farmacológico establecido, Glimepiride es una sulfonilurea que actúa cerrando los canales de potasio sensibles a ATP (KATP) en las células β del páncreas, despolarizando la membrana celular y estimulando así la liberación de insulina endógena. También posee una leve actividad agonista parcial sobre los receptores PPARγ.

El Síndrome de la Persona Rígida Clásico (SPS) es una enfermedad autoinmune neurológica caracterizada por la presencia de autoanticuerpos contra la enzima GAD65 (descarboxilasa del ácido glutámico, isoforma 65 kDa). Este mismo antígeno es relevante en la Diabetes Mellitus Tipo 1, donde los anticuerpos anti-GAD65 son marcadores de destrucción autoinmune de células β. Esta comorbilidad autoinmune compartida es, con alta probabilidad, el nodo de conexión que el modelo TxGNN detectó en el grafo de conocimiento para generar esta predicción.

Sin embargo, la aplicabilidad mecanística presenta limitaciones importantes: aunque los canales KATP están presentes también en neuronas del sistema nervioso central, la patología central del SPS es la pérdida funcional de las interneuronas GABAérgicas inhibitorias, un mecanismo completamente distinto al de la secreción de insulina. La predicción del modelo parece corresponder a una conexión indirecta vía nodo compartido (GAD65/autoinmunidad), y no a una transferencia directa del mecanismo farmacológico. Esto la clasifica como una inferencia especulativa del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Glimepiride **no cuenta con ninguna autorización de comercialización en Argentina** según los datos disponibles (ANMAT: 0 licencias registradas). No es posible mostrar tabla de autorizaciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN se sustenta únicamente en una conexión indirecta a través del nodo de comorbilidad autoinmune GAD65, compartido entre la Diabetes Mellitus y el SPS. No existe ningún ensayo clínico ni publicación que valide el uso de Glimepiride en esta indicación, y la lógica mecanística directa es inconsistente: el SPS no tiene células β como diana terapéutica funcional. La ausencia de registro en Argentina añade una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Obtener los datos formales de MOA desde DrugBank (remediar Data Gap DG002) para completar el análisis de red mecanística
- Recuperar las advertencias y contraindicaciones del prospecto oficial (remediar Data Gap DG001) antes de cualquier evaluación clínica
- Realizar estudios preclínicos en modelos animales de SPS para evaluar si el bloqueo de canales KATP neuronales tiene algún efecto sobre la rigidez muscular o la actividad GABAérgica
- Evaluar el riesgo de hipoglucemia severa en población sin diabetes (pacientes con SPS no son diabéticos), lo cual podría representar un riesgo de seguridad significativo
- Gestionar el registro de Glimepiride en Argentina como prerrequisito regulatorio para cualquier ensayo clínico local
---

