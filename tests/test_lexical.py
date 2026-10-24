from syntheval.metrics.lexical import rouge_n, bleu_score

def test_rouge_bleu():
    c = "transformers enable deep language models"
    r = "transformers enable deep language models"
    assert rouge_n(c, r, n=1)["f1"] == 1.0
    assert bleu_score(c, r, max_n=2) == 1.0
