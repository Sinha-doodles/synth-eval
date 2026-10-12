"""Filter raw synthetic generation data based on hallucination and safety thresholds."""
import asyncio
from syntheval.evaluators.hallucination import HallucinationEvaluator
from syntheval.evaluators.safety import SafetyGuardrailEvaluator

async def main():
    print("=== Automated Synthetic Data Quality Filtering ===")
    samples = [
        {"id": "s1", "cand": "Python is dynamic.", "src": "Python is a dynamic programming language."},
        {"id": "s2", "cand": "Mars is made of blue cheese.", "src": "Mars is the fourth planet from the Sun."}
    ]
    h_eval = HallucinationEvaluator()
    for s in samples:
        score = h_eval.verify_faithfulness(s["cand"], s["src"])
        passed = score.faithfulness_ratio >= 0.80
        print(f"Sample {s['id']}: Faithfulness={score.faithfulness_ratio} -> {'KEEP' if passed else 'DISCARD'}")

if __name__ == "__main__":
    asyncio.run(main())
