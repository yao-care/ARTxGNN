---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Desogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

El skill de TxGNN pipeline no agrega instrucciones adicionales para la generación del informe. Procedo con el informe según el formato definido.

---

# Desogestrel: De Anticoncepción Hormonal a Amenorrea

## Resumen en Una Frase

Desogestrel es un progestágeno de tercera generación, ampliamente utilizado como componente de anticonceptivos orales combinados (AOC) y como píldora solo de progestágeno (POP).
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, con **2 ensayos clínicos** y **16 publicaciones** que actualmente respaldan esta dirección.
Sin embargo, la relación es bidireccional y requiere cautela interpretativa: como POP (75 µg), desogestrel es precisamente una causa frecuente de amenorrea, no un tratamiento.

---

## Resumen Rapido

| Item | Contenido |
|------|-----------|
| Indicación Original | Anticoncepción hormonal (progestágeno en AOC/POP) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Con base en la información farmacológica conocida, desogestrel es un progestágeno gonano de tercera generación cuyo metabolito activo, etonogestrel, actúa selectivamente sobre receptores de progesterona con baja afinidad androgénica. En formulaciones de AOC (combinado con etinilestradiol), suprime el eje hipotálamo-hipófisis-ovario y regula el ciclo menstrual mediante retroalimentación hormonal.

La relación entre desogestrel y la amenorrea es compleja y bidireccional. Como componente de AOC (con EE), la suplementación cíclica de estrógeno-progestágeno puede restaurar ciclos menstruales en pacientes con amenorrea hipotalámica o amenorrea del atleta, contextos donde el eje hipotálamo-hipofisario está suprimido por déficit energético o estrés. En cambio, como POP (75 µg), desogestrel inhibe la ovulación en más del 97% de las usuarias y adelgaza el endometrio, lo que genera amenorrea como efecto adverso frecuente (hasta el 50% de las usuarias). Esta dualidad hace que la predicción de TxGNN refleje probablemente la asociación de red entre desogestrel y amenorrea, sin distinguir dirección causal.

La predicción tiene una base mecanística parcial pero con dirección ambigua: el modelo TxGNN puede haber capturado la co-ocurrencia de desogestrel y amenorrea en la literatura (p. ej., como efecto adverso del POP y como tratamiento en AOC para amenorrea hipotalámica), sin discriminar si la relación es causante o terapéutica. Para que esta indicación sea viable clínicamente, es necesario especificar el subtipo de amenorrea (hipotalámica, atlética, post-AOC) y la formulación exacta (AOC vs. POP).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Fase 3 | Completado | 121 | Modulación de la función reproductiva por grasa corporal en atletas jóvenes; evalúa si estradiol transdérmico u oral mejora densidad ósea en atletas con amenorrea y déficit estrogénico. La intervención hormonal podría incluir componentes progestagénicos. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Fase 4 | Desconocido | 42 | Comparación de efectos de AOC oral vs. anillo vaginal sobre andrógenos, metabolismo de insulina y glucosa, perfil lipídico y SHBG en mujeres con SOP (síndrome de ovario poliquístico). La amenorrea no es el endpoint primario. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Estudio Clínico | Gynecological Endocrinology | Compara perfil de sangrado de drospirenona 4 mg vs. desogestrel 75 µg (POP); el DSG se asocia a mayor tasa de amenorrea e irregularidades del ciclo, lo que compromete la adherencia. |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Estudio Clínico | Journal of Reproductive Medicine | Evalúa el efecto de dosis decrecientes de EE en la pérdida ósea asociada a amenorrea hipotalámica; el AOC con progestágeno puede preservar la DMO en mujeres con amenorrea. |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Estudio Clínico | Georgian Medical News | Manejo de trastornos menstruales de origen central (oligomenorrea y amenorrea) en 159 mujeres infértiles; compara tratamiento hormonal estándar con tratamiento guiado por disfunción cerebral. |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Revisión Cochrane | Cochrane Database of Systematic Reviews | Revisión sistemática de AOC con 20 µg vs. >20 µg EE; evalúa eficacia anticonceptiva y patrones de sangrado, incluyendo incidencia de amenorrea por formulación. |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Revisión Sistemática | Cochrane Database of Systematic Reviews | Versión anterior de la revisión Cochrane sobre dosis de EE en AOC; preocupación por cambios en patrones de sangrado al reducir dosis estrogénica. |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | ECA Comparativo | British Journal of Obstetrics and Gynaecology | Compara dos AOC con 150 µg desogestrel más 20 µg (Mercilon) vs. 30 µg EE (Marvelon) en confiabilidad, control del ciclo y perfil de efectos adversos. |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Estudio Farmacodinámico | Acta Obstet Gynecol Scand (Suplemento) | Evalúa androgenicidad de progestágenos incluyendo desogestrel; menciona el contexto del SOP con amenorrea e hirsutismo, y la comparativa de perfil androgénico frente a otros progestágenos. |
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA Multicéntrico | Contraception | Compara Implanon (etonogestrel, metabolito activo de desogestrel) vs. Norplant en eficacia y patrones de sangrado; Implanon presenta tasas significativas de amenorrea durante el seguimiento. |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Estudio Clínico | American Journal of Obstetrics and Gynecology | Perfil de tolerabilidad de DSG/EE como AOC; describe beneficios no anticonceptivos incluyendo reducción de dismenorrea y control del ciclo. |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Revisión | Obstetrical & Gynecological Survey | Revisión sobre los nuevos progestágenos de tercera generación (desogestrel, norgestimato, gestodeno): farmacología, eficacia y ventajas sobre progestágenos de generaciones anteriores. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** La información de advertencias clave, contraindicaciones e interacciones farmacológicas no está disponible en el Evidence Pack actual. Se recomienda revisar el prospecto oficial del fabricante y la base de datos de la ANMAT antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN refleja una asociación real entre desogestrel y amenorrea, pero la dirección del efecto es inversa a la esperada para una indicación terapéutica: desogestrel como POP (75 µg) es una **causa** frecuente de amenorrea, no un tratamiento. La aplicación clínica requeriría especificar formulación (AOC con EE) y subtipo de amenorrea (hipotalámica/atlética), escenario con evidencia L3 pero sin ensayos que prueben desogestrel específicamente para el tratamiento de la amenorrea. Adicionalmente, el fármaco no está comercializado en Argentina, lo que eleva la barrera regulatoria.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) de desogestrel y su metabolito etonogestrel
- Información de seguridad completa: advertencias, contraindicaciones e interacciones farmacológicas (prospecto ANMAT o ficha técnica equivalente)
- Definición precisa del subtipo de amenorrea objetivo: hipotalámica, atlética, post-AOC o por SOP
- Ensayo clínico prospectivo que pruebe la hipótesis terapéutica (AOC con desogestrel para tratamiento de amenorrea hipotalámica), diferenciado del efecto adverso del POP
- Evaluación del camino regulatorio en Argentina para una nueva indicación dado que el fármaco no tiene autorización vigente
- Valoración del perfil riesgo-beneficio frente a las alternativas ya aprobadas (EE/LNG, EE/DRSP con indicación formal en amenorrea secundaria)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

