from typing import List

from fastapi import APIRouter, Depends, HTTPException

from database.schemas import (
    ClerkStaffMatch,
    StaffDetailsPydantic,
    StaffReportingOfficerPydantic,
    StaffRolesPydantic,
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


@router.get("/get-all", response_model=List[StaffDetailsPydantic])
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
    GET /staff/get-all
    Authorization: <Clerk Token>
    Content-Type: Null
    Body: Null
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
    if mock_data:
        return mock_data
    else:
        raise HTTPException(status_code=404, detail="No staff found")


@router.get("/get-staff/{staff_id}", response_model=StaffDetailsPydantic)
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
    Authorization: <Clerk Token>
    Content-Type: Null
    Body: Null
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
    staffMatch = None
    for staff in mock_data:
        if staff["staff_id"] == staff_id:
            staffMatch = staff
            break
    if staffMatch:
        return staffMatch
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Staff with staff_id: '{staff_id}' not found",
        )
