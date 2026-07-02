from backend.repositories.machine_repository import (
    get_all_machines as repo_get_all_machines,
    get_machine_by_id as repo_get_machine_by_id,
    get_machine_state as repo_get_machine_state,
    get_machine_alarm as repo_get_machine_alarm,
    get_machine_tool as repo_get_machine_tool,
    get_machine_cycle_event as repo_get_machine_cycle_event,
    machine_exists as repo_machine_exists,
    get_machine_history as repo_get_machine_history
    
)

def get_machine_history(
    machine_id: str,
    limit: int = 100
):
    return repo_get_machine_history(
        machine_id,
        limit
    )

def get_all_machines():
    return repo_get_all_machines()

def get_machine_by_id(machine_id: str):
    return repo_get_machine_by_id(machine_id)

def get_machine_state(machine_id: str):
    return repo_get_machine_state(machine_id)

def get_machine_alarm(machine_id: str):
    return repo_get_machine_alarm(machine_id)

def get_machine_tool(machine_id: str):
    return repo_get_machine_tool(machine_id)

def get_machine_cycle_event(machine_id: str):
    return repo_get_machine_cycle_event(machine_id)

def machine_exists(machine_id: str):
    return repo_machine_exists(machine_id)