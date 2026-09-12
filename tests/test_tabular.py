from pathlib import Path
from syntheval.pipeline.tabular_connector import TabularConnector

def test_tabular_csv(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("item_id,prompt,candidate,rater_1,rater_2\n1,p,c,pass,pass\n")
    recs = TabularConnector.read_csv(f)
    assert len(recs) == 1
    assert recs[0].ratings == {"1": "pass", "2": "pass"}
