"""Domain schemas and contracts using Pydantic v2."""
from typing import List, Dict, Any, Optional, Literal, Union
from datetime import datetime, timezone
from pydantic import BaseModel, Field, ConfigDict

class AnnotationRecord(BaseModel):
    model_config = ConfigDict(extra="ignore")
    item_id: str
    prompt: Optional[str] = None
    candidate_text: Optional[str] = None
    ground_truth: Optional[str] = None
    ratings: Dict[str, Union[str, int, float]] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AgreementResult(BaseModel):
    metric_name: str
    coefficient: float = Field(..., ge=-1.0, le=1.0)
    num_items: int
    num_raters: int
    confidence_interval_95: Optional[tuple[float, float]] = None
    interpretation: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class HallucinationScore(BaseModel):
    claim_count: int
    supported_claims: int
    unsupported_claims: int
    faithfulness_ratio: float = Field(..., ge=0.0, le=1.0)
    flagged_hallucinations: List[str] = Field(default_factory=list)
    confidence: float = Field(..., ge=0.0, le=1.0)

class PairwisePreference(BaseModel):
    prompt: str
    completion_a: str
    completion_b: str
    chosen: Literal["A", "B", "tie"]
    rater_id: Optional[str] = None
    rationale: Optional[str] = None
    confidence: float = Field(1.0, ge=0.0, le=1.0)

class EvaluationJob(BaseModel):
    job_id: str
    status: Literal["pending", "processing", "completed", "failed"] = "pending"
    total_records: int = 0
    processed_records: int = 0
    agreement_summary: Optional[Dict[str, Any]] = None
    hallucination_summary: Optional[Dict[str, Any]] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    error: Optional[str] = None
