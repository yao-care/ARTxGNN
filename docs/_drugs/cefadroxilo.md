---
layout: default
title: Cefadroxilo
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Cefadroxilo
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Cefadroxilo: Evaluación de Reposicionamiento — Predicción No Disponible

## Resumen en Una Frase

Cefadroxilo es un antibiótico beta-lactámico de primera generación de la familia cefalosporina, utilizado ampliamente en el tratamiento de infecciones bacterianas de piel, vías urinarias y faringoamigdalitis estreptocócica. El modelo TxGNN **no generó predicciones de nuevas indicaciones** para este fármaco en el ciclo de análisis actual, debido a brechas críticas en los datos de entrada. Sin una indicación predicha, no es posible realizar una evaluación completa de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos en el Evidence Pack |
| Nueva Indicación Predicha | No disponible |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 — Sin estudios reales |
| Estado de Mercado en Argentina | Sin registro ANMAT (no comercializado) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué No hay Predicciones Disponibles

El Evidence Pack presenta dos brechas de datos clasificadas como **Blocking / High** que impidieron la generación de predicciones por el modelo TxGNN:

**Brecha DG001 — Advertencias del Prospecto (Severidad: Bloqueante)**
No se pudieron obtener las advertencias y contraindicaciones oficiales del prospecto ANMAT. Sin esta información, el pipeline no puede completar la evaluación de seguridad inicial (S1), que es un requisito previo para la generación de candidatos.

**Brecha DG002 — Mecanismo de Acción (Severidad: Alta)**
Los datos de MOA no están disponibles en DrugBank para este registro. TxGNN utiliza el mecanismo de acción como uno de los insumos principales para construir relaciones en el Knowledge Graph y proyectar nuevas indicaciones. Sin este dato, la capacidad del modelo queda limitada.

**Nota informativa:** A partir de conocimiento farmacológico general, Cefadroxilo es una cefalosporina de primera generación cuyo mecanismo consiste en la inhibición de la síntesis de pared celular bacteriana mediante la unión a proteínas fijadoras de penicilina (PBPs). Estos datos, sin embargo, no están reflejados en el Evidence Pack actual y no pueden utilizarse como insumo formal del pipeline sin validación desde DrugBank.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El pipeline TxGNN no pudo generar predicciones de reposicionamiento para Cefadroxilo debido a brechas en los datos de MOA y en el prospecto oficial. Sin una indicación predicha, toda evaluación posterior (evidencia clínica, literatura, análisis mecanístico) carece de objeto.

**Para avanzar se necesita:**

- **[DG001 — Bloqueante]** Descargar y parsear el prospecto oficial desde el sitio de ANMAT para extraer advertencias, contraindicaciones y categorías de seguridad
- **[DG002 — Alta]** Consultar la API de DrugBank con el nombre genérico "Cefadroxil" (sin tilde, nombre INN en inglés) para obtener MOA, categorías farmacológicas y targets
- **Re-ejecutar el pipeline TxGNN** una vez resueltas DG001 y DG002, con los datos de MOA y seguridad completados
- **Verificar registros ANMAT** bajo nombres alternativos: *Cefadroxil*, *Duricef*, *Ultracef*, *Baxan*, ya que la búsqueda con el nombre en español pudo haber fallado por variación ortográfica
---

