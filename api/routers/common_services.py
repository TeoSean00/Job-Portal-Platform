import datetime as dt

from database.schemas import User


def authenticate_user(user_role: str):
    """
    Function to authenticate user. Hard coded.
    """
    accepted_roles = ["hr", "manager", "staff"]
    if user_role not in accepted_roles:
        return False
    return True


def convert_str_to_datetime(date_str: str):
    """
    Function to convert string to datetime object.
    """
    if isinstance(date_str, str):
        return dt.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    else:
        return date_str


def add_days_to_str_datetime(date_str: str, days: int = 14):
    """
    Function to add days to string datetime object.
    """
    if isinstance(date_str, str):
        date = dt.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        date += dt.timedelta(days=days)
        return date.strftime("%Y-%m-%dT%H:%M:%S")
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
    return {
        c.name: getattr(sqlalchemy_object, c.name)
        for c in sqlalchemy_object.__table__.columns
    }
