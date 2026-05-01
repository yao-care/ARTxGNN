---
layout: default
title: Ciclosporina
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 0
---

# Ciclosporina
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

# Ciclosporina: Evaluación No Disponible — Datos Insuficientes para el Análisis

## Resumen en Una Frase

Ciclosporina (CICLOSPORINA) es un fármaco conocido por sus propiedades inmunosupresoras, empleado históricamente en el trasplante de órganos y enfermedades autoinmunes.
Sin embargo, el presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, ni datos regulatorios en Argentina, ni información de seguridad recuperable.
En consecuencia, **no es posible realizar una evaluación de reposicionamiento en este momento**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin estudios reales; datos de modelo ausentes) |
| Estado de Mercado en Argentina | ✗ No comercializado (0 autorizaciones registradas) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No Es Posible Continuar el Análisis

El pipeline de generación del Evidence Pack encontró tres bloqueos críticos para este candidato:

**1. Ausencia de indicaciones predichas (`predicted_indications: []`)**
El modelo TxGNN no devolvió ninguna indicación candidata para CICLOSPORINA en la corrida del 2026-03-29. Sin una indicación objetivo, no es posible construir ninguna de las secciones centrales del informe (mecanismo, ensayos clínicos, literatura, ni decisión basada en evidencia).

**2. Sin registro regulatorio en Argentina**
La consulta a ANMAT/TFDA devolvió `result_count: 0` para el nombre INN "CICLOSPORINA". Esto puede deberse a que el fármaco está registrado bajo una grafía diferente ("ciclosporina", "ciclosporin" o marcas comerciales como Sandimmun / Neoral), lo cual requiere reejecutar la consulta con términos alternativos.

**3. Mecanismo de acción y datos de seguridad no recuperados**
Los campos `original_moa`, `key_warnings` y `contraindications` están marcados como `[Data Gap]`, con severidad **Blocking** y **High** respectivamente (DG001, DG002). Sin esta información no se pueden evaluar la plausibilidad mecanística ni los riesgos clínicos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para CICLOSPORINA está incompleto en sus tres dimensiones críticas: predicción del modelo, datos regulatorios y datos de seguridad. No existe base suficiente para emitir una recomendación de reposicionamiento.

**Para avanzar se necesita:**

- [ ] **Re-ejecutar la consulta TxGNN** para CICLOSPORINA / ciclosporin / ciclosporina y verificar que el ID de DrugBank sea correcto (actualmente `null`)
- [ ] **Corregir el término de búsqueda regulatoria**: intentar variantes de grafía ("ciclosporina", "ciclosporin A", "Sandimmun", "Neoral") en ANMAT para obtener registros de autorización
- [ ] **Resolver DG001**: descargar e interpretar el prospecto oficial (TFDA o ANMAT) para obtener advertencias y contraindicaciones
- [ ] **Resolver DG002**: consultar DrugBank API con el ID correcto para recuperar MOA, categorías farmacológicas y datos de toxicidad
- [ ] **Re-ejecutar el pipeline completo** una vez subsanados los gaps anteriores, y volver a generar el Evidence Pack antes de emitir un nuevo informe
---

