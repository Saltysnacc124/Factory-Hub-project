from typing import Optional
from pydantic import BaseModel


class AxisPosition(BaseModel):
    x: float
    y: float
    z: float


class LoadData(BaseModel):
    spindle: float
    x_axis: float
    y_axis: float
    z_axis: float


class TemperatureData(BaseModel):
    spindle: float
    motor: float


class OverrideData(BaseModel):
    feed_override: int
    spindle_override: int


class Telemetry(BaseModel):

    status: str
    state: str

    program_id: Optional[str] = None
    tool_id: Optional[int] = None
    cycle_id: Optional[str] = None

    cycle_active: bool

    current_cycle_time: float
    cycle_time_target: float

    part_count: int

    spindle_rpm: float
    feed_rate: float

    axis_position: AxisPosition

    load: LoadData

    temperature: TemperatureData

    tool_wear: float

    override: OverrideData


class Alarm(BaseModel):

    alarm_code: str

    message: str

    severity: str

    status: str

    active: bool


class ToolChange(BaseModel):

    tool_id: int

    previous_tool_id: int

    tool_offset: float

    tool_wear: float

    reason: str


class CycleEvent(BaseModel):

    event: str

    cycle_id: str

    program_id: str

    tool_id: int

    cycle_time_sec: float

    part_number: int


class MachineResponse(BaseModel):

    machine_id: str

    current_state: Optional[Telemetry] = None

    active_alarm: Optional[Alarm] = None

    current_tool: Optional[ToolChange] = None

    last_cycle_event: Optional[CycleEvent] = None

    last_update: Optional[str] = None


from datetime import datetime


class TelemetryHistoryPoint(BaseModel):
    timestamp: datetime
    spindle_temp: float
    motor_temp: float
    spindle_rpm: float
    feed_rate: float
    tool_wear: float   