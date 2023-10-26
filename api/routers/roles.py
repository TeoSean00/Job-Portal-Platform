import datetime as dt
import json
from collections import defaultdict
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


# =========================== Master: Get Roles  ===========================
@router.get("/role_listings_info")
def get_role_info(
    role: str = Header(..., description="User role"),
):
    """
    Description: This endpoint is a compiled end point that returns all information about all role_listings in the database.

    Parameters:
    - role: Taken from Headers, key is `role`.

    Returns:
    A JSON object containing the details of role_listings.

    Errors:
    - 500 Internal Server Error: Generic server error that can occur for various reasons.

    Example Request:
    ```
    GET /role/role_details
    Authorization: <Clerk Token>
    role: "hr"
    ```

    Example Response:
    ```
        {
        "2": {
        "role_id": 234567899,
        "role_listing_desc": "Role Listing 234567899 Description",
        "role_listing_source": 123456787,
        "role_listing_open": "2023-09-16T00:00:00",
        "role_listing_close": "2023-10-05T00:00:00",
        "role_listing_hide": "2023-10-29T00:00:00",
        "role_listing_creator": 123456787,
        "role_listing_ts_create": "2023-09-22T14:38:42",
        "role_listing_updater": 123456787,
        "role_listing_ts_update": "2023-09-22T14:38:42",
        "role_department": "Group Technology",
        "role_location": "Front Office, Hong Kong SAR",
        "role_name": "Butcher",
        "role_desc": "added by elton on 22/9/23 10.12pm to fix fk constraints",
        "role_status": "active",
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
                "skill_id": 345678922,
                "skill_name": "React Beast",
                "skill_status": "active"
            }
        ]
    },
    }
    ```
    """
    try:
        if not common_services.authenticate_user(role):
            raise HTTPException(status_code=401, detail="Unauthorized user!")
        (
            role_listing_results,
            role_skills_details,
        ) = db_services.get_all_role_listings_info()
        response = process_roles_info(
            role_listing_results, role_skills_details
        )
        return response
    except HTTPException as e:
        raise e


def process_roles_info(role_listing_results, role_skills_details):
    """
    This works for both single and multiple info,
    since there might multiple skills for a single role.
    """
    if role_skills_details is None:
        return {}
    skills = defaultdict(list)
    for row in role_skills_details:
        role_details, row_skills, skills_details = row
        role_id = role_details.role_id
        skills[role_id].append(
            {
                "skill_id": row_skills.skill_id,
                "skill_name": skills_details.skill_name,
                "skill_status": skills_details.skill_status,
            }
        )

    response = {}
    for row in role_listing_results:
        role_listings, role_details = row
        id = role_listings.role_listing_id
        response[id] = {
            "role_id": role_details.role_id,
            "role_listing_desc": role_listings.role_listing_desc,
            "role_listing_source": role_listings.role_listing_source,
            "role_listing_open": role_listings.role_listing_open,
            "role_listing_close": role_listings.role_listing_close,
            "role_listing_hide": role_listings.role_listing_hide,
            "role_listing_creator": role_listings.role_listing_creator,
            "role_listing_ts_create": role_listings.role_listing_ts_create,
            "role_listing_updater": role_listings.role_listing_updater,
            "role_listing_ts_update": role_listings.role_listing_ts_update,
            "role_department": role_listings.role_department,
            "role_location": role_listings.role_location,
            "role_name": role_details.role_name,
            "role_desc": role_details.role_description,
            "role_status": role_details.role_status,
            "skills": skills[role_details.role_id],
        }
    return response


# =========================== Start: Role Details  ===========================


@router.get("/role_details")
def get_role_details(
    role: str = Header(..., description="User role"),
    role_id: int = Query(None, description="Role ID"),
):
    """
    ### Description:
    This endpoint returns either all or specific role details from the database.

    ### Parameters:
    `role`: Taken from Headers, expected values are hr, manager, staff or invalid
    `role_id`: Optional, if provided returns role details for a specific role. If not specifed, returns all.

    ### Returns:
    A JSON object with the key "role_details" that contains a list of all
    role details in the database or just one role details if role_id is specified.
    Noted that if specified role_id, response is double nested role_details.

    ### Example:
    #### Request:
    ```
    GET /role/role_details
    GET /role/role_details?role_id=1
    Authorization: <Clerk Token>
    role: "hr"
    ```
    #### Response:
    {
        "role_details": [
            {
                "role_id": 1,
                "role_name": "Clerk",
                "role_desc": "Clerk role",
                "role_status": "active"
            },
            ...
        ]
    }
    ```
    ### Errors:
    `401 Unauthorized`: User is not authorized to access this endpoint.<br /><br />
    `404 Not Found: No role details matching the given role details ID found in the system.
    `500 Internal Server Error: Generic server error that can occur for various reasons.
    """
    try:
        # Authenticate user
        if not common_services.authenticate_user(role):
            raise HTTPException(status_code=401, detail="Unauthorized user!")

        if role_id is None:
            role_details = db_services.get_all_role_details()
            role_detail = process_role_details(role_details)
        else:
            role_detail = db_services.get_role_details(role_id)
            role_detail = process_single_role_detail(role_detail, role_id)

        return {"role_details": role_detail}

    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": str(e)})


def process_role_details(role_details):
    if isinstance(role_details, dict):
        return role_details

    processed_role_details = []
    for item in role_details.all():
        processed_role_details.append(
            common_services.convert_sqlalchemy_object_to_dict(item)
        )
    return processed_role_details


def process_single_role_detail(role_detail, role_id):
    if isinstance(role_detail, dict):
        return role_detail

    if role_detail is None:
        raise HTTPException(
            status_code=404,
            detail={"message": f"Role details with id {role_id} not found!"},
        )

    return {
        "role_details": common_services.convert_sqlalchemy_object_to_dict(
            role_detail
        )
    }


# =========================== End: Role Details  ===========================


@router.get("/role_skills")
def get_role_skills(
    role: str = Header(..., description="User role"),
    role_id: int = Query(description="Required role_id"),
):
    """
    ### Description:
    This endpoint takes in a role_id and returns the skills associated with it.
    This is meant to be used to return all skills associated with a particular role.
    Returns an empty list if no skills associated or if the role does NOT exist.

    ### Parameters:
    `role`: Taken from Headers, expected values are hr, manager, staff or invalid
    `role_id`: Specifies the role_id to get the skills for.

    ### Returns:
    A JSON object with the key "role_skills" that contains a list of all
    skills details associated with the role_id.

    ### Example:
    #### Request:
    ```
    GET /role/role_skills
    GET /role/role_skills?role_id=234567893
    Authorization: <Clerk Token>
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
    `401 Unauthorized`: User is not authorized to access this endpoint.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Authenticate user
    if not common_services.authenticate_user(role):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        role_skills = db_services.get_role_skills(role_id)
        if isinstance(role_skills, dict):
            return {"role_skills": role_skills}
        if role_skills is None:
            raise HTTPException(
                status_code=404,
                detail={
                    "message": f"Role with id {role_id} either has no skills, or does not exist!"
                },
            )
        res = [
            common_services.convert_sqlalchemy_object_to_dict(role_skill)
            for role_skill in role_skills
        ]

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
    role: str = Header(..., description="User role"),
    role_listing_id: int = Query(None, description="Optional role_listing_id"),
):
    """
    ### Description:
    This endpoint returns either one or all role listings in the database.

    ### Parameters:
    `role`: Taken from Headers, expected values are hr, manager, staff or invalid
    `role_listing_id`: Optional, returns specific listing if provided else all.

    ### Returns:
    A JSON object with the key "role_listing" that contains a list of all
    roles_listings in the database.
    If a role_listing_id is specified, keep in mind that response will be
    double nested with "role_listing" key.

    ### Example:
    #### Request:
    ```
    GET /role/role_listing
    GET /role/role_listing?role_listing_id=31251332
    Authorization: <Clerk Token>
    role: "hr"
    ```
    #### Response:
    {
        "role_listing": {
            "role_listing_id": 0,
            ...
        }
    }
    ```
    ### Errors:
    `401 Unauthorized`: User is not authorized to access this endpoint.<br /><br />
    `404 Not Found`: No role details matching the given role details ID found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons.<br /><br />
    """
    try:
        if not common_services.authenticate_user(role):
            raise HTTPException(status_code=401, detail="Unauthorized user!")

        if role_listing_id is None:
            role_listings = db_services.get_all_role_listings()
            role_listing = process_role_listings(role_listings)
        else:
            role_listing = db_services.get_role_listings(role_listing_id)
            role_listing = process_single_role_listing(
                role_listing, role_listing_id
            )

        return {"role_listing": role_listing}

    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": str(e)})


def process_role_listings(role_listings):
    if isinstance(role_listings, dict):
        return role_listings

    processed_role_listings = []
    for item in role_listings.all():
        processed_role_listings.append(
            common_services.convert_sqlalchemy_object_to_dict(item)
        )
    return processed_role_listings


def process_single_role_listing(role_listing, role_listing_id):
    if isinstance(role_listing, dict):
        return role_listing

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


@router.post("/role_listing")
def create_role_listing(
    role_listing_details: RoleListingsPydantic,
    role: str = Header(..., description="User role"),
):
    """
    ### Description:
    This endpoint creates a role listings in the database.

    ### Parameters:
    `role`: Taken from Headers, expected values are hr, manager, staff or invalid
    `role_details`: JSON object containing the required details

    ### Returns:
    Status code 201 if successful, "message" : "Created!".

    ### Example:
    #### Request:
    ```
    POST/role/role_listing
    Authorization: <Clerk Token>
    role: "hr"
    ```
    #### Body:
    {
        "role_listing_id": 312513332,
        "role_id": 234511581,
        "role_listing_desc": "This is death",
        "role_listing_source": 123456786,
        "role_listing_open": "2023-10-22T16:00:00",
        "role_listing_creator": 123456786,
        "role_department": "Tech Support",
        "role_location": "Down Under"
    }
    ```
    #### Response:
    {
        "message": "Created!"
    }
    ### Errors:
    `401 Unauthorized`: User is not authorized to access this endpoint.<br /><br />
    TODO: Work on more detailed error handling for this.
    `500 Internal Server Error`: Generic server error, can be due to role details not being found, integrity issue.<br /><br />
    """
    # Authenticate user
    if not common_services.authenticate_user(role):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Validate form-details
        role_listing_ts_create = dt.datetime.utcnow()
        if validate_role_listing(role_listing_details):
            data = {
                "role_listing_id": role_listing_details.role_listing_id,
                "role_id": role_listing_details.role_id,  # Links to ID inside role details
                "role_listing_desc": role_listing_details.role_listing_desc,
                "role_listing_source": role_listing_details.role_listing_source,
                "role_listing_open": common_services.convert_str_to_datetime(
                    role_listing_details.role_listing_open
                ),
                "role_listing_close": common_services.add_days_to_str_datetime(
                    role_listing_details.role_listing_open, 14
                ),
                "role_listing_hide": common_services.add_days_to_str_datetime(
                    role_listing_details.role_listing_hide, 14
                ),
                "role_listing_creator": role_listing_details.role_listing_creator,
                "role_listing_ts_create": common_services.convert_str_to_datetime(
                    role_listing_ts_create
                ),
                "role_listing_updater": None,
                "role_listing_ts_update": None,
                "role_department": role_listing_details.role_department,
                "role_location": role_listing_details.role_location,
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
