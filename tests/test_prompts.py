from syntheval.core.prompts import PromptTemplates
from syntheval.core.exemplars import ExemplarBuilder

def test_prompts():
    assert "judge" in PromptTemplates.NLI_SYSTEM
    eb = ExemplarBuilder()
    eb.add("2+2?", "4")
    assert "Q: 2+2?" in eb.render()
