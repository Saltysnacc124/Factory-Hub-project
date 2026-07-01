from mqtt.machine_state import machine_states

from backend.schemas.machine_schema import (
    MachineResponse,
    Telemetry,
    Alarm,
    ToolChange,
    CycleEvent
)

from database.db import SessionLocal
from database import crud

from datetime import datetime


def machine_exists(machine_id: str):
    return machine_id in machine_states


def get_all_machines():

    machines = []

    for machine_id, data in machine_states.items():

        machines.append(
            MachineResponse(
                machine_id=machine_id,
                current_state=data["current_state"],
                active_alarm=data["active_alarm"],
                current_tool=data["current_tool"],
                last_cycle_event=data["last_cycle_event"],
                last_update=data["last_update"]
            )
        )

    return machines


def get_machine_by_id(machine_id: str):

    data = machine_states.get(machine_id)

    if data is None:
        return None

    return MachineResponse(
        machine_id = machine_id,
        current_state = data["current_state"],
        active_alarm = data["active_alarm"],
        current_tool = data["current_tool"],
        last_cycle_event = data["last_cycle_event"],
        last_update = data["last_update"]
    )


def get_machine_state(machine_id: str):

    data = machine_states.get(machine_id)

    if data is None:
        return None

    return data["current_state"]


def get_machine_alarm(machine_id: str):

    data = machine_states.get(machine_id)

    if data is None:
        return None
    
    return data["active_alarm"]


def get_machine_tool(machine_id: str):

    data = machine_states.get(machine_id)

    if data is None:
        return None
    
    return data["current_tool"]


def get_machine_cycle_event(machine_id: str):

    data = machine_states.get(machine_id)

    if data is None:
        return None
    
    return data["last_cycle_event"]


def save_telemetry( machine_id: str, timestamp: str, telemetry: Telemetry):
    
    db = SessionLocal()

    try:
        parsed_timestamp = datetime.fromisoformat(timestamp)

        telemetry_data = {
            "machine_id": machine_id,
            "timestamp": parsed_timestamp,

            "status": telemetry.status,
            "state": telemetry.state,

            "program_id": telemetry.program_id,
            "tool_id": telemetry.tool_id,
            "cycle_id": telemetry.cycle_id,

            "cycle_active": telemetry.cycle_active,

            "current_cycle_time": telemetry.current_cycle_time,
            "cycle_time_target": telemetry.cycle_time_target,

            "part_count": telemetry.part_count,

            "spindle_rpm": telemetry.spindle_rpm,
            "feed_rate": telemetry.feed_rate,

            "axis_x": telemetry.axis_position.x,
            "axis_y": telemetry.axis_position.y,
            "axis_z": telemetry.axis_position.z,

            "spindle_load": telemetry.load.spindle,
            "x_load": telemetry.load.x_axis,
            "y_load": telemetry.load.y_axis,
            "z_load": telemetry.load.z_axis,

            "spindle_temp": telemetry.temperature.spindle,
            "motor_temp": telemetry.temperature.motor,

            "tool_wear": telemetry.tool_wear,

            "feed_override": telemetry.override.feed_override,
            "spindle_override": telemetry.override.spindle_override,
        }

        crud.insert_telemetry(
            db,
            **telemetry_data
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def save_alarm( machine_id: str, timestamp: str, alarm: Alarm):
    
    db = SessionLocal()

    try:
        parsed_timestamp = datetime.fromisoformat(timestamp)

        alarm_data = {
            "machine_id": machine_id,
            "timestamp": parsed_timestamp,

            "alarm_code": alarm.alarm_code,
            "message": alarm.message,
            "severity": alarm.severity,
            "status": alarm.status,
            "active": alarm.active
        }

        crud.insert_alarm(
            db,
            **alarm_data
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def save_tool_change( machine_id: str, timestamp: str, tool_change: ToolChange):
    
    db = SessionLocal()

    try:
        parsed_timestamp = datetime.fromisoformat(timestamp)

        tool_change_data = {
            "machine_id": machine_id,
            "timestamp": parsed_timestamp,

            "tool_id": tool_change.tool_id,
            "previous_tool_id": tool_change.previous_tool_id,
            "tool_offset": tool_change.tool_offset,
            "tool_wear": tool_change.tool_wear,
            "reason": tool_change.reason
        }

        crud.insert_tool_change(
            db,
            **tool_change_data
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def save_cycle_event( machine_id: str, timestamp: str, cycle_event: CycleEvent):
    
    db = SessionLocal()

    try:
        parsed_timestamp = datetime.fromisoformat(timestamp)

        cycle_event_data = {
            "machine_id": machine_id,
            "timestamp": parsed_timestamp,

            "event": cycle_event.event,
            "cycle_id": cycle_event.cycle_id,
            "program_id": cycle_event.program_id,
            "tool_id": cycle_event.tool_id,
            "cycle_time_sec": cycle_event.cycle_time_sec,
            "part_number": cycle_event.part_number
        }

        crud.insert_cycle_event(
            db,
            **cycle_event_data
        )

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()