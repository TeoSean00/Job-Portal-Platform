from fastapi import APIRouter, Query, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import json

import datetime as dt

from typing import Optional
import api.routers.common_services as common_services
import database.services as db_services 
from database.schemas import (
    User,
    RoleListingsPydantic
)

router = APIRouter(
  prefix = "/role",
  tags = ["Role"],
)


@router.get("/")
def default_message():
    return {"role router endpoints, refer to staff router endpoints for template!"}

# =========================== Start: Role Details  ===========================
@router.get("/role_details")
def get_role_details(
    user_token: int = Query(..., description="User token"),
    role: str = Query(..., description="User role"),
    role_id: int = Query(None,  description="Role ID"),
):

    """
    End point that returns all the created role_listings inside the table.
    If a role_id is specified, only return information for that role_id
    """
    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), 
        "ADMIN"
        ):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role details for all
        if role_id == None:
            role_details = db_services.get_all_role_details()
            role_detail = []
            # For testing, since we do not return a SQLAlchemy object
            if type(role_details) == dict:
                return {"role_details": role_details}
            for item in role_details.all():
                # For some reason, json.dumps don't work for this particular object
                role_details_dict = common_services.convert_sqlalchemy_object_to_dict(item)
         
                role_detail.append(
                    role_details_dict
                )
            return {"role_details": role_detail}
        else:
            role_detail = db_services.get_role_details(role_id)
            # For testing, since we do not return a SQLAlchemy object
            if type(role_detail) == dict:
                return {"role_details": role_detail}
            if role_detail == None:
                raise HTTPException(
                    status_code=404, 
                    detail={
                        "message":f"Role details with id {role_id} not found!"
                        })
            # return {"role_details": json.dumps(role_detail)}
            return {"role_details": common_services.convert_sqlalchemy_object_to_dict(role_detail)}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass
# =========================== End: Role Details  ===========================

@router.get("/role_skills")
def get_role_skills(
    user:User,
    role_id: int = Query(description="Required role_id"),
):
    """
    End point that takes in a role ID and returns the skills associated with that role.
    """
    if not common_services.authenticate_user(user, "ADMIN", "STAFF", "DIRECTOR"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        role_skills = db_services.get_role_skill(role_id)
        if role_skills == None:
            raise HTTPException(
                status_code=404, 
                detail={
                    "message":f"Role with id {role_id} either has no skills, or does not exist!"
                    })
        return {"role_skills": json.dumps(role_skills)}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass
# =========================== End: Role Skills ===========================


# =========================== Start: Role Listing  ===========================

def validate_role_listing(role_details: RoleListingsPydantic):
    if role_details.role_listing_desc == "This is an invalid role listing.":
        return False
    return True

@router.get("/role_listing")
def get_role_listing(
    user: User,
    role_listing_id: int = Query(None, description="Optional role_listing_id"),
):
    """
    End point that takes in an optional role_listing_id and returns the role_listing.
    If role_listing_id is provided, it returns information about that ID.
    If role_listing_id is blank, it returns all role_listings.
    """
    if not common_services.authenticate_user(user, "ADMIN", "STAFF", "DIRECTOR"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role listing for all
        if role_listing_id == None:
            role_listings = db_services.get_all_role_listings()
            role_listing = []
            for item in role_listings.all():
                
                role_listing.append(
                    common_services.convert_sqlalchemy_object_to_dict(item)
                    # json.dumps(item)
                )
            return {"role_listing": role_listing}
        # Return role listing for specific role_listing_id
        else:
            role_listing = db_services.get_role_listings(role_listing_id)
            if role_listing == None:
                raise HTTPException(
                    status_code=404, 
                    detail={
                        "message":f"Role listing with id {role_listing_id} not found!"
                        })
            return {"role_listing": common_services.convert_sqlalchemy_object_to_dict(role_listing)}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass

@router.post("/role_listing")
def create_role_listing(
    user: User,
    role_details: RoleListingsPydantic
    ):
    """
    End point that takes in a role_listing, validates and creates it.
    """
    # Authenticate user 
    if not common_services.authenticate_user(user, "ADMIN"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Validate form-details
        role_listing_ts_create = dt.datetime.utcnow()
        if validate_role_listing(role_details):
            data = {
                "role_id": 234511581, # Links to ID inside role details
                "role_listing_desc": role_details.role_listing_desc,
                "role_listing_source": user.user_token,
                "role_listing_open": common_services.convert_str_to_datetime(role_details.role_listing_open),
                "role_listing_close": common_services.convert_str_to_datetime(role_details.role_listing_close),
                "role_listing_hide": common_services.convert_str_to_datetime(role_details.role_listing_hide),
                "role_listing_creator": user.user_token,
                "role_listing_ts_create": common_services.convert_str_to_datetime(role_listing_ts_create),
                # "role_listing_updater": None,
                # "role_listing_ts_update": None,
                # Set the updater and update time to the creator on first occurence
                "role_listing_updater": user.user_token,
                "role_listing_ts_update": common_services.convert_str_to_datetime(role_listing_ts_create),
            }
            # Create role_listing
            db_services.create_role_listing(**data)
        else:
            raise HTTPException(status_code=400, detail={"message":"Invalid role details!"})
        # Connect to DB and create role_listing there
        return JSONResponse(content={"message": "Created!"}, status_code=201)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail={"message":"Invalid role details!"})
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close db connection 
        pass
# =========================== End: Role Listing  ===========================