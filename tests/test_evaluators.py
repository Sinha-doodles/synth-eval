import pytest
from syntheval.evaluators.hallucination import HallucinationEvaluator
from syntheval.evaluators.safety import SafetyGuardrailEvaluator
from syntheval.evaluators.pairwise import BradleyTerryModel
from syntheval.core.schemas import PairwisePreference

def test_hallucination():
    h = HallucinationEvaluator()
    res = h.verify_faithfulness("Paris is capital of France.", "Paris is France's capital city.")
    assert res.faithfulness_ratio >= 0.50

def test_safety():
    s = SafetyGuardrailEvaluator()
    assert s.scan_pii("Contact me at user@example.com") == ["email"]

def test_bt():
    bt = BradleyTerryModel()
    scores = bt.fit([PairwisePreference(prompt="q", completion_a="a", completion_b="b", chosen="A", rater_id="claude-3")], ["claude-3", "model_B"])
    assert scores["claude-3"] > scores["model_B"]
