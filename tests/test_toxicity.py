import pytest
from syntheval.evaluators.toxicity import ToxicityLexiconEvaluator

@pytest.mark.asyncio
async def test_toxicity():
    ev = ToxicityLexiconEvaluator()
    res = await ev.evaluate("This is safe educational content.", {})
    assert res["is_toxic"] is False
    res2 = await ev.evaluate("Expressions of hate are prohibited.", {})
    assert res2["is_toxic"] is True
