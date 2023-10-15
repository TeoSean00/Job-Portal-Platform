import os
import sys
from unittest.mock import call, patch

from fastapi.testclient import TestClient

import api.routers.common_services as common_services
from api.main import app
from database.schemas import RoleListingsPydantic, User

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
client = TestClient(app)


# =========================== Start: Role Listings  ===========================
@patch("api.routers.roles.db_services.create_role_listing")
def test_success_create_role_listing(mock_create_role_listing):
    """
    Endpoint Tested:
        POST /role/role_listing
    Scenario:
        Tests a successful, authorized POST request to create a role listing.
    """
    role_details = {
        "role_id": 234511581,  # Existing ID
        "role_name": "Pokemon",
        "role_listing_desc": "Additional Description",
        "role_listing_source": 123456,
        "role_listing_open": "2023-10-22T16:00:00",
        "role_listing_close": "2023-10-25T16:00:00",
        "role_listing_hide": "2023-10-25T16:00:00",
        "role_listing_creator": 123123,
        "role_listing_updater": 2,
    }

    # Define headers
    headers = {"user-token": "123456789", "role": "hr"}

    # Set the behavior of the mock function
    mock_create_role_listing.return_value = {"message": "Created!"}

    # Act
    response = client.post(
        "/role/role_listing", json=role_details, headers=headers
    )
    mock_create_role_listing.assert_called()

    assert response.status_code == 201
    assert response.json() == {
        "message": "Created!"
    }, "Response content does not match expected JSON"


def test_unauthorized_create_role_listing():
    """
    Endpoint Tested:
        POST /role/role_listing
    Scenario:
        Tests a unauthorized POST request to create a role listing.
    """
    role_details = {
        "role_id": 234511581,  # Existing ID
        "role_name": "Pokemon",
        "role_listing_desc": "Additional Description",
        "role_listing_source": 123456,
        "role_listing_open": "2023-10-22T16:00:00",
        "role_listing_close": "2023-10-25T16:00:00",
        "role_listing_hide": "2023-10-25T16:00:00",
        "role_listing_creator": 123123,
        "role_listing_updater": 2,
    }

    # Define headers
    headers = {"user-token": "123456789", "role": "invalid"}

    response = client.post(
        "/role/role_listing", json=role_details, headers=headers
    )

    # Assert
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized user!"}


def test_invalid_create_role_listing():
    """
    Endpoint Tested:
        POST /role/role_listing
    Scenario:
        Tests a authorized POST request to create a role listing where role details
        are no valid.
    """
    role_details = {
        "role_id": 234511581,  # Existing ID
        "role_name": "Pokemon",
        "role_listing_desc": "This is an invalid role listing.",
        "role_listing_source": 123456,
        "role_listing_open": "2023-10-22T16:00:00",
        "role_listing_close": "2023-10-25T16:00:00",
        "role_listing_hide": "2023-10-25T16:00:00",
        "role_listing_creator": 123123,
        "role_listing_updater": 2,
    }

    # Define headers
    headers = {"user-token": "123456789", "role": "hr"}

    response = client.post(
        "/role/role_listing", json=role_details, headers=headers
    )
    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": {"message": "Invalid role details!"}}


# Get Role Listings
@patch("api.routers.roles.db_services.get_all_role_listings")
def test_success_get_all_role_listings(mock_get_all_role_listings):
    """
    Endpoint Tested:
        GET /role/role_listing
    Scenario:
        Tests a authorized GET request to get all role listings.
    """
    # Define headers
    mock_get_all_role_listings.return_value = {
        "role_listing": [
            {
                "role_listing_id": 0,
                "role_id": 234511581,
                "role_listing_desc": "Additional Description",
                "role_listing_source": 123456789,
                "role_listing_open": "2023-10-22T16:00:00",
                "role_listing_close": "2023-10-25T16:00:00",
                "role_listing_hide": "2023-10-25T16:00:00",
                "role_listing_creator": 123456789,
                "role_listing_ts_create": "2023-10-01T15:41:52",
                "role_listing_updater": 123456789,
                "role_listing_ts_update": "2023-10-01T15:41:52",
            },
            {
                "role_listing_id": 1,
                "role_id": 234567891,
                "role_listing_desc": "Role Listing 123456789 Description",
                "role_listing_source": 123456787,
                "role_listing_open": "2023-09-15T00:00:00",
                "role_listing_close": "2023-10-22T00:00:00",
                "role_listing_hide": "2023-10-29T00:00:00",
                "role_listing_creator": 123456787,
                "role_listing_ts_create": "2023-09-22T14:38:42",
                "role_listing_updater": 123456787,
                "role_listing_ts_update": "2023-09-22T14:38:42",
            },
            {
                "role_listing_id": 2,
                "role_id": 234567899,
                "role_listing_desc": "Role Listing 234567899 Description",
                "role_listing_source": 123456787,
                "role_listing_open": "2023-09-16T00:00:00",
                "role_listing_close": "2023-10-05T00:00:00",
                "role_listing_hide": "2023-10-29T00:00:00",
                "role_listing_creator": 123456787,
                "role_listing_ts_create": "2023-09-22T14:38:42",
                "role_listing_updater": 123456787,
                "role_listing_ts_update": "2023-09-22T14:38:42",
            },
        ]
    }

    headers = {"user-token": "123456789", "role": "hr"}

    response = client.get("/role/role_listing", headers=headers)
    print(response.json())
    mock_get_all_role_listings.assert_called()

    assert response.status_code == 200


@patch("api.routers.roles.db_services.get_role_listings")
def test_success_get_role_listings(mock_get_role_listings):
    """
    Endpoint Tested:
        GET /role/role_listing?role_listing_id=0
    Scenario:
        Tests a authorized GET request to get a particular role listings.
    """
    # Define headers
    mock_get_role_listings.return_value = {
        "role_listing": {
            "role_listing_id": 0,
            "role_id": 234511581,
            "role_listing_desc": "Additional Description",
            "role_listing_source": 123456789,
            "role_listing_open": "2023-10-22T16:00:00",
            "role_listing_close": "2023-10-25T16:00:00",
            "role_listing_hide": "2023-10-25T16:00:00",
            "role_listing_creator": 123456789,
            "role_listing_ts_create": "2023-10-01T15:41:52",
            "role_listing_updater": 123456789,
            "role_listing_ts_update": "2023-10-01T15:41:52",
        }
    }

    headers = {"user-token": "123456789", "role": "hr"}

    response = client.get(
        "/role/role_listing?role_listing_id=0", headers=headers
    )
    mock_get_role_listings.assert_called()

    assert response.status_code == 200


@patch("api.routers.roles.db_services.get_role_listings")
def test_failure_role_listing_not_exist(mock_get_role_listings):
    """
    Endpoint Tested:
        GET /role/role_listing?role_listing_id=0
    Scenario:
        Tests a authorized GET request to get an non existing role listing.
    Expected Status Code:
        404
    """
    # Define headers
    mock_get_role_listings.return_value = None

    headers = {"user-token": "123456789", "role": "hr"}

    response = client.get(
        "/role/role_listing?role_listing_id=0", headers=headers
    )
    mock_get_role_listings.assert_called()

    assert response.status_code == 404


def test_failure_not_authorized_get_role_listings():
    """
    Endpoint Tested:
        GET /role/role_listing
    Scenario:
        Tests a unauthorized GET request to get role listing.
    Expected Status Code:
        401
    """
    # Define headers
    headers = {"user-token": "123456789", "role": "invalid"}

    response = client.get(
        "/role/role_listing?role_listing_id=0", headers=headers
    )

    assert response.status_code == 401


# =========================== End: Role Listings  ===========================


# =========================== Start: Role Details  ===========================
@patch("api.routers.roles.db_services.get_all_role_details")
def test_success_get_all_role_details(mock_get_all_role_details):
    """
    Endpoint Tested:
        GET /role/role_details
    Scenario:
        Tests a authorized GET request to get role details.
    Expected Status Code:
        200
    """
    # Set the behavior of the mock function
    mock_get_all_role_details.return_value = {
        "role_details": [
            {
                "role_id": 234511581,
                "role_name": "Fire Warden",
                "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
                "role_status": "active",
            }
        ]
    }

    # Define headers
    headers = {"user-token": "123456789", "role": "manager"}

    response = client.get("/role/role_details", headers=headers)

    mock_get_all_role_details.assert_called()

    assert response.status_code == 200


@patch("api.routers.roles.db_services.get_role_details")
def test_success_get_role_details(mock_get_role_details):
    """
    Endpoint Tested:
        GET /role/role_details?role_id=234511581
    Scenario:
        Tests a authorized GET request to get specific role details.
    Expected Status Code:
        200
    """
    # Set the behavior of the mock function
    mock_get_role_details.return_value = {
        "role_details": [
            {
                "role_id": 234511581,
                "role_name": "Fire Warden",
                "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
                "role_status": "active",
            }
        ]
    }
    # Define headers
    headers = {"user-token": "123456789", "role": "manager"}

    response = client.get(
        "/role/role_details?role_id=234511581", headers=headers
    )

    mock_get_role_details.assert_called()

    assert response.status_code == 200


@patch("api.routers.roles.db_services.get_role_details")
def test_failure_role_not_exist_get_role_details(mock_get_role_details):
    """
    Endpoint Tested:
        GET /role/role_details?role_id=234511581
    Scenario:
        Tests a authorized GET request to get non existing role details.
    Expected Status Code:
        404
    """
    # Set the behavior of the mock function
    mock_get_role_details.return_value = None
    # Define headers
    headers = {"user-token": "123456789", "role": "manager"}
    # Act
    response = client.get("/role/role_details?role_id=123", headers=headers)

    mock_get_role_details.assert_called()

    assert response.status_code == 404


def test_not_authorized_get_role_details():
    """
    Endpoint Tested:
        GET /role/role_details
    Scenario:
        Tests a unauthorized GET request to get role details.
    Expected Status Code:
        401
    """
    # Arrange
    headers = {"user-token": "123456789", "role": "invalid"}
    response = client.get("/role/role_details", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized user!"}


@patch("api.routers.roles.db_services.get_role_skills")
def test_success_get_role_skills(mock_get_role_skills):
    """
    Endpoint Tested:
        GET /role/role_skills?role_id=23456789
    Scenario:
        Tests a successful GET request to get role details.
    Expected Status Code:
        200
    """
    mock_get_role_skills.return_value = {
        "role_skills": [
            {"role_id": 234567899, "skill_id": 345678790},
            {"role_id": 234567899, "skill_id": 345678866},
        ]
    }

    headers = {"user-token": "123456789", "role": "hr"}

    response = client.get(
        f"/role/role_skills?role_id=23456789", headers=headers
    )

    assert response.status_code == 200


def test_unauthorized_get_role_skills():
    """
    Endpoint Tested:
        GET /role/role_skills?role_id=23456789
    Scenario:
        Tests an GET request to get role details.
    Expected Status Code:
        200
    """

    headers = {"user-token": "123456789", "role": "invalid"}

    response = client.get(
        f"/role/role_skills?role_id=23456789", headers=headers
    )

    # Assert
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized user!"}


# =========================== End: Role Details  ===========================
