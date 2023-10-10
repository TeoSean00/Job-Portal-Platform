from fastapi import APIRouter, Query, HTTPException, Header
from typing import List

import api.routers.common_services as common_services
import api.routers.common_services as common_services
import database.services as db_services 
from database.schemas import (
    User,
    SkillDetailsPydantic
)

router = APIRouter(
  prefix = "/skill",
  tags = ["Skill"],
)


@router.get("/")
def default_message():
    return {"skill router endpoints, refer to staff router endpoints for template!"}

@router.get("/get-all")
def get_all_skills(
    user_token: int = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
):
    """
    End point that returns all skills inside skills table.
    """

    if not common_services.authenticate_user(            
            User(user_token=user_token, role=role),
            "STAFF"
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
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass 
    

