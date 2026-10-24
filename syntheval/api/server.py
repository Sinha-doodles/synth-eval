"""FastAPI server."""
from fastapi import FastAPI
from typing import List
from syntheval.core.schemas import AnnotationRecord, AgreementResult, HallucinationScore
from syntheval.metrics.agreement import krippendorff_alpha
from syntheval.evaluators.hallucination import HallucinationEvaluator

app = FastAPI(title="SynthEval API", version="0.2.0")
h_eval = HallucinationEvaluator()

@app.get("/healthz")
async def health(): return {"status": "healthy"}

@app.post("/v1/eval/agreement")
async def agreement(records: List[AnnotationRecord]) -> AgreementResult:
    return krippendorff_alpha(records)

@app.post("/v1/eval/hallucination")
async def hallucination(candidate: str, source: str) -> HallucinationScore:
    return h_eval.verify_faithfulness(candidate, source)
