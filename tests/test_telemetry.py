from syntheval.api.telemetry import EvaluationMetricsTracker
from syntheval.api.tracing import TracingContext

def test_telemetry():
    t = EvaluationMetricsTracker()
    t.record("krippendorff", 12.5)
    assert t.evaluation_counts["krippendorff"] == 1
    assert TracingContext.create_span("eval")["span_name"] == "eval"
