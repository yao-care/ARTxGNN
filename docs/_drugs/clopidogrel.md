---
layout: default
title: Clopidogrel
parent: Evidencia Alta (L1-L2)
nav_order: 117
evidence_level: L2
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

# Clopidogrel: De Síndrome Coronario Agudo a Trastorno de Migraña

## Resumen en Una Frase

Clopidogrel es un antiagregante plaquetario (inhibidor del receptor P2Y12), originalmente utilizado en el síndrome coronario agudo, la embolia intracraneal y el infarto de miocardio con elevación del ST.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **6 ensayos clínicos** y **22 publicaciones** que respaldan esta dirección, incluyendo ensayos aleatorizados publicados. El beneficio parece limitarse a la migraña asociada a foramen oval permeable (FOP) o a cortocircuitos derecha-izquierda.

> Nota: la predicción con mayor puntaje es "migraña con aura de tronco encefálico" (99.44%). Sin embargo, esta evaluación se centra en "trastorno de migraña" (99.44%), que tiene una evidencia mucho más sólida (nivel L2). La evidencia para el subtipo con aura de tronco encefálico se trata de forma específica en la sección de mecanismo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo, embolia intracraneal e infarto de miocardio con elevación del ST (según el grafo de conocimiento; los textos de indicación de ANMAT no están disponibles) |
| Nueva Indicación Predicha | Trastorno de migraña (migraña con aura de tronco encefálico en primer lugar del ranking, con evidencia más débil) |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, clopidogrel es un antagonista del receptor plaquetario P2Y12 que reduce la activación y agregación plaquetaria. Su eficacia en la prevención de eventos trombóticos (síndrome coronario agudo, infarto, embolia cerebral) está bien establecida.

La hipótesis mecanística propuesta para la migraña, en particular con aura, es la del FOP o cortocircuito derecha-izquierda: microémbolos o sustancias vasoactivas (por ejemplo, serotonina liberada por las plaquetas) evitan el filtro pulmonar y podrían desencadenar la depresión cortical propagada. Al reducir la activación plaquetaria, clopidogrel podría disminuir estos desencadenantes. También hay datos preclínicos que implican a los receptores P2Y12 en modelos animales de migraña (nitroglicerina y migraña crónica).

Es importante matizar: la evidencia es específica de la migraña con aura en pacientes con FOP o cortocircuito, y no es específica del subtipo con aura de tronco encefálico. El respaldo para ese subtipo se limita a un ECA piloto pequeño, datos retrospectivos y abiertos, y reportes de caso. Los resultados globales son mixtos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Fase 2 | Completado | 1000 | Estudio COMPETE: compara anticoagulación vs antiplaquetarios vs tratamiento antimigrañoso en migraña con FOP. Resultados publicados (PMID 42526943) |
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Fase 4 | Completado | 220 | Estudio CANOA: clopidogrel sumado a aspirina para prevenir migraña de nueva aparición tras cierre transcatéter de comunicación interauricular |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Fase 4 | Desconocido | 50 | Eficacia profiláctica de clopidogrel en migraña con cortocircuito derecha-izquierda; estudio pequeño y de estado desconocido |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | CLOSE: cierre de FOP vs anticoagulantes vs antiplaquetarios para prevenir recurrencia de ictus. La migraña no es el objetivo principal (evidencia indirecta) |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Fase 3 | Activo, sin reclutamiento | 440 | SPRING: cierre de FOP vs tratamiento médico en migraña. Intervención con dispositivo (evidencia indirecta) |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | No aplica | Terminado | 7 | Estudio con dispositivo Gore Cardioform; terminado con 7 participantes, no informativo para clopidogrel |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | ECA multicéntrico | BMJ | Eficacia y seguridad del tratamiento antitrombótico para prevenir migraña en pacientes con FOP (ensayo abierto con control activo) |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | ECA | JAMA | CANOA: clopidogrel más aspirina vs aspirina sola para migraña tras cierre de comunicación interauricular |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | ECA (seguimiento a 1 año) | JAMA Cardiology | Resultados a 1 año de CANOA, tras suspender clopidogrel a los 3 meses |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | ECA piloto | Cephalalgia | Estudio piloto aleatorizado de clopidogrel como profilaxis de migraña |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisión sistemática | Headache | Papel de los fármacos antitrombóticos en la prevención de la migraña |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Revisión sistemática | Indian J Thorac Cardiovasc Surg | Incidencia y manejo de la cefalea de nueva aparición tras cierre transcatéter de comunicación interauricular |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohorte | J Investig Med | Clopidogrel como profilaxis complementaria en migraña refractaria con FOP |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohorte | Heart | Clopidogrel reduce la migraña con aura tras el cierre de FOP y defectos septales auriculares |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Revisión retrospectiva | Neurology | Tienopiridinas en pacientes con migraña y FOP |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Estudio piloto abierto | Neurology | TRACTOR: ticagrelor (inhibidor P2Y12 relacionado) en migraña refractaria con FOP |

## Información de Mercado en Argentina

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 22962 | PLAVIX (Sanofi-Aventis) | 75 mg comprimidos recubiertos x 28 | No disponible en los datos |
| 44514 | PLAVIX (Sanofi-Aventis) | 300 mg comprimidos recubiertos x 4 | No disponible en los datos |
| 47456 | CLOPILEP (Lepetit) | 75 mg comprimidos recubiertos x 30 | No disponible en los datos |
| 47399 | NADENEL (Gémines Farmacéutica) | 75 mg comprimidos recubiertos x 30 | No disponible en los datos |
| 46131 | CLODREL (Baliarda) | 75 mg comprimidos recubiertos x 30 | No disponible en los datos |

Hay 20 autorizaciones vigentes en total, todas de monofármaco, sin autorizaciones canceladas.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: insuficiencia hepática aguda, hepatitis, trastornos de la coagulación, lesiones/traumatismos, púrpura trombocitopénica, úlcera péptica activa y hemorragia intracraneal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las más relevantes:
  - **Mayores**: rabeprazol, omeprazol, esomeprazol, pioglitazona, loperamida y repaglinida.
  - **Moderadas**: ácido acetilsalicílico, bupropión, morfina, cimetidina, claritromicina, lansoprazol y pantoprazol, entre otros.
  - Los inhibidores de la bomba de protones (especialmente omeprazol y esomeprazol) son especialmente relevantes por su efecto sobre la activación de clopidogrel vía CYP2C19.
- **Señales en la literatura**: reportes de artritis inflamatoria asociada a clopidogrel y riesgo de sangrado combinado con otros antitrombóticos.

Las advertencias del prospecto de ANMAT no estaban disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen ECA completados (CANOA y COMPETE, este último publicado en 2026) y un ECA piloto que respaldan el uso de antiplaquetarios en migraña asociada a FOP o cortocircuito. Sin embargo, los resultados son mixtos, el beneficio se limita a ese subgrupo y no hay ECA de Fase 3 que confirmen la indicación general.

**Otras predicciones del modelo (todas en Hold):** osteoartritis (L4, sin vínculo mecanístico y con señal desfavorable frente a ticagrelor), tendinitis, miositis fibrosa y miositis granulomatosa idiopática (L5, solo predicción), artritis reumatoide (L4, con señales de posible daño) y susceptibilidad a osteoartritis (L5).

**Para avanzar se necesita:**
- Revisar en detalle los resultados completos del ensayo COMPETE (PMID 42526943), incluyendo eficacia y sangrado.
- Definir la población objetivo (migraña con aura y FOP o cortocircuito derecha-izquierda confirmado) y excluir el uso generalizado.
- Obtener el prospecto de ANMAT (advertencias, contraindicaciones e indicaciones aprobadas) y los datos del mecanismo de acción.
- Plan de monitoreo de sangrado y de interacciones, en especial con inhibidores de la bomba de protones y AINE.
- Evaluar si un ECA de Fase 3 específico en migraña es necesario antes de una indicación formal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

