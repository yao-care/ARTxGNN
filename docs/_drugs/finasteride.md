---
layout: default
title: Finasteride
parent: Solo Predicción del Modelo (L5)
nav_order: 143
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Finasteride: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: Hiperplasia prostática benigna"
---

# Finasteride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Finasterida: De Hiperplasia Prostática Benigna a Ambras tipo hipertricosis universal congénita

## Resumen en Una Frase

Finasterida es un inhibidor de la 5-alfa-reductasa tipo II, originalmente utilizado para el tratamiento de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Finasterida inhibe la 5-alfa-reductasa tipo II y reduce los niveles de dihidrotestosterona (DHT). Este mecanismo explica su uso en la hiperplasia prostática benigna y, a dosis menores (1 mg), en la alopecia androgenética, lo que indica que el fármaco actúa sobre la biología del folículo piloso dependiente de andrógenos.

Sin embargo, el síndrome de Ambras es una hipertricosis congénita rara, asociada a reordenamientos del cromosoma 8q22 que afectan la regulación del gen TRPS1. No es claramente dependiente de andrógenos, por lo que la reducción de DHT encaja débilmente con su causa. El puntaje del modelo es muy alto (0,99994), pero no se respalda con ensayos ni literatura.

Conviene señalar también que, entre las otras predicciones, la hipertricosis en general (puntaje 99.99%) cuenta con 4 documentos de literatura, aunque son revisiones narrativas y un trabajo de métodos, sin evidencia controlada sobre finasterida. Esa indicación alcanza el nivel L4, pero también se mantiene en Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11845 | PROSCAR (Organon Arg.) | Comprimidos x 30 | No disponible |
| 21216 | PROPECIA (Organon Arg.) | 1 mg, comprimidos recubiertos x 30 | No disponible |
| 13953 | PROSTENE (Teva Argentina) | 5 mg, comprimidos x 30 | No disponible |
| 48814 | HPB PANALAB (Panalab) | 5 mg, comprimidos recubiertos x 28 | No disponible |
| 23124 | CAPILFOR (Finadiet) | 1 mg, comprimidos x 30 | No disponible |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según grafo de conocimiento, no texto de prospecto)**: enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 100 posibles interacciones, todas con nivel de gravedad no clasificado. Entre las listadas figuran calcitriol, doxiciclina, clotrimazol, bupropión, metformina, omeprazol, ácido acetilsalicílico y morfina.
- **Contexto del desarrollo**: dado que finasterida puede afectar el desarrollo genital del feto masculino, su uso en indicaciones congénitas o pediátricas exige especial cautela.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero carece de ensayos clínicos y literatura (nivel L5), y el mecanismo de reducción de DHT es un ajuste débil para una hipertricosis congénita no claramente androgénica.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del fármaco
- Revisión de las advertencias y contraindicaciones del prospecto de ANMAT
- Evidencia preclínica o mecanística que vincule la vía de la DHT con la regulación de TRPS1 en el síndrome de Ambras
- Evaluación de compatibilidad de vía de administración y de población objetivo (incluida la seguridad en pediatría)
- Considerar priorizar indicaciones con más respaldo (por ejemplo, hirsutismo/hipertricosis) antes de invertir en esta predicción
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

