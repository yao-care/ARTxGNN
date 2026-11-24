"""PAMI 價目表成分欄（證據包 tfda.records 的 ingredients）的成分切分與單方／複方判定（2026-11-24）。

原本 reviewer/drug_evidence_pack.py 用「;;」切成分，但本站成分欄的複方以「+」連接（例「diosmina+hesperidina micronizada」
「homatropina,metilbr.+asoc.」，「asoc.」＝asociados），事實層把複方也算成單方（single_total＝total）。用戶 2026-11-24 決定：
事實層依本站成分欄正確切分。逗號是「成分,鹽類」寫法（「morfina,clorhidrato」「timolol,maleato」），不是分隔。
"""


def split_ingredients(s):
    return [x.strip() for x in str(s or "").split("+") if x.strip()]


def kind(s):
    """單方 single／複方 combo；成分欄空白時照舊算 single（跟原本「;;」切法空白時的結果相同）"""
    return "combo" if len(split_ingredients(s)) > 1 else "single"
