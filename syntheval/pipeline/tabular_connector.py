"""Tabular connector for CSV and TSV annotation datasets."""
import csv
from pathlib import Path
from typing import List
from syntheval.core.schemas import AnnotationRecord

class TabularConnector:
    @staticmethod
    def read_csv(file_path: Path, delimiter: str = ",") -> List[AnnotationRecord]:
        records: List[AnnotationRecord] = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                item_id = row.get("item_id", "item-auto")
                prompt = row.get("prompt")
                candidate = row.get("candidate")
                ground_truth = row.get("ground_truth")
                ratings = {k.replace("rater_", ""): v for k, v in row.items() if k.startswith("rater_")}
                records.append(AnnotationRecord(
                    item_id=item_id,
                    prompt=prompt,
                    candidate_text=candidate,
                    ground_truth=ground_truth,
                    ratings=ratings
                ))
        return records
