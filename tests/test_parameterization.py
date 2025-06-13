import pytest
import requests


@pytest.mark.parametrize("name, status_code", [("ValidName", 201), ("", 201), (None, 201)])
def test_create_user_param(name, status_code):
    payload = {"name": name}
    r = requests.post(
        "https://jsonplaceholder.typicode.com/users", json=payload)
    assert r.status_code == status_code, f"except 201, but code is :{status_code}"
