---
layout: default
title: Oxymetazoline
parent: Evidencia Moderada (L3-L4)
nav_order: 208
evidence_level: L4
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Oximetazolina: De Faringitis y Resfriado Común a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La oximetazolina es un simpaticomimético tópico, utilizado originalmente para aliviar la congestión nasal asociada a la faringitis y al resfriado común.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**,
pero actualmente no hay **ensayos clínicos** registrados y solo existen **5 publicaciones** de relevancia heterogénea, por lo que la evidencia es limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Faringitis y resfriado común (según el grafo de conocimiento; el texto de indicación de la licencia local no está disponible) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la oximetazolina es un agonista adrenérgico alfa-1/alfa-2 de uso tópico que provoca vasoconstricción de la mucosa, con lo que reduce la congestión nasal y el flujo sanguíneo mucoso. Los datos farmacológicos compilados muestran además afinidad por receptores adrenérgicos alfa-1 (A, B, D) y alfa-2 (A, B, C), así como por los receptores serotoninérgicos 5-HT1B, 5-HT1D y 5-HT2C.

Este mecanismo es coherente con diversas afecciones de la cavidad nasal que cursan con congestión, inflamación o sangrado. Sin embargo, las indicaciones originales (resfriado común y faringitis) ya se solapan en gran medida con esta categoría. El puntaje elevado del modelo puede reflejar la cercanía con usos ya aprobados y no una indicación realmente nueva.

La literatura de apoyo es heterogénea: incluye un estudio de función olfatoria en rinitis aguda, un estudio animal de sinusitis, reportes de casos y estudios procedimentales o diagnósticos en los que la oximetazolina probablemente es un agente accesorio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Estudio clínico | Annals of the New York Academy of Sciences | Evaluó el efecto del resfriado común sobre la función olfatoria en 36 sujetos, con potenciales evocados quimiosensoriales y rinometría acústica |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Estudio animal | Annals of Otology, Rhinology, and Laryngology | Evaluó gotas nasales de oximetazolina sobre la defensa tisular local en sinusitis bacteriana aguda en 14 conejos |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Serie de casos/procedimental | American Journal of Rhinology & Allergy | Tratamiento con coblación de telangiectasias nasales en telangiectasia hemorrágica hereditaria; la oximetazolina probablemente es coadyuvante |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Estudio de medición clínica | Journal of Plastic Surgery and Hand Surgery | Permeabilidad nasal por rinometría acústica tras reparación de fisura labiopalatina unilateral; la oximetazolina probablemente se usó como descongestionante para la medición |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Reporte de caso | Global Pediatric Health | Rinoescleroma en un niño de 9 años, con obstrucción nasal como presentación frecuente |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43788 | OXILER D | Spray x 10 ml | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, diabetes mellitus, cetoacidosis diabética, hiperplasia prostática benigna, enfermedad cardíaca y cardiovascular, enfermedad coronaria, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis), enfermedades infecciosas oculares, conjuntivitis, arteriosclerosis y aterosclerosis, y trastornos de la visión o ceguera.
- **Interacciones farmacológicas**: la consulta se completó y devolvió 9 registros, todos de tipo farmacológico (afinidad por receptores 5-HT1B, 5-HT1D, 5-HT2C, alfa-1A/1B/1D y alfa-2A/2B/2C), sin interacciones medicamentosas con nivel de gravedad asignado.
- **Nota para la cefalea**: una revisión sobre interacciones con inhibidores de la MAO (PMID 36425231) sugiere riesgo de eventos hipertensivos o cefalea con simpaticomiméticos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de enfermedad de la cavidad nasal tiene un puntaje muy alto, pero no cuenta con ensayos clínicos y su literatura es indirecta o accesoria (nivel L4). Además, se solapa con las indicaciones ya conocidas, por lo que no constituye una señal clara de reposicionamiento.

**Para avanzar se necesita:**
- Obtener el prospecto de ANMAT con advertencias y contraindicaciones oficiales, así como el texto de la indicación aprobada
- Complementar los datos del mecanismo de acción desde DrugBank
- Definir si la indicación predicha es realmente distinta de los usos ya aprobados (resfriado común y faringitis)
- Generar estudios clínicos específicos, en los que la oximetazolina sea el agente principal
- Evaluar el perfil de riesgo cardiovascular y de otras comorbilidades señaladas en las contraindicaciones del grafo de conocimiento

---

### Otras indicaciones predichas (referencia)

- **Laringofaringitis aguda** (TxGNN 99.95%, L5, Hold): sin ensayos ni literatura; se solapa con la faringitis original y no aporta una señal de reposicionamiento distinta.
- **Trastorno de cefalea** (TxGNN 99.04%, L3, pregunta de investigación): el estudio de tetracaína intranasal al 3% con oximetazolina al 0.05% en estatus migrañoso (PMID 31919839) sugiere un posible efecto sobre el ganglio esfenopalatino, pero no permite atribuirlo a la oximetazolina sola. No hay ensayos registrados y existen preocupaciones de seguridad con simpaticomiméticos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

