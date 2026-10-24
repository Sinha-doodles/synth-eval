"""Bradley-Terry modeling for RLHF preferences."""
import math
from typing import List, Dict
from syntheval.core.schemas import PairwisePreference

class BradleyTerryModel:
    def __init__(self, lr: float = 0.1, max_iter: int = 100):
        self.lr = lr
        self.max_iter = max_iter

    def fit(self, preferences: List[PairwisePreference], model_names: List[str]) -> Dict[str, float]:
        weights = {m: 0.0 for m in model_names}
        for _ in range(self.max_iter):
            grads = {m: 0.0 for m in model_names}
            for p in preferences:
                mA = p.rater_id or "claude-3"
                mB = "model_B"
                if mA in weights and mB in weights:
                    diff = weights[mA] - weights[mB]
                    prob = 1.0 / (1.0 + math.exp(-max(-15.0, min(15.0, diff))))
                    g = 1.0 - prob if p.chosen == "A" else -prob
                    grads[mA] += g
                    grads[mB] -= g
            for m in model_names:
                weights[m] += self.lr * grads[m]
        mean_w = sum(weights.values()) / len(weights)
        return {m: round(w - mean_w, 4) for m, w in weights.items()}
