from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String(50))
    machine_type = Column(String(50))

class MachineEvent(Base):
    __tablename__ = "machine_events"

    id = Column(Integer, primary_key=True, index=True)

    machine_name = Column(String(50))
    status = Column(String(20))

    spindle_rpm = Column(Float)
    feed_rate = Column(Float)
    spindle_load = Column(Float)
    spindle_temp = Column(Float)

    x_position = Column(Float)
    y_position = Column(Float)
    z_position = Column(Float)

    tool_id = Column(Integer)
    tool_wear = Column(Float)
    current_cycle_time = Column(Float)

    cycle_duration = Column(Float)
    production_count = Column(Integer)

    alarm_code = Column(String(50))
    alarm_severity = Column(String(20))
    alarm_message = Column(String(255))

    event_type = Column(String(50))

    timestamp = Column(DateTime, default=datetime.utcnow)
