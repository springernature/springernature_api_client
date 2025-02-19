import pytest
from springernature_api_client.metadata import MetadataAPI

@pytest.fixture
def metadata_client():
    return MetadataAPI(api_key="test_key")

def test_metadata_search(metadata_client, mocker):
    mock_response = {"records": [{"title": "Bitcoin Research"}]}
    mocker.patch.object(metadata_client, "search", return_value=mock_response)

    response = metadata_client.search(q="bitcoin", p=1, s=1)
    assert "records" in response
    assert response["records"][0]["title"] == "Bitcoin Research"
