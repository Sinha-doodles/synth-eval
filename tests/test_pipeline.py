import pytest
from syntheval.core.schemas import AnnotationRecord
from syntheval.pipeline.orchestrator import EvaluationOrchestrator

@pytest.mark.asyncio
async def test_orch():
    orch = EvaluationOrchestrator()
    recs = [AnnotationRecord(item_id="1", ratings={"r1": "A", "r2": "A"})]
    job = await orch.run_batch_evaluation(recs)
    assert job.status == "completed"
