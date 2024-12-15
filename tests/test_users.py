import pytest # type: ignore

def test_get_all_users(api_client):
    """
    Test that all users are retrieved successfully.
    """
    users = api_client.get("/users")

    assert len(users) == 10  # JSONPlaceholder has 10 users by default
    assert "id" in users[0] # Check if 'id' is a key in the response
    assert "name" in users[0] # Check if 'name' is a key in the response
    assert "username" in users[0] # Check if 'username' is a key in the response
    assert "email" in users[0] # Check if 'email' is a key in the response

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

