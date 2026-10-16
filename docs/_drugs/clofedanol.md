---
layout: default
title: Clofedanol
parent: Solo Predicción del Modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Clofedanol: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L5). Indicación original: Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común…"
---

# Clofedanol
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

# Clofedanol: De Rinitis Alérgica y Resfriado Común a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

Clofedanol (comercializado como UNITOS y COFRON) se utiliza originalmente para el alivio sintomático de cuadros de las vías respiratorias altas, como la rinitis alérgica, la rinitis vasomotora, la faringitis, el resfriado común y la nasofaringitis.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, rinitis y nasofaringitis (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, clofedanol se usa en preparados para la tos y el resfriado, y su uso en patologías de las vías respiratorias altas está establecido. Mecanísticamente podría ser aplicable a afecciones nasales, pero este vínculo no puede verificarse con los datos disponibles.

La "enfermedad de la cavidad nasal" es una categoría más amplia que las indicaciones de rinitis ya conocidas. Por ello, esta predicción aporta poca información nueva: se parece más a una generalización del uso existente que a un reposicionamiento genuino. El puntaje alto (99.99%) es un resultado computacional y no sustituye a la evidencia clínica.

**Otras predicciones del modelo (todas con nivel L5, sin ensayos ni literatura):**

| Posición | Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Laringofaringitis aguda | 99.99% | Adyacente a faringitis y resfriado; más una extensión de uso que un reposicionamiento |
| 3 | Urticaria alérgica | 99.97% | Posible vínculo indirecto vía rinitis alérgica; especulativo sin MOA confirmado |
| 4 | Conjuntivitis papilar | 99.84% | Posible solapamiento alérgico; sin datos oculares ni de formulación |
| 5 | Urticaria por frío | 99.78% | Sin necesidad no cubierta evidente; existen tratamientos definidos |
| 6 | Difteria fauccial | 99.33% | Probable falso positivo; requiere antitoxina y antibióticos |
| 7 | Trastorno degenerativo del disco cervical | 99.29% | Sin conexión mecanística identificable; probable artefacto del grafo |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59698 | UNITOS (Casasco) | Jarabe adultos, 100 ml | No disponible |
| 59699 | UNITOS (Casasco) | Jarabe pediátrico, 100 ml | No disponible |
| 50820 | COFRON (Abbott EPD) | Jarabe adultos, 100 ml | No disponible |
| 50821 | COFRON (Abbott EPD) | Jarabe adultos, 180 ml | No disponible |
| 50822 | COFRON (Abbott EPD) | Jarabe pediátrico, 100 ml | No disponible |

Hay 8 autorizaciones vigentes en total, todas de monofármaco y ninguna cancelada. Las tres restantes corresponden a PECTORAL HEBERT PEDIÁTRICO (13429), PECTORAL HEBERT N.F. (35669) y COFRON pediátrico de 180 ml (50823), todas en forma de jarabe.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no provienen del prospecto): hipertensión, pancreatitis, úlcera péptica, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad coronaria e infarto de miocardio, aterosclerosis, glaucoma de ángulo cerrado e hipertensión ocular, hipertiroidismo, obstrucción del cuello vesical, taquicardia ventricular, bloqueo auriculoventricular, acidosis y hemoglobinopatías.
- **Interacciones farmacológicas**: se identificaron 212 interacciones; las 20 principales son de nivel moderado. Destacan los depresores del sistema nervioso central y opioides (morfina, codeína, dihidrocodeína, fentanilo, alfentanilo, tramadol, opio, difenoxina, difenoxilato), cannabinoides (dronabinol, nabilona), antihistamínicos (clorfeniramina, prometazina, cetirizina, feniltoloxamina), alprazolam, etanol, metoclopramida, sibutramina y dicloralfenazona. El riesgo principal es la sedación aditiva.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni literatura, y sin mecanismo de acción verificable. Además, la indicación principal es una categoría amplia que aporta poco valor nuevo respecto de los usos ya conocidos.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT con advertencias y contraindicaciones, ya que es un vacío bloqueante para el cribado de seguridad.
- Consultar el mecanismo de acción en DrugBank.
- Obtener los textos de indicación aprobados de las autorizaciones locales.
- Revisar sistemáticamente la literatura y los registros de ensayos para clofedanol en patología nasal.
- Evaluar si la indicación predicha ofrece un beneficio distinto del uso actual, o si es solo una ampliación de la categoría.
- Descartar las predicciones de baja credibilidad (difteria fauccial, disco cervical) salvo que aparezca evidencia nueva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

