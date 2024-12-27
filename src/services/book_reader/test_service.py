import requests


def test_get_books():
    # Define the URL
    url = "http://localhost:8000/books"

    # Send the GET request
    response = requests.get(url)

    # Verify the response status code
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"

    # Verify the response body is a list
    assert isinstance(
        response.json(), list
    ), f"Response body is not a list: {response.json()}"
