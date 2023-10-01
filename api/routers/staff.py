from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
  prefix = "/staff",
  tags = ["Staff"],
)


mock_data = {
  123: {
    "name": "John Doe",
    "role": "Software Developer",
    "skills": ["Python", "Django", "FastAPI", "ReactJS", "JavaScript", "HTML", "CSS"],
  },
  456: {
    "name": "John Doe2",
    "role": "Software Tester",
    "skills": ["Python", "React", "Flask", "TypeScript", "HTML", "CSS"],
  }
}


@router.get("/get-all")
async def get_all_staff():
  """
    ### Description:
    This endpoint returns a list of all staff members currently in the system.

    ### Parameters:
    Null.

    ### Returns:
    A JSON object containing the details of all staff members.

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
    {
      123: {
        "name": "John Doe",
        "role": "Software Developer",
        "skills": ["Python", "Django", "FastAPI", "ReactJS", "JavaScript", "HTML", "CSS"],
      },
      456: {
        "name": "John Doe2",
        "role": "Software Tester",
        "skills": ["Python", "React", "Flask", "TypeScript", "HTML", "CSS"],
      }
    }
    ```
    ### Errors:
    `404 Not Found`: No staff members found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
  if mock_data:
    return mock_data
  else:
    raise HTTPException(status_code=404, detail="No staff found")
  

@router.get("/get-staff/{staff_id}")
async def get_staff(
  staff_id: int
  ):
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
      123: {
        "name": "John Doe",
        "role": "Software Developer",
        "skills": ["Python", "Django", "FastAPI", "ReactJS", "JavaScript", "HTML", "CSS"],
      }
    }
    ```
    ### Errors:
    `404 Not Found`: No staff member matching the given staff_id found in the system.<br /><br />
    `500 Internal Server Error`: Generic server error that can occur for various reasons, such as unhandled exceptions in the endpoint, indicates that something went wrong with the server.<br /><br />
    """
    if staff_id in mock_data:
      return mock_data[staff_id]
    else:
      raise HTTPException(status_code=404, detail="Staff with staff_id {staff_id} not found")