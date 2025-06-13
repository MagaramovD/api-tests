import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com/users"
DEFAULT_NAME = "Din"


@pytest.fixture
def auth_token():
    response = requests.post(
        "https://api.example.com/login", json={"username": "user", "password": "pass"})
    return response.json()["token"]


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def default_name():
    return DEFAULT_NAME
