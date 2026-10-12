---
layout: default
title: Thiocolchicoside
parent: Solo Predicción del Modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 2
---

# Thiocolchicoside
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Tiocolchicósido: De Indicación No Especificada a Insomnio

## Resumen en Una Frase

Tiocolchicósido es un derivado semisintético de la colchicósida, utilizado como relajante muscular y comercializado en Argentina bajo la marca MOLAGAR; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio** (y, en segundo lugar, para delirium por abstinencia alcohólica), pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones registradas (el texto de indicación está vacío); como referencia, se lo conoce como relajante muscular |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción original del fármaco. Según la información farmacológica conocida, el tiocolchicósido es un derivado semisintético de la colchicósida usado como relajante muscular. Su farmacología mejor caracterizada es el antagonismo competitivo de los receptores GABA-A y, en menor medida, de los receptores de glicina sensibles a estricnina. La modulación de GABA-A es una vía plausible para la sedación, lo que ofrece un vínculo teórico con el insomnio.

Sin embargo, existe un conflicto de dirección importante: el tiocolchicósido actúa como **antagonista** de GABA-A y tiene potencial proconvulsivante, lo cual es opuesto a la modulación GABAérgica positiva de los hipnóticos establecidos (benzodiazepinas, fármacos Z). El puntaje alto de TxGNN (0.999) proviene de una predicción basada en redes, sin ensayos clínicos ni literatura que la sustenten, por lo que el vínculo mecanístico no puede verificarse con la evidencia disponible.

La segunda predicción, **delirium por abstinencia alcohólica** (puntaje 99.21%), presenta el mismo problema: este cuadro implica hipofunción GABAérgica e hiperexcitabilidad glutamatérgica, y un antagonista de GABA-A podría empeorar, no aliviar, la hiperexcitabilidad neuronal y el riesgo de convulsiones. El tratamiento de primera línea (benzodiazepinas) potencia la señal GABA-A, por lo que el mecanismo propuesto parece direccionalmente inconsistente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45510 | MOLAGAR (Finadiet) | 4 mg a.x 6 | No especificada |
| 45397 | MOLAGAR (Finadiet) | 4 mg comp.x 20 | No especificada |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal de alerta mecanística (no proveniente del texto del prospecto), se describe que el tiocolchicósido se asocia con convulsiones en estudios en animales y en farmacovigilancia clínica, lo que es especialmente relevante para las indicaciones predichas. No se encontraron interacciones farmacológicas registradas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ambas predicciones (insomnio y delirium por abstinencia alcohólica) son solo del modelo (nivel L5), sin ensayos ni literatura, y su mecanismo contradice la farmacología conocida del fármaco (antagonismo de GABA-A con riesgo proconvulsivante).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de ANMAT (advertencias y contraindicaciones), que es un vacío bloqueante para el análisis de seguridad
- Confirmar el mecanismo de acción en DrugBank y resolver la inconsistencia direccional con GABA-A
- Realizar una revisión sistemática de literatura y estudios preclínicos que respalden (o refuten) un efecto sobre el sueño
- Evaluar con especial cuidado el riesgo de convulsiones antes de considerar cualquier estudio clínico
- Completar el texto de las indicaciones aprobadas de las dos autorizaciones locales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

