---
layout: default
title: Olmesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Olmesartan: nueva indicación predicha, Angina de Prinzmetal (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "OLMESARTAN"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartán: De Indicación No Registrada en ANMAT a Angina de Prinzmetal
{: .text-alpha }

## Resumen en Una Frase

Olmesartán es un antagonista del receptor AT1 de la angiotensina II, comercializado en Argentina en siete autorizaciones vigentes; los datos compilados no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **Angina de Prinzmetal** (puntaje 99,84%), pero para esta predicción **no hay ensayos clínicos ni publicaciones** que la respalden.
La única indicación con evidencia clínica parcial entre las diez predichas es la **migraña** (3 publicaciones, sin ensayos registrados).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Angina de Prinzmetal |
| Puntaje de Predicción TxGNN | 99,84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción. Según el conocimiento general de la clase, olmesartán es un antagonista del receptor AT1 de la angiotensina II, de uso habitual en hipertensión arterial. Esto es conocimiento farmacológico general y no proviene de la indicación registrada en ANMAT.

Para la angina de Prinzmetal (vasoespástica), un vínculo plausible sería la reducción del vasoespasmo mediante el bloqueo de la angiotensina II y la mejora de la función endotelial. Sin embargo, es solo una hipótesis: no se aportaron ensayos ni literatura que la respalden, y la predicción se basa únicamente en el modelo.

Otras predicciones de alto puntaje merecen una lectura distinta:
- **Migraña** (puntaje 99,64%): es la que cuenta con más respaldo clínico indirecto. Hay un estudio pequeño en pacientes hipertensos/prehipertensos, un comentario y una revisión sistemática de 2019 sobre IECA y ARA-II (nivel L3). El efecto en los estudios específicos de olmesartán puede estar confundido por la reducción de la presión arterial.
- **Hipertensión pulmonar** (99,61%): solo hay estudios preclínicos en ratas y ratones (L4), sin evidencia en humanos.
- **Alopecia y trastornos capilares congénitos**: no hay mecanismo plausible evidente; el puntaje podría reflejar cercanía en el grafo de conocimiento más que una relación farmacológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Angina de Prinzmetal.

Como referencia, el único ensayo identificado entre las predicciones corresponde a hipertensión pulmonar y se evaluó como no relevante:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Fase 4 | Suspendido | 2414 | Ensayo en COVID-19 sobre continuar o suspender IECA/ARA-II; no aborda hipertensión pulmonar |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Angina de Prinzmetal.

La literatura disponible para la predicción con mayor respaldo (migraña) es:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Revisión sistemática | Current Pain and Headache Reports | Eficacia de IECA y ARA-II en la prevención de migraña episódica en adultos; respaldo a nivel de clase |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | Estudio clínico pequeño | Headache | Efecto de olmesartán sobre la frecuencia y gravedad de la migraña en pacientes con hipertensión/prehipertensión |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | Comentario/Carta | Headache | Comentario sobre olmesartán, migraña y presión arterial |

Para hipertensión pulmonar, la evidencia es preclínica (PMID [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/), [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/) y [17089097](https://pubmed.ncbi.nlm.nih.gov/17089097/)): en modelos de rata y ratón, olmesartán atenuó la hipertensión pulmonar inducida por monocrotalina e hipoxia, posiblemente mediante la inhibición de ERK1/2 y de señales proinflamatorias.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60980 | OLTUX (Nolter) | 40 mg, comprimidos recubiertos x 30 | No disponible |
| 40680 | OLMETEC (MSD Argentina) | 40 mg, comprimidos recubiertos x 28 | No disponible |
| 40679 | OLMETEC (MSD Argentina) | 20 mg, comprimidos recubiertos x 28 | No disponible |
| 60979 | OLTUX (Nolter) | 20 mg, comprimidos recubiertos x 30 | No disponible |
| 35191 | TENSONIT (Teva Argentina) | 20 mg, comprimidos recubiertos x 30 | No disponible |

Hay 7 autorizaciones vigentes en total; se muestran las 5 principales. Las otras dos corresponden a OLMETEC D 20/12.5 (40681) y OLMETEC D 40/12.5 (40682), de MSD Argentina.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 94 interacciones en total. Entre las principales:
  - **Mayor**: cloruro de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - **Moderada**: hidrocortisona, eluxadolina, exenatida, polietilenglicol con electrolitos y múltiples insulinas (humana, aspart, degludec, detemir, glargina, glulisina, lispro, entre otras).

Como contexto de seguridad, un reporte de caso reciente (2026) recuerda que los ARA-II están contraindicados en el embarazo por riesgo de oligohidramnios, disgenesia renal e hipoplasia pulmonar fetal. Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (angina de Prinzmetal) se apoya solo en el puntaje del modelo (L5), sin ensayos ni publicaciones. La migraña es la línea con más respaldo (L3, "pregunta de investigación"), pero se basa en estudios pequeños y en datos de clase, con efecto confundido por la presión arterial.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT (indicación aprobada, advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de evidencia clínica sobre olmesartán (o ARA-II) en angina vasoespástica.
- Para migraña, evaluar la viabilidad de un ensayo controlado en pacientes normotensos que separe el efecto antimigrañoso del hipotensor.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

