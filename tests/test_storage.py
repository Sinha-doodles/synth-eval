from syntheval.storage.cache import EvaluationCache

def test_cache():
    cache = EvaluationCache(":memory:")
    cache.set("p", "c", {"score": 1.0})
    assert cache.get("p", "c") == {"score": 1.0}
    assert cache.get("other", "c") is None
