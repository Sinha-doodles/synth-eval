"""Detects degenerate repetitive generation loops and verbosity bias."""
from collections import Counter
from typing import Dict, Any

def repetition_ratio(text: str, n: int = 3) -> float:
    tokens = text.lower().split()
    if len(tokens) < n:
        return 0.0
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    unique = len(set(ngrams))
    return round(1.0 - (unique / len(ngrams)), 4)
