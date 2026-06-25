from typing import List

from fastapi import APIRouter, HTTPException

from backend.schemas.machine_schema import MachineResponse
from backend.services.machine_service import (
    get_all_machines,
    get_machine_by_id,
    get_machine_state,
    get_machine_alarm,
    get_machine_tool,
    get_machine_cycle_event,
    machine_exists
)

router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)


@router.get("/", response_model=List[MachineResponse])
def get_machines():
    return get_all_machines()


@router.get("/{machine_id}", response_model=MachineResponse)
def get_machine(machine_id: str):

    machine =  get_machine_by_id(machine_id)

    if not machine_exists(machine_id):
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return machine


@router.get("/{machine_id}/state")
def get_state(machine_id: str):

    if not machine_exists(machine_id):
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return get_machine_state(machine_id)


@router.get("/{machine_id}/alarm")
def get_alarm(machine_id: str):

    if not machine_exists(machine_id):
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return get_machine_alarm(machine_id)

@router.get("/{machine_id}/tool")
def get_tool(machine_id: str):

    if not machine_exists(machine_id):
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return get_machine_tool(machine_id)


@router.get("/{machine_id}/cycle")
def get_cycle(machine_id: str):

    if not machine_exists(machine_id):
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return get_machine_cycle_event(machine_id)