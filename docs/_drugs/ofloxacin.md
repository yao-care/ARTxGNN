---
layout: default
title: Ofloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ofloxacin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Infecciones bacterianas (fiebre tifoidea, salmonelosis…"
---

# Ofloxacin
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

# Ofloxacino: De Infecciones Bacterianas (Fiebre Tifoidea) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

El ofloxacino es un antibiótico fluoroquinolónico, usado originalmente para infecciones bacterianas como la fiebre tifoidea, las infecciones urinarias, la bronquitis y la neumonía bacteriana.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (fiebre tifoidea, salmonelosis, infección urinaria, bronquitis, neumonía bacteriana, entre otras), según el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El ofloxacino es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas, enzimas necesarias para que la bacteria replique su ADN. Esto explica su eficacia en infecciones por *Salmonella*, *Pseudomonas aeruginosa*, estreptococos y estafilococos. No se dispone de datos detallados del mecanismo de acción en la información compilada para este informe.

**Con los datos actuales, esta predicción no tiene una base biológica plausible.** La hiperviscosidad policlonal se origina por un exceso de inmunoglobulinas séricas, un proceso sin relación con la acción antibacteriana del ofloxacino. El puntaje alto de TxGNN (99.91%) refleja patrones del grafo de conocimiento, no evidencia experimental o clínica.

No hay vínculo entre la indicación original (infecciones bacterianas) y la nueva (un trastorno hematológico asociado a inmunoglobulinas). Por ello, el puntaje debe tomarse solo como una hipótesis sin respaldo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 22487 | OTOFLOX | Gotas óticas x 10 ml | Cassará |
| 13697 | OFLOX | Solución oftálmica x 5 ml | Abbvie |

Ambas autorizaciones están vigentes y son de monofármaco. Las dos presentaciones disponibles son de uso local (ótico y oftálmico). Estas vías no alcanzarían niveles sistémicos adecuados para una condición hematológica sistémica como la hiperviscosidad.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no texto de prospecto)**:
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes.
  - Hepáticas y renales: insuficiencia hepática, enfermedad hepática, lesión hepática inducida por fármacos, enfermedad de la vesícula biliar, enfermedad renal, función renal alterada.
  - Neurológicas y neuromusculares: epilepsia, neuropatía periférica y enfermedades del sistema nervioso periférico, miastenia gravis y enfermedades de la unión neuromuscular.
  - Musculoesqueléticas: tendinitis, periartritis, rabdomiólisis, fascitis nodular, exostosis.
  - Metabólicas: diabetes mellitus, cetoacidosis diabética, deficiencia de potasio.
  - Hematológicas: trombocitopenia, leucopenia, anemia (incluida la macrocítica).
  - Gastrointestinales: colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal.
- **Interacciones farmacológicas**: se registraron 383 interacciones. Entre las primeras 20 listadas:
  - **Mayores**: hidrocortisona, dexametasona, betametasona, triamcinolona (corticoides), bupropión y clorpropamida.
  - **Moderadas**: antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodilo y sales de calcio o potasio (fosfato de calcio, acetato de calcio, citrato de potasio).

Para advertencias específicas de uso, consultar el prospecto aprobado por ANMAT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de hiperviscosidad policlonal es de nivel L5. No hay ensayos, no hay literatura y no hay mecanismo plausible. Además, las presentaciones disponibles en Argentina son de uso local (ótico y oftálmico), poco adecuadas para una condición sistémica.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que conecte el ofloxacino con la hiperviscosidad, o evidencia preclínica que la respalde. Sin ella no se justifica continuar.
- Los datos de mecanismo de acción y el texto aprobado de indicaciones y advertencias del prospecto de ANMAT.
- Si se busca valor de reposicionamiento, priorizar otras predicciones del mismo modelo. La **peste septicémica** tiene evidencia preclínica (nivel L4): sensibilidad *in vitro* de *Yersinia pestis* y eficacia del ofloxacino en modelos murinos. Es una extensión de su espectro antibacteriano y no un reposicionamiento a un mecanismo nuevo. Aun así, carece de ensayos en humanos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

