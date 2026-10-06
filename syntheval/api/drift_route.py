"""FastAPI router for distribution drift detection."""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from syntheval.evaluators.drift import population_stability_index

router = APIRouter(prefix="/v1/eval", tags=["drift"])

class DriftRequest(BaseModel):
    baseline_scores: List[float]
    current_scores: List[float]

@router.post("/drift")
async def evaluate_drift(req: DriftRequest):
    psi = population_stability_index(req.baseline_scores, req.current_scores)
    return {"psi": psi, "drift_detected": psi > 0.20}
