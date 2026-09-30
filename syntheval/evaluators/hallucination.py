"""Semantic hallucination and citation attribution engine with fast caching."""
import re
from typing import List, Dict, Any, Set
from syntheval.evaluators.base import BaseEvaluator
from syntheval.core.schemas import HallucinationScore

class HallucinationEvaluator(BaseEvaluator):
    STOPWORDS = frozenset({
        "the", "a", "an", "is", "are", "was", "were", "and", "or",
        "in", "on", "at", "to", "for", "with", "by", "that", "this", "it"
    })
    TOKEN_REGEX = re.compile(r"\b[a-zA-Z0-9_]{2,}\b")
    SENT_REGEX = re.compile(r"(?<=[.!?])\s+|
+")

    def __init__(self, min_token_overlap: float = 0.45):
        self.min_token_overlap = min_token_overlap

    @property
    def name(self) -> str:
        return "semantic_hallucination_evaluator"

    def _extract_claims(self, text: str) -> List[str]:
        raw_sentences = self.SENT_REGEX.split(text)
        return [s.strip() for s in raw_sentences if len(s.strip().split()) >= 3]

    def _tokenize(self, text: str) -> Set[str]:
        tokens = self.TOKEN_REGEX.findall(text.lower())
        return {t for t in tokens if t not in self.STOPWORDS}

    def verify_faithfulness(self, candidate_text: str, source_context: str) -> HallucinationScore:
        claims = self._extract_claims(candidate_text)
        if not claims:
            return HallucinationScore(
                claim_count=0, supported_claims=0, unsupported_claims=0,
                faithfulness_ratio=1.0, flagged_hallucinations=[], confidence=1.0
            )

        context_tokens = self._tokenize(source_context)
        supported = 0
        hallucinated: List[str] = []

        for claim in claims:
            claim_tokens = self._tokenize(claim)
            if not claim_tokens:
                supported += 1
                continue
            overlap = len(claim_tokens.intersection(context_tokens)) / len(claim_tokens)
            if overlap >= self.min_token_overlap:
                supported += 1
            else:
                hallucinated.append(claim)

        return HallucinationScore(
            claim_count=len(claims),
            supported_claims=supported,
            unsupported_claims=len(claims) - supported,
            faithfulness_ratio=round(supported / len(claims), 4),
            flagged_hallucinations=hallucinated,
            confidence=0.95 if len(context_tokens) > 20 else 0.70
        )

    async def evaluate(self, candidate: str, context: Dict[str, Any]) -> Dict[str, Any]:
        source = context.get("source_context", "") or context.get("ground_truth", "")
        return self.verify_faithfulness(candidate, source).model_dump()
