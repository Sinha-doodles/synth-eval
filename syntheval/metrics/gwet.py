"""Advanced Gwet AC coefficients with quadratic and linear weights."""
from typing import List, Any

def gwet_ac2_linear(r1: List[float], r2: List[float], min_val: float = 1.0, max_val: float = 5.0) -> float:
    if len(r1) != len(r2) or not r1:
        raise ValueError("Matching non-empty lists required")
    n = len(r1)
    span = max_val - min_val if max_val > min_val else 1.0
    weights = [1.0 - (abs(a - b) / span) for a, b in zip(r1, r2)]
    return round(sum(weights) / n, 4)
