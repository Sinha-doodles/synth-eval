from syntheval.evaluators.drift import population_stability_index

def test_psi():
    data = [0.1, 0.2, 0.5, 0.8] * 10
    assert population_stability_index(data, data) < 0.05
