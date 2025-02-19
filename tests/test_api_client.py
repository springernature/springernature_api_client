import pytest
from springernature_api_client.api_client import SpringerNatureAPI

@pytest.fixture
def api_client():
    return SpringerNatureAPI(api_key="test_key")

def test_api_key_not_provided():
    with pytest.raises(Exception, match="No API key provided."):
        SpringerNatureAPI(api_key=None)

def test_api_request(api_client, mocker):
    mock_response = {"records": [{"title": "API Response"}]}
    mocker.patch.object(api_client, "_make_request", return_value=mock_response)

    response = api_client._make_request(endpoint="metadata")
    assert "records" in response
    assert response["records"][0]["title"] == "API Response"
