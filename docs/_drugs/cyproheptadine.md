---
layout: default
title: Cyproheptadine
parent: Evidencia Moderada (L3-L4)
nav_order: 118
evidence_level: L4
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Ciproheptadina: De Rinitis Alérgica y Urticaria a Urticaria Alérgica

## Resumen en Una Frase

Ciproheptadina es un antihistamínico de primera generación, utilizado originalmente para rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, conjuntivitis alérgicas, urticaria y angioedema.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero no hay **ensayos clínicos registrados** y la evidencia se limita a **9 publicaciones**, en su mayoría antiguas (1961-1995).
Cabe señalar que esta indicación es en gran parte una reformulación de un uso ya existente, y no un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, conjuntivitis atópica, urticaria y angioedema (según el grafo de conocimiento; el texto de indicación aprobado en las autorizaciones locales no está disponible) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la ciproheptadina es un antihistamínico H1 de primera generación con actividad adicional antagonista de 5-HT2 y efecto anticolinérgico. Su eficacia en cuadros alérgicos y urticaria es conocida, y mecanísticamente es aplicable a la urticaria alérgica.

La urticaria ya figura entre las indicaciones originales del fármaco (junto con angioedema y dermatosis alérgicas). Por ello, la predicción refleja sobre todo un uso existente más que una nueva indicación. La formación de ronchas y el prurito mediados por histamina y serotonina ofrecen un vínculo mecanístico plausible.

La literatura de apoyo consiste principalmente en evaluaciones clínicas antiguas (1961-1976), sin ensayos registrados en los datos compilados.

**Otras predicciones del modelo (para contexto):**
- **Urticaria por frío** (99.76%, nivel L3): extensión cercana de la indicación de urticaria. Existen estudios comparativos y doble ciego (1977-1995) con muestras pequeñas, donde la ciproheptadina fue a menudo tratamiento de referencia. Las guías actuales favorecen antihistamínicos de segunda generación por la sedación y la carga anticolinérgica.
- **Enfermedad de la cavidad nasal** (99.21%, L5) y **laringofaringitis aguda** (99.13%, L5): predicciones amplias o inespecíficas, probablemente derivadas de indicaciones ya existentes, sin evidencia directa. No deben considerarse señales de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Ensayo comparativo doble ciego cruzado | Asian Pac J Allergy Immunol | Comparación de ciproheptadina y ketotifeno en 6 niños tailandeses con urticaria por frío primaria adquirida |
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | Evaluación comparativa de eficacia | Curr Ther Res | Eficacia relativa de ciproheptadina e hidroxizina en el prurito de dermatosis alérgicas |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Revisión (indirecta, acrivastina) | Drugs | Revisión de acrivastina en rinitis alérgica y urticaria; evidencia indirecta para ciproheptadina |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | Estudio diagnóstico/cohorte | Asian Pac J Allergy Immunol | Prueba del cubo de hielo en niños; tras 4 semanas de ciproheptadina, solo 17% positivo a los 3 minutos |
| [4382319](https://pubmed.ncbi.nlm.nih.gov/4382319/) | 1967 | Estudio clínico/revisión | Med Lett Drugs Ther | Revisión de ciproheptadina (Periactin) en dermatosis alérgicas y pruriginosas |
| [13685954](https://pubmed.ncbi.nlm.nih.gov/13685954/) | 1961 | Estudio clínico temprano (no controlado) | Br Med J | Ciproheptadina en el tratamiento de la urticaria |
| [14347187](https://pubmed.ncbi.nlm.nih.gov/14347187/) | 1965 | Estudio clínico (combinación con dexametasona) | Rev Lyon Med | Resultados iniciales de una combinación de ciproheptadina y dexametasona en dermatosis inflamatorias y alérgicas |
| [14106555](https://pubmed.ncbi.nlm.nih.gov/14106555/) | 1964 | Evaluación clínica | J Assoc Physicians India | Evaluación clínica de ciproheptadina en dermatosis alérgica |
| [14138414](https://pubmed.ncbi.nlm.nih.gov/14138414/) | 1964 | Estudio clínico pediátrico | Arerugi | Efecto terapéutico de inhibidores de serotonina en enfermedades alérgicas infantiles |

**Evidencia adicional para urticaria por frío (predicción de rango 2):**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | Ensayo doble ciego comparativo | Arch Dermatol | Ciproheptadina, clorfeniramina y placebo en 8 sujetos con urticaria por frío primaria adquirida |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | Ensayo aleatorizado doble ciego | J Am Acad Dermatol | Comparación de cinarizina, ciproheptadina, doxepina e hidroxizina; la doxepina fue preferida |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | Ensayo doble ciego cruzado | Dermatologica | Acrivastina y ciproheptadina redujeron significativamente las ronchas frente a placebo; acrivastina fue más eficaz (18 pacientes) |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | Estudio clínico | J Allergy Clin Immunol | Con ciproheptadina los pacientes quedaron asintomáticos y la prueba del cubo de hielo se normalizó |

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49668 | CIPROVIT CALCICO | Comprimidos en blíster x 60 | No disponible |
| 158 | CIPROVIT MAGNESICO | Granulado en sobres x 20 | No disponible |
| 50366 | CIPROVIT CALCICO | Jarabe x 150 ml | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): trastorno hipertensivo e hipertensión, enfermedad ulcerosa péptica, hiperplasia prostática benigna, hipertensión ocular, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis) y obstrucción del cuello vesical.
- **Interacciones Farmacológicas**: se identificaron 308 interacciones. Las más relevantes:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas** (sobre todo por efecto anticolinérgico o depresor del SNC): atropina, hiosciamina, escopolamina, glicopirronio, diciclomina, trospio, propantelina, metescopolamina, mepenzolato, loperamida, morfina, opio, dronabinol, nabilona, eluxadolina, metoclopramida y fenfluramina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La urticaria ya es una indicación original de la ciproheptadina, por lo que la predicción no representa un reposicionamiento real. La evidencia disponible es antigua, de baja calidad (nivel L4) y sin ensayos registrados. Las guías actuales favorecen antihistamínicos de segunda generación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del texto de indicación aprobado en los prospectos de ANMAT.
- Advertencias y contraindicaciones del prospecto de ANMAT, ya que actualmente solo se dispone de contraindicaciones derivadas del grafo de conocimiento.
- Si se desea explorar la urticaria por frío, una revisión sistemática o ensayos modernos que comparen la ciproheptadina con antihistamínicos de segunda generación.
- Evaluación de la carga anticolinérgica y sedante en poblaciones vulnerables (niños, adultos mayores, pacientes con hipertensión o glaucoma).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

