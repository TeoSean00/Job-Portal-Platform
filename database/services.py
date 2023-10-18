import datetime as dt

from fastapi import HTTPException
from sqlalchemy.exc import OperationalError

from database.database import SessionLocal
from database.models import (
    ClerkStaffMatch,
    RoleApplications,
    RoleDetails,
    RoleListings,
    RoleSkills,
    SkillDetails,
    StaffDetails,
    StaffReportingOfficer,
    StaffRoles,
    StaffSkills,
)


# Healthcheck
def healthcheck():
    try:
        db = SessionLocal()

        # Attempt a simple query to check the database connection
        db.execute("SELECT 1")
        return True  # Database is reachable
    except OperationalError:
        return False  # Database is not reachable
    finally:
        db.close()


# RoleDetails CRUD operations


def get_role_details(role_id: int):
    db = SessionLocal()
    role = db.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()
    db.close()
    return role


def get_all_role_details():
    db = SessionLocal()
    role = db.query(RoleDetails)
    db.close()
    return role


def create_role_details(
    role_name: str, role_description: str, role_status: str
):
    db = SessionLocal()
    role = RoleDetails(
        role_name=role_name,
        role_description=role_description,
        role_status=role_status,
    )
    db.add(role)
    db.commit()
    db.refresh(role)
    db.close()
    return role


def update_role_details(
    role_id: int, role_name: str, role_description: str, role_status: str
):
    db = SessionLocal()
    role = db.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()
    if role:
        role.role_name = role_name
        role.role_description = role_description
        role.role_status = role_status
        db.commit()
        db.refresh(role)
        db.close()
        return role
    db.close()
    raise HTTPException(status_code=404, detail="Role not found")


def delete_role_details(role_id: int):
    db = SessionLocal()
    role = db.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
        db.close()
        return role
    db.close()
    raise HTTPException(status_code=404, detail="Role not found")


# StaffDetails CRUD operations


def get_staff_details(staff_id: int):
    db = SessionLocal()
    staff = (
        db.query(StaffDetails)
        .filter(StaffDetails.staff_id == staff_id)
        .first()
    )
    db.close()
    return staff


def create_staff_details(
    fname: str,
    lname: str,
    dept: str,
    email: str,
    phone: str,
    biz_address: str,
    sys_role: str,
):
    db = SessionLocal()
    staff = StaffDetails(
        fname=fname,
        lname=lname,
        dept=dept,
        email=email,
        phone=phone,
        biz_address=biz_address,
        sys_role=sys_role,
    )
    db.add(staff)
    db.commit()
    db.refresh(staff)
    db.close()
    return staff


def update_staff_details(
    staff_id: int,
    fname: str,
    lname: str,
    dept: str,
    email: str,
    phone: str,
    biz_address: str,
    sys_role: str,
):
    db = SessionLocal()
    staff = (
        db.query(StaffDetails)
        .filter(StaffDetails.staff_id == staff_id)
        .first()
    )
    if staff:
        staff.fname = fname
        staff.lname = lname
        staff.dept = dept
        staff.email = email
        staff.phone = phone
        staff.biz_address = biz_address
        staff.sys_role = sys_role
        db.commit()
        db.refresh(staff)
        db.close()
        return staff
    db.close()
    raise HTTPException(status_code=404, detail="Staff not found")


def delete_staff_details(staff_id: int):
    db = SessionLocal()
    staff = (
        db.query(StaffDetails)
        .filter(StaffDetails.staff_id == staff_id)
        .first()
    )
    if staff:
        db.delete(staff)
        db.commit()
        db.close()
        return staff
    db.close()
    raise HTTPException(status_code=404, detail="Staff not found")


# RoleListings CRUD operations


def get_role_listings(role_listing_id: int):
    db = SessionLocal()
    role_listing = (
        db.query(RoleListings)
        .filter(RoleListings.role_listing_id == role_listing_id)
        .first()
    )
    db.close()
    return role_listing


def get_all_role_listings():
    db = SessionLocal()
    role_listing = db.query(RoleListings)
    db.close()
    return role_listing


def create_role_listing(
    role_listing_id:int,
    role_id: int,
    role_listing_desc: str,
    role_listing_source: int,
    role_listing_open: dt.datetime,
    role_listing_close: dt.datetime,
    role_listing_hide: dt.datetime,
    role_listing_creator: int,
    role_listing_ts_create: dt.datetime,
    role_listing_updater: int,
    role_listing_ts_update: dt.datetime,
):
    db = SessionLocal()
    role_listing = RoleListings(
        role_listing_id=role_listing_id,
        role_id=role_id,
        role_listing_desc=role_listing_desc,
        role_listing_source=role_listing_source,
        role_listing_open=role_listing_open,
        role_listing_close=role_listing_close,
        role_listing_hide=role_listing_hide,
        role_listing_creator=role_listing_creator,
        role_listing_ts_create=role_listing_ts_create,
        role_listing_updater=role_listing_updater,
        role_listing_ts_update=role_listing_ts_update,
    )
    db.add(role_listing)
    db.commit()
    db.refresh(role_listing)
    db.close()
    return role_listing


def update_role_listing(
    role_listing_id: int,
    role_id: int,
    role_listing_desc: str,
    role_listing_source: int,
    role_listing_open: dt.datetime,
    role_listing_close: dt.datetime,
    role_listing_hide: dt.datetime,
    role_listing_creator: int,
    role_listing_ts_create: dt.datetime,
    role_listing_updater: int,
    role_listing_ts_update: dt.datetime,
):
    db = SessionLocal()
    role_listing = (
        db.query(RoleListings)
        .filter(RoleListings.role_listing_id == role_listing_id)
        .first()
    )
    if role_listing:
        role_listing.role_id = role_id
        role_listing.role_listing_desc = role_listing_desc
        role_listing.role_listing_source = role_listing_source
        role_listing.role_listing_open = role_listing_open
        role_listing.role_listing_close = role_listing_close
        role_listing.role_listing_hide = role_listing_hide
        role_listing.role_listing_creator = role_listing_creator
        role_listing.role_listing_ts_create = role_listing_ts_create
        role_listing.role_listing_updater = role_listing_updater
        role_listing.role_listing_ts_update = role_listing_ts_update
        db.commit()
        db.refresh(role_listing)
        db.close()
        return role_listing
    db.close()
    raise HTTPException(status_code=404, detail="Role listing not found")


def delete_role_listing(role_listing_id: int):
    db = SessionLocal()
    role_listing = (
        db.query(RoleListings)
        .filter(RoleListings.role_listing_id == role_listing_id)
        .first()
    )
    if role_listing:
        db.delete(role_listing)
        db.commit()
        db.close()
        return role_listing
    db.close()
    raise HTTPException(status_code=404, detail="Role listing not found")


# RoleApplications CRUD operations
def get_role_application(role_app_id: int):
    db = SessionLocal()
    role_app = (
        db.query(RoleApplications)
        .filter(RoleApplications.role_app_id == role_app_id)
        .first()
    )
    db.close()
    return role_app


def create_role_application(
    role_listing_id: int, staff_id: int, role_app_status: str
):
    db = SessionLocal()
    role_app = RoleApplications(
        role_listing_id=role_listing_id,
        staff_id=staff_id,
        role_app_status=role_app_status,
    )
    db.add(role_app)
    db.commit()
    db.refresh(role_app)
    db.close()
    return role_app


def update_role_application(
    role_app_id: int, role_listing_id: int, staff_id: int, role_app_status: str
):
    db = SessionLocal()
    role_app = (
        db.query(RoleApplications)
        .filter(RoleApplications.role_app_id == role_app_id)
        .first()
    )
    if role_app:
        role_app.role_listing_id = role_listing_id
        role_app.staff_id = staff_id
        role_app.role_app_status = role_app_status
        db.commit()
        db.refresh(role_app)
        db.close()
        return role_app
    db.close()
    raise HTTPException(status_code=404, detail="Role application not found")


def delete_role_application(role_app_id: int):
    db = SessionLocal()
    role_app = (
        db.query(RoleApplications)
        .filter(RoleApplications.role_app_id == role_app_id)
        .first()
    )
    if role_app:
        db.delete(role_app)
        db.commit()
        db.close()
        return role_app
    db.close()
    raise HTTPException(status_code=404, detail="Role application not found")


# SkillDetails CRUD operations


def get_skill_details(skill_id: int):
    db = SessionLocal()
    skill = (
        db.query(SkillDetails)
        .filter(SkillDetails.skill_id == skill_id)
        .first()
    )
    db.close()
    return skill


def get_all_skills():
    db = SessionLocal()
    skills = db.query(SkillDetails).distinct().all()
    db.close()
    return skills


def create_skill_details(skill_name: str, skill_status: str):
    db = SessionLocal()
    skill = SkillDetails(skill_name=skill_name, skill_status=skill_status)
    db.add(skill)
    db.commit()
    db.refresh(skill)
    db.close()
    return skill


def update_skill_details(skill_id: int, skill_name: str, skill_status: str):
    db = SessionLocal()
    skill = (
        db.query(SkillDetails)
        .filter(SkillDetails.skill_id == skill_id)
        .first()
    )
    if skill:
        skill.skill_name = skill_name
        skill.skill_status = skill_status
        db.commit()
        db.refresh(skill)
        db.close()
        return skill
    db.close()
    raise HTTPException(status_code=404, detail="Skill not found")


def delete_skill_details(skill_id: int):
    db = SessionLocal()
    skill = (
        db.query(SkillDetails)
        .filter(SkillDetails.skill_id == skill_id)
        .first()
    )
    if skill:
        db.delete(skill)
        db.commit()
        db.close()
        return skill
    db.close()
    raise HTTPException(status_code=404, detail="Skill not found")


# RoleSkills CRUD operations


def create_role_skill(role_id: int, skill_id: int):
    db = SessionLocal()
    role_skill = RoleSkills(role_id=role_id, skill_id=skill_id)
    db.add(role_skill)
    db.commit()
    db.refresh(role_skill)
    db.close()
    return role_skill


# Original
# def get_role_skill(role_id: int, skill_id: int):
#     db = SessionLocal()
#     role_skill = (
#         db.query(RoleSkills)
#         .filter(RoleSkills.role_id == role_id, RoleSkills.skill_id == skill_id)
#         .first()
#     )
#     db.close()
#     return role_skill
# Updated, allow us to get all skills associated with a role id
def get_role_skills(role_id: int):
    db = SessionLocal()
    role_skill = db.query(RoleSkills).filter(RoleSkills.role_id == role_id)
    db.close()
    return role_skill


def update_role_skill(role_id: int, skill_id: int):
    db = SessionLocal()
    role_skill = (
        db.query(RoleSkills)
        .filter(RoleSkills.role_id == role_id, RoleSkills.skill_id == skill_id)
        .first()
    )
    if role_skill:
        role_skill.role_id = role_id
        role_skill.skill_id = skill_id
        db.commit()
        db.refresh(role_skill)
        db.close()
        return role_skill
    db.close()
    raise HTTPException(status_code=404, detail="Role skill not found")


def delete_role_skill(role_id: int, skill_id: int):
    db = SessionLocal()
    role_skill = (
        db.query(RoleSkills)
        .filter(RoleSkills.role_id == role_id, RoleSkills.skill_id == skill_id)
        .first()
    )
    if role_skill:
        db.delete(role_skill)
        db.commit()
        db.close()
        return role_skill
    db.close()
    raise HTTPException(status_code=404, detail="Role skill not found")


# StaffReportingOfficer CRUD operations


def create_staff_reporting_officer(staff_id: int, RO_id: int):
    db = SessionLocal()
    staff_ro = StaffReportingOfficer(staff_id=staff_id, RO_id=RO_id)
    db.add(staff_ro)
    db.commit()
    db.refresh(staff_ro)
    db.close()
    return staff_ro


def get_staff_reporting_officer(staff_id: int):
    db = SessionLocal()
    staff_ro = (
        db.query(StaffReportingOfficer)
        .filter(StaffReportingOfficer.staff_id == staff_id)
        .first()
    )
    db.close()
    return staff_ro


def update_staff_reporting_officer(staff_id: int, RO_id: int):
    db = SessionLocal()
    staff_ro = (
        db.query(StaffReportingOfficer)
        .filter(StaffReportingOfficer.staff_id == staff_id)
        .first()
    )
    if staff_ro:
        staff_ro.RO_id = RO_id
        db.commit()
        db.refresh(staff_ro)
        db.close()
        return staff_ro
    db.close()
    raise HTTPException(
        status_code=404, detail="Staff reporting officer not found"
    )


def delete_staff_reporting_officer(staff_id: int):
    db = SessionLocal()
    staff_ro = (
        db.query(StaffReportingOfficer)
        .filter(StaffReportingOfficer.staff_id == staff_id)
        .first()
    )
    if staff_ro:
        db.delete(staff_ro)
        db.commit()
        db.close()
        return staff_ro
    db.close()
    raise HTTPException(
        status_code=404, detail="Staff reporting officer not found"
    )


# StaffRoles CRUD operations


def create_staff_role(
    staff_id: int, staff_role: int, role_type: str, sr_status: str
):
    db = SessionLocal()
    staff_role = StaffRoles(
        staff_id=staff_id,
        staff_role=staff_role,
        role_type=role_type,
        sr_status=sr_status,
    )
    db.add(staff_role)
    db.commit()
    db.refresh(staff_role)
    db.close()
    return staff_role


def get_staff_role(staff_id: int, staff_role: int):
    db = SessionLocal()
    staff_role = (
        db.query(StaffRoles)
        .filter(
            StaffRoles.staff_id == staff_id,
            StaffRoles.staff_role == staff_role,
        )
        .first()
    )
    db.close()
    return staff_role


def update_staff_role(
    staff_id: int, staff_role: int, role_type: str, sr_status: str
):
    db = SessionLocal()
    staff_role = (
        db.query(StaffRoles)
        .filter(
            StaffRoles.staff_id == staff_id,
            StaffRoles.staff_role == staff_role,
        )
        .first()
    )
    if staff_role:
        staff_role.role_type = role_type
        staff_role.sr_status = sr_status
        db.commit()
        db.refresh(staff_role)
        db.close()
        return staff_role
    db.close()
    raise HTTPException(status_code=404, detail="Staff role not found")


def delete_staff_role(staff_id: int, staff_role: int):
    db = SessionLocal()
    staff_role = (
        db.query(StaffRoles)
        .filter(
            StaffRoles.staff_id == staff_id,
            StaffRoles.staff_role == staff_role,
        )
        .first()
    )
    if staff_role:
        db.delete(staff_role)
        db.commit()
        db.close()
        return staff_role
    db.close()
    raise HTTPException(status_code=404, detail="Staff role not found")


# StaffSkills CRUD operations


def create_staff_skill(staff_id: int, skill_id: int, ss_status: str):
    db = SessionLocal()
    staff_skill = StaffSkills(
        staff_id=staff_id, skill_id=skill_id, ss_status=ss_status
    )
    db.add(staff_skill)
    db.commit()
    db.refresh(staff_skill)
    db.close()
    return staff_skill


def get_staff_skill(staff_id: int, skill_id: int):
    db = SessionLocal()
    staff_skill = (
        db.query(StaffSkills)
        .filter(
            StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id
        )
        .first()
    )
    db.close()
    return staff_skill


def update_staff_skill(staff_id: int, skill_id: int, ss_status: str):
    db = SessionLocal()
    staff_skill = (
        db.query(StaffSkills)
        .filter(
            StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id
        )
        .first()
    )
    if staff_skill:
        staff_skill.ss_status = ss_status
        db.commit()
        db.refresh(staff_skill)
        db.close()
        return staff_skill
    db.close()
    raise HTTPException(status_code=404, detail="Staff skill not found")


def delete_staff_skill(staff_id: int, skill_id: int):
    db = SessionLocal()
    staff_skill = (
        db.query(StaffSkills)
        .filter(
            StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id
        )
        .first()
    )
    if staff_skill:
        db.delete(staff_skill)
        db.commit()
        db.close()
        return staff_skill
    db.close()
    raise HTTPException(status_code=404, detail="Staff skill not found")


# ClerkStaffMatch CRUD operations


def create_clerk_staff_match(clerk_id: int, staff_id: int):
    db = SessionLocal()
    clerk_staff_match = ClerkStaffMatch(clerk_id=clerk_id, staff_id=staff_id)
    db.add(clerk_staff_match)
    db.commit()
    db.refresh(clerk_staff_match)
    db.close()
    return clerk_staff_match


def get_clerk_staff_match(clerk_id: int):
    db = SessionLocal()
    clerk_staff_match = (
        db.query(ClerkStaffMatch)
        .filter(ClerkStaffMatch.clerk_id == clerk_id)
        .first()
    )
    db.close()
    return clerk_staff_match


def update_clerk_staff_match(clerk_id: int, staff_id: int):
    db = SessionLocal()
    clerk_staff_match = (
        db.query(ClerkStaffMatch)
        .filter(ClerkStaffMatch.clerk_id == clerk_id)
        .first()
    )
    if clerk_staff_match:
        clerk_staff_match.staff_id = staff_id
        db.commit()
        db.refresh(clerk_staff_match)
        db.close()
        return clerk_staff_match
    db.close()
    raise HTTPException(status_code=404, detail="Clerk staff match not found")


def delete_clerk_staff_match(clerk_id: int):
    db = SessionLocal()
    clerk_staff_match = (
        db.query(ClerkStaffMatch)
        .filter(ClerkStaffMatch.clerk_id == clerk_id)
        .first()
    )
    if clerk_staff_match:
        db.delete(clerk_staff_match)
        db.commit()
        db.close()
        return clerk_staff_match
    db.close()
    raise HTTPException(status_code=404, detail="Clerk staff match not found")
