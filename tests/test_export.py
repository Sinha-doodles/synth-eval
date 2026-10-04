from syntheval.core.export import export_all_schemas

def test_export(tmp_path):
    export_all_schemas(tmp_path)
    assert (tmp_path / "AnnotationRecord.schema.json").exists()
