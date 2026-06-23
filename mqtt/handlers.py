from machine_state import (
    update_machine_state,
    update_alarm,
    update_tool,
    update_cycle_event,
    update_time
)

def handle_telemetry(data):
    
    machine_id = data["machine_id"]
    time_data = data["timestamp"]

    state_data = data.copy()

    state_data.pop("message_type", None)
    state_data.pop("machine_id", None)
    state_data.pop("timestamp", None)

    update_machine_state(machine_id, state_data)
    update_time(machine_id, time_data)
    
    print("\n[TELEMETRY]")
    print(data)

def handle_alarm(data):

    machine_id = data["machine_id"]
    time_data = data["timestamp"]

    state_data = data.copy()

    state_data.pop("message_type", None)
    state_data.pop("machine_id", None)
    state_data.pop("timestamp", None)

    update_alarm(machine_id, state_data)
    update_time(machine_id, time_data)
       
    print("\n[ALARM]")
    print(data)

def handle_cycle_event(data):

    machine_id = data["machine_id"]
    time_data = data["timestamp"]

    state_data = data.copy()

    state_data.pop("message_type", None)
    state_data.pop("machine_id", None)
    state_data.pop("timestamp", None)

    update_cycle_event(machine_id, state_data)
    update_time(machine_id, time_data)

    print("\n[CYCLE EVENT]")
    print(data)

def handle_tool_change(data):

    machine_id = data["machine_id"]
    time_data = data["timestamp"]

    state_data = data.copy()

    state_data.pop("message_type", None)
    state_data.pop("machine_id", None)
    state_data.pop("timestamp", None)

    update_tool(machine_id, state_data)
    update_time(machine_id, time_data)

    print("\n[TOOL CHANGE]")
    print(data)