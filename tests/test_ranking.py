from syntheval.metrics.ranking import kendall_tau_b, spearman_correlation, ndcg_at_k

def test_rankings():
    assert kendall_tau_b([1, 2, 3], [1, 2, 3]) == 1.0
    assert spearman_correlation([1, 2, 3], [1, 2, 3]) == 1.0
    assert ndcg_at_k([3, 2, 1], k=2) == 1.0
