from syntheval.evaluators.citation_validator import CitationValidator

def test_citations():
    text = "Refer to https://arxiv.org/abs/1706.03762 and doi:10.1145/3308558."
    res = CitationValidator.validate_citations(text)
    assert len(res["detected_urls"]) >= 1
    assert len(res["detected_dois"]) >= 1
