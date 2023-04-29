from sqlalchemy import Table, Column, String, DateTime, Integer, create_engine, ForeignKey
from datetime import datetime
from sqlalchemy.orm import declarative_base,sessionmaker
import os


# DATABASE CONSTRUCTION
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')

Base = declarative_base()

engine = create_engine(connection_string,echo=True)

Session = sessionmaker()
# Table: adminInfo
class adminInfo(Base):
    __tablename__ = 'adminInfo'

    adminID = Column(Integer, primary_key=True)
    firstName = Column(String(25), nullable=False, unique=False)
    lastName = Column(String(25), nullable=False, unique=False)
    dateCreated = Column(DateTime, default=datetime.utcnow)

    # Check this login info later!
    password = Column(String)
    email = Column(String(80), unique=True, nullable=False)
'''
    # many-to-many relationship with eventLog and residentInfo table
    admins = relationship('residentInfo', secondary='admin_resident')
    admin_logs = relationship('eventLog', secondary='admin_event')
'''
##Table: residentInfo
class residentInfo(Base):
    __tablename__ = 'residentInfo'

    residentID = Column(Integer, primary_key=True)
    firstName = Column(String(25), nullable=False, unique=False)
    lastName = Column(String(25), nullable=False, unique=False)
    dateCreated = Column(DateTime, default=datetime.utcnow)

    # Check this login info later!
    password = Column(String)
    email = Column(String(80), unique=True, nullable=False)
'''
    # many-to-many relationship with adminInfo and eventLog table
    admins = relationship('adminInfo', secondary='admin_resident')
    resident_logs = relationship('eventLog', secondary='resident_info')
'''
## Table: eventLog#
class eventLog(Base):
    __tablename__ = 'eventLog'

    eventID = Column(Integer, primary_key=True)
    eventType = Column(String)
    eventDate = Column(DateTime, default=datetime.utcnow)
    result = Column(String)
'''
    # many-to-many relationship with adminInfo and residentInfo table
    event_admin = relationship('adminInfo', secondary='admin_event')
    event_resident = relationship('residentInfo', secondary='resident_info')
'''
'''
    # define admin_event relationship
    admin_event = Table('admin_event', Base.metadata,
        Column('adminID', Integer, ForeignKey('adminInfo.adminID')),
        Column('eventID', Integer, ForeignKey('eventLog.eventID'))
    )

    # define resident_info relationship
    resident_info = Table('resident_info', Base.metadata,
        Column('residentID', Integer, ForeignKey('residentInfo.residentID')),
        Column('eventID', Integer, ForeignKey('eventLog.eventID'))
    )

    # define admin_resident relationship
    admin_resident = Table('admin_resident', Base.metadata,
        Column('adminID', Integer, ForeignKey('adminInfo.adminID')),
        Column('residentID', Integer, ForeignKey('residentInfo.residentID'))
    )
'''
##Table: permission

