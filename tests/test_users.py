import pytest
from tests.helpers.api.reqres_api_utility import ReqResApiUtility
from tests.helpers.api import constants


# Fixture for reqres client
@pytest.fixture
def client():
    # Creates ReqResApiUtility which creates its own HttpClient internally
    return ReqResApiUtility(base_url=constants.BASE_URL, timeout=constants.TEST_TIMEOUT)


# GET USER TESTS

@pytest.mark.smoke
def test_get_existing_user(client):
    response = client.get_user(2)
    
    assert "data" in response
    assert response["data"]["id"] == 2
    assert response["data"]["email"].endswith("@reqres.in")


def test_get_user_that_does_not_exist(client):
    # Try to get a user that doesn't exist - should fail
    with pytest.raises(Exception):
        client.get_user(999)


# LIST USERS TESTS

@pytest.mark.smoke
def test_list_users(client):
    response = client.list_users()
    
    assert "page" in response
    assert response["page"] == 1
    assert "data" in response
    assert isinstance(response["data"], list)
    assert len(response["data"]) > 0


# CREATE USER TESTS

@pytest.mark.smoke
def test_create_user(client, sample_user_data):
    response = client.create_user(
        name=sample_user_data["name"],
        job=sample_user_data["job"]
    )
    
    assert "id" in response
    assert response["name"] == sample_user_data["name"]
    assert response["job"] == sample_user_data["job"]
    assert "createdAt" in response


# UPDATE USER TESTS

@pytest.mark.smoke
def test_update_user(client, sample_user_update_data):
    # create a user first
    created_user = client.create_user(name="Original Name", job="Original Job")
    user_id = created_user.get("id") or 1
    
    # update it
    updated_user = client.update_user(user_id, sample_user_update_data)
    
    assert updated_user["name"] == sample_user_update_data["name"]
    assert updated_user["job"] == sample_user_update_data["job"]
    assert "updatedAt" in updated_user


# DELETE USER TESTS

@pytest.mark.smoke
def test_delete_user(client):
    # need to create one first
    created_user = client.create_user(name="User To Delete", job="Delete Job")
    user_id = created_user.get("id") or 1
    
    delete_response = client.delete_user(user_id)
    
    # 200 or 204 means it worked
    assert delete_response.status_code in (200, 204)


# COMPLETE FLOW TESTS

@pytest.mark.integration
def test_create_update_delete_user_flow(client):
    # create
    created_user = client.create_user(name="Workflow User", job="Workflow Job")
    user_id = created_user.get("id") or 1
    assert "id" in created_user
    
    # update
    updated_user = client.update_user(user_id, {"name": "Updated Name", "job": "Updated Job"})
    assert updated_user["name"] == "Updated Name"
    assert "updatedAt" in updated_user
    
    # delete
    delete_response = client.delete_user(user_id)
    assert delete_response.status_code in (200, 204)

