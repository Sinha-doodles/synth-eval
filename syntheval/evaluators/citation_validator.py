"""Validates citation formatting, URL structure, and academic DOIs."""
import re
from typing import List, Dict, Any

class CitationValidator:
    DOI_REGEX = re.compile(r"10.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
    URL_REGEX = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")

    @classmethod
    def validate_citations(cls, text: str) -> Dict[str, Any]:
        urls = cls.URL_REGEX.findall(text)
        dois = cls.DOI_REGEX.findall(text)
        return {
            "detected_urls": urls,
            "detected_dois": dois,
            "citation_count": len(urls) + len(dois),
            "is_grounded": len(urls) + len(dois) > 0
        }
