---
layout: default
title: Budesonide
parent: Solo Predicción del Modelo (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Budesonide: nueva indicación predicha, Eccema atópico (nivel de evidencia L5). Indicación original: Enfermedad de Crohn, enfermedad inflamatoria intestinal, asma…"
monitor_inn: "BUDESONIDE"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
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

## Budesonida: De Enfermedad de Crohn y Asma a Eccema Atópico
{: .text-alpha }

## Resumen en Una Frase

La budesonida es un glucocorticoide utilizado originalmente en la enfermedad de Crohn, la enfermedad inflamatoria intestinal, el asma y la rinitis alérgica.
El modelo TxGNN predice que podría ser efectiva para **eccema atópico**, pero la evidencia directa es muy limitada: **0 ensayos clínicos** y **20 publicaciones**, en su mayoría indirectas (revisiones, estudios de sensibilización de contacto y un trabajo preclínico de formulación).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Crohn, enfermedad inflamatoria intestinal, asma, rinitis alérgica (las autorizaciones locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Budesonide (traducción no oficial): «La budesonida es un corticosteroide antiinflamatorio que presenta una potente actividad glucocorticoide y una débil actividad mineralocorticoide. En modelos estándar in vitro y en animales, la budesonida tiene una afinidad por el receptor de glucocorticoides aproximadamente 200 veces mayor y una potencia antiinflamatoria tópica 1000 veces mayor que el cortisol (ensayo de edema auricular inducido por aceite de crotón en ratas).» Texto original en inglés: "Budesonide is an anti-inflammatory corticosteroid that exhibits potent glucocorticoid activity and weak mineralocorticoid activity. In standard in vitro and animal models, budesonide has approximately a 200-fold higher affinity for the glucocorticoid receptor and a 1000-fold higher topical anti-inflammatory potency than cortisol (rat croton oil ear edema assay)." ([DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da), versión del 2026-06-10; consultado el 2026-11-19). Según la información conocida, la budesonida es un glucocorticoide con actividad antiinflamatoria e inmunosupresora amplia. Su eficacia en enfermedades inflamatorias del intestino y de las vías respiratorias está comprobada.

El eccema atópico es una enfermedad inflamatoria de la piel dirigida por citocinas Th2, con participación de eosinófilos y mastocitos. Mecanísticamente, la supresión de esas vías es biológicamente plausible. Esa es la misma lógica que respalda su uso en asma y rinitis alérgica, que son también enfermedades atópicas.

Conviene interpretar el puntaje alto con cautela. Refleja principalmente la similitud de clase entre corticosteroides y no datos clínicos específicos de budesonida. Además, los corticosteroides tópicos ya son un tratamiento establecido para esta condición, por lo que la novedad del reposicionamiento es baja.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Las publicaciones disponibles son indirectas. Ninguna demuestra eficacia clínica de la budesonida en eccema atópico.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Estudio preclínico de formulación | Gels | Nanopartículas de budesonida sensibles al pH en hidrogeles para terapia local de dermatitis atópica pediátrica. |
| [35056927](https://pubmed.ncbi.nlm.nih.gov/35056927/) | 2021 | Estudio ex vivo | Pharmaceutics | Estrategias con ciclodextrina e hidrogeles de poloxámero para mejorar la retención cutánea de budesonida. |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Estudio clínico abierto | Pediatric Dermatology | En 14 niños con dermatitis atópica, se evaluó con knemometría si la budesonida tópica afecta el crecimiento a corto plazo. |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Estudio in vitro | Int Immunopharmacol | La budesonida, a diferencia del tacrolimus, modifica funciones inmunes de queratinocitos humanos normales. |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisión | Neuroimmunomodulation | Corticosteroides intranasales y supresión adrenal en enfermedades alérgicas, incluida la dermatitis atópica. |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Revisión | Allergy | Alergia de contacto e inmediata a corticosteroides en pacientes con asma. |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Revisión | J Allergy Clin Immunol | Terapias emergentes para esofagitis eosinofílica, incluidas formulaciones de esteroides tópicos. Es una enfermedad distinta. |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Estudio de pruebas de parche | Contact Dermatitis | La budesonida es marcador de hipersensibilidad a corticosteroides, con tendencia decreciente de alergia en las últimas dos décadas. |
| [9543750](https://pubmed.ncbi.nlm.nih.gov/9543750/) | 1997 | Revisión | Ned Tijdschr Geneeskd | La alergia de contacto a corticosteroides no es rara, sobre todo en personas con dermatitis atópica de larga data. |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Reporte de caso | Cureus | Reacción de hipersensibilidad tipo I (angioedema y urticaria) inducida por un corticosteroide en un paciente con dermatitis atópica. |

## Información de Mercado en Argentina

Se registran 20 autorizaciones vigentes, todas de monofármaco. A continuación se muestran 5 de ellas. Ninguna incluye texto de indicación aprobada en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Laboratorio |
|---------|------|------|-----------|
| 46033 | AEROVIAL HFA | Aerosol x 200 dosis + adaptador bucal | Lab Internacional |
| 22488 | RINO-B 50 | Aerosol x 200 dosis | Elea |
| 28697 | HYPERSOL B 50 | Spray nasal x 200 dosis | Cassarß |
| 45935 | NEUMOCORT HFA | Aerosol 200 mcg x 200 dosis | Cassarß |
| 47091 | BUDENOFALK | Espuma rectal x 14 aplicaciones | LKM |

Las formas disponibles son inhalatorias, nasales, nebulizables y rectales. No se identifica una presentación dérmica, por lo que una eventual indicación en eccema atópico requeriría desarrollar una formulación tópica o justificar otra vía.

## Consideraciones de Seguridad

- **Contraindicaciones (relaciones fármaco-enfermedad del grafo de conocimiento, no texto del prospecto)**: hipertensión, epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, sarampión, insuficiencia cardíaca congestiva, queratitis por herpes simple, hipopituitarismo y otras deficiencias hipofisarias o hipogonadismos hipogonadotrópicos, además de varios trastornos del ciclo de la urea (deficiencia de carbamoil fosfato sintetasa I, hiperargininemia, citrulinemia).
- **Interacciones Farmacológicas**: se registraron 100 interacciones, de las cuales se revisaron 20.
  - **Mayores**: adalimumab y fosamprenavir.
  - **Moderadas** (ejemplos): zidovudina, isotretinoína, ketorolaco, ibuprofeno, nifedipina, etinilestradiol, fluvoxamina, aldesleucina, alemtuzumab, fosinopril.
  - **Menores**: formoterol y salbutamol.
- **Señales de la literatura**: supresión del eje hipotálamo-hipófisis-adrenal con corticosteroides intranasales, posible efecto sobre el crecimiento y el recambio óseo y de colágeno en niños con dermatitis atópica tratados con corticosteroides tópicos, y sensibilización de contacto a corticosteroides, incluida la budesonida.

Para advertencias y precauciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura es indirecta, sin evidencia de eficacia específica de budesonida en eccema atópico (nivel L4). El puntaje alto de TxGNN refleja similitud de clase con corticosteroides ya establecidos para esta enfermedad, por lo que la novedad es baja. Dentro de las predicciones del modelo, bronquitis muestra más respaldo (nivel L2, con ensayos de Fase 2 completados), aunque pequeños y heterogéneos.

**Para avanzar se necesita:**
- Ensayos clínicos controlados de budesonida tópica frente a corticosteroides tópicos estándar en eccema atópico.
- Una formulación dérmica viable, ya que las autorizaciones locales no incluyen vía tópica.
- Datos oficiales de mecanismo de acción, advertencias y contraindicaciones del prospecto de ANMAT.
- Evaluación de seguridad pediátrica (crecimiento, supresión adrenal) y del riesgo de sensibilización de contacto.
- Justificar el valor diferencial frente a las opciones tópicas actuales.

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

