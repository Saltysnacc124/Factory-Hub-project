from backend.schemas.machine_schema import (
    Telemetry,
    Alarm,
    ToolChange,
    CycleEvent
)

from backend.services.ingestion_service import (
    process_telemetry,
    process_alarm,
    process_tool_change,
    process_cycle_event
)

def handle_telemetry(data):
    
    machine_id = data["machine_id"]
    timestamp = data["timestamp"]

    payload = data.copy()

    payload.pop("message_type", None)
    payload.pop("machine_id", None)
    payload.pop("timestamp", None)

    telemetry = Telemetry(**payload)

    process_telemetry(
        machine_id,
        timestamp,
        telemetry
    )
    
    print("\n[TELEMETRY]")
    print(data)

def handle_alarm(data):

    machine_id = data["machine_id"]
    timestamp = data["timestamp"]

    payload = data.copy()

    payload.pop("message_type", None)
    payload.pop("machine_id", None)
    payload.pop("timestamp", None)

    alarm = Alarm(**payload)

    process_alarm(
        machine_id,
        timestamp,
        alarm
    )
       
    print("\n[ALARM]")
    print(data)

def handle_cycle_event(data):

    machine_id = data["machine_id"]
    timestamp = data["timestamp"]

    payload = data.copy()

    payload.pop("message_type", None)
    payload.pop("machine_id", None)
    payload.pop("timestamp", None)

    cycle_event = CycleEvent(**payload)

    process_cycle_event(
        machine_id,
        timestamp,
        cycle_event
    )

    print("\n[CYCLE EVENT]")
    print(data)

def handle_tool_change(data):

    machine_id = data["machine_id"]
    timestamp = data["timestamp"]

    payload = data.copy()

    payload.pop("message_type", None)
    payload.pop("machine_id", None)
    payload.pop("timestamp", None)

    tool_change = ToolChange(**payload)

    process_tool_change(
        machine_id,
        timestamp,
        tool_change
    )

    print("\n[TOOL CHANGE]")
    print(data)