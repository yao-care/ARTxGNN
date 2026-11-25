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

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 258 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `ar-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（español）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：225 頁寫入紀錄（美國仿單 203、ChEMBL 22），33 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 22 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）1 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indicación original: No consta en los datos locales」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：PAMI 給付清單（不寫 ANMAT）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acenocumarol「Indicación original: No consta en los datos locales」→「En Argentina, productos en el listado de PAMI: 5 (en el listado vigente: 5)」；2026-11-19 改了 216 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site ARTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 市場段落許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站逐站做，本站做表＋B）：每週許可證排程只改概覽表狀態列／張數列，AI 寫的自由格式許可證表（多半只列前 5 筆、第四欄寫「No registrada en los datos locales」）與正文寫死的張數會跟每週變的 PAMI 價目表矛盾、checker 擋頁。做法照 BrTxGNN（結構同為 site_config）與 COTxGNN（同為西班牙文）。
- A. `scripts/sync_license_tables.py`：市場段落（「## Información de Mercado en Argentina」，known_use 頁的標題「Usos conocidos y situación de mercado」不算）的第一張表換成程式依證據包 tfda.records 產生的表
  「| Número de Autorización | Nombre del Producto | Presentación | Laboratorio | Estado |」（ALFABETA 代碼、nombre_comercial、presentacion、laboratorio_titular 原文；PAMI 把非 ASCII 字存成「¿」「ß」的 9 個廠商名照 LAB_FIX 寫回，例 Bag¿→Bagó、Cassarß→Cassará）；
  狀態只有「Vigente」（在 PAMI 現行清單）與「Ya no figura en el listado de PAMI」（adapter 的 pami_not_listed），不寫 ANMAT 註冊狀態；在清單的在前。
  列數照 CO：原表列數與 min(5, 筆數) 取大（最多 20），段落裡有 AI 的「列了幾筆」說明句（se muestran／la lista muestra／principales…）時照原表列數；重排時以頁面現有程式表列數為準。
  表下程式句「La tabla muestra N de los M productos … (listado de medicamentos para entidades de PAMI); el estado del registro en ANMAT no está incluido en estos datos.」（部分收錄另寫「los datos solo incluyen una parte…」）；沒有紀錄時 NONE_LINE。
  段落沒有表的公開頁在段落最後補程式區塊（noindex 頁不補）。正文或查核紀錄更正文字指名「表上／表外」產品的 6 頁（fexofenadina、levocetirizina、naphazoline、modafinil、metilfenidato、oxcarbazepina）照 `config/license_table_pins.json` 置頂原表的號碼與順序。
  前後 `<!-- licenses:begin/end -->`；快照存 rows／total／partial；gate 第 18 項（`src/artxgnn/regulatory/licenses.py` 的 program_block_problems）擋「段落有表卻不是程式區塊」「程式區塊≠快照重算」。
  接進：每週排程（`scripts/license_adapter.py` 的 sync_tables＋PAGE_NOTE）、`apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾（`--from-snapshot`；`--ws` 可省略，預設 tools/txgnn）、`sync_notes_to_docs.py` 重套紀錄之後。
- B. `scripts/rewrite_license_counts.py`＋`src/artxgnn/regulatory/count_prose.py`（照 CO 移植，本站句型）：依快照事實層改寫句型明確的「N autorizaciones vigentes／N productos／ya no figuran」；本站 vigente＝在 PAMI 現行清單。
  有保留、講證據包或查詢、相對數、劑型或廠商子集、顯示筆數、partial 頁不動；同一行有判斷不了的整行不動。不改、列待查：文字數詞不符（word-numeral）、同一行另有 las otras dos／los demás／todas 之類說法（relative）、跨過 1（plural）、0 張前提或改成 0、
  單方／複方張數（本站事實層 single_total 沒拆「+」複方，只驗不改：single-combo）。`apply_drug_reviews.py`（非 --check）、`build_license_snapshot.py` 結尾自動跑；gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 套用（Release data-20261117-103852）：公開藥物頁 325 頁全部有程式區塊（AI 表換掉 318 頁、段落沒有表補 7 頁；noindex 頁 0 頁），改到的行只有表格列、區塊標記與表下程式句，last_modified_at 改 2026-11-24。
  被換掉的表上沒有錨著查核紀錄（superseded 0 筆）。正文張數現況全部跟快照一致，B 改寫 0 句、判斷不了 0 句（有保留而略過 10 句）；以「每藥有效＋3」模擬事實變動，B 會改 12 行、列待查 71 句（single-combo 44、word-numeral 19、relative 4、plural 3、ambiguous 1），其餘 22 句有保留不動。
  checker 全量前後都是 0、gate exit 0；另寫的寬偵測（正文張數／全部有效／不在清單說法跟事實不符）前後都是 7 句，全是誤中（DDI 查詢「devolvió 4 registros」、「una sexta autorización」等）。
- 未處理：noindex 的 cefalexina、ciclopirox 正文寫「沒有許可」但證據包有 5、2 筆（段落沒有表，沒補程式區塊）；母目錄 `.claude/license_labels/ARTxGNN.json` 只有「Vigente」，要加「Ya no figura en el listado de PAMI」→cancelled（不在本站改）。

## 第二輪：舊錯句、單方／複方、劑型說法與紀錄張數（2026-11-24）

用戶 2026-11-24 第二輪決定（處理第一輪列待查的事；本站第一輪待查清單沒有新增項目，處理派工點名的句子與全站掃描）。依據照本站口徑：PAMI 給付清單（證據包 tfda.records、`data/raw/ar_fda_drugs.json` 2026-03-01 全量），不寫 ANMAT 註冊狀態。
- 派工點名：noindex 的 cefalexina（證據包 61 筆收 20 筆）、ciclopirox（2 筆）正文寫「沒有許可／沒有登記」，以 `ar-lic-20261124b-cefalexina-1`～`-5`、`ciclopirox-1`～`-3` 更正（待辦條目只拿掉「查不到、要換名稱再查」的前提）。noindex 頁照本站規則不補程式許可證表，更正文字指向概覽表。
  另 tinidazol、varenicline 的「autorizaciones vigentes de ANMAT」改成 PAMI 口徑（`ar-lic-20261124b-*`）。
- 單方／複方標籤（第一輪 B 的 single-combo 只驗不改）：全量掃公開頁寫「un solo principio activo／monofármaco／monodroga／producto único／sin combinaciones」的句子 176 句，逐句對照證據包成分欄（「+」＝複方），部分收錄的頁另對 2026-03 全量同成分品項；跟事實相反的 54 句以 `ar-lic-20261124-<藥>-N` 更正（例：amilorida、sulfametoxazol、trimetoprima、sacubitril、salmeterol 全部是複方；allopurinol、nimodipina、salbutamol「至少 20 張單方」實際單方不到 20）；其餘查證成立（例：pioglitazona「單方或與 metformina 複方」、部分收錄頁單方確實 ≥20）。
- 劑型說法：全量掃市場相關句子 384 句（劑型、品牌、單方字樣），自動比對證據包劑型類別後人工讀過，只有 prednisolona 待辦寫「orales」不成立（`ar-lic-20261124b-prednisolona-1`），其餘成立。
- 缺表：公開頁 325 頁都有程式區塊（第一輪已做），沒有「表另行補上」之類矛盾句。
- 張數樣板：site_config 的 `figures` 改成不寫數字（FIGURES_NOTE）；既有 9 筆紀錄說明裡寫死張數的同 id 重發。查核紀錄更正文字裡寫死張數／舊表筆數的 7 筆 `ar-lic-20261117-*`（cyproheptadine、fexofenadina、insulina_glargina、levocetirizina、naphazoline、olopatadine、pheniramine）同 id 重發，前版存 history，順便補正其中的單方說法（fexofenadina 有 ALERCAS D、levocetirizina 有 montelukast 複方、cyproheptadine／pheniramine 全是複方）。
- 驗證：checker 全量前後 0、gate exit 0、B 改寫 0 句；寬偵測（ar_wide）剩 8 句都是誤中（DDI 查詢筆數、「una sexta autorización」等）；單方字樣重掃剩下的命中都已查證成立或是文獻句。

## 缺市場段落的公開頁（2026-11-24 第三輪）

用戶 2026-11-24 決定（比照 JpTxGNN 第二輪 `add_section`）：公開頁（非 noindex、非轉址）整頁沒有市場段落（## Información de Mercado en Argentina）、證據包卻有許可證紀錄的，要補段落與程式表。
2026-11-24 全量量測本站 0 頁，所以只加 gate：`src/artxgnn/regulatory/licenses.py` 的 page_problems 擋「公開頁快照有程式表列卻沒有市場段落」（之後若出現，再比照 Jp 在 `scripts/sync_license_tables.py` 加 add_section）。gate exit 0。
2026-11-24 第四輪（用戶決定）：補上自動補段落的程式。`scripts/sync_license_tables.py` 的 `add_section`（process 找不到市場段落時呼叫）：公開頁、證據包有紀錄的，
在「## Consideraciones de Seguridad」之前（沒有就 Conclusión y Próximos Pasos、Registro de verificación、Descargo de responsabilidad 之前；查核紀錄段標題在 `<!-- review:begin log -->` 區塊裡時放在區塊之前）
補「## Información de Mercado en Argentina」與程式表（min(5, 筆數) 列＋程式說明句）；noindex 頁、沒有紀錄的頁不補。快照模式與證據包模式都會補，所以 apply_drug_reviews.py、build_license_snapshot.py 結尾、
每週排程 sync_tables、sync_notes_to_docs.py 重寫後都會自動補；license_adapter 的 PAGE_NOTE 放行新標題行。全量量測 0 頁要補（dry-run 0 頁）。
驗證：拿掉 acenocumarol、adapaleno（公開頁）與 bromhexina（noindex）的市場段落：gate 擋 2 頁（noindex 不擋），快照模式與證據包模式（adapter sync_tables）補回的程式表與原頁一字不差（AI 寫的段落說明句不會補回，預期內）、
noindex 不補、再跑 0 頁；另以拿掉市場／安全性／結論段的 acetazolamida 確認段落放在 log 區塊之前、可重複執行；之後還原原頁。checker 全量 0、gate exit 0。

## 事實層單方／複方依本站成分欄切分（2026-11-24）

用戶 2026-11-24 決定：事實層依各站成分欄正確切分。reviewer/drug_evidence_pack.py 原本用「;;」切成分，本站 PAMI 成分欄的複方以「+」連接（diosmina+hesperidina、「+asoc.」），都算成單方；改用 `src/artxgnn/regulatory/ingredients.py`（逗號是「成分,鹽類」寫法，不切）。
事實層 479 藥中 165 藥 single_total 改變；證據包 122 個重算（data-overlay）。寬偵測掃事實有變的頁：第二輪紀錄已更正，跟新事實矛盾 0 句；B（單方數字只驗不改）判斷不了 0 句；checker 0→0。

## 每週排程存現行 PAMI 清單的成分、量新代碼漏收（2026-11-25 第五輪）

用戶 2026-11-25 決定（第五輪第 3 條）：`scripts/license_adapter.py` 的 fetch() 原本只存 ALFABETA 代碼，改成連同 PRINCIPIO ACTIVO、MARCA COMERCIAL、PRESENTACION、LABORATORIO
一起存進 `data/raw/pami_alfabeta.json`（欄名同 ar_fda_drugs.json：nombre_generico、nombre_comercial、presentacion、laboratorio_titular；成分欄大多空白就 raise），Release 就帶著現行清單的成分。
2026-11-25 抓 2026-11-05 版（8,734 列）寫入，經 data-overlay 進 Release。
- `scripts/measure_pami_new_items.py`（只量、不改）：照原收集器規則（成分字串已在 drug_mapping.csv 就沿用其 DrugBank ID，否則用 run_kg_prediction 同一支 map_fda_drugs_to_drugbank 逐成分對照，跟證據包 drugbank_ids 有交集）量現行清單有、證據包沒收的代碼。
- 2026-11-25 量測：不在 2026-03 基準的新代碼 754 個，對得到 DrugBank 671 個、屬於某證據包 645 個；涉及 151 個證據包、890 筆（公開頁 108、noindex 22、轉址 3、沒有頁 18；部分收錄 89 包、完整 62 包）。
  例：amlodipina 29、carvedilol 31、empagliflozina 20（證據包原本 4 筆）、diclofenac 19、bisoprolol 14、etoricoxib 13。複方依原規則逐成分歸屬（例 ciproheptadina+calcio+asoc. 也歸 calcio）。
  超過 50 個證據包，照第五輪說明先停下回報，沒有補收、沒有接進排程（待用戶決定）。

## PAMI 現行清單新代碼依原規則補收（2026-11-25 第六輪）

用戶 2026-11-25 決定（第六輪第 1 條「新許可補收：全部照原規則補」，接第五輪量測 151 包／890 筆）：證據包 tfda 區塊是 collectors/arfda.py 依 data/processed/drug_mapping.csv（2026-03-01 版價目表 ar_fda_drugs.json 的代碼→DrugBank ID）收的，之後才出現在 PAMI 價目表的代碼永遠收不進來。
- `scripts/add_current_licenses.py [--download] [--dry-run] [--report out.tsv]`（照 ESTxGNN 第五輪同名檔的做法）：每個證據包第一次跑時判定收集規則，記在 tfda.collection_rule——collection_log 的 tfda queried_at 早於 2026-10-12 的（2026-03-29 收的 414 包）照 drug_mapping.csv.bak_20261012，之後收的（2026-10-12 的 65 包）照現行 drug_mapping.csv（rescue 後）；用那份對照在 ar_fda_drugs.json 重算原收集器，筆數＝total_matches、現有紀錄都在裡面才算數（另一份也試，都不對就整包停損不補）。2026-11-25 全部 479 包都重算得出（只有 bak 對得上 16 包、只有現行 65 包、兩份都對 390 包、空的 8 包）；當時因 20 筆上限沒存的代碼回填 tfda.records_not_stored（113 包），防重複計數。
  補收：現行清單（data/raw/pami_alfabeta.json，第五輪起 adapter 存成分）的新代碼，成分字串（PRINCIPIO ACTIVO＝nombre_generico）照該份 drug_mapping 的「原始成分字串→DrugBank ID」（見過、當時對不到的照舊對不到）；沒見過的字串用 Phase 1 的 drugbank_mapper（get_all_synonyms 逐成分）；現行對照另把對不到的成分照 rescue 規則補救（`src/artxgnn/mapping/rescue_20261012.py`，逐字取自母 repo .claude/rescue_mapping.py，只改詞表路徑）。records 未滿 20 存進 records（單方在前），滿了只記代碼在 records_not_stored，都算進 total_matches；每筆記 source、added；只加不刪、可重複執行；EXCLUDE 表（目前空）。原收集器的成分欄備援比對（mapping 一筆都沒有時）也照做。
  `.github/workflows/license-refresh.yml` 在 license_refresh 前以 `--download` 跑（失敗不擋排程），有補收就照常發新 Release。
- 2026-11-25 套用（Release data-20261125-005536，清單 2026-11-05 版 8,734 列）：152 個證據包補 865 筆（存進 records 136、只記代碼 729）；第二次跑 0 筆。比第五輪量測（全部用現行對照）少的 32 筆是 rescue 之前收的證據包、只有 rescue 後對照才對得到的字串（diclofenac potásico、amlodipina+losartán,potásico、ketorolac trometamina、mometasona furoato、loteprednol,etabonato），照收集當時的規則不收；多的 7 筆是 10-12 收的證據包靠 rescue 才對得到的（prasterona 4、fenazopiridina、dexametasona+nafazolina+asoc.、homatropina,metilbr.＝rescue 對到 homatropine，跟 2026-03 清單的 SUMAL 等同一規則）。逐筆看過 865 筆，沒有醫藥外品、獸用或別的藥（複方照原規則逐成分歸屬，例 CIPROVIT CALCICO 也歸 calcio），EXCLUDE 沒有加。`scripts/measure_pami_new_items.py` 的 have 加上 records_not_stored，補收後剩 32 筆（上面那類）。
  證據包 local_regulatory 重算 51 個（refresh_pack_regulatory）；部分收錄 113→120 包；概覽狀態列／張數列 57 頁 114 格（sync_market_rows）、程式表 48 頁、正文張數 B 改寫 3 頁、description 句尾 34 頁由程式同步。
- 正文：寬偵測（改到的 152 包的頁，含 noindex，市場與摘要的張數、todas／ambas／las N、único／solo、劑型、品牌、廠商）226 句逐句對照證據包全部代碼（records＋records_not_stored，對現行清單），跟新事實矛盾的 20 處以 `ar-lic-20261125-*` 更正（更正文字不寫張數）：eplerenone、flecainida、imiquimod、labetalol、lactulose、metilfenidato×2、modafinil（「另外兩張是 FORCILIN」）、orlistat、oxibutinina、prednisolona、terazosin、zolpidem、dutasteride 的張數或「Las N」；midazolam（新增 DORMICUM，Siegfried）、phenazopyridine（新增 CISTALGINA 單方）、idebenone（新增 GENICERAL）、fluorouracil（「唯一劑型是乳膏」→另有 5 FU 軟膏）、aciclovir 摘要與待辦（另有 aciclovir＋hidrocortisona 外用；LISOVYR CORT 補收前就在證據包未存的代碼裡，一併更正）。prednisolona 同一行的模型預測文字不動。
  沒改：部分收錄頁原本就寫「Se registran 20 autorizaciones」的 etoricoxib、pridinol（補收前就是部分收錄、句子早就不精確，不是這次造成的）。
- 驗證：checker 全量前後都是 0、--row-status 0；gate exit 0；apply --check 0；rewrite_license_counts --list 改前 0、補收後 10 句、更正後 0；ar_wide 寬偵測回到改前的 8 句（都是第一輪判定的誤中）。正文有變的 58 頁 last_modified_at 改 2026-11-25。證據包經 data-overlay 推進 Release。

## 部分收錄頁正文寫死的總數（2026-11-25 第七輪）

用戶 2026-11-25 決定（第七輪第 2 條）：部分收錄頁（快照事實層 partial，證據包存 20 筆、total_matches 較多）正文寫死的總數或表上列數，小於 total_matches 或跟程式表列數不符的，照之前部分收錄頁的做法改成不寫死數字（查核紀錄）。
- 全量掃（快照 partial 的 102 頁，含 noindex；排除查核框、程式區塊）：數字＋許可字樣的句子 68 句，其中 58 句是「al menos 20」等保留語（20 ≤ total_matches，成立）、5 句是「Se listan 5 …」這類講表上列數（＝程式表 5 列，成立）。
  不成立的 9 句以 9 筆 `ar-lic-20261125b-<藥>-1` 更正（更正文字不寫張數，指向概覽表與程式表）：etoricoxib、pridinol「Se registran 20 autorizaciones vigentes」（91、71 張；pridinol 另把「todas de productos de un solo registro」照實改成「en su mayoría asociaciones」，存下的 20 筆單方只有 2 筆）、
  clobetasol、ketorolac「5 de las 20」（26、42 張）、hidrocortisona「Se listan 20」、ezetimibe「se muestran 20 registros」（表上 5 列）、clindamicina、metformina「las 20 (autorizaciones) listadas」、meloxicam「20 autorizaciones vigentes en la lista disponible」。單方／全部在清單的說法只講「存下的紀錄」（事實層只涵蓋這 20 筆），其餘只記號碼的代碼不另推定。
- 另寫的獨立寬偵測（不靠名詞鄰接：許可字樣 ±80 字內任何數字或文字數詞，小於 total_matches、不是 5、同句沒有保留語；含 description、快速總覽格）：改前 16 句（6 句是上面的、metformina 1 句是 scan 漏的，已併入；其餘是作用機轉節錄與 Data Gaps 誤中），改後 10 句全是誤中。
- 驗證：apply --check 0、rewrite_license_counts --check 0、sync_license_tables --from-snapshot --dry-run 0；checker 前後都是 P1 160（本機沒還原證據包，P1 前後相同、跟許可證無關）、--row-status 0；gate exit 0。正文有變的 9 頁 last_modified_at 改 2026-11-25。證據包沒有改，不用 data-overlay。
