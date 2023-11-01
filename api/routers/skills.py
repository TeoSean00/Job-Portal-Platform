from typing import List

from fastapi import APIRouter, Header, HTTPException, Query

import api.database.services as db_services
import api.routers.common_services as common_services
from api.database.schemas import SkillDetailsPydantic, User

router = APIRouter(
    prefix="/skill",
    tags=["Skill"],
)


@router.get("/")
def default_message():
    return {
        "skill router endpoints, refer to staff router endpoints for template!"
    }


@router.get("/get-all")
def get_all_skills(
    role: str = Header(..., description="User role"),
):
    """
    ### Description:
    This endpoint returns all unique skills in the database.

    ### Parameters:

    `role`: Taken from Headers, expected values are hr, manager, staff or invalid

    ### Returns:
    A JSON object with the key "skills" that contains a list of all
    unique skills details in the database.

    ### Example:
    #### Request:
    ```
    GET /skill/get-all
    Authorization: <Clerk Token>
    role: "hr"
    ```
    #### Response:
    {
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
            }
        ]
    }
    ```
    ### Errors:
    `401 Unauthorized`: User is not logged in or invalid token<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """

    if not common_services.authenticate_user(role):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        skills = db_services.get_all_skills()
        skill_list = []
        if len(skills) > 0:
            for obj in skills:
                skill_list.append(obj)
        return {"skills": skill_list}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message": str(e)})
    finally:
        # Close DB connection if needed
        pass
