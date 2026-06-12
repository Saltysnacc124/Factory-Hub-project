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

    temperature = Column(Float)
    production_count = Column(Integer)

    timestamp = Column(DateTime, default=datetime.utcnow)
