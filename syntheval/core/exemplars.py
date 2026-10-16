"""Dynamic few-shot exemplar builder."""
from typing import List, Dict

class ExemplarBuilder:
    def __init__(self):
        self.exemplars: List[Dict[str, str]] = []

    def add(self, query: str, gold: str):
        self.exemplars.append({"query": query, "gold": gold})

    def render(self) -> str:
        return "\n".join(f"Q: {e['query']}\nA: {e['gold']}" for e in self.exemplars)
