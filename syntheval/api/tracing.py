"""Tracing span context helpers."""
class TracingContext:
    @staticmethod
    def create_span(name: str):
        return {"span_name": name, "timestamp": 1729800000}
