---
layout: default
title: Salbutamol
parent: Solo Predicción del Modelo (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Salbutamol: nueva indicación predicha, Conjuntivitis papilar (nivel de evidencia L5). Indicación original: Asma y enfermedad bronquial (según el grafo de conocimiento de TxGNN"
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture", "obstructive lung disease"]
---

# Salbutamol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Salbutamol: De Asma a Conjuntivitis Papilar

## Resumen en Una Frase

Salbutamol es un agonista beta-2 adrenérgico, utilizado originalmente para el tratamiento del asma y de la enfermedad bronquial.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**,
pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma y enfermedad bronquial (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, salbutamol es un agonista beta-2 adrenérgico de acción corta. Su eficacia en asma y en obstrucción reversible de las vías aéreas está comprobada, y mecanísticamente podría ser aplicable a procesos inflamatorios de la conjuntiva.

La relación entre la indicación original y la nueva es indirecta. En modelos preclínicos, los agonistas beta-2 muestran cierto efecto antiinflamatorio y de estabilización de mastocitos en la conjuntiva. Esto podría ser relevante para una conjuntivitis de componente alérgico o inflamatorio. Sin embargo, **no existe evidencia directa en conjuntivitis papilar**, y la relación de similitud con la indicación original aún no ha sido evaluada.

Por lo tanto, la predicción es mecanísticamente plausible pero especulativa. Se apoya únicamente en el puntaje alto del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Argentina

Hay 20 autorizaciones vigentes, todas de producto único (sin combinaciones) y ninguna cancelada. Se muestran las 5 principales. Los textos de indicación aprobada no figuran en los datos disponibles.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 13001 | VENTOLIN HFA | Aerosol inhalador con aplicador x 200 dosis | GlaxoSmithKline |
| 3909 | VENTOLIN | Solución para nebulizar x 20 ml | GlaxoSmithKline |
| 19840 | SALBUTAMOL FABRA | Gotas 0.5% x 20 ml | Fabra |
| 14931 | SALBUTAMOL DENVER FARMA | Solución para nebulizar x 20 ml | Denver Farma |
| 45295 | SALBUDEN | Inhalador HFA x 250 dosis | Denver Farma |

## Consideraciones de Seguridad

- **Contraindicaciones / precauciones según el grafo de conocimiento** (no provienen del texto del prospecto): hipertensión arterial, hipertensión ocular, síndrome de QT largo (incluida la forma familiar), paro cardíaco súbito, enfermedad de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria, epilepsia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, acidosis metabólica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hiperplasia prostática benigna, obstrucción del cuello vesical y glaucoma de ángulo cerrado.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales, de nivel moderado:
  - Antidiabéticos: acarbosa, acetohexamida, albiglutida, alogliptina, canagliflozina, clorpropamida y dapagliflozina.
  - Simpaticomiméticos: epinefrina, isometepteno y dietilpropión.
  - Otros: famotidina, cisaprida y claritromicina.
  - Laxantes: bisacodilo y aceite de ricino.
  - De nivel menor: corticoides como hidrocortisona, beclometasona, betametasona, budesonida y dexametasona.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por ANMAT. Esa información no estaba disponible en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no existen ensayos clínicos ni literatura que la respalden (nivel L5). El mecanismo propuesto solo cuenta con respaldo preclínico indirecto. Con los datos actuales no se justifica avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción, por ejemplo desde DrugBank.
- Revisión sistemática de la literatura específica sobre salbutamol y conjuntivitis papilar.
- Estudios preclínicos o clínicos que evalúen una formulación oftálmica. Las presentaciones autorizadas en Argentina son inhaladas, nebulizadas u orales, y la compatibilidad de vía de administración aún no está evaluada.
- Revisión del prospecto de ANMAT para completar la información de seguridad, dado el perfil cardiovascular y metabólico indicado arriba.

**Nota de contexto:** otras indicaciones predichas para este fármaco cuentan con más respaldo. La enfermedad pulmonar obstructiva (L1) coincide en gran parte con el uso ya aprobado, por lo que no es un reposicionamiento genuino. La anafilaxia (L2) tiene un ensayo de Fase 3 terminado prematuramente. La conjuntivitis atópica (L4) tiene estudios preclínicos en conjuntiva que podrían servir de referencia indirecta para la conjuntivitis papilar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

