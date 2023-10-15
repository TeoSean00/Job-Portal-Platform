import os
import sys
from unittest.mock import call, patch

from fastapi.testclient import TestClient

from api.main import app
from database.schemas import User

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
client = TestClient(app)
# Testing pre commit

@patch("api.routers.skills.db_services.get_all_skills")
def test_success_get_all_skills(mock_get_all_skills):
    mock_get_all_skills.return_value = [
        {
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active",
        },
        {
            "skill_id": 345678866,
            "skill_name": "Java Developer",
            "skill_status": "active",
        },
        {
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive",
        },
        {
            "skill_id": 345678912,
            "skill_name": "Pascal Programming",
            "skill_status": "inactive",
        },
    ]
    # Define headers
    headers = {"user-token": "123456789", "role": "manager"}

    response = client.get("/skill/get-all", headers=headers)
    mock_get_all_skills.assert_called()

    assert response.status_code == 200
    assert response.json() == {
        "skills": [
            {
                "skill_id": 345678790,
                "skill_name": "Typescript Developer",
                "skill_status": "active",
            },
            {
                "skill_id": 345678866,
                "skill_name": "Java Developer",
                "skill_status": "active",
            },
            {
                "skill_id": 345678890,
                "skill_name": "VMWare Villian",
                "skill_status": "inactive",
            },
            {
                "skill_id": 345678912,
                "skill_name": "Pascal Programming",
                "skill_status": "inactive",
            },
        ]
    }
