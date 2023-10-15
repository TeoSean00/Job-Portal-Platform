from typing import List

from fastapi import APIRouter, HTTPException

import database.services as db_services
from database.schemas import StaffDetailsPydantic

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
