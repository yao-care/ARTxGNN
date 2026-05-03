---
layout: default
title: Acitretina
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 0
---

# Acitretina
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

# Acitretina: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Acitretina (acitretin) es un retinoide sistémico de segunda generación, utilizado ampliamente para el tratamiento de psoriasis severa y otros trastornos graves de la queratinización.
El modelo TxGNN **no ha generado predicciones de nuevas indicaciones** para este fármaco en el presente ciclo de análisis,
y los datos regulatorios y de seguridad presentan **brechas significativas** que impiden una evaluación completa.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Psoriasis severa y trastornos de la queratinización (según literatura de referencia; sin registro local) |
| Nueva Indicación Predicha | — No disponible (sin predicciones TxGNN) |
| Puntaje de Predicción TxGNN | — No disponible |
| Nivel de Evidencia | L5 — Solo datos preliminares, sin predicción ni estudios asociados |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué no hay Predicciones Disponibles?

Acitretina es el metabolito activo de etretinato y pertenece a la familia de los retinoides. Su mecanismo de acción se basa en la modulación de la diferenciación y proliferación celular epidérmica mediante la unión a receptores nucleares de ácido retinoico (RAR), regulando la expresión génica asociada a la queratinización. Se utiliza internacionalmente para psoriasis severa (eritrodérmica, pustular), ictiosis, liquen plano, enfermedad de Darier y otros trastornos de la queratinización refractarios.

Sin embargo, en el presente ciclo de análisis del modelo TxGNN, **no se generaron predicciones de nuevas indicaciones** para acitretina. Esto puede deberse a varias razones:

1. **Ausencia en el grafo de conocimiento (KG):** Es posible que acitretina no esté representada adecuadamente en el grafo de conocimiento utilizado por TxGNN, o que su identificador DrugBank no haya sido mapeado correctamente (el campo `drugbank_id` figura como `null`).
2. **Falta de datos regulatorios locales:** El fármaco no está registrado ni comercializado en Argentina (0 autorizaciones ANMAT), lo que limita la integración de datos regulatorios locales en el pipeline de análisis.
3. **Datos del mecanismo de acción no disponibles en el pack:** El campo `original_moa` figura como brecha de datos, lo cual impacta la capacidad de correlación mecanística del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con nuevas indicaciones predichas, dado que no se generaron predicciones TxGNN para este fármaco.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con nuevas indicaciones predichas disponible en este Evidence Pack.

---

## Información de Mercado en Argentina

Acitretina **no se encuentra comercializada en Argentina**. No existen autorizaciones de ANMAT registradas para este principio activo.

> **Nota:** Acitretina se comercializa internacionalmente bajo marcas como Neotigason® y Soriatane®, y cuenta con aprobación en la Unión Europea, Estados Unidos y otros mercados para el tratamiento de psoriasis severa.

---

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad.

**Nota importante sobre retinoides:** Aunque los datos de seguridad específicos no están disponibles en este Evidence Pack, acitretina pertenece a la clase de los retinoides sistémicos, los cuales presentan un perfil de seguridad bien documentado que incluye:

- **Teratogenicidad:** Acitretina es altamente teratogénica. Está absolutamente contraindicada en el embarazo y requiere anticoncepción estricta durante el tratamiento y hasta 3 años después de su discontinuación.
- **Hepatotoxicidad:** Se requiere monitoreo periódico de función hepática.
- **Dislipidemia:** Puede elevar triglicéridos y colesterol; monitoreo lipídico recomendado.
- **Sequedad mucocutánea:** Efecto adverso frecuente (labios, piel, ojos).

*Estos datos provienen de la literatura de referencia general para retinoides y no del Evidence Pack proporcionado.*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen predicciones TxGNN de nuevas indicaciones para acitretina en el presente ciclo de análisis. Además, el fármaco no está comercializado en Argentina, carece de identificador DrugBank mapeado, y presenta brechas críticas en los datos de mecanismo de acción y seguridad regulatoria local. No es posible avanzar con una evaluación de reposicionamiento sin resolver estas deficiencias.

**Para avanzar se necesita:**
- Resolver el mapeo del identificador DrugBank (`drugbank_id` actualmente `null`) para permitir la integración en el grafo de conocimiento de TxGNN
- Obtener datos detallados del mecanismo de acción (MOA) desde DrugBank u otra fuente curada
- Evaluar la viabilidad regulatoria de registro en Argentina (consulta con ANMAT o búsqueda de antecedentes de importación)
- Re-ejecutar el modelo TxGNN una vez que el fármaco esté correctamente representado en el grafo de conocimiento
- Obtener información de seguridad del prospecto oficial (advertencias, contraindicaciones, interacciones farmacológicas)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

