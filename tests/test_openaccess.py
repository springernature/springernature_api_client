import pytest
from springernature_api.openaccess import OpenAccessAPI

@pytest.fixture
def openaccess_client():
    return OpenAccessAPI(api_key="test_key")

def test_openaccess_search(openaccess_client, mocker):
    mock_response = {"records": [{"title": "Open Access Research"}]}
    mocker.patch.object(openaccess_client, "search", return_value=mock_response)

    response = openaccess_client.search(q="AI", p=1, s=1)
    assert "records" in response
    assert response["records"][0]["title"] == "Open Access Research"
