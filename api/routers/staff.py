import json
from typing import List

from fastapi import APIRouter, HTTPException

import database.services as db_services
from database.database import SessionLocal
from database.models import StaffDetails
from database.schemas import (
    MatchResult,
    RoleApplicationsPydantic,
    StaffDetailsPydantic,
    StaffSkillsPydantic,
)

router = APIRouter(
    prefix="/staff",
    tags=["Staff"],
)

mock_data = [
    {
        "staff_id": 123,
        "fname": "John",
        "lname": "Doe",
        "dept": "Finance",
        "email": "johndoe@gmail.com",
        "phone": "65-1234-5678",
        "biz_address": "smu scis stamford road",
        "sys_role": "staff",
    },
    {
        "staff_id": 456,
        "fname": "Tom",
        "lname": "Harry",
        "dept": "Sales",
        "email": "tomharry@gmail.com",
        "phone": "65-4566-5678",
        "biz_address": "smu scis stamford road",
        "sys_role": "hr",
    },
]


# Get specific staff details based on given clerk_id
@router.get("/clerk/{clerk_id}", response_model=StaffDetailsPydantic)
async def get_clerk_staff(clerk_id: str):
    """
    ### Description:
    This endpoint returns a specifc staff member and the corresponding staff's details based on the given clerk_id.

    ### Parameters:
    `clerk_id`: The clerk_id of the staff to be queried and returned.

    ### Returns:
    A JSON object containing the details of the given staff member.

    ### Example:
    #### Request:
    ```
    GET /staff/get-staff/123
    clerk_id: 12345678
    ```
    #### Response:
    ```
    {
            "staff_id": 456,
            "fname": "Tom",
            "lname": "Harry",
            "dept": "Sales",
            "email": "tomharry@gmail.com",
            "phone": "65-4566-5678",
            "biz_address": "smu scis stamford road",
            "sys_role": "hr"
    }
    ```
    ### Errors:
    `404 Not Found`: No staff member matching the given clerk_id found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get staff details with try-catch block
    try:
        response = db_services.get_clerk_staff(clerk_id)

        if response is None:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with clerk_id: '{clerk_id}' not found",
            )
        else:
            return response

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with clerk_id: '{clerk_id}' not found",
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )


# Get all staff details
@router.get("", response_model=List[StaffDetailsPydantic])
async def get_all_staff():
    """
    ### Description:
    This endpoint returns a list of all staff members currently in the system.

    ### Parameters:
    Null.

    ### Returns:
    A list containing the details of all staff members in JSON format.

    ### Example:
    #### Request:
    ```
    GET /staff/get-all-staff
    ```
    #### Response:
    ```
    [
            {
                    "staff_id": 123,
                    "fname": "John",
                    "lname": "Doe",
                    "dept": "Finance",
                    "email": "johndoe@gmail.com",
                    "phone": "65-1234-5678",
                    "biz_address": "smu scis stamford road",
                    "sys_role": "staff"
            },
            {
                    "staff_id": 456,
                    "fname": "Tom",
                    "lname": "Harry",
                    "dept": "Sales",
                    "email": "tomharry@gmail.com",
                    "phone": "65-4566-5678",
                    "biz_address": "smu scis stamford road",
                    "sys_role": "hr"
            },
    ]
    ```
    ### Errors:
    `404 Not Found`: No staff members found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get staff details with try-catch block
    try:
        response = db_services.get_all_staff_details()

        if response is None:
            raise HTTPException(
                status_code=404, detail="No staff members found in the system"
            )
        else:
            return response

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404, detail="No staff members found in the system"
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )


# Get specific staff details based on given staff_id
@router.get("/{staff_id}", response_model=StaffDetailsPydantic)
async def get_staff(staff_id: int):
    """
    ### Description:
    This endpoint returns a specifc staff member and the corresponding staff's details based on the given staff_id.

    ### Parameters:
    `staff_id`: The staff_id of the staff to be queried and returned.

    ### Returns:
    A JSON object containing the details of the given staff member.

    ### Example:
    #### Request:
    ```
    GET /staff/get-staff/123
    staff_id: 12345678
    ```
    #### Response:
    ```
    {
            "staff_id": 456,
            "fname": "Tom",
            "lname": "Harry",
            "dept": "Sales",
            "email": "tomharry@gmail.com",
            "phone": "65-4566-5678",
            "biz_address": "smu scis stamford road",
            "sys_role": "hr"
    }
    ```
    ### Errors:
    `404 Not Found`: No staff member matching the given staff_id found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get staff details with try-catch block
    try:
        response = db_services.get_staff_details(staff_id)

        if response is None:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' not found",
            )
        else:
            return response

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' not found",
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )


# Get all the skills of each staff
@router.get("/skills/{staff_id}", response_model=List[StaffSkillsPydantic])
async def get_staff_skills(staff_id: int):
    """
    ### Description:
    This endpoint returns a list of all skills and their details for a given staff member based on the given staff_id.

    ### Parameters:
    `staff_id`: The staff_id of the staff to be queried and returned.

    ### Returns:
    A JSON object containing the details of all skills for the given staff member.

    ### Example:
    #### Request:
    ```
    GET /staff/skills/12345678
    staff_id: 12345678
    ```
    #### Response:
    ```
    [
        {
            "staff_id": 123456789,
            "skill_id": 345678790,
            "skill_name": "Typescript Developer",
            "skill_status": "active",
            "ss_status": "active"
        },
        {
            "staff_id": 123456789,
            "skill_id": 345678890,
            "skill_name": "VMWare Villian",
            "skill_status": "inactive",
            "ss_status": "unverified"
        }
    ]
    ```
    ### Errors:
    `404 Not Found`: staff member with the given staff_id does not have any skills in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get all staff's skills details with try-catch block
    try:
        response = db_services.get_staff_skill(staff_id)

        if response is not None:
            return response
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' does not exist in the system",
            )

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' does not exist in the system",
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )


# Get the match and gaps between staff skills and role listing required skills
@router.get(
    "/role-skills-match/{staff_id}/{role_listing_id}",
    response_model=MatchResult,
)
async def get_staff_role_skills_match(
    staff_id: int,
    role_listing_id: int,
):
    """
    ### Description:
    This endpoint returns a list of skills a staff has that matches the skills required for a role listing, and a list of the staff's missing required skills too.<br /><br />
    The matching skills are further grouped into 3 categories based on the staff to skill status: active, in-progress, and unverified.
    ### Parameters:
    `staff_id`: The staff_id of the staff to be queried and returned.<br /><br />
    `role_listing_id`: The role_listing_id of the role listing to be queried and returned.
    ### Returns:
    A JSON object containing the details of the staff's skills that matches and that are missing from the role listing's required skills.

    ### Example:
    #### Request:
    ```
    GET /staff/role-skills-match/12345678/678
    staff_id: 12345678
    role_listing_id: 678
    ```
    #### Response:
    ```
        {
            "match": {
                "active": [
                    {
                        "skill_id": 345678866,
                        "skill_name": "Java Developer",
                        "skill_status": "active",
                        "ss_status": "active"
                    }
                ],
                "in-progress": [
                    {
                        "skill_id": 345678790,
                        "skill_name": "Typescript Developer",
                        "skill_status": "active",
                        "ss_status": "in-progress"
                    }
                ],
                "unverified": []
            },
            "missing": [
                {
                    "skill_id": 345678922,
                    "skill_name": "React Beast",
                    "skill_status": "active"
                }
            ]
        }
    ```
    ### Errors:
    `404 Not Found`: staff member with the given staff_id or role_listing with the given role_listing_id does not exist.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get all staff's skills details with try-catch block
    try:
        response = db_services.get_staff_role_skills_match(
            staff_id, role_listing_id
        )

        if response is not None:
            return response
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system.",
            )

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system.",
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )


# Staff applying for an available role listing
@router.post(
    "/role/{staff_id}/{role_listing_id}",
    response_model=RoleApplicationsPydantic,
)
async def create_staff_role_listing_application(
    staff_id: int,
    role_listing_id: int,
):
    """
    ### Description:
    This endpoint allows a staff to apply for an available role listing, with the given staff_id and role_listing_id.
    ### Parameters:
    `staff_id`: The staff_id of the staff to be used to create a new role_listing application.<br /><br />
    `role_listing_id`: The role_listing_id of the role listing to be used to create a new role_listing application.
    ### Returns:
    A JSON object containing the details of the newly created role_listing application if successfull, raising an exception otherwise if not successfull.
    ### Example:
    #### Request:
    ```
    POST /staff/role-listing/12345678/678
    staff_id: 12345678
    role_listing_id: 678
    ```
    #### Response:
    ```
        {
            "role_app_id": 4,
            "staff_id": 123456789,
            "role_app_ts_create": "2023-10-16T06:14:30",
            "role_app_status": "applied",
            "role_listing_id": 2
        }
    ```
    ### Errors:
    `400 Bad Request`: staff member with the given staff_id has already applied for the role_listing with the given role_listing_id previously.<br /><br />
    `404 Not Found`: staff member with the given staff_id or role_listing with the given role_listing_id does not exist.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    # Invoking database service to get all staff's skills details with try-catch block
    try:
        response = db_services.create_role_application(
            role_listing_id=role_listing_id,
            staff_id=staff_id,
            role_app_status="applied",
        )

        if response is not None:
            if response == "applied before":
                raise HTTPException(
                    status_code=400,
                    detail=f"Staff with staff_id: '{staff_id}' has already applied for role_listing with role_listing_id: '{role_listing_id}' previously.",
                )
            else:
                return response
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system.",
            )

    # Catching exceptions and raising them
    except Exception as e:
        # Catching 404 HTTPException specfically
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Staff with staff_id: '{staff_id}' or role_listing with role_listing_id: '{role_listing_id}' does not exist in the system.",
            )
        # Catching 400 HTTPException specfically
        elif e.status_code == 400:
            raise HTTPException(
                status_code=400,
                detail=f"Staff with staff_id: '{staff_id}' has already applied for role_listing with role_listing_id: '{role_listing_id}' previously.",
            )
        # Catching any other unexpected exceptions, returning a 500 error
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error"
            )
