from syntheval.evaluators.degeneracy import repetition_ratio

def test_repetition():
    repeated = "echo echo echo echo echo echo"
    clean = "the quick brown fox jumps over the lazy dog"
    assert repetition_ratio(repeated, n=2) > 0.50
    assert repetition_ratio(clean, n=2) < 0.20
