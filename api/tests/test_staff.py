import os
import sys
from unittest.mock import call, patch

from fastapi.testclient import TestClient
from pytest import raises

import api.routers.common_services as common_services
from api.main import app
from database.schemas import RoleListingsPydantic, User

client = TestClient(app)


# Unit tests for get_clerk_staff endpoint
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


# Unit tests for get_all_staff endpoint
@patch("api.routers.staff.db_services.get_all_staff_details")
def test_success_get_all_staff(mock_get_all_staff):
    """
    Endpoint Tested:
      - GET /staff
    Scenario:
      - Tests a successful GET request to get all staff details
    """
    # Set the behavior of the mock function
    mock_get_all_staff.return_value = [
        {
            "staff_id": 123456786,
            "fname": "TEST",
            "lname": "USER",
            "dept": "IT",
            "email": "John_doe@ all-in-one.com.sg",
            "phone": "65-5824-7888",
            "biz_address": "1 Scotts Rd, #24-10 Shaw Centre, Singapore 228208",
            "sys_role": "hr",
        },
        {
            "staff_id": 123456787,
            "fname": "FAUD",
            "lname": "NIZAM",
            "dept": "SALES",
            "email": "faud_nizam@all-in-one.com.sg",
            "phone": "60-03-21345678",
            "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
            "sys_role": "manager",
        },
        {
            "staff_id": 123456788,
            "fname": "VINCENT REX",
            "lname": "COLINS",
            "dept": "HUMAN RESOURCE AND ADMIN",
            "email": "colins_vincent_rex@all-in-one.com.sg",
            "phone": "65-1234-5679",
            "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
            "sys_role": "hr",
        },
        {
            "staff_id": 123456789,
            "fname": "AH GAO",
            "lname": "TAN",
            "dept": "FINANCE",
            "email": "tan_ah_gao@all-in-one.com.sg",
            "phone": "65-1234-5678",
            "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
            "sys_role": "staff",
        },
    ]

    # Act
    response = client.get("/staff")
    mock_get_all_staff.assert_called()

    assert response.status_code == 200
    assert response.json() == [
        {
            "staff_id": 123456786,
            "fname": "TEST",
            "lname": "USER",
            "dept": "IT",
            "email": "John_doe@ all-in-one.com.sg",
            "phone": "65-5824-7888",
            "biz_address": "1 Scotts Rd, #24-10 Shaw Centre, Singapore 228208",
            "sys_role": "hr",
        },
        {
            "staff_id": 123456787,
            "fname": "FAUD",
            "lname": "NIZAM",
            "dept": "SALES",
            "email": "faud_nizam@all-in-one.com.sg",
            "phone": "60-03-21345678",
            "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
            "sys_role": "manager",
        },
        {
            "staff_id": 123456788,
            "fname": "VINCENT REX",
            "lname": "COLINS",
            "dept": "HUMAN RESOURCE AND ADMIN",
            "email": "colins_vincent_rex@all-in-one.com.sg",
            "phone": "65-1234-5679",
            "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
            "sys_role": "hr",
        },
        {
            "staff_id": 123456789,
            "fname": "AH GAO",
            "lname": "TAN",
            "dept": "FINANCE",
            "email": "tan_ah_gao@all-in-one.com.sg",
            "phone": "65-1234-5678",
            "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
            "sys_role": "staff",
        },
    ], "Response body matches the expected response"


# Unit tests for get_all_managers endpoint
@patch("api.routers.staff.db_services.get_all_manager_details")
def test_success_get_all_managers(mock_get_all_manager):
    """
    Endpoint Tested:
      - GET /staff/manager
    Scenario:
      - Tests a successful GET request to get all manager details
    """
    # Set the behavior of the mock function
    mock_get_all_manager.return_value = [
        {
            "staff_id": 123456787,
            "fname": "FAUD",
            "lname": "NIZAM",
            "dept": "SALES",
            "email": "faud_nizam@all-in-one.com.sg",
            "phone": "60-03-21345678",
            "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
            "sys_role": "manager",
        }
    ]

    # Act
    response = client.get("/staff/manager")
    mock_get_all_manager.assert_called()

    assert response.status_code == 200
    assert response.json() == [
        {
            "staff_id": 123456787,
            "fname": "FAUD",
            "lname": "NIZAM",
            "dept": "SALES",
            "email": "faud_nizam@all-in-one.com.sg",
            "phone": "60-03-21345678",
            "biz_address": "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
            "sys_role": "manager",
        }
    ], "Response body matches the expected response"


# Unit tests for get_staff endpoint
@patch("api.routers.staff.db_services.get_staff_details")
def test_success_get_staff(mock_get_staff):
    """
    Endpoint Tested:
      - GET /staff/{staff_id}
    Scenario:
      - Tests a successful GET request to get staff details based on given staff_id
    """
    # Provided staff_id
    staff_id = 123456789

    # Set the behavior of the mock function
    mock_get_staff.return_value = {
        "staff_id": 123456789,
        "fname": "AH GAO",
        "lname": "TAN",
        "dept": "FINANCE",
        "email": "tan_ah_gao@all-in-one.com.sg",
        "phone": "65-1234-5678",
        "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
        "sys_role": "staff",
    }

    # Act
    response = client.get(f"/staff/{staff_id}")
    mock_get_staff.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "staff_id": 123456789,
        "fname": "AH GAO",
        "lname": "TAN",
        "dept": "FINANCE",
        "email": "tan_ah_gao@all-in-one.com.sg",
        "phone": "65-1234-5678",
        "biz_address": "60 Paya Lebar Rd, #06-33 Paya Lebar Square, Singapore 409051",
        "sys_role": "staff",
    }, "Response body matches the expected response"


def test_unsuccessful_get_staff():
    """
    Endpoint Tested:
      - GET /staff/{staff_id}
    Scenario:
      - Tests an unsuccessful GET request to get staff details based on given staff_id
    """
    # Provided staff_id
    staff_id = 1234567891234

    # Act
    response = client.get(f"/staff/{staff_id}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Staff with staff_id: '{staff_id}' not found"
    }


# Unit tests for get_staff_skills endpoint
@patch("api.routers.staff.db_services.get_staff_skill")
def test_success_get_staff_skill(mock_get_staff_skill):
    """
    Endpoint Tested:
      - GET /staff/skills/{staff_id}
    Scenario:
      - Tests a successful GET request to get staff skills based on given staff_id
    """
    # Provided staff_id
    staff_id = 123456789

    # Set the behavior of the mock function
    mock_get_staff_skill.return_value = [
        {
            "staff_id": 123456789,
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678866,
            "skill_name": "Java Developer",
            "skill_status": "active",
            "ss_status": "active",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive",
            "ss_status": "unverified",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678912,
            "skill_name": "Pascal Programming",
            "skill_status": "inactive",
            "ss_status": "active",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678927,
            "skill_name": "LinkedIn Master",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678935,
            "skill_name": "MongoDB Maniac",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
    ]

    # Act
    response = client.get(f"/staff/skills/{staff_id}")
    mock_get_staff_skill.assert_called()

    assert response.status_code == 200
    assert response.json() == [
        {
            "staff_id": 123456789,
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678866,
            "skill_name": "Java Developer",
            "skill_status": "active",
            "ss_status": "active",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive",
            "ss_status": "unverified",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678912,
            "skill_name": "Pascal Programming",
            "skill_status": "inactive",
            "ss_status": "active",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678927,
            "skill_name": "LinkedIn Master",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678935,
            "skill_name": "MongoDB Maniac",
            "skill_status": "active",
            "ss_status": "in-progress",
        },
    ], "Response body matches the expected response"


def test_unsuccessful_get_staff_skills():
    """
    Endpoint Tested:
      - GET /staff/skills/{staff_id}
    Scenario:
      - Tests an unsuccessful GET request to get staff skills based on given staff_id
    """
    # Provided staff_id
    staff_id = 12345678912312414

    # Act
    response = client.get(f"/staff/skills/{staff_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Staff with staff_id: '{staff_id}' does not exist in the system"
    }


# Unit tests for get_staff_role_listing_skills_match endpoint
@patch("api.routers.staff.db_services.get_staff_role_skills_match")
def test_success_get_staff_role_skills_match(mock_get_staff_role_skills_match):
    """
    Endpoint Tested:
      - GET /staff/role-skills-match/{staff_id}/{role_listing_id}
    Scenario:
      - Tests a successful GET request to get the matches and mismatches between staff skills and given role_listing required skills
    """
    # Provided role_id
    staff_id = 123456789
    role_listing_id = 312

    # Set the behavior of the mock function
    mock_get_staff_role_skills_match.return_value = {
        "match": {
            "active": [
                {
                    "skill_id": 345678866,
                    "skill_name": "Java Developer",
                    "skill_status": "active",
                    "ss_status": "active",
                }
            ],
            "in_progress": [
                {
                    "skill_id": 345678790,
                    "skill_name": "Typescript Developer",
                    "skill_status": "active",
                    "ss_status": "in-progress",
                }
            ],
            "unverified": [],
        },
        "missing": [
            {
                "skill_id": 345678922,
                "skill_name": "React Beast",
                "skill_status": "active",
            }
        ],
    }

    # Act
    response = client.get(
        f"/staff/role-skills-match/{staff_id}/{role_listing_id}"
    )
    mock_get_staff_role_skills_match.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "match": {
            "active": [
                {
                    "skill_id": 345678866,
                    "skill_name": "Java Developer",
                    "skill_status": "active",
                    "ss_status": "active",
                }
            ],
            "in_progress": [
                {
                    "skill_id": 345678790,
                    "skill_name": "Typescript Developer",
                    "skill_status": "active",
                    "ss_status": "in-progress",
                }
            ],
            "unverified": [],
        },
        "missing": [
            {
                "skill_id": 345678922,
                "skill_name": "React Beast",
                "skill_status": "active",
            }
        ],
    }, "Response body matches the expected response"


def test_unsuccessful_get_staff_role_skills_match():
    """
    Endpoint Tested:
      - GET /staff/role-skills-match/{staff_id}/{role_listing_id}
    Scenario:
      - Tests an unsuccessful GET request to get the matches and mismatches between staff skills and given role_listing required skills
    """
    # Provided role_id
    staff_id = 123456789
    role_listing_id = 312312313

    # Act
    response = client.get(
        f"/staff/role-skills-match/{staff_id}/{role_listing_id}"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system."
    }


# Unit tests for get_staff_role_listing_application endpoint
@patch("api.routers.staff.db_services.get_staff_role_application")
def test_success_get_staff_role_application(mock_get_staff_role_application):
    """
    Endpoint Tested:
      - GET /staff/role/{staff_id}/{role_listing_id}
    Scenario:
      - Tests a successful GET request to get the application status of a staff for a given role_listing
    """
    # Provided role_id
    staff_id = 123456789
    role_listing_id = 312

    # Set the behavior of the mock function
    mock_get_staff_role_application.return_value = {
        "role_app_status": "applied",
        "role_app_id": 10,
        "role_listing_id": 312,
        "staff_id": 123456789,
        "role_app_ts_create": "2023-10-30T04:52:25",
    }

    # Act
    response = client.get(f"/staff/role/{staff_id}/{role_listing_id}")
    mock_get_staff_role_application.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "role_app_status": "applied",
        "role_app_id": 10,
        "role_listing_id": 312,
        "staff_id": 123456789,
        "role_app_ts_create": "2023-10-30T04:52:25",
    }


def test_unsuccessful_get_staff_role_application():
    """
    Endpoint Tested:
      - GET /staff/role/{staff_id}/{role_listing_id}
    Scenario:
      - Tests an unsuccessful GET request to get the application status of a staff for a given role_listing
    """
    # Provided role_id
    staff_id = 123456789
    role_listing_id = 312312313

    # Act
    response = client.get(f"/staff/role/{staff_id}/{role_listing_id}")

    assert response.status_code == 404
    assert response.json() == {
        "detail": f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system."
    }
