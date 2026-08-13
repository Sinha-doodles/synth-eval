"""Lexical n-gram and surface similarity metrics."""
import math
from typing import Dict, List

def _ngrams(tokens: List[str], n: int) -> List[tuple[str, ...]]:
    return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

def rouge_n(candidate: str, reference: str, n: int = 1) -> Dict[str, float]:
    cand_tokens = candidate.lower().split()
    ref_tokens = reference.lower().split()
    cand_ng = _ngrams(cand_tokens, n)
    ref_ng = _ngrams(ref_tokens, n)
    if not cand_ng or not ref_ng:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}
    counts = {}
    for g in ref_ng:
        counts[g] = counts.get(g, 0) + 1
    overlap = 0
    for g in cand_ng:
        if counts.get(g, 0) > 0:
            overlap += 1
            counts[g] -= 1
    p = overlap / len(cand_ng)
    r = overlap / len(ref_ng)
    f1 = (2 * p * r) / (p + r) if (p + r) > 0 else 0.0
    return {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4)}

def bleu_score(candidate: str, reference: str, max_n: int = 4) -> float:
    cand_tokens = candidate.lower().split()
    ref_tokens = reference.lower().split()
    if not cand_tokens or not ref_tokens:
        return 0.0
    bp = 1.0 if len(cand_tokens) > len(ref_tokens) else math.exp(1.0 - (len(ref_tokens) / len(cand_tokens)))
    precisions = []
    for n in range(1, max_n + 1):
        c_ng = _ngrams(cand_tokens, n)
        r_ng = _ngrams(ref_tokens, n)
        if not c_ng:
            continue
        rc = {}
        for g in r_ng:
            rc[g] = rc.get(g, 0) + 1
        m = sum(1 for g in c_ng if rc.get(g, 0) > 0)
        precisions.append((m + 1e-9) / len(c_ng))
    return round(bp * math.exp(sum(math.log(p) for p in precisions) / len(precisions)), 4)
