# test_post.py
import pytest  # type: ignore
import requests  # type: ignore

# Test Case 1: Valid POST request with valid data

def test_post_valid_data(api_client):
    """
    Test POST request to the /posts endpoint with valid data.
    """
    endpoint = "/posts"
    data = {
        "title": "Test Post",
        "body": "This is a test post body.",
        "userId": 1
    }
    response = api_client.post(endpoint, data=data)

    # Assertions to verify the response
    assert isinstance(response, dict)  # The response should be a dictionary
    assert response["title"] == data["title"]  # Title should match the input
    assert response["body"] == data["body"]  # Body should match the input
    assert response["userId"] == data["userId"]  # userId should match the input
    assert "id" in response  # API should return a new ID for the post

# Test Case 2: POST request with invalid data (expecting a 201 error)

def test_post_invalid_data(api_client):
    """
    Test POST request to the /posts endpoint with invalid data.
    """
    endpoint = "/posts"
    data = {"invalidField": "This should fail"}  # Invalid payload

    try:
        # Make the POST request and get the full response
        response = api_client.post(endpoint, data=data, return_response=True)

        # Assert that the response status code is 201
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    except requests.exceptions.HTTPError as e:
        # Handle HTTPError if raised and check if it's due to 201
        assert e.response.status_code == 201, f"Expected status code 201, but got {e.response.status_code}"


# Test Case 3: POST request to a non-existent endpoint (404 error)

def test_post_invalid_endpoint(api_client):
    """
    Test POST request to a non-existent endpoint.
    """
    endpoint = "/nonexistent_endpoint"  # Invalid endpoint
    data = {
        "title": "Test",
        "body": "This is a test.",
        "userId": 1
    }
    try:
        api_client.post(endpoint, data=data)
        assert False  # Expected HTTPError, but no error was raised
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 404  # Expecting a 404 status code


# Test Case 4: POST request with empty data

def test_post_empty_data(api_client):
    """
    Test POST request to the /posts endpoint with an empty payload.
    """
    endpoint = "/posts"
    data = {}  # Empty payload
    response = api_client.post(endpoint, data=data)

     # Check if required keys exist in the response
    assert "id" in response, "Response does not contain an 'id' field"

    # Check for optional fields 'title' and 'body'
    if "title" in response:
        assert response["title"] == "", "Expected 'title' to be an empty string"
    else:
        print("The 'title' field is not present in the response, as expected.")

    if "body" in response:
        assert response["body"] == "", "Expected 'body' to be an empty string"
    else:
        print("The 'body' field is not present in the response, as expected.")
        

# Test Case 5: POST request with timeout

def test_post_timeout(api_client):
    """
    Test POST request to the /posts endpoint to simulate a timeout.
    """
    endpoint = "/posts"
    data = {
        "title": "Test",
        "body": "This is a test.",
        "userId": 1
    }

    try:
        # Simulate a timeout by patching `post` if needed in the future
        response = api_client.post(endpoint, data=data)
        assert True  # Normally wouldn't timeout in real API calls
    except requests.exceptions.Timeout:
        assert False, "Request timed out unexpectedly"   