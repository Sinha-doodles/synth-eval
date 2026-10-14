"""Demonstrates model calibration assessment on synthetic confidence scores."""
from syntheval.metrics.calibration import expected_calibration_error, brier_score

def main():
    print("=== LLM Confidence Calibration Benchmark ===")
    confidences = [0.95, 0.90, 0.85, 0.60, 0.55, 0.40, 0.30]
    outcomes =    [1,    1,    1,    0,    1,    0,    0]
    ece = expected_calibration_error(confidences, outcomes, n_bins=5)
    bs = brier_score(confidences, outcomes)
    print(f"Expected Calibration Error: {ece:.4f}")
    print(f"Brier Score: {bs:.4f}")

if __name__ == "__main__":
    main()
