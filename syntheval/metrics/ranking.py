"""Ranking and ordinal correlation metrics."""
import math
from typing import List

def kendall_tau_b(x: List[float], y: List[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("Matching lists of length >= 2 required")
    n = len(x)
    concordant = 0
    discordant = 0
    t_x = 0
    t_y = 0
    for i in range(n):
        for j in range(i + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx == 0 and dy == 0:
                t_x += 1
                t_y += 1
            elif dx == 0:
                t_x += 1
            elif dy == 0:
                t_y += 1
            elif (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                concordant += 1
            else:
                discordant += 1
    denom = math.sqrt((concordant + discordant + t_x) * (concordant + discordant + t_y))
    return round((concordant - discordant) / denom, 4) if denom > 0 else 0.0

def spearman_correlation(x: List[float], y: List[float]) -> float:
    n = len(x)
    indexed_x = sorted(range(n), key=lambda i: x[i])
    indexed_y = sorted(range(n), key=lambda i: y[i])
    rx = [0.0] * n
    ry = [0.0] * n
    for rank, idx in enumerate(indexed_x):
        rx[idx] = rank + 1
    for rank, idx in enumerate(indexed_y):
        ry[idx] = rank + 1
    d_sq = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return round(1.0 - (6.0 * d_sq) / (n * (n * n - 1)), 4)

def ndcg_at_k(relevance_scores: List[float], k: int = 5) -> float:
    cutoff = min(len(relevance_scores), k)
    if cutoff == 0:
        return 0.0
    dcg = sum((2 ** r - 1) / math.log2(idx + 2) for idx, r in enumerate(relevance_scores[:cutoff]))
    ideal = sorted(relevance_scores, reverse=True)[:cutoff]
    idcg = sum((2 ** r - 1) / math.log2(idx + 2) for idx, r in enumerate(ideal))
    return round(dcg / idcg, 4) if idcg > 0 else 0.0
