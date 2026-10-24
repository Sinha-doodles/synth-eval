"""Inter-Annotator Agreement metrics."""
import math
from typing import List, Dict, Any, Literal
from collections import Counter
from syntheval.core.schemas import AnnotationRecord, AgreementResult
from syntheval.core.exceptions import InsufficientDataError

def _interpret(c: float) -> str:
    if c < 0: return "Poor"
    elif c <= 0.2: return "Slight"
    elif c <= 0.4: return "Fair"
    elif c <= 0.6: return "Moderate"
    elif c <= 0.8: return "Substantial"
    return "Near Perfect"

def cohen_kappa(r1: List[Any], r2: List[Any]) -> float:
    if len(r1) != len(r2) or not r1:
        raise ValueError("Matching non-empty lists required")
    n = len(r1)
    cats = sorted(list(set(r1).union(set(r2))))
    c2i = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    mat = [[0] * k for _ in range(k)]
    for a, b in zip(r1, r2):
        mat[c2i[a]][c2i[b]] += 1
    p_o = sum(mat[i][i] for i in range(k)) / n
    p1 = [sum(mat[i][j] for j in range(k)) / n for i in range(k)]
    p2 = [sum(mat[j][i] for j in range(k)) / n for i in range(k)]
    p_e = sum(p1[i] * p2[i] for i in range(k))
    if math.isclose(p_e, 1.0): return 1.0 if math.isclose(p_o, 1.0) else 0.0
    return round((p_o - p_e) / (1.0 - p_e), 4)

def fleiss_kappa(records: List[AnnotationRecord]) -> AgreementResult:
    if not records: raise InsufficientDataError("Empty records")
    all_cats = sorted(list({v for r in records for v in r.ratings.values()}))
    c2i = {c: i for i, c in enumerate(all_cats)}
    k = len(all_cats)
    n = len(records)
    m = len(records[0].ratings)
    p_item = []
    p_cat = [0.0] * k
    for r in records:
        counts = [0] * k
        for val in r.ratings.values():
            counts[c2i[val]] += 1
            p_cat[c2i[val]] += 1
        sq_sum = sum(cnt * cnt for cnt in counts)
        p_item.append((sq_sum - m) / (m * (m - 1)) if m > 1 else 1.0)
    p_bar = sum(p_item) / n
    tot = n * m
    p_e = sum((cnt / tot) ** 2 for cnt in p_cat)
    coeff = 1.0 if math.isclose(p_e, 1.0) else (p_bar - p_e) / (1.0 - p_e)
    coeff = max(-1.0, min(1.0, round(coeff, 4)))
    return AgreementResult(metric_name="Fleiss Kappa", coefficient=coeff, num_items=n, num_raters=m, interpretation=_interpret(coeff))

def krippendorff_alpha(records: List[AnnotationRecord], level: str = "nominal") -> AgreementResult:
    if not records: raise InsufficientDataError("Empty records")
    unique_vals = sorted(list({v for r in records for v in r.ratings.values()}))
    if len(unique_vals) <= 1:
        return AgreementResult(metric_name=f"Krippendorff Alpha ({level})", coefficient=1.0, num_items=len(records), num_raters=len(records[0].ratings), interpretation="Near Perfect")
    marginal = Counter()
    do_num = 0.0
    do_den = 0.0
    for r in records:
        vals = list(r.ratings.values())
        m_u = len(vals)
        if m_u < 2: continue
        for v in vals: marginal[v] += 1
        for i in range(m_u):
            for j in range(i + 1, m_u):
                dist = 0.0 if vals[i] == vals[j] else 1.0
                do_num += dist / (m_u - 1)
        do_den += 1.0
    d_o = do_num / do_den if do_den > 0 else 0.0
    tot = sum(marginal.values())
    de_num = sum(c1 * c2 * (0.0 if v1 == v2 else 1.0) for v1, c1 in marginal.items() for v2, c2 in marginal.items())
    d_e = de_num / (tot * (tot - 1)) if tot > 1 else 1.0
    alpha = 1.0 - (d_o / d_e) if not math.isclose(d_e, 0.0) else 1.0
    coeff = max(-1.0, min(1.0, round(alpha, 4)))
    return AgreementResult(metric_name=f"Krippendorff Alpha ({level})", coefficient=coeff, num_items=len(records), num_raters=len(records[0].ratings), interpretation=_interpret(coeff))

def gwet_ac1(r1: List[Any], r2: List[Any]) -> float:
    n = len(r1)
    cats = sorted(list(set(r1).union(set(r2))))
    k = len(cats)
    p_a = sum(1 for a, b in zip(r1, r2) if a == b) / n
    cat_probs = [(sum(1 for x in r1 if x == c) + sum(1 for x in r2 if x == c)) / (2 * n) for c in cats]
    p_e = sum(pj * (1.0 - pj) for pj in cat_probs) / (k - 1) if k > 1 else 0.0
    return round((p_a - p_e) / (1.0 - p_e), 4) if not math.isclose(p_e, 1.0) else 1.0
