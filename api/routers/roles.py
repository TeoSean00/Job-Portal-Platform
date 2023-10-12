import datetime as dt
import json
from typing import Optional

from fastapi import APIRouter, Header, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import ValidationError

import api.routers.common_services as common_services
import database.services as db_services
from database.schemas import RoleListingsPydantic, User

router = APIRouter(
    prefix="/role",
    tags=["Role"],
)


@router.get("/")
def default_message():
    return {
        "role router endpoints, refer to staff router endpoints for template!"
    }


# =========================== Start: Role Details  ===========================
@router.get("/role_details")
def get_role_details(
    user_token: int = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
    role_id: int = Query(None, description="Role ID"),
):
    """
    ### Description:
    This endpoint returns either all or specific role details from the database.

    ### Parameters:
    `role_id`: Optional, if provided returns role details for specific role. Else, returns all

    `user_token`: Taken from Headers, key is `user-token`

    `role`: Taken from Headers, key is `role`,

    ### Returns:
    A JSON object containing the details of the given staff member.

    ### Example:
    #### Request:
    ```
    GET /role/role_details
    Authorization: <Clerk Token>
    user-token: "123456789"
    role: "hr"

    ```
    #### Response:
    ```
    {
     "role_details": [
        {
            "role_id": 1,
            "role_name": "Clerk",
            "role_desc": "Clerk role",
            "role_status": "active",
        }, ...
     ]
    }
    ```
    ### Errors:
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), "ADMIN"
    ):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role details for all
        if role_id is None:
            role_details = db_services.get_all_role_details()
            role_detail = []
            # For testing, since we do not return a SQLAlchemy object
            if type(role_details) == dict:
                return {"role_details": role_details}
            for item in role_details.all():
                # For some reason, common_services.convert_sqlalchemy_object_to_dict don't work for this particular object
                role_details_dict = (
                    common_services.convert_sqlalchemy_object_to_dict(item)
                )

                role_detail.append(role_details_dict)
            return {"role_details": role_detail}
        else:
            role_detail = db_services.get_role_details(role_id)
            # For testing, since we do not return a SQLAlchemy object
            if type(role_detail) == dict:
                return {"role_details": role_detail}
            if role_detail is None:
                raise HTTPException(
                    status_code=404,
                    detail={
                        "message": f"Role details with id {role_id} not found!"
                    },
                )
            # return {"role_details": json.dumps(role_detail)}
            return {
                "role_details": common_services.convert_sqlalchemy_object_to_dict(
                    role_detail
                )
            }
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message": str(e)})
    finally:
        # Close DB connection if needed
        pass


# =========================== End: Role Details  ===========================


@router.get("/role_skills")
def get_role_skills(
    user_token: int = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
    role_id: int = Query(description="Required role_id"),
):
    """
    ### Description:
    This endpoint takes in a role_id and returns the skills associated with it.
    This is meant to be used to return all skills associated with a particular role.
    Returns an empty list if no skills associated.

    ### Parameters:
    `role_id`: Specifies the role_id to get the skills for.

    `user_token`: Taken from Headers, key is `user-token`

    `role`: Taken from Headers, key is `role`  

    ### Returns:
    A JSON object containing the skills associated.

    ### Example:
    #### Request:
    ```
    GET /role/role_skills
    GET /role/role_skills?role_id=234567893
    Authorization: <Clerk Token>
    user-token: "123456789"
    role: "hr"

    ```
    #### Response:
    ```
    {
        "role_skills": [
            {
                "role_id": 234567899,
                "skill_id": 345678790
            },
            {
                "role_id": 234567899,
                "skill_id": 345678866
            }
        ]
    }
    ```
    ### Errors:
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), "ADMIN", "STAFF", "DIRECTOR"
    ):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        role_skills = db_services.get_role_skills(role_id)
        if type(role_skills) == dict:
            return {"role_skills": role_skills}
        if role_skills == None:
            raise HTTPException(
                status_code=404,
                detail={
                    "message":f"Role with id {role_id} either has no skills, or does not exist!"
                    })
        res = [common_services.convert_sqlalchemy_object_to_dict(role_skill) for role_skill in role_skills]
        
        return {"role_skills": res}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message": str(e)})
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
    user_token: int = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
    role_listing_id: int = Query(None, description="Optional role_listing_id"),
):
    """
    ### Description:
    This endpoint returns either one or all role listings in the database.

    ### Parameters:
    `role_listing_id`: Optional, returns specific listing if provided else all.

    `user_token`: Taken from Headers, key is `user-token`

    `role`: Taken from Headers, key is `role`,

    ### Returns:
    A JSON object containing the role_listing associated.

    ### Example:
    #### Request:
    ```

    GET /role/role_listing
    GET /role/role_listing?role_listing_id=0
    Authorization: <Clerk Token>
    user-token: "123456789"
    role: "hr"

    ```
    #### Response:
    ```
    {
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
            "role_listing_ts_update": "2023-10-01T15:41:52"
        }
    }
    ```
    ### Errors:
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), "ADMIN", "STAFF", "DIRECTOR"
    ):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role listing for all
        if role_listing_id is None:
            role_listings = db_services.get_all_role_listings()
            role_listing = []
            # For testing purposes
            if type(role_listings) == dict:
                return {"role_listing": role_listings}
            for item in role_listings.all():
                role_listing.append(
                    common_services.convert_sqlalchemy_object_to_dict(item)
                )
            return {"role_listing": role_listing}
        # Return role listing for specific role_listing_id
        else:
            role_listing = db_services.get_role_listings(role_listing_id)
            # For testing purposes, since cannot return SQLAlchemy object
            if type(role_listing) == dict:
                return {"role_listing": role_listing}
            if role_listing is None:
                raise HTTPException(
                    status_code=404,
                    detail={
                        "message": f"Role listing with id {role_listing_id} not found!"
                    },
                )
            return {
                "role_listing": common_services.convert_sqlalchemy_object_to_dict(
                    role_listing
                )
            }
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        print(e)
        raise HTTPException(status_code=500, detail={"message": str(e)})
    finally:
        # Close DB connection if needed
        pass


@router.post("/role_listing")
def create_role_listing(
    role_details: RoleListingsPydantic,
    user_token: int = Header(..., description="User token"),
    role: str = Header(..., description="User role"),
):
    """
    ### Description:
    This endpoint creates a role listings in the database.

    ### Parameters:
    `role_details`: JSON object, schema further down

    `user_token`: Taken from Headers, key is `user-token`

    `role`: Taken from Headers, key is `role`,

    ### Returns:
    Sampel Text

    ### Example:
    #### Request:
    ```

    POST/role/role_listing
    Authorization: <Clerk Token>
    user-token: "123456789"
    role: "hr"

    ```
    #### Response:
    ```
    ```
    ### Errors:
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Authenticate user
    if not common_services.authenticate_user(
        User(user_token=user_token, role=role), "ADMIN"
    ):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Validate form-details
        role_listing_ts_create = dt.datetime.utcnow()
        if validate_role_listing(role_details):
            data = {
                "role_id": role_details.role_id,  # Links to ID inside role details
                "role_listing_desc": role_details.role_listing_desc,
                "role_listing_source": user_token,
                "role_listing_open": common_services.convert_str_to_datetime(
                    role_details.role_listing_open
                ),
                "role_listing_close": common_services.convert_str_to_datetime(
                    role_details.role_listing_close
                ),
                "role_listing_hide": common_services.convert_str_to_datetime(
                    role_details.role_listing_hide
                ),
                "role_listing_creator": user_token,
                "role_listing_ts_create": common_services.convert_str_to_datetime(
                    role_listing_ts_create
                ),
                # "role_listing_updater": None,
                # "role_listing_ts_update": None,
                # Set the updater and update time to the creator on first occurence
                "role_listing_updater": user_token,
                "role_listing_ts_update": common_services.convert_str_to_datetime(
                    role_listing_ts_create
                ),
            }
            # Create role_listing
            db_services.create_role_listing(**data)
        else:
            raise HTTPException(
                status_code=400, detail={"message": "Invalid role details!"}
            )
        # Connect to DB and create role_listing there
        return JSONResponse(content={"message": "Created!"}, status_code=201)
    except ValidationError as e:
        raise HTTPException(
            status_code=400, detail={"message": f"{e}. Invalid role details!"}
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message": str(e)})
    finally:
        # Close db connection
        pass


# =========================== End: Role Listing  ===========================
