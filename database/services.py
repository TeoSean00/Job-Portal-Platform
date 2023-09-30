from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# assuming engine is created already, replace with your actual engine
Session = sessionmaker(bind=engine)

# Create functions for StaffDetails
def create_staff_details(fname, lname, dept, email, phone, biz_address, sys_role):
    session = Session()
    new_staff = StaffDetails(fname=fname, lname=lname, dept=dept, email=email,
                             phone=phone, biz_address=biz_address, sys_role=sys_role)
    session.add(new_staff)
    session.commit()
    session.close()

def get_staff_details(staff_id):
    session = Session()
    staff = session.query(StaffDetails).filter_by(staff_id=staff_id).first()
    session.close()
    return staff

def update_staff_details(staff_id, new_dept):
    session = Session()
    staff = session.query(StaffDetails).filter_by(staff_id=staff_id).first()
    if staff:
        staff.dept = new_dept
        session.commit()
    session.close()

def delete_staff_details(staff_id):
    session = Session()
    staff = session.query(StaffDetails).filter_by(staff_id=staff_id).first()
    if staff:
        session.delete(staff)
        session.commit()
    session.close()

# Create functions for other models (StaffReportingOfficer, RoleDetails, etc.)
# Add similar CRUD functions for each model

# StaffReportingOfficer
def create_staff_reporting_officer(staff_id, RO_id):
    staff_reporting_officer = StaffReportingOfficer(staff_id=staff_id, RO_id=RO_id)
    session.add(staff_reporting_officer)
    session.commit()
    return staff_reporting_officer

def get_staff_reporting_officer(staff_id):
    return session.query(StaffReportingOfficer).filter(StaffReportingOfficer.staff_id == staff_id).first()

def update_staff_reporting_officer(staff_id, new_RO_id):
    staff_ro = session.query(StaffReportingOfficer).filter(StaffReportingOfficer.staff_id == staff_id).first()
    staff_ro.RO_id = new_RO_id
    session.commit()

def delete_staff_reporting_officer(staff_id):
    staff_ro = session.query(StaffReportingOfficer).filter(StaffReportingOfficer.staff_id == staff_id).first()
    session.delete(staff_ro)
    session.commit()

# Add similar CRUD functions for other models like RoleDetails, 
def create_role_details(role_name, role_description, role_status):
    role_details = RoleDetails(role_name=role_name, role_description=role_description, role_status=role_status)
    session.add(role_details)
    session.commit()
    return role_details

def get_role_details(role_id):
    return session.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()

def update_role_details(role_id, new_values):
    role = session.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()
    for key, value in new_values.items():
        setattr(role, key, value)
    session.commit()

def delete_role_details(role_id):
    role = session.query(RoleDetails).filter(RoleDetails.role_id == role_id).first()
    session.delete(role)
    session.commit()

# ...

# Usage example:
# create_role_details('Engineer', 'Responsible for engineering tasks.', 'active')
# get_role_details(1)
# update_role_details(1, {'role_status': 'inactive'})
# delete_role_details(1)

# Add similar CRUD functions for other models like StaffSkills
# ...

def create_staff_skill(staff_id, skill_id, ss_status):
    staff_skill = StaffSkills(staff_id=staff_id, skill_id=skill_id, ss_status=ss_status)
    session.add(staff_skill)
    session.commit()
    return staff_skill

def get_staff_skill(staff_id, skill_id):
    return session.query(StaffSkills).filter(StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id).first()

def update_staff_skill(staff_id, skill_id, new_ss_status):
    staff_skill = session.query(StaffSkills).filter(StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id).first()
    staff_skill.ss_status = new_ss_status
    session.commit()

def delete_staff_skill(staff_id, skill_id):
    staff_skill = session.query(StaffSkills).filter(StaffSkills.staff_id == staff_id, StaffSkills.skill_id == skill_id).first()
    session.delete(staff_skill)
    session.commit()

# ...

# Usage example:
# create_staff_skill(1, 1, 'active')
# get_staff_skill(1, 1)
# update_staff_skill(1, 1, 'inactive')
# delete_staff_skill(1, 1)


# Add similar CRUD functions for other models like RoleSkills
# ...

def create_role_skill(role_id, skill_id):
    role_skill = RoleSkills(role_id=role_id, skill_id=skill_id)
    session.add(role_skill)
    session.commit()
    return role_skill

def get_role_skill(role_id, skill_id):
    return session.query(RoleSkills).filter(RoleSkills.role_id == role_id, RoleSkills.skill_id == skill_id).first()

def delete_role_skill(role_id, skill_id):
    role_skill = session.query(RoleSkills).filter(RoleSkills.role_id == role_id, RoleSkills.skill_id == skill_id).first()
    session.delete(role_skill)
    session.commit()

# ...

# Usage example:
# create_role_skill(1, 1)
# get_role_skill(1, 1)
# delete_role_skill(1, 1)

# CRUD for StaffRoles
# ...

def create_staff_role(staff_id, staff_role, role_type, sr_status):
    staff_role = StaffRoles(staff_id=staff_id, staff_role=staff_role, role_type=role_type, sr_status=sr_status)
    session.add(staff_role)
    session.commit()
    return staff_role

def get_staff_role(staff_id, staff_role):
    return session.query(StaffRoles).filter(StaffRoles.staff_id == staff_id, StaffRoles.staff_role == staff_role).first()

def update_staff_role(staff_id, staff_role, new_sr_status):
    staff_role = session.query(StaffRoles).filter(StaffRoles.staff_id == staff_id, StaffRoles.staff_role == staff_role).first()
    staff_role.sr_status = new_sr_status
    session.commit()

def delete_staff_role(staff_id, staff_role):
    staff_role = session.query(StaffRoles).filter(StaffRoles.staff_id == staff_id, StaffRoles.staff_role == staff_role).first()
    session.delete(staff_role)
    session.commit()

# ...

# Usage example:
# create_staff_role(1, 1, 'primary', 'active')
# get_staff_role(1, 1)
# update_staff_role(1, 1, 'inactive')
# delete_staff_role(1, 1)


# CRUD for SkillDetails
# ...

def create_skill(skill_name, skill_status):
    skill = SkillDetails(skill_name=skill_name, skill_status=skill_status)
    session.add(skill)
    session.commit()
    return skill

def get_skill(skill_id):
    return session.query(SkillDetails).filter(SkillDetails.skill_id == skill_id).first()

def update_skill(skill_id, new_values):
    skill = session.query(SkillDetails).filter(SkillDetails.skill_id == skill_id).first()
    for key, value in new_values.items():
        setattr(skill, key, value)
    session.commit()

def delete_skill(skill_id):
    skill = session.query(SkillDetails).filter(SkillDetails.skill_id == skill_id).first()
    session.delete(skill)
    session.commit()

# ...

# Usage example:
# create_skill('Python Programming', 'active')
# get_skill(1)
# update_skill(1, {'skill_status': 'inactive'})
# delete_skill(1)


# CRUD for RoleListings
# ...

def create_role_listing(role_id, role_listing_desc, role_listing_source, role_listing_open, role_listing_close,
                        role_listing_hide, role_listing_creator, role_listing_updater):
    role_listing = RoleListings(role_id=role_id, role_listing_desc=role_listing_desc,
                                role_listing_source=role_listing_source, role_listing_open=role_listing_open,
                                role_listing_close=role_listing_close, role_listing_hide=role_listing_hide,
                                role_listing_creator=role_listing_creator, role_listing_updater=role_listing_updater)
    session.add(role_listing)
    session.commit()
    return role_listing

def get_role_listing(role_listing_id):
    return session.query(RoleListings).filter(RoleListings.role_listing_id == role_listing_id).first()

def update_role_listing(role_listing_id, new_values):
    role_listing = session.query(RoleListings).filter(RoleListings.role_listing_id == role_listing_id).first()
    for key, value in new_values.items():
        setattr(role_listing, key, value)
    session.commit()

def delete_role_listing(role_listing_id):
    role_listing = session.query(RoleListings).filter(RoleListings.role_listing_id == role_listing_id).first()
    session.delete(role_listing)
    session.commit()

# ...

# Usage example:
# create_role_listing(1, 'Description', 1, '2023-09-15', '2023-09-30', None, 1, 1)
# get_role_listing(1)
# update_role_listing(1, {'role_listing_desc': 'New description'})
# delete_role_listing(1)


# CRUD for RoleApplications
# ...

def create_role_application(role_listing_id, staff_id, role_app_status):
    role_application = RoleApplications(role_listing_id=role_listing_id, staff_id=staff_id, role_app_status=role_app_status)
    session.add(role_application)
    session.commit()
    return role_application

def get_role_application(role_app_id):
    return session.query(RoleApplications).filter(RoleApplications.role_app_id == role_app_id).first()

def update_role_application(role_app_id, new_values):
    role_application = session.query(RoleApplications).filter(RoleApplications.role_app_id == role_app_id).first()
    for key, value in new_values.items():
        setattr(role_application, key, value)
    session.commit()

def delete_role_application(role_app_id):
    role_application = session.query(RoleApplications).filter(RoleApplications.role_app_id == role_app_id).first()
    session.delete(role_application)
    session.commit()

# ...

# Usage example:
# create_role_application(1, 1, 'applied')
# get_role_application(1)
# update_role_application(1, {'role_app_status': 'withdrawn'})
# delete_role_application(1)
