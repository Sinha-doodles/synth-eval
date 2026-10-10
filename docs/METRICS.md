# Extended Metrics Reference

### Expected Calibration Error (ECE)
Measures alignment between confidence and empirical accuracy across $M$ bins:
$$ECE = \sum_{m=1}^M \frac{|B_m|}{N} |acc(B_m) - conf(B_m)|$$

### Population Stability Index (PSI)
Quantifies divergence between reference distribution $P$ and current distribution $Q$:
$$PSI = \sum (Q_i - P_i) \times \ln(Q_i / P_i)$$
- PSI < 0.10: Stable distribution
- 0.10 <= PSI < 0.20: Moderate shift
- PSI >= 0.20: Significant drift requiring retraining/re-annotation
