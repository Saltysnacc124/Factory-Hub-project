from backend.repositories.machine_repository import (
    get_all_machines as repo_get_all_machines,
    get_machine_by_id as repo_get_machine_by_id
)


def get_all_machines():
    return repo_get_all_machines()

def get_machine_by_id(machine_id: str):
    return repo_get_machine_by_id(machine_id)