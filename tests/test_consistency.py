from syntheval.evaluators.consistency import shannon_entropy, majority_vote_consensus

def test_consistency():
    assert shannon_entropy(["A", "A"]) == 0.0
    assert majority_vote_consensus(["pass", "pass", "fail"])["consensus"] == "pass"
