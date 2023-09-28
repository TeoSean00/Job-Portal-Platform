from fastapi import FastAPI
from pydantic import BaseModel
import pprint
from datetime import datetime
from enum import Enum, auto

from fastapi import HTTPException, status

app = FastAPI()

class RolesEnum(str, Enum):
    ADMIN = auto()
    STAFF = auto()
    DIRECTOR = auto()
    INVALID = auto()

# Used to verify user for any action
class User(BaseModel):
    user_token:int
    role: RolesEnum

class RoleListing(BaseModel):
    role_name:str
    role_listing_desc: str
    role_listing_source: int
    role_listing_open: str
    role_listing_close: str
    role_listing_creator: int
    # role_listing_ts_created: datetime, change to now

def authenticate_user(
        user:User,
        role:str
        ):
    """
    Function to authenticate user based on token and role.
    In practice, decode user token and see if it matches the role
    you are trying to verify for.
    For the context of this project, we will assume that the token is valid.
    """
    print(f"User role is {user.role}")
    if user.role == 4:
        return False
    return True

def validate_role_listing(role_details: RoleListing):
    print(f"Validating role_name: {role_details.role_name}")
    if role_details.role_name == "Invalid Role":
        print("Role details are invalid.")
        return False
    print("Role details are valid.")
    return True

    
@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.post("/api/role_listing")
def create_role_listing(
    user: User,
    role_details: RoleListing
    ):
    """
    End point that takes in a role_listing, validates and creates it.
    """
    # Authenticate user 
    if not authenticate_user(user, "ADMIN"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Validate form-details
        pprint.pprint(role_details)
        if validate_role_listing(role_details):
            print("Put in DB")
        else:
            print("Why are you raising me?")
            raise HTTPException(status_code=400, detail={"message":"Invalid role details!"})
             
        # Connect to DB and create role_listing there
        return {"message": "Created!"}    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close db connection 
        pass
