import pytest
from springernature_api.exceptions import (
    APIError,
    InvalidAPIKeyError,
    RateLimitExceededError,
    APIRequestError,
)

def test_api_error():
    with pytest.raises(APIError, match="Base API Error"):
        raise APIError("Base API Error")

def test_invalid_api_key_error():
    with pytest.raises(InvalidAPIKeyError, match="Invalid API key provided"):
        raise InvalidAPIKeyError()

def test_invalid_api_key_error_custom_message():
    with pytest.raises(InvalidAPIKeyError, match="Custom invalid key message"):
        raise InvalidAPIKeyError("Custom invalid key message")

def test_rate_limit_exceeded_error():
    with pytest.raises(RateLimitExceededError, match="API rate limit exceeded"):
        raise RateLimitExceededError()

def test_rate_limit_exceeded_error_custom_message():
    with pytest.raises(RateLimitExceededError, match="Rate limit reached!"):
        raise RateLimitExceededError("Rate limit reached!")

def test_api_request_error():
    with pytest.raises(APIRequestError, match="An error occurred while making an API request"):
        raise APIRequestError()

def test_api_request_error_custom_message():
    with pytest.raises(APIRequestError, match="Network failure"):
        raise APIRequestError("Network failure")
