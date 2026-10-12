---
layout: default
title: Itopride
parent: Solo Predicción del Modelo (L5)
nav_order: 169
evidence_level: L5
indication_count: 4
---

# Itopride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Itoprida: De Gastritis a Enfermedad de Crohn del Intestino Delgado

## Resumen en Una Frase

Itoprida es un procinético gastrointestinal utilizado originalmente para el tratamiento de la gastritis. El modelo TxGNN predice que podría ser efectivo para la **enfermedad de Crohn del intestino delgado**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gastritis (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de Crohn del intestino delgado |
| Puntaje de Predicción TxGNN | 99,90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Itoprida es un antagonista del receptor de dopamina D2 y un inhibidor de la acetilcolinesterasa que favorece la motilidad del tracto gastrointestinal superior. Esta descripción proviene del análisis de la predicción; los datos detallados del mecanismo de acción no figuran en la información compilada para este informe.

La relación entre la indicación original y la nueva es débil. La gastritis y la enfermedad de Crohn afectan al tubo digestivo, pero la enfermedad de Crohn es de naturaleza inflamatoria e inmunomediada, y no hay un vínculo mecanístico claro con la actividad procinética. Además, los procinéticos suelen utilizarse con cautela en presencia de estenosis u obstrucción, frecuentes en el Crohn del intestino delgado.

Por ello, el puntaje elevado (0,999) debe interpretarse con prudencia: refleja una predicción basada en la red de conocimiento y no está respaldado por estudios reales.

### Otras predicciones del modelo (todas con evidencia L5 y decisión Hold)

| Posición | Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Insuficiencia venosa | 99,23% | No se identificó un vínculo mecanístico plausible; probablemente sea un artefacto de la red. |
| 3 | Aclorhidria | 99,16% | Itoprida actúa sobre la motilidad, no sobre la secreción ácida; un alivio sintomático sería solo especulativo. |
| 4 | Hernia de hiato | 99,02% | La más plausible biológicamente (mejora del vaciamiento gástrico y del tono del esfínter esofágico inferior), pero no corrige el defecto anatómico y no hay evidencia directa. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se listan 5 de las 12 autorizaciones vigentes (todas de monodroga y en estado válido):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51944 | ITOPLUS (Eczane) | Comprimidos 50 mg x 10 | No disponible |
| 50125 | DOMEKA (Rossmore Pharma) | Comprimidos 50 mg x 60 | No disponible |
| 47759 | AFLUSAN (Domínguez) | Comprimidos 50 mg x 10 | No disponible |
| 52589 | IDELIS (Casasco) | Comprimidos 50 mg x 30 | No disponible |
| 40987 | ITOPRID (Eurofarma) | Comprimidos 50 mg x 60 | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la enfermedad de Crohn del intestino delgado se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, y sin un mecanismo plausible. Además, el uso de procinéticos en estenosis u obstrucción exige cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado por ANMAT (advertencias, contraindicaciones e indicaciones autorizadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura y de registros de ensayos para Crohn y para la hernia de hiato.
- Si se desea avanzar, priorizar la hernia de hiato (reflujo asociado), que es mecanísticamente la más plausible, evaluando evidencia indirecta en ERGE y dispepsia funcional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

