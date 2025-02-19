import pytest
from springernature_api_client.tdm import TDMAPI

@pytest.fixture
def tdm_client():
    return TDMAPI(api_key="test_key")

def test_tdm_search(tdm_client, mocker):
    mock_response = {"records": [{"title": "TDM Research"}]}
    mocker.patch.object(tdm_client, "search", return_value=mock_response)

    response = tdm_client.search(q="machine learning", p=1, s=1)
    assert "records" in response
    assert response["records"][0]["title"] == "TDM Research"
