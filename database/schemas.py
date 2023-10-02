from datetime import datetime
from typing import Optional

from .enums import (
    RoleApplicationStatusEnum,
    RoleTypeEnum,
    StatusEnum,
    SysRoleEnum,
    VerificationStatusEnum,
)
from pydantic import BaseModel


class RoleDetailsPydantic(BaseModel):
    role_id: int
    role_name: str
    role_description: str
    role_status: StatusEnum

    class Config:
        orm_mode = True


class StaffDetailsPydantic(BaseModel):
    staff_id: int
    fname: str
    lname: str
    dept: str
    email: str
    phone: str
    biz_address: str
    sys_role: SysRoleEnum

    class Config:
        orm_mode = True


class RoleListingsPydantic(BaseModel):
    role_listing_id: int
    role_id: int
    role_listing_desc: str
    role_listing_source: int
    role_listing_open: datetime
    role_listing_close: datetime
    role_listing_hide: Optional[datetime]
    role_listing_creator: int
    role_listing_ts_create: datetime
    role_listing_updater: int
    role_listing_ts_update: Optional[datetime]

    class Config:
        orm_mode = True


class RoleApplicationsPydantic(BaseModel):
    role_app_id: int
    role_listing_id: int
    staff_id: int
    role_app_status: RoleApplicationStatusEnum
    role_app_ts_create: datetime

    class Config:
        orm_mode = True


class SkillDetailsPydantic(BaseModel):
    skill_id: int
    skill_name: str
    skill_status: StatusEnum

    class Config:
        orm_mode = True


class RoleSkillsPydantic(BaseModel):
    role_id: int
    skill_id: int

    class Config:
        orm_mode = True


class StaffReportingOfficerPydantic(BaseModel):
    staff_id: int
    RO_id: int

    class Config:
        orm_mode = True


class StaffRolesPydantic(BaseModel):
    staff_id: int
    staff_role: int
    role_type: RoleTypeEnum
    sr_status: StatusEnum

    class Config:
        orm_mode = True


class StaffSkillsPydantic(BaseModel):
    staff_id: int
    skill_id: int
    ss_status: VerificationStatusEnum

    class Config:
        orm_mode = True


class ClerkStaffMatch(BaseModel):
    clerk_id: int
    staff_id: int

    class Config:
        orm_mode = True
