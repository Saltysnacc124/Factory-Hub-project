from backend.repositories.machine_repository import (
    save_telemetry,
    save_alarm,
    save_tool_change,
    save_cycle_event
)

from backend.schemas.machine_schema import (
    Telemetry,
    Alarm,
    ToolChange,
    CycleEvent
)

from mqtt.machine_state import (
    update_machine_state,
    update_alarm,
    update_tool,
    update_cycle_event,
    update_time
)

def process_telemetry(machine_id: str, timestamp: str, data: Telemetry):

    update_machine_state(
        machine_id,
        data.model_dump()
    )

    update_time(
        machine_id,
        timestamp
    )

    save_telemetry(
        machine_id,
        timestamp,
        data
    )

    print(
        f"\n[PROCESS] Telemetry | "
        f"Program = {data.program_id} "
        f"| Tool = {data.tool_id} "
        f"| Status = {data.status}"
    )

    return data


def process_alarm(machine_id: str, timestamp: str, data: Alarm):

    update_alarm(
        machine_id,
        data.model_dump()
    )

    update_time(
        machine_id,
        timestamp
    )

    save_alarm(
        machine_id,
        timestamp,
        data
    )

    print(
        f"\n[PROCESS] Alarm | "
        f"Code = {data.alarm_code} "
        f"| Severity = {data.severity} "
    )

    return data


def process_tool_change(machine_id: str, timestamp: str, data: ToolChange):

    update_tool(
        machine_id,
        data.model_dump()
    )

    update_time(
        machine_id,
        timestamp
    )

    save_tool_change(
        machine_id,
        timestamp,
        data
    )

    print(
        f"\n[PROCESS] Tool Change | "
        f"{data.previous_tool_id} -> {data.tool_id}"
    )

    return data


def process_cycle_event(machine_id: str, timestamp: str, data: CycleEvent):

    update_cycle_event(
        machine_id,
        data.model_dump()
    )

    update_time(
        machine_id,
        timestamp
    )

    save_cycle_event(
        machine_id,
        timestamp,
        data
    )
    
    print(
        f"\n[PROCESS] Cycle Event | "
        f"{data.event}"
    )

    return data