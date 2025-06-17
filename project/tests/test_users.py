import requests
import pytest

from conftest import DEFAULT_NAME


def test_get_users(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]


def test_create_user(base_url):
    payload_create = {"name": DEFAULT_NAME}
    response = requests.post(
        base_url, json=payload_create)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    data = response.json()
    assert data["name"] == DEFAULT_NAME, f"Expected name {DEFAULT_NAME}, but got{data}"


def test_update_user():
    payload_update = {"name": f"Updated {DEFAULT_NAME}"}
    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1", json=payload_update)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data[
        "name"] == "Updated Din", f"Expected name Updated {DEFAULT_NAME}, but got {data.get('name')}"


def test_delete_user():
    payload_delete = {"name": DEFAULT_NAME}
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/users/1", json=payload_delete)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_get_users_negative():
    response = requests.get("https://jsonplaceholder.typicode.com/notusers")
    assert response.status_code == 404
    try:
        data = response.json()
        assert data == {}, f"Expected empty dict, got {data}"
    except ValueError:
        pytest.fail("Expected JSON, got invalid format")


def test_login_with_wrong_credentials():
    payload = {"email": "wrong@example.com", "password": "wrongpassword"}
    r = requests.post("https://reqres.in/api/login", json=payload)
    assert r.status_code in {
        400, 401}, f"Expected 400 or 401, but it was {r.status_code}"

    data = r.json()
    assert "error" in data, f"Expected 'error' in repsonce body, got {data}"
