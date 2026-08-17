"""Statistical distribution drift detector for evaluation scores."""
import math
from typing import List

def population_stability_index(reference: List[float], current: List[float], n_bins: int = 10) -> float:
    if not reference or not current:
        raise ValueError("Non-empty distributions required")
    min_v = min(min(reference), min(current))
    max_v = max(max(reference), max(current))
    if min_v == max_v:
        return 0.0
    step = (max_v - min_v) / n_bins
    psi = 0.0
    n_ref = len(reference)
    n_cur = len(current)
    for i in range(n_bins):
        low = min_v + i * step
        high = low + step
        ref_cnt = sum(1 for x in reference if low <= x < high or (i == n_bins - 1 and low <= x <= high))
        cur_cnt = sum(1 for x in current if low <= x < high or (i == n_bins - 1 and low <= x <= high))
        p_ref = max(1e-4, ref_cnt / n_ref)
        p_cur = max(1e-4, cur_cnt / n_cur)
        psi += (p_cur - p_ref) * math.log(p_cur / p_ref)
    return round(psi, 4)
