import pytest
from springernature_api.meta import MetaAPI

@pytest.fixture
def meta_client():
    return MetaAPI(api_key="test_key")

def test_meta_search(meta_client, mocker):
    mock_response = {"records": [{"title": "Cancer Studies"}]}
    mocker.patch.object(meta_client, "search", return_value=mock_response)

    response = meta_client.search(q="cancer", p=1, s=1)
    assert "records" in response
    assert response["records"][0]["title"] == "Cancer Studies"
