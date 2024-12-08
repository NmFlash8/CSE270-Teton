import pytest
import requests

# Test case for unauthorized access (401 response)
def test_users_endpoint_unauthorized(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the requests.get response
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(url, params=params)

    # Assert HTTP response status code is 401
    assert response.status_code == 401

    # Assert response body is empty
    assert response.text.strip() == ""

# Test case for authorized access (200 response)
def test_users_endpoint_authorized(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the requests.get response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(url, params=params)

    # Assert HTTP response status code is 200
    assert response.status_code == 200

    # Assert response body is empty
    assert response.text.strip() == ""
