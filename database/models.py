from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import datetime as dt

Base = declarative_base()

class StaffDetails(Base):
    __tablename__ = 'STAFF_DETAILS'

    staff_id = Column(Integer, primary_key=True)
    fname = Column(String(50))
    lname = Column(String(50))
    dept = Column(String(50))
    email = Column(String(50))
    phone = Column(String(20))
    biz_address = Column(String(255))
    sys_role = Column(Enum('staff', 'hr', 'manager', 'inactive'))

class StaffReportingOfficer(Base):
    __tablename__ = 'STAFF_REPORTING_OFFICER'

    staff_id = Column(Integer, primary_key=True)
    RO_id = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'))
    staff = relationship('StaffDetails')

class RoleDetails(Base):
    __tablename__ = 'ROLE_DETAILS'

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50))
    role_description = Column(String(50000))
    role_status = Column(Enum('active', 'inactive'))

class StaffRoles(Base):
    __tablename__ = 'STAFF_ROLES'

    staff_id = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'), primary_key=True)
    staff_role = Column(Integer, ForeignKey('ROLE_DETAILS.role_id'), primary_key=True)
    role_type = Column(Enum('primary', 'secondary'))
    sr_status = Column(Enum('active', 'inactive'))

class SkillDetails(Base):
    __tablename__ = 'SKILL_DETAILS'

    skill_id = Column(Integer, primary_key=True)
    skill_name = Column(String(50))
    skill_status = Column(Enum('active', 'inactive'))

class StaffSkills(Base):
    __tablename__ = 'STAFF_SKILLS'

    staff_id = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('SKILL_DETAILS.skill_id'), primary_key=True)
    ss_status = Column(Enum("active", "unverified", "in-progress"))

class RoleSkills(Base):
    __tablename__ = 'ROLE_SKILLS'

    role_id = Column(Integer, ForeignKey('ROLE_DETAILS.role_id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('SKILL_DETAILS.skill_id'), primary_key=True)



# self defined tables for deriving additional information 

class RoleListings(Base):
    __tablename__ = 'ROLE_LISTINGS'

    role_listing_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('ROLE_DETAILS.role_id'))
    role_listing_desc = Column(String)
    role_listing_source = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'))
    role_listing_open = Column(Date)
    role_listing_close = Column(Date)
    role_listing_hide = Column(Date)
    role_listing_creator = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'))
    role_listing_ts_create = Column(DateTime, default=dt.datetime.utcnow)
    role_listing_updater = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'))
    role_listing_ts_update = Column(DateTime, default=dt.datetime.utcnow)

    role = relationship('RoleDetails', backref='listings')
    source_staff = relationship('StaffDetails', foreign_keys=[role_listing_source])
    creator_staff = relationship('StaffDetails', foreign_keys=[role_listing_creator])
    updater_staff = relationship('StaffDetails', foreign_keys=[role_listing_updater])

class RoleApplications(Base):
    __tablename__ = 'ROLE_APPLICATIONS'

    role_app_id = Column(Integer, primary_key=True, autoincrement=True)
    role_listing_id = Column(Integer, ForeignKey('ROLE_LISTINGS.role_listing_id'))
    staff_id = Column(Integer, ForeignKey('STAFF_DETAILS.staff_id'))
    role_app_status = Column(Enum('applied', 'withdrawn'))
    role_app_ts_create = Column(DateTime, default=dt.datetime.utcnow)

    role_listing = relationship('RoleListings', backref='applications')
    staff = relationship('StaffDetails', backref='applications')