"""GSM8K mathematical reasoning verification."""
import re

class GSM8KVerifier:
    @staticmethod
    def extract_final_number(solution: str) -> str:
        matches = re.findall(r"####\s*(-?\d+(?:\.\d+)?)", solution)
        return matches[-1] if matches else ""
