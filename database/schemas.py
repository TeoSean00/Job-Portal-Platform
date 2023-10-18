from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel

from database.enums import (
    RoleApplicationStatusEnum,
    RoleTypeEnum,
    StatusEnum,
    SysRoleEnum,
    VerificationStatusEnum,
)


class User(BaseModel):
    """
    Represents the requestor user information.
    """

    user_token: str
    role: SysRoleEnum


class RoleDetailsPydantic(BaseModel):
    role_id: int
    role_name: str
    role_description: str
    role_status: StatusEnum

    class Config:
        from_attributes = True


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
        from_attributes = True


class SkillDetailsPydantic(BaseModel):
    skill_id: int
    skill_name: str
    skill_status: StatusEnum

    class Config:
        orm_mode = True


class MatchStatus(BaseModel):
    active: List[SkillDetailsPydantic] = []
    in_progress: List[SkillDetailsPydantic] = []
    unverified: List[SkillDetailsPydantic] = []

    class Config:
        orm_mode = True


class MatchResult(BaseModel):
    match: MatchStatus
    missing: List[SkillDetailsPydantic]

    class Config:
        orm_mode = True


# class RoleListingsPydantic(BaseModel):
#     role_listing_id: int
#     role_id: int
#     role_listing_desc: str
#     role_listing_source: int
#     role_listing_open: datetime
#     role_listing_close: datetime
#     role_listing_hide: Optional[datetime]
#     role_listing_creator: int
#     role_listing_ts_create: datetime
#     role_listing_updater: int
#     role_listing_ts_update: Optional[datetime]

#     class Config:
#         from_attributes = True


class RoleListingsPydantic(BaseModel):
    # Updated model to get from frontend
    role_listing_id: int
    role_id: int
    role_listing_desc: str
    role_listing_source: int
    role_listing_open: str
    role_listing_hide: Optional[str] = None
    role_listing_creator: int
    role_listing_ts_create: Optional[str] = None
    role_listing_updater: Optional[int] = None
    role_listing_ts_update: Optional[str] = None

    class Config:
        from_attributes = True


class RoleApplicationsPydantic(BaseModel):
    role_app_id: int
    role_listing_id: int
    staff_id: int
    role_app_status: RoleApplicationStatusEnum
    role_app_ts_create: datetime

    class Config:
        from_attributes = True


class RoleSkillsPydantic(BaseModel):
    role_id: int
    skill_id: int

    class Config:
        from_attributes = True


class StaffReportingOfficerPydantic(BaseModel):
    staff_id: int
    RO_id: int

    class Config:
        from_attributes = True


class StaffRolesPydantic(BaseModel):
    staff_id: int
    staff_role: int
    role_type: RoleTypeEnum
    sr_status: StatusEnum

    class Config:
        from_attributes = True


class StaffSkillsPydantic(BaseModel):
    staff_id: int
    skill_id: int
    skill_name: str
    skill_status: StatusEnum
    ss_status: VerificationStatusEnum

    class Config:
        from_attributes = True


class ClerkStaffMatch(BaseModel):
    clerk_id: int
    staff_id: int

    class Config:
        from_attributes = True
