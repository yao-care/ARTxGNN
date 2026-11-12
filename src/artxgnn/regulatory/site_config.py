"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（西班牙文）；依據是 PAMI 給付清單（medicamentos para entidades）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "ARTxGNN",
 "ID_PREFIX": "ar",
 "SNAPSHOT": "ar_licenses.json.gz",
 "HEADER_LABEL": "Nivel de evidencia",
 "OVERVIEW_LABELS": [
  "Nivel de Evidencia",
  "Nivel de evidencia"
 ],
 "WITHDRAWN_RE": "Retirad[oa]",
 "DESC_LEVEL_RE": "nivel de evidencia (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "nivel de evidencia {lv}",
 "NA_DESC": "solo usos conocidos",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的 173 頁，頁首全部等於第一個等級（整格取最高會有 2 頁不同）",
 "MARKET_RE": "[Mm]ercado",
 "ID_RE": "\\b\\d{4,6}\\b",
 "PROSE_ID_RE": null,
 "ORIGINAL_LABELS": [
  "Indicación Original",
  "Indicacion Original",
  "Indicación original"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(no consta|no disponible|ninguna|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\by\\b|\\bo\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 PAMI 給付清單（只涵蓋 PAMI 有給付的藥，不是 ANMAT 全量）；可比對頁數以程式輸出為準",
 "COMMITS": [
  "be3fcd07",
  "101ac6e8"
 ],
 "REGEN_COMMITS": [
  "7b9250d7",
  "c3de0a1e",
  "db2235d8",
  "4d09f026",
  "8d09c6b8"
 ],
 "SOURCES": [
  {
   "title": "PAMI – Medicamentos para entidades (datos abiertos)",
   "url": "https://datos.pami.org.ar/api/3/action/package_show?id=medicamentos-para-entidades"
  }
 ],
 "PROGRAM_LINE_RE": null,
 "CLASSIFY": [
  [
   "tw",
   "Taiw[aá]n|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "monodroga|monofármaco|en combinaci[oó]n|un solo principio activo|asociaci[oó]n"
  ],
  [
   "cancel",
   "cancelad|revocad|dad[oa]s? de baja|anulad|vencid|sin (?:registro|autorizaci[oó]n|licencia)s? (?:vigente|v[aá]lid)|no (?:está |figura |consta )?(?:comercializ|vigente|registrad|incluid|en el listado)|no hay (?:registro|licencia|autorizaci)|no se (?:encontraron|identificaron|registraron) (?:ninguna |ningún )?(?:autorizaci|registro|licencia)|no cuenta con (?:ninguna |ningún )?(?:autorizaci|registro|licencia)|ausencia de (?:autorizaci|registro)|0 licencias"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:autorizaci|registro|licencia|producto|presentaci)|(?:autorizaci|registro|licencia|presentaci)[^.;]{0,30}\\b\\d+\\b|\\b(?:todos|todas|ambos)\\b[^.;]{0,30}(?:registro|licencia|vigente|v[aá]lid)|\\bvigentes?\\b"
  ],
  [
   "product",
   "\\b(?:como|en forma de|forma farmac|comprimid|c[aá]psul|inyectabl|pomada|comercializ)"
  ]
 ],
 "T": {
  "label": {
   "correct": "Corrección de verificación",
   "annotate": "Nota de verificación",
   "rereview": "Revisión pendiente",
   "rereview_result": "Resultado de la revisión"
  },
  "action": {
   "correct": "Corregido",
   "annotate": "Nota añadida",
   "rereview": "Marcado para revisión",
   "section": "Sección con fuentes añadida",
   "rereview_result": "Revisión completada",
   "header_level": "Nivel de evidencia del encabezado recalculado desde el resumen rápido",
   "description_level": "Nivel de evidencia de la descripción alineado con el encabezado"
  },
  "verdict": {
   "maintain": "Mantenido",
   "downgrade": "Rebajado",
   "upgrade": "Elevado",
   "withdraw": "Retirado"
  },
  "log_head": "## Registro de verificación",
  "disclaimer_re": "Descargo de responsabilidad",
  "log_cols": [
   "Fecha de verificación",
   "Elemento",
   "Acción",
   "Fuente"
  ],
  "level_same": "nivel de evidencia {o} sin cambios",
  "level_change": "nivel de evidencia {o} → {n}",
  "orig": "Texto original: «{x}»",
  "table_updated": "Los elementos «{labels}» de esta página se actualizaron según el resultado de la revisión; los valores originales figuran en el registro de abajo.",
  "decision": "Recomendación de decisión: {x}",
  "source": "Fuente",
  "rereviewed": "Marcado para revisión → revisado (ver el resultado de la revisión)",
  "hdr": "Nivel de evidencia del encabezado recalculado desde el resumen rápido ({o} → {n})",
  "hdr_withdraw": "Predicción principal retirada en la revisión; nivel de evidencia del encabezado recalculado ({o} → {n})",
  "now_listed": ", ahora listado en «{x}»",
  "rr": "Revisión: {v}, {c}",
  "tu": "; {l}: «{a}» → «{b}»",
  "desc": "Descripción de la página: «{a}» cambiado a «{b}» (sigue al encabezado; resto del texto sin cambios, original conservado en el registro)",
  "revised": " (revisado el {d}; versión anterior conservada en el registro)",
  "superseded": "Reemplazado por la tabla generada por programa (antes: {a})",
  "regen": "Ya no aparece tras regenerar el informe ({d}: {n}; antes: {a})",
  "program": "Ya no aparece tras una corrección del programa ({d}: {n}; antes: {a})",
  "withdrawn": "Verificación retirada ({d}: {n}; antes: {a})",
  "intro": "A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.",
  "intro_header": "A continuación, el registro de verificación de esta página; el nivel de evidencia del encabezado sigue al resumen rápido. Las predicciones del modelo, la tabla resumen y las conclusiones no se reescribieron.",
  "intro_rr": "A continuación, el registro de verificación de esta página: afirmaciones contrastadas con los datos oficiales (listado de medicamentos de PAMI). Las correcciones se limitan a datos básicos y el texto de la predicción no se reescribió; los niveles de evidencia y las decisiones solo cambiaron por un resultado de revisión (rebaja, elevación o retiro), con los valores originales abajo.",
  "figures": "En los datos (listado de medicamentos de PAMI) figuran {total} registros para este medicamento, {valid} vigentes; las cifras actualizadas están en el resumen rápido y en la información de mercado.",
  "data_as_of": "listado de medicamentos de PAMI, al {date}",
  "notes": {
   "rewrite": "Corregido: la afirmación no coincidía con los datos oficiales ({d}) y se reemplazó por el texto actual.",
   "tw": "Eliminado: texto residual de la plantilla taiwanesa (TFDA), que no corresponde a esta página.",
   "combo": "Eliminado: la indicación de productos monodroga o en combinación no coincidía con los datos oficiales ({d}).",
   "cancel": "Eliminado: la afirmación de que el medicamento no figura o de que sus registros están dados de baja no coincidía con los datos oficiales ({d}).",
   "count": "Eliminado: el número o el estado de los registros indicado no coincidía con los datos oficiales ({d}).",
   "product": "Eliminado: la descripción de los productos no coincidía con los datos oficiales ({d}).",
   "generic": "Eliminado: la afirmación contradecía los datos oficiales ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Eliminado: «{x}»",
  "regen_note": "el informe se regeneró en noviembre de 2026 y ya no contiene esta afirmación"
 }
}""")
