import pytest  # type: ignore
import requests  # type: ignore

# Test Case 1: Valid PUT request to update a resource
def test_put_valid_request(api_client):
    """
    Test a valid PUT request to update a resource.
    """
    endpoint = "/posts/1"  # Valid endpoint to update post with ID 1
    data = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = api_client.put(endpoint, data=data)

    # Assertions
    assert isinstance(response, dict)  # Response should be a dictionary
    assert response["title"] == "Updated Title"  # Verify the updated title
    assert response["body"] == "Updated Body"  # Verify the updated body
    assert response["userId"] == 1  # Ensure userId remains the same
    assert response["id"] == 1  # ID should remain unchanged

# Test Case 2: PUT request with empty data
def test_put_empty_data(api_client):
    """
    Test a PUT request with empty data payload.
    """
    endpoint = "/posts/1"  # Valid endpoint to update post with ID 1
    response = api_client.put(endpoint, data={})  # Empty payload

    # Assertions
    assert isinstance(response, dict)  # Response should still be a dictionary
    assert response["id"] == 1  # ID should remain unchanged
    # Depending on API behavior, check if fields are cleared or unchanged

# Test Case 3: PUT request to a non-existent resource (404 error)
def test_put_invalid_endpoint(api_client):
    """
    Test a PUT request to a non-existent endpoint.
    """
    endpoint = "/nonexistent_endpoint"  # Invalid endpoint
    data = {"title": "This won't work"}
    
    # Expecting a 404 error
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api_client.put(endpoint, data=data)
    
    # Assertions
    assert excinfo.value.response.status_code == 404  # Verify 404 status code

# Test Case 4: PUT request with incomplete data
def test_put_incomplete_data(api_client):
    """
    Test a PUT request with only some fields provided in the payload.
    """
    endpoint = "/posts/1"  # Valid endpoint to update post with ID 1
    data = {"title": "Partially Updated Title"}  # Only the title is provided

    response = api_client.put(endpoint, data=data)

    # Assertions
    assert isinstance(response, dict)  # Response should be a dictionary
    assert response["title"] == "Partially Updated Title"  # Title should be updated
    # Check that other fields remain unchanged (behavior depends on API)
    #assert "body"  in response  # Verify 'body' is still present
    assert response["id"] == 1  # ID should remain unchanged

def test_put_invalid_data_format(api_client):
    """
    Test a PUT request with an invalid data format (e.g., non-dict payload).
    """
    endpoint = "/posts/1"  # Valid endpoint to update post with ID 1
    data = "Invalid payload"  # Invalid format (string instead of dictionary)

    # Expecting HTTPError due to server-side error
    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.put(endpoint, data=data)

    # Validate the server's response
    assert e.value.response.status_code == 500  # Expecting 500 Internal Server Error
