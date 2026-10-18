"""Telemetry counters and duration metrics."""
import time
from typing import Dict

class EvaluationMetricsTracker:
    def __init__(self):
        self.evaluation_counts: Dict[str, int] = {}
        self.latencies: Dict[str, float] = {}

    def record(self, metric_name: str, duration_ms: float):
        self.evaluation_counts[metric_name] = self.evaluation_counts.get(metric_name, 0) + 1
        self.latencies[metric_name] = duration_ms
