import pytest  # type: ignore
import requests  # type: ignore
from unittest.mock import patch, Mock

# Test Case 1: Valid DELETE request to a valid endpoint
def test_delete_valid_endpoint(api_client):
    """
    Test DELETE request to a valid endpoint.
    """
    endpoint = "/users/1"  # Assume a valid user exists with id=1
    with patch("requests.delete") as mock_delete:
        # Mock successful DELETE response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_delete.return_value = mock_response

        response_code = api_client.delete(endpoint)

        # Assertions
        assert response_code == 200  # Successful DELETE returns 200
        mock_delete.assert_called_once_with(f"{api_client.base_url}{endpoint}")

# Test Case 2: DELETE request to a non-existent endpoint (404 error)
def test_delete_invalid_endpoint(api_client):
    """
    Test DELETE request to a non-existent endpoint.
    """
    endpoint = "/nonexistent_endpoint"
    with patch("requests.delete") as mock_delete:
        # Mock 404 error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=Mock(status_code=404))
        mock_delete.return_value = mock_response

        # Expecting an HTTPError to be raised
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            api_client.delete(endpoint)
        
        assert exc_info.value.response.status_code == 404  # Ensure the exception is due to a 404
        mock_delete.assert_called_once_with(f"{api_client.base_url}{endpoint}")

# Test Case 3: DELETE request with server error (500 error)
def test_delete_server_error(api_client):
    """
    Test DELETE request that triggers a server error (500).
    """
    endpoint = "/users/1"  # Example endpoint
    with patch("requests.delete") as mock_delete:
        # Mock 500 error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=Mock(status_code=500))
        mock_delete.return_value = mock_response

        # Expecting an HTTPError to be raised
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            api_client.delete(endpoint)
        
        assert exc_info.value.response.status_code == 500  # Ensure the exception is due to a 500
        mock_delete.assert_called_once_with(f"{api_client.base_url}{endpoint}")

# Test Case 4: DELETE request to a valid endpoint but no resource to delete (204 response)
def test_delete_no_content(api_client):
    """
    Test DELETE request to an endpoint with no resource (204 No Content).
    """
    endpoint = "/users/999"  # Assume no user exists with id=999
    with patch("requests.delete") as mock_delete:
        # Mock 204 No Content response
        mock_response = Mock()
        mock_response.status_code = 204
        mock_response.raise_for_status.return_value = None
        mock_delete.return_value = mock_response

        response_code = api_client.delete(endpoint)

        # Assertions
        assert response_code == 204  # DELETE returns 204 No Content when successful
        mock_delete.assert_called_once_with(f"{api_client.base_url}{endpoint}")

# Test Case 5: DELETE request with invalid authentication (401 error)
def test_delete_unauthorized(api_client):
    """
    Test DELETE request that fails due to invalid authentication (401).
    """
    endpoint = "/users/1"
    with patch("requests.delete") as mock_delete:
        # Mock 401 Unauthorized error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=Mock(status_code=401))
        mock_delete.return_value = mock_response

        # Expecting an HTTPError to be raised
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            api_client.delete(endpoint)
        
        assert exc_info.value.response.status_code == 401  # Ensure the exception is due to a 401
        mock_delete.assert_called_once_with(f"{api_client.base_url}{endpoint}")