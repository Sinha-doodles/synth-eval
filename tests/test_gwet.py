from syntheval.metrics.gwet import gwet_ac2_linear

def test_gwet_ac2():
    assert gwet_ac2_linear([1.0, 2.0], [1.0, 2.0]) == 1.0
    assert gwet_ac2_linear([1.0, 2.0], [2.0, 3.0], 1.0, 5.0) > 0.50
