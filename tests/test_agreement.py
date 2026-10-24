from syntheval.metrics.agreement import cohen_kappa, fleiss_kappa, krippendorff_alpha, gwet_ac1
from syntheval.core.schemas import AnnotationRecord

def test_cohen(): assert cohen_kappa(["A", "B"], ["A", "B"]) == 1.0
def test_fleiss():
    recs = [AnnotationRecord(item_id="1", ratings={"r1": "A", "r2": "A"})]
    assert fleiss_kappa(recs).coefficient == 1.0
def test_krippendorff():
    recs = [AnnotationRecord(item_id="1", ratings={"r1": "A", "r2": "A"})]
    assert krippendorff_alpha(recs).coefficient == 1.0
def test_gwet(): assert gwet_ac1(["A", "B"], ["A", "B"]) == 1.0
