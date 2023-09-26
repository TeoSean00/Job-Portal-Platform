from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum

class StaffReportingOfficerPydantic(BaseModel):
    staff_id: int
    RO_id: int

    class Config:
        orm_mode = True

class RoleDetailsPydantic(BaseModel):
    role_id: int
    role_name: str
    role_description: str
    role_status: str

    class Config:
        orm_mode = True

class StaffRolesPydantic(BaseModel):
    staff_id: int
    staff_role: int
    role_type: str
    sr_status: str

    class Config:
        orm_mode = True

class SkillDetailsPydantic(BaseModel):
    skill_id: int
    skill_name: str
    skill_status: str

    class Config:
        orm_mode = True

class StaffSkillsPydantic(BaseModel):
    staff_id: int
    skill_id: int
    ss_status: str

    class Config:
        orm_mode = True

class RoleSkillsPydantic(BaseModel):
    role_id: int
    skill_id: int

    class Config:
        orm_mode = True

class RoleListingsPydantic(BaseModel):
    role_listing_id: int
    role_id: int
    role_listing_desc: Optional[str]
    role_listing_source: int
    role_listing_open: date
    role_listing_close: date
    role_listing_hide: Optional[date]
    role_listing_creator: int
    role_listing_ts_create: datetime
    role_listing_updater: int
    role_listing_ts_update: datetime

    class Config:
        orm_mode = True

class RoleApplicationsPydantic(BaseModel):
    role_app_id: int
    role_listing_id: int
    staff_id: int
    role_app_status: str
    role_app_ts_create: datetime

    class Config:
        orm_mode = True