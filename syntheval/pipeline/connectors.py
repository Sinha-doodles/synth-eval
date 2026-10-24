"""Dataset connectors."""
import json
from pathlib import Path
from typing import List, Union
from syntheval.core.schemas import AnnotationRecord, PairwisePreference

class DatasetConnector:
    @staticmethod
    def read_jsonl(path: Union[str, Path]) -> List[AnnotationRecord]:
        records = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    records.append(AnnotationRecord.model_validate(json.loads(line)))
        return records
