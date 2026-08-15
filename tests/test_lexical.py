from syntheval.metrics.lexical import rouge_n, bleu_score

def test_rouge_bleu():
    c = "transformers enable deep language models"
    r = "transformers enable language models"
    assert rouge_n(c, r, n=1)["f1"] > 0.70
    assert bleu_score(c, r) > 0.30
