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
