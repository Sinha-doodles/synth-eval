"""TruthfulQA synthetic QA evaluation benchmark."""
from typing import List, Dict, Any
from syntheval.core.schemas import HallucinationScore

class TruthfulQABenchmark:
    @staticmethod
    def evaluate_qa_batch(predictions: List[Dict[str, str]]) -> Dict[str, Any]:
        total = len(predictions)
        truthful = sum(1 for p in predictions if p.get("predicted") == p.get("gold_truth"))
        return {
            "total_questions": total,
            "accuracy": round(truthful / total, 4) if total > 0 else 0.0,
            "metric": "truthful_qa_mc1"
        }
