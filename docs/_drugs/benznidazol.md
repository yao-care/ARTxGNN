---
layout: default
title: Benznidazol
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 0
---

# Benznidazol
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

# Benznidazol: Evaluación Preliminar — Sin Indicaciones Predichas por TxGNN

## Resumen en Una Frase

Benznidazol es un fármaco antiparasitario de la clase nitroimidazol, reconocido internacionalmente como tratamiento de primera línea para la enfermedad de Chagas (tripanosomiasis americana causada por *Trypanosoma cruzi*). Actualmente, el modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco, y no se encontraron autorizaciones de comercialización en el mercado regulatorio consultado.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Enfermedad de Chagas (tripanosomiasis americana) — según uso reconocido internacionalmente¹ |
| Nueva Indicación Predicha | — No disponible (sin predicciones TxGNN) |
| Puntaje de Predicción TxGNN | — No disponible |
| Nivel de Evidencia | L5 — Solo información de referencia, sin predicción ni estudios asociados |
| Estado de Mercado | ✗ No comercializado en el mercado regulatorio consultado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

> ¹ Benznidazol no presenta indicaciones aprobadas en las bases de datos regulatorias consultadas (TFDA). Sin embargo, es ampliamente reconocido como tratamiento estándar para la enfermedad de Chagas en Latinoamérica (aprobado por ANMAT en Argentina, FDA en EE.UU. para uso pediátrico, y recomendado por la OMS).

---

## ¿Por qué no hay Predicciones?

El modelo TxGNN no generó predicciones de reposicionamiento para benznidazol. Esto puede deberse a varios factores:

1. **Ausencia en el grafo de conocimiento (KG):** Benznidazol es un fármaco antiparasitario de nicho, principalmente utilizado en regiones endémicas de la enfermedad de Chagas. Es posible que el fármaco no esté suficientemente representado en las redes de conocimiento biomédico utilizadas por TxGNN, lo que impide la generación de predicciones.

2. **Mecanismo de acción específico:** Benznidazol actúa mediante la generación de radicales libres y metabolitos reactivos que dañan el ADN y las proteínas del parásito *Trypanosoma cruzi*. Este mecanismo es altamente específico contra organismos parasitarios y podría tener limitada aplicabilidad a otras patologías humanas según los modelos de predicción.

3. **Brechas de datos:** El Evidence Pack registra brechas significativas en datos clave (DrugBank ID ausente, MOA no disponible en la base consultada, sin información de seguridad regulatoria local), lo que limita la capacidad del modelo para establecer conexiones con otras indicaciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones registrados en el Evidence Pack.

> **Nota:** Existen numerosos ensayos clínicos para benznidazol en su indicación original (enfermedad de Chagas), incluyendo el estudio BENEFIT (NCT01162967), pero estos corresponden a la indicación establecida y no a reposicionamiento.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones disponible en el Evidence Pack.

---

## Información de Mercado

| Item | Detalle |
|------|---------|
| Estado de Mercado | No comercializado en el mercado regulatorio consultado |
| Autorizaciones Vigentes | 0 |
| Formas Farmacéuticas Disponibles | Ninguna registrada |

> **Contexto internacional:** Benznidazol se comercializa en Argentina (laboratorio ELEA, bajo el nombre Abarax®), Brasil y otros países de Latinoamérica. Fue aprobado por la FDA de EE.UU. en 2017 para el tratamiento de la enfermedad de Chagas en pacientes pediátricos de 2 a 12 años.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en las bases regulatorias consultadas.

> Consultar el prospecto para información de seguridad. La información internacional de referencia indica que los efectos adversos más frecuentes de benznidazol incluyen:
> - Reacciones dermatológicas (dermatitis alérgica, rash)
> - Neuropatía periférica (dosis-dependiente)
> - Trastornos gastrointestinales (náuseas, vómitos)
> - Depresión de médula ósea (raro, pero grave)
>
> *Esta información es de referencia general y no reemplaza la consulta del prospecto oficial.*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El modelo TxGNN no ha generado predicciones de nuevas indicaciones para benznidazol. Adicionalmente, existen brechas significativas de datos (sin DrugBank ID vinculado, MOA no registrado, sin información regulatoria local) que impiden una evaluación completa. No hay base suficiente para avanzar con una propuesta de reposicionamiento en este momento.

**Para avanzar se necesita:**
- Completar la vinculación con DrugBank (ID y datos farmacológicos completos)
- Obtener datos detallados del mecanismo de acción (MOA) desde fuentes primarias
- Verificar si benznidazol está representado en el grafo de conocimiento de TxGNN; si no lo está, considerar su incorporación al KG
- Obtener información de seguridad regulatoria (prospecto/ficha técnica)
- Re-ejecutar la predicción TxGNN una vez que el fármaco esté adecuadamente representado en el modelo
- Evaluar si las bases de datos regulatorias consultadas son las apropiadas para este fármaco (considerar consultar ANMAT, ANVISA u OMS directamente)

---

*⚠️ Aviso: Este informe es únicamente para fines de investigación y no constituye consejo médico. Cualquier candidato a reposicionamiento requiere validación clínica rigurosa antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

