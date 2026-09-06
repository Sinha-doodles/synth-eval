"""Lexical toxicity and profanity filter."""
from typing import List, Dict, Any
from syntheval.evaluators.base import BaseEvaluator

class ToxicityLexiconEvaluator(BaseEvaluator):
    BANNED_ROOTS = {"hate", "slur", "harass", "threaten", "violence"}

    @property
    def name(self) -> str:
        return "toxicity_lexicon_evaluator"

    async def evaluate(self, candidate: str, context: Dict[str, Any]) -> Dict[str, Any]:
        lowered = candidate.lower()
        matches = [root for root in self.BANNED_ROOTS if root in lowered]
        return {
            "is_toxic": len(matches) > 0,
            "detected_keywords": matches,
            "toxicity_score": 1.0 if matches else 0.0
        }
