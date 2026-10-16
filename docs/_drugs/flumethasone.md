---
layout: default
title: Flumethasone
parent: Solo Predicción del Modelo (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flumethasone: nueva indicación predicha, Alopecia areata (nivel de evidencia L5). Indicación original: Dermatosis inflamatorias (según el grafo de conocimiento: eccema atóp…"
monitor_inn: "flumethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "primary cutaneous B-cell lymphoma", "alopecia universalis onychodystrophy vitiligo"]
---

# Flumethasone
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

# Flumetasona: De Dermatosis Inflamatorias (Eccema Atópico) a Alopecia Areata

## Resumen en Una Frase

Flumetasona es un corticosteroide de uso tópico, originalmente utilizado para dermatosis inflamatorias como el eccema atópico, la dermatitis de contacto y la dermatitis seborreica.
El modelo TxGNN predice que podría ser efectivo para **alopecia areata**, con un puntaje muy alto (99,93%).
Por ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, de modo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatosis inflamatorias (según el grafo de conocimiento: eccema atópico, dermatitis de contacto, dermatitis seborreica, entre otras); el texto de indicación aprobado en la autorización local no está disponible |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la flumetasona. Según la información conocida, es un corticosteroide, una clase con acción antiinflamatoria e inmunomoduladora, y su uso en dermatosis inflamatorias está establecido. Mecanísticamente podría ser aplicable a la alopecia areata.

La alopecia areata es una enfermedad autoinmune mediada por linfocitos T que ataca el folículo piloso. Los corticosteroides tópicos e intralesionales son un tratamiento reconocido de esta clase para esa condición. Esto es coherente con el puntaje alto del modelo.

Sin embargo, este vínculo se infiere a partir de la clase terapéutica y no de datos propios de la flumetasona: no hay ensayos ni literatura sobre este fármaco para esta indicación. Además, la compatibilidad de la vía de administración y la similitud con la indicación original están pendientes de evaluar.

### Otras indicaciones predichas

Con el mismo nivel de evidencia (L5, sin ensayos ni literatura), el modelo también propone:

| Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|
| Alopecia mucinosa | 99,93% | Plausible: trastorno folicular inflamatorio, a veces asociado a linfoma cutáneo de células T |
| Foliculitis decalvante de Quinquaud | 99,91% | Plausible: alopecia cicatricial neutrofílica con componente inflamatorio importante |
| Linfoma cutáneo de células B primario | 99,22% | Plausible a nivel de clase (efecto linfolítico), probablemente solo adyuvante |
| Alopecia universal con onicodistrofia y vitiligo | 99,11% | Parcial: rasgos autoinmunes, pero síndrome raro y sistémico |
| Efluvio telógeno | 99,93% | Débil: cuadro habitualmente no inflamatorio |
| Hipotricosis hereditaria con vesículas cutáneas recurrentes | 99,91% | Sin mecanismo evidente |
| Alopecia con deficiencia de anticuerpos | 99,90% | Especulativa: el origen es inmunodeficiencia |
| Síndrome de alopecia, discapacidad intelectual e hipogonadismo hipergonadotrófico | 99,90% | Sin relevancia mecanística evidente |
| Atriquia con lesiones papulares | 99,70% | Débil: defecto genético del ciclo folicular |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48735 | TRESITE F | Pomada x 40 g | No disponible en el registro |

El producto es de tipo monofármaco, está vigente y su fabricante es Temis-Lostal.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): el grafo asocia la flumetasona con contraindicaciones en hipopituitarismo y otras deficiencias hormonales hipofisarias (incluido el déficit aislado de hormona de crecimiento y el síndrome de Sheehan), hipogonadismo hipogonadotrófico (incluido el síndrome de Kallmann), enfermedad del timo, atrofia cutánea, telangiectasia (incluida la telangiectasia hemorrágica hereditaria) y enfermedad capilar. La atrofia cutánea y la telangiectasia son relevantes para el uso tópico prolongado.

Para advertencias, contraindicaciones oficiales e interacciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5) y en el razonamiento por clase terapéutica, sin ensayos clínicos ni literatura sobre la flumetasona en alopecia areata. Además, faltan los datos de seguridad del prospecto y del mecanismo de acción.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), requisito para pasar al cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar el texto de indicación aprobado de la autorización 48735
- Evaluar la compatibilidad de la vía de administración y la similitud con las indicaciones originales
- Realizar una búsqueda sistemática de literatura y ensayos sobre corticosteroides tópicos de potencia comparable en alopecia areata
- Priorizar para estudio posterior las indicaciones con mayor plausibilidad mecanística (alopecia areata, alopecia mucinosa y foliculitis decalvante) y descartar por ahora las de mecanismo débil o inexistente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

