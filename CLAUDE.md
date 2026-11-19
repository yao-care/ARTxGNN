# ARTxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用西班牙文，依據是 PAMI 給付清單（medicamentos para entidades）；在地字樣集中在 `src/artxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/artxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/artxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/ar_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/artxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 23 筆紀錄（14 頁；
其中 0 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。


## 新資料查不到的許可證（2026-11-17）

11-16 每週排程「新資料查不到」53 張（證據包 3,917 個代碼的 1.4%，沒開 issue）。本站的號碼是 PAMI 價目表的 ALFABETA 代碼（Alfabeta／Manual Farmacéutico 的品項碼，不是 ANMAT certificado），
PAMI「medicamentos para entidades」只列當期給付的品項——代碼消失＝「ya no figura en el listado de PAMI」，不等於 ANMAT 註冊失效（ANMAT 註冊狀態不在這份資料裡，也沒有可下載的全量註冊檔；servicios.anmat.gob.ar 從雲端連不到）。
2026-11-17 用戶要求確認實際狀態：53 張全部在 2026-03-01 版價目表（`data/raw/ar_fda_drugs.json`，PVP PAMI AL 01/03/2026）裡、2026-11-05 版（現行，8,734 列）沒有；
同一 CKAN 上的「medicamentos para afiliados」（同 8,734 列、沒有 ALFABETA 欄）依品名＋包裝也查不到這些包裝，沒有「其實還在別份清單上」的號。集中在抗組織胺類（olopatadina、feniramina／nafazolina 眼藥、levocetirizina 單方、fexofenadina 60／120 mg、dimenhidrinato 錠）等 14 個藥；olopatadina 與 feniramina 的現行清單已沒有任何產品。
- `scripts/license_adapter.py`：fetch() 把整份清單代碼記成 CURRENT（少於 7,000 不判定；CKAN 給的 http 網址改用 https）；preprocess 對不在 CURRENT 的代碼標
  `license_status: cancelled`（本站事實層 cancelled＝不在 PAMI 現行清單）＋`pami_not_listed`（第一次發現日），status 改「Ya no figura en el listado de PAMI」（原值存 `status_before_pami_not_listed`），又出現在清單就還原。
  `confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」。
- 頁面照 PAMI 的口徑寫，不寫 ANMAT 註冊失效：母目錄 check_drug_page.py 加 AR 的 SCOPE_CANCELLED（全部不在清單的頁狀態列＝「No figura en el listado vigente de PAMI (los N productos de estos datos ya no figuran) – el estado del registro en ANMAT no está incluido en estos datos」，olopatadine、pheniramine 2 頁）；本站 tools/txgnn 同步同一份。
- 13 頁狀態列／張數列照事實層同步；正文寫「N autorizaciones vigentes／todas vigentes」而相反的 7 頁以 7 筆 `ar-lic-20261117-*` 更正（注記：que un producto ya no figure en el listado de PAMI no significa que su registro en ANMAT esté dado de baja）。
- 同日另修：7 個公開頁（aniracetam、camylofin、clenbuterol、mosapride、nandrolone、pridinol、thiocolchicoside）front matter 補 drugbank_id，FHIR 從 4cac653c 前一版找回（預測跟頁面 predicted_indications 相同），再由 sync_fhir_levels 對齊。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定：公開藥物頁 front matter drugbank_id 相同的 2 組，各留內容較完整的一頁、另一頁改成轉址（照 11-16 重複頁轉址的格式：layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）：amlodipino→amlodipina（DB00381）、carbocisteína→carboximetilcisteína（DB04339）。兩組預測與等級相同（L5），4 頁都沒有查核紀錄；公開藥物頁 328→326，衍生檔照重產，hreflang 拿掉 /drugs/amlodipino/ 一組（CO 同步）。兩個 ID 本來就沒有 FHIR MedicationKnowledge，FHIR 不變。

2026-11-19 補掃（證據包 drugbank_id 推斷沒有 front matter drugbank_id 的頁）：再找到 1 組 DB01222 budesonida／budesonide（預測 10 項、等級 L5 相同、許可證 20 張相同、都沒有查核紀錄），留字數較多的 budesonide，budesonida 改轉址；公開藥物頁 326→325。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indicación original: No consta en los datos locales」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：PAMI 給付清單（不寫 ANMAT）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acenocumarol「Indicación original: No consta en los datos locales」→「En Argentina, productos en el listado de PAMI: 5 (en el listado vigente: 5)」；2026-11-19 改了 216 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site ARTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。
