import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from a .env file if available
load_dotenv()

API_KEY = os.getenv("SPRINGERNATURE_API_KEY", "your_default_api_key_here")

def set_api_key(api_key):
    """Dynamically set API Key if needed."""
    global API_KEY
    API_KEY = api_key
