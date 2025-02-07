import requests
from .config import API_KEY
from .exceptions import APIRequestError, RateLimitExceededError, InvalidAPIKeyError
from .logging_config import logger

class SpringerNatureAPI:
    BASE_URL = "https://api.springernature.com/"
    TDM_BASE_URL = "https://spdi.public.springernature.app/"

    def __init__(self, api_key=None):
        """Initialize API with user-provided API key (or use default from config)"""
        self.api_key = api_key or API_KEY
        if not self.api_key:
            raise InvalidAPIKeyError("No API key provided.")

    def _make_request(self, endpoint: str, fetch_all: bool = False, is_tdm: bool = False, **params):
        """Handles API requests and pagination dynamically"""
        params["api_key"] = self.api_key
        base_url = self.TDM_BASE_URL if is_tdm else self.BASE_URL  # Select base URL based on is_tdm
        url = f"{base_url}{endpoint}"
        all_results = []

        while True:
            try:
                logger.info(f"Making request to: {url} with params: {params}")
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                logger.debug(f"Response received: {data}")

                all_results.extend(data.get("records", []))

                # Check for API rate limiting
                if response.status_code == 429:
                    raise RateLimitExceededError("API rate limit exceeded. Try again later.")

                # If pagination is enabled, check for "nextPage"
                if fetch_all and "nextPage" in data:
                    url = f"{base_url}{data['nextPage']}"  # Ensure correct base URL for pagination
                    params = {}  # Reset params as they are included in nextPage
                    logger.info(f"Next page found, new URL: {url}")
                else:
                    break  # Stop if pagination is disabled or no nextPage link is found
            except requests.exceptions.Timeout:
                logger.warning("Request timed out. Retrying...")
            except requests.exceptions.RequestException as e:
                logger.error(f"API Error: {e}")
                raise APIRequestError(str(e)) from e
        
        return {"records": all_results}
