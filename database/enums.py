from enum import Enum


class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class SysRoleEnum(str, Enum):
    STAFF = "staff"
    HR = "hr"
    MANAGER = "manager"


class RoleApplicationStatusEnum(str, Enum):
    APPLIED = "applied"
    WITHDRAWN = "withdrawn"


class RoleTypeEnum(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class VerificationStatusEnum(str, Enum):
    ACTIVE = "active"
    UNVERIFIED = "unverified"
    IN_PROGRESS = "in-progress"
