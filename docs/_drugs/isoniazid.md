---
layout: default
title: Isoniazid
parent: Solo Predicción del Modelo (L5)
nav_order: 168
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Isoniazid: nueva indicación predicha, Conjuntivitis (nivel de evidencia L4). Indicación original: Tuberculosis pulmonar (según la base de conocimiento de TxGNN"
monitor_inn: "isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Isoniazida: De Tuberculosis Pulmonar a Conjuntivitis
{: .text-alpha }

## Resumen en Una Frase

Isoniazida es un antibiótico antituberculoso, utilizado originalmente para el tratamiento de la tuberculosis pulmonar.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis**, pero no existen ensayos clínicos registrados y las **11 publicaciones** encontradas son en su mayoría reportes de casos, revisiones y estudios antiguos, sin evidencia terapéutica sólida.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis pulmonar (según la base de conocimiento de TxGNN; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Conjuntivitis |
| Puntaje de Predicción TxGNN | 0.9936 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción. Según la información conocida, la isoniazida inhibe la síntesis de ácidos micólicos en las micobacterias (vía InhA), y su eficacia en la tuberculosis pulmonar está comprobada.

No se establece un vínculo mecanístico directo con la conjuntivitis en general. La relación solo es plausible en conjuntivitis de origen micobacteriano, como la queratoconjuntivitis flictenular, que es una reacción de hipersensibilidad inmunomediada frente a antígenos tuberculosos. En esos casos, tratar la infección tuberculosa subyacente podría resolver el cuadro ocular.

El puntaje alto de TxGNN (0.9936) es una predicción del modelo y no está respaldado por datos de ensayos clínicos. Varios artículos recuperados describen efectos adversos oculares de fármacos sistémicos o artritis reactiva asociada a BCG, lo que no constituye evidencia terapéutica para la conjuntivitis.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohorte | Am Rev Respir Dis | Profilaxis con isoniazida en queratoconjuntivitis flictenular entre esquimales del suroeste de Alaska (sin resumen disponible) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Reporte de caso | Medicine | Queratoconjuntivitis flictenular asociada a tuberculosis sinonasal primaria en un paciente pediátrico, con revisión de la literatura |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Reporte de caso | Arch Ophthalmol | Tuberculosis primaria de la conjuntiva |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Serie de casos | Oftalmologia (Bucarest) | 28 casos de queratoconjuntivitis tuberculosa, 13 de ellos en niños con tuberculosis primaria y prueba cutánea de tuberculina positiva |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | No clasificado | Annales d'oculistique | Uso de isoniazida en el tratamiento local de la tuberculosis ocular (sin resumen disponible) |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Revisión | Optom Clin | Efectos adversos oculares de fármacos sistémicos; la conjuntivitis aparece como efecto adverso, no como indicación |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Reporte de caso/Revisión | Rev Rhum (Engl Ed) | Poliartritis tras inmunoterapia intravesical con BCG; revisión de 26 casos |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Reporte de caso | Rev Rhum (Engl Ed) | Artropatía refractaria tras BCG intravesical; utilidad de la isoniazida para la artritis, no para la conjuntivitis |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Reporte de caso | Dtsch Med Wochenschr | Artritis reactiva crónica asociada a BCG, con conjuntivitis como manifestación acompañante |
| [8136810](https://pubmed.ncbi.nlm.nih.gov/8136810/) | 1993 | Serie de casos | Rev Rhum (Ed Fr) | Poliartritis en 4 pacientes tratados con BCG intravesical por carcinoma de vejiga |

Nota: se omitieron dos publicaciones de relevancia muy baja (necrólisis epidérmica tóxica, 1964; síndrome de Munchausen por poder, 1993). Ninguna es un ensayo controlado aleatorizado.

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 5080 | NICOTIBINA (Sanofi-Aventis) | Comprimidos 300 mg x 30 | No se dispone del texto de indicación |
| 5099 | RIFINAH (Sanofi-Aventis) | Cápsulas x 30 | No se dispone del texto de indicación |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según la base de conocimiento (no proviene del prospecto)**: insuficiencia hepática (incluida la aguda), hepatitis y enfermedad hepática, porfiria (incluidas la hereditaria y otros trastornos del metabolismo de porfirinas), enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, gota, enfermedad del sistema nervioso periférico y neuropatía periférica, abuso/dependencia de sustancias y acetilación lenta.
- **Interacciones Farmacológicas**: se identificaron 242 interacciones en total. Entre las listadas, la mayoría son de nivel moderado, por ejemplo con antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina), metronidazol, budesonida, alosetrón, picosulfato y análogos de vitamina D (colecalciferol, calcifediol, calcitriol). Con corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona) las interacciones son de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura consiste en reportes de casos antiguos, sin evidencia terapéutica directa para conjuntivitis. El puntaje de TxGNN no se sustenta en un mecanismo plausible fuera de la conjuntivitis de origen tuberculoso.

**Para avanzar se necesita:**
- Delimitar la indicación a conjuntivitis/queratoconjuntivitis de etiología micobacteriana, en lugar de conjuntivitis en general
- Datos del mecanismo de acción y análisis de compatibilidad de vía de administración (las presentaciones locales son orales; no hay formulación oftálmica)
- Obtener y revisar el prospecto de ANMAT (advertencias y contraindicaciones oficiales)
- Evidencia clínica prospectiva (ensayos o estudios observacionales) que respalde el uso en esta indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

