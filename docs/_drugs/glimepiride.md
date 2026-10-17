---
layout: default
title: Glimepiride
parent: Solo Predicción del Modelo (L5)
nav_order: 153
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Glimepiride: nueva indicación predicha, Síndrome de la persona rígida clásico (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Glimepirida: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásica

## Resumen en Una Frase

Glimepirida es una sulfonilurea utilizada originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la persona rígida clásico**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, glimepirida es una sulfonilurea que cierra los canales de potasio sensibles a ATP (K-ATP) de las células beta pancreáticas y estimula la liberación de insulina. Su eficacia en la diabetes tipo 2 está comprobada.

El síndrome de la persona rígida es un trastorno autoinmune asociado a anticuerpos anti-GAD65 y a una señalización GABAérgica alterada. Existe un vínculo teórico muy débil a través de la autoinmunidad contra GAD65, que se solapa con la diabetes, pero esto no es evidencia de que glimepirida trate la enfermedad. No hay una vía mecanística clara respaldada por los datos.

Además, la variante "síndrome de la extremidad rígida focal" recibe exactamente el mismo puntaje (99.75%), lo que sugiere que el modelo propaga la señal desde un nodo de la familia de enfermedades y no a partir de una señal específica. Otras predicciones del modelo (lipodistrofias localizadas, opsismodisplasia, síndrome sensible a tiamina, agenesia pancreática) tampoco cuentan con ensayos ni literatura de apoyo. En la agenesia pancreática, la predicción es mecanísticamente implausible, ya que glimepirida requiere células beta funcionales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de producto único. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 25924 | GLEMAZ | 4 mg comprimidos trirranurados x 30 | — |
| 42330 | GLIMEPLIC | 4 mg comprimidos ranurados x 30 | — |
| 43474 | HIPOGLUT 4 | 4 mg comprimidos x 30 | — |
| 38772 | NEXT STEP 4 | 4 mg comprimidos x 30 | — |
| 17745 | AMARYL | 4 mg comprimidos x 15 | — |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipopituitarismo y déficits hormonales hipofisarios, hipogonadismo hipogonadotrópico (incluido el síndrome de Kallmann), síndrome de Sheehan, enfermedad del timo, osteoporosis (incluida la posmenopáusica) y enfermedades infecciosas.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las listadas, la mayoría son de nivel moderado, por ejemplo: fenilefrina, acebutolol, acetazolamida, famotidina, ranitidina, acitretina, formoterol, pseudoefedrina, ketorolaco, epinefrina, ibuprofeno, etinilestradiol, hidrocortisona, albiglutida, salbutamol, etanol, nitazoxanida e hidroclorotiazida. Las interacciones con hidrocortisona tópica y alclometasona tópica son de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que vincule el cierre de canales K-ATP de glimepirida con el síndrome de la persona rígida. El puntaje idéntico para una enfermedad hermana sugiere propagación por familia de enfermedades.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de glimepirida y análisis de un posible vínculo con la señalización GABAérgica/GAD65
- Estudios preclínicos o series de casos que sustenten un efecto en el síndrome de la persona rígida
- Advertencias y contraindicaciones del prospecto aprobado por ANMAT
- Revisión de las interacciones y contraindicaciones frente a la población de pacientes con enfermedades autoinmunes y neurológicas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

