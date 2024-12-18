import pytest # type: ignore
import re

def test_get_all_users(api_client):
    """
    Test that all users are retrieved successfully.
    """
    users = api_client.get("/users")

    assert isinstance(users, list)#Response should be a list of users
    assert len(users) == 10  # JSONPlaceholder has 10 users by default

    for user in users:
       assert "id" in user # Check if 'id' is a key in the response
       assert "name" in user # Check if 'name' is a key in the response
       assert "username" in user # Check if 'username' is a key in the response
       assert "email" in user # Check if 'email' is a key in the response

       # Validate key types
       assert isinstance(user["id"], int) #"'id' should be an integer, but got {type(user['id'])}: {user}"
       assert isinstance(user["name"], str) #"'name' should be a string, but got {type(user['name'])}: {user}"
       assert isinstance(user["username"], str) #"'username' should be a string, but got {type(user['username'])}: {user}"
       assert isinstance(user["email"], str) #"'email' should be a string, but got {type(user['email'])}: {user}"

@pytest.mark.parametrize("user_id,expected_name",[
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])    

def test_get_user_by_id(api_client,user_id,expected_name):
    """
    Test that a user can be retrieved by their ID.
    """
    users = api_client.get(f"/users/{user_id}")
    assert users ["id"]== user_id
    assert users ["name"]== expected_name

def test_get_nonexistent_user(api_client):
    """
    Test that fetching a non-existent user returns a 404 error.
    """
    # JSONPlaceholder has only 10 users; IDs > 10 should return a 404 error
    with pytest.raises(Exception) as excinfo:
        api_client.get("/users/11")

    # Assertions
    assert "404 Client Error" in str(excinfo.value) #Expected 404 error for non-existent user

def test_all_user_emails_have_valid_format(api_client):
    """
    Test that all users retrieved from the API have valid email formats.
    """
    users = api_client.get("/users")
    email_regex = r"[^@]+@[^@]+\.[^@]+"

    for user in users:
        assert "email" in user #"User {user['id']} is missing an email field"
        assert re.match(email_regex, user["email"]) #"Invalid email format: {user['email']}"

def test_get_user_invalid_id(api_client):
    """
    Test that an invalid user ID returns a client error.
    """
    # Call the API client with an invalid user ID
    with pytest.raises(Exception) as excinfo:
        api_client.get("/users/abc")

    # Assertions
    assert "404 Client Error" in str(excinfo.value) #Expected 404 error for invalid user ID"
