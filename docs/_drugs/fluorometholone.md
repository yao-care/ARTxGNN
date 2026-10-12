---
layout: default
title: Fluorometholone
parent: Solo Predicción del Modelo (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Fluorometholone
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

# Fluorometolona: De Uveítis y Enfermedades Inflamatorias Oculares a Postinfectious Vasculitis (Vasculitis Postinfecciosa)

## Resumen en Una Frase

Fluorometolona es un corticosteroide tópico oftálmico, utilizado originalmente para tratar la uveítis, la conjuntivitis alérgica y otras inflamaciones del segmento anterior del ojo.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Indicación aprobada no disponible en las autorizaciones locales; según el grafo de conocimiento: uveítis, enfermedades del iris y del cuerpo ciliar, conjuntivitis atópica, papilar y primaveral, iritis, iridociclitis, úlcera corneal |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica conocida, la fluorometolona actúa sobre el receptor de glucocorticoides (NR3C1) y ejerce efectos antiinflamatorios e inmunosupresores. Su eficacia en la inflamación ocular está establecida, y mecanísticamente podría ser aplicable a procesos inflamatorios mediados por el sistema inmune.

La vasculitis postinfecciosa suele estar mediada por complejos inmunes, y los glucocorticoides pueden atenuar ese tipo de respuesta. Sin embargo, la relación con la indicación original es débil: la fluorometolona se presenta como suspensión oftálmica con exposición sistémica mínima, por lo que es poco probable que alcance concentraciones relevantes para una enfermedad vascular sistémica.

El puntaje del modelo es alto, pero no hay ensayos ni literatura que lo respalden. Esta predicción debe considerarse una hipótesis, no una conclusión.

### Otras predicciones del modelo (contexto)

Entre las 10 principales predicciones, algunas están mucho más cerca del uso actual del fármaco:

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Queratoconjuntivitis epitelial punteada | 99.89% | L4 | Cercana a las indicaciones oculares actuales; 2 publicaciones indirectas |
| Iridociclitis inducida por el cristalino | 99.82% | L4 | Subtipo de uveítis anterior, alineado con indicaciones existentes |
| Crisis glaucomatociclítica | 99.82% | L4 | Uveítis anterior recurrente con presión intraocular elevada; se requiere monitoreo de la PIO |

Estas tres se consideran "preguntas de investigación" y son más plausibles que la candidata principal. En cambio, otitis externa, estenosis uretral infecciosa, síndrome urémico hemolítico asociado a infección y cardiomiopatía de Chagas carecen de respaldo mecanístico sólido o de datos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para vasculitis postinfecciosa.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11935 | FLAREX (Novartis) | Suspensión oftálmica x 5 ml | No especificada |
| 241 | F M L LIQUIFILM (Abbvie) | Suspensión oftálmica x 10 ml | No especificada |
| 242 | F M L NEO LIQUIFILM (Abbvie) | Suspensión oftálmica x 5 ml | No especificada |

Las tres autorizaciones están vigentes y corresponden a productos de un solo principio activo.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): queratitis por herpes simple, infecciones oculares (incluidas las fúngicas y virales), tuberculosis ocular, conjuntivitis infecciosa, glaucoma de ángulo abierto, hipertensión ocular, diabetes mellitus, cetoacidosis diabética, porfiria, déficit de G6PD, enfermedades de depósito de glucógeno, cistinuria, galactosemia y pigmentación corneal.
- **Interacciones farmacológicas**: se identificaron 12 registros, y las 11 interacciones con otros fármacos tienen nivel de gravedad desconocido. Entre ellos figuran doxiciclina, salbutamol, ciclosporina, acetaminofén, digoxina, brimonidina, cefalexina, ácido alendrónico, aciclovir, diazepam y fenofibrato. El registro restante corresponde a la interacción con el receptor de glucocorticoides, que es su diana farmacológica.
- **Presión intraocular**: para las indicaciones oculares, el aumento de la PIO inducido por esteroides requiere monitoreo.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para vasculitis postinfecciosa se basa solo en el modelo (L5), sin ensayos ni literatura, y la formulación oftálmica tiene exposición sistémica mínima, lo que debilita la plausibilidad biológica.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT para completar las advertencias y contraindicaciones oficiales
- Completar los datos del mecanismo de acción desde DrugBank
- Considerar priorizar las predicciones oculares más cercanas (queratoconjuntivitis epitelial punteada, iridociclitis inducida por el cristalino, crisis glaucomatociclítica), con revisión focalizada de la literatura
- Evaluar si existe alguna vía de administración o formulación adecuada para una indicación no ocular
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

