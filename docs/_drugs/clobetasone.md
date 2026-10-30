---
layout: default
title: Clobetasone
parent: Solo Predicción del Modelo (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Clobetasone: nueva indicación predicha, Linfoma cutáneo primario de células T (nivel de evidencia L4). Indicación original: No disponible en la autorización de ANMAT (texto de indicación vacío)"
monitor_inn: "clobetasone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "Sezary syndrome", "primary cutaneous B-cell lymphoma", "granulomatous slack skin disease", "Crohn's colitis", "adrenocortical insufficiency", "primary cutaneous T-cell non-Hodgkin lymphoma", "nephrotic syndrome", "cystic teratoma", "spinal cord dermoid cyst"]
---

# Clobetasone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Clobetasona: De Indicación Original No Especificada a Linfoma Cutáneo Primario de Células T
{: .text-alpha }

## Resumen en Una Frase

Clobetasona (comercializada en Argentina como EUMOVATE) es un corticosteroide tópico de potencia baja a moderada, utilizado en afecciones dermatológicas; la autorización de ANMAT consultada no detalla el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **linfoma cutáneo primario de células T**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata de una predicción computacional con apoyo solo indirecto, basado en el efecto de clase de los corticosteroides.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de ANMAT (texto de indicación vacío) |
| Nueva Indicación Predicha | Linfoma cutáneo primario de células T |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (1 de 1) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de clobetasona. Según la información conocida, es un corticosteroide tópico, y los corticosteroides activan el receptor de glucocorticoides, lo que induce apoptosis en linfocitos y suprime la inflamación local.

Los corticosteroides tópicos son una terapia dirigida a la piel establecida para la micosis fungoide en estadio temprano (el linfoma cutáneo de células T más frecuente). Esto ofrece un vínculo mecanístico plausible con la predicción. Sin embargo, ese respaldo corresponde a la clase terapéutica y, sobre todo, a agentes de mayor potencia.

Clobetasona es de potencia baja a moderada (clase III), por lo que **no puede asumirse eficacia**. El puntaje elevado de TxGNN (0.9997) es una predicción computacional y no constituye evidencia clínica.

### Otras predicciones del modelo

| Posición | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Valoración |
|------|------|------|------|------|
| 2 | Síndrome de Sézary | 0.9978 | L5 | Los corticosteroides son solo terapia adyuvante o sintomática; los agentes tópicos de potencia baja a moderada difícilmente modifiquen la enfermedad. |
| 3 | Linfoma cutáneo primario de células B | 0.9977 | L5 | El tratamiento estándar es radioterapia, escisión o rituximab; los corticosteroides tópicos no tienen un papel establecido. |
| 4 | Enfermedad de la piel laxa granulomatosa | 0.9974 | L5 | Variante muy rara de linfoma cutáneo de células T; la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. |
| 5 | Colitis de Crohn | 0.9972 | L5 | Los corticosteroides sistémicos o entéricos se usan en Crohn, pero clobetasona es tópica y su traslación es implausible sin reformulación. |
| 6 | Insuficiencia suprarrenal | 0.9971 | L5 | Probable artefacto de efecto de clase; el uso excesivo de clobetasona puede, de hecho, suprimir el eje HHA. |
| 7 | Linfoma cutáneo primario de células T no Hodgkin | 0.9970 | L5 | Categoría superpuesta con la primera; mismo razonamiento indirecto y misma limitación de potencia. |
| 8 | Síndrome nefrótico | 0.9969 | L5 | Los corticosteroides sistémicos son de primera línea, pero la exposición sistémica de clobetasona tópica es mínima. |
| 9 | Teratoma quístico | 0.9965 | L5 | Sin mecanismo biológico plausible; la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. |
| 10 | Quiste dermoide de médula espinal | 0.9965 | L5 | Lesión congénita de manejo quirúrgico; sin mecanismo farmacológico plausible. |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1669 | EUMOVATE | Crema (cr.x 15 g) | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden clobetasona en linfoma cutáneo primario de células T. El único apoyo es el efecto de clase de los corticosteroides tópicos, con la reserva de que clobetasona es de potencia baja a moderada. La predicción es de nivel L4 y se considera una pregunta de investigación más que una opción lista para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada en la autorización de ANMAT.
- Revisar sistemáticamente la literatura sobre corticosteroides tópicos en micosis fungoide en estadio temprano y comparar la potencia de clobetasona con la de agentes de mayor potencia.
- Evaluar la compatibilidad de vía de administración y formulación (la presentación local es una crema tópica).
- Si se avanza, considerar estudios preclínicos o exploratorios en lesiones cutáneas tempranas antes de cualquier ensayo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

