class APIError(Exception):
    """Base class for API-related exceptions."""
    pass

class InvalidAPIKeyError(APIError):
    """Raised when an invalid API key is used."""
    def __init__(self, message="Invalid API key provided"):
        super().__init__(message)

class RateLimitExceededError(APIError):
    """Raised when the API rate limit is exceeded."""
    def __init__(self, message="API rate limit exceeded"):
        super().__init__(message)

class APIRequestError(APIError):
    """Raised for generic API request errors."""
    def __init__(self, message="An error occurred while making an API request"):
        super().__init__(message)
