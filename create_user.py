from db_tables import Session,engine
from db_tables import residentInfo
from datetime import datetime
local_session=Session(bind=engine)

new_resident=residentInfo(residentID=1, firstName='John', lastName='Doe', password='abc123', email='john.doe@example.com')

local_session.add(new_resident)

local_session.commit()