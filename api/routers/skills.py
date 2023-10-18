from typing import List

from fastapi import APIRouter, Header, HTTPException, Query

import api.routers.common_services as common_services
import database.services as db_services
from database.schemas import SkillDetailsPydantic, User

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
    user_token: str = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
):
    """
    ### Description:
    This endpoint returns all unique skills in the database.

    ### Parameters:

    `user_token`: Taken from Headers, key is `user-token`

    `role`: Taken from Headers, key is `role`,

    ### Returns:
    {
        "skills": [
            {
                "skill_id": 345678790,
                "skill_name": "Typescript Developer",
                "skill_status": "active"
            }, ...
    }

    ### Example:
    #### Request:
    ```

    GET /skill/get-all
    Authorization: <Clerk Token>
    user-token: "123456789"
    role: "hr"

    ```
    ```
    ### Errors:
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """

    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), "STAFF"
    ):
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
