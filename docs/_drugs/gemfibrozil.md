---
layout: default
title: Gemfibrozil
parent: Evidencia Moderada (L3-L4)
nav_order: 151
evidence_level: L4
indication_count: 10
---

# Gemfibrozil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Gemfibrozilo: De Hipertrigliceridemia a Artritis Reumatoide

## Resumen en Una Frase

Gemfibrozilo es un fármaco hipolipemiante (agonista de PPAR-alfa), originalmente utilizado para el tratamiento de la hipertrigliceridemia.
El modelo TxGNN predice que podría ser efectivo para **Artritis Reumatoide**,
pero actualmente **no hay ensayos clínicos** y solo existen **4 publicaciones** de apoyo indirecto (estudios preclínicos o de un fármaco relacionado), por lo que se trata de una predicción con evidencia muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertrigliceridemia (según el grafo de conocimiento; los textos de indicación de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, gemfibrozilo es un agonista del receptor activado por proliferadores de peroxisomas alfa (PPAR-alfa), su eficacia en la hipertrigliceridemia está bien establecida, y mecanísticamente podría ser aplicable a la artritis reumatoide a través de efectos antiinflamatorios e inmunomoduladores.

La activación de PPAR se ha asociado con una menor señalización inflamatoria (por ejemplo, citoquinas inflamatorias y vía Th17) y con la modulación de Foxp3 en linfocitos T. Un estudio preclínico de 2026 con bezafibrato (un agonista pan-PPAR) en artritis reumatoide experimental, y un estudio de 2019 en ratas con artritis inducida por adyuvante que combinó gemfibrozilo con una dosis reducida de esteroide, aportan un respaldo indirecto.

Cabe subrayar que la relación entre la indicación original (trastorno lipídico) y la nueva (enfermedad autoinmune inflamatoria) es débil y puramente mecanística. No existen ensayos clínicos en humanos, y la evidencia proviene de un fármaco relacionado o de estudios de diseño poco claro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Estudio en animales (rata) | Modern Rheumatology | Gemfibrozilo combinado con una dosis reducida de prednisolona logró un control similar al de la dosis completa de esteroide en un modelo de artritis inducida por adyuvante |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclínico (bezafibrato, no gemfibrozilo) | International Immunopharmacology | El bezafibrato, agonista pan-PPAR, atenuó la artritis reumatoide experimental mediante modulación de vías inflamatorias dependientes de PPAR, con énfasis en PPAR-γ |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclínico/mecanístico | Journal of Immunology | El óxido nítrico reduce la expresión de Foxp3 en linfocitos T tras la exposición a la proteína básica de mielina; apoyo mecanístico indirecto |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revisión/reporte de caso | American Journal of Clinical Dermatology | Revisión sobre el eritema palmar y sus causas fisiológicas y sistémicas; relación indirecta con la indicación |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 13209 | LOPID UD | 900 mg, comprimidos x 15 | No disponible en los datos compilados |
| 13210 | LOPID UD | 900 mg, comprimidos x 30 | No disponible en los datos compilados |
| 6327 | LOPID 600 | Comprimidos x 60 | No disponible en los datos compilados |
| 6326 | LOPID 600 | Comprimidos x 30 | No disponible en los datos compilados |
| 45027 | HIPOLIXAN 900 | Comprimidos x 30 | No disponible en los datos compilados |

Hay 7 autorizaciones vigentes en total (titulares: Pfizer, Bagó y Duncan); aquí se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, colelitiasis y colecistolitiasis, coledocolitiasis, colangitis biliar primaria, trombocitopenia, anemia (incluida la macrocítica), leucopenia e insuficiencia renal.
- **Interacciones farmacológicas** (se identificaron 100 en total; se listan las principales):
  - **Mayores:** rosuvastatina, simvastatina (riesgo de toxicidad muscular), pioglitazona, repaglinida, eluxadolina y loperamida.
  - **Moderadas:** insulinas (aspart, degludec, detemir, glargina, glulisina, humana), clorpropamida, tolazamida, nateglinida, rosiglitazona, rifaximina y ácido quenodesoxicólico.
- La advertencia sobre toxicidad hepática es especialmente relevante: la literatura recuperada para colangitis esclerosante también señala preocupaciones de seguridad hepática con fibratos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta (99.90%), pero no existen ensayos clínicos y la evidencia se limita a estudios preclínicos, algunos con un fármaco relacionado (bezafibrato). El nivel de evidencia es L4 y el vínculo mecanístico es solo indirecto.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del gemfibrozilo
- Estudios preclínicos adicionales con gemfibrozilo específicamente en modelos de artritis reumatoide
- Obtener del prospecto de ANMAT las advertencias y contraindicaciones oficiales (bloqueante para el cribado de seguridad)
- Evaluación de seguridad en pacientes con artritis reumatoide, considerando la hepatotoxicidad y las interacciones con medicamentos de uso habitual
- Si se desea explorar alternativas con más respaldo, valorar indicaciones predichas de mayor evidencia (hipoalfalipoproteinemia o dislipidemia asociada a inhibidores de proteasa del VIH, ambas con nivel L2)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

