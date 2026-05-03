---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Imiquimod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

El skill `txgnn-pipeline` cubre gestión del pipeline técnico; la generación del informe sigue las instrucciones del sistema. Procedo directamente.

---

# Imiquimod: De Queratosis Actínica a Neoplasia Premaligna

## Resumen en Una Frase

Imiquimod (Aldara®) es un agonista del receptor Toll-like 7 (TLR7) aprobado mundialmente para el tratamiento de la queratosis actínica, el carcinoma basocelular superficial y las verrugas genitales externas; sin embargo, actualmente no se encuentra comercializado en Argentina.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia Premaligna** —incluyendo la neoplasia intraepitelial cervical (CIN), vulvar (VIN) y anal (AIN)—, con **19 ensayos clínicos** y **9 publicaciones** que actualmente respaldan esta dirección.
La base de evidencia incluye dos revisiones Cochrane independientes y ensayos de Fase 2 y 3, lo que posiciona este candidato en un nivel de evidencia L2.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Queratosis actínica, carcinoma basocelular superficial, verrugas genitales externas (aprobación global; sin registro en Argentina) |
| Nueva Indicación Predicha | Neoplasia Premaligna (CIN, VIN, AIN, queilitis actínica) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Argentina | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia analizado. Sin embargo, a partir de la información contenida en los ensayos clínicos y la literatura recuperados, imiquimod es un **agonista del receptor Toll-like 7 (TLR7)**, un receptor de reconocimiento de patrones de la inmunidad innata. Al activar TLR7, imiquimod desencadena la producción de interferón alfa (IFN-α) y otras citocinas proinflamatorias, reforzando la vigilancia inmunológica local frente a células displásicas e induciendo señales proapoptóticas en epitelios alterados. Este mecanismo es la base de su aprobación global para la queratosis actínica —una lesión premaligna por excelencia— y el carcinoma basocelular superficial.

La queratosis actínica (indicación original) y las neoplasias premalignas intraepiteliales como CIN, VIN y AIN comparten un sustrato biológico común: son lesiones displásicas de epitelios estratificados con potencial de progresión maligna, frecuentemente asociadas a infección por VPH de alto riesgo o a daño actínico crónico. El denominador fisiopatológico es la evasión de la vigilancia inmune local en epitelios accesibles, exactamente el punto de acción del TLR7. La extensión de la indicación no es, por tanto, un salto mecanístico, sino una ampliación anatómica y etiológica de la misma vía de señalización.

El respaldo es sólido: dos revisiones Cochrane independientes —PMID 21491403 (VIN de alto grado) y PMID 23235673 (AIN asociada a VPH)— documentan eficacia clínicamente relevante. El ensayo de Fase 3 NCT02329171 (CIN 2-3) fue diseñado directamente para esta expansión de indicación, aunque se terminó por dificultades de reclutamiento, lo que no invalida la racionalidad mecanística. El **guard point** crítico es la accesibilidad anatómica: imiquimod sólo es aplicable de forma efectiva en lesiones superficiales accesibles a formulación tópica; las lesiones profundas o endoluminales requieren formulaciones especiales (nanoencapsulación, instilación intravesical como TMX-101).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Fase 3 | Completado | 259 | Imiquimod como tratamiento neoadyuvante para reducir el tamaño de escisión en lentigo maligno facial (melanosis de Dubreuilh); directamente relevante para enfermedad intraepidérmica premaligna de gran tamaño |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Fase 2 | Completado | 90 | ECA aleatorizado que evalúa la eficacia del tratamiento tópico con imiquimod en lesiones intraepiteliales cervicales de alto grado (CIN); publicado con resultados positivos |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | ECA multicéntrico de imiquimod tópico en CIN 2-3 como alternativa no invasiva a LLETZ; terminado por dificultades de reclutamiento (n=9), pero diseño Fase 3 directamente relevante |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Fase 4 | Desconocido | 20 | Imiquimod 3.75% crema post-criocirugía en queratosis actínicas hipertróficas en dorso de manos y antebrazos; aplicación directa sobre lesión premaligna en contexto de uso aprobado |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Imiquimod 5% crema 3 días/semana en 1-2 ciclos para queratosis actínicas de cabeza; evaluación de duración del efecto tras tratamiento en lesión premaligna |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Fase 1 | Terminado | 49 | Comparación de imiquimod 5% vs. 0.05% vs. nanoencapsulado en queilitis actínica (lesión premaligna del labio inferior); terminado prematuramente pero único ensayo en esta localización |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Fase 1 Temprana | Completado | 16 | Imiquimod como agonista TLR7 en inmunoterapia neoadyuvante para carcinoma escamoso oral temprano (Estadio I-II); demuestra el mecanismo TLR7 en epitelio mucoso y viabilidad como terapia neoadyuvante |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Fase 3 | Desconocido | 145 | ECA de no inferioridad: escisión quirúrgica vs. curetaje + imiquimod en carcinoma basocelular nodular; mayor ensayo disponible de imiquimod en lesión cutánea maligna |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Fase 2 | Completado | 5 | Análisis exploratorio de mecanismos de escape inmune en VIN 2/3 y verrugas anogenitales; evaluación de eficacia y mecanismos de imiquimod como agonista TLR7 en neoplasia intraepitelial vulvar |
| [NCT00142454](https://clinicaltrials.gov/study/NCT00142454) | Fase 1 | Completado | 9 | Vacunación con proteína NY-ESO-1 con imiquimod como adyuvante en melanoma maligno resecado (Estadios IIB-III); evaluación de seguridad e inmunogenicidad de imiquimod como adyuvante sistémico |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane RS | Cochrane Database Syst Rev | Revisión sistemática sobre intervenciones para neoplasia intraepitelial anal (AIN); documenta imiquimod como opción activa para lesión premaligna anogenital asociada a VPH en HSH con VIH |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane RS | Cochrane Database Syst Rev | Intervenciones médicas para VIN de alto grado; Cochrane respalda imiquimod como alternativa no quirúrgica válida con eficacia documentada en neoplasia intraepitelial vulvar |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Tratamientos combinados con terapia fotodinámica para cáncer de piel no melanoma (NMSC); imiquimod evaluado en combinación con PDT para lesiones premalignas y BCC superficial |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión Clínica | Skin Therapy Letter | Manejo actual de queratosis actínicas; imiquimod identificado como terapia tópica de campo de primera línea para cancerización en campo (field cancerization) |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión Clínica | Semin Cutan Med Surg | Estrategias de tratamiento tópico para NMSC y lesiones precursoras; imiquimod comparado con 5-FU y diclofenac para manejo no quirúrgico de lesiones premalignas |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Estudio PK-PD | Urologic Oncology | Farmacocinética y farmacodinamia de agonistas TLR7 (TMX-101 y TMX-202) en modelo de rata; extensión del mecanismo TLR7 hacia instilación intravesical para cáncer de vejiga no músculo-invasivo |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Caso Clínico | Int J STD AIDS | Tratamiento exitoso de VIN de alto grado con imiquimod 5% en receptora de trasplante renal; demuestra eficacia incluso en pacientes inmunosuprimidas de alto riesgo |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Caso Clínico | Int J STD AIDS | Resolución completa de papulosis bowenoide (condición premaligna anogenital HPV-dependiente) con imiquimod crema 5% tópica una vez a la semana; tratamiento bien tolerado |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Caso Clínico | Der Hautarzt | Poroqueratosis actínica superficial diseminada con múltiples lesiones (pre)malignas cutáneas resistentes a tratamientos tópicos incluyendo imiquimod; caso relevante para evaluar límites del mecanismo |

---

## Información de Mercado en Argentina

Imiquimod **no se encuentra comercializado en Argentina**. La consulta regulatoria no registró ninguna autorización de comercialización (0 registros). Para uso clínico en Argentina, se requeriría importación bajo régimen de medicamentos especiales (art. 14 Ley 16.463) o autorización de uso compasivo ante ANMAT. A modo de referencia, el producto está aprobado en EE.UU. (FDA), Unión Europea (EMA) y múltiples otros mercados bajo el nombre comercial Aldara® (3M/Meda), con formulaciones en crema al 3.75% y 5%.

---

## Citotoxicidad

Imiquimod no es un fármaco citotóxico convencional. Está aprobado por la FDA para el tratamiento del carcinoma basocelular superficial (una neoplasia maligna cutánea), por lo que posee propiedades antineoplásicas; sin embargo, su mecanismo es inmunomodulador y no implica citotoxicidad directa sobre el ADN ni supresión medular.

| Item | Contenido |
|------|------|
| Clasificación | Inmunomodulador tópico / Agonista TLR7 (antineoplásico de mecanismo inmune; no citotóxico convencional) |
| Riesgo de Mielosupresión | Bajo (uso tópico con absorción sistémica mínima; no se han reportado citopenias en uso estándar) |
| Clasificación de Emetogenicidad | No aplica para formulación tópica |
| Ítems de Monitoreo | Reacciones cutáneas locales (eritema, vesiculación, erosión, costra); síntomas seudogripales (fiebre, mialgias, fatiga) ante absorción sistémica elevada por área extensa o piel erosionada |
| Protección en Manejo | No requiere medidas especiales de manejo de citotóxicos; precauciones estándar para cremas medicinales; evitar contacto con mucosas y ojos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias clave y contraindicaciones no están disponibles en esta evaluación; se recomienda revisar el prospecto aprobado por FDA/EMA (Aldara®) para obtener información completa antes de cualquier uso clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La activación de TLR7 por imiquimod tiene una base mecanística sólida y directamente translacional para neoplasias premalignas epiteliales superficiales, respaldada por dos revisiones Cochrane independientes (VIN y AIN), un ensayo de Fase 3 completado en lentigo maligno (n=259), y un ensayo de Fase 2 completado en CIN de alto grado (n=90); el nivel de evidencia L2 justifica avanzar con precauciones específicas de selección de pacientes, localización anatómica y formulación.

**Para avanzar se necesita:**
- Obtener datos completos de mecanismo de acción (MOA) y categorías de DrugBank para completar el análisis de relación mecanística
- Revisar advertencias, contraindicaciones y perfil de seguridad del prospecto aprobado por FDA/EMA
- Gestionar autorización de importación o uso compasivo ante ANMAT, dado que el producto no está comercializado en Argentina
- Definir subpoblación objetivo prioritaria: lesiones superficiales accesibles tópicamente (CIN exocervical, VIN, AIN, queilitis actínica, AK de campo)
- Evaluar formulaciones especiales (nanoencapsulado, instilación intravesical) para indicaciones donde la penetración tisular convencional es insuficiente
- Diseñar protocolo de monitoreo de reacciones locales y síntomas sistémicos para las poblaciones de mayor riesgo (inmunosuprimidos, áreas de gran extensión)
- Considerar el hallazgo de seguridad de PMID 12719972 (conversión maligna en papilomatosis oral bajo imiquimod) al definir los criterios de exclusión para estudios de expansión en mucosa oral
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

