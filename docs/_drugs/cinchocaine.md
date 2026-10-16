---
layout: default
title: Cinchocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 102
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cinchocaine: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Dermatitis (según el grafo de conocimiento"
---

# Cinchocaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cinchocaína: De Dermatitis a Bronquitis

## Resumen en Una Frase

La cinchocaína (dibucaína) es un anestésico local de tipo amida, originalmente asociado al tratamiento de la dermatitis.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis (según el grafo de conocimiento; las autorizaciones locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la cinchocaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, y se comercializa en Argentina en presentaciones de uso tópico (PROCTYL, pomada).

Teóricamente, el bloqueo de los canales de sodio podría suprimir la actividad de los nervios sensitivos de las vías respiratorias (reflejo de la tos), como ocurre con otros anestésicos tópicos. Esta relación con la dermatitis es solo indirecta (alivio sintomático) y no existe una similitud mecanística clara entre ambas indicaciones.

Cabe subrayar que el puntaje alto (99.77%) es una asociación computacional y no evidencia clínica. Además, la seguridad por vía sistémica o inhalada de la cinchocaína no está establecida, ya que el fármaco está comercializado para uso tópico.

## Otras Predicciones del Modelo

| Posición | Nueva Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Acrodermatitis crónica atrófica | 99.76% | Manifestación tardía de la infección por *Borrelia*; requiere antibióticos. El anestésico no tiene papel modificador de la enfermedad. |
| 3 | Dermatomiositis neonatal | 99.72% | Enfermedad inmunomediada sin vínculo mecanístico; el uso en neonatos plantea preocupaciones de seguridad. |
| 4 | Enfermedad pulmonar intersticial secundaria infantil asociada a enfermedad del tejido conectivo | 99.72% | Sin racional mecanístico; población pediátrica con mayor exigencia de seguridad. |
| 5 | Acné queloideo | 99.67% | La más plausible, solo como alivio sintomático (dolor o picazón) por vía tópica. |
| 6 | Hidroa vacciniforme familiar | 99.66% | Fotosensibilidad rara; sin mecanismo relevante. |
| 7 | Dermatomiositis amiopática | 99.65% | Enfermedad autoinmune; a lo sumo alivio tópico sintomático. |

Todas estas predicciones tienen nivel de evidencia L5, sin ensayos clínicos ni literatura.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 27593 | PROCTYL | Pomada (pda.x 10 g) | No disponible en los datos compilados |
| 24920 | PROCTYL | Pomada (pda.x 30 g) | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no provienen del texto del prospecto): epilepsia, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, paro cardíaco súbito, enfermedad de la conducción cardíaca, insuficiencia respiratoria, miastenia gravis (incluida la de inicio en adulto), enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular y enfermedad cardíaca.
- No se encontraron interacciones farmacológicas registradas en la consulta realizada.

Consultar el prospecto para obtener las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para bronquitis se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y la seguridad por vía sistémica o inhalada no está establecida para un fármaco de uso tópico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones oficiales).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de literatura y ensayos que respalden el uso en afecciones respiratorias.
- Evaluar la compatibilidad de la vía de administración (actualmente solo tópica) y la seguridad sistémica o inhalada.
- Estudios preclínicos que justifiquen cualquier uso en vías respiratorias antes de considerar estudios clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

