import os
import sys
from unittest.mock import call, patch

from fastapi.testclient import TestClient
from pytest import raises

import api.routers.common_services as common_services
from api.main import app
from database.schemas import RoleListingsPydantic, User

client = TestClient(app)


@patch("api.routers.staff.db_services.get_clerk_staff")
def test_success_get_clerk_staff(mock_get_clerk_staff):
    """
    Endpoint Tested:
      - GET /api/staff/clerk
    Scenario:
      - Tests a successful GET request to get the relevant staff details information based on given clerk_id
    """
    # Provided clerk_id
    clerk_id = "user_2VyiaGNu4nOSAj7ZleHdwpoVORt"

    # Set the behavior of the mock function
    mock_get_clerk_staff.return_value = {
        "staff_id": 123456787,
        "fname": "FAUD",
        "lname": "NIZAM",
        "dept": "SALES",
        "email": "faud_nizam@all-in-one.com.sg",
        "phone": "60-03-21345678",
        "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
        "sys_role": "manager",
    }

    # Act
    response = client.get(f"/staff/clerk/{clerk_id}")
    mock_get_clerk_staff.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "staff_id": 123456787,
        "fname": "FAUD",
        "lname": "NIZAM",
        "dept": "SALES",
        "email": "faud_nizam@all-in-one.com.sg",
        "phone": "60-03-21345678",
        "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
        "sys_role": "manager",
    }, "Response body matches the expected response"


def test_unsuccessful_get_clerk_staff():
    """
    Endpoint Tested:
      - GET /api/staff/clerk
    Scenario:
      - Tests an unsuccessful GET request to get the relevant staff details information based on given clerk_id
    """
    # Provided clerk_id
    clerk_id = "uaffser_2VyiaGNu4nOSAj7ZleHdwpoVORfafaft"

    # Act
    response = client.get(f"/staff/clerk/{clerk_id}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Staff with clerk_id: '{clerk_id}' not found"
    }
