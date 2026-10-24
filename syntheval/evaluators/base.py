"""Base abstract evaluator."""
from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseEvaluator(ABC):
    @property
    @abstractmethod
    def name(self) -> str: pass

    @abstractmethod
    async def evaluate(self, candidate: str, context: Dict[str, Any]) -> Dict[str, Any]: pass
