from syntheval.benchmarks.truthful_qa import TruthfulQABenchmark

def test_truthful_qa():
    preds = [
        {"predicted": "Earth", "gold_truth": "Earth"},
        {"predicted": "Mars", "gold_truth": "Venus"}
    ]
    res = TruthfulQABenchmark.evaluate_qa_batch(preds)
    assert res["accuracy"] == 0.50
