---
layout: default
title: Salbutamol
parent: Solo Predicción del Modelo (L5)
nav_order: 226
evidence_level: L5
indication_count: 8
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
last_modified_at: 2026-11-03
description: "Salbutamol: nueva indicación predicha, conjuntivitis papilar (papillary conjunctivitis) (nivel de evidencia L5). En Argentina, productos en el listado de PAMI: al menos 20"
---

# Salbutamol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Salbutamol: agonista beta-2 adrenérgico → conjuntivitis papilar (papillary conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Salbutamol es un agonista beta-2 adrenérgico, utilizado como broncodilatador inhalado y comercializado en Argentina en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar (papillary conjunctivitis)**, con un puntaje de 0.9999.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción; se trata de una predicción exclusivamente del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | conjuntivitis papilar (papillary conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | Incluido en el listado de medicamentos de PAMI (al menos 20) – el estado del registro en ANMAT no está incluido en estos datos |
| Número de productos en el listado PAMI | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Salbutamol (traducción no oficial): «El sulfato de salbutamol es un agonista beta 2 -adrenérgico. Los efectos farmacológicos del sulfato de salbutamol se atribuyen a la activación de los receptores beta 2 -adrenérgicos del músculo liso de las vías respiratorias. La activación de los receptores beta 2 -adrenérgicos produce la activación de la adenilciclasa y un aumento de la concentración intracelular de 3',5'-adenosín monofosfato cíclico (AMP cíclico).» Texto original en inglés: "Albuterol sulfate is a beta 2 -adrenergic agonist. The pharmacologic effects of albuterol sulfate are attributable to activation of beta 2 -adrenergic receptors on airway smooth muscle. Activation of beta 2 -adrenergic receptors leads to the activation of adenylcyclase and to an increase in the intracellular concentration of cyclic-3', 5’-adenosine monophosphate (cyclic AMP)." ([DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d), versión del 2024-12-20; consultado el 2026-11-19). Según la información conocida, salbutamol es un agonista del receptor beta-2 adrenérgico, clase que produce relajación del músculo liso bronquial y puede reducir la liberación de mediadores desde los mastocitos.

Mecanísticamente, un efecto beta-2 sobre los mastocitos conjuntivales o sobre la vasculatura ocular es teóricamente plausible, ya que la conjuntivitis papilar tiene un componente alérgico/inflamatorio mediado en parte por mastocitos. Sin embargo, este vínculo es solo una hipótesis: no hay ensayos clínicos ni literatura que evalúen salbutamol en esta enfermedad.

Cabe señalar que el puntaje del modelo es alto, pero por sí solo no constituye evidencia clínica. La similitud con la indicación original no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Salbutamol se encuentra comercializado en Argentina. Hay al menos 20 autorizaciones registradas, todas vigentes y de producto de un solo principio activo; la lista podría ser parcial. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19370 | MICROTEROL | 5mg/ml sol.p/nebul.x20ml | No registrada |
| 50519 | SALBUDEN HFA CON AEROCAMARA DF 280 | inh.HFA+aeroc.x 250ds. | No registrada |
| 19840 | SALBUTAMOL FABRA | 0.5% gts.x 20 ml | No registrada |
| 13001 | VENTOLIN HFA | aer.inh.c/aplic.x200ds. | No registrada |
| 47141 | SALBUTRAL C/AEROMED | aer.hfa x 250 dosis | No registrada |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución registradas en los datos de relaciones fármaco-enfermedad (no provienen del texto del prospecto)**: hipertensión, síndrome de QT largo, epilepsia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperplasia prostática benigna, hipertensión ocular, acidosis metabólica, paro cardíaco súbito, enfermedad de conducción cardíaca, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción del cuello vesical, isquemia miocárdica y enfermedad arterial coronaria.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; entre las primeras listadas:
  - Moderadas: acarbosa, isometepteno, famotidina, epinefrina, albiglutida, acetohexamida, alogliptina, bisacodilo, canagliflozina, aceite de ricino, clorpropamida, cisaprida, claritromicina, dapagliflozina, dietilpropión.
  - Leves: hidrocortisona, dipropionato de beclometasona, betametasona, budesonida, dexametasona.
- Un hallazgo relevante para una eventual vía ocular: el glaucoma de ángulo cerrado y la hipertensión ocular figuran entre las condiciones de precaución, lo que exigiría evaluación específica de seguridad ocular.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (0.9999), sin ensayos clínicos ni literatura que estudien salbutamol en conjuntivitis papilar. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados
- Estudios preclínicos (p. ej., modelos de conjuntivitis alérgica) que evalúen la acción beta-2 sobre mastocitos conjuntivales
- Evaluación de viabilidad de una vía de administración oftálmica, ya que las presentaciones disponibles en Argentina son inhaladas, nebulizadas o en gotas orales/de inhalación
- Revisión de advertencias y contraindicaciones del prospecto de ANMAT
- Evaluación específica de seguridad ocular (glaucoma de ángulo cerrado, hipertensión ocular)

<!-- review:begin log -->

## Registro de verificación

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de verificación | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

