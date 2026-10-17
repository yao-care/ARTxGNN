---
layout: default
title: Natamycin
parent: Solo Predicción del Modelo (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Natamycin: nueva indicación predicha, Candidiasis vulvovaginal (nivel de evidencia L5). Indicación original: Úlcera corneal micótica"
monitor_inn: "natamycin"
predicted_indications: ["vulvovaginal candidiasis", "candidiasis", "vulvitis", "vulvovaginitis", "trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginitis (disease)", "tinea nigra"]
---

# Natamycin
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

# Natamicina: De Úlcera Corneal Micótica a Candidiasis Vulvovaginal

## Resumen en Una Frase

La natamicina es un antifúngico polieno utilizado originalmente para tratar la úlcera corneal micótica (queratitis fúngica).
El modelo TxGNN predice que podría ser efectiva para la **candidiasis vulvovaginal**,
con **1 ensayo clínico de Fase 3 completado** y **14 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que la natamicina vaginal ya se usa en varios mercados, por lo que esto se acerca más a una extensión de un uso antifúngico tópico establecido que a un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Úlcera corneal micótica (según el grafo de conocimiento; el texto de indicación de la licencia en ANMAT está vacío) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 (con la salvedad de que el ensayo de Fase 3 evaluó una combinación con lactulosa) |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

La natamicina es un antifúngico macrólido polieno. Se une al ergosterol de la membrana celular de los hongos, alterando su función e inhibiendo el crecimiento fúngico. Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank; este mecanismo proviene del conocimiento farmacológico general.

La úlcera corneal micótica y la candidiasis vulvovaginal son ambas infecciones fúngicas de superficies mucosas o epiteliales. Las especies de *Candida* contienen ergosterol, por lo que el mecanismo es directamente aplicable. La natamicina se absorbe poco, lo que la hace adecuada para uso tópico o mucoso, pero no para candidiasis sistémica.

La plausibilidad mecanística es alta, y la natamicina ya se utiliza como antifúngico vaginal (por ejemplo, Pimafucin) en varios mercados.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Fase 3 | Completado | 218 | Supositorios vaginales de natamicina 100 mg + lactulosa 300 mg frente a Pimafucin (natamicina 100 mg) o lactulosa 300 mg sola en mujeres adultas no embarazadas con candidiasis vulvovaginal; ensayo internacional, aleatorizado, de superioridad (2022-2023) |

**Nota:** al tratarse de una combinación con lactulosa, no se puede aislar la contribución de la natamicina sola.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | ECA | BMC Women's Health | Eficacia y seguridad de supositorios de natamicina + lactulosa en candidiasis vulvovaginal (publicación del ensayo NCT06411314) |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | ECA | Med J Aust | Comparación de óvulos de anfotericina B y natamicina (Pimafucin) en candidiasis vaginal |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Estudio clínico | Acta Obstet Gynecol Scand | Tabletas vaginales de natamicina durante 10 días; curación del 94% con tratamiento de la pareja frente al 88% con placebo, sin diferencia significativa |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | Estudio clínico | N Z Med J | Tabletas vaginales de Pimafucin durante 10 días en 50 mujeres; curación del 76% a las 2 semanas, mantenida a las 4 semanas |
| [12849848](https://pubmed.ncbi.nlm.nih.gov/12849848/) | 2003 | Caso-control | Reprod Toxicol | Estudio teratológico del tratamiento vaginal con natamicina durante el embarazo; no mostró riesgo teratogénico |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Estudio clínico | Zentralbl Gynakol | Metronidazol oral más natamicina vaginal en infecciones urogenitales mixtas; curación clínica de la candidiasis vaginal en 89% |
| [159686](https://pubmed.ncbi.nlm.nih.gov/159686/) | 1979 | Estudio clínico controlado | Aust N Z J Obstet Gynaecol | Elase como terapia adyuvante a natamicina en 120 pacientes con vulvovaginitis monilial; mejor respuesta con la combinación |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Revisión | Ceska Gynekol | Diagnóstico y tratamiento de la candidiasis vaginal crónica; comparación de natamicina con clotrimazol |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Encuesta | Ceska Slov Farm | Manejo de la candidiasis vulvovaginal en Lviv, Ucrania (408 mujeres); prevalencia a lo largo de la vida del 72.6% |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | Estudio preclínico de formulación | J Pharm Sci | Complejo de inclusión natamicina:γ-ciclodextrina en tabletas vaginales mucoadhesivas; CIM90 inferior a 0.0313 µg/mL |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11149 | NATACYN (Daxley) | Frasco de 15 ml | No disponible en el registro |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.
- **Embarazo:** un estudio de casos y controles (PMID 12849848) no mostró riesgo teratogénico con el uso vaginal de natamicina durante el embarazo.
- **Uso adecuado:** limitar el uso a etiología fúngica confirmada, ya que las vaginitis bacterianas, tricomoniásicas o atróficas no responderán.

Consultar el prospecto para información adicional de seguridad (advertencias y contraindicaciones).

---

## Otras Indicaciones Predichas (Contexto)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Candidiasis | 99.86% | L1 (Fase 3 solo en forma vaginal) | Proceed with Guardrails |
| Vulvitis | 99.81% | L1 (solo etiología candidiásica) | Proceed with Guardrails |
| Vulvovaginitis | 99.78% | L1 | Proceed with Guardrails |
| Vaginitis | 99.59% | L1 (solo subtipo candidiásico) | Proceed with Guardrails |
| Vulvovaginitis tricomonásica | 99.74% | L4 | Hold (sin mecanismo plausible; el metronidazol trató el componente protozoario) |
| Vaginitis atrófica posmenopáusica | 99.66% | L5 | Hold (causa hormonal, no fúngica) |
| Úlcera de vulva | 99.64% | L5 | Hold |
| Neoplasia de vulva | 99.63% | L5 | Hold (probable artefacto del grafo) |
| Tinea nigra | 99.34% | L5 | Pregunta de investigación (plausibilidad biológica, sin evidencia) |

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado (n=218) con publicación en 2025, además de décadas de literatura clínica sobre natamicina vaginal, y el mecanismo (unión al ergosterol) es directamente aplicable a *Candida*. La salvedad es que el ensayo principal evaluó una combinación con lactulosa y que no hay datos de ANMAT sobre advertencias ni sobre la indicación aprobada.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Verificar que exista una forma farmacéutica vaginal autorizada en Argentina; la licencia actual (frasco de 15 ml) corresponde probablemente a una presentación oftálmica y no es compatible con la vía vaginal.
- Confirmar la etiología fúngica antes de su uso, dado que no es eficaz en vaginitis no fúngicas.
- Aclarar la eficacia de la natamicina sola frente a la combinación con lactulosa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

