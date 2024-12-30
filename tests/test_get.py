# test_get.py
import pytest # type: ignore
import requests # type: ignore

#Test Case 1: Valid GET request with valid endpoint

def test_get_valid_endpoint(api_client):
    """
    Test GET request to the /users endpoint.
    """
    endpoint = "/users"
    response = api_client.get(endpoint)
    
    # Assertions to verify the response
    assert isinstance(response, list)  # The response should be a list (list of users)
    assert len(response) > 0  # Expecting some data in the response

#Test Case 2: Valid GET request with query parameters

def test_get_with_query_params( api_client):
    
    endpoint = "/users"
    params = {"id": 1}  # Query parameter to filter by user id
    response = api_client.get(endpoint, params=params)
    assert isinstance(response, list)  # Should return a list
    assert len(response) == 1  # Only one user should be returned with id=1
    assert response[0]["id"] == 1  # Ensure the returned user has id=1

#Test Case 3: GET request to a non-existent endpoint (404 error)

def test_get_invalid_endpoint(api_client):
    endpoint = "/nonexistent_endpoint"  # Invalid endpoint
    try:
        api_client.get(endpoint)
        assert False #Expected HTTPError, but no error was raised"
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 404  # Expecting a 404 status code

#Test Case 4: GET request with empty response

def test_get_empty_response(api_client):
    endpoint = "/posts"  # Assuming no posts for a certain condition (you could simulate that)
    params = {"userId": 999}  # User ID that likely has no posts
    response = api_client.get(endpoint, params=params)
    assert isinstance(response, list)  # Response should still be a list, even if empty
    assert len(response) == 0  # Expecting an empty list

