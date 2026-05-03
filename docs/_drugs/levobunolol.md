---
layout: default
title: Levobunolol
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 3
---

# Levobunolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Levobunolol: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Levobunolol es un agente bloqueante beta-adrenérgico no selectivo, utilizado en solución oftálmica para reducir la presión intraocular (PIO) en pacientes con glaucoma de ángulo abierto e hipertensión ocular. El modelo TxGNN predice que podría ser efectivo para el **Glaucoma Hereditario Primario**, aunque actualmente **no se registran ensayos clínicos ni publicaciones** que respalden específicamente esta indicación. La plausibilidad mecanística es razonable, dado que esta forma hereditaria comparte como característica central la elevación de la PIO, que es precisamente el blanco terapéutico del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin registro ANMAT — uso farmacológico reconocido: Glaucoma de ángulo abierto / Hipertensión ocular |
| Nueva Indicación Predicha | Glaucoma Hereditario Primario (Primary Hereditary Glaucoma) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 — Predicción del modelo con racionalidad mecanística; sin ensayos clínicos ni literatura específica |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en la fuente consultada (DrugBank, pendiente de resolución). Según la información disponible en la literatura farmacológica, levobunolol es un potente bloqueante no selectivo de los receptores beta-adrenérgicos (β1 y β2), formulado como solución oftálmica tópica. Su eficacia para reducir la PIO en glaucoma de ángulo abierto e hipertensión ocular está ampliamente documentada — múltiples ensayos clínicos controlados con seguimiento de hasta 4 años demuestran reducciones de PIO del 27–30% (≈7–8 mmHg), comparables a las del timolol.

El Glaucoma Hereditario Primario — que incluye formas causadas por mutaciones en genes como *MYOC*, *OPTN* y *WDR36* — comparte con el glaucoma de ángulo abierto común la fisiopatología central de elevación de la PIO con daño progresivo del nervio óptico. Levobunolol reduce la producción de humor acuoso al bloquear los receptores β2 del cuerpo ciliar, inhibiendo la vía del AMPc y disminuyendo directamente la PIO. Este mecanismo es, en principio, independiente de la etiología genética, lo que hace conceptualmente plausible la extrapolación a esta subforma hereditaria.

No obstante, el Glaucoma Hereditario Primario presenta particularidades importantes que justifican cautela: inicio más temprano en la vida (a menudo en niños o adultos jóvenes), progresión más agresiva, y posible respuesta diferente a los hipotensores oculares respecto al glaucoma del adulto de inicio tardío. Actualmente no existen datos clínicos directos que validen la eficacia o la seguridad de levobunolol en este subgrupo específico, lo que clasifica esta predicción en nivel L4.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para levobunolol en Glaucoma Hereditario Primario.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible específicamente para levobunolol en Glaucoma Hereditario Primario.

---

## Información de Mercado en Argentina

Levobunolol no cuenta con autorizaciones de comercialización registradas en Argentina (ANMAT). La consulta a la base de datos regulatoria argentina realizada el 29/03/2026 no arrojó resultados. El fármaco no tiene expedientes de registro activos a la fecha de corte de datos (01/05/2026).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Si bien el mecanismo de acción de levobunolol (reducción de PIO mediante bloqueo β-adrenérgico no selectivo) es farmacológicamente plausible para el Glaucoma Hereditario Primario, la ausencia total de ensayos clínicos y literatura directa para esta indicación específica, combinada con la falta de registro en Argentina, no permite avanzar en este momento. Vale destacar que las predicciones de rango 2 y 3 del modelo (glaucoma 1 de ángulo abierto; glaucoma de ángulo abierto en general) están respaldadas por evidencia nivel L1 con múltiples ECAs y revisiones sistemáticas, lo que confirma el perfil establecido del fármaco en indicaciones relacionadas.

**Para avanzar se necesita:**
- Resolver brecha de datos DG001: obtener advertencias y contraindicaciones del prospecto oficial (fuente: ANMAT/FDA/EMA)
- Resolver brecha de datos DG002: confirmar mecanismo de acción formal en DrugBank
- Revisar literatura sobre el uso de beta-bloqueantes oftálmicos en glaucomas congénitos o hereditarios (población pediátrica y adultos jóvenes)
- Evaluar compatibilidad de formulación tópica ocular para la población objetivo y sus particularidades farmacocinéticas
- Iniciar gestión de registro ante ANMAT como requisito previo a cualquier uso clínico en Argentina
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

