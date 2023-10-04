import sys
import os
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from fastapi.testclient import TestClient
from unittest.mock import patch, call

from api.main import app
from database.schemas import (
    User,
)

client = TestClient(app)

@patch("api.routers.skills.db_services.get_all_skill_names")
def test_success_create_role_listing(mock_get_all_skill_names):
    user = User(user_token=123456789, role="staff")

    mock_get_all_skill_names.return_value = "Hello"
    mock_get_all_skill_names.return_value = [
        {
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active"
        },
        {
            "skill_id": 345678866,
            "skill_name": "Java Developer",
            "skill_status": "active"
        },
        {
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive"
        },
        {
            "skill_id": 345678912,
            "skill_name": "Pascal Programming",
            "skill_status": "inactive"
        }
    ]
    print(user.user_token, user.role)
    response = client.get("/skill/get-all", params={"user_token": user.user_token, "role": "staff"})
    print("Response here is !")
    print(response, response.text)
    mock_get_all_skill_names.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "skills": [
        {
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active"
        },
        {
            "skill_id": 345678866,
            "skill_name": "Java Developer",
            "skill_status": "active"
        },
        {
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive"
        },
        {
            "skill_id": 345678912,
            "skill_name": "Pascal Programming",
            "skill_status": "inactive"
        }
    ]
    }