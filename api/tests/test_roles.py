import sys
import os
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import api.routers.common_services as common_services
from fastapi.testclient import TestClient
from unittest.mock import patch, call

from api.main import app
from database.schemas import (
    User,
    RoleListingsPydantic
)

client = TestClient(app)

# =========================== Start: Role Listings  ===========================
@patch("api.routers.roles.db_services.create_role_listing")
def test_success_create_role_listing(mock_create_role_listing):
    # Arrange
    user = User(user_token=123456789, role="manager")

    role_details = RoleListingsPydantic(
        role_id= 234511581, # Existing ID
        role_listing_desc= "This role is added during testing of creating role listing",
        role_listing_source= 123456789, # Existing user ID 
        role_listing_open= "2023-10-22T16:00:00",
        role_listing_close= "2023-10-25T16:12:00",
        role_listing_hide= "2023-10-30T16:23:59",
        role_listing_creator= 123456789,
        role_listing_ts_create= "2023-10-20T16:00:00",
        role_listing_updater= 123456789,
        role_listing_ts_update= "2023-10-20T16:00:00",
    )

    # Set the behavior of the mock function
    mock_create_role_listing.return_value = {"message": "Created!"}  

    # Act
    response = client.post("/role/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})

    mock_create_role_listing.assert_called()

    assert response.status_code == 201
    assert response.json() == {"message": "Created!"}, f"Response content does not match expected JSON"

def test_unauthorized_create_role_listing():
    # Arrange
    user = User(user_token=123456789, role="invalid")
    role_details = RoleListingsPydantic(
        role_id= 234511581, # Existing ID
        role_listing_desc= "This role is added during testing of creating role listing",
        role_listing_source= 123456789, # Existing user ID 
        role_listing_open= "2023-10-22T16:00:00",
        role_listing_close= "2023-10-25T16:12:00",
        role_listing_hide= "2023-10-30T16:23:59",
        role_listing_creator= 123456789,
        role_listing_ts_create= "2023-10-20T16:00:00",
        role_listing_updater= 123456789,
        role_listing_ts_update= "2023-10-20T16:00:00",
    )

    # Act
    response = client.post("/role/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})

    # Assert
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized user!"}

def test_invalid_create_role_listing():
    user = User(user_token=123456789, role="hr")
    role_details = RoleListingsPydantic(
        role_id= 234511581, # Existing ID
        role_listing_desc= "This is an invalid role listing.",
        role_listing_source= 123456789, # Existing user ID 
        role_listing_open= "2023-10-22T16:00:00",
        role_listing_close= "2023-10-25T16:12:00",
        role_listing_hide= "2023-10-30T16:23:59",
        role_listing_creator= 123456789,
        role_listing_ts_create= "2023-10-20T16:00:00",
        role_listing_updater= 123456789,
        role_listing_ts_update= "2023-10-20T16:00:00",
    )

    # Act
    response = client.post("/role/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})
    print(response.json())
    # Assert
    assert response.status_code == 400
    assert response.json() == {'detail': {'message': 'Invalid role details!'}}
# =========================== End: Role Listings  ===========================

# =========================== Start: Role Details  ===========================

# =========================== Start: Role Listings  ===========================
@patch("api.routers.roles.db_services.get_all_role_details")
def test_success_get_role_details(mock_get_role_details):
    # Arrange
    user_token = 123456789
    role = "manager"

    # Set the behavior of the mock function
    mock_get_role_details.return_value =  {
            "role_details": [
                    {
                        "role_id": 234511581,
                        "role_name": "Fire Warden",
                        "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
                        "role_status": "active"
                    }
                ]
            }
        
    # Act
    response = client.get(f"/role/role_details?user_token={user_token}&role={role}")

    mock_get_role_details.assert_called()

    assert response.status_code == 200

@patch("api.routers.roles.db_services.get_all_role_details")
def test_success_get_role_details(mock_get_all_role_details):
    # Arrange
    user_token = 123456789
    role = "manager"

    # Set the behavior of the mock function
    mock_get_all_role_details.return_value =  {
            "role_details": [
                    {
                        "role_id": 234511581,
                        "role_name": "Fire Warden",
                        "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
                        "role_status": "active"
                    }
                ]
            }
        
    # Act
    response = client.get(f"/role/role_details?user_token={user_token}&role={role}")

    mock_get_all_role_details.assert_called()

    assert response.status_code == 200

@patch("api.routers.roles.db_services.get_role_details")
def test_success_get_role_details(mock_get_role_details):
    # Arrange
    user_token = 123456789
    role = "manager"
    role_id = 234511581

    # Set the behavior of the mock function
    mock_get_role_details.return_value =  {
        
                 
                        "role_id": 234511581,
                        "role_name": "Fire Warden",
                        "role_description": "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
                        "role_status": "active"
                 
                
            }
        
    # Act
    response = client.get(f"/role/role_details?user_token={user_token}&role={role}&role_id={role_id}")

    mock_get_role_details.assert_called()

    assert response.status_code == 200

@patch("api.routers.roles.db_services.get_role_details")
def test_role_not_exist_get_role_details(mock_get_role_details):
    # Arrange
    user_token = 123456789
    role = "manager"
    role_id = 234511581

    # Set the behavior of the mock function
    mock_get_role_details.return_value =  None        
    # Act
    response = client.get(f"/role/role_details?user_token={user_token}&role={role}&role_id={role_id}")

    mock_get_role_details.assert_called()

    assert response.status_code == 404

@patch("api.routers.roles.db_services.get_role_details")
def test_not_authorized_get_role_details(mock_get_role_details):
    # Arrange
    user_token = 123456789
    role = "invalid"
    role_id = 234511581

    response = client.get(f"/role/role_details?user_token={user_token}&role={role}&role_id={role_id}")

    assert response.status_code == 401
    assert response.json() == {'detail': 'Unauthorized user!'}

# =========================== End: Role Details  ===========================
