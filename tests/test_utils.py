import pytest
import pandas as pd
import os
from springernature_api.utils import results_to_dataframe

@pytest.fixture
def sample_results():
    return {
        "records": [
            {"id": 1, "title": "Cancer Research", "author": "John Doe"},
            {"id": 2, "title": "Genetics Study", "author": "Jane Smith"},
        ]
    }

@pytest.fixture
def empty_results():
    return {"records": []}

def test_results_to_dataframe_valid(sample_results):
    df = results_to_dataframe(sample_results)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 2
    assert list(df.columns) == ["id", "title", "author"]

def test_results_to_dataframe_empty(empty_results, capsys):
    df = results_to_dataframe(empty_results)

    assert isinstance(df, pd.DataFrame)
    assert df.empty

    captured = capsys.readouterr()
    assert "⚠️ No records found. DataFrame is empty." in captured.out

def test_results_to_dataframe_export_to_excel(sample_results):
    filename = "test_output.xlsx"
    
    df = results_to_dataframe(sample_results, export_to_excel=True, filename=filename)
    
    assert os.path.exists(filename)
    assert isinstance(df, pd.DataFrame)
    
    os.remove(filename)
