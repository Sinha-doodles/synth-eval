"""Statistical bootstrapping and variance estimation utilities."""
import random
from typing import List, Callable, Tuple, TypeVar

T = TypeVar("T")

def bootstrap_ci(
    data: List[T],
    metric_fn: Callable[[List[T]], float],
    n_resamples: int = 300,
    alpha: float = 0.05,
    seed: int = 42
) -> Tuple[float, float]:
    if len(data) < 2:
        val = metric_fn(data) if data else 0.0
        return (val, val)
    rng = random.Random(seed)
    n = len(data)
    boot_estimates: List[float] = []
    for _ in range(n_resamples):
        sample = [data[rng.randint(0, n - 1)] for _ in range(n)]
        try:
            boot_estimates.append(metric_fn(sample))
        except Exception:
            continue
    if not boot_estimates:
        base_val = metric_fn(data)
        return (base_val, base_val)
    boot_estimates.sort()
    low = max(0, int((alpha / 2.0) * len(boot_estimates)))
    high = min(len(boot_estimates) - 1, int((1.0 - alpha / 2.0) * len(boot_estimates)))
    return (round(boot_estimates[low], 4), round(boot_estimates[high], 4))
