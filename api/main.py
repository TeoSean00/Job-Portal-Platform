from fastapi import FastAPI
from pydantic import BaseModel
import datetime as dt
from enum import Enum, auto

from fastapi import HTTPException, Query

# Import database services
import database.services as db_services # This is for npm run dev
app = FastAPI()

# =========================== Start: Pydantic Classes ===========================
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
    # What I am getting from keith's frontend
    # Clarify if role_listing_ts_update, role_listing_updater is
    role_name:str
    role_listing_desc: str
    role_listing_source: int
    role_listing_open: str
    role_listing_close: str
    role_listing_hide: str
    role_listing_creator: int
    role_listing_updater: int
# =========================== End: Pydantic Classes ===========================
# =========================== Start: Helper Functions  ===========================

def authenticate_user(
        user:User,
        *role:str
        ):
    """
    Function to authenticate user based on token and role.
    In practice, decode user token and see if it matches the role
    you are trying to verify for.
    For the context of this project, we will assume that the token is valid.
    """
    if user.role == 4:
        return False
    return True

def convert_str_to_datetime(date_str:str):
    """
    Function to convert string to datetime object.
    """
    return dt.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

def get_attrs_from_model(model):
    """
    Function to get attributes from model.
    """
    return [column.name for column in model.__table__.columns]

def convert_sqlalchemy_object_to_dict(sqlalchemy_object):
    """
    Function to convert sqlalchemy object to dict.
    """
    return {c.name: getattr(sqlalchemy_object, c.name) for c in sqlalchemy_object.__table__.columns}

def validate_role_listing(role_details: RoleListing):
    print(f"Validating role_name: {role_details.role_name}")
    if role_details.role_name == "Invalid Role":
        return False
    return True

# =========================== End: Helper Functions  ===========================
# =========================== Start: End points  ===========================

@app.get("/api/python")
def hello_world():
    # Modify the below function to easily retrieve data from db
    # _ = db_services.get_staff_details(123)
    # print(get_attrs_from_model(_.all()[0]))
    # for tmp in _.all():
    #     print(tmp.staff_id)
    return {"message": "Hello World"}
 
# =========================== Start: Role Details  ===========================

@app.get("/api/role_details")
def get_role_details(
    user: User,
    role_id: int = Query(None, description="Optional role_id"),
):
    """
    End point that returns all the created role_listings inside the table.
    If a role_id is specified, only return information for that role_id
    """
    if not authenticate_user(user, "ADMIN"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role details for all
        if role_id == None:
            role_details = db_services.get_all_role_details()
            role_detail = []
            for item in role_details.all():
                role_detail.append(
                    convert_sqlalchemy_object_to_dict(item)
                )
            return {"role_details": role_detail}
        else:
            role_detail = db_services.get_role_details(role_id)
            if role_detail == None:
                raise HTTPException(
                    status_code=404, 
                    detail={
                        "message":f"Role details with id {role_id} not found!"
                        })
            return {"role_details": convert_sqlalchemy_object_to_dict(role_detail)}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass
# =========================== End: Role Details  ===========================

# =========================== Start: Role Skills  ===========================

@app.get("/api/role_skills")
def get_role_skills(
    user:User,
    role_id: int = Query(description="Required role_id"),
):
    """
    End point that takes in a role ID and returns the skills associated with that role.
    """
    if not authenticate_user(user, "ADMIN", "STAFF", "DIRECTOR"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        role_skills = db_services.get_role_skill(role_id)
        if role_skills == None:
            raise HTTPException(
                status_code=404, 
                detail={
                    "message":f"Role with id {role_id} either has no skills, or does not exist!"
                    })
        return {"role_skills": convert_sqlalchemy_object_to_dict(role_skills)}
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

@app.get("/api/role_listing")
def get_role_listing(
    user: User,
    role_listing_id: int = Query(None, description="Optional role_listing_id"),
):
    """
    End point that takes in an optional role_listing_id and returns the role_listing.
    If role_listing_id is provided, it returns information about that ID.
    If role_listing_id is blank, it returns all role_listings.
    """
    if not authenticate_user(user, "ADMIN", "STAFF", "DIRECTOR"):
        raise HTTPException(status_code=401, detail="Unauthorized user!")
    try:
        # Return role listing for all
        if role_listing_id == None:
            role_listings = db_services.get_all_role_listings()
            role_listing = []
            for item in role_listings.all():
                role_listing.append(
                    convert_sqlalchemy_object_to_dict(item)
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
            return {"role_listing": convert_sqlalchemy_object_to_dict(role_listing)}
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close DB connection if needed
        pass

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
        role_listing_ts_create = dt.datetime.utcnow()
        if validate_role_listing(role_details):
            data = {
                "role_id": 234511581, # Links to ID inside role details
                "role_listing_desc": role_details.role_listing_desc,
                "role_listing_source": user.user_token,
                "role_listing_open": convert_str_to_datetime(role_details.role_listing_open),
                "role_listing_close": convert_str_to_datetime(role_details.role_listing_close),
                "role_listing_hide": convert_str_to_datetime(role_details.role_listing_hide),
                "role_listing_creator": user.user_token,
                "role_listing_ts_create": role_listing_ts_create,
                # "role_listing_updater": None,
                # "role_listing_ts_update": None,
                # Set the updater and update time to the creator on first occurence
                "role_listing_updater": user.user_token,
                "role_listing_ts_update": role_listing_ts_create,
            }
            # Create role_listing
            db_services.create_role_listing(**data)
        else:
            raise HTTPException(status_code=400, detail={"message":"Invalid role details!"})
             
        # Connect to DB and create role_listing there
        return {"message": "Created!"}    
    except HTTPException as e:
        raise e
    except Exception as e:
        # This catches all other exceptions
        raise HTTPException(status_code=500, detail={"message":"Internal Server Error!"})
    finally:
        # Close db connection 
        pass
# =========================== End: Role Listing  ===========================

# =========================== End: Endpoints  ===========================
