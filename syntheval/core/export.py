"""Exports Pydantic domain models to JSON Schema files."""
import json
from pathlib import Path
from syntheval.core.schemas import AnnotationRecord, AgreementResult, HallucinationScore

def export_all_schemas(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    models = [AnnotationRecord, AgreementResult, HallucinationScore]
    for m in models:
        path = output_dir / f"{m.__name__}.schema.json"
        path.write_text(json.dumps(m.model_json_schema(), indent=2), encoding="utf-8")
