from typing import List

from fastapi import APIRouter, HTTPException

from backend.schemas.machine_schema import MachineResponse
from backend.services.machine_service import (
    get_all_machines,
    get_machine_by_id
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

    if machine is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Machine {machine_id} not found"
        )

    return machine