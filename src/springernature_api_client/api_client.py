import requests
import time
import random
from .config import API_KEY
from .exceptions import APIRequestError, RateLimitExceededError, InvalidAPIKeyError
from .logging_config import logger

class SpringerNatureAPI:
    BASE_URL = "https://api.springernature.com/"
    TDM_BASE_URL = "https://spdi.public.springernature.app/"

    def __init__(self, api_key=None, max_retries=5, backoff_factor=1):
        """Initialize API with user-provided API key (or use default from config)"""
        self.api_key = api_key or API_KEY
        self.max_retries = max_retries  # Maximum number of retries
        self.backoff_factor = backoff_factor  # Factor to control wait time scaling

        if not api_key:
            raise InvalidAPIKeyError("No API key provided.")

    def _make_request(self, endpoint: str, fetch_all: bool = False, is_tdm: bool = False, **params):
        """Handles API requests with proper retry logic and pagination"""
        params["api_key"] = self.api_key
        base_url = self.TDM_BASE_URL if is_tdm else self.BASE_URL
        url = f"{base_url}{endpoint}"
        all_results = []

        retries = 0  # Track retry attempts

        while True:
            try:
                logger.info(f"Making request to: {url} with params: {params}")
                response = requests.get(url, params=params, timeout=10)
                
                if response.status_code == 429:
                    if retries >= self.max_retries:
                        raise RateLimitExceededError("API rate limit exceeded. Max retries reached.")
                    
                    retry_after = int(response.headers.get("Retry-After", 2))  # Default to 2 sec
                    wait_time = min(self.backoff_factor * (2 ** retries) + random.uniform(0, 1), 60)
                    logger.warning(f"Rate limit hit. Retrying in {retry_after} seconds...")
                    time.sleep(retry_after)
                    retries += 1
                    continue  # Retry request after delay
                
                response.raise_for_status()
                data = response.json()
                logger.debug(f"Response received: {data}")

                all_results.extend(data.get("records", []))
                
                # If pagination is enabled and nextPage exists, continue fetching
                if fetch_all and "nextPage" in data:
                    url = f"{base_url}{data['nextPage']}"
                    params = {}
                    logger.info(f"Next page found, new URL: {url}")
                else:
                    break  # Exit loop if no pagination

            except requests.exceptions.Timeout:
                if retries >= self.max_retries:
                    logger.error("Max retries reached. Request failed.")
                    raise APIRequestError("Request timed out after multiple attempts.")
                
                wait_time = min(self.backoff_factor * (2 ** retries) + random.uniform(0, 1), 60)
                logger.warning(f"Request timed out. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
                retries += 1
                continue

            except requests.exceptions.RequestException as e:
                logger.error(f"API Error: {e}")
                raise APIRequestError(str(e)) from e
        
        return {"records": all_results}
