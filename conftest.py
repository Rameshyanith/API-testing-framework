import pytest  # type: ignore
from utils.api_client import APIClient 
from config.settings import BASE_URL

@pytest.fixture(scope="session")
def api_client():
    """
    Fixture for creating an API client.
    Returns:
        APIClient: A reusable API client instance.
    """
    return APIClient(BASE_URL)