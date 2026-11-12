---
noindex: true
sitemap: false
layout: default
title: Ciclosporina
parent: Solo Predicción del Modelo (L5)
nav_order: 99
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Ciclosporina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **0** 
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

## Ciclosporina: Evaluación No Disponible — Datos Insuficientes para el Análisis
{: .text-alpha }

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
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (4 de 4) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | 4 (vigentes: 4) |
| Decisión Recomendada | **Hold** |

---

## Por qué No Es Posible Continuar el Análisis

El pipeline de generación del Evidence Pack encontró tres bloqueos críticos para este candidato:

**1. Ausencia de indicaciones predichas (`predicted_indications: []`)**
El modelo TxGNN no devolvió ninguna indicación candidata para CICLOSPORINA en la corrida del 2026-03-29. Sin una indicación objetivo, no es posible construir ninguna de las secciones centrales del informe (mecanismo, ensayos clínicos, literatura, ni decisión basada en evidencia).

**2. Sin registro regulatorio en Argentina**

<!-- review:begin ar-lic-20261106-ciclosporina-1 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «Sin registro regulatorio en Argentina** / La consulta a ANMAT/TFDA devolvió `result_count: 0` para el nombre INN "CICLOSPORINA". Esto puede deberse a que el fármaco está registrado bajo una grafía diferente ("ciclosporina", "ciclosporin" o marcas comerciales como Sandimmun / Neoral), lo cual requiere reejecutar la consulta con términos alternativos.» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-ciclosporina-1 -->

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
- [ ] **Resolver DG001**: descargar e interpretar el prospecto oficial (ANMAT) para obtener advertencias y contraindicaciones
- [ ] **Resolver DG002**: consultar DrugBank API con el ID correcto para recuperar MOA, categorías farmacológicas y datos de toxicidad
- [ ] **Re-ejecutar el pipeline completo** una vez subsanados los gaps anteriores, y volver a generar el Evidence Pack antes de emitir un nuevo informe

<!-- review:begin ar-lic-20261106-ciclosporina-2 -->

> **Corrección de verificación (2026-11-06)**: Texto original: «[ ] **Resolver DG001**: descargar e interpretar el prospecto oficial (TFDA o ANMAT) para obtener advertencias y contraindicaciones» Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página. Fuente: [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades).

<!-- review:end ar-lic-20261106-ciclosporina-2 -->

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-06 | Eliminado: «La consulta a ANMAT/TFDA devolvió `result_count: 0` para el nombre INN "CICLOSPORINA". Esto puede deberse a que el fármaco está registrado b» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |
| 2026-11-06 | Eliminado: «TFDA o» | Corregido | [PAMI – Medicamentos para entidades (datos abiertos)](https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

