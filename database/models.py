from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from database.db import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=True)
    location = Column(String, nullable=True)

    telemetry = relationship("Telemetry", back_populates="machine", cascade="all, delete-orphan")
    alarms = relationship("Alarm", back_populates="machine", cascade="all, delete-orphan")
    tool_changes = relationship("ToolChange", back_populates="machine", cascade="all, delete-orphan")
    cycle_events = relationship("CycleEvent", back_populates="machine", cascade="all, delete-orphan")


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(
        String,
        ForeignKey("machines.machine_id"),
        nullable=False,
        index=True
    )

    timestamp = Column(DateTime)
    status = Column(String)
    state = Column(String)
    program_id = Column(String)
    tool_id = Column(Integer)
    cycle_id = Column(String)
    cycle_active = Column(Boolean)
    current_cycle_time = Column(Float)
    cycle_time_target = Column(Float)
    part_count = Column(Integer)
    spindle_rpm = Column(Float)
    feed_rate = Column(Float)
    axis_x = Column(Float)
    axis_y = Column(Float)
    axis_z = Column(Float)
    spindle_load = Column(Float)
    x_load = Column(Float)
    y_load = Column(Float)
    z_load = Column(Float)
    spindle_temp = Column(Float)
    motor_temp = Column(Float)
    tool_wear = Column(Float)
    feed_override = Column(Float)
    spindle_override = Column(Float)

    machine = relationship("Machine", back_populates="telemetry")


class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(
        String,
        ForeignKey("machines.machine_id"),
        nullable=False,
        index=True
    )

    timestamp = Column(DateTime)
    alarm_code = Column(String)
    message = Column(String)
    severity = Column(String)
    status = Column(String)
    active = Column(Boolean)

    machine = relationship("Machine", back_populates="alarms")


class ToolChange(Base):
    __tablename__ = "tool_changes"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(
        String,
        ForeignKey("machines.machine_id"),
        nullable=False,
        index=True
    )

    timestamp = Column(DateTime)
    tool_id = Column(Integer)
    previous_tool_id = Column(Integer)
    tool_offset = Column(Float)
    tool_wear = Column(Float)
    reason = Column(String)

    machine = relationship("Machine", back_populates="tool_changes")


class CycleEvent(Base):
    __tablename__ = "cycle_events"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(
        String,
        ForeignKey("machines.machine_id"),
        nullable=False,
        index=True
    )

    timestamp = Column(DateTime)
    event = Column(String)
    cycle_id = Column(String)
    program_id = Column(String)
    tool_id = Column(Integer)
    cycle_time_sec = Column(Float)
    part_number = Column(Integer)

    machine = relationship("Machine", back_populates="cycle_events")
