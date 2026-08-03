from syntheval.metrics.calibration import brier_score, expected_calibration_error

def test_brier_score():
    assert brier_score([1.0, 0.0], [1, 0]) == 0.0

def test_ece():
    assert expected_calibration_error([0.8, 0.9], [1, 1], n_bins=5) < 0.25
