from mqtt.machine_state import machine_states
from backend.schemas.machine_schema import MachineResponse


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