from db_tables import Base,engine
from db_tables import adminInfo, residentInfo, eventLog

Base.metadata.create_all(engine)
