"""Probability calibration metrics for generative model confidence."""
import math
from typing import List

def brier_score(probabilities: List[float], outcomes: List[int]) -> float:
    if not probabilities or len(probabilities) != len(outcomes):
        raise ValueError("Matching non-empty lists required")
    return round(sum((p - y) ** 2 for p, y in zip(probabilities, outcomes)) / len(probabilities), 4)

def expected_calibration_error(confidences: List[float], accuracies: List[int], n_bins: int = 10) -> float:
    if not confidences or len(confidences) != len(accuracies):
        raise ValueError("Matching non-empty lists required")
    n = len(confidences)
    bin_boundaries = [i / n_bins for i in range(n_bins + 1)]
    ece = 0.0
    for i in range(n_bins):
        low, high = bin_boundaries[i], bin_boundaries[i + 1]
        indices = [idx for idx, c in enumerate(confidences) if (low <= c < high or (i == n_bins - 1 and low <= c <= high))]
        if not indices:
            continue
        bin_acc = sum(accuracies[idx] for idx in indices) / len(indices)
        bin_conf = sum(confidences[idx] for idx in indices) / len(indices)
        ece += (len(indices) / n) * abs(bin_acc - bin_conf)
    return round(ece, 4)
