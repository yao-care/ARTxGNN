---
layout: default
title: Diphenhydramine
parent: Solo Predicción del Modelo (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Difenhidramina: De Insomnio y Rinitis Alérgica a Conjuntivitis Rosácea

## Resumen en Una Frase

La difenhidramina es un antihistamínico de primera generación, originalmente utilizado en insomnio, rinitis vasomotora, rinitis alérgica y distintas formas de conjuntivitis (atópica, papilar y primaveral).
El modelo TxGNN predice que podría ser efectiva para **conjuntivitis rosácea**, pero **no existen ensayos clínicos ni publicaciones** que respalden actualmente esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insomnio, rinitis vasomotora, rinitis alérgica, conjuntivitis atópica, papilar y primaveral (según el grafo de conocimiento de TxGNN; los textos de indicación aprobada de las autorizaciones locales están vacíos) |
| Nueva Indicación Predicha | Conjuntivitis rosácea |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La difenhidramina es un antagonista (agonista inverso) del receptor de histamina H1 de primera generación. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe; lo descrito aquí se basa en el conocimiento farmacológico general de la clase.

Existe un vínculo plausible: el fármaco ya se emplea en conjuntivitis alérgica, atópica, primaveral y papilar, donde alivia el picor, el enrojecimiento y la irritación ocular mediados por histamina. La predicción del modelo parece apoyarse en esa similitud con otras indicaciones de conjuntivitis.

Sin embargo, el vínculo es solo parcial. La conjuntivitis rosácea (rosácea ocular) se debe principalmente a disfunción de las glándulas de Meibomio, inestabilidad de la película lagrimal, desregulación inmune e inflamatoria innata y participación de Demodex o microorganismos, no a una alergia dominada por histamina. Por ello, el beneficio probablemente se limitaría al alivio sintomático. El puntaje alto (0.992) refleja una predicción del modelo y no constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Argentina

Se muestran 5 de las 11 autorizaciones vigentes (todas de producto único, ninguna cancelada).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49698 | BENADRYL (Elea) | Cápsulas x 30 | No especificada en los datos |
| 41413 | FADALEX (Biosintex Retai) | Jarabe 2.5 mg/ml x 120 ml | No especificada en los datos |
| 20854 | DIFENHIDRAMINA DENVER FARMA | Jarabe x 120 ml | No especificada en los datos |
| 30218 | DIFENHIDRAMINA DENVER FARMA | Comprimidos 50 mg x 20 | No especificada en los datos |
| 23319 | BENADRYL (Elea) | Inyectable x 1 x 5 ml | No especificada en los datos |

Las demás autorizaciones corresponden a presentaciones de BENADRYL (jarabe, antitusivo y DM compuesto), FADALEX, HISTALER y CORIZINA CETUS.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 394 interacciones registradas. Entre las principales:
  - **Mayores**: citrato de potasio, eliglustat.
  - **Moderadas**: anticolinérgicos (hiosciamina, atropina, glicopirronio, diciclomina, clidinio, mepenzolato, metescopolamina), opioides (morfina, loperamida, eluxadolina), bupropión, lorcaserina, dronabinol, nabilona, metoclopramida y fenilbutirato de glicerol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (L5), sin ensayos ni literatura, y el mecanismo de la conjuntivitis rosácea no está dominado por histamina, por lo que el beneficio sería, como máximo, sintomático.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre antihistamínicos en rosácea ocular.
- Datos del mecanismo de acción del fármaco (DrugBank).
- Advertencias y contraindicaciones del prospecto de ANMAT.
- Evaluación de la compatibilidad de vía y formulación (p. ej., presentación oftálmica, no disponible entre las autorizaciones locales).
- Análisis de interacciones relevantes y del perfil anticolinérgico en población con ojo seco, frecuente en rosácea ocular.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

