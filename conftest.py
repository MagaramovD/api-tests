import pytest
import requests

DEFAULT_NAME = "Din"


@pytest.fixture
def auth_token():
    response = requests.post(
        "https://api.example.com/login", json={"username": "user", "password": "pass"})
    return response.json()["token"]


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com/users"


@pytest.fixture
def default_name():
    return DEFAULT_NAME


@pytest.fixture
def saucedemo_url():
    return "https://www.saucedemo.com/"
