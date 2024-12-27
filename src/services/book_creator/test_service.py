import pytest
import requests

def test_post_books():
    # Define the URL and payload
    url = "http://localhost:9000/books"
    payload = {
        "title": "Second book",
        "authors": ["Someone"],
        "isbn": "978-00-00-00-00-00",
        "genres": ["Fiction"],
        "published_date": "2019-01-10",
        "summary": "Second book"
    }

    # Define the expected response
    expected_response = {
        "message": "Book created successfully"
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    # Verify the response status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Verify the response body
    assert response.json() == expected_response, f"Unexpected response body: {response.json()}"
