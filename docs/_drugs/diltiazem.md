---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

---

# Diltiazem: De Hipertensión y Arritmias a Susceptibilidad a Accidente Cerebrovascular Isquémico

## Resumen en Una Frase

Diltiazem es un bloqueador de canales de calcio tipo L (clase benzotiazepina), utilizado ampliamente para el tratamiento de la hipertensión arterial, angina de pecho y arritmias cardíacas supraventriculares.
El modelo TxGNN predice que podría ser efectivo para la **Susceptibilidad a Accidente Cerebrovascular Isquémico**, aunque actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta dirección.
Cabe señalar que la indicación predicha utiliza un término de enfermedad marcado como **obsoleto** en la ontología de enfermedades empleada por TxGNN, lo que añade incertidumbre interpretativa adicional a la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial, angina de pecho y arritmias cardíacas (CCB clase benzotiazepina) |
| Nueva Indicación Predicha | Susceptibilidad a Accidente Cerebrovascular Isquémico |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde DrugBank. Sin embargo, diltiazem es un bloqueador de canales de calcio de tipo L dependientes de voltaje, perteneciente a la clase benzotiazepina. Su efecto farmacológico principal consiste en inhibir la entrada de iones calcio en el músculo cardíaco y el músculo liso vascular, lo que produce vasodilatación periférica y coronaria, reducción de la frecuencia cardíaca y supresión de focos arrítmicos supraventriculares.

Desde el punto de vista mecanístico, existen al menos cuatro vínculos potenciales con la prevención del accidente cerebrovascular isquémico: (1) **vasodilatación cerebrovascular**, que reduce la resistencia vascular cerebral y mejora la perfusión; (2) **inhibición de la sobrecarga de calcio intracelular** en neuronas isquémicas, dado que la entrada masiva de calcio es el mecanismo central de neurotoxicidad durante la isquemia; (3) **control de la hipertensión arterial**, el principal factor de riesgo modificable del ACV isquémico; y (4) **efecto antiarrítmico**, que puede reducir el riesgo de embolias cardioembólicas secundarias a fibrilación auricular.

No obstante, es importante contextualizar estos vínculos con la evidencia disponible. Fármacos del mismo grupo — en particular nimodipina, un CCB dihidropiridínico con mayor penetración en el sistema nervioso central — han mostrado resultados decepcionantes en ensayos clínicos de neuroprotección en ACV isquémico agudo. Diltiazem específicamente carece de ensayos clínicos directos para esta indicación. Asimismo, el término predicho **"obsolete susceptibility to ischemic stroke"** está marcado como obsoleto en la ontología de enfermedades de TxGNN, lo que sugiere que esta categoría diagnóstica ha sido reclasificada o discontinuada, dificultando el diseño de estudios de seguimiento sobre una base nosológica sólida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Diltiazem no cuenta con ninguna autorización de comercialización registrada en Argentina según los datos disponibles.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN se basa exclusivamente en señales del modelo de grafo de conocimiento (nivel L5), sin ningún ensayo clínico ni publicación científica que respalde directamente el uso de diltiazem en la prevención o tratamiento del ACV isquémico. El término de enfermedad predicho está además marcado como obsoleto en la ontología de referencia, lo que dificulta la interpretación clínica y el diseño de estudios prospectivos.

**Para avanzar se necesita:**
- Verificar el mecanismo de acción detallado (MOA) mediante consulta a DrugBank (DG002 pendiente)
- Obtener datos completos de seguridad — advertencias, contraindicaciones e interacciones farmacológicas — desde la ficha técnica oficial (DG001 pendiente)
- Resolver la ambigüedad ontológica: identificar a qué término diagnóstico vigente corresponde "obsolete susceptibility to ischemic stroke" (p. ej., ACV isquémico agudo, AIT, ACV cardioembólico) para acotar el alcance clínico real
- Realizar una búsqueda bibliográfica ampliada sobre CCB de clase benzotiazepina en modelos preclínicos y estudios observacionales de ACV isquémico
- Evaluar si diltiazem presenta ventajas farmacocinéticas o farmacodinámicas frente a otros CCB mejor estudiados para indicaciones neurológicas (p. ej., nimodipina) antes de considerar su desarrollo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

