import datetime as dt


from database.schemas import (
    User
)

def authenticate_user(
        user:User,
        *role:str
):
    """
    Pseudo function for authenticating if user is of the required role.
    User will be the user object, while role will be the priviledge
    we are checking for.
    Eg, authenticate_user(user, "staff", "admin") will check if the user
    is either a staff or admin.
    """
    # 4 corrosponds to invalid in SysRoleEnum
    # if user.role ==  *role:
    #     return True
    if user.role == "invalid":
        return False
    return True

def convert_str_to_datetime(date_str:str):
    """
    Function to convert string to datetime object.
    """
    if type(date_str) == str:
        return dt.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    else:
        return date_str

def get_attrs_from_model(model):
    """
    Function to get attributes from model.
    Model refers to an SQLAlchemy model / object.
    Used when trying to decipher columns of an objecta model.
    """
    return [column.name for column in model.__table__.columns]

def convert_sqlalchemy_object_to_dict(sqlalchemy_object):
    """
    Function to convert sqlalchemy object to dict.
    Used when returning retrieved items to frontend.
    """
    return {c.name: getattr(sqlalchemy_object, c.name) for c in sqlalchemy_object.__table__.columns}
