from mqtt.machine_state import machine_states
from backend.schemas.machine_schema import MachineResponse


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