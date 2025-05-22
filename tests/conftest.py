import os
import pytest
import requests
from dotenv import load_dotenv
from utils.api_client import ApiClient

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def auth_token(base_url):
    payload = {
        "username": os.getenv("ADMIN_USER"),
        "password": os.getenv("ADMIN_PW")
    }
    response = requests.post(f"{base_url}/auth", json=payload)
    assert response.status_code == 200, "Failed to obtain token"
    return response.json()["token"]


@pytest.fixture(scope="session")
def api_client(base_url):
    return ApiClient(base_url)
