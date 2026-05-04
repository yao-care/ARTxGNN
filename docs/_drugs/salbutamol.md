---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: De Asma / COPD a Conjuntivitis Papilar

## Resumen en Una Frase

Salbutamol es un broncodilatador de accion corta (agonista β2-adrenérgico), ampliamente reconocido a nivel mundial para el alivio del broncoespasmo asociado al asma y la enfermedad pulmonar obstructiva cronica (EPOC), aunque no figura con autorizaciones en la base de datos de ANMAT consultada.
El modelo TxGNN predice que podria ser efectivo para **Conjuntivitis Papilar**,
sin embargo, actualmente **no existen ensayos clinicos ni publicaciones cientificas** que respalden directamente esta nueva direccion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Broncoespasmo / Asma y EPOC (uso global establecido; sin registro ANMAT en la base de datos consultada) |
| Nueva Indicacion Predicha | Conjuntivitis Papilar (Papillary Conjunctivitis) |
| Puntaje de Prediccion TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | No Comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Salbutamol es un agonista selectivo del receptor β2-adrenérgico de accion corta (SABA). Su mecanismo de accion establecido consiste en estimular los receptores β2 presentes en el musculo liso bronquial, lo que incrementa el AMP ciclico (AMPc) intracelular y produce relajacion del musculo liso con la consecuente broncodilatacion. Ademas, se ha descrito que los agonistas β2 poseen efectos secundarios de estabilizacion de mastocitos, inhibiendo su degranulacion y la liberacion de mediadores proinflamatorios. Actualmente no se dispone de datos detallados sobre el mecanismo de accion en la fuente de datos consultada; la descripcion anterior se basa en el conocimiento farmacologico globalmente disponible.

La conjuntivitis papilar es una enfermedad inflamatoria de la conjuntiva cuya patogenia principal involucra irritacion mecanica cronica (depositos en lentes de contacto, protesis oculares) o mecanismos mediados por IgE. Dado que el tejido conjuntival expresa receptores β2-adrenérgicos, teoricamente un agonista β2 podria ejercer algun efecto antiinflamatorio local mediante la inhibicion de la degranulacion de mastocitos y la reduccion de la permeabilidad vascular, lo que tendria relevancia particular en la variante alérgica de esta patologia.

Sin embargo, la relacion mecanistica es considerada débil para esta indicacion. La principal via patogénica de la conjuntivitis papilar involucra friccion mecanica y respuesta IgE, frente a las cuales los β2-agonistas no constituyen un mecanismo terapéutico de primera linea. El elevado puntaje TxGNN probablemente refleja proximidad a nivel de red biologica entre tejidos de la via respiratoria superior y el segmento ocular, mas que una prediccion directa de eficacia farmacologica. La ausencia total de evidencia clinica en humanos refuerza la necesidad de cautela.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en Argentina

No se registran autorizaciones de comercializacion de Salbutamol en la base de datos de ANMAT consultada (0 registros). Cabe destacar que Salbutamol es un farmaco de uso ampliamente difundido a nivel mundial y es posible que existan registros vigentes bajo denominaciones comerciales o titulares distintos no capturados en la presente consulta.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion TxGNN para conjuntivitis papilar alcanza nivel de evidencia L5 (solo prediccion computacional, sin ningun estudio real disponible), y la relacion mecanistica entre el agonismo β2 y los principales mecanismos patogenicos de esta enfermedad (friccion mecanica, mediacion IgE) es debil. No existe base suficiente para avanzar hacia desarrollo clinico en este momento.

**Para avanzar se necesita:**
- Datos de expresion del receptor β2-adrenérgico en tejido conjuntival humano (evidencia preclínica de mecanismo)
- Estudios preclínicos en modelos animales de conjuntivitis papilar con salbutamol topico oftalmico
- Evaluacion de seguridad y tolerabilidad de una formulacion topica ocular de salbutamol
- Publicaciones o reportes de caso que documenten cualquier uso ocular de salbutamol en humanos
- Aclaracion sobre el estado real de registro de Salbutamol en ANMAT (busqueda ampliada por nombre comercial o titular)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

