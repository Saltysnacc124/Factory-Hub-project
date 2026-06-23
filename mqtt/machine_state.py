

machine_states = {}

def initialize_machine(machine_id):
    if machine_id not in machine_states:
        machine_states[machine_id] = {
            "current_state": {},
            "active_alarm": None,
            "current_tool": None,
            "last_cycle_event": None,
            "last_update": None,
        }


def update_machine_state(machine_id, data):

    initialize_machine(machine_id)
    machine_states[machine_id]["current_state"].update(data)


def update_alarm(machine_id, alarm_data):
    initialize_machine(machine_id)
    machine_states[machine_id]["active_alarm"] = alarm_data


def update_cycle_event(machine_id, event_data):
    initialize_machine(machine_id)
    machine_states[machine_id]["last_cycle_event"] = event_data


def update_tool(machine_id, tool_id):
    initialize_machine(machine_id)
    machine_states[machine_id]["current_tool"] = tool_id


def update_time(machine_id, time_data):
    machine_states[machine_id]["last_update"] = time_data


def get_machine_state(machine_id):
    return machine_states.get(machine_id)


def print_machine_states():
    print(machine_states)