from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String

from database import Base


class RoleDetails(Base):
    __tablename__ = "ROLE_DETAILS"
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)
    role_description = Column(String(50000))
    role_status = Column(Enum("active", "inactive"))


class StaffDetails(Base):
    __tablename__ = "STAFF_DETAILS"
    staff_id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    dept = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    biz_address = Column(String(255), nullable=False)
    sys_role = Column(Enum("staff", "hr", "manager"), nullable=False)


class RoleListings(Base):
    __tablename__ = "ROLE_LISTINGS"
    role_listing_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("ROLE_DETAILS.role_id"), nullable=False)
    role_listing_desc = Column(String(50000))
    role_listing_source = Column(
        Integer, ForeignKey("STAFF_DETAILS.staff_id"), nullable=False
    )
    role_listing_open = Column(DateTime, nullable=False)
    role_listing_close = Column(DateTime, nullable=False)
    role_listing_hide = Column(DateTime)
    role_listing_creator = Column(
        Integer, ForeignKey("STAFF_DETAILS.staff_id"), nullable=False
    )
    role_listing_ts_create = Column(DateTime, nullable=False)
    role_listing_updater = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"))
    role_listing_ts_update = Column(DateTime)


class RoleApplications(Base):
    __tablename__ = "ROLE_APPLICATIONS"
    role_app_id = Column(Integer, primary_key=True, autoincrement=True)
    role_listing_id = Column(
        Integer, ForeignKey("ROLE_LISTINGS.role_listing_id"), nullable=False
    )
    staff_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), nullable=False)
    role_app_status = Column(Enum("applied", "withdrawn"))
    role_app_ts_create = Column(DateTime, default=datetime.utcnow)


class SkillDetails(Base):
    __tablename__ = "SKILL_DETAILS"
    skill_id = Column(Integer, primary_key=True)
    skill_name = Column(String(50), nullable=False)
    skill_status = Column(Enum("active", "inactive"), nullable=False)


class RoleSkills(Base):
    __tablename__ = "ROLE_SKILLS"
    role_id = Column(Integer, ForeignKey("ROLE_DETAILS.role_id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("SKILL_DETAILS.skill_id"), primary_key=True)


class StaffReportingOfficer(Base):
    __tablename__ = "STAFF_REPORTING_OFFICER"
    staff_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), primary_key=True)
    RO_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), nullable=False)


class StaffRoles(Base):
    __tablename__ = "STAFF_ROLES"
    staff_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), primary_key=True)
    staff_role = Column(Integer, ForeignKey("ROLE_DETAILS.role_id"), primary_key=True)
    role_type = Column(Enum("primary", "secondary"), nullable=False)
    sr_status = Column(Enum("active", "inactive"), nullable=False)


class StaffSkills(Base):
    __tablename__ = "STAFF_SKILLS"
    staff_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("SKILL_DETAILS.skill_id"), primary_key=True)
    ss_status = Column(Enum("active", "unverified", "in-progress"), nullable=False)


class ClerkStaffMatch(Base):
    __tablename__ = "CLERK_STAFF_MATCH"
    clerk_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("STAFF_DETAILS.staff_id"), nullable=False)
