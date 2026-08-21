"""Self-consistency consensus and generation entropy."""
import math
from collections import Counter
from typing import List, Dict, Any

def shannon_entropy(labels: List[str]) -> float:
    if not labels:
        return 0.0
    counts = Counter(labels)
    n = len(labels)
    entropy = 0.0
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def majority_vote_consensus(labels: List[str]) -> Dict[str, Any]:
    if not labels:
        return {"consensus": None, "agreement_ratio": 0.0}
    counts = Counter(labels)
    top_label, top_count = counts.most_common(1)[0]
    return {
        "consensus": top_label,
        "agreement_ratio": round(top_count / len(labels), 4),
        "entropy": shannon_entropy(labels)
    }
